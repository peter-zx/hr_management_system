import pytest
from app import create_app
from app.extensions import db
from app.models.employee import Employee

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

def test_create_employee(test_client):
    response = test_client.post('/api/employee/', json={
        'name': 'John Doe',
        'id_number': '123456789012345678',
        'entry_date': '2025-04-01',
        'phone': '12345678901'
    })
    assert response.status_code == 201
    assert b'John Doe' in response.data

def test_get_employee(test_client):
    response = test_client.get('/api/employee/1')  # 这里假设 ID 为 1 的员工已存在
    assert response.status_code == 200
    assert b'John Doe' in response.data

def test_update_employee(test_client):
    response = test_client.put('/api/employee/1', json={
        'name': 'Jane Doe',
        'phone': '09876543210'
    })
    assert response.status_code == 200
    assert b'Jane Doe' in response.data

def test_delete_employee(test_client):
    response = test_client.delete('/api/employee/1')
    assert response.status_code == 204
