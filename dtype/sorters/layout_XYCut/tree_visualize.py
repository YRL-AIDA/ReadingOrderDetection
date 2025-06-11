from treelib import Node, Tree
from ...datasets import ExampleDataset
from .XYCut_sorter import XYCut
from ....utils.drawer import Drawer

page = ExampleDataset().pages[2]
xycut = XYCut()
result = xycut.sort(page=page)
Drawer.draw_with_arrows(page, pred_read=[int(item) for item in result])
