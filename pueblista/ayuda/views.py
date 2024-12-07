from django.shortcuts import render

# Create your views here.
def ayuda(request):
    user = request.user
    return render(request, 'ayuda.html', {'user': user})