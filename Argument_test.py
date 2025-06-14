from dtype.sorters.argument_sorter.argument_sorter import Argument_sorter
from dtype.sorters.argument_sorter.argumentation_framework import ArgumentationFramework, Argument

args = [
    Argument(0,3),
    Argument(1,2),
    Argument(3,1),
    Argument(2,4),
    Argument(4,5),
    Argument(4,6),
    Argument(4,7),
    Argument(5,6),
    Argument(5,9),
    Argument(6,7),
    Argument(8,0),
    Argument(8,4),
    Argument(8,9),
    
]
ArgumentationFramework1 = ArgumentationFramework(args)


ArgumentationFramework1.get_complete_extensions()
ArgumentationFramework1.get_stable_extensions()
ArgumentationFramework1.get_preffered_extentions()
for a in ArgumentationFramework1.attacks:
    print(a)
ArgumentationFramework1.print_complete_extensions()
print("!!!!!!")
ArgumentationFramework1.print_stable_extensions()
print("!!!")
ArgumentationFramework1.get_preffered_extentions()
ArgumentationFramework1.print_preferred_extensions()