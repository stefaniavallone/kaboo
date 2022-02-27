import os
import sys
import traceback

root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.path.insert(0, os.path.join(root_dir, "utils"))

from base_app import BaseApp
from utils.setup.env import setup_env


if __name__ == "__main__":
    setup_env()

    try:
        BaseApp().run()
    except Exception as e:
        error = traceback.format_exc()
        print(error)
