from pixellib.instance import instance_segmentation
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
Window.size = (450, 500)
Window.clearcolor = (60/255, 63/255, 65/255, 1)
photo = ""

def pr():
    def object_detection_on_an_image():
        segment_image = instance_segmentation()
        segment_image.load_model('fruits_360_model.h5')

        segment_image.segmentImage(
            image_path = photo,
            output_image_name="C:\\Users\\Ilya Blokhin\\Desktop\\result2.jpg",
            show_bboxes=True
        )
    def main():
        object_detection_on_an_image()


    main()

class Container(BoxLayout):

    def run(self):
        global photo
        photo = self.txt.text
        self.l1.text = "Операция выполнена успешно"
        pr()

class MyApp(App):
    def build(self):
        return Container()


if __name__ == "__main__":
    MyApp().run()
