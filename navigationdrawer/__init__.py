# -*- coding: utf-8 -*-
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivymd.elevationbehavior import ElevationBehavior
from kivymd.icon_definitions import md_icons
from kivymd.list import ILeftBody
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivymd.label import MDLabel
from kivymd.list import OneLineIconListItem, ILeftBody, BaseListItem
from kivymd.slidingpanel import SlidingPanel
from kivymd.theming import ThemableBehavior

Builder.load_string('''
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import MDLabel kivymd.label
<NavDrawerToolbar@Image>
    canvas:
        Color:
            rgba: root.parent.theme_cls.divider_color
        Line:
            points: self.x, self.y, self.x+self.width,self.y

<NavigationDrawer>
    _list: list
    elevation: 0
    canvas:
        Color:
            rgba: root.theme_cls.bg_light
        Rectangle:
            size: root.size
            pos: root.pos
    BoxLayout:
        size_hint: (1, .4)
        Label:
            padding: 10, 10
            canvas.after:
                Color:
                    rgba: (1, 1, 1, 1)
                RoundedRectangle:
                    size: (self.size[1]-dp(14), self.size[1]-dp(14))
                    pos: (self.pos[0]+(self.size[0]-self.size[1])/2, self.pos[1]+dp(7))
                    source: root.image_source
                    radius: [self.size[1]-(self.size[1]/2)]

    ScrollView:
        do_scroll_x: False
        MDList:
            id: ml
            id: list

<NavigationDrawerIconButton>
    NDIconLabel:
        id: _icon
        font_style: 'Icon'
        theme_text_color: 'Secondary'
''')


class NavigationDrawer(SlidingPanel, ThemableBehavior, ElevationBehavior):
    title = StringProperty()
    image_source = StringProperty()
    _list = ObjectProperty()

    def add_widget(self, widget, index=0):
        if issubclass(widget.__class__, BaseListItem):
            self._list.add_widget(widget, index)
            widget.bind(on_release=lambda x: self.toggle())
        else:
            super(NavigationDrawer, self).add_widget(widget, index)

    def _get_main_animation(self, duration, t, x, is_closing):
        a = super(NavigationDrawer, self)._get_main_animation(duration, t, x,
                                                              is_closing)
        a &= Animation(elevation=0 if is_closing else 5, t=t, duration=duration)
        return a


class NDIconLabel(ILeftBody, MDLabel):
    pass


class NavigationDrawerIconButton(OneLineIconListItem):
    icon = StringProperty()

    def on_icon(self, instance, value):
        self.ids['_icon'].text = u"{}".format(md_icons[value])
