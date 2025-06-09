from ..base_sorter import BBox
class Walley:
    '''
    Класс который нужен для раздлеления блоков на группы, в завимости от их расположения относительно разделений.

    '''
    id = 0

    def __init__(self, bboxes:list[BBox] = None):
        self.id = Walley.id
        Walley.id += 1

        if bboxes is None: 
            self.bboxes = []
        else:
            self.bboxes = bboxes


    @staticmethod
    def get_max_min(bboxes: list[BBox]):
        min_x = min([bbox.x_top_left for bbox in bboxes])
        min_y = min([bbox.y_top_left for bbox in bboxes])
        max_x = max([bbox.x_bottom_right for bbox in bboxes])
        max_y = max([bbox.y_bottom_right for bbox in bboxes])

        return (min_x, min_y), (max_x, max_y)
    def __repr__(self):
        return f"id:{self.id}, {self.bboxes}, минимальные и максимальные координаты: {Walley.get_max_min(self.bboxes)}"
        