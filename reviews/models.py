from django import forms
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('__all__')


class City(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('__all__')


class Person(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('__all__')


class Scenario(models.Model):
    GRADES = (
        ('o', '∅'),
        ('g', 'Good'),
        ('a', 'Average'),
        ('b', 'Bad'),
    )

    name = models.CharField(max_length=128)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    done = models.BooleanField(default=True)
    reviewers = models.ManyToManyField(Person)
    date = models.DateField(blank=True, null=True)

    scenery = models.CharField(
        max_length=1,
        choices=GRADES,
        default=GRADES[0][0]
    )
    puzzles = models.CharField(
        max_length=1,
        choices=GRADES,
        default=GRADES[0][0]
    )
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'scenarii'

    def __str__(self):
        return '{} (by {})'.format(
            self.name, ', '.join([str(r) for r in self.reviewers.all()]))


class ScenarioForm(forms.ModelForm):
    class Meta:
        model = Scenario
        fields = ('__all__')

    def clean(self):
        cleaned_data = super().clean()

        done = cleaned_data.get("done")
        date = cleaned_data.get("date")

        if done and not date:
            raise forms.ValidationError(
                "A scenario that has been done must have a date")
