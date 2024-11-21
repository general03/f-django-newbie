from sun.models import Sun
import pytest

def test_health_check(client):
    """ > pipenv run pytest --ds=weather.settings """
    assert b'{"status": "ok"}' == client.get('/health/').content

def test_app_settings(settings):
    assert "sun" in settings.INSTALLED_APPS

@pytest.mark.django_db
def test_django_db_sun_country_fr(init_data):
    assert Sun.objects.filter(country="Paris")
