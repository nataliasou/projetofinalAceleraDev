from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, render_to_response
from api.models import ErrorInstances, Group
from django.views.generic import CreateView, FormView
from .forms import RegisterErrorForm


import datetime

from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404



def index(request):

    return render(request, 'index.html')


class ErrorInstancesListView(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('/')
    model = ErrorInstances
    paginate_by = 2

    # Deletar erros
    def deletar_erros(request):
        if request.method == "POST":
            if request.POST.get('delete'):
                error_delete = request.POST.getlist('item')
                ErrorInstances.objects.filter(pk__in=error_delete).delete()
                return render(request, 'errorinstances_list.html', {'error_delete': error_delete})
            else:
                return render(request, 'errorinstances_list.html', {})


    def get_context_data(self, **kwargs):
        context = super(ErrorInstancesListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return ErrorInstances.objects.all()


class ErrorInstancesDetailView(generic.DetailView):
    login_url = reverse_lazy('/')
    model = ErrorInstances

#
# class LogListView(LoginRequiredMixin, generic.ListView):
#     login_url = reverse_lazy('login')
#     model = Log
#
#     def get_context_data(self, **kwargs):
#         context = super(LogListView, self).get_context_data(**kwargs)
#         return context
#
#     def get_queryset(self):
#         return Log.objects.all()


# class LogDetailView(generic.DetailView):
#     login_url = reverse_lazy('login')
#     model = Log

class RegisterErrorView(CreateView):
    form_class = RegisterErrorForm
    template_name = 'api/register_error.html'
    success_url = '/api/pesquisa/'


"""
def register_error(request):
    error_instances = get_object_or_404(ErrorInstances)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RegisterErrorForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)

            error_instances.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('api/pesquisa/') )

    context = {
        'form': form,
        'error': error_instances,
    }

    return render(request, 'api/register_error.html', context)

from django.views.generic import UpdateView
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from .forms import UserEditMultiForm

User = get_user_model()

class generateView(UpdateView):
    model = User
    form_class = UserEditMultiForm
    success_url = reverse_lazy('api/pesquisa/')

    def get_form_kwargs(self):
        kwargs = super(generateView, self).get_form_kwargs()
        kwargs.update(instance={
            'user': self.object,
            'profile': self.object.profile,
            'log': self.object.log,
            'error_instances': self.object.errorInstances,
        })
        return kwargs
"""
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def generateView(request):
    if request.method == 'POST':  # If the form has been submitted...
        error_instance_form = RegisterErrorInstanceForm(request.POST, prefix="errorinstanceform")
        log_form = RegisterLogForm(request.POST, prefix="logform")
        if not error_instance_form.is_valid():
            # save them into context
            error_instance_form.save()
        if not log_form.is_valid():
            # save them into context
            log_form.save()

        if error_instance_form.is_valid() and log_form.is_valid():
            # that's mean both form is valid and saved successfully
            return HttpResponseRedirect("/api/pesquisa")

    return render_to_response('api/register_error.html', {
            'error_instance_form': RegisterErrorInstanceForm,
            'log_form': RegisterLogForm,
        })

    #     if error_instance_form.is_valid() and log_form.is_valid():  # All validation rules pass
    #         print("all validation passed")
    #         error = error_instance_form.save()
    #         log_form.cleaned_data["error"] = error
    #         b = log_form.save()
    #         print(error_instance_form.save())
    #         #         erro = super(RegisterUserErrorForm, self).save(commit=False)
    #         # print(error_instance_form.is_valid())
    #         # print(log_form.errors)
    #         # print(log_form.is_valid())
    #         return HttpResponseRedirect("/api/pesquisa")
    #     else:
    #         print("failed")
    #
    # else:
    #     error_instance_form = RegisterErrorInstanceForm(prefix="errorinstanceform")
    #     log_form = RegisterLogForm(prefix="logform")
    #
    # return render_to_response('api/register_error.html', {
    #     'error_instance_form': RegisterErrorInstanceForm,
    #     'log_form': RegisterLogForm,
    # })
"""
if request.method == 'POST':
   

    if form1.is_valid() and  form2.is_valid(): 
       #that's mean both form is valid and saved successfully 
       return redirect('page')
    else:
        return render('/page', context)


else:
    form1 = Form1(prefix="form1")
    form2 = Form2(prefix="form2")
    """