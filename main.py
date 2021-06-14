from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.uix.picker import MDTimePicker
from datetime import datetime
from kivymd.uix.picker import MDDatePicker


KV = '''
BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: "MDFileManager"
        left_action_items: [['menu', lambda x: None]]
        elevation: 10

    FloatLayout:

        MDRoundFlatIconButton:
            text: "Open manager"
            icon: "folder"
            pos_hint: {'center_x': .5, 'center_y': .6}
            on_release: app.file_manager_open()
            
    MDRaisedButton:
        text: "Open time picker"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_time_picker()
    
    MDToolbar:
        title: "MDDatePicker"
        pos_hint: {"top": 1}
        elevation: 10

    MDRaisedButton:
        text: "Open time picker"
        color: "red"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_date_picker()
'''


class Example(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )

    def build(self):
        return Builder.load_string(KV)

    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def build(self):
        return Builder.load_string(KV)

    def show_time_picker(self):
        # Must be a datetime object
        previous_time = datetime.strptime("04:20:00", '%H:%M:%S').time()
        time_dialog = MDTimePicker()
        time_dialog.set_time(previous_time)
        time_dialog.open()

    def build(self):
        return Builder.load_string(KV)

    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''

        print(instance, value, date_range)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()



    def build(self):
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(
            '''
BoxLayout:
    orientation:'vertical'

    MDBottomNavigation:
        panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Файлы'
            icon: 'folder-multiple'

            MDRoundFlatIconButton:
                text: "Открыть файловый менеджер"
                icon: "folder"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.file_manager_open()

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Часы'
            icon: 'clock'

            MDRoundFlatIconButton:
                text: "Открыть часы"
                icon: "clock"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.show_time_picker()

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Календарь'
            icon: 'calendar'

            MDRoundFlatIconButton:
                text: "Открыть календарь"
                icon: "calendar"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.show_date_picker()
'''
        )



Example().run()

