
from dtype.datasets import ExampleDataset
from dtype.sorters import *
from dtype.metrics import *
from utils.drawer import Drawer

pages = ExampleDataset().pages[0]
sorter = XYCut()

sorter.sort(pages)

Drawer.draw_with_arrows(pages, pred_read=sorter.sort(pages))

