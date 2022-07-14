from factory.django import DjangoModelFactory
from factory import Faker
from django.contrib.auth.models import User
from django.utils import timezone

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    password = Faker('md5')
    last_login = Faker('date_time', tzinfo = timezone.get_current_timezone())
    is_superuser = Faker('pybool')
    username = Faker('user_name')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')
    is_staff = Faker('pybool')
    is_active = True
    date_joined = Faker('date_time', tzinfo = timezone.get_current_timezone())
