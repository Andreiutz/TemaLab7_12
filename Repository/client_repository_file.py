from Repository.client_repository import ClientRepository
from Domain.client import Client

class ClientRepositoryFile(ClientRepository):

    def __init__(self, path_name):
        self.__path_name = path_name
        ClientRepository.__init__(self)

    def __len__(self):
        self.__read_all_from_file()
        return ClientRepository.__len__(self)

    def __read_all_from_file(self):
        with open(self.__path_name, "r") as f:
            self._repo_clienti = []
            lines = f.readlines()
            for line in lines:
                if len(line) != 0:
                    line = line.strip()
                    parts = line.split(",")
                    id_client = int(parts[0])
                    nume_client = parts[1]
                    cnp_client = parts[2]
                    client = Client(id_client, nume_client, cnp_client)
                    self._repo_clienti.append(client)


    def __write_all_to_file(self):
        with open(self.__path_name, "w") as f:
            for client in self._repo_clienti:
                f.write(f"{str(client.get_id())},{client.get_nume()},{client.get_cnp()}\n")

    def __add_to_file(self, client):
        with open(self.__path_name, "a") as f:
            f.write(f"{str(client.get_id())},{client.get_nume()},{client.get_cnp()}\n")

    def add_client(self, client_nou):
        self.__read_all_from_file()
        ClientRepository.add_client(self, client_nou)
        self.__add_to_file(client_nou)

    def delete_client(self, id_client):
        self.__read_all_from_file()
        ClientRepository.delete_client(self, id_client)
        self.__write_all_to_file()

    def modify_client(self, client_nou):
        self.__read_all_from_file()
        ClientRepository.modify_client(self, client_nou)
        self.__write_all_to_file()

    def get_all(self):
        self.__read_all_from_file()
        return ClientRepository.get_all(self)

    def get_client(self, id_client):
        self.__read_all_from_file()
        return ClientRepository.get_client(self, id_client)
