from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import numpy as np

Builder.load_file("interface.kv")

class MyLayout(BoxLayout):
    def calculate(self):
        try:
            val1 = float(self.ids.input1.text.strip())
            val2 = float(self.ids.input2.text.strip())
            arr = np.array([val1, val2])
            result_sum = np.sum(arr)
            result_product = np.prod(arr)
            self.ids.result.text = f"Array: {arr}\nSum: {result_sum}, Product: {result_product}"
        except:
            self.ids.result.text = "Invalid input. Enter valid numbers."

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
