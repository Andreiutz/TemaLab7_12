class ClientCartiRaportDto:
    def __init__(self, id_client, nume_client, lista_carti):
        self.__id_client = id_client
        self.__nume_client = nume_client
        self.__lista_carti = lista_carti

    def __str__(self):
        s = ""
        s += f"Clientul cu id-ul {self.__id_client}) {self.__nume_client}:\n"
        for i, carte in enumerate(self.__lista_carti):
            s += f"{i}) {carte} \n"
        return s

    def get_id_client(self):
        return self.__id_client

    def get_nume_client(self):
        return self.__nume_client

    def get_lista_carti(self):
        return self.__lista_carti