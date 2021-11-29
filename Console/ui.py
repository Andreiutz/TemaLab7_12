class Console():

    def __init__(self, client_service, carte_service, enroll_service):
        self.__client_service = client_service
        self.__carte_service = carte_service
        self.__enroll_service = enroll_service

    def __ui_print_main_options(self):
        print("")
        print("___Meniu Optiuni___")
        print("1) 'client'")
        print("2) 'carte'")
        print("3) 'statistici'")
        print("4) 'exit'")
        print("")

    def __ui_print_optiuni_client(self):
        print("")
        print("___Optiuni Client___")
        print("1) 'adauga_client'")
        print("2) 'sterge_client'")
        print("3) 'afisare_clienti'")
        print("4) 'generare_clienti'")
        print("5) 'modificare_date'")
        print("6) 'cautare_client'")
        print("7) 'inchiriere_carte'")
        print("8) 'returnare_carte'")
        print("X) 'exit'")
        print("")

    def __ui_print_optiuni_carte(self):
        print("")
        print("__Optiuni Carte___")
        print("1) 'adauga_carte'")
        print("2) 'sterge_carte'")
        print("3) 'afisare_carti'")
        print("4) 'modificare_carte'")
        print("X) 'exit'")
        print("")

    def __ui_print_optiuni_statistici(self):
        print("")
        print("___Optiuni Statistici___")
        print("1) 'afisare_inchirieri'      - afisare inchirieri active")
        print("2) 'max_inch_carti")
        print("3) 'top_trei_carti'")
        print("4) 'clienti_carti'           - afisare lista clienti cu carti inchiriate sortati dupa nume")
        print("5) 'top20'                   - top 20% cei mai activi clienti")
        print("X) 'exit'")
        print("")

    '''CLIENT'''
    def __UI_CLIENT(self):
        while True:
            self.__ui_print_optiuni_client()
            cmd = input(">>>")
            if cmd == "adauga_client":
                self.__ui_adauga_client()
            elif cmd == "sterge_client":
                self.__ui_sterge_client()
            elif cmd == "afisare_clienti":
                self.__ui_afisare_clienti()
            elif cmd == "generare_clienti":
                self.__ui_generare_clienti()
            elif cmd == "modificare_date":
                self.__ui_modificare_date()
            elif cmd == "cautare_client":
                pass
            elif cmd == "inchiriere_carte":
                self.__ui_inchiriere_carte()
            elif cmd == "returnare_carte":
                self.__ui_returnare_carte()
            elif cmd == "exit":
                return
            else:
                print("comanda invalida!\n")

    def __ui_adauga_client(self):
        try:
            id_client = int(input("id client: "))
        except ValueError:
            print("id invalid!\n")
            return
        nume_client = input("nume client: ")
        cnp_client = input("cnp client: ")
        try:
            self.__client_service.add_client(id_client, nume_client, cnp_client)
        except Exception as ex:
            print(ex)
            return
        print("client adaugat!\n")

    def __ui_sterge_client(self):
        try:
            id_client = int(input("id client: "))
        except ValueError:
            print("id client invalid!\n")
            return
        try:
            self.__enroll_service.delete_client(id_client)
        except Exception as ex:
            print(ex)
            return
        print("client sters!\n")

    def __ui_afisare_clienti(self):
        for client in self.__client_service.get_all():
            print(client)

    def __ui_generare_clienti(self):
        try:
            n = int(input("numar clienti: "))
        except ValueError:
            print("numar invalid!\n")
            return
        try:
            self.__client_service.generare_clienti(n)
        except Exception as ex:
            print(ex)
            return
        print("adaugati!\n")

    def __ui_modificare_date(self):
        try:
            id_client = int(input("id client: "))
        except ValueError:
            print("id invalid!\n")
            return
        print("Modificati: \n 'nume' \n 'cnp'")
        cmd = input(">>>")
        new_data = input("Valoarea noua: ")
        try:
            self.__client_service.modificare_client(id_client, cmd, new_data)
        except Exception as ex:
            print(ex)
            return
        print("modificare reusita!\n")

    def __ui_cautare_client(self):
        pass

    def __ui_inchiriere_carte(self):
        try:
            id_enrollment = int(input("id inchiriere: "))
        except ValueError:
            print("id inchiriere invalid!\n")
            return
        try:
            id_client = int(input("id client: "))
        except ValueError:
            print("id client invalid!\n")
            return
        try:
            id_carte = int(input("id carte: "))
        except ValueError:
            print("id carte invalid!\n")
            return
        try:
            self.__enroll_service.add_enrollment(id_enrollment, id_client, id_carte)
        except Exception as ex:
            print(ex)
            return
        print("Inchiriere salvata!\n")

    def __ui_returnare_carte(self):
        try:
            id_enroll = int(input("id legatura: "))
        except ValueError:
            print("id-ul legaturii invalid!\n")
            return
        try:
            self.__enroll_service.remove_enrollment(id_enroll)
        except Exception as ex:
            print(ex)
            return
        print("inchiriere stearsa!\n")

    '''CARTE'''
    def __UI_CARTE(self):
        while True:
            self.__ui_print_optiuni_carte()
            cmd = input(">>>")
            if cmd == "adauga_carte":
                self.__ui_adauga_carte()
            elif cmd == "sterge_carte":
                self.__ui_sterge_carte()
            elif cmd == "afisare_carti":
                self.__ui_afisare_carti()
            elif cmd == "modificare_carte":
                self.__ui_modificare_carte()
            elif cmd == "exit":
                return
            else: print("comanda invalida!\n")

    def __ui_adauga_carte(self):
        try:
            id_carte = int(input("id carte: "))
        except ValueError:
            print("id invalid!\n")
            return
        titlu = input("titlu: ")
        autor = input("autor: ")
        descriere = input("descriere: ")

        try:
            self.__carte_service.add_carte(id_carte, titlu, autor, descriere)
        except Exception as ex:
            print(ex)
            return
        print("carte adaugata!\n")

    def __ui_afisare_carti(self):
        for carte in self.__carte_service.get_all():
            print(carte)

    def __ui_modificare_carte(self):
        try:
            id_carte = int(input("id carte: "))
        except ValueError:
            print("id invalid!\n")
            return
        print("Modificati: \n 'titlu' \n 'autor' \n 'descriere'")
        cmd = input(">>>")
        new_data = input("Valoare noua: ")
        try:
            self.__carte_service.modify_carte(id_carte, cmd, new_data)
        except Exception as ex:
            print(ex)
            return
        print("modificare reusita!\n")

    def __ui_sterge_carte(self):
        try:
            id_carte = int(input("id carte: "))
        except ValueError:
            print("id invalid!\n")
            return
        try:
            self.__enroll_service.delete_carte(id_carte)
        except Exception as ex:
            print(ex)
            return
        print("carte stearsa!\n")

    '''STATS'''

    def __UI_STATS(self):
        while True:
            self.__ui_print_optiuni_statistici()
            cmd = input(">>>")
            if cmd == "afisare_inchirieri":
                self.__ui_afisare_inchirieri()
            elif cmd == "top_trei_carti":
                self.__ui_top_trei_carti()
            elif cmd == "max_inch_carti":
                self.__ui_max_inch_carti()
            elif cmd == "clienti_carti":
                self.__ui_clienti_carti_sortat()
            elif cmd == "top20":
                self.__ui_top20()
            elif cmd == "exit":
                return
            else: print("comanda invalida!\n")

    def __ui_afisare_inchirieri(self):
        enroll_list = self.__enroll_service.get_all()
        for en in enroll_list:
            if en.get_status():
                print(en)

    def __ui_top_trei_carti(self):
        top_3 = self.__enroll_service.get_top_3()
        for carte in top_3:
            print(carte)

    def __ui_max_inch_carti(self):
        try:
            list = self.__enroll_service.cele_mai_inchiriate_carti()
        except Exception as ex:
            print(ex)
            return
        for elem in list:
            print(elem)

    def __ui_clienti_carti_sortat(self):
        list = self.__enroll_service.raport_clienti_carti()
        if len(list) == 0:
            print("nu exista date!\n")
            return
        for elem in list:
            print(elem)

    def __ui_top20(self):
        list = self.__enroll_service.top20()
        if len(list) == 0:
            print("nu exista date!\n")
            return
        for elem in list:
            print(elem)

    def run(self):
        while True:
            self.__ui_print_main_options()
            cmd = input(">>>")
            if cmd == "client":
                self.__UI_CLIENT()
            elif cmd == "carte":
                self.__UI_CARTE()
            elif cmd == "statistici":
                self.__UI_STATS()
            elif cmd == "exit":
                return
            else:
                print("comanda invalida!\n")



