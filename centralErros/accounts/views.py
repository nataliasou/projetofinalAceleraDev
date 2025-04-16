from django.views.generic import CreateView, FormView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .forms import LoginForm, RegisterForm, UsersForm
from .models import UsersEmail
from django.utils.http import url_has_allowed_host_and_scheme


def users_register_view(request):
    """
        Register a new user.
        Is related to :model:'accounts.User'.
    """
    form = UsersForm(request.POST or None)
    context = {
         "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email = form.cleaned_data.get("email")
        new_users_email = UsersEmail.objects.create(email=email)
        request.session['users_email_id'] = new_users_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")
    return redirect("/register/")


class LoginView(FormView):
    """
    Login the user.
    Is related to :model:'accounts.User'.
    """
    form_class = LoginForm
    success_url = '/api/pesquisa/'
    template_name = 'accounts/login.html'
    default_next = '/api/pesquisa/'

    def form_valid(self, form):
        """
        Show the form so the user can login.
        Is related to :model:'accounts.User'.
        """
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['users_email_id']
            except:
                pass
            if url_has_allowed_host_and_scheme(redirect_path, request.get_host(), require_https=False):
                return redirect(redirect_path)
            else:
                return redirect("/api/pesquisa/")
        return super(LoginView, self).form_invalid(form)


class RegisterView(CreateView):
    """
    Is a view to register a new user.
    Is related to :model:'accounts.User'.
    """
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'
