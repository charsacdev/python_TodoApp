from django import forms

class TodolistForm(forms.Form):
    text = forms.CharField(max_length=45,

    #Create Widget and Attribute for forms
    widget = forms.TextInput(
        attrs={"id":"taskInput","class":"form-control","placeholder":"Enter task...eg washing","name":"text","required":"required"}
    ))