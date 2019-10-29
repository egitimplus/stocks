from learning.forms import Contact
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def contact_form(request):

    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            message = form.cleaned_data['content']
            sender = form.cleaned_data['email']

            recipients = ['info@internet.com.tr']

            #send_mail(subject, message, sender, recipients)
            print(subject)

            return HttpResponseRedirect('/')
    else:
        form = Contact()

    return render(request=request, template_name='contact/form.html', context={'form': form})