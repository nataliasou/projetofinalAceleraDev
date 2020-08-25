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
    return render(request, 'index.html')


class ErrorInstancesListView(LoginRequiredMixin, generic.ListView):
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
        # Filtrar dados
        queryset = ErrorInstances.objects.all()
        search_bar = self.request.GET.get('search_bar')
        search_type = self.request.GET.get('search_type')
        search_order = self.request.GET.get('search_order')
        search_topic = self.request.GET.get('search_topic')
        if search_bar is not None:
            queryset = queryset.filter(
                Q(description__icontains=search_bar) | Q(level__icontains=search_bar) | Q(origin__icontains=search_bar))
            if search_topic:
                if search_topic == 'description':
                    queryset = queryset.filter(
                        description__icontains=search_bar
                    )
                elif search_topic == 'level':
                    queryset = queryset.filter(level__icontains=search_bar)
                elif search_topic == 'origin':
                    queryset = queryset.filter(origin__icontains=search_bar)
            if search_type:
                if search_type == 'dev':
                    queryset = queryset.filter(type_error__icontains='dev')
                    print(queryset)
                if search_type == 'hom':
                    queryset = queryset.filter(type_error__icontains='hom')
                if search_type == 'prod':
                    queryset = queryset.filter(type_error__icontains='prod')
            if search_order:
                if search_order == 'freq':
                    queryset = queryset.annotate(
                        frequency=Count("event")).order_by('frequency')
                    print(queryset)
                if search_order == 'level':
                    queryset = queryset.order_by('level')
        return queryset


class ErrorInstancesDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = reverse_lazy('login')
    model = ErrorInstances


class RegisterErrorView(LoginRequiredMixin, CreateView):
    model = ErrorInstances
    form_class = RegisterErrorForm
    template_name = 'api/errorinstances_form.html'
    success_url = '/api/pesquisa/'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(RegisterErrorView, self).get_form_kwargs(
            *args,
            **kwargs
        )
        kwargs['user_id'] = self.request.user
        return kwargs


class DeleteErrorView(LoginRequiredMixin, generic.DetailView):
    def get(self, request, id):
        error_delete = ErrorInstances.objects.get(id=id)
        error_delete.delete()
        return redirect('pesquisa')


class ShelvedView(LoginRequiredMixin, generic.DetailView):
    def get(self, request, id):
        error_shelve = ErrorInstances.objects.get(id=id)
        error_shelve.shelved = True
        error_shelve.save()
        return redirect('pesquisa')
