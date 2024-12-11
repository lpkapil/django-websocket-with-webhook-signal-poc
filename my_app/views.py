# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
from channels.layers import get_channel_layer
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

def websocket_notifications(request):
    return render(request, 'my_app/notifications.html')


@csrf_exempt
@require_POST
async def send_message_to_websocket(request):
    # Get the message from the POST data
    # message = request.POST.get('message', 'Hello, WebSocket!')

    try:
        data = json.loads(request.body)  # Parse the body as JSON
        print(data)
        message = data.get('message', 'Hello, WebSocket!')  # Get the message from the parsed JSON data
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    # Get the channel layer
    channel_layer = get_channel_layer()

    # Send a message to the group
    await channel_layer.group_send(
        'notifications_notifications',  # The group name in the consumer
        {
            'type': 'send_message',  # This matches the method name in the consumer
            'message': data,  # The message we want to send
        }
    )

    return JsonResponse({'status': 'Message sent', 'message': message})

