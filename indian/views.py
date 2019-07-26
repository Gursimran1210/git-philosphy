from django.shortcuts import render,get_object_or_404
from .models import India

# Create your views here.
def indian(request):
    india = India.objects
    return render(request,'indian/indian.html',{'india':india})

def inde(request,indian_id):
    inde = get_object_or_404(India, pk=indian_id)
    return render(request,'indian/inde.html',{'inde':inde})





