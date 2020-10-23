from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class Branch(models.Model):
    name = models.CharField(max_length=60, blank=True)
    address = models.TextField(max_length=500, blank=True)

class Profile(models.Model):
    class ReaderStatus(models.TextChoices):
        NOBOOK = 'NB', _('Без книги')
        BORROWED = 'BR', _('Пользуется книгу')
        DEBTOR = 'DB', _('Должник')
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_librarian = models.BooleanField(default=False)
    full_name = models.CharField(max_length=100, blank=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2, choices=ReaderStatus.choices, 
        default=ReaderStatus.NOBOOK 
    )

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

