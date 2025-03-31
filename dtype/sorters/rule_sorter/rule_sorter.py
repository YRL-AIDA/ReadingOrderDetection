from ..base_sorter import BaseSorter, BBox, Page
from ..triangular_sorter.sortable_bbox import Left2RightTop2BottomImageSegment
from typing import List

import copy
class RuleSorter(BaseSorter):


    def sort(self, page: Page):
        return self.__sort_bboxes_using_rules(page.bboxes)

    # Сортируем блоки в соответствии с правилами статьи 1
    def __sort_bboxes_using_rules(self, segs_):    
        segs = []
        for i in range(len(segs_)):
            segs.append(Left2RightTop2BottomImageSegment.converter(segs_[i]))
            segs[i].index = i

        for i in range(len(segs)):
            for j in range(i, len(segs)):
                if self.__rule_first(segs[i], segs[j]) or self.__rule_second(segs[i], segs[j], segs):
                    segs[i], segs[j] = segs[j], segs[i]
                    
        return  [seg.index for seg in segs][::-1]
        
    # Правило сравнения в статье номер 2
    def __rule_second(self, a:BBox, b:BBox, segs:List[BBox]):
        if  a.x_top_left + a.width < b.x_top_left and not self.__has_block_between(a, b, segs):
            return True
        return False
    
    # Проверяет, есть ли блоки между двумя данными
    def __has_block_between(self, a, b, segs):
        for seg in segs:
            if self.__overlaps(seg, a) and self.__overlaps(seg, b) and self.__between(a, b, seg):
                return True 
        return False

    # Правило сравнения в статье номер 1
    def __rule_first(self, a:BBox, b:BBox) -> bool:
        if self.__overlaps(a=a, b=b) and a.y_bottom_right < b.y_top_left:
            return True
        return False

    # Проверка наложения координат по x
    def __overlaps(self, a:BBox, b:BBox) -> bool:
        if (a.x_top_left > b.x_top_left and a.x_top_left < b.x_bottom_right) or \
            (a.x_bottom_right < b.x_bottom_right and a.x_bottom_right > b.x_top_left) or \
            (b.x_top_left > a.x_top_left and b.x_top_left < a.x_bottom_right) or \
            (b.x_bottom_right < a.x_bottom_right and b.x_bottom_right > a.x_top_left):
            return True
        return False
    
    # Проверка на то, что блок с находится между блоками a, b по координате y
    def __between(self, a:BBox, b:BBox, c:BBox) -> bool:
        if (c.y_top_left > min(a.y_top_left, b.y_top_left)) or (c.y_bottom_right < max(a.y_bottom_right, b.y_bottom_right)):
            return True
        return False 
