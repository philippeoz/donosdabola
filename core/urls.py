from django.conf.urls import include, url
from .views import *
from .forms import CadastroCampoForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from class_based_auth_views.views import LoginView, LogoutView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home_page'),

    url(r'cliente/add/$', cliente_create, name='cliente_add'),

    url(r'cliente/(?P<pk>[0-9]+)/$', cliente_update, name='cliente_update'),

    url(r'cliente/(?P<pk>[0-9]+)/delete/$', cliente_delete, name='cliente_delete'),

    url(r'campo/add/$', campo_create, name='campo_add'),

    url(r'campo/(?P<pk>[0-9]+)/$', campo_update, name='campo_update'),

    url(r'campo/(?P<pk>[0-9]+)/delete/$', campo_delete, name='campo_delete'),

    url(r'reserva/add/$', reserva_create, name='reserva_add'),

    url(r'reserva/(?P<pk>[0-9]+)/$', reserva_update, name='reserva_update'),

    url(r'reserva/(?P<pk>[0-9]+)/delete/$', reserva_delete, name='reserva_delete'),

    url(r'^login/$', csrf_exempt(LoginView.as_view(form_class=AuthenticationForm)), name="login"),

    url(r'^logout/$', csrf_exempt(LogoutView.as_view()), name="logout"),

    url(r'^accounts/profile/$',csrf_exempt(DashboardView.as_view()), name='dashboard'),

    url(r'^accounts/login/$',csrf_exempt(LoginView.as_view(form_class=AuthenticationForm)), name="login"),
]

