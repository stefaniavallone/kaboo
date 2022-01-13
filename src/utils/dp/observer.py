from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self, *args) -> None:
        pass


class ConcreteSubject(Subject):
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, property_name, previous_state, new_state) -> None:
        for observer in self._observers:
            observer.update(property_name, previous_state, new_state)


class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject, *args) -> None:
        pass
