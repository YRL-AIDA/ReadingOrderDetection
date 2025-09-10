from ..base_dataset import BaseDataset
from ...page import Page, BBox
import os
import json
from pydoc import text


PATH_DATASET = os.path.join(os.path.dirname(__file__), 'dataset', 'val.json')



class PuplayNet(BaseDataset):

    def get_pages(self) -> list[Page]:
        with open(PATH_DATASET, 'r') as file:
            data = json.load(file)
            images = data['images']
            image_ids = [im['id'] for im in images]
        return [self.__open_page_num(image_id) for image_id in image_ids]

    def __open_page_num(self, image_id:int):

        with open(PATH_DATASET, 'r') as file:
            bboxes = []
            reading_order = []
            i = 0
            for annotation in json.load(file)['annotations']:
                if annotation['image_id'] == image_id:
                    xt, yt, w, h = annotation['bbox']
                    d = 3 if h >= 10 and w >= 10 else 0
                    xt, yt, xb, yb = xt+d, yt+d, xt+w-d, yt+h-d

                    bboxes.append(BBox(id = i, *list(map(round, [xt, xb, yt, yb]))))
                    reading_order.append(annotation['RO'])
                    i+=1
                else:
                    i=0

            true_reading_order = [0]*len(reading_order)
            for index, value in enumerate(reading_order):
                true_reading_order[value] = index
        page = Page(bboxes, true_reading_order=true_reading_order, img=image_id, text=reading_order)
        return page

    def get_answers(self):
        pass
