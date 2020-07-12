from django import forms
from .models import ErrorInstances
from accounts.models import User


# class RegisterErrorInstanceForm(forms.ModelForm):
#     level = forms.ChoiceField(label='Nivel', required=False, choices=ErrorInstances.LEVEL_STATUS, widget=forms.Select)
#     events = forms.IntegerField(label='Eventos', required=False, widget=forms.NumberInput)
#     type_error = forms.ChoiceField(label='Tipo', required=False, choices=ErrorInstances.TYPE_ERROR_STATUS, widget=forms.Select)
#
#     class Meta:
#         model = ErrorInstances
#         fields = ('level', 'events', 'type_error')  # pode botar o name aquiii

    # def save(self, commit=True):
    #     erro = super(RegisterErrorInstanceForm, self).save(commit=False)
    #     #erro.set_password(self.cleaned_data["password1"])
    #     #user.active = False isso é pra mandar email de confirmação
    #     if commit:
    #         erro.save()
    #     return erro


# class RegisterLogForm(forms.ModelForm):
#     title = forms.CharField(label='Titulo', required=False, widget=forms.TextInput)
#     description = forms.CharField(label='Decrição', required=False, widget=forms.TextInput)
#     origin = forms.CharField(label='Origem', required=False, widget=forms.TextInput)
#     date = forms.DateTimeField(label='Data', required=False, widget=forms.DateTimeInput)
#     details = forms.CharField(label='Detalhes', required=False, widget=forms.TextInput)
#
#     class Meta:
#         model = Log
#         fields = ('title', 'description', 'origin', 'date', 'details')# pode botar o name aquiii
#
    # def save(self, commit=True):
    #     erro = super(RegisterLogForm, self).save(commit=False)
    #     if commit:
    #         erro.save()
    #     return erro

#
# class RegisterUserErrorForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('name',) # pode botar o name aquiii
#
#     def save(self, commit=True):
#         erro = super(RegisterUserErrorForm, self).save(commit=False)
#         #erro.set_password(self.cleaned_data["password1"])
#         #user.active = False isso é pra mandar email de confirmação
#         if commit:
#             erro.save()
#         return erro

#class UserEditMultiForm(MultiModelForm):
#    form_classes = {
#        'user': RegisterUserErrorForm,
#        'log': RegisterLogForm,
#        'error_instances': RegisterErrorInstanceForm,
#    }
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
        ErrorInstances.user_id = request.user.id
        erro = super(RegisterErrorForm, self).save(commit=False)
        if commit:
            erro.save()
        return erro