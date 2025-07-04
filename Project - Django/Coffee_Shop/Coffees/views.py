from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import UserForm,PlaceOrderForm
from .utils import generate_pdf

# Create your views here.
def manu(request):
    coffees = CoffeeTypes.objects.all()
    return render(request,"manu.html",{'coffees':coffees})

def about(request):
    staff = EmployeesData.objects.all()
    return render(request,"about.html",{'staff':staff})

def contact(request):
    if request.method == 'POST':
        register_form = UserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('/coffee/ordernow/') 
    else:
        register_form = UserForm()

    return render(request,"contact.html",{'register_form':register_form})


def ordernow(request):
    selected_coffee = None
    quentity = None
    total_price = None

    if request.method == 'POST':
        form = PlaceOrderForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            coffee = form.cleaned_data['coffee']
            quentity = form.cleaned_data['quantity']
            selected_coffee = coffee
            total_price = quentity * coffee.price

            Order = form.save(commit=False)
            Order.price = total_price
            Order.save()

            # Generate PDF 
            pdf = generate_pdf('invoice.html', {'Order': Order})

            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = f"Invoice_{Order.id}.pdf"
                content = f"attachment; filename={filename}"
                response['Content-Disposition'] = content
                return response
            
    else:
        form = PlaceOrderForm()

    coffees = CoffeeTypes.objects.all()        
      
    return render(request,"ordernow.html",{
        'form':form,
        'selected_coffee':selected_coffee,
        'quentity':quentity,
        'total_price':total_price,
        'coffees':coffees
        })