from django.shortcuts import render,redirect
from .models import HeaderModel,MiddleModel,FooterModel
from .forms import CombinedForm,HeaderForm,MiddleForm,FooterForm

def home(request):
    return render(request, 'html.html')


def create(request):
    if request.method == "POST":
        form = CombinedForm(request.POST)
        if form.is_valid():
            HeaderModel.objects.create(
                number = form.cleaned_data['user_number'],
                text = form.cleaned_data['user_text'],
                time = form.cleaned_data['user_time']
            )
            MiddleModel.objects.create(

                title = form.cleaned_data['user_title'],       
            )
            FooterModel.objects.create(
                text = form.cleaned_data['text'],
                description = form.cleaned_data['user_description']
                
            )
            return redirect('list')
    else:
        form = CombinedForm()
    return render(request, 'create.html', {"form":form})

def list(request):
    product1 = HeaderModel.objects.all() 
    product2 = MiddleModel.objects.all() 
    product3 = FooterModel.objects.all() 
    context = {
        "product1":product1,
        "product2":product2,
        "product3":product3
    }
    return render(request, 'list.html', context)

def delete(request,id):
    product1 = HeaderModel.objects.get(id=id).delete()
    product2 = MiddleModel.objects.get(id=id).delete()
    product3 = FooterModel.objects.get(id=id).delete()
    return redirect( 'list')


def update(request, id):
    product1 = HeaderModel.objects.get(id=id)
    product2 = MiddleModel.objects.get(id=id)
    product3 = FooterModel.objects.get(id=id)
    if request.method == 'POST':
        form1 = HeaderForm(request.POST, instance=product1)
        form2 = MiddleForm(request.POST, instance=product2)
        form3 = FooterForm(request.POST, instance=product3)
        if form1.is_valid():
            form1.save()
            return redirect('list')
        if form2.is_valid():
            form2.save()
            return redirect('list')
        if form3.is_valid():
            form3.save()
            return redirect('list')
    else:
        form1 = HeaderForm( instance=product1)
        form2 = MiddleForm(instance=product2)
        form3 = FooterForm(instance=product3)
    return render(request, 'create.html', {'form1':form1,'form2':form2,'form3':form3})








    


















































