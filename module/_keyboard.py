import asyncio
durum=0
def _klv_button_event(widget=None):
     #os.system(get("screen-keyboard", "sh -c 'pkill e-keyboard;/usr/bin/e-keyboard login;'", "keyboard")+"&")
     #loginwindow.o("ui_entry_password").grab_focus()
     global durum
     if durum==0:
         durum=1
         os.system(get("screen-keyboard", "sh -c 'pkill e-keyboard;/usr/bin/e-keyboard login;'", "keyboard")+"&")
     elif durum==1:
         durum=0
         os.system(get("screen-keyboard", "sh -c 'pkill e-keyboard;'", "keyboard")+"&")
     loginwindow.o("ui_entry_password").grab_focus()

def module_init():
    global durum
    icon = Gtk.Image()
    icon.set_from_file("/usr/share/icons/hicolor/scalable/status/keyboard.svg")
    button = Gtk.Button(image=icon)
    button.get_style_context().add_class("icon")
    button.connect("clicked", _klv_button_event)
    loginwindow.o("ui_box_bottom_right").pack_start(button, False, True, 10)
    button.show_all()
    #loginwindow.o("ui_entry_passwords").connect("focus-in-event",_klv_button_event)

