from dtype.sorters.argument_sorter.argument_sorter import Argument_sorter
from dtype.datasets.example_dataset.example_dataset import ExampleDataset
from dtype.metrics import *
from utils.drawer import Drawer

sorter = Argument_sorter()
for page in ExampleDataset().pages:

    Drawer.draw_with_arrows(page, pred_read=sorter.sort(page))
print(ARD().compute(ExampleDataset(), sorter))
