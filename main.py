import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix. textinput import TextInput
from kivy.uix.button import Button


class BruhGrid(GridLayout):
    def __init__(self, **kwargs):
        super(BruhGrid, self).__init__()
        self.cols = 2
        self.add_widget(Label(text = "Please Enter Name: "))
        self.s_name = TextInput()
        self.add_widget(self.s_name)
        self.add_widget(Label(text = "Enter Age: "))
        self.s_age = TextInput()
        self.add_widget(self.s_age)
        self.add_widget(Label(text = "Gender"))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.press = Button(text = "Click Me")
        self.add_widget(self.press)
        self.press.bind(on_press = self.click_me)


    def click_me(self, instance):
        print("Your name is " + self.s_name.text +
              " and you are " + self.s_age.text + " years old."
              "I also know that you are a " + self.s_gender.text + "!!")

class BruhApp(App):
    def build(self):
        return BruhGrid()

if __name__ == "__main__":
    BruhApp().run()
