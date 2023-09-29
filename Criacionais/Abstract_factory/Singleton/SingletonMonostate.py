class SingletonMonostate(object):
    __shared_state = {"1": "2"}

    def __init__(self) -> None:
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


class Borg(object):
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj
