import abc

class IMigrate(abc.ABC):
    @abc.abstractmethod
    def onLoadCatalog(self):
        pass