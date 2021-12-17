from Domain.carte import Carte
from Sorting_Algorithms.sort_algorithms import SortAlg

class CarteService():

    def __init__(self, carte_validator, carte_repository):
        self.__carte_validator = carte_validator
        self.__carte_repository = carte_repository

    def __len__(self):
        return len(self.__carte_repository)

    def get_all(self):
        return self.__carte_repository.get_all()

    def add_carte(self, id_carte, titlu, autor, descriere):
        '''
        Functia adauga in lista o carte cu datele introduse, daca sunt corecte
        altfel returneaza eroare
        :param id_carte: numar intreg pozitiv
        :param titlu: string nevid
        :param autor: string nevid
        :param descriere: string nevid
        :return:
        '''
        self.__carte_validator.validare_date(id_carte, titlu, autor, descriere)
        carte_noua = Carte(id_carte, titlu, autor, descriere, 0)
        self.__carte_repository.add_carte(carte_noua)

    def modify_carte(self, id_carte, param, new_data):
        '''
        Functia modifica un parametru al cartii cu id-ul id_carte in fucntie de
        valoarea parametrului param
        :param id_carte:
        :param param:
        :param new_data:
        :return:
        '''
        carte = self.__carte_repository.get_carte(id_carte)
        titlu = carte.get_titlu()
        autor = carte.get_autor()
        descriere = carte.get_descriere()
        status = carte.get_status_carte()
        if param == "titlu": titlu = new_data
        elif param == "autor": autor = new_data
        elif param == "descriere": descriere = new_data
        else: raise Exception("comanda invalida!\n")
        self.__carte_validator.validare_date(id_carte, titlu, autor, descriere)
        new_carte = Carte(id_carte, titlu, autor, descriere, status)
        self.__carte_repository.modify_carte(new_carte)

    def sort_carti(self, reverse):
        '''
        Functia sorteaza lista cartilor in functie de id
        daca reverse = True, o sorteaza descrescator, altfel crescator
        :return:
        '''
        sort = SortAlg()
        repo = self.__carte_repository.get_all()
        sort.insertion_sort(repo, key = lambda x: x.get_id())
        return repo
