from Domain.client import Client
from Domain.randomizer import Random

class ClientService():
    def __init__(self, client_validator, client_repository):
        self.__client_validator = client_validator
        self.__client_repository = client_repository

    def __len__(self):
        return len(self.__client_repository)

    def get_all(self):
        return self.__client_repository.get_all()

    def add_client(self, id_client, nume, cnp):
        '''
        Functia adauga in repo un client nou cu id_client, nume si cnp, daca datele
        sunt valide
        :param id_client: numar intreg, pozitiv
        :param nume: sir de caractere, nevid
        :param cnp: sir de caractere nevid, doar cifre
        :return:
        '''
        self.__client_validator.validare_date(id_client, nume, cnp)
        client_nou = Client(id_client, nume, cnp)
        self.__client_repository.add_client(client_nou)

    def modificare_client(self, id_client, param, new_data):
        '''
        Functia modifica unul din campurile clientului, in functie de param
        :param id_client: numar intreg pozitiv
        :param param: "nume" / "cnp"
        :param new_data: valoarea cu care se inlocuieste
        :return: -
        '''
        client = self.__client_repository.get_client(id_client)
        nume_client = client.get_nume()
        cnp_client = client.get_cnp()

        if param == "nume":
            nume_client = new_data
        elif param == "cnp":
            cnp_client = new_data
        else:
            raise Exception("comanda invalida!\n")

        self.__client_validator.validare_date(id_client, nume_client, cnp_client)
        client_nou = Client(id_client, nume_client, cnp_client)
        self.__client_repository.modify_client(client_nou)

    def generare_clienti(self, n):
        '''
        Functia genereaza aleatoriu n clienti
        :param n:
        :return:
        '''
        random = Random()
        while n:
            id_client = random.get_random_id()
            nume_client = random.get_random_nume()
            cnp_client = random.get_random_cnp()
            try:
                self.__client_validator.validare_date(id_client, nume_client, cnp_client)
                client_nou = Client(id_client, nume_client, cnp_client)
                self.__client_repository.add_client(client_nou)
                n -= 1
            except Exception as ex:
                pass
