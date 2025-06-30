from .bbox import BBox
from typing import List, Dict

class Page:
    def __init__(self, bboxes: List[BBox], true_reading_order: Dict[int, int], img=None, text:List=None):
        self.bboxes = bboxes
        self.img = img
        self.true_reading_order = true_reading_order
        self.text = text
    
    def get_max_min(self):
        min_x = min([bbox.x_top_left for bbox in self.bboxes])
        min_y = min([bbox.y_top_left for bbox in self.bboxes])
        max_x = max([bbox.x_bottom_right for bbox in self.bboxes])
        max_y = max([bbox.y_bottom_right for bbox in self.bboxes])
        return (min_x, min_y), (max_x, max_y)