from abc import ABC, abstractmethod
from ..datasets import BaseDataset
from ..sorters import BaseSorter
from typing import List

class Metric(ABC):
    def compute(self, dataset: BaseDataset, sorter: BaseSorter):
        data = []
        for page in dataset.pages:
            bboxs = page.bboxs
            inds = sorter(page)
            true_inds = [page.true_reading_order[bbox.id] for bbox in bboxs]
            data.append(inds, true_inds)

        return self.metric(data)
    
    @abstractmethod
    def metric(self, data:List[List[int]]) -> float:
        pass