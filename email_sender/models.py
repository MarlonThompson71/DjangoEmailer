from django.db import models

class Email(models.Model):
    sender = models.EmailField()
    receivers = models.TextField()  
    cc = models.TextField(blank=True, null=True)  
    subject = models.CharField(max_length=255)
    body = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
