from ..base_sorter import BaseSorter, Page, BBox
import itertools

class ArgumentationFramework:
    '''
    Класс, который хранит в себе набор элементов, называемые аргументами, а также матрицу, которая определяет
    наличие атак между элементами
    '''

    def __init__(self, arguments:list['Argument'], attacks = None):
        '''
        При создании фреймворка аргументаций достаточно задать только сами аргументы. Атаки фреймфорк построит сам
        Также фреймворк сам выделит стабильное расширение для этого множества аргументов и атак.

        Также, при работе с множествами: множество S это массив длины len(self.arguments), заполненный либо 0 либо 1. 1 означает то,
        что этот аргумент попадает в множество S.
        '''
        self.arguments = arguments
        if attacks is None:
            self.attacks = self.get_attacks()
        else:
            self.attacks = attacks


    def get_complete_extensions(self):
        compete_extensions = []
        all_variants = itertools.product("01", repeat=len(self.arguments))
        for variant in all_variants:
            variant = [int(item) for item in variant]
            if self.is_complete_extension(variant) and self.is_conflict_free(variant):
                compete_extensions.append(variant)
        self.complete_extensions = compete_extensions

    def get_preffered_extentions(self):
        max_len = max(sum(i) for i in self.complete_extensions)

        pref_ext = []
        for ext in self.complete_extensions:
            if sum(ext) == max_len:
                pref_ext.append(ext)
        self.preffered_extentions = pref_ext


    def get_stable_extensions(self):
        stable_extensions = []
        complete_extensions = self.complete_extensions
        for S in complete_extensions:
            is_stable = True
            for i in range(len(self.arguments)):
                if S[i] == 1:
                    continue
                attacks = False
                for j in range(len(S)):
                    if self.attacks[j][i] == 1 and S[j] == 1:
                        attacks = True
                if attacks == False:
                    is_stable = False
            if is_stable == True:
                stable_extensions.append(S)
        self.stable_extensions = stable_extensions


    def is_conflict_free(self, S:list[int]) -> bool:
        ''' Определяет, является ли множество безконфликтным
        '''
        for i in range(len(S)):
            if S[i] == 0:
                continue
            if S[i] == 1:
                attacks_from_this_arg = self.attacks[i]
                for j in range(len(attacks_from_this_arg)):
                    if attacks_from_this_arg[j] == 1 and S[j] == 1:
                        return False
        return True

    def is_complete_extension(self, S:list[int]) -> bool:
        F_S = self.F(S)
        for i in range(len(F_S)):
            if S[i] != F_S[i]:
                return False
        return True


    def F(self, S:list[int]) -> list['Argument']:
        '''
        Функция из работы F(S) = {a | те элементы, которые защищены элементами множества а}. Под защитой элемента b понимается атака на тот аргумент, который атакует b
        Проверка осуществляется так (подразумевается что множество S безконфликтно)
        '''
        F_S = [0 for i in range(len(S))]
        for i in range(len(self.attacks)): #АтакуеМый элемент
            flag = 1
            for j in range(len(self.attacks)): #АтакуюЩий элемент
                if self.attacks[j][i] == 1 and S[j] == 1: # Проверяем, если атакует элемент S, то аргумент защищен быть не может
                    flag = 0
                    break
                if self.attacks[j][i] == 1:
                    # Есть атака i-го элемента на j-ый. Проверим, защищает ли какой нибудь элемент множества S j элемент.
                    # Для этого проверим, атакует ли какой нибудь элемент множества S i-ый элемент
                    is_defended = False
                    for k in range(len(S)):
                        if self.attacks[k][j] == 1 and S[k] == 1:
                            is_defended = True
                            break
                    if not is_defended:
                        flag = 0
                        break
            if flag == 1:
                F_S[i] = 1
        return F_S


    def get_attacks(self) -> list[list]:
        attack_matrix = [[0 for _ in range(len(self.arguments))] for _ in range(len(self.arguments))]

        for i in range(len(self.arguments)):
            for j in range(len(self.arguments)):
                if i == j:
                    continue
                if self.arguments[i].bbox_first == self.arguments[j].bbox_first:
                    attack_matrix[i][j] = 1
                if self.arguments[i].bbox_second == self.arguments[j].bbox_second:
                    attack_matrix[i][j] = 1
        return attack_matrix

    def print_attacks(self) -> None:
        for i in range(len(self.attacks)):
            for j in range(len(self.attacks[i])):
                if self.attacks[i][j]:
                    print(f'{self.arguments[i]}-{self.arguments[j]}', end = ' ')
            print()

    def print_stable_extensions(self):
        for ext in self.stable_extensions:
            print('(', end = '')
            for i in range(len(ext)):
                if ext[i] == 1:
                    print(self.arguments[i], end = '')
            print(')')

    def print_complete_extensions(self):
        for ext in self.complete_extensions:
            print('(', end = '')
            for i in range(len(ext)):
                if ext[i] == 1:
                    print(self.arguments[i], end = '')
            print(')')

    def print_preferred_extensions(self):
        for ext in self.preffered_extentions:
            print('(', end = '')
            for i in range(len(ext)):
                if ext[i] == 1:
                    print(self.arguments[i], end = '')
            print(')')

class Argument:

    def __init__(self, bbox_first:int, bbox_second:int):
        self.bbox_first = bbox_first
        self.bbox_second = bbox_second

    def __repr__(self):
        return f"next({self.bbox_first}, {self.bbox_second})"
