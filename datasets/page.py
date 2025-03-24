from .bbox import BBox
from typing import List, Dict

class Page:
    def __init__(self, bboxs: List[BBox], true_reading_order: Dict[int, int], img=None):
        self.bboxs = bboxs
        self.img = img
        self.true_reading_order = true_reading_order