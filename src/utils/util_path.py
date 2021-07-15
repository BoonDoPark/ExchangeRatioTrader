import os


class PathUtils:
    PROJECT_PATH = os.getcwd()

    @classmethod
    def ui_path(cls, path: str):
        path = cls.PROJECT_PATH + f'\\{path}'
        return path
