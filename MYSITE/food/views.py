from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse
from .models import Item
from django.template import loader
from MYSITE.forms import ItemForm

def home_page(request):
    return HttpResponse("<h1><center> Welcome My first Page</cemter></h1>")


# # First way
# def get_data(request):
#     data = Item.objects.all()
#     template = loader.get_template('food/index.html')
#     context = {'data': data}
#     return HttpResponse(template.render(context, request))

# first way
def get_data(request):
    data = Item.objects.all()
    context = {'data': data}
    return render(request, "food/index.html", context)


def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context={'item':item}
    return render(request,"food\detail.html",context)


def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:alldata")
    return render(request, 'food/item-forms.html', {'form': form})


def update_item(request, id):
    # item = get_object_or_404(Item, id=id) 
    item = Item.objects.get(id=id) 
    form = ItemForm(request.POST or None, instance=item)
    
    if form.is_valid():
        form.save()
        return redirect("food:alldata")  # Ensure this URL name matches the name in your urls.py
    return render(request, 'food/item-forms.html', {'form': form, 'item': item})


def delete_item(request, item_id):
    item =Item.objects.get(id=item_id)
    if request.method== 'POST':
        item.delete()
        return redirect("food:alldata")
    return render(request, 'food/item-delete.html', {'item':item})