from Domain.client import Client
from Domain.carte import Carte
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

class TestClient():

    def __test_eq(self):
        client1 = Client(1, "Andrei", "1234")
        client2 = Client(1, "Andrei", "1234")
        client3 = Client(2, "Andrei", "1234")

        assert (client1 == client2)
        assert (client2 != client3)

    def run_teste_client(self):
        self.__test_eq()

class TestRepoClienti():

    def __test_add_client(self):

        with open("Testing/test_clienti.txt", "w") as f:
            f.write("")

        #repo_client = ClientRepository()
        repo_client = ClientRepositoryFile("Testing/test_clienti.txt")
        assert (len(repo_client) == 0)
        repo_client.add_client(Client(1, "Andrei", "1234"))
        assert (len(repo_client) == 1)

        try:
            repo_client.add_client(Client(1, "Andrei", "1234"))
            assert False
        except Exception as ex:
            assert (str(ex) == "id-ul exista deja!\n")


    def __test_delete_client(self):
        with open("Testing/test_clienti.txt", "w") as f:
            f.write("")

        # repo_client = ClientRepository()
        repo_client = ClientRepositoryFile("Testing/test_clienti.txt")

        client1 = Client(1, "Andrei", "1234")
        client2 = Client(2, "Maria", "3234")
        client3 = Client(3, "Gigel", "2234")

        repo_client.add_client(client1)
        repo_client.add_client(client2)
        repo_client.add_client(client3)

        repo_client.delete_client(2)
        assert (len(repo_client) == 2)
        assert (repo_client.get_all() == [client1, client3])

        try:
            repo_client.delete_client(10)
            assert False
        except Exception as ex:
            assert (str(ex) == "id-ul nu exista!\n")

    def __test_modify_client(self):
        with open("Testing/test_clienti.txt", "w") as f:
            f.write("")

        #repo_client = ClientRepository()
        repo_client = ClientRepositoryFile("Testing/test_clienti.txt")
        client1 = Client(1, "Andrei", "1234")
        client2 = Client(2, "Maria", "3234")
        client3 = Client(3, "Gigel", "2234")

        client4 = Client(3, "Marcel", "9999")

        bad_client = Client(5, "MM", "11")

        repo_client.add_client(client1)
        repo_client.add_client(client2)
        repo_client.add_client(client3)
        repo_client.modify_client(client4)

        assert (repo_client.get_all() == [client1, client2, client4])

        try:
            repo_client.modify_client(bad_client)
            assert False
        except Exception as ex:
            assert (str(ex) == "Clientul nu a fost gasit!\n")

    def __test_get_client(self):
        with open("Testing/test_clienti.txt", "w") as f:
            f.write("")

        #repo_client = ClientRepository()
        repo_client = ClientRepositoryFile("Testing/test_clienti.txt")
        client1 = Client(1, "Andrei", "1234")
        client2 = Client(2, "Maria", "3234")
        client3 = Client(3, "Gigel", "2234")
        repo_client.add_client(client1)
        repo_client.add_client(client2)
        repo_client.add_client(client3)
        assert (repo_client.get_client(1) == client1)
        try:
            var = repo_client.get_client(4) == client2
            assert False
        except Exception as ex:
            assert (str(ex) == "id-ul nu exista!\n")


    def run_teste_repo_client(self):
        self.__test_add_client()
        self.__test_delete_client()
        self.__test_modify_client()
        self.__test_get_client()

class TestCarti():

    def __test_eq(self):
        carte1 = Carte(1, "Ion", "Len", "--",0)
        carte2 = Carte(1, "Ion", "Len", "--",0)
        carte3 = Carte(2, "Ion", "Len", "--",0)
        assert carte1 == carte2
        assert carte1 != carte3

    def run_teste_carte(self):
        self.__test_eq()

class TestRepoCarti():

    def __test_add_carte(self):
        with open("Testing/test_carti.txt", "w") as f:
            f.write("")
        #repo_carte = CarteRepository()
        repo_carte = CarteRepositoryFile("Testing/test_carti.txt")
        assert (len(repo_carte) == 0)
        repo_carte.add_carte(Carte(1, "Ion", "Reb", "--",0))
        assert (len(repo_carte) == 1)
        try:
            repo_carte.add_carte(Carte(1, "Ion", "Reb", "--",0))
            assert False
        except Exception as ex:
            assert (str(ex) == "id-ul exista deja!\n")

    def __test_delete_carte(self):
        with open("Testing/test_carti.txt", "w") as f:
            f.write("")

        carte1 = Carte(1, "AA", "aa", "--",0)
        carte2 = Carte(2, "BB", "bb", "--",0)
        carte3 = Carte(3, "CC", "cc", "--",0)

        #repo_carte = CarteRepository()
        repo_carte = CarteRepositoryFile("Testing/test_carti.txt")

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

    def __test_modify_carte(self):
        with open("Testing/test_carti.txt", "w") as f:
            f.write("")

        carte1 = Carte(1, "AA", "aa", "--",0)
        carte2 = Carte(2, "BB", "bb", "--",0)
        carte3 = Carte(3, "CC", "cc", "--",0)
        carte4 = Carte(3, "DD", "cc", "--",0)
        bad_carte = Carte(4, "CC", "cc", "--",0)

        #repo_carte = CarteRepository()
        repo_carte = CarteRepositoryFile("Testing/test_carti.txt")

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

    def __test_get_carte(self):
        with open("Testing/test_carti.txt", "w") as f:
            f.write("")

        carte1 = Carte(1, "AA", "aa", "--",0)
        carte2 = Carte(2, "BB", "bb", "--",0)
        carte3 = Carte(3, "CC", "cc", "--",0)

        #repo_carte = CarteRepository()
        repo_carte = CarteRepositoryFile("Testing/test_carti.txt")

        repo_carte.add_carte(carte1)
        repo_carte.add_carte(carte2)
        repo_carte.add_carte(carte3)

        assert repo_carte.get_carte(1) == carte1
        try:
            repo_carte.get_carte(5)
            assert False
        except Exception as ex:
            assert (str(ex) == "id-ul nu exista!\n")

    def run_teste_repo_carte(self):
         self.__test_add_carte()
         self.__test_delete_carte()
         self.__test_modify_carte()
         self.__test_get_carte()

class TestValidareClient():

    def __test_validare_date(self):
        validator_client = ClientValidator()
        id = 2
        nume = "Andrei"
        cnp = "1234"

        bad_id = -4
        bad_nume = ""
        bad_cnp = "abc4d"
        validator_client.validare_date(id, nume, cnp)
        try:
            validator_client.validare_date(bad_id, nume, cnp)
            assert False
        except Exception as ex:
            assert (str(ex) == "id invalid!\n")

        try:
            validator_client.validare_date(bad_id, bad_nume, bad_cnp)
            assert False
        except Exception as ex:
            assert (str(ex) == "id invalid!\nnume invalid!\ncnp invalid!\n")

    def run_teste_validare_client(self):
        self.__test_validare_date()

class TestValidareCarte():

    def __test_validare_date(self):
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

    def run_teste_validare_carte(self):
        self.__test_validare_date()

class TestRepoEnroll():

    def __test_add_enrollment(self):
        with open("Testing/test_enroll.txt", "w") as f:
            f.write("")
        #repo_enroll = EnrollmentRepository()
        repo_enroll = EnrollmentRepositoryFile("Testing/test_enroll.txt")
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

    def __test_delete_enrollment(self):
        with open("Testing/test_enroll.txt", "w") as f:
            f.write("")
        # repo_enroll = EnrollmentRepository()
        repo_enroll = EnrollmentRepositoryFile("Testing/test_enroll.txt")
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


    def run_teste_repo_enrollment(self):
        self.__test_add_enrollment()
        self.__test_delete_enrollment()

class TestEnrollService():

    def __test_add_enrollment(self):
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

    def __test_remove_enrollment(self):
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

    def __test_top_3(self):
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

    def __test_cele_mai_inchiriate_carti(self):
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

    def __test_delete_carte(self):
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

    def __test_delete_client(self):
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

    def __test_raport_clienti_carti(self):
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

    def __test_top20(self):
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

    def run_teste_enroll_service(self):
        self.__test_add_enrollment()
        self.__test_remove_enrollment()
        self.__test_top_3()
        self.__test_delete_carte()
        self.__test_delete_client()
        self.__test_cele_mai_inchiriate_carti()
        self.__test_raport_clienti_carti()
        self.__test_top20()

class TestClientService():

    def __test_add_client(self):
        valid = ClientValidator()
        repo = ClientRepository()
        srv = ClientService(valid, repo)

        srv.add_client(1, "Andrei", "1234")
        srv.add_client(2, "Ion", "2345")

        assert len(srv) == 2

        try:
            srv.add_client(1, "A", "11")
            assert False
        except Exception as ex:
            assert str(ex) == "id-ul exista deja!\n"

        try:
            srv.add_client(-1, "", "")
            assert False
        except Exception as ex:
            assert str(ex) == "id invalid!\nnume invalid!\ncnp invalid!\n"

    def __test_modificare_client(self):
        valid = ClientValidator()
        repo = ClientRepository()
        srv = ClientService(valid, repo)
        srv.add_client(1, "Andrei", "1234")

        srv.modificare_client(1, "nume", "Madalin")
        assert repo.get_client(1) == Client(1, "Madalin", "1234")
        try:
            srv.modificare_client(2, "Madalin", "1234")
            assert False
        except Exception as ex:
            assert str(ex) == "id-ul nu exista!\n"


    def run_teste_client_service(self):
        self.__test_add_client()
        self.__test_modificare_client()

class TestCarteService():

    def __test_add_carte(self):
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

    def __test_modify_carte(self):
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

    def run_teste_carte_service(self):
        self.__test_add_carte()
        self.__test_modify_carte()

class Tests():

    def __init__(self):
        self.__teste_client = TestClient()
        self.__teste_repo_client = TestRepoClienti()
        self.__teste_carte = TestCarti()
        self.__teste_repo_carte = TestRepoCarti()
        self.__teste_validator_client = TestValidareClient()
        self.__teste_validare_carte = TestValidareCarte()
        self.__teste_repo_enrollment = TestRepoEnroll()
        self.__teste_client_service = TestClientService()
        self.__teste_carte_service = TestCarteService()
        self.__teste_enroll_service = TestEnrollService()

    def run_all_tests(self):
        self.__teste_client.run_teste_client()
        self.__teste_repo_client.run_teste_repo_client()
        self.__teste_carte.run_teste_carte()
        self.__teste_repo_carte.run_teste_repo_carte()
        self.__teste_validator_client.run_teste_validare_client()
        self.__teste_validare_carte.run_teste_validare_carte()
        self.__teste_repo_enrollment.run_teste_repo_enrollment()
        self.__teste_client_service.run_teste_client_service()
        self.__teste_carte_service.run_teste_carte_service()
        self.__teste_enroll_service.run_teste_enroll_service()