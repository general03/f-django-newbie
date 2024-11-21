def test_health_check(client):
    """ > pipenv run pytest --ds=weather.settings """
    assert b'{"status": "ok"}' == client.get('/health/').content

def test_app_settings(settings):
    assert "sun" in settings.INSTALLED_APPS