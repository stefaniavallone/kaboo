import os
import platform
import sys
from kivy.core.window import Window
from kivy.logger import LOG_LEVELS, Logger
import kivy
from kivymd.uix.screen import MDScreen
from kivy.app import App


def go_to_screen(self, screen, direction="left"):
    self.manager.transition.direction = direction
    self.manager.current = screen


def setup_env():
    MDScreen.app = App.get_running_app
    MDScreen.go_to_screen = go_to_screen
    root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
    sys.path.insert(0, os.path.join(root_dir, "libs", "utils"))
    Logger.setLevel(LOG_LEVELS["debug"])

    # This is needed for supporting Windows 10 with OpenGL < v2.0
    if platform.system() == "Windows":
        from win32api import GetSystemMetrics  # pip install pywin32 
        
        app_size = (360, 740)
        Window.size = app_size
        Window.top = 50
        Window.left = GetSystemMetrics(0) - 50 - app_size[0] 
        os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

    if kivy.utils.platform == "android":
        from android.permissions import request_permissions, Permission
        
        request_permissions([Permission.READ_EXTERNAL_STORAGE,
                             Permission.WRITE_EXTERNAL_STORAGE])