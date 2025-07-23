from ..base_metric import BaseMetric
from typing import List, Tuple


class BLEU(BaseMetric):
    def metric(self, right_read, pred_read) -> float:
        self.right_read = right_read
        self.pred_read = pred_read
        n = len(right_read); m = len(pred_read)
        score = 0
        if m!=n:
            score += self.get_right_read()
        for a, b in zip(self.right_read, self.pred_read):
            if a!=b:
                score +=1
        return score


    def get_right_read(self):
        c = 0
        for item in self.right_read:
            if not item in self.pred_read:
                c+=1
                self.right_read.remove(item)
        return c
        