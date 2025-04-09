import os
from werkzeug.utils import secure_filename
from app.extensions import db
from app.models.document import Document

def save_uploaded_file(file, upload_folder="app/static/uploads"):
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    filename = secure_filename(file.filename)
    filepath = os.path.join(upload_folder, filename)

    file.save(filepath)
    return filename, filepath

def create_document(employee_id, file_name, file_type, upload_folder="app/static/uploads"):
    new_doc = Document(employee_id=employee_id, filename=file_name, file_type=file_type)
    db.session.add(new_doc)
    db.session.commit()
    return new_doc

def delete_document(document_id):
    doc = Document.query.get(document_id)
    if doc:
        file_path = os.path.join("app/static/uploads", doc.filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        db.session.delete(doc)
        db.session.commit()
        return True
    return False
