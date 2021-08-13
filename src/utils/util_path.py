import os
import shutil


class PathUtils:
    PROJECT_PATH = os.getcwd()
    FOLDER_PATH = os.makedirs('../../../imgs', exist_ok=True)

    @classmethod
    def ui_path(cls, path: str):
        path = cls.PROJECT_PATH + f'\\{path}'
        return path

    @classmethod
    def folder_make_path(cls):
        path = cls.FOLDER_PATH
        return path

    @classmethod
    def img_save_path(cls, name: str, path: str):
        cls.img_save = shutil.move(f'{name}', cls.PROJECT_PATH + f'\\{path}')
        path = cls.img_save
        return path

    @classmethod
    def img_read_path(cls, path: str):
        pass
