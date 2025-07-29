import matplotlib.pyplot as plt
from dtype.bbox import BBox
from dtype.sorters.triangular_sorter.sortable_bbox import Left2RightTop2BottomImageSegment
from typing import Tuple, Dict
import numpy as np
from dtype.page import Page

class Drawer():
    '''
    Для отрисовки со стрелками нужно передать страницу, а также по желанию предсказанный порядок
    '''
    @staticmethod
    def draw_with_arrows(page:Page, pred_read=None):
        bboxes = page.bboxes

        x_bottom = 0
        y_bottom = 0

        x_bottom = 0
        y_bottom = 0

        for i in range(len(bboxes)):
            if x_bottom < bboxes[i].x_bottom_right:
                x_bottom = bboxes[i].x_bottom_right
            if y_bottom < bboxes[i].y_bottom_right:
                y_bottom = bboxes[i].y_bottom_right
        labeling = []

        x_bottom +=10
        y_bottom += 10

        image_for_bboxes = np.full((y_bottom, x_bottom, 3), 255)

        for i in range(len(bboxes)):
            labeling.append((bboxes[i].x_top_left, bboxes[i].y_top_left, page.text[i]))

            for height in range(bboxes[i].height):

                for width in range(bboxes[i].width):
                    image_for_bboxes[bboxes[i].y_top_left+height][bboxes[i].x_top_left+width] = np.array([156,156,156])


        sizes = Drawer.font_sizes(bboxes)
        Drawer.draw_and_img(image_for_bboxes, labeling=labeling, sizes=sizes, page = page, pred_read=pred_read)



    @staticmethod
    def font_sizes(bboxes : Tuple['BBox']):
        sizes = []
        for i in range(len(bboxes)):
            sizes.append(bboxes[i].height)

        return sizes


    @staticmethod
    def draw_and_img(img, labeling = None , sizes = None, page:Page = None, pred_read = None):

        plt.imshow(img, interpolation='nearest')
        i = 0
        if labeling:
            for x_coord, y_coord, label in labeling:
                plt.text(x_coord, y_coord, label, ha='left', va='top', fontsize = sizes[i])
                i+=1
        # Отрисовка заданного по датасету порядка чтения
        _temp_order = page.true_reading_order
        print(page.true_reading_order)
        for i, j in zip(_temp_order, _temp_order[1:]):
            bbox_first = page.get_bbox_by_RO(i)
            bbox_second = page.get_bbox_by_RO(j)
            print(bbox_first, bbox_second)
            x1, w1, y1, h1 = bbox_first.x_top_left, \
                            bbox_first.width/2, \
                            bbox_first.y_top_left, \
                            bbox_first.height/2
            x2, w2, y2, h2 = bbox_second.x_top_left, \
                            bbox_second.width/2, \
                            bbox_second.y_top_left, \
                            bbox_second.height/2

            plt.annotate(" ",
                        xy=(x2+w2, y2+h2),
                        xytext=(x1+w1, y1+h1),
                            arrowprops=dict(arrowstyle='->', color='blue', lw=1.5)  )

        if pred_read:
            print(pred_read)
            _temp_pred_order = sorted(pred_read)
            for i, j in zip(_temp_pred_order, _temp_pred_order[1:]):
                bbox_first = page.get_bbox_by_RO(i)
                bbox_second = page.get_bbox_by_RO(j)
                x1, w1, y1, h1 = bbox_first.x_top_left, \
                                bbox_first.width/2 + 0.5, \
                                bbox_first.y_top_left, \
                                bbox_first.height/2 + .5
                x2, w2, y2, h2 = bbox_second.x_top_left, \
                                bbox_second.width/2 + .5, \
                                bbox_second.y_top_left, \
                                bbox_second.height/2 + .5

                plt.annotate(" ",
                            xy=(x2+w2, y2+h2),
                            xytext=(x1+w1, y1+h1),
                                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
            plt.title('Синий - данный. Красный - полученный')

        plt.show()


    @staticmethod
    def draw_bbox(bboxes : Tuple['BBox'], text : Tuple['str']):
        x_bottom = 0
        y_bottom = 0

        for i in range(len(bboxes)):
            if x_bottom < bboxes[i].x_bottom_right:
                x_bottom = bboxes[i].x_bottom_right
            if y_bottom < bboxes[i].y_bottom_right:
                y_bottom = bboxes[i].y_bottom_right
        labeling = []

        x_bottom +=10
        y_bottom += 10

        image_for_bboxes = np.full((y_bottom, x_bottom, 3), 255)

        for i in range(len(bboxes)):
            labeling.append((bboxes[i].x_top_left, bboxes[i].y_top_left, text[i]))
            for height in range(bboxes[i].height):
                for width in range(bboxes[i].width):
                    image_for_bboxes[bboxes[i].y_top_left+height][bboxes[i].x_top_left+width] = np.array([156,156,156])


        sizes = Drawer.font_sizes(bboxes)
        Drawer.draw_and_img(image_for_bboxes, labeling=labeling, sizes=sizes)
