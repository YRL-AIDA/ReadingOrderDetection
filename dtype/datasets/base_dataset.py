from abc import ABC, abstractmethod
from ..page import Page

class BaseDataset(ABC):

    @property
    def pages(self) -> list[Page]:
        return self.get_pages()
    
    @abstractmethod
    def get_pages(self) -> list[Page]:
        pass