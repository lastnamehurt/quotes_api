# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import logging

from django.http import JsonResponse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from quotes_api.settings import SENDGRID_API_KEY


def send_quote_confirmation(**data):
    message = Mail(
        from_email='info+apt@globalentrynow.com',
        to_emails=data['email_address'],
        subject='Your Quote from All Purpose Trucking!',
        html_content=f'<h1>Hello {data["company_name"]}!</h1><br><p>We received your quote request with the below '
                     f'details. Please let us know if you have any questions!</p><br><strong>Container Type:</strong> '
                     f'{data["container_type"]}<br><strong>Estimated Distance: '
                     f'{data["estimated_distance"]}<br><strong>Legal Weight:</strong> '
                     f'{data["is_legal_weight"]}<br><strong>Hazmat:</strong> '
                     f'{data["is_hazmat"]}<br><strong>Total:</strong> {data["total"]}')
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)
        return JsonResponse({"success": "Ok"})
    except Exception as e:
        logging.error(e)


def send_contact_request(**data):
    message = Mail(
        from_email='info+apt@globalentrynow',
        to_emails=[data['email_address'], 'support@drivewithapt.com', 'info@globalentrynow.com'],
        subject='New Contact Request',
        html_content=f'<h1>Name: {data["company_name"]}</h1><br>'
                     f'Email: {data["email"]}<br><strong>Phone: {data["phone_number"]}</strong><br><strong>Message: '
                     f'{data["message"]}</strong><br>')
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)
        return JsonResponse({"success": "Ok"})
    except Exception as e:
        logging.error(e)
