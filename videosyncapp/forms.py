from django import forms
from .models import Group


class CreateGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group_name',)
    def __init__(self, *args, **kwargs):
        super(CreateGroup,self).__init__(*args,**kwargs)
        self.fields['group_name'].widget.attrs.update({'id': 'group_name', 'class': 'form-control'})

    def save(self, user, commit=True):
        group = super(CreateGroup, self).save(commit=False)
        group.admin = user
        if commit:
            group.save()
        return group

class CreateGroupgdrive(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group_name','link')
    def __init__(self, *args, **kwargs):
        super(CreateGroupgdrive,self).__init__(*args,**kwargs)
        self.fields['group_name'].widget.attrs.update({'id': 'group_name', 'class': 'form-control'})
        self.fields['group_name'].widget.attrs.update({'id': 'link', 'class': 'form-control'})

    def save(self, user, commit=True):
        group = super(CreateGroupgdrive, self).save(commit=False)
        group.admin = user
        if commit:
            group.save()
        return group