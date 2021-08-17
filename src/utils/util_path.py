import os
import shutil


class PathUtils:
    PROJECT_NAME = 'ExchangeRatioTrader'
    # FOLDER_PATH = os.makedirs('../../../imgs', exist_ok=True)

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
    def folder_path(cls):
        return os.makedirs(f'{cls.project_path()}/imgs', exist_ok=True)

    @classmethod
    def img_path(cls, path: str):
        path = cls.project_path() + '/imgs' + f'/{path}'
        return path

