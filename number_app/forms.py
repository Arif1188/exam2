from django import forms
from .models import HeaderModel, MiddleModel,FooterModel

class HeaderForm(forms.ModelForm):
    class Meta:
        model = HeaderModel
        fields = ['number','text','time','id']
        
        
class MiddleForm(forms.ModelForm):
    class Meta:
        model = MiddleModel
        fields = ['title']
        
        
class FooterForm(forms.ModelForm):
    class Meta:
        model = FooterModel
        fields = ['text','description','id']
        
        
class CombinedForm(forms.Form):
    user_number = forms.IntegerField()
    user_text = forms.CharField(max_length=10000)
    user_time = forms.DateField()
    user_title = forms.CharField(max_length=10000)
    text = forms.CharField(max_length=10000)
    user_description = forms.CharField(max_length=100000)