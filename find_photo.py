from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import os

class ImageViewerApp(App):
    def build(self):
        self.layout = GridLayout(cols=1)

        
        self.text_input = TextInput(hint_text="Enter image file name (e.g., image.jpg)", size_hint=(1,0.1))
        self.layout.add_widget(self.text_input)

        
        self.button = Button(text="Open Image", size_hint=(1, 0.1))
        self.button.bind(on_press=self.open_image)
        self.layout.add_widget(self.button)

        self.error_label = Label(size_hint=(1, 0.1)) 
        self.layout.add_widget(self.error_label)

        self.image = Image(size_hint=(1, 0.7))
        self.layout.add_widget(self.image)

        return self.layout

    def open_image(self, instance):
        file_name = self.text_input.text.strip() 
        if file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
            if os.path.exists(file_name): 
                self.image.source = file_name  
                self.error_label.text = ""  
            else:
                self.error_label.text = "File not found!!!!!" 
        else:
            self.error_label.text = 'Please enter a valid .jpg or .jpeg file!!!!'
if __name__ == "__main__":
    imageapp=ImageViewerApp()
    imageapp.run()
    
#sample input (vijay.jpeg)
#sample input (harish.jpg)
