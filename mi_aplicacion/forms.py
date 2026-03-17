from crispy_forms.layout import Row, Column, Layout,Submit
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from mi_aplicacion.models import Escuela, Maestro

class EscuelaForm(ModelForm):
    class Meta:
        model = Escuela
        fields = ['nombre','siglas']

class MaestroForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MaestroForm,self).__init__(*args, **kwargs)
        self.fields['escuela'].queryset = Escuela.objects.all()
        self.helper = FormHelper()
        self.helper.layout = Layout()


    class Meta:
        model = Maestro
        fields = ['nombre','escuela','sexo','fecha_nacimiento']
