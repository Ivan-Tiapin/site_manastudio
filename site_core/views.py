from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from .forms import RegistrationFrom, AssetsDBForm
from .models import AssetsDB, LibraryDB
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Authentication magagement
def sign_up(request):
    if request.method == "POST":
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect ('/')
    else:
        form = RegistrationFrom()
    return render(request,'registration/sign_up.html',{'form':form})

def log_out(request):
    logout(request)

class CustomLoginView(LoginView):
    success_url = '/'  # Set a default success URL
    def form_valid(self, form):
        next_url = self.request.GET.get('next', self.success_url)
        self.success_url = next_url
        return super().form_valid(form)

# Asset management
@login_required
def asset_add(request):
    form = AssetsDBForm()
    if request.method == 'POST':
        form = AssetsDBForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render (request,'asset_add.html',context)

def assets_all(request):
    if request.method == 'POST':
        id = request.POST.get('asset_id')
        asset = get_object_or_404(AssetsDB, pk=id)
        LibraryDB.objects.create(user=request.user, asset=asset)
    assets = AssetsDB.objects.all()
    context = {'assets' : assets}

    if request.user.is_authenticated:
        saved_assets = LibraryDB.objects.filter(user = request.user)
        context['saved_assets'] = [el.asset for el in saved_assets]
    return render(request, 'assets_all.html', context)   

@login_required
def asset_update(request,id):
    asset = get_object_or_404(AssetsDB, pk=id)
    if request.method == 'POST':
        form = AssetsDBForm(request.POST, request.FILES, instance=asset)
        if form.is_valid():
            print('form is valid')
            form.save()    
            return redirect('/')
    else:
        form = AssetsDBForm(instance=asset)
    context = {'form': form}
    return render(request, 'asset_update.html', context)

@login_required
@require_POST
def asset_delete(request,id):
    asset = AssetsDB.objects.get(pk=id)
    next_url = request.POST.get('next', '/')
    if asset is not None:
        asset.image.delete()
        asset.delete()
    return redirect(next_url)

@login_required
def assets_library(request):
    user = request.user
    if request.method == 'POST':
        asset = request.POST.get('asset_id')
        saved_asset = LibraryDB.objects.get(user = user, asset = asset)
        saved_asset = get_object_or_404(LibraryDB,user = user, asset = asset)
        if asset is not None:
            saved_asset.delete() 
    assets = LibraryDB.objects.filter(user = user)
    return render(request, 'assets_library.html', {'assets': [el.asset for el in assets]}) 
