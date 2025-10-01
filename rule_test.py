
from dtype.datasets import PuplayNet
from dtype.sorters.rule_sorter.rule_sorter import RuleSorter
from dtype.sorters import *
from dtype.metrics import *
from utils.drawer import Drawer

pages = PuplayNet().pages
sorter = RuleSorter()
for page in PuplayNet().pages[10:30]:
    Drawer.draw_with_arrows(page=page, pred_read=sorter.sort(page))
print(ARD().compute(PuplayNet(), sorter))
