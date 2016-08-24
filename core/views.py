from django.http import HttpRequest
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.shortcuts import render
from .models import Campo, Cliente
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator
from django.views import View


# Create your views here.
class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['lista_campos'] = Campo.objects.all()[:15]
        return context

class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        lista_campos = Campo.objects.all()
        # paginator  = Paginator(lista_campos,3)
        # page = HttpRequest.GET

        # try:
        #     campos = paginator.page(page)
        # except PageNotAnInteger:
        # # If page is not an integer, deliver first page.
        #     campos = paginator.page(1)
        # except EmptyPage:
        # # If page is out of range (e.g. 9999), deliver last page of results.
        # campos = paginator.page(paginator.num_pages)
        context['lista_clientes'] = Cliente.objects.all()
        context['lista_campos'] = lista_campos
        context['cliente'] = Cliente
        return context


class ClienteCreate(CreateView):
    model = Cliente
    form_class = CadastroClienteForm


class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = CadastroClienteForm


class ClienteDelete(DeleteView):
    model = Cliente
    form_class = CadastroClienteForm
    success_url = reverse_lazy('home_page')

class CampoCreate(CreateView):
    model = Campo
    form_class = CadastroCampoForm


class CampoUpdate(UpdateView):
    model = Campo
    form_class = CadastroCampoForm


class CampoDelete(DeleteView):
    model = Campo
    form_class = CadastroCampoForm
    success_url = reverse_lazy('dashboard')

class ReservaCreate(CreateView):
    model = Reserva
    form_class = CadastroReservaForm


class ReservaUpdate(UpdateView):
    model = Reserva
    form_class = CadastroReservaForm


class ReservaDelete(DeleteView):
    model = Reserva
    form_class = CadastroReservaForm
    success_url = reverse_lazy('dashboard')




cliente_create = csrf_exempt(ClienteCreate.as_view())
cliente_update = csrf_exempt(ClienteUpdate.as_view())
cliente_delete = csrf_exempt(ClienteDelete.as_view())
campo_create = csrf_exempt(CampoCreate.as_view())
campo_update = csrf_exempt(CampoUpdate.as_view())
campo_delete = csrf_exempt(CampoDelete.as_view())
reserva_create = csrf_exempt(ReservaCreate.as_view())
reserva_update = csrf_exempt(ReservaUpdate.as_view())
reserva_delete = csrf_exempt(ReservaDelete.as_view())