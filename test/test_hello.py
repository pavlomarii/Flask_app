import http

from wsgi import app


def test_hello():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == http.HTTPStatus.OK
