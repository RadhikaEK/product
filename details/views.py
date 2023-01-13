from django.shortcuts import render
from details.models import Details
# Create your views here.

def add(request):
    if request.method=='POST':
        obj=Details()
        obj.material_type=request.POST.get('Meterial type')
        obj.name=request.POST.get('name')
        obj.category=request.POST.get('category')
        obj.size=request.POST.get('size')
        obj.save()
    return render(request,'details/add.html')


def search(request):
    if request.method=='POST':
        vv=request.POST.get('search')
        obj=Details.objects.filter(name__icontains=vv)
        context={
            'x':obj
        }
        return render(request,'details/view_search.html',context)
    else:
        obj=Details.objects.all()
        context={
            'x':obj
        }
    return render(request,'details/view_search.html',context)

    
