from django.db import models


class Contact(models.Model):
    """
    Model for Contact Form
    """
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email
