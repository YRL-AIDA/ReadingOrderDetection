from ..base_dataset import BaseDataset
from ...page import Page, BBox
import os
import json


PATH_DATASET = os.path.join(os.path.dirname(__file__), 'dataset')
NAME_FILES = os.listdir(PATH_DATASET)

# TODO: Можно сделать лучше :) 
class ExampleDataset(BaseDataset):

    def get_pages(self) -> list[Page]:
        return [self.__open_page_num(i) for i, name in enumerate(NAME_FILES) if '.json' in name ]

    def __open_page_num(self, num:int):
        if num > len(NAME_FILES) or num < 0:
            raise ValueError("Page number is not correct")
        
        name_file = os.path.join(PATH_DATASET, f'boxes_{num}.json')
        with open(name_file, 'r') as f:
            blocks =json.load(f)['blocks']
        bboxes = [BBox(id=i,
                       x_top_left =     b['x_top_left'],
                       x_bottom_right = b['x_bottom_right'],
                       y_top_left =     b['y_top_left'],
                       y_bottom_right = b['y_bottom_right']) for i, b in enumerate(blocks)]
        true_reading_order = dict() 
        text = []
        for i, b in enumerate(blocks):
            true_reading_order[int(b["text"])] = i
            text.append(b['text'])
        page = Page(bboxes, true_reading_order, img=None, text=text)
        return page
    
    def get_answers(self):
        pass