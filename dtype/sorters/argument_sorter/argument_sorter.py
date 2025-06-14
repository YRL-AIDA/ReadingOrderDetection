from ..base_sorter import BaseSorter, Page, BBox


class Argument_sorter(BaseSorter):
    
    def sort(self, page:'Page'):
        return self.sort_using_ArugemtationFramework(page)
