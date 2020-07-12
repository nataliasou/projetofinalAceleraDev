from django.urls import path, re_path, include
from api.views import (index, ErrorInstancesDetailView, ErrorInstancesListView, RegisterErrorView)
from api import views
from django.conf.urls import url


from django.views.generic import RedirectView, TemplateView
urlpatterns = [
    path('', index, name='index'),
    path('pesquisa/', ErrorInstancesListView.as_view(), name='pesquisa'),
    path('pesquisa/<uuid:pk>', ErrorInstancesDetailView.as_view(), name='errorinstances-detail'),
    path('pesquisa/cadastrar/', RegisterErrorView.as_view(), name='register-error'),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]