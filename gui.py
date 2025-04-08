import kivy
import requests
from kivy.config import Config
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock
from kivy.uix.spinner import Spinner

response_react = requests.get("http://127.0.0.1:5000/reaction")
response_chem = requests.get("http://127.0.0.1:5000/chemical")

class MyGrid(Widget):
    odstranene = False
    pozicia = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.dropdown_menu, 0.25)
    def dropdown_menu(self, dt):
        data = response_chem.json()
        chemikalie = []
        horny_panel = self.ids.chem_input
        for chem in data["Chemicals..."]:
            chemikalie.append(chem["name"])
        self.chem_dropdown = Spinner(
            text="Chemikálie",
            values=chemikalie,
            size_hint_y=None,
            size_hint_x=0.195,
            height=150,
        )
        def pridanie(spinner, text):
            print(spinner, text)
            return self.pridat_do_sidebaru(self.chem_dropdown.text)
        self.chem_dropdown.bind(text=pridanie)
        horny_panel.add_widget(self.chem_dropdown, index=2)



    def pridat_do_sidebaru(self, chem_name):
        sidebar_label = ObjectProperty(None)
        grid = self.ids.sidebar
        if chem_name:
            if not self.odstranene:
                grid.remove_widget(self.sidebar_label)
                self.odstranene += True
            data = response_chem.json()
            for prvok in data["Chemicals..."]:
                if prvok["name"] == chem_name:
                    idcko = prvok['id']
                    new_button = DraggableButton(text=chem_name, size_hint_y=None, size_hint_x=0.5, height=60)
                    new_button.pos = (self.sidebar.width/2 - self.sidebar.width/4, self.pozicia)
                    new_button.custom_id = idcko
                    new_button.pozicia_x, new_button.pozicia_y = new_button.pos
                    grid.add_widget(new_button)
                    self.pozicia += 62
                    if self.pozicia == 930:
                        self.pozicia = 0
                    break



class DraggableButton(Button):

   def on_touch_down(self, touch):

      if touch.button == "right" and self.collide_point(*touch.pos):
            self.popup_screen()
      if self.collide_point(*touch.pos):
         touch.grab(self)
         return True
      return super().on_touch_down(touch)

   def on_touch_move(self, touch):
      if touch.grab_current == self:
         self.pos = (self.pos[0] + touch.dx, self.pos[1] + touch.dy)

   def on_touch_up(self, touch):
      if touch.grab_current == self:
         touch.ungrab(self)
         self.check_for_collisions()
         return True
      return super().on_touch_up(touch)

   def check_for_collisions(self):
       for other_button in self.parent.children:
           if isinstance(other_button, DraggableButton) and other_button != self:
               if self.is_collision(other_button):
                   self.check_for_reaction(other_button)

   def is_collision(self, other_button):
       x1, y1 = self.pos
       x2, y2 = other_button.pos
       width1, height1 = self.size
       width2, height2 = other_button.size

       if x1 < x2 + width2 and x1 + width1 > x2 and y1 < y2 + height2 and y1 + height1 > y2:
           return True
       return False

   def check_for_reaction(self, other_button):
       print("CHECKUJEM")
       match = False
       try:
           moje_id = [other_button.custom_id, self.custom_id]
           data = response_react.json()
           for reaction in data["Reactions..."]:
               api_id = [reaction["reactant_one_id"], reaction["reactant_two_id"]]
               if sorted(api_id) == sorted(moje_id):
                   print("našiel sa match")
                   parent_layout = self.parent
                   pozicia_xx, pozicia_yy = self.pos
                   parent_layout.remove_widget(self)
                   parent_layout.remove_widget(other_button)
                   reakcia = DraggableButton(text=f" {reaction['formula']} \n {reaction['name']}" , size_hint_y=None, size_hint_x=0.5, height=60)
                   reakcia.pos = (pozicia_xx - 5, pozicia_yy + 5)
                   smajli = reaction["smiles"].split(" ")
                   popi = reaction["desc"].split("., ")
                   reakcia.smajls = len(smajli)
                   reakcia.smajls_pole = smajli
                   try:
                       popi.remove("")
                   except ValueError:
                       print("ups chybička cca")
                   reakcia.desc = popi
                   reakcia.desc_len = len(popi)
                   parent_layout.add_widget(reakcia)
                   match += True
           if not match:
               print("nie je match")
               self.pos = (self.pozicia_x, self.pozicia_y)
               other_button.pos = (other_button.pozicia_x, other_button.pozicia_y)


       except AttributeError:
           print("tento objekt nemá id")


   def popup_screen(self):
       try:
           show = PopupOkno(smajls_pole=self.smajls_pole, smajls=self.smajls, desc=self.desc, desc_len=self.desc_len)
           show.pridavanie_obrazkov()
           show.pridavanie_desc()
           popup_window = Popup(title="popisok reakcie", content=show, size_hint=(None,None), size=(1000, 800))
           popup_window.open()
       except AttributeError:
           print("ešte nie je reakcia definovana")
class PopupOkno(GridLayout):
   pocet_koloniek = NumericProperty(1)
   pocet_koloniek_desc = NumericProperty(1)
   def __init__(self, smajls_pole, smajls, desc, desc_len, **kwargs):
       super().__init__(**kwargs)
       self.smajls_pole = smajls_pole
       self.pocet_koloniek = smajls
       self.popisok = desc
       self.pocet_koloniek_desc = desc_len



   def pridavanie_obrazkov(self):
          obrazky = self.ids.riadok_smiles
          for smajl in self.smajls_pole:
              if smajl == "":
                  continue
              image_smile = Image(source=f"smiles/{smajl}.jpg")
              obrazky.add_widget(image_smile)

   def pridavanie_desc(self):
       popisok = self.ids.riadok_popisok
       for des in self.popisok:
           popisok.add_widget(TextInput(text=des, multiline=True, readonly=True))


class MyApp(App):
    Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()