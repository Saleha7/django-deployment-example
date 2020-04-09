from django import forms
from basic_app.models import User

class NewUser(forms.ModelForm):
    class Meta():
        model=User
        fields=['Name','Bdate','Gender','Email','Contact']
        labels={
        'Name':'FullName',
        'Bdate':'BirthDate(yyyy-mm-dd)',
        }
