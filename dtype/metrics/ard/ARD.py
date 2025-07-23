from ..base_metric import BaseMetric
from typing import List, Tuple


class ARD(BaseMetric):
    def metric(self, data: Tuple[List[int]]) -> float:
        right_order = data[0]
        pred_order = data[1]

        n = len(right_order)
        score = 0
        for bbox in right_order:
            try:
                index_in_pred_order = pred_order.index(bbox)
                delta = abs(right_order.index(bbox) - index_in_pred_order)
                score += delta
            except ValueError:
                score += n

        return score