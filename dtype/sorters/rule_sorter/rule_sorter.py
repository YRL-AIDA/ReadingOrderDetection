from ..base_sorter import BaseSorter, BBox, Page
from ..triangular_sorter.sortable_bbox import Left2RightTop2BottomImageSegment
from typing import List

import copy
class RuleSorter(BaseSorter):


    def sort(self, page: Page):
        return self.__sort_bboxes_using_rules(page.bboxes)

    # Сортируем блоки в соответствии с правилами статьи 1
    def __sort_bboxes_using_rules(self, bboxess):
        bboxes = copy.deepcopy(bboxess)

        for i in range(len(bboxes)):
            for j in range(i + 1, len(bboxes)):

                if bboxes[j].y_top_left < bboxes[i].y_top_left:
                    bboxes[i], bboxes[j] = bboxes[j], bboxes[i]
                
                elif (bboxes[j].y_top_left == bboxes[i].y_top_left and 
                    bboxes[j].x_top_left < bboxes[i].x_top_left):
                    bboxes[i], bboxes[j] = bboxes[j], bboxes[i]
                    
                    
        return  [seg.id for seg in bboxes]
        
