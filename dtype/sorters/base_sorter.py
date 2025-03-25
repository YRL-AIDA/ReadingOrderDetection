from ..page import Page
from ..bbox import BBox
from abc import ABC, abstractmethod


class BaseSorter(ABC):
    @abstractmethod
    def sort(self, page: Page):
        pass
    

