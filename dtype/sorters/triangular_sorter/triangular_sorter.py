from ..base_sorter import BaseSorter, BBox, Page
from .sortable_bbox import Left2RightTop2BottomImageSegment
from typing import List

import copy
class TriangularSorter(BaseSorter):
    def sort(self, page: Page):
        return self.__sort_bboxes_using_triangles(page.bboxes)

    def __sort_bboxes_using_triangles(self, segs_):    
        segs = []
        for i in range(len(segs_)):
            segs.append(Left2RightTop2BottomImageSegment.converter(segs_[i]))
            segs[i].index = i
        
        for i in range(len(segs)):
            for j in range(len(segs)):
                if segs[j].greater_then_vertical(segs[i]):
                    segs[i], segs[j] = segs[j], segs[i]
                elif segs[j].greater_then_vertical(segs[i]) is None and segs[j].greater_then_horizont(segs[i]):
                    segs[i], segs[j] = segs[j], segs[i]
                    
        return  [seg.index for seg in segs]