from abc import ABC, abstractmethod
from .page import Page

class BaseDataset(ABC):
    @abstractmethod
    @property
    def pages(self) -> list[Page]:
        pass