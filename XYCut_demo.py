from dtype.datasets import ExampleDataset
from dtype.sorters.rule_sorter.rule_sorter import RuleSorter
from dtype.sorters import *
from dtype.metrics import *
from utils.drawer import Drawer
from dtype.sorters.layout_XYCut.XYCut_sorter import XYCut

pages = ExampleDataset().pages
xycut = XYCut()
for page in pages:
    result = xycut.sort(page=page)
    print(page.true_reading_order)
    print(result)
    Drawer.draw_with_arrows(page, pred_read=[int(item) for item in result])
