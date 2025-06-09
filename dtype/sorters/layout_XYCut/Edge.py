class Edge:
    '''
    Узел, нужен для составления дерева
    '''
    id = 0
    def __init__(self, number, childs:list['Edge'] = None):
        self.id = Edge.id
        Edge.id += 1

        self.number = number
        if childs is None: 
            self.childs = []
        else:
            self.childs = childs

    def __repr__(self):
        return f"Узел id:{self.id}, number = {self.number}"
