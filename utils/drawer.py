from matplotlib import pyplot as plt
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
        
        image_for_bboxes = np.zeros((y_bottom, x_bottom, 3))
        
        for i in range(len(bboxes)):
            labeling.append((bboxes[i].x_top_left, bboxes[i].y_top_left, page.text[i]))

            for height in range(bboxes[i].height):
                
                for width in range(bboxes[i].width):
                    image_for_bboxes[bboxes[i].y_top_left+height][bboxes[i].x_top_left+width] = np.array([225, 225, 225])
                    
                    
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
        for i in range(len(page.true_reading_order) - 1):        
            x1, w1, y1, h1 = page.bboxes[page.true_reading_order[i]].x_top_left, \
                            page.bboxes[page.true_reading_order[i]].width/2, \
                            page.bboxes[page.true_reading_order[i]].y_top_left, \
                            page.bboxes[page.true_reading_order[i]].height/2
            x2, w2, y2, h2 = page.bboxes[page.true_reading_order[i+1]].x_top_left, \
                            page.bboxes[page.true_reading_order[i+1]].width/2, \
                            page.bboxes[page.true_reading_order[i+1]].y_top_left, \
                            page.bboxes[page.true_reading_order[i+1]].height/2

            plt.annotate(" ",
                        xy=(x2+w2, y2+h2),
                        xytext=(x1+w1, y1+h1), 
                            arrowprops=dict(arrowstyle='->', color='blue', lw=1.5)  )
            
        if pred_read:
            for i in range(len(pred_read) - 1):        
                x1, w1, y1, h1 = page.bboxes[pred_read[i]].x_top_left, \
                                page.bboxes[pred_read[i]].width/2 + 0.5, \
                                page.bboxes[pred_read[i]].y_top_left, \
                                page.bboxes[pred_read[i]].height/2 + .5
                x2, w2, y2, h2 = page.bboxes[pred_read[i+1]].x_top_left, \
                                page.bboxes[pred_read[i+1]].width/2 + .5, \
                                page.bboxes[pred_read[i+1]].y_top_left, \
                                page.bboxes[pred_read[i+1]].height/2 + .5

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
        
        image_for_bboxes = np.zeros((y_bottom, x_bottom, 3))
        
        for i in range(len(bboxes)):
            labeling.append((bboxes[i].x_top_left, bboxes[i].y_top_left, text[i]))

            for height in range(bboxes[i].height):
                
                for width in range(bboxes[i].width):
                    image_for_bboxes[bboxes[i].y_top_left+height][bboxes[i].x_top_left+width] = np.array([225, 225, 225])
                    
                    
        sizes = Drawer.font_sizes(bboxes)
        Drawer.draw_and_img(image_for_bboxes, labeling=labeling, sizes=sizes)
        
        
        