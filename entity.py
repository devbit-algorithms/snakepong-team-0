from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    @abstractmethod
    def render(self, field):
        pass

class EntitySymbol:
    def __init__(self, entity, char, color = 0):
        self.entity = entity
        self.char = char
        self.color = color

    def __str__(self):
        return self.char

    def get_entity(self):
        return self.entity

    def get_color(self):
        return self.color