def test_health_check(client):
    """ > pipenv run pytest --ds=weather.settings """
    assert b'{"status": "ok"}' == client.get('/health/').content
