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
            max_i = i
            for j in range(i+1, len(segs)):
                j_gt_max_i_v = segs[j].greater_then_vertical(segs[max_i])
                j_gt_max_i_h = segs[j].greater_then_horizont(segs[max_i])
                if  (j_gt_max_i_v) or (j_gt_max_i_v is None and j_gt_max_i_h):
                    max_i = j
            segs[i], segs[max_i] = segs[max_i], segs[i]          
        return  [seg.index for seg in segs]