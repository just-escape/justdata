from django import forms
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('__all__')


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    tel = PhoneNumberField(blank=True)
    mail = models.CharField(max_length=128, blank=True)
    tags = models.ManyToManyField(Tag)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'people'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('__all__')
