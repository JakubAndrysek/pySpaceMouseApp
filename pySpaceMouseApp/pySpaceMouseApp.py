import pySpaceMouse
from typing import Callable, Union, List, Dict


class Config:
    def __init__(self, config: Dict[str, pySpaceMouse.Config]):
        check_config(config)
        self.config = config


class App:
    def __init__(self, appConfig: Config):
        self.appConfig = appConfig

    def run(self):
        pass


def check_config(config):
    if type(config) is dict:
        for name, cfg in config.items():
            if type(name) is str:
                pass
            else:
                raise Exception(f"Some pySpaceMouse.Config key is not string")

            if isinstance(cfg, pySpaceMouse.Config):
                pass
            else:
                raise Exception(f"'pySpaceMouse.Config[{name}]' is not instance of 'pySpaceMouse.Config'")
    else:
        raise Exception("Input is not dict of 'str': 'pySpaceMouse.Config'")

    print("Checked successfully")
