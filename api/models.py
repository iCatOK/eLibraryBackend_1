from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=60, blank=True)
    address = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):

    class ReaderStatus(models.TextChoices):
        NOBOOK = 'NB', _('Без книги')
        BORROWED = 'BR', _('Пользуется книгу')
        DEBTOR = 'DB', _('Должник')
    

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    status = models.CharField(
        max_length=2, choices=ReaderStatus.choices, 
        default=ReaderStatus.NOBOOK 
    )

    username = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=200)


    is_staff = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.full_name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, null=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.CASCADE)
    is_free = models.BooleanField(default=True)


class Order(models.Model):
    
    class OrderStatus(models.TextChoices):
        INQUEUE = 'В очереди'
        ACCEPTED = 'Принята'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=15, choices=OrderStatus.choices, 
        default=OrderStatus.INQUEUE 
    )
    date = models.DateTimeField(auto_now=True)


class BookTransaction(models.Model):

    class TransactionStatus(models.TextChoices):
        INUSE = 'В пользовании'
        RETURNED = 'Сдана'
        DEBT = 'Долг'

    borrow_date = models.DateTimeField(auto_now=True)
    return_date = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    cooperator = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=15, choices=TransactionStatus.choices, 
        default=TransactionStatus.INUSE 
    )
    

