#/usr/bin/python3 

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def button_clicked(button):
    print('Hello World!')


def main():
    window = Gtk.Window()
    window.set_default_size(240, 180)
    window.set_title('Hello World!')
    window.connect('destroy', lambda w:
gtk.main_quit())
    button = Gtk.Button('Press Me')
    button.connect('clicked', button_clicked)
    button.show()

    window.add(button)
    window.present()

    Gtk.main()

if __name__ == '__main__':
    main()