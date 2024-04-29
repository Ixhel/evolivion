from django import forms
from NMX_R_025_SCFI_2015.models import LogMessage
from NMX_R_025_SCFI_2015.models import LogEval

# Django form que contiene los datos definidos en el modelo model.LogMessage
class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("empresa",)   # trailing comma required
        
class LogEvalForm(forms.ModelForm):
    class Result:
        model = LogEval
        fiels =("...","....",)