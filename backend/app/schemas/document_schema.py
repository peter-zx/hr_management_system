from app.extensions import ma
from app.models.document import Document

class DocumentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Document
        include_fk = True
        load_instance = True

document_schema = DocumentSchema()
documents_schema = DocumentSchema(many=True)
