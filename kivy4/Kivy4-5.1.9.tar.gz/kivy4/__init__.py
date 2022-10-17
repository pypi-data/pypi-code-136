import json
import darkdetect
import os
import pyperclip
import threading
import time
import sys
from kivy import Config
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDDatePicker, MDTimePicker

Config.set('graphics', 'resizable', 0)
Config.set('input', 'mouse', 'mouse, multitouch_on_demand')
Config.set('kivy', 'exit_on_escape', 0)
Config.write()

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.settings import ContentPanel
from kivy.properties import *
from kivymd.app import MDApp
from screeninfo import get_monitors

__version__ = '5.1.9'


class Content(BoxLayout):
    pass


def icons(search_value: str = ''):
    from kivymd.icon_definitions import md_icons
    print([icon for icon in list(md_icons.keys()) if search_value in icon])


def get_spec(name: str, icon: str = 'icon.ico', filename: str = 'main.py', path: str = os.getcwd()):
    path = path.replace("\\", r"\\")

    with open(filename.replace('.py', '.spec'), 'w') as f:
        f.write(fr"""from kivy_deps import sdl2, glew

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['{filename}'],
             pathex=['{path}'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={{}},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='{name}',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None, icon='{icon}')

coll = COLLECT(exe, Tree('{path}'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='{name}')""")


def thread(func):
    def inner(*args, **kwargs):
        threading.Thread(target=lambda: func(*args, **kwargs), daemon=True).start()

    return inner


def measure_time(func):
    def inner(*args, **kwargs):
        tic = time.perf_counter()
        func(*args, **kwargs)
        toc = time.perf_counter()

        print(f'Duration of {func.__name__}: {round(toc - tic, 8)}')

    return inner


@thread
def file_dialog(callback: callable):
    from tkinter import Tk, filedialog

    if sys.platform == "darwin":
        fd = os.popen("""osascript -e 'tell application (path to frontmost application as text)
set myFile to choose file
POSIX path of myFile
end'""")
        file_path = fd.read()
        fd.close()
        file_path = file_path[:-1]
    else:
        tk = Tk()
        tk.withdraw()
        file_path = filedialog.askopenfilename()

    if file_path:
        callback(file_path)


class Kivy4(MDApp):
    dark_mode_icon = StringProperty('')

    def __init__(self, string: str = '', app_name: str = '', dict_of_files: dict[str, str] = None,
                 list_of_dirs: list[str] = None,
                 screen_size=None, minimum=None, center: bool = True,
                 sun_icon: str = 'white-balance-sunny', moon_icon: str = 'weather-night',
                 main_color: str = 'Blue', icon: str = '', toolbar=False, app_data: bool = True,
                 disable_x: bool = False, pre_string: str = '', toolbar_name: str = None, **kwargs):

        super().__init__(**kwargs)

        if minimum is None:
            minimum = [0.1, 0.1]

        self.app_name = app_name
        self.builder_string = '''<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "100dp"'''

        if app_data:
            is_windows = sys.platform.startswith('win')
            app_data_path = os.getenv('APPDATA') + '/' + app_name if is_windows else app_name

            self.appdata_path = app_data_path
            self.create_files(dict_of_files)
            self.create_dirs(list_of_dirs)

            self.moon_icon = moon_icon
            self.sun_icon = sun_icon
            self.is_dark_mode()

        self.dialog = None
        self.set_properties(main_color, icon, toolbar, string, pre_string, toolbar_name)
        self.disable_x = disable_x

        screen = get_monitors()[0]
        self.width = screen.width
        self.height = screen.height

        self.screen_positions(screen_size, minimum, center)

    @property
    def ids(self):
        return self.root.ids

    def set_properties(self, main_color, icon, toolbar, string, pre_string, toolbar_name):

        for x in pre_string.split('\n'):
            if 'x,y=' in x.replace(' ', '') and '#' not in x:
                self.builder_string += '\n' + self.x_y(x)

            else:
                self.builder_string += '\n' + x

        self.builder_string += self.custom_classes()

        if toolbar:
            self.builder_string += self.get_toolbar(toolbar, toolbar_name)

            for x in string.split('\n'):
                if 'x,y=' in x.replace(' ', '') and '#' not in x:
                    self.builder_string += '\n            ' + self.x_y(x)

                else:
                    self.builder_string += '\n            ' + x

        self.theme_cls.primary_palette = main_color
        self.icon = icon

    def build(self):
        self.use_kivy_settings = False
        self.settings_cls = ContentPanel
        self.title = self.app_name

        Window.bind(on_dropfile=lambda *args: self.on_drop_file(*args),
                    on_request_close=lambda x: self.on_request_close(self.disable_x))

        self.pre_build()
        return Builder.load_string(self.builder_string)

    def pre_build(self):
        pass

    def screen_positions(self, screen_size, minimum=None, center=True):

        if minimum is None:
            minimum = [0.1, 0.1]

        min_x, min_y = minimum

        if screen_size is None:
            x, y = 0.6, 0.6

        else:
            x, y = screen_size[0], screen_size[1]

        if x <= 1 or y <= 1:
            Window.size = (self.width * x, self.height * y)
            Window.minimum_height = self.height * min_y
            Window.minimum_width = self.width * min_x

        else:
            Window.size = (x, y)
            Window.minimum_height = min_y
            Window.minimum_width = min_x

            if center:
                Window.left = (self.width - x) / 2
                Window.top = (self.height - y) / 2
                return

            else:
                return

        if center:
            Window.left = (self.width - (self.width * x)) / 2
            Window.top = (self.height - (self.height * y)) / 2

    def create_files(self, list_of_files):
        try:
            if not os.path.isdir(self.appdata_path):
                os.mkdir(self.appdata_path)

            if list_of_files:
                for file in list_of_files:
                    self.set_file(file, list_of_files[file])

        except Exception as e:
            return e

    def create_dirs(self, list_of_dirs):
        try:
            if list_of_dirs:
                for folder in list_of_dirs:
                    if not os.path.isdir(self.appdata_path + '/' + folder):
                        os.makedirs(self.appdata_path + '/' + folder)

        except Exception as e:
            return e

    def set_file(self, file, value, extension='.txt', is_json=False):
        if is_json:
            extension = '.json'

        path_to_create = f'{self.appdata_path}/{file}{extension}'
        if is_json:
            value = json.dumps(value, indent=4)

        with open(path_to_create, 'w') as f:
            f.write(value)

    def get_file(self, file, default=None, create_file_if_not_exist: str="", extension='.txt', is_json=False):
        if is_json:
            extension = '.json'
        path_of_file = f'{self.appdata_path}/{file}{extension}'

        try:
            with open(path_of_file, 'r') as f:
                value = f.read()

            if is_json:
                return json.loads(value)
            return value

        except FileNotFoundError:
            if create_file_if_not_exist:
                self.set_file(file, create_file_if_not_exist)

            return default

        except Exception as e:
            print(e)
            return default

    def is_dark_mode(self, filename='dark mode.txt'):
        try:
            with open(self.appdata_path + '/' + filename, 'r') as f:
                current_mode = f.read()
                self.set_dark_mode_icon(current_mode)

                return current_mode == 'Dark'

        except FileNotFoundError:
            with open(self.appdata_path + '/' + filename, 'w') as f:
                default = darkdetect.theme()
                f.write(default)

                self.set_dark_mode_icon(default)

                return default == 'Dark'

        except AttributeError:
            return False

    def on_theme_change(self, value):
        pass

    def set_dark_mode(self, value=None, filename='dark mode'):
        if value is None:
            value = darkdetect.theme()

        self.set_file(filename, value)
        self.set_dark_mode_icon(value)
        self.on_theme_change(value)

    def reverse_dark_mode(self, filename: str = 'dark mode.txt'):
        try:
            with open(self.appdata_path + '/' + filename, 'r') as f:
                current_mode = f.read()

                if current_mode == 'Dark':
                    self.set_dark_mode('Light')
                    return 'Light'

                self.set_dark_mode('Dark')
                return 'Dark'

        except FileNotFoundError:
            with open(self.appdata_path + '/' + filename, 'w') as f:
                default = darkdetect.theme()
                f.write(default)

                self.set_dark_mode_icon(default)

                return default

        except AttributeError:
            return False

    def set_dark_mode_icon(self, value):
        if value == 'Dark':
            self.dark_mode_icon = self.moon_icon

        else:
            self.dark_mode_icon = self.sun_icon

        self.theme_cls.theme_style = value

    def get_toolbar(self, properties: list, toolbar_name: str):
        if properties is True:
            right_icons, left_icons = '[[app.dark_mode_icon, lambda x: app.reverse_dark_mode()]]', '[]'

        elif len(properties) == 2:
            left_icons, right_icons, name = properties[0], properties[1], self.app_name

        else:
            left_icons, right_icons, name = properties

        if toolbar_name:
            name = toolbar_name

        else:
            name = self.app_name

        return f'''
Screen:
    MDTopAppBar:
        id: toolbar
        pos_hint: {{"top": 1}}
        elevation: 10
        title: "{name}"
        right_action_items: {right_icons}
        left_action_items: {left_icons}

    MDNavigationLayout:
        x: toolbar.height
        ScreenManager:
            id: screen_manager
'''

    @staticmethod
    def toast(text, duration=2.5):
        from kivymd.toast import toast

        toast(text=text, duration=duration)

    @staticmethod
    def snack(text, button_text=None, func=None):
        from kivymd.uix.button import MDFlatButton
        from kivymd.uix.snackbar import Snackbar

        snack = Snackbar(text=text)

        if func and button_text:
            snack.buttons = [MDFlatButton(text=f"[color=#1aaaba]{button_text}[/color]", on_release=func)]

        snack.open()

    @staticmethod
    def x_y(x_y):
        x, y = eval(x_y.split("=")[1])
        return f"{x_y.index('x') * ' '}pos_hint: {{'center_x': {x}, 'center_y': {y}}}"

    @staticmethod
    def custom_classes():
        return '''
<Text@MDLabel>:
    halign: 'center'

<Input@MDTextField>:
    mode: "rectangle"
    text: ""
    size_hint_x: 0.5

<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48)

<Btn@MDFillRoundFlatButton>:
    text: ""

<BtnIcon@MDFillRoundFlatIconButton>:
    text: ""

<Img@Image>:    
    allow_stretch: True

<CircleIcon@MDFloatingActionButton>:
    md_bg_color: app.theme_cls.primary_color
'''

    @staticmethod
    def on_drop_file(*args):
        print(*args)

    @staticmethod
    def on_request_close(disable_x: bool = False):
        return disable_x

    @staticmethod
    def write_to_clipboard(text: str):
        pyperclip.copy(text)

    def show_date_picker(self, on_save, mode='picker'):
        date_dialog = MDDatePicker(mode=mode)
        date_dialog.bind(on_save=on_save, on_cancel=self.on_cancel_picker)
        date_dialog.open()

    def show_time_picker(self, on_save):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=on_save, on_cancel=self.on_cancel_picker)
        time_dialog.open()

    def on_cancel_picker(self, instance, value):
        pass

    def popup_kivy4(self, title='My popup', content=Content(), cancel_text='CANCEL', okay_text='OKAY',
                    okay_func=lambda *args: print('yes'), cancel_func=None):

        if cancel_func is None:
            cancel_func = lambda *args: self.dismiss()

        if self.dialog:
            self.dismiss()

        buttons = []
        if cancel_text:
            buttons.append(MDFlatButton(
                    text=cancel_text,
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=cancel_func
                ))

        if okay_text:
            buttons.append(MDFlatButton(
                    text=okay_text,
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=okay_func
                ))

        self.dialog = MDDialog(
            title=title,
            type="custom",
            content_cls=content,
            buttons=buttons,
        )

        self.dialog.open()

    def dismiss(self):
        try:
            self.dialog.dismiss()
        except Exception as e:
            print(e)

    def get_files_content(self, path: str, is_json: bool = False):
        dir_path = self.appdata_path + '/' + path
        for file in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, file)):
                with open(os.path.join(dir_path, file), 'r') as f:
                    if is_json:
                        yield json.load(f)
                    else:
                        yield f.read()

    def delete_file(self, path):
        os.remove(self.appdata_path + '/' + path)
