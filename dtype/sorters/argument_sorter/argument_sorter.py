from ..base_sorter import BaseSorter, Page, BBox
from .argumentation_framework import Argument, ArgumentationFramework
import time


class Argument_sorter(BaseSorter):


    def sort(self, page:'Page'):
        self.programm_start_time = time.time()
        return self.sort_using_ArugemtationFramework(page)


    def sort_using_ArugemtationFramework(self, page:Page):
        self.page = page
        arguments = []
        for bbox in page.bboxes:
            arguments += self.get_bbox_arguments(bbox)
        argumentation_framework = ArgumentationFramework(arguments=arguments)
        get_complete_ext_time = time.time()
        argumentation_framework.get_complete_extensions()
        print("Получение комплит расширений %s seconds ---" % (time.time() - get_complete_ext_time))
        get_prefered_ext_time = time.time()
        argumentation_framework.get_preffered_extentions()
        print("Получение prefered расширений %s seconds ---" % (time.time() - get_prefered_ext_time))

        pred_reads = argumentation_framework.preffered_extentions[0]
        args = []
        for i in range(len(pred_reads)):
            if pred_reads[i] == 1:
                args.append(argumentation_framework.arguments[i])
        self.args = args

        line = self.get_lines(args=args)
        reading_order = self.get_reading_order(line)
        print("Выполнение всего алгоритма %s seconds ---" % (time.time() - self.programm_start_time))

        return reading_order


    def get_reading_order(self, line):
        reading_order = []
        for arg in line:
            reading_order.append(arg.bbox_first)
        reading_order.append(line[-1].bbox_second)
        return reading_order


    def get_lines(self, args):
        maxx = 0
        line = None
        for arg in args:
            current_max = 0
            current_line = [arg]
            self.get_line_from_arg(arg,current_max, current_line,)
            if len(current_line) > maxx:
                maxx = len(current_line)
                line = current_line
        return line



    def get_line_from_arg(self, arg, current_max, current_line):
        has_continue = False
        for temp_arg in self.args:
            if temp_arg.bbox_first == arg.bbox_second:
                has_continue = True
        if has_continue:
            for temp_arg in self.args:
                if temp_arg.bbox_first == arg.bbox_second:
                    current_max += 1
                    current_line.append(temp_arg)
                    self.get_line_from_arg(temp_arg, current_max, current_line)



    def get_bbox_arguments(self, bbox:BBox) -> list[Argument]:
        arguments = self.get_bbox_arguments_vertical(bbox) + self.get_bbox_arguments_horizontal(bbox)
        new_args = []
        for argument in arguments:
            arg = Argument(bbox.id, argument.id)
            new_args.append(arg)
        return new_args



    def get_bbox_arguments_horizontal(self, bbox:BBox):
        arguments = []

        minn, maxx = self.page.get_max_min()
        delta_x = abs(minn[0] - maxx[0])//100
        closest = self.get_closets_bbox_x(bbox)
        consts = closest + delta_x

        for temp_bbox in self.page.bboxes:
            if (bbox.y_top_left <= temp_bbox.y_top_left <= bbox.y_bottom_right \
                  or bbox.y_top_left <= temp_bbox.y_bottom_right <= bbox.y_bottom_right) and \
                    bbox.x_bottom_right <= temp_bbox.x_top_left <= consts:

                arguments.append(temp_bbox)
        return arguments

    def get_bbox_arguments_vertical(self, bbox:BBox):
        arguments = []

        minn, maxx = self.page.get_max_min()
        delta_x = abs(minn[1] - maxx[1])//100
        closest = self.get_closets_bbox_y(bbox)
        consts = closest + delta_x

        for temp_bbox in self.page.bboxes:
            if bbox.y_bottom_right <= temp_bbox.y_top_left <= consts:

                arguments.append(temp_bbox)
        return arguments


    def get_closets_bbox_x(self, bbox:BBox) -> BBox:
        y_min = bbox.y_top_left
        y_max = bbox.y_bottom_right
        current_min = self.page.get_max_min()[1][0]
        for bboxx in self.page.bboxes:
            if bboxx == bbox:
                continue
            if bbox.x_bottom_right <=bboxx.x_top_left <=current_min and y_min <= bboxx.y_top_left <= y_max:
                current_min = bboxx.x_top_left
        return current_min

    def get_closets_bbox_y(self, bbox:BBox) -> BBox:
        x_min = bbox.x_top_left
        x_max = bbox.x_bottom_right
        current_min = self.page.get_max_min()[1][1]
        for bboxx in self.page.bboxes:
            if bboxx == bbox:
                continue

            if bbox.y_bottom_right <=bboxx.y_top_left <=current_min and x_min <= bboxx.x_top_left <= x_max:
                current_min = bboxx.y_top_left
        return current_min
