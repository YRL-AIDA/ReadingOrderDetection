from dtype.sorters.argument_sorter.argument_sorter import Argument_sorter
from dtype.sorters.argument_sorter.argumentation_framework import ArgumentationFramework, Argument
from dtype.datasets.example_dataset.example_dataset import ExampleDataset
from utils.drawer import Drawer


sorter = Argument_sorter()
for page in ExampleDataset().pages:
    pred_read = sorter.sort(page=page)

    Drawer.draw_with_arrows(page, pred_read=pred_read)

