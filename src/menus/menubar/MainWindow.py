# -*- coding: utf-8 -*-
"""Gtk MenuBar."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()
        self.set_title(title='Gtk MenuBar')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.add(widget=vbox)

        # Criando a barra de menu.
        menubar = Gtk.MenuBar.new()
        # Adicionando a barra de menu no box vertical que está na janela principal.
        vbox.pack_start(child=menubar, expand=False, fill=False, padding=0)

        menu_file = Gtk.Menu.new()
        menu_item_file = Gtk.MenuItem.new_with_label(label='Arquivo')
        menu_item_file.set_submenu(submenu=menu_file)
        menubar.add(widget=menu_item_file)

        item_new = Gtk.MenuItem.new_with_label(label='Novo')
        item_new.connect('activate', self.menu_item_clicked)
        menu_file.add(widget=item_new)

        menu_help = Gtk.Menu.new()
        menu_item_help = Gtk.MenuItem.new_with_label(label='Ajuda')
        menu_item_help.set_submenu(submenu=menu_help)
        menubar.add(widget=menu_item_help)

        item_about = Gtk.MenuItem.new_with_label(label='Sobre')
        item_about.connect('activate', self.about)
        menu_help.add(widget=item_about)

    def menu_item_clicked(self, widget):
        print(widget.get_label())

    def about(self, widget):
        about = Gtk.AboutDialog.new()
        about.set_authors(authors=['Renato Cruz'])
        about.set_comments(
            comments='Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                     'sed do eiusmod tempor incididunt ut labore et dolore '
                     'magna aliqua.'
        )
        about.set_website(website='https://github.com/natorsc/gui-python-gtk')
        about.run()
        about.destroy()


if __name__ == '__main__':
    win = MainWindow()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
