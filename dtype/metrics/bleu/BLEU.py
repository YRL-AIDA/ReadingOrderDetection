from ..base_metric import BaseMetric
from typing import List, Tuple


class BLEU(BaseMetric):
    '''
    Метрика BLEU будет считаться по среднему значению по страницам документов
    '''
    def metric(self, data) -> float:
        result = 0
        for temp_data in data:
            self.right_read = temp_data[1]
            self.pred_read = temp_data[0]

            n = len(self.right_read); m = len(self.pred_read)
            score = 0
            if m!=n:
                score += self.get_right_read()
            for a, b in zip(self.right_read, self.pred_read):
                if a==b:
                    score +=1
            result += score
        return result / len(data)


    def get_right_read(self):
        c = 0
        for item in self.right_read:
            if not item in self.pred_read:
                c+=1
                self.right_read.remove(item)
        return c
