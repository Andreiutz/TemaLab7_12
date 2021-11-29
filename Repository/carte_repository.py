class CarteRepository:
    def __init__(self):
        self._repo_carti = []

    def __len__(self):
        return len(self._repo_carti)

    def add_carte(self, carte_noua):
        '''
        Functia adauga in repository cartea carte_noua, doar daca aceasta nu se afla deja in repo
        :param carte_noua: cartea noua care se adauga in repo
        :return: -
        :raise: "id-ul exista deja!\n", daca id-ul cartii carte_noua se afla deja in repo
                "cartea cu acest nume si acest autor exista deja!\n", daca titlul si autorul cartii
                carte_noua se afla deja in repo
        '''
        err = ""
        for carte in self._repo_carti:
            if carte.get_id() == carte_noua.get_id():
                err += "id-ul exista deja!\n"
        if len(err) > 0:
            raise Exception(err)
        self._repo_carti.append(carte_noua)

    def delete_carte(self, id_carte):
        for i, carte in enumerate(self._repo_carti):
            if carte.get_id() == id_carte:
                del(self._repo_carti[i])
                return
        raise Exception("id-ul nu exista!\n")

    def modify_carte(self, carte_noua):
        for i, carte in enumerate(self._repo_carti):
            if carte.get_id() == carte_noua.get_id():
                self._repo_carti[i] = carte_noua
                return
        raise Exception("cartea nu a fost gasita!\n")

    def get_all(self):
        return self._repo_carti

    def get_carte(self, id_carte):
        for carte in self._repo_carti:
            if carte.get_id() == id_carte:
                return carte
        raise Exception("id-ul nu exista!\n")
