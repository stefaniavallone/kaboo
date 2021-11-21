import os
import platform
import sys
from kivy.core.window import Window
from kivy.logger import LOG_LEVELS, Logger
#from android.permissions import request_permissions, Permission


def setup_env():
    root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
    sys.path.insert(0, os.path.join(root_dir, "libs", "utils"))
    Logger.setLevel(LOG_LEVELS["debug"])

    # This is needed for supporting Windows 10 with OpenGL < v2.0
    if platform.system() == "Windows":
        Window.size = (360, 740)
        os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

    # if kivy.utils.platform == "android":
    #     request_permissions([Permission.READ_EXTERNAL_STORAGE,
    #                          Permission.WRITE_EXTERNAL_STORAGE])