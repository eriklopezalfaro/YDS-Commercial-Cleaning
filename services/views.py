from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import Service

# Create your views here.
def home(request):
    return render(request, 'services/index.html')

def about(request):
    return render(request, 'services/about.html')

def services(request):
    services = Service.objects.all()

    return render(request, 'services/services.html', {'services':services})

def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        msg = f'Message from {full_name}\n'
        msg += f'Email address: {email}\n'
        msg += f'Message: "{message}"\n'
        msg += f'Phone number to reach {full_name} at: "{phone}"\n'

        # send email
        send_mail(
            subject=f'{full_name} sent a message on the YDS website',
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS],
        )

        return render(request, 'services/contact.html', {'success' : full_name})
    
    return render(request, 'services/contact.html')

    