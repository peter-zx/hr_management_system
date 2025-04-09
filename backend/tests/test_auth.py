import pytest
from app import create_app
from app.extensions import db
from app.models.user import User

@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # 使用内存数据库
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()  # 初始化数据库
        yield testing_client
        with app.app_context():
            db.drop_all()  # 测试完毕后删除数据库

def test_register(test_client):
    response = test_client.post('/api/auth/register', json={
        'username': 'testuser',
        'password': 'testpassword',
        'role': 'admin'
    })
    assert response.status_code == 201
    assert b'User created' in response.data

def test_login(test_client):
    # 首先注册用户
    test_client.post('/api/auth/register', json={
        'username': 'testuser',
        'password': 'testpassword',
        'role': 'admin'
    })
    response = test_client.post('/api/auth/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 200
    assert b'Login successful' in response.data

def test_invalid_login(test_client):
    response = test_client.post('/api/auth/login', json={
        'username': 'testuser',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert b'Invalid credentials' in response.data
