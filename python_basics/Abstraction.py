from abc import ABC, abstractmethod


class Animal(ABC):
    @staticmethod
    @abstractmethod
    def make_sound():
        pass


class Lion(Animal):
    def make_sound():
        print("Roar")


l1 = Lion()

print(l1.make_sound())
