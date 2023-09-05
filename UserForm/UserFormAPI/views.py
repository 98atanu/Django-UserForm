from django.shortcuts import render, redirect
from .forms import ModelForm
from .models import UserForm


# Create your views here.
def home_user_form(request):
        form = UserForm.objects.all()
        if request.method == "POST":
            form = ModelForm(request.POST)
            if form.is_valid():
                form.save()
                
            form = UserForm.objects.all()    
            all_user = {'all_user': form}
            return render(request,"index.html", all_user)
        if request.method == "GET":
            all_user = {'all_user': form}
            return render(request,"index.html",all_user)
        
def delete_UserForm(request,pk):
    delete_info = UserForm.objects.get(pk=pk)
    delete_info.delete()      
    return redirect('/')

def update_UserForm(request,pk):
    update_info = UserForm.objects.get(pk=pk)
    if request.method=='POST':
        new_form = ModelForm(request.POST)
        if new_form.is_valid():
            update_info.customer_name = request.POST['customer_name']
            update_info.product_name = request.POST['product_name']
            update_info.price = request.POST['price']
            update_info.save()
            return redirect('/')
    return render(request, 'update.html', {'user_info': update_info})
    
    
    
        
    
    
    
        
        

    
     
    
        
            
    