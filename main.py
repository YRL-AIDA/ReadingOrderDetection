from dtype.datasets import *
from dtype.sorters.rule_sorter.rule_sorter import RuleSorter
from dtype.sorters import *
from dtype.metrics import *
from utils.drawer import *


page =ExampleDataset().pages[2]

Drawer.draw_with_arrows(page)
