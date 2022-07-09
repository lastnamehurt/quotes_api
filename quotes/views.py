from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from quotes.mailer import send_quote_confirmation
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from quotes.models import Quote


@csrf_exempt
def send_quote_email(request):
    # email_address = request.POST['to_email']
    send_quote_confirmation(**request.POST)
    # create quote
    model = Quote.objects.create(
        **request.POST
    )
    data = serializers.serialize("json", model)
    return JsonResponse(data)

