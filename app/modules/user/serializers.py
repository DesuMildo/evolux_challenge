from app.base.serializers import BaseSQLAlchemySchema
from app.modules.user.models import User
from marshmallow import fields


class UserSchema(BaseSQLAlchemySchema):
    class Meta(BaseSQLAlchemySchema.Meta):
        model = User

    username = fields.Str(required=True)
    password = fields.Str(required=True)
