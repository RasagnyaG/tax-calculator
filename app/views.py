from django.shortcuts import render
from django.http import HttpResponse
from .utils import get_tax

# Create your views here.
def index(request):
    tax = None
    if request.method == "POST":
        income = request.POST.get('income')
        print(f"inc: {income}")
        if income:
            income = float(income) 
            tax = get_tax(income)
            print(tax)
    return render(request, 'calculator.html', {'tax': tax})
