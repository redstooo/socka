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
        url = f"http://127.0.0.1:5000/chemical/{self.chem1.text}"
        url2 = f"http://127.0.0.1:5000/chemical/{self.chem2.text}"
        response = requests.get(url)
        response2 = requests.get(url2)
        if response.status_code == 200 and response.status_code == 200:
            data = response.json()
            data2 = response2.json()
            self.ukazovanie.text = str(data)
            self.ukazovanie2.text = str(data2)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()