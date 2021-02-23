from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    tagline = models.CharField(max_length=100, null=True, blank=True)

class Ticket(models.Model):
    TICKET_STATUS_CHOICES = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Invalid', 'Invalid'),
    ]
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=14, choices=TICKET_STATUS_CHOICES, default='New')
    assigned = models.ForeignKey(CustomUser, related_name='assigned_ticket', on_delete=models.CASCADE, null=True, blank=True)
    completed = models.ForeignKey(CustomUser, related_name='completed_ticket', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title} | {self.creator}'

