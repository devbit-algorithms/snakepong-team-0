from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def getx(self):
        return self.__x

    def gety(self):
        return self.__x
    
    @abstractmethod
    def render(self, field):
        pass