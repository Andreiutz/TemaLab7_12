from Domain.enrollment import Enrollment
from Domain.carte_frecventa_dto import CarteFrecventaDto
from Domain.client_carti_raport_dto import ClientCartiRaportDto
from Domain.client_frecventa_dto import ClientFrecventaDto
from Domain.carte import Carte

class EnrollmentService():
    def __init__(self, validator_enroll, repo_enroll, repo_client, repo_carte):
        self.__validator_enroll = validator_enroll
        self.__repo_enroll = repo_enroll
        self.__repo_client = repo_client
        self.__repo_carte = repo_carte

    def get_all(self):
        return self.__repo_enroll.get_all()

    def add_enrollment(self, id_enrollment, id_client, id_carte):
        '''
        Functia adauga legatura dintre clientul cu id-ul id_client si cartea cu id-ul
        id_carte
        returneaza eroare daca id_client sau id_carte nu exista
        :param id_enrollment:
        :param id_client:
        :param id_carte:
        :return:
        '''
        self.__validator_enroll.validare_date(id_enrollment, id_client, id_carte, self.__repo_client, self.__repo_carte)
        new_enrollment = Enrollment(id_enrollment, id_client, id_carte, 1)
        self.__repo_enroll.add_enrollment(new_enrollment)
        carte = self.__repo_carte.get_carte(id_carte)
        id_carte = carte.get_id()
        titlu = carte.get_titlu()
        autor = carte.get_autor()
        descriere = carte.get_descriere()
        carte_noua = Carte(id_carte, titlu, autor, descriere, 1)
        self.__repo_carte.modify_carte(carte_noua)

    def remove_enrollment(self, id_enrollment):
        '''
        Functia dezactiveaza enrollment-ul cu id-ul enrollment
        :param id_enrollment:
        :return:
        '''

        self.__repo_enroll.delete_enrollment(id_enrollment)
        enroll = self.__repo_enroll.get_enrollment(id_enrollment)
        id_carte = enroll.get_id_carte()
        carte = self.__repo_carte.get_carte(id_carte)
        id_carte = carte.get_id()
        titlu = carte.get_titlu()
        autor = carte.get_autor()
        descriere = carte.get_descriere()
        carte_noua = Carte(id_carte, titlu, autor, descriere, 0)
        self.__repo_carte.modify_carte(carte_noua)

    def get_top_3(self):
        '''
        Functia returneaza primele 3 cele mai inchiriate carti
        :return:
        '''
        inchirieri = self.__repo_enroll.get_all()
        situatie_carti = {}
        for inchiriere in inchirieri:
            id_carte = inchiriere.get_id_carte()
            if  id_carte not in situatie_carti:
                situatie_carti[id_carte] = 0
            situatie_carti[id_carte] += 1
        res = []
        for cheie_situatie_carte in situatie_carti:
            nume_carte = self.__repo_carte.get_carte(cheie_situatie_carte).get_titlu()
            frecv = situatie_carti[cheie_situatie_carte]
            carte_frecv_dto = CarteFrecventaDto(nume_carte, frecv)
            res.append(carte_frecv_dto)

        res.sort(key = lambda x: x.get_frecventa(), reverse = True)

        return res[:3]

    def cele_mai_inchiriate_carti(self):
        '''
        Functia returneaza cele mai inchiriate carti
        :return:
        '''
        if len(self.__repo_enroll) == 0: raise Exception("nu exista inchirieri salvate!\n")
        inchirieri = self.__repo_enroll.get_all()
        situatie_carti = {}
        for inchiriere in inchirieri:
            id_carte = inchiriere.get_id_carte()
            if id_carte not in situatie_carti:
                situatie_carti[id_carte] = 0
            situatie_carti[id_carte] += 1

        res = []
        for cheie_situatie_carte in situatie_carti:
            nume_carte = self.__repo_carte.get_carte(cheie_situatie_carte).get_titlu()
            frecv = situatie_carti[cheie_situatie_carte]
            carte_frecv_dto = CarteFrecventaDto(nume_carte, frecv)
            res.append(carte_frecv_dto)

        res.sort(key = lambda x: x.get_frecventa(), reverse = True)

        final_res = []
        fr_max = res[0].get_frecventa()
        i = 0
        while (i < len(res) and res[i].get_frecventa() == fr_max):
            final_res.append(res[i])
            i += 1
        return final_res

    def raport_clienti_carti(self):
        '''
        Functia returneaza lista sortata cu clientii si cartile inchiriate
        :return:
        '''
        situatie_biblioteca = {}
        inchirieri = self.__repo_enroll.get_all()
        for inchiriere in inchirieri:
            if inchiriere.get_status():
                id_client = inchiriere.get_id_client()
                id_carte = inchiriere.get_id_carte()
                if id_client not in situatie_biblioteca:
                    situatie_biblioteca[id_client] = []
                situatie_biblioteca[id_client].append(self.__repo_carte.get_carte(id_carte).get_titlu())
        res = []
        for cheie_client in situatie_biblioteca:
            lista_carti = situatie_biblioteca[cheie_client]
            id_client = cheie_client
            nume_client = self.__repo_client.get_client(id_client).get_nume()
            odt = ClientCartiRaportDto(id_client, nume_client, lista_carti)
            res.append(odt)

        res.sort(key = lambda x: (x.get_nume_client(), len(x.get_lista_carti())))
        return res

    def top20(self):
        '''
        Functia returneaza 20% cei mai activi clienti
        :return:
        '''
        situatie_clienti = {}
        inchirieri = self.__repo_enroll.get_all()
        for inchiriere in inchirieri:
            id_client = inchiriere.get_id_client()
            if id_client not in situatie_clienti:
                situatie_clienti[id_client] = 0
            situatie_clienti[id_client] += 1
        res = []
        for cheie in situatie_clienti:
            nume_client = self.__repo_client.get_client(cheie).get_nume()
            frecventa = situatie_clienti[cheie]
            rap_cl = ClientFrecventaDto(nume_client, frecventa)
            res.append(rap_cl)
        res.sort(key = lambda x: x.get_frecventa(), reverse=True)
        return res[:(len(res)-1)//5+1]

    def delete_carte(self, id_carte):
        '''
        Functia sterge din repository cartea cu id-ul id_carte
        Se sterg toate legaturile active ce contin cartea cu id-ul id_carte
        :param id_carte:
        :return:
        '''
        inchirieri = self.__repo_enroll.get_all()
        for inchiriere in inchirieri:
            if inchiriere.get_id_carte() == id_carte and inchiriere.get_status():
                self.__repo_enroll.delete_enrollment(inchiriere.get_id())
        self.__repo_carte.delete_carte(id_carte)

    def delete_client(self, id_client):
        '''
        Functia sterge din repository clientul cu id-ul id_client
        Se sterg toate legaturile active ce contin clientul cu id-ul id_client
        :param id_client:
        :return:
        '''
        inchirieri = self.__repo_enroll.get_all()
        for inchiriere in inchirieri:
            if inchiriere.get_id_client() == id_client and inchiriere.get_status():
                self.__repo_enroll.delete_enrollment(inchiriere.get_id())
                id_carte = inchiriere.get_id_carte()
                self.__repo_carte.get_carte(id_carte).set_status = False
        self.__repo_client.delete_client(id_client)

