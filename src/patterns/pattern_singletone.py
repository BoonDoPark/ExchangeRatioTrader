#! -*- coding:utf-8 -*-


class SingletonInstance:
    __instance = None
    __tmp_method = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.__tmp_method = cls.instance
        cls.instance = cls.__getInstance
        return cls.__instance

    @classmethod
    def clearInstance(cls):
        """
        새로운 싱글톤 인스턴스 생성
        :return:
        """
        if cls.__instance:
            # initialize new instance.
            obj = cls.__new__(cls)
            # call __init__() method.
            obj.__init__()
            cls.__instance = obj

    @classmethod
    def removeInstance(cls):
        """
        싱글톤 인스턴스 제거
        :return:
        """
        if cls.__instance:
            cls.__instance = None
            cls.instance = cls.__tmp_method
