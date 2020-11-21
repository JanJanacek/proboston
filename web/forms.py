from django import forms
from web.models import Users
from ares_util.validators import czech_company_id_numeric_validator, czech_company_id_ares_api_validator

class UserForm(forms.ModelForm):
    ico = forms.CharField(required=True, validators=[czech_company_id_ares_api_validator])
    class Meta():
        model = Users
        fields = ('name','email','ico')
