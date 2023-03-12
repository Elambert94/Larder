from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self._app_window = GridLayout()
        self._app_window._cols = 1
        self._app_window.size_hint = (0.6, 0.7)
        self._app_window.pos_hint = {"center_x": 0.5, "center_y" : 0.5}
        #add widgets to window

        #text widget
        self.greeting = Label(text="Hello World")
        self._app_window.add_widget(self.greeting)
        self.greeting.pos_hint = {"center_x": 0.5, "center_y" : 0.5}

        return self._app_window

if __name__ == "__main__":
    SayHello().run()