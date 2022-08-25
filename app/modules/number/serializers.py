from app.base.serializers import BaseSQLAlchemySchema
from app.modules.number.models import Number
from marshmallow import fields, validate


class NumberSchema(BaseSQLAlchemySchema):
    class Meta(BaseSQLAlchemySchema.Meta):
        model = Number

    value = fields.Str(required=True)
    monthyPrice = fields.Decimal(required=True, validate=validate.Range(min=0))
    setupPrice = fields.Decimal(required=True, validate=validate.Range(min=0))
    currency = fields.Str(required=True)
