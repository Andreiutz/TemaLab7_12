from Testing.test import Tests

from Repository.client_repository import ClientRepository
from Repository.carte_repository import CarteRepository
from Repository.enrollmen_repository import EnrollmentRepository
from Repository.carte_repository_file import CarteRepositoryFile
from Repository.client_repository_file import ClientRepositoryFile
from Repository.enrollment_repository_file import EnrollmentRepositoryFile

from Validation.client_validator import ClientValidator
from Validation.carte_validator import CarteValidator
from Validation.enroll_validator import EnrollmentValidator

from Service.client_service import ClientService
from Service.carte_service import CarteService
from Service.enrollment_service import EnrollmentService

from Console.ui import Console

teste = Tests()
# repo_client = ClientRepository()
# repo_carte = CarteRepository()
# repo_enroll = EnrollmentRepository()

repo_carte_file = CarteRepositoryFile("Text_Files/carte_file.txt")
repo_client_file = ClientRepositoryFile("Text_Files/client_file.txt")
repo_enroll_file = EnrollmentRepositoryFile("Text_Files/enroll_file.txt")

valid_client = ClientValidator()
valid_carte = CarteValidator()
valid_enroll = EnrollmentValidator()

service_client = ClientService(valid_client, repo_client_file)
service_carte = CarteService(valid_carte, repo_carte_file)
service_enroll = EnrollmentService(valid_enroll, repo_enroll_file, repo_client_file, repo_carte_file)

console = Console(service_client, service_carte, service_enroll)

teste.run_all_tests()

console.run()
