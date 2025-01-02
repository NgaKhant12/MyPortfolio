from django.forms import ModelForm
from .models import ContactInfo

class Contact_Info_Form(ModelForm):
    class Meta:
        model = ContactInfo
        fields = "__all__"