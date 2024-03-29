from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from .forms import ClientForm, CompteForm, OperationForm
from .models import Compte, Client, Operation


def home(request):
    return render(request, 'base.html')

def admin(request):
    return render(request, 'admin/')


def allClients(request):
    clients = Client.objects.all()
    paginator = Paginator(clients, 10)
    page_number = request.GET.get('page')
    if page_number is not None:
        pageObj = paginator.get_page(page_number)
    else:
        pageObj = paginator.get_page(1)
    context = {'clients': pageObj}
    return render(request, 'clients.html', context)


def searchClient(request):
    searchedClients = Client.objects.filter(nom__icontains=request.GET.get("search", ""))
    paginator = Paginator(searchedClients, 10)
    page_number = request.GET.get('page')
    if page_number is not None:
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = paginator.get_page(1)
    context = {'clients': page_obj}
    return render(request, "clients.html", context)


def getClient(request, numero):
    client = Client.objects.get(numero=numero)
    context = {'client': client}
    return render(request, 'clients.html', context)


def operationsClient(request, numero):
    compte = Compte.objects.get(client=numero)
    operations = Operation.objects.get(compte=compte.numero)
    context = {'operations': operations}
    return render(request, 'clients.html', context)


def allComptes(request):
    comptes = Compte.objects.all()
    paginator = Paginator(comptes, 10)
    page_number = request.GET.get('page')
    if page_number is not None:
        pageObj = paginator.get_page(page_number)
    else:
        pageObj = paginator.get_page(1)
    context = {'comptes': pageObj}
    return render(request, 'comptes.html', context)

def searchCompte(request):
    searchedCompte = Compte.objects.filter(numero__icontains=request.GET.get("search", ""))
    paginator = Paginator(searchedCompte, 10)
    page_number = request.GET.get('page')
    if page_number is not None:
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = paginator.get_page(1)
    context = {'comptes': page_obj}
    return render(request, "comptes.html", context)


def view_client(request):
    form = ClientForm()
    return render(request, "formTemplate.html", {"form": form})


def view_compte(request):
    form = CompteForm()
    return render(request, "formTemplate.html", {"form": form})


def view_operation(request):
    form = OperationForm()
    return render(request, "formTemplate.html", {"form": form})
