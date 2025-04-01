from ..base_sorter import BBox
import math

class Left2RightTop2BottomImageSegment(BBox):
     
    def __init__(self, x_top_left: int, y_top_left: int, x_bottom_right: int, y_bottom_right: int) -> None:
        super().__init__(x_top_left=x_top_left, 
                         y_top_left=y_top_left, 
                         x_bottom_right=x_bottom_right, 
                         y_bottom_right=y_bottom_right)
        
    
    @staticmethod
    def converter(seg: BBox):        
        return Left2RightTop2BottomImageSegment(seg.x_top_left, seg.y_top_left, seg.x_bottom_right, seg.y_bottom_right)
    
    def __get_dist(self, l, r, c):
        A = math.sqrt((l[0] - r[0])**2 + (l[1] - r[1])**2)
        B = math.sqrt((l[0] - c[0])**2 + (l[1] - c[1])**2)
        C = math.sqrt((c[0] - r[0])**2 + (c[1] - r[1])**2)
        return A, B, C
        
    def __get_min_cos(self, l, r, c):
        A, B, C = self.__get_dist(l, r, c)
        if 0 in (A, B, C): # TODO: Проверить
            return -1
        return min([(B**2+C**2-A**2)/(2*B*C), (A**2+C**2-B**2)/(2*A*C), (B**2+A**2-C**2)/(2*B*A)])
            

    def greater_then_horizont(self, BBox: BBox):
        w1 = abs(self.x_top_left - self.x_bottom_right)
        w2 = abs(BBox.x_top_left - BBox.x_bottom_right)
        l1, c1, r1 = (self.x_top_left,      self.y_top_left), \
                     (self.x_top_left+w1/2, self.y_top_left), \
                     (self.x_bottom_right,  self.y_top_left)
        
        l2, c2, r2 = (BBox.x_top_left,      BBox.y_top_left), \
                     (BBox.x_top_left+w2/2, BBox.y_top_left), \
                     (BBox.x_bottom_right,  BBox.y_top_left)
       
        cos1 = self.__get_min_cos(l1, r1, c2)
        cos2 = self.__get_min_cos(l2, r2, c1)
        
        if cos1 < 0 and cos2 < 0:
            return (BBox.x_top_left + BBox.width/2) > (self.x_top_left + self.width/2)
        else:
            return None # ответ на вопрос больше будет отрицателен, не сравнимы
        
        
    def greater_then_vertical(self, BBox: BBox):
        h1 = abs(self.y_top_left - self.y_bottom_right)
        h2 = abs(BBox.y_top_left - BBox.y_bottom_right)
        l1, c1, r1 = (self.x_top_left, self.y_top_left), \
                     (self.x_top_left, self.y_top_left + h1/2), \
                     (self.x_top_left, self.y_bottom_right)
            
        l2, c2, r2 = (BBox.x_top_left, BBox.y_top_left), \
                     (BBox.x_top_left, BBox.y_top_left + h2/2), \
                     (BBox.x_top_left, BBox.y_bottom_right)
            
        cos1 = self.__get_min_cos(l1, r1, c2)
        cos2 = self.__get_min_cos(l2, r2, c1)
        
        if cos1 < 0 and cos2 < 0:
            return (BBox.y_top_left + BBox.height/2) > (self.y_top_left + self.height/2)
        else:
            return None