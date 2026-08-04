from ninja import ModelSchema
from .models import Message, MessageRecipient, MessageAttachment

class MessageIn(ModelSchema):
    class Meta:
        model = Message
        fields = [
            'sender',
            'subject',
            'body'
        ]

class MessageOut(ModelSchema):
    class Meta:
        model = Message
        fields = '__all__'
