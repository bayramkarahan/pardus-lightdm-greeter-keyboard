import asyncio

def _klv_button_event(widget=None):
    #qrpopover.popup()
     os.system(get("screen-keyboard", "sh -c 'pkill e-keyboard;/usr/bin/e-keyboard login;'", "keyboard")+"&")
     loginwindow.o("ui_entry_password").grab_focus()
    #GLib.idle_add(qrkod_control_event)

def module_init():
    icon = Gtk.Image()
    icon.set_from_file("/usr/share/icons/hicolor/scalable/status/keyboard.svg")
    button = Gtk.Button(image=icon)
    button.get_style_context().add_class("icon")
    button.connect("clicked", _klv_button_event)
    loginwindow.o("ui_box_bottom_right").pack_start(button, False, True, 10)
    button.show_all()
