
import uuid
from django.urls import reverse
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photos",default='download.png')
    country = CountryField(blank_label='(select country)')



    def __str__(self):
        return self.name + '' + self.surname + 'from' + self.country.name

    class Meta:
        ordering = ['surname']


class Book(models.Model):
    BOOK_TYPE = (
       ('regular', _('Regular')),
       ('fiction', _('Fiction')),
       ('novels', _('Novels')),
       )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isbn = models.CharField(_("ISBN"), max_length=13, unique=True)
    title = models.CharField(_("Book's title"), max_length=128)
    publisher = models.CharField(_("Publisher"), max_length=64)
    book_type = models.CharField(_('Book Type'), max_length=20, choices=BOOK_TYPE,default='regular')
    pages = models.IntegerField(_("Pages"), default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name="books")
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

   
            
    def __str__(self):
        return self.title