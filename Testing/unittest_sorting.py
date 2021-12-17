import unittest

from Domain.carte import Carte
from Sorting_Algorithms.sort_algorithms import SortAlg

class SortAlgtest(unittest.TestCase):

    def test_insertion_sort(self):
        sort = SortAlg()
        carte1 = Carte(1, "A", "a", "-", False)
        carte2 = Carte(2, "A", "a", "-", False)
        carte3 = Carte(3, "A", "a", "-", False)
        carte4 = Carte(4, "A", "a", "-", False)

        list = [carte4, carte3, carte2, carte1]

        sort.insertion_sort(list, key = lambda x: x.get_id(), reversed = False)

        for c in list:
            print (c)

    def test_comb_sort(self):
        sort = SortAlg()
        carte1 = Carte(1, "A", "a", "-", False)
        carte2 = Carte(2, "A", "a", "-", False)
        carte3 = Carte(3, "A", "a", "-", False)
        carte4 = Carte(4, "A", "a", "-", False)

        list = [carte4, carte3, carte2, carte1]

        sort.comb_sort(list, key = lambda x: x.get_id(), reversed = True)
