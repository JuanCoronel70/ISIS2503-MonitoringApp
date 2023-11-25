from django import forms
from .models import Measurement
from variables.models import Variable
from places.models import Place

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = [
            'variable',
            'value',
            'unit',
            'place',
            #'dateTime',
        ]

        labels = {
            'variable' : 'Variable',
            'value' : 'Value',
            'unit' : 'Unit',
            'place' : 'Place',
            #'dateTime' : 'Date Time',
        }

    def clean(self):
        cleaned_data = super().clean()
        variable = cleaned_data.get('variable')
        place = cleaned_data.get('place')

        # Realizamos la validación de la existencia de la ForeignKey aquí
        if variable and not Variable.objects.filter(pk=variable.pk).exists():
            self.add_error('variable', forms.ValidationError('La variable no existe.'))

        if place and not Place.objects.filter(pk=place.pk).exists():
            self.add_error('place', forms.ValidationError('El lugar no existe.'))
