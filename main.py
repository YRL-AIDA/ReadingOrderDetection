from dtype.datasets import *
from dtype.sorters.rule_sorter.rule_sorter import RuleSorter
from dtype.sorters import *
from dtype.metrics import *
from utils.drawer import *

datasets ={ "ExampleDataset":ExampleDataset(),
          }
sorters ={ "TriangularSorter":TriangularSorter(),
          "Rule_sorter" : RuleSorter(),
          }
metrics = {
    "FullMatchPrecision":FullMatchPrecision(),
}

for name_sorter, sorter in sorters.items():
    print("="*10, name_sorter, "="*10)
    for name_dataset, dataset in datasets.items():
        print("*"*5, name_dataset, "*"*5)
        for name_metric, metric in metrics.items():
            print(name_metric, f':\t{metric.compute(dataset, sorter):.4f}')

page = datasets["ExampleDataset"].pages[2]
sorter = sorters["TriangularSorter"]
inds = sorter.sort(page)
print(inds)

true_inds = [page.true_reading_order[bbox.id] for bbox in page.bboxes]
print(true_inds)
Drawer.draw_with_arrows(page, pred_read=inds)
# inds = sorter.sort(page)


# print("pred_inds:", inds)
# print("true_inds:", true_inds)