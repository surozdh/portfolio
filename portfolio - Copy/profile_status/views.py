from django.shortcuts import render

# Create your views here.
def propro(request):
    return render(request,'profile_status/profile/home.html')

def Statistics(request):
    return render(request,'profile_status/Statistics.html')