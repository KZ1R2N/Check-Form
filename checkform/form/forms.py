from django import forms
from .models import FormData

class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['number_field', 'text_field', 'date_field', 
                  'is_number_checked', 'is_text_checked', 'is_date_checked']

    def clean(self):
        cleaned_data = super().clean()

        is_number_checked = cleaned_data.get('is_number_checked')
        is_text_checked = cleaned_data.get('is_text_checked')
        is_date_checked = cleaned_data.get('is_date_checked')

        if not is_number_checked:
            cleaned_data['number_field'] = None
        
        if not is_text_checked:
            cleaned_data['text_field'] = None
        
        if not is_date_checked:
            cleaned_data['date_field'] = None
        
        return cleaned_data
