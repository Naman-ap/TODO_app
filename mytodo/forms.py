from django import forms

class todoform(forms.Form):
    todo_text=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Tasks"}))