from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.document import Document
from app.schemas.document_schema import document_schema, documents_schema

document_bp = Blueprint('document', __name__)

@document_bp.route("/", methods=["GET"])
def list_documents():
    documents = Document.query.all()
    return jsonify(documents_schema.dump(documents))

@document_bp.route("/", methods=["POST"])
def upload_document():
    data = request.json
    new_doc = document_schema.load(data, session=db.session)
    db.session.add(new_doc)
    db.session.commit()
    return jsonify(document_schema.dump(new_doc)), 201

@document_bp.route("/<int:id>", methods=["DELETE"])
def delete_document(id):
    doc = Document.query.get_or_404(id)
    db.session.delete(doc)
    db.session.commit()
    return jsonify({"message": "Deleted"}), 204
