import json
strings = json.loads(open("strings.json", "r").read())

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Global Hello World")
        self.set_default_size(300, 250)

        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.box = Gtk.Box(spacing=1, orientation=1)
        scrolledwindow.add(self.box)

        for lang in strings:
            self.label = Gtk.Label(label=lang['country']+": "+lang['string'])
            self.box.pack_start(self.label, True, True, 0)
        self.add(scrolledwindow)


    def on_button_clicked(self, widget):
        print("Hello World")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
