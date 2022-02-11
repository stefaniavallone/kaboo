from abc import ABC


class AbstractTrophy(ABC):

    def __init__(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image

    def check(self, games):
        raise NotImplementedError()

    def __repr__(self):
        return str(vars(self))