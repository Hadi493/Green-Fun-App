from django.shortcuts import render # type: ignore

# Create your views here.
def gfun(request):
    return render(request, 'gfun.html')