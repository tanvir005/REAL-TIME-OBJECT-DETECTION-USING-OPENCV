from kivy.app import App
from kivy.uix.widget import Widget


class objectDetec(Widget):
    pass


class objectDetection(App):
    def build(self):

        return objectDetec()

objectDetection().run()