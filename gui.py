import kivy
import requests
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.button import Button


class MyGrid(Widget):
    odstranene = False
    pozicia = 0
    def pridat_do_sidebaru(self):
        chem_input = ObjectProperty(None)
        sidebar = ObjectProperty(None)
        sidebar_label = ObjectProperty(None)
        chem_name = self.chem_input.text.strip()
        if chem_name:
            if not self.odstranene:
                self.sidebar.remove_widget(self.sidebar_label)
                self.odstranene += True
            response = requests.get("http://127.0.0.1:5000/chemical")
            data = response.json()
            for prvok in data["Chemicals..."]:
                if prvok["name"] == chem_name:
                    idcko = prvok['id']
                    new_button = DraggableButton(text=f"{idcko} \n{chem_name}", size_hint_y=None, size_hint_x=0.5, height=60)
                    new_button.pos = (self.sidebar.width/2 - self.sidebar.width/4, self.pozicia)
                    new_button.custom_id = idcko
                    new_button.pozicia_x, new_button.pozicia_y = new_button.pos
                    self.sidebar.add_widget(new_button)
                    self.chem_input.text = ""
                    self.pozicia += 62
                    if self.pozicia == 930:
                        self.pozicia = 0
                    self.chem_input.hint_text = " "
                    break
                else:
                    self.chem_input.text = ""
                    self.chem_input.hint_text = "tento prvok \n nie je v databáze"
        else:
            self.chem_input.hint_text = "zadajte vzorec"


class DraggableButton(Button):
   def on_touch_down(self, touch):
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
           response = requests.get("http://127.0.0.1:5000/reaction")
           data = response.json()
           for reaction in data["Reactions..."]:
               api_id = [reaction["reactant_one_id"], reaction["reactant_two_id"]]
               if sorted(api_id) == sorted(moje_id):
                   print("našiel sa match")
                   parent_layout = self.parent
                   pozicia_xx, pozicia_yy = self.pos
                   parent_layout.remove_widget(self)
                   parent_layout.remove_widget(other_button)
                   reakcia = DraggableButton(text=reaction["name"], size_hint_y=None, size_hint_x=0.5, height=60)
                   reakcia.pos = (pozicia_xx - 5, pozicia_yy + 5)
                   parent_layout.add_widget(reakcia)
                   match += True
                   break
           if not match:
               print("nie je match")
               self.pos = (self.pozicia_x, self.pozicia_y)
               other_button.pos = (other_button.pozicia_x, other_button.pozicia_y)


       except AttributeError:
           print("tento objekt nemá id")

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()