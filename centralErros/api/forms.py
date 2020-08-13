from django import forms
from .models import ErrorInstances
from accounts.models import User


class RegisterErrorForm(forms.ModelForm):
    """
        A form for add new errors.
    """
    title = forms.CharField(label='Titulo', widget=forms.TextInput)
    description = forms.CharField(label='Decrição', widget=forms.Textarea)
    origin = forms.CharField(label='Origem', widget=forms.Textarea)
    date = forms.DateTimeField(label='Data', widget=forms.DateTimeInput)
    details = forms.CharField(label='Detalhes', widget=forms.Textarea)
    level = forms.ChoiceField(label='Nivel', choices=ErrorInstances.LEVEL_STATUS, widget=forms.Select)
    events = forms.IntegerField(label='Eventos', widget=forms.NumberInput)
    type_error = forms.ChoiceField(label='Tipo', choices=ErrorInstances.TYPE_ERROR_STATUS,  widget=forms.Select)

    class Meta:
        model = ErrorInstances
        fields = ('title', 'description', 'origin', 'date', 'details', 'level', 'events', 'type_error')  # pode botar o name aquiii

    def save(self, commit=True):
        erro = super(RegisterErrorForm, self).save(commit=False)
        if commit:
            erro.save()
        return erro
