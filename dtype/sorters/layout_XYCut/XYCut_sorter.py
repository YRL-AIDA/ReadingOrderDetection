from ..base_sorter import BaseSorter, Page, BBox
from .Edge import Edge
from .Walley import Walley


class XYCut(BaseSorter):

    def sort(self, page:'Page') -> list[int]:
        return self.sort_using_XYCut(page)

    def sort_using_XYCut(self, page:'Page') -> list[int]:
        bboxes = page.bboxes
        init_edge = Edge(number = "init")
        init_walley = Walley(bboxes=bboxes)
        XYCut.reqursion_step(walley=init_walley, edge=init_edge)
        res = []
        def print_childs(childsd):
            for child in childsd:
                if child.number == -1:
                    print_childs(child.childs)
                else:
                    res.append(child.number)
        print_childs(init_edge.childs)
        return res


    @staticmethod
    def reqursion_step(walley: Walley, edge:Edge) -> list[Edge]:
        '''
        Шаг рекурсии, возвращает массив эджей, который представляет собой детей родительского эджа.
        '''
        bboxes = walley.bboxes
        min_coor, max_coor = Walley.get_max_min(bboxes)
        proec_x = XYCut._proection_x(bboxes, min_coor, max_coor)
        proec_y = XYCut._proection_y(bboxes, min_coor, max_coor)

        if proec_y:
            XYCut._get_childs_y(bboxes, proec_y, min_coor, max_coor, edge=edge)
        elif proec_x:
            XYCut._get_childs_x(bboxes, proec_x, min_coor, max_coor, edge=edge)
        else:
            grups = [Edge(number=bbox.id) for bbox in bboxes]
            print(grups, "Если не произошло разделения")
            return grups

    @staticmethod
    def _get_childs_x(bboxes:list[BBox], proec_x, min_coor, max_coor, edge:Edge):
        steps = [min_coor[0]] + proec_x + [max_coor[0]]
        grups = []
        for _ in range(len(proec_x) + 1):
            grups.append(Walley())

        for i, (first, second) in enumerate(zip(steps[:-1], steps[1:])):
            for bbox in bboxes:
                if first <= bbox.x_top_left <= second: #Расчет на то что если левый угол ббокса в группе проекционной, то и правая тоже
                    grups[i].bboxes.append(bbox)

        result = []
        for walley in grups:
            if len(walley.bboxes) <= 1:
                result.append(Edge(walley.bboxes[0].id))
            else:
                temp = Edge(number=-1)
                XYCut.reqursion_step(walley, edge=temp)
                result.append(temp)
        edge.childs = result


    @staticmethod
    def _get_childs_y(bboxes:list[BBox], proec_y, min_coor, max_coor, edge:Edge):
        steps = [min_coor[1]] + proec_y + [max_coor[1]]
        grups = []
        for _ in range(len(proec_y) + 1):
            grups.append(Walley())

        for i, (first, second) in enumerate(zip(steps[:-1], steps[1:])):
            for bbox in bboxes:
                if first <= bbox.y_top_left <= second: #Расчет на то что если левый угол ббокса в группе проекционной, то и правая тоже
                    grups[i].bboxes.append(bbox)
        result = []
        for walley in grups:
            if len(walley.bboxes) <= 1:

                result.append(Edge(walley.bboxes[0].id))
            else:
                temp = Edge(number=-1)
                XYCut.reqursion_step(walley, edge=temp)
                result.append(temp)
        edge.childs = result


    @staticmethod
    def _proection_x(bboxes:list[BBox], min_ccor, max_coor):
        proections = []
        flag = 1
        for x in range(min_ccor[0], max_coor[0], 1): #шаг тут конечно под вопросом какой ставить
            count = 0
            for bbox in bboxes:
                if bbox.x_top_left <= x < bbox.x_bottom_right:
                    count += 1
            if count == 0:
                if len(proections)!=0:
                    if x != (proections[-1] + 1) and flag == 1:
                        proections.append(x)
                        flag = 0
                else:
                    flag = 0
                    proections.append(x)
            else:
                flag = 1
        return proections if len(proections) != 0 else False


    @staticmethod
    def _proection_y(bboxes:list[BBox], min_ccor, max_coor):
        proections = []
        flag = 1
        for y in range(min_ccor[1], max_coor[1], 1): #шаг тут конечно под вопросом какой ставить
            count = 0
            for bbox in bboxes:
                if bbox.y_top_left <= y < bbox.y_bottom_right:
                    count += 1

            if count == 0:
                if len(proections)!=0:
                    if y != (proections[-1] + 1) and flag == 1:
                        flag = 0
                        proections.append(y)
                else:
                    proections.append(y)
                    flag = 0
            else:
                flag = 1
        return proections if len(proections) != 0 else False
