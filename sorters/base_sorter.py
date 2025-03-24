from ..datasets import Page
from abc import ABC, abstractmethod


class BaseSorter(ABC):
    @abstractmethod
    def sort(page: Page):
        pass
    

