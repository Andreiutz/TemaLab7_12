import copy

class SortAlg:

    def insertion_sort(self, list, key = lambda x: x, reversed = False):
        '''
        Functia sorteaza lista list folosind insertion sort
        :param list: lista de obiecte
        :param reversed: True/False
        :return:
        '''
        n = len(list)
        for i in range(1, n):
            aux = list[i]
            p = i-1
            while p >= 0 and self.__compare(reversed, key(aux),  key(list[p])):
                list[p+1] = list[p]
                p -= 1
            list[p+1] = aux

    def __next_gap(self, gap):
        gap = (gap*10)//13
        if gap < 1:
            return 1
        return gap

    def comb_sort(self, list, key = lambda x: x, reversed = False):
        '''
        Functia sorteaza lista list folosind comb sort
        :param list: lista de obiecte
        :param reversed: True/False
        :return:
        '''
        n = len(list)
        gap = n
        swapped = True
        while gap != 1 or swapped == 1:
            gap = self.__next_gap(gap)
            swapped = False
            for i in range(n-gap):
                if self.__compare(reversed, key(list[i+gap]), key(list[i])):
                    list[i], list[i+gap] = list[i+gap], list[i]
                    swapped = True


    def __compare(self, reverse, param1, param2):
        if reverse:
            return param1 > param2
        else:
            return param1 < param2
