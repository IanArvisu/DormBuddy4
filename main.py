from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.font_definitions import theme_font_styles
from kivy.uix.image import Image
from kivymd.uix.behaviors.backgroundcolor_behavior import BackgroundColorBehavior
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.window import Window
from kivy.properties import StringProperty
Window.size = (350, 600)

class TodoCard(CommonElevationBehavior, MDFloatLayout):
    title = StringProperty()
    description = StringProperty()
class DormBuddy(MDApp):

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("task_main.kv"))
        screen_manager.add_widget(Builder.load_file("task_add.kv"))
        screen_manager.add_widget(Builder.load_file("recipe_main.kv"))
        return screen_manager

    def add_task(self, title, description):
        screen_manager.get_screen("task_main").todo_list.add_widget(TodoCard(title=title, description=description))

    def on_complete(self, checkbox, value, description):
        if value:
            todo_card = checkbox.parent  # Access the parent, which is the TodoCard instance
            screen_manager.get_screen("task_main").todo_list.remove_widget(todo_card)

if __name__ == "__main__":
    DormBuddy().run()