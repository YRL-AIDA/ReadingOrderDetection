
from dtype.datasets import ExampleDataset
from dtype.sorters.rule_sorter.rule_sorter import RuleSorter
from dtype.sorters import *
from dtype.metrics import *
from utils.drawer import Drawer

pages = ExampleDataset().pages
xycut = XYCut()
print(pages[1].bboxes, pages[1].true_reading_order, pages[1].get_bbox_by_RO(4))
Drawer.draw_with_arrows(pages[1])
print(ARD().compute(ExampleDataset(), xycut))
