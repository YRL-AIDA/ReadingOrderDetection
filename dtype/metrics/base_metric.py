from abc import ABC, abstractmethod
from ..datasets import BaseDataset
from ..sorters import BaseSorter
from typing import List, Tuple


class BaseMetric(ABC):
    def compute(self, dataset: BaseDataset, sorter: BaseSorter):
        data = [(sorter.sort(page), page.true_reading_order) for page in dataset.pages]

        return self.metric(data)

    @abstractmethod
    def metric(self, data: List[Tuple[List[int], List[int]]]) -> float:
        pass
