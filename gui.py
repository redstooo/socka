import kivy
import requests
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.app import App


class MyGrid(Widget):
    def stlacenie(self):
        chem1 = ObjectProperty(None)
        chem2 = ObjectProperty(None)
        ukazovanie = ObjectProperty(None)
        ukazovanie2 = ObjectProperty(None)
        url = "http://127.0.0.1:5000/reaction"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.ukazovanie.text = str(data)
            self.ukazovanie2.text = str(data)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()