import os
import shutil


class PathUtils:
    PROJECT_NAME = 'ExchangeRatioTrader'
    FOLDER_PATH = os.makedirs('../../../imgs', exist_ok=True)

    @classmethod
    def project_path(cls):
        cur_dir = os.path.abspath(os.curdir)
        prefix, suffix = cur_dir.split(cls.PROJECT_NAME)
        return prefix + cls.PROJECT_NAME

    @classmethod
    def ui_path(cls, path: str):
        path = cls.project_path() + '/ui' + f'/{path}'
        return path

    @classmethod
    def folder_make_path(cls):
        path = cls.FOLDER_PATH
        return path

    @classmethod
    def img_save_path(cls, name: str, path: str):
        cls.img_save = shutil.move(f'{name}', cls.project_path() + f'\\{path}')
        path = cls.img_save
        return path

    @classmethod
    def img_read_path(cls, path: str):
        pass
