'''
SignIn with Google+ using kivy.

Using KivyMD.
'''

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.uix.relativelayout import RelativeLayout
from kivymd.theming import ThemeManager
from navigationdrawer import NavigationDrawer


main_widget_kv = '''
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager

BoxLayout:
    orientation: 'vertical'
    Toolbar:
        id: toolbar
        title: 'Google+'
        background_color: app.theme_cls.primary_dark
        left_action_items: [['menu', lambda x: app.nav_drawer.toggle()]]
        right_action_items: [['more-vert', lambda x: app.nav_drawer.toggle()]]
    ScreenManager:
        id: scr_mngr
        Screen:
            name: 'Home'

<GPlusNavigate>:
    title: "NavigationDrawer"
    image_source: 'images/me.jpg'
    NavigationDrawerIconButton:
        icon: 'face'
        text: 'Kuldeep Singh'
    NavigationDrawerIconButton:
        icon: 'email'
        text: 'kuldeepbb.grewal@gmail.com'
        on_release: app.root.ids.scr_mngr.current = 'bottomsheet'
    NavigationDrawerIconButton:
        icon: 'phone'
        text: '+91-7727935906'
    NavigationDrawerIconButton:
        icon: 'cake'
        text: '26/11/1994'
    NavigationDrawerIconButton:
        icon: 'city-alt'
        text: 'Rohtak'
    NavigationDrawerIconButton:
        icon: 'settings'
        text: 'Settings'
'''


class GPlusNavigate(NavigationDrawer):
    pass


class GPlusApp(App):
    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    def build(self):
        main_widget = Builder.load_string(main_widget_kv)
        self.nav_drawer = GPlusNavigate()
        return main_widget

    def on_resume(self):
        return True

    def on_pause(self):
        pass


if __name__ == '__main__':
    app = GPlusApp()
    app.run()
