import os
from werkzeug.utils import secure_filename
from app.extensions import db
from app.models.document import Document
from flask import current_app

# 设置文件上传的最大大小（可根据实际需求进行调整）
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16 MB
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'png', 'jpeg', 'doc', 'docx'}

# 检查文件类型是否允许
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 保存文件并记录到数据库
def save_file(file, employee_id, upload_folder="app/static/uploads"):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(upload_folder, filename)

        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        file.save(filepath)

        # 保存文件信息到数据库
        document = Document(employee_id=employee_id, filename=filename, file_type=file.content_type)
        db.session.add(document)
        db.session.commit()

        return document
    else:
        raise ValueError("File not allowed")

# 删除文件
def delete_file(file_id, upload_folder="app/static/uploads"):
    document = Document.query.get(file_id)
    if document:
        # 删除磁盘中的文件
        file_path = os.path.join(upload_folder, document.filename)
        if os.path.exists(file_path):
            os.remove(file_path)

        # 删除数据库中的记录
        db.session.delete(document)
        db.session.commit()
        return True
    return False
