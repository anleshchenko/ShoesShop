from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import *
from django.utils.translation import ugettext as _
from .forms import *


def index(request):
    shoes = Shoes.objects.all()
    entity_delete_name = 'delete-shoes'
    entity_update_name = 'update-shoes'
    return render(request, 'main/index.html', {'shoes': shoes, 'entity_delete_name': entity_delete_name,
                                               'entity_update_name': entity_update_name})


class IndexView(ListView):
    @staticmethod
    @login_required(login_url='login')
    def get(request, *args, **kwargs):
        shoes = Shoes.objects.all()
        entity_delete_name = 'delete-shoes'
        entity_update_name = 'update-shoes'
        return render(request, 'main/index.html', {'shoes': shoes, 'entity_delete_name': entity_delete_name,
                                                   'entity_update_name': entity_update_name})


# class ShoesCreateView(CreateView):
#     model = Shoes
#     template_name = 'main/add.html'
#     form_class = AddShoes
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['form'] = self.form_class
#         return context
#
#     def form_valid(self, form):
#         SKU = form.cleaned_data['SKU']
#         name = form.cleaned_data['name']
#         price = form.cleaned_data['price']
#         size = form.cleaned_data['size']
#         category = form.cleaned_data['category']
#         color = form.cleaned_data['color']
#         manufacturer = form.cleaned_data['manufacturer']
#         data = Shoes(SKU=SKU,
#                      name=name,
#                      price=price,
#                      size=size,
#                      category=category,
#                      color=color,
#                      manufacturer=manufacturer)
#         data.save()
#         return HttpResponseRedirect('/')


@login_required(login_url='login')
def add_shoes(request):
    if request.method == 'POST':
        form = AddShoes(request.POST)
        if form.is_valid():
            SKU = form.cleaned_data['SKU']
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            size = form.cleaned_data['size']
            category = form.cleaned_data['category']
            color = form.cleaned_data['color']
            manufacturer = form.cleaned_data['manufacturer']
            data = Shoes(SKU=SKU,
                         name=name,
                         price=price,
                         size=size,
                         category=category,
                         color=color,
                         manufacturer=manufacturer)
            data.save()
            form = AddShoes()
    else:
        form = AddShoes()
    return render(request, 'main/add.html', {'form': form})


@login_required(login_url='login')
def update_shoes(request, id):
    if request.method == 'POST':
        data = Shoes.objects.get(pk=id)
        form = AddShoes(request.POST, instance=data)
        if form.is_valid():
            form.save()
    else:
        data = Shoes.objects.get(pk=id)
        form = AddShoes(instance=data)
    return render(request, 'main/update.html', {'form': form})


@login_required(login_url='login')
def delete_shoes(request, id):
    if request.method == 'POST':
        data = Shoes.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')


@login_required(login_url='login')
def show_manufacturers(request):
    manufacturers = Manufacturer.objects.all()
    page_name = _('Manufacturers')
    entity_delete_name = 'delete-manufacturer'
    entity_update_name = 'update-manufacturer'

    return render(request, 'main/show.html',
                  {'data': manufacturers, 'page_name': page_name, 'entity_delete_name': entity_delete_name,
                   'entity_update_name': entity_update_name})


@login_required(login_url='login')
def add_manufacturer(request):
    if request.method == 'POST':
        form = AddManufacturer(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            data = Manufacturer(name=name)
            data.save()
            form = AddManufacturer()
    else:
        form = AddManufacturer()
    return render(request, 'main/add.html', {'form': form})


@login_required(login_url='login')
def update_manufacturer(request, id):
    if request.method == 'POST':
        data = Manufacturer.objects.get(pk=id)
        form = AddManufacturer(request.POST, instance=data)
        if form.is_valid():
            form.save()
    else:
        data = Manufacturer.objects.get(pk=id)
        form = AddManufacturer(instance=data)
    return render(request, 'main/update.html', {'form': form})


@login_required(login_url='login')
def delete_manufacturer(request, id):
    if request.method == 'POST':
        data = Manufacturer.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/manufacturers')


@login_required(login_url='login')
def show_categories(request):
    categories = Category.objects.all()
    page_name = _('Categories')
    entity_delete_name = 'delete-category'
    entity_update_name = 'update-category'
    return render(request, 'main/show.html',
                  {'data': categories, 'page_name': page_name, 'entity_delete_name': entity_delete_name,
                   'entity_update_name': entity_update_name})


@login_required(login_url='login')
def add_category(request):
    if request.method == 'POST':
        form = AddCategory(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            data = Category(name=name)
            data.save()
            form = AddCategory()
    else:
        form = AddCategory()
    return render(request, 'main/add.html', {'form': form})


@login_required(login_url='login')
def update_category(request, id):
    if request.method == 'POST':
        data = Category.objects.get(pk=id)
        form = AddCategory(request.POST, instance=data)
        if form.is_valid():
            form.save()
    else:
        data = Category.objects.get(pk=id)
        form = AddCategory(instance=data)
    return render(request, 'main/update.html', {'form': form})


@login_required(login_url='login')
def delete_category(request, id):
    if request.method == 'POST':
        data = Category.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/categories')


@login_required(login_url='login')
def show_colors(request):
    colors = Color.objects.all()
    page_name = _('Colors')
    entity_delete_name = 'delete-color'
    entity_update_name = 'update-color'
    return render(request, 'main/show.html',
                  {'data': colors, 'page_name': page_name, 'entity_delete_name': entity_delete_name,
                   'entity_update_name': entity_update_name})


@login_required(login_url='login')
def add_color(request):
    if request.method == 'POST':
        form = AddColor(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            data = Color(name=name)
            data.save()
            form = AddColor()
    else:
        form = AddColor()
    return render(request, 'main/add.html', {'form': form})


@login_required(login_url='login')
def update_color(request, id):
    if request.method == 'POST':
        data = Color.objects.get(pk=id)
        form = AddColor(request.POST, instance=data)
        if form.is_valid():
            form.save()
    else:
        data = Color.objects.get(pk=id)
        form = AddColor(instance=data)
    return render(request, 'main/update.html', {'form': form})


@login_required(login_url='login')
def delete_color(request, id):
    if request.method == 'POST':
        data = Color.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/colors')


def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        login_form = CreateUserForm()

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password1')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, _('WrongData'))

        context = {'form': login_form}
        return render(request, 'auth/login.html', context)


def userLogout(request):
    logout(request)
    return redirect('login')


def userRegister(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        register_form = CreateUserForm()

        if request.method == 'POST':
            register_form = CreateUserForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request, _('RegistrationSuccess'))
                return redirect('login')

        context = {'form': register_form}
        return render(request, 'auth/register.html', context)
