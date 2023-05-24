from django.shortcuts import render, redirect
from app.forms import CarrosForm
from app.models import Carros
from django.core.paginator import Paginator
#from django.http import HttpResponse

# Create your views here.
def home(request):
    data = {}
    search= request.GET.get('search')
    if search:
        data['db'] = Carros.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Carros.objects.all()
    # all = Carros.objects.all()
    # paginator = Paginator(all, 2)
    # pages = request.GET.get('page')
    # data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)

def create(request):
    """
    Creates a new Car object based on the data provided by the form.

    Args:
        request (HttpRequest): The HttpRequest object containing the request data.

    Returns:
        HttpResponseRedirect: Redirects to the home page after saving the Car object.

    Example:
        In the following example, a valid form is submitted and the data is saved,
        redirecting the user to the home page.

        ### create(request)
        HttpResponseRedirect('/home')
    """
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')

## https://www.youtube.com/watch?v=PMjwCB5rShY&list=PLbnAsJ6zlidvszSXnxplfYgtB6KQ-fZ-N&index=7 