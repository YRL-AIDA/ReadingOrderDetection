from ..base_metric import BaseMetric
from typing import List, Tuple
from unittest.mock import right


class ARD(BaseMetric):
    '''
    Метрика ARD будет считаться по среднему значению по страницам документов
    '''
    def metric(self, data) -> float:
        result = 0
        for temp_data in data:
            pred_order = temp_data[0]
            right_order = temp_data[1]
            

            n = len(right_order)
            score = 0
            for bbox in right_order:
                try:
                    index_in_pred_order = pred_order.index(bbox)
                    delta = abs(right_order.index(bbox) - index_in_pred_order)
                    score += delta
                except ValueError:
                    score += n

            result += score
        return result / len(data)
