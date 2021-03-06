# -*- coding: utf-8 -*-
"""GTK Entry."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()
        self.set_title(title='GTK Entry')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        entry = Gtk.Entry.new()
        entry.set_icon_from_icon_name(
            icon_pos=Gtk.EntryIconPosition.PRIMARY,
            icon_name='system-search-symbolic')
        # Sinal é emitido quando o `Enter` é pressionando.
        entry.connect('activate', self.on_key_enter_pressed)
        # Sinal é emitido quando o ícone é pressionando.
        entry.connect('icon-press', self.on_icon_pressed)
        vbox.add(widget=entry)

    def on_key_enter_pressed(self, widget):
        print(widget.get_text())

    def on_icon_pressed(self, widget, icon, event):
        print(widget.get_text())


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
