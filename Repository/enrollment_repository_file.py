from Repository.enrollmen_repository import EnrollmentRepository
from Domain.enrollment import Enrollment


class EnrollmentRepositoryFile(EnrollmentRepository):

    def __init__(self, path_name):
        EnrollmentRepository.__init__(self)
        self.__path_name = path_name

    def __len__(self):
        return EnrollmentRepository.__len__(self)

    def __read_all_from_file(self):
        self._repo_enrollment = []
        with open(self.__path_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                if len(line) > 0:
                    line = line.strip()
                    parts = line.split(",")
                    id_enroll = int(parts[0])
                    id_client = int(parts[1])
                    id_carte = int(parts[2])
                    status_enroll = int(parts[3])
                    enroll = Enrollment(id_enroll, id_client, id_carte, status_enroll)
                    self._repo_enrollment.append(enroll)

    def __write_all_to_file(self):
        with open(self.__path_name, "w") as f:
            for enrollment in self._repo_enrollment:
                f.write(f"{str(enrollment.get_id())},{str(enrollment.get_id_client())},{str(enrollment.get_id_carte())},{str(enrollment.get_status())}\n")

    def __add_to_file(self, enrollment):
        with open(self.__path_name, "a") as f:
            f.write(
                f"{str(enrollment.get_id())},{str(enrollment.get_id_client())},{str(enrollment.get_id_carte())},{str(enrollment.get_status())}\n")

    def add_enrollment(self, enrollment):
        self.__read_all_from_file()
        EnrollmentRepository.add_enrollment(self, enrollment)
        self.__add_to_file(enrollment)

    def delete_enrollment(self, id_enroll):
        self.__read_all_from_file()
        EnrollmentRepository.delete_enrollment(self, id_enroll)
        self.__write_all_to_file()

    def get_all(self):
        self.__read_all_from_file()
        return EnrollmentRepository.get_all(self)

    def get_enrollment(self, id_enrollment):
        self.__read_all_from_file()
        return EnrollmentRepository.get_enrollment(self, id_enrollment)
