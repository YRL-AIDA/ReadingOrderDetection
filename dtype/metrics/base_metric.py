from abc import ABC, abstractmethod
from ..datasets import BaseDataset
from ..sorters import BaseSorter
from typing import List, Tuple

class BaseMetric(ABC):
    def compute(self, dataset: BaseDataset, sorter: BaseSorter):
        data = []
        for page in dataset.pages:
            bboxes = page.bboxes
            inds = sorter.sort(page)
            true_inds = [page.true_reading_order[bbox.id] for bbox in bboxes]
            data.append((inds, true_inds))

        return self.metric(data)

    @abstractmethod
    def metric(self, right_order: List[int], pred_order: List[int]) -> float:
        pass
