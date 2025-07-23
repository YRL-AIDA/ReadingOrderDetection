from ..base_metric import BaseMetric
from typing import List, Tuple


class FullMatchPrecision(BaseMetric):
    def metric(self, data: List[Tuple[int]]) -> float:
        true_ = 0
        false_ = 0
        for d in data:
            if d[0] == d[1]:
                true_ += 1
            else:
                false_ += 1
        return true_/(true_+false_) if true_+false_ != 0 else -1 

