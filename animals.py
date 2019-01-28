# -*- coding: utf-8 -*-


class Animal(object):
    DOG = 'dog'
    CAT = 'cat'
    ALL_TYPES = [DOG, CAT]

    def __init__(self, name, the_type):
        super(Animal, self).__init__()
        if the_type not in self.ALL_TYPES:
            template = 'Cannot create an animal of type: `{type}`'
            raise ValueError(template.format(type=the_type))
        self.type = the_type

    def is_dog(self):
        return self.type == self.DOG

    def is_cat(self):
        return self.type == self.CAT

    @staticmethod
    def create_dog(name):
        return Animal(name, Animal.DOG)

    @staticmethod
    def create_cat(name):
        return Animal(name, Animal.CAT)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
