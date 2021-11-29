from Repository.carte_repository import CarteRepository
from Domain.carte import Carte


class CarteRepositoryFile(CarteRepository):

    def __init__(self, file_path):
        CarteRepository.__init__(self)
        self.__file_path = file_path

    def __len__(self):
        self.__read_all_from_file()
        return CarteRepository.__len__(self)

    def __read_all_from_file(self):
        with open(self.__file_path, "r") as f:
            self._repo_carti = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    parts = line.split(",")
                    id_carte = int(parts[0])
                    titlu_carte = parts[1]
                    autor_carte = parts[2]
                    descriere_carte = parts[3]
                    inchiriere = int(parts[4])
                    carte = Carte(id_carte, titlu_carte, autor_carte, descriere_carte, inchiriere)
                    self._repo_carti.append(carte)



    def __write_all_to_file(self):
        with open(self.__file_path, "w") as f:
            for carte in self._repo_carti:
                f.write(f"{str(carte.get_id())},{carte.get_titlu()},{carte.get_autor()},{carte.get_descriere()},{int(carte.get_status_carte())}\n")

    def __append_to_file(self, carte):
        with open(self.__file_path, "a") as f:
            f.write(f"{str(carte.get_id())},{carte.get_titlu()},{carte.get_autor()},{carte.get_descriere()},{int(carte.get_status_carte())}\n")

    def add_carte(self, carte_noua):
        self.__read_all_from_file()
        CarteRepository.add_carte(self, carte_noua)
        self.__append_to_file(carte_noua)

    def delete_carte(self, id_carte):
        self.__read_all_from_file()
        CarteRepository.delete_carte(self, id_carte)
        self.__write_all_to_file()

    def modify_carte(self, carte_noua):
        self.__read_all_from_file()
        CarteRepository.modify_carte(self, carte_noua)
        self.__write_all_to_file()

    def get_all(self):
        self.__read_all_from_file()
        return CarteRepository.get_all(self)

    def get_carte(self, id_carte):
        self.__read_all_from_file()
        return CarteRepository.get_carte(self, id_carte)
