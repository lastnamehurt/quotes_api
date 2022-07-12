from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from quotes.mailer import send_quote_confirmation, send_contact_request
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


@csrf_exempt
def send_contact_email(request):
    if request.method == 'POST':
        import pdb;pdb.set_trace()
    send_contact_request(**request.POST)
    return HttpResponse("<h1>Thank You</h1>")
