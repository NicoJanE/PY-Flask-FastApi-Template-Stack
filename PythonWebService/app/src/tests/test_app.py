# test_app.py

import pytest
from unittest.mock import patch
from app import app, get_hit_count, cache

@pytest.fixture
def app_client():
    app.testing = True
    return app.test_client()

@pytest.fixture
def test_data():
    return {'nm': 'testuser'}

def test_index(app_client):
    response = app_client.get('/')
    assert response.status_code == 200
    assert b'hostname' in response.data
    assert b'count' in response.data

def test_login_post(app_client, test_data):
    response = app_client.post('/login', data=test_data, follow_redirects=True)
    assert response.status_code == 200
    assert test_data['nm'] in response.data.decode('utf-8')

def test_login_get(app_client):
    response = app_client.get('/login')
    assert response.status_code == 200
    assert b'(None POST)' in response.data

def test_get_hit_count():
    with patch('redis.Redis') as mock_redis:
        mock_redis.incr.return_value = 1
        assert get_hit_count() == 1

def test_get_hit_count_redis_error():
    with patch('redis.Redis') as mock_redis:
        mock_redis.incr.side_effect = redis.exceptions.ConnectionError
        assert get_hit_count() == 'Redis Error'

def test_get_hit_count_other_error():
    with patch('redis.Redis') as mock_redis:
        mock_redis.incr.side_effect = Exception('test')
        assert get_hit_count() == 'Error'

# How to run these tests:
# 1. Install pytest: pip install pytest pytest-mock
# 2. Save this content as test_app.py
# 3. Run tests: pytest test_app.py -v
# 4. Run with coverage: pytest --cov=[module_name] test_app.py