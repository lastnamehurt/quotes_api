# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

from django.http import JsonResponse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_quote_confirmation(**data):

    print(f"Send QUote Confirm: {data}")
    message = Mail(
        from_email='info@globalentrynow.com',
        to_emails=data['email_address'],
        # to_emails='courtney.hurt@icloud.com',
        subject='Your Quote from All Purpose Trucking!',
        html_content=f'<h1>Hello {data["company_name"]}!</h1><br><p>We received your quote request with the below '
                     f'details. Please let us know if you have any questions!</p><br><strong>Container Type:</strong> '
                     f'{data["container_type"]}<br><strong>Estimated Distance: '
                     f'{data["estimated_distance"]}<br><strong>Legal Weight:</strong> '
                     f'{data["is_legal_weight"]}<br><strong>Hazmat:</strong> '
                     f'{data["is_hazmat"]}<br><strong>Total:</strong> {data["total"]}')
    try:
        # sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg = SendGridAPIClient("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")
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return JsonResponse({"Result": "Success"})
    except Exception as e:
        print(e)
