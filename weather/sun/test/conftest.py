import pytest 
from sun.models import Sun

@pytest.fixture
def init_data():
    print("***********TEARUP DATA SUN***********")
    Sun.objects.create(country="Paris")

    yield

    print("***********TEARDOWN DATA SUN***********")
    Sun.objects.all().delete()