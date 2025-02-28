import kivy
import requests
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.app import App


class MyGrid(Widget):
    def stlacenie(self):
        nieco = ObjectProperty(None)
        url = "http://127.0.0.1:5000/reaction"  # Adresa Flask API
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.nieco.text = str(data)

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()