from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from api.models import ErrorInstances
from django.views.generic import CreateView
from .forms import RegisterErrorForm
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views import generic
from django.db.models import Count
from .serializers import ErrorInstancesModelSerializers
from rest_framework.renderers import TemplateHTMLRenderer


def index(request):
    """
    Show the initial page with some instructions.
    """
    return render(request, 'index.html')


class ErrorInstancesListView(LoginRequiredMixin, generic.ListView):
    """
    List all the registered errors with the filter's form.
    It shows the option to delete and shelve the error.
    Is related to :model: 'api.ErrorInstances'.
    """
    renderer_classes = [TemplateHTMLRenderer]
    login_url = reverse_lazy('login')
    model = ErrorInstances
    paginate_by = 10
    serializer_class = ErrorInstancesModelSerializers

    def get_context_data(self, **kwargs):
        context = super(
            ErrorInstancesListView,
            self
        ).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        """
        Search errors with some filters,
        related to :model:'api.ErrorInstances'

        **Template:**
        :template:'api/errorinstances_list.html'
        """
        queryset = ErrorInstances.objects.get_queryset().order_by('id')
        search_bar = self.request.GET.get('search_bar')
        search_type = self.request.GET.get('search_type')
        search_order = self.request.GET.get('search_order')
        search_topic = self.request.GET.get('search_topic')
        if search_bar is not None:
            queryset = queryset.filter(
                Q(description__icontains=search_bar) | Q(level__icontains=search_bar) | Q(origin__icontains=search_bar)).order_by('id')
            if search_topic:
                if search_topic == 'description':
                    queryset = queryset.filter(
                        description__icontains=search_bar
                    ).order_by('id')
                elif search_topic == 'level':
                    queryset = queryset.filter(level__icontains=search_bar).order_by('id')
                elif search_topic == 'origin':
                    queryset = queryset.filter(origin__icontains=search_bar).order_by('id')
            if search_type:
                if search_type == 'dev':
                    queryset = queryset.filter(type_error__icontains='dev').order_by('id')
                    print(queryset)
                if search_type == 'hom':
                    queryset = queryset.filter(type_error__icontains='hom').order_by('id')
                if search_type == 'prod':
                    queryset = queryset.filter(type_error__icontains='prod').order_by('id')
            if search_order:
                # if search_order == 'freq':
                #     queryset = queryset.annotate(
                #         frequency=Count("event")).order_by('frequency')
                #     print(queryset)
                if search_order == 'level':
                    queryset = queryset.order_by('level').order_by('id')
        return queryset


class ErrorInstancesDetailView(LoginRequiredMixin, generic.DetailView):
    """
    Show the details of a particular error.
    Is related to :model:'api.ErrorInstances'.
    """
    login_url = reverse_lazy('login')
    model = ErrorInstances


class RegisterErrorView(LoginRequiredMixin, CreateView):
    """
        Show the form to register a new error.
        Is related to :model:'api.ErrorInstances'.
    """
    model = ErrorInstances
    form_class = RegisterErrorForm
    template_name = 'api/errorinstances_form.html'
    success_url = '/api/pesquisa/'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        """
            This function save the data with the user token.
            Is related to :model:'api.ErrorInstances'.
            """
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self, *args, **kwargs):
        """
            This function request and return the user token.
            Is related to :model:'api.ErrorInstances'.
        """
        kwargs = super(RegisterErrorView, self).get_form_kwargs(
            *args,
            **kwargs
        )
        kwargs['user_id'] = self.request.user
        return kwargs


class DeleteErrorView(LoginRequiredMixin, generic.DetailView):
    """
        Delete a particular error.
        Is related to :model:'api.ErrorInstances'.
    """
    def get(self, request, id):
        """
            This function take the error id and delete.
            Is related to :model:'api.ErrorInstances'.
        """
        error_delete = ErrorInstances.objects.get(id=id)
        error_delete.delete()
        return redirect('pesquisa')


class ShelvedView(LoginRequiredMixin, generic.DetailView):
    """
        Shelve s particular error.
        Is related to :model:'api.ErrorInstances'.
    """
    def get(self, request, id):
        """
            Change the value from false to true.
            Is related to :model:'api.ErrorInstances'.
        """
        error_shelve = ErrorInstances.objects.get(id=id)
        error_shelve.shelved = True
        error_shelve.save()
        return redirect('pesquisa')
