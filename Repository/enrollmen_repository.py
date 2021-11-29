class EnrollmentRepository():
    def __init__(self):
        self._repo_enrollment = []

    def __len__(self):
        return len(self._repo_enrollment)

    def add_enrollment(self, enrollment):
        for enroll in self._repo_enrollment:
            if enroll.get_id() == enrollment.get_id():
                raise Exception("id-ul exista deja!\n")
            if enroll.get_id_client() == enrollment.get_id_client() and enroll.get_id_carte() == enrollment.get_id_carte() and enroll.get_status():
                raise Exception("clientul are deja aceasta carte!\n")
        self._repo_enrollment.append(enrollment)

    def delete_enrollment(self, id_enroll):
        for enroll in self._repo_enrollment:
            if enroll.get_id() == id_enroll and enroll.get_status():
                enroll.cancel_enrollment()
                return
        raise Exception("inchirierea nu exista!\n")

    def get_all(self):
        return self._repo_enrollment

    def get_enrollment(self, id_enrollment):
        for enroll in self._repo_enrollment:
            if enroll.get_id() == id_enrollment:
                return enroll
        raise Exception("id invalid!\n")