from abc import ABCMeta, abstractmethod


class FileContainer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def read(self):
        raise NotImplementedError()