from django.shortcuts import render
from django.core.mail import mail_admins, send_mail, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage


# def say_hello(request):
#     try:
#         # send_mail('subject', 'message', 'info@masud.com', ['bob@masud.com'])
#         # mail_admins('subject', 'message', html_message="message")
#         # message = EmailMessage('subject', 'message', 'info@masud.com', ['bob@masud.com'])
#         # message.attach_file('playground/static/images/gofi.png')
#         # message.send()

#         message = BaseEmailMessage(
#             template_name='emails/hello.html',
#             context={'name': "Masud"}
#         )

#         message.send(['bob@masud.com'])
#     except BadHeaderError:
#         pass
#     return render(request, 'hello.html', {'name': 'Mosh'})


from .tasks import notify_customers

def say_hello(request):
    notify_customers.delay("hello")
    return render(request, 'hello.html', {'name': 'Mosh'})
