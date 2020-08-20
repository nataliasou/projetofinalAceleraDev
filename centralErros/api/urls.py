from django.urls import path, re_path, include
from api.views import (
    index,
    ErrorInstancesDetailView,
    ErrorInstancesListView,
    RegisterErrorView,
    DeleteErrorView,
    ShelvedView
)
from django.conf.urls import url

urlpatterns = [
    path('', index, name='index'),
    path('pesquisa/', ErrorInstancesListView.as_view(), name='pesquisa'),
    path(
        "pesquisa/<uuid:pk>/",
        ErrorInstancesDetailView.as_view(),
        name='errorinstances-detail'
    ),
    url(r"^cadastrar/$", RegisterErrorView.as_view(), name='register-error'),
    re_path(
        r'(?P<id>[\w-]+)?/delete',
        DeleteErrorView.as_view(),
        name='delete-error'
    ),
    re_path(
        r'(?P<id>[\w-]+)?/shelve',
        ShelvedView.as_view(),
        name='shelved-error'
    ),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
