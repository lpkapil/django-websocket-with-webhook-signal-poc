from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Message

@receiver(post_save, sender=Message)
def send_new_message_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        message = instance.content  # assuming 'content' holds the message text

        # Send message to all connected clients in the chat group
        async_to_sync(channel_layer.group_send)(
            'chat_chat_room',  # Room name to broadcast the message
            {
                'type': 'chat_message',
                'message': message,
            }
        )
