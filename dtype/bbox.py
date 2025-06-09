

class BBox:
    def __init__(self, x_top_left, x_bottom_right, y_top_left, y_bottom_right, id=None):
        self.id = id
        self.x_top_left = x_top_left
        self.x_bottom_right = x_bottom_right
        self.y_top_left = y_top_left
        self.y_bottom_right = y_bottom_right
    
    @property
    def width(self):
        return self.x_bottom_right-self.x_top_left
    
    @property
    def height(self):
        return self.y_bottom_right-self.y_top_left
    
    def __str__(self):
        return f"<BBox id: {self.id}>"
    
    def __repr__(self):
        return f"<BBox id: {self.id}, {self.x_top_left}, {self.y_top_left}, {self.x_bottom_right}, {self.y_bottom_right}>"
    