import unittest
from Domain.client import Client
from Repository.client_repository_file import ClientRepositoryFile
from Repository.client_repository import ClientRepository
from Validation.client_validator import ClientValidator
from Service.client_service import ClientService

class TestClient(unittest.TestCase):
    '''CONSTRUCTOR'''
    def test_eq(self):
        client1 = Client(1, "Andrei", "1234")
        client2 = Client(1, "Andrei", "1234")
        client3 = Client(2, "Andrei", "1234")

        self.assertEqual(client1,client2)
        self.assertNotEqual(client2, client3)


    '''REPOSITORY'''
    def test_add_client(self):

        with open("test_clienti.txt", "w") as f:
            f.write("")

        #repo_client = ClientRepository()
        repo_client = ClientRepositoryFile("test_clienti.txt")
        assert (len(repo_client) == 0)
        repo_client.add_client(Client(1, "Andrei", "1234"))
        assert (len(repo_client) == 1)

        try:
            repo_client.add_client(Client(1, "Andrei", "1234"))
            assert False
        except Exception as ex:
            assert (str(ex) == "id-ul exista deja!\n")

    def test_delete_client(self):
        with open("test_clienti.txt", "w") as f:
            f.write("")

        #repo_client = ClientRepository()
        repo_client = ClientRepositoryFile("test_clienti.txt")

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

    def test_modify_client(self):
        with open("test_clienti.txt", "w") as f:
            f.write("")

        #repo_client = ClientRepository()
        repo_client = ClientRepositoryFile("test_clienti.txt")
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

    def test_get_client(self):
        with open("test_clienti.txt", "w") as f:
            f.write("")

        #repo_client = ClientRepository()
        repo_client = ClientRepositoryFile("test_clienti.txt")
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

    '''VALIDARE'''
    def test_validare_date(self):
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


    '''SERVICE'''
    def test_add_client_service(self):
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

    def test_modificare_client(self):
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



