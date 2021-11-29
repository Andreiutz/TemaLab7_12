class ClientRepository():
    def __init__(self):
        self._repo_clienti = []

    def __len__(self):
        return len(self._repo_clienti)

    def add_client(self, client_nou):
        err = ""
        for client in self._repo_clienti:
            if client.get_id() == client_nou.get_id():
                err += "id-ul exista deja!\n"
        if len(err) > 0:
            raise Exception(err)
        self._repo_clienti.append(client_nou)

    def delete_client(self, id_client):
        for i, client in enumerate(self._repo_clienti):
            if client.get_id() == id_client:
                del(self._repo_clienti[i])
                return
        raise Exception("id-ul nu exista!\n")

    def modify_client(self, client_nou):
        for i, client in enumerate(self._repo_clienti):
            if client.get_id() == client_nou.get_id():
                self._repo_clienti[i] = client_nou
                return
        raise Exception("Clientul nu a fost gasit!\n")

    def get_all(self):
        return self._repo_clienti

    def get_client(self, id_client):
        for client in self._repo_clienti:
            if client.get_id() == id_client:
                return client
        raise Exception("id-ul nu exista!\n")

