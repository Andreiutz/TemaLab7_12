import unittest

from Domain.enrollment import Enrollment

from Repository.carte_repository_file import CarteRepositoryFile
from Repository.client_repository_file import ClientRepositoryFile
from Repository.enrollment_repository_file import EnrollmentRepositoryFile
from Repository.client_repository import ClientRepository
from Repository.carte_repository import CarteRepository
from Repository.enrollmen_repository import EnrollmentRepository

from Validation.client_validator import ClientValidator
from Validation.carte_validator import CarteValidator
from Validation.enroll_validator import EnrollmentValidator

from Service.client_service import ClientService
from Service.carte_service import CarteService
from Service.enrollment_service import EnrollmentService

class EnrollmentTest(unittest.TestCase):

    '''
    REPOSITORY
    '''
    def test_add_enrollment(self):
        with open("test_enroll.txt", "w") as f:
            f.write("")
        #repo_enroll = EnrollmentRepository()
        repo_enroll = EnrollmentRepositoryFile("test_enroll.txt")
        repo_enroll.add_enrollment(Enrollment(1, 1, 1, 1))
        repo_enroll.add_enrollment(Enrollment(2, 1, 2, 1))
        repo_enroll.add_enrollment(Enrollment(3, 1, 3, 1))
        try:
            repo_enroll.add_enrollment(Enrollment(1, 2, 3, 1))
            assert False
        except Exception as ex:
            assert (str(ex) == "id-ul exista deja!\n")

        try:
            repo_enroll.add_enrollment(Enrollment(4, 1, 1, 1))
            assert False
        except Exception as ex:
            assert str(ex) == "clientul are deja aceasta carte!\n"


    def test_delete_enrollment(self):
        with open("test_enroll.txt", "w") as f:
            f.write("")
        # repo_enroll = EnrollmentRepository()
        repo_enroll = EnrollmentRepositoryFile("test_enroll.txt")
        repo_enroll.add_enrollment(Enrollment(1, 1, 1, 1))
        repo_enroll.add_enrollment(Enrollment(2, 1, 4, 1))
        repo_enroll.add_enrollment(Enrollment(3, 1, 2, 1))
        repo_enroll.add_enrollment(Enrollment(4, 1, 3, 1))

        repo_enroll.delete_enrollment(1)
        try:
            repo_enroll.delete_enrollment(1)
            assert False
        except Exception as ex:
            assert str(ex) == "inchirierea nu exista!\n"

        try:
            repo_enroll.delete_enrollment(5)
            assert False
        except Exception as ex:
            assert str(ex) == "inchirierea nu exista!\n"


    '''SERVICE'''
    def test_add_enrollment(self):
        valid_carte = CarteValidator()
        valid_client = ClientValidator()
        valid_enroll = EnrollmentValidator()

        repo_carte = CarteRepository()
        repo_client = ClientRepository()
        repo_enroll = EnrollmentRepository()

        srv_carte = CarteService(valid_carte, repo_carte)
        srv_client = ClientService(valid_client, repo_client)
        srv_enroll = EnrollmentService(valid_enroll, repo_enroll,  repo_client, repo_carte)

        srv_client.add_client(1, "Andrei", "1234")
        srv_client.add_client(2, "Dorin", "2345")
        srv_client.add_client(3, "Edi", "5594")

        srv_carte.add_carte(1, "AAA", "aaa", "---")
        srv_carte.add_carte(2, "BBB", "bbb", "---")
        srv_carte.add_carte(3, "CCC", "ccc", "---")

        srv_enroll.add_enrollment(1, 1, 1)
        srv_enroll.add_enrollment(2, 1, 2)
        try:
            srv_enroll.add_enrollment(3, 1, 1)
            assert False
        except Exception as ex:
            assert str(ex) == "cartea este inchiriata deja!\n"

        try:
            srv_enroll.add_enrollment(-1, -1, -1)
            assert False
        except Exception as ex:
            assert str(ex) == "id client invalid!\nid carte invalid!\nid inchiriere invalid!\n"


    def test_remove_enrollment(self):
        valid_carte = CarteValidator()
        valid_client = ClientValidator()
        valid_enroll = EnrollmentValidator()

        repo_carte = CarteRepository()
        repo_client = ClientRepository()
        repo_enroll = EnrollmentRepository()

        srv_carte = CarteService(valid_carte, repo_carte)
        srv_client = ClientService(valid_client, repo_client)
        srv_enroll = EnrollmentService(valid_enroll, repo_enroll, repo_client, repo_carte)

        srv_client.add_client(1, "Andrei", "1234")
        srv_client.add_client(2, "Dorin", "2345")
        srv_client.add_client(3, "Edi", "5594")

        srv_carte.add_carte(1, "AAA", "aaa", "---")
        srv_carte.add_carte(2, "BBB", "bbb", "---")
        srv_carte.add_carte(3, "CCC", "ccc", "---")

        srv_enroll.add_enrollment(1, 1, 1)
        srv_enroll.add_enrollment(2, 1, 2)

        srv_enroll.remove_enrollment(1)

        assert repo_enroll.get_all()[0].get_status() == False
        assert repo_enroll.get_all()[1].get_status() == True

        srv_enroll.remove_enrollment(2)

        assert repo_enroll.get_all()[0].get_status() == False
        assert repo_enroll.get_all()[0].get_status() == False


    def test_top_3(self):
        valid_carte = CarteValidator()
        valid_client = ClientValidator()
        valid_enroll = EnrollmentValidator()

        repo_carte = CarteRepository()
        repo_client = ClientRepository()
        repo_enroll = EnrollmentRepository()

        srv_carte = CarteService(valid_carte, repo_carte)
        srv_client = ClientService(valid_client, repo_client)
        srv_enroll = EnrollmentService(valid_enroll, repo_enroll, repo_client, repo_carte)

        srv_client.add_client(1, "Andrei", "1234")
        srv_client.add_client(2, "Dorin", "2345")
        srv_client.add_client(3, "Edi", "5594")
        srv_client.add_client(4, "EDD", "1111")
        srv_client.add_client(5, "EEE", "2222")

        srv_carte.add_carte(1, "AAA", "aaa", "---")
        srv_carte.add_carte(2, "BBB", "bbb", "---")
        srv_carte.add_carte(3, "CCC", "ccc", "---")
        srv_carte.add_carte(4, "DDD", "ddd", "---")
        srv_carte.add_carte(5, "EEE", "eee", "---")

        srv_enroll.add_enrollment(1, 1, 1)
        srv_enroll.remove_enrollment(1)
        srv_enroll.add_enrollment(2, 1, 2)
        srv_enroll.remove_enrollment(2)
        srv_enroll.add_enrollment(3, 2, 2)
        srv_enroll.remove_enrollment(3)
        srv_enroll.add_enrollment(4, 3, 2)
        srv_enroll.remove_enrollment(4)
        srv_enroll.add_enrollment(5, 4, 2)
        srv_enroll.remove_enrollment(5)
        srv_enroll.add_enrollment(6, 5, 2)
        srv_enroll.add_enrollment(7, 2, 1)
        srv_enroll.remove_enrollment(7)
        srv_enroll.add_enrollment(8, 3, 1)
        srv_enroll.remove_enrollment(8)
        srv_enroll.add_enrollment(9, 4, 1)
        srv_enroll.remove_enrollment(9)
        srv_enroll.add_enrollment(10, 4, 5)
        srv_enroll.remove_enrollment(10)
        srv_enroll.add_enrollment(11, 1, 5)

        res = srv_enroll.get_top_3()
        assert len(res) == 3

        assert res[0].get_frecventa() == 5
        assert res[0].get_nume_carte() == "BBB"

        assert res[1].get_frecventa() == 4
        assert res[1].get_nume_carte() == "AAA"

        assert res[2].get_frecventa() == 2
        assert res[2].get_nume_carte() == "EEE"


    def test_cele_mai_inchiriate_carti(self):
        valid_carte = CarteValidator()
        valid_client = ClientValidator()
        valid_enroll = EnrollmentValidator()

        repo_carte = CarteRepository()
        repo_client = ClientRepository()
        repo_enroll = EnrollmentRepository()

        srv_carte = CarteService(valid_carte, repo_carte)
        srv_client = ClientService(valid_client, repo_client)
        srv_enroll = EnrollmentService(valid_enroll, repo_enroll, repo_client, repo_carte)

        srv_client.add_client(1, "Andrei", "1234")
        srv_client.add_client(2, "Dorin", "2345")
        srv_client.add_client(3, "Edi", "5594")
        srv_client.add_client(4, "EDD", "1111")
        srv_client.add_client(5, "EEE", "2222")

        srv_carte.add_carte(1, "AAA", "aaa", "---")
        srv_carte.add_carte(2, "BBB", "bbb", "---")
        srv_carte.add_carte(3, "CCC", "ccc", "---")
        srv_carte.add_carte(4, "DDD", "ddd", "---")
        srv_carte.add_carte(5, "EEE", "eee", "---")

        srv_enroll.add_enrollment(1, 1, 1)
        srv_enroll.remove_enrollment(1)
        srv_enroll.add_enrollment(2, 1, 2)
        srv_enroll.remove_enrollment(2)
        srv_enroll.add_enrollment(3, 2, 2)
        srv_enroll.remove_enrollment(3)
        srv_enroll.add_enrollment(4, 3, 2)
        srv_enroll.remove_enrollment(4)
        srv_enroll.add_enrollment(5, 4, 2)
        srv_enroll.remove_enrollment(5)
        srv_enroll.add_enrollment(6, 5, 2)
        srv_enroll.add_enrollment(7, 2, 1)
        srv_enroll.remove_enrollment(7)
        srv_enroll.add_enrollment(8, 3, 1)
        srv_enroll.remove_enrollment(8)
        srv_enroll.add_enrollment(9, 4, 1)
        srv_enroll.remove_enrollment(9)
        srv_enroll.add_enrollment(10, 4, 5)
        srv_enroll.remove_enrollment(10)
        srv_enroll.add_enrollment(11, 1, 5)

        res = srv_enroll.cele_mai_inchiriate_carti()
        assert len(res) == 1
        assert res[0].get_nume_carte() == "BBB"


    def test_delete_carte(self):
        valid_carte = CarteValidator()
        valid_client = ClientValidator()
        valid_enroll = EnrollmentValidator()

        repo_carte = CarteRepository()
        repo_client = ClientRepository()
        repo_enroll = EnrollmentRepository()

        srv_carte = CarteService(valid_carte, repo_carte)
        srv_client = ClientService(valid_client, repo_client)
        srv_enroll = EnrollmentService(valid_enroll, repo_enroll, repo_client, repo_carte)

        srv_client.add_client(1, "Andrei", "1234")
        srv_client.add_client(2, "Dorin", "2345")
        srv_client.add_client(3, "Edi", "5594")
        srv_client.add_client(4, "EDD", "1111")
        srv_client.add_client(5, "EEE", "2222")

        srv_carte.add_carte(1, "AAA", "aaa", "---")
        srv_carte.add_carte(2, "BBB", "bbb", "---")
        srv_carte.add_carte(3, "CCC", "ccc", "---")
        srv_carte.add_carte(4, "DDD", "ddd", "---")
        srv_carte.add_carte(5, "EEE", "eee", "---")

        srv_enroll.add_enrollment(1, 1, 1)

        assert repo_enroll.get_all()[0].get_status() == True
        assert len(repo_carte) == 5
        srv_enroll.delete_carte(1)

        assert repo_enroll.get_all()[0].get_status() == False
        assert len(repo_carte) == 4


    def test_delete_client(self):
        valid_carte = CarteValidator()
        valid_client = ClientValidator()
        valid_enroll = EnrollmentValidator()

        repo_carte = CarteRepository()
        repo_client = ClientRepository()
        repo_enroll = EnrollmentRepository()

        srv_carte = CarteService(valid_carte, repo_carte)
        srv_client = ClientService(valid_client, repo_client)
        srv_enroll = EnrollmentService(valid_enroll, repo_enroll, repo_client, repo_carte)

        srv_client.add_client(1, "Andrei", "1234")
        srv_client.add_client(2, "Dorin", "2345")

        srv_carte.add_carte(1, "AAA", "aaa", "---")
        srv_carte.add_carte(2, "BBB", "bbb", "---")
        srv_carte.add_carte(3, "CCC", "ccc", "---")
        srv_carte.add_carte(4, "DDD", "ddd", "---")
        srv_carte.add_carte(5, "EEE", "eee", "---")

        srv_enroll.add_enrollment(1, 1, 1)
        srv_enroll.add_enrollment(2, 1, 2)
        srv_enroll.add_enrollment(3, 1, 3)
        srv_enroll.add_enrollment(4, 1, 4)
        srv_enroll.add_enrollment(5, 1, 5)

        assert len(srv_client) == 2
        assert repo_enroll.get_all()[3].get_status() == True

        srv_enroll.delete_client(1)

        assert len(srv_client) == 1
        assert repo_enroll.get_all()[3].get_status() == False


    def test_raport_clienti_carti(self):
        repo_client = ClientRepository()
        repo_carte = CarteRepository()
        repo_enroll = EnrollmentRepository()

        valid_client = ClientValidator()
        valid_carte = CarteValidator()
        valid_enroll = EnrollmentValidator()

        srv_client = ClientService(valid_client, repo_client)
        srv_carte = CarteService(valid_carte, repo_carte)
        srv_enroll = EnrollmentService(valid_enroll, repo_enroll, repo_client, repo_carte)

        srv_client.add_client(1, "Andrei", "1234")
        srv_client.add_client(2, "Dorin", "2345")
        srv_client.add_client(3, "E", "23445")

        srv_carte.add_carte(1, "AAA", "aaa", "---")
        srv_carte.add_carte(2, "BBB", "bbb", "---")
        srv_carte.add_carte(3, "CCC", "ccc", "---")
        srv_carte.add_carte(4, "DDD", "ddd", "---")
        srv_carte.add_carte(5, "EEE", "eee", "---")
        srv_carte.add_carte(6, "FFF", "fff", "---")
        srv_carte.add_carte(7, "GGG", "ggg", "---")
        srv_carte.add_carte(8, "HHH", "hhh", "---")
        srv_carte.add_carte(9, "III", "iii", "---")
        srv_carte.add_carte(10, "JJJ", "jjj", "---")

        srv_enroll.add_enrollment(1, 1, 1)
        srv_enroll.add_enrollment(2, 1, 2)
        srv_enroll.add_enrollment(3, 1, 3)
        srv_enroll.add_enrollment(4, 1, 4)
        srv_enroll.add_enrollment(5, 1, 5)
        srv_enroll.add_enrollment(6, 3, 6)
        srv_enroll.add_enrollment(7, 3, 7)
        srv_enroll.add_enrollment(8, 3, 8)
        srv_enroll.add_enrollment(9, 3, 9)
        srv_enroll.add_enrollment(10, 2, 10)

        odt = srv_enroll.raport_clienti_carti()

        assert len(odt) == 3
        assert len(odt[0].get_lista_carti()) == 5
        assert odt[0].get_nume_client() == "Andrei"

        assert len(odt[1].get_lista_carti()) == 1
        assert odt[1].get_nume_client() == "Dorin"


    def test_top20(self):
        repo_client = ClientRepository()
        repo_carte = CarteRepository()
        repo_enroll = EnrollmentRepository()

        valid_client = ClientValidator()
        valid_carte = CarteValidator()
        valid_enroll = EnrollmentValidator()

        srv_client = ClientService(valid_client, repo_client)
        srv_carte = CarteService(valid_carte, repo_carte)
        srv_enroll = EnrollmentService(valid_enroll, repo_enroll, repo_client, repo_carte)

        srv_client.add_client(1, "Andrei", "1234")
        srv_client.add_client(2, "Dorin", "2345")
        srv_client.add_client(3, "E", "23445")
        srv_client.add_client(4, "E", "23445")
        srv_client.add_client(5, "E", "23445")

        srv_carte.add_carte(1, "AAA", "aaa", "---")
        srv_carte.add_carte(2, "BBB", "bbb", "---")
        srv_carte.add_carte(3, "CCC", "ccc", "---")
        srv_carte.add_carte(4, "DDD", "ddd", "---")
        srv_carte.add_carte(5, "EEE", "eee", "---")
        srv_carte.add_carte(6, "FFF", "fff", "---")
        srv_carte.add_carte(7, "GGG", "ggg", "---")
        srv_carte.add_carte(8, "HHH", "hhh", "---")
        srv_carte.add_carte(9, "III", "iii", "---")
        srv_carte.add_carte(10, "JJJ", "jjj", "---")

        srv_enroll.add_enrollment(1, 3, 1)
        srv_enroll.add_enrollment(2, 1, 2)
        srv_enroll.add_enrollment(3, 1, 3)

        res = srv_enroll.top20()
        assert len(res) == 1
        assert res[0].get_nume() == "Andrei"