
from treelib import Node, Tree
from ...datasets import ExampleDataset
from .XYCut_sorter import XYCut

page = ExampleDataset().pages[2]
tree = Tree()
xycut = XYCut()
edge = xycut.sort_using_XYCut(page=page)
print(edge.childs, "Дети")
    
