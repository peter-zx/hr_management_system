import pytest
from app import create_app
from app.extensions import db
from io import BytesIO

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

def test_upload_file(test_client):
    data = {
        'file': (BytesIO(b"test file content"), 'test_file.pdf'),
        'employee_id': 1
    }
    response = test_client.post('/api/document/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 201
    assert b'Upload successful' in response.data

def test_delete_file(test_client):
    # 假设文件 ID 为 1
    response = test_client.delete('/api/document/1')
    assert response.status_code == 204
