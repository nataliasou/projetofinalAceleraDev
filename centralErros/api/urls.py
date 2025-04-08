from django.urls import path, re_path, include
from api.views import (
    index,
    ErrorInstancesDetailView,
    ErrorInstancesListView,
    RegisterErrorView,
    DeleteErrorView,
    ShelvedView
)

urlpatterns = [
    path('', index, name='index'),
    path('pesquisa/', ErrorInstancesListView.as_view(), name='pesquisa'),
    path(
        "pesquisa/<uuid:pk>/",
        ErrorInstancesDetailView.as_view(),
        name='errorinstances-detail'
    ),
    # Usando re_path para cadastrar
    re_path(r"^cadastrar/$", RegisterErrorView.as_view(), name='register-error'),
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

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
