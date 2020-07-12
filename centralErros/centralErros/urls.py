from django.contrib import admin
from django.urls import path, include

from django.views.generic import RedirectView, TemplateView

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url

from accounts.views import RegisterView, LoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/register/', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('', RedirectView.as_view(url='api/', permanent=True)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

