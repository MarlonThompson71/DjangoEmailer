import smtplib
from email.message import EmailMessage
from django.shortcuts import render
from .forms import EmailForm

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            receiver = form.cleaned_data['receiver']
            cc = form.cleaned_data.get('cc')  # Retrieve the CC field
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            attachment = request.FILES.get('attachment', None)

            msg = EmailMessage()
            msg['From'] = sender
            msg['To'] = receiver
            msg['Subject'] = subject
            msg.set_content(body)
            if cc:
                msg['Cc'] = cc  # Add CC field to the message headers
            if attachment:
                with attachment.open(mode='rb') as f:
                    attachment_data = f.read()
                msg.add_attachment(attachment_data, maintype='application', subtype='octet-stream', filename=attachment.name)

            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            smtp_username = ''
            smtp_password = ''

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)

            server.send_message(msg)

            server.quit()

            return render(request, 'email_sender/email_sent.html', {
                'sender': sender,
                'receiver': receiver,
                'cc': cc,
                'subject': subject,
                'body': body,
                'attachment': attachment,
            })

    else:
        form = EmailForm()
    return render(request, 'email_sender/email_form.html', {'form': form})
