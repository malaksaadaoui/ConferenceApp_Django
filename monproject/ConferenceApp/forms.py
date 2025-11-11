from django import forms
from .models import Conference,Submission
class ConferenceForm(forms.ModelForm):
    class Meta:
        model=Conference
        fields=['name','theme','location','description','start_date','end_date']
        labels = {
            'name' :"titre de la conference",
            'theme': "thematique de la conference",
        }
        widgets = {
            'name' : forms.TextInput(
                attrs = {
                    'placeholder' : "entrer un titre a la conference",
                    'class'  : "",
                }
            ),
            'start_date' : forms.DateInput(
                attrs = {
                    'type' :"date",
                }
            ),
            'end_date' : forms.DateInput(
                attrs = {
                    'type' :"date",
                }
            ),
        }




class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['title', 'abstract', 'keywords', 'paper', 'conference', 'payed','status']  
