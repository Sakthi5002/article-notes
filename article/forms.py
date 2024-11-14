from django import forms

from .models import Group, Link

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('name',)

class LinkForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = ('text',)