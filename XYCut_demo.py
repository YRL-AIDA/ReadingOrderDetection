
from dtype.datasets import PuplayNet
from dtype.sorters.rule_sorter.rule_sorter import RuleSorter
from dtype.sorters import *
from dtype.metrics import *
from utils.drawer import Drawer

pages = PuplayNet().pages
sorter = XYCut()
for page in PuplayNet().pages[24:40]:

    Drawer.draw_with_arrows(page, pred_read=sorter.sort(page))
print(ARD().compute(PuplayNet(), sorter))
