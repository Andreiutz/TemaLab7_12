import unittest
from Domain.carte import Carte
from Repository.carte_repository_file import CarteRepositoryFile
from Repository.carte_repository import CarteRepository
from Validation.carte_validator import CarteValidator
from Service.carte_service import CarteService

from Sorting_Algorithms.sort_algorithms import SortAlg

class TestCarte(unittest.TestCase):

    '''CONSTRUCTOR'''
    def test_eq(self):
        carte1 = Carte(1, "Ion", "Len", "--",0)
        carte2 = Carte(1, "Ion", "Len", "--",0)
        carte3 = Carte(2, "Ion", "Len", "--",0)

        self.assertEqual(carte1, carte2)
        self.assertNotEqual(carte1, carte3)

    '''REPOSITORY'''
    def test_add_carte(self):
        with open("test_carti.txt", "w") as f:
            f.write("")
        #repo_carte = CarteRepository()
        repo_carte = CarteRepositoryFile("test_carti.txt")
        assert (len(repo_carte) == 0)
        repo_carte.add_carte(Carte(1, "Ion", "Reb", "--",0))
        assert (len(repo_carte) == 1)
        try:
            repo_carte.add_carte(Carte(1, "Ion", "Reb", "--",0))
            assert False
        except Exception as ex:
            assert (str(ex) == "id-ul exista deja!\n")

    def test_delete_carte(self):
        with open("test_carti.txt", "w") as f:
            f.write("")

        carte1 = Carte(1, "AA", "aa", "--",0)
        carte2 = Carte(2, "BB", "bb", "--",0)
        carte3 = Carte(3, "CC", "cc", "--",0)

        #repo_carte = CarteRepository()
        repo_carte = CarteRepositoryFile("test_carti.txt")

        repo_carte.add_carte(carte1)
        repo_carte.add_carte(carte2)
        repo_carte.add_carte(carte3)

        repo_carte.delete_carte(2)
        assert repo_carte.get_all() == [carte1, carte3]

        try:
            repo_carte.delete_carte(4)
            assert False
        except Exception as ex:
            assert (str(ex) == "id-ul nu exista!\n")

    def test_modify_carte(self):
        with open("test_carti.txt", "w") as f:
            f.write("")

        carte1 = Carte(1, "AA", "aa", "--",0)
        carte2 = Carte(2, "BB", "bb", "--",0)
        carte3 = Carte(3, "CC", "cc", "--",0)
        carte4 = Carte(3, "DD", "cc", "--",0)
        bad_carte = Carte(4, "CC", "cc", "--",0)

        #repo_carte = CarteRepository()
        repo_carte = CarteRepositoryFile("test_carti.txt")

        repo_carte.add_carte(carte1)
        repo_carte.add_carte(carte2)
        repo_carte.add_carte(carte3)

        repo_carte.modify_carte(carte4)
        assert repo_carte.get_all() == [carte1, carte2, carte4]

        try:
            repo_carte.modify_carte(bad_carte)
            assert False
        except Exception as ex:
            assert (str(ex) == "cartea nu a fost gasita!\n")

    def test_get_carte(self):
        with open("test_carti.txt", "w") as f:
            f.write("")

        carte1 = Carte(1, "AA", "aa", "--",0)
        carte2 = Carte(2, "BB", "bb", "--",0)
        carte3 = Carte(3, "CC", "cc", "--",0)

        #repo_carte = CarteRepository()
        repo_carte = CarteRepositoryFile("test_carti.txt")

        repo_carte.add_carte(carte1)
        repo_carte.add_carte(carte2)
        repo_carte.add_carte(carte3)

        assert repo_carte.get_carte(1) == carte1
        try:
            repo_carte.get_carte(5)
            assert False
        except Exception as ex:
            assert (str(ex) == "id-ul nu exista!\n")

    '''VALIDARE'''
    def test_validare_date(self):
        id_carte = 1
        titlu = "Ion"
        autor = "Reb"
        descriere = "--"

        bad_id = -1
        bad_titlu = ""
        bad_autor = ""
        bad_descriere = ""

        valid = CarteValidator()

        valid.validare_date(id_carte, titlu, autor, descriere)
        try:
            valid.validare_date(bad_id, bad_titlu, bad_autor, bad_descriere)
            assert False
        except Exception as ex:
            assert (str(ex) == "id invalid!\ntitlu invalid!\nautor invalid!\ndescriere invalida!\n")

        try:
            valid.validare_date(bad_id, titlu, bad_autor, descriere)
            assert False
        except Exception as ex:
            assert str(ex) == "id invalid!\nautor invalid!\n"

    '''SERVICE'''
    def test_add_carte_service(self):
        valid_carte = CarteValidator()
        repo_carte = CarteRepository()
        serv_carte = CarteService(valid_carte, repo_carte)

        assert len(serv_carte) == 0

        serv_carte.add_carte(1, "a", "a", "--")

        assert len(serv_carte) == 1

        try:
            serv_carte.add_carte(1, "a", "a", "--")
            assert False
        except Exception as ex:
            assert str(ex) == "id-ul exista deja!\n"

        try:
            serv_carte.add_carte(-2, "", "", "")
            assert False
        except Exception as ex:
            assert str(ex) == "id invalid!\ntitlu invalid!\nautor invalid!\ndescriere invalida!\n"

    def test_modify_carte_service(self):
        valid = CarteValidator()
        repo = CarteRepository()
        srv = CarteService(valid, repo)
        srv.add_carte(1, "a", "a", "--")

        srv.modify_carte(1, "titlu", "AAA")
        srv.modify_carte(1, "autor", "BBB")
        srv.modify_carte(1, "descriere", "CCC")

        assert repo.get_carte(1) == Carte(1, "AAA", "BBB", "CCC", False)

        try:
            srv.modify_carte(1, "titlu", "")
            assert False
        except Exception as ex:
            assert str(ex) == "titlu invalid!\n"

    def test_sort_carti(self):
        sort = SortAlg()

        valid = CarteValidator()
        repo = CarteRepository()
        srv = CarteService(valid, repo)

        carte1 = Carte(1, "A", "a", "-", False)
        carte2 = Carte(2, "A", "a", "-", False)
        carte3 = Carte(3, "A", "a", "-", False)
        carte4 = Carte(4, "A", "a", "-", False)

        srv.add_carte(1, "A", "a", "-")
        srv.add_carte(3, "A", "a", "-")
        srv.add_carte(4, "A", "a", "-")
        srv.add_carte(2, "A", "a", "-")

        list = repo.get_all()
        sort.comb_sort(list, key = lambda x: x.get_id())

        assert list == [carte1, carte2, carte3, carte4]