from ninja import Router, UploadedFile, File
from ninja.pagination import paginate
from ninja_jwt.authentication import JWTAuth
from django.shortcuts import get_object_or_404
from .schemas import *

router = Router(auth=JWTAuth())

@router.post('/')
def send_message(request, payload: MessageIn, recipient_ids: list[int]):
    message = Message.objects.create(sender=request.auth, subject=payload.subject, body=payload.body)
    for rid in recipient_ids:
        MessageRecipient.objects.create(message=message, recipient_id=rid)
    return {'id': message.id}

@router.get('/inbox', response=list[MessageOut])
@paginate
def inbox(request):
    return Message.objects.filter(recipients__recipient=request.auth)

@router.get('/outbox', response=list[MessageOut])
@paginate
def outbox(request):
    return Message.objects.filter(sender=request.auth)

@router.post('/{message_id}/attachments')
def add_attachment(request, message_id: int, file: UploadedFile = File(...)):
    message = get_object_or_404(Message, id=message_id, sender=request.auth)
    MessageAttachment.objects.create(message=message, file=file)
    return {'success': True}
