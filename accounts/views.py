from django.shortcuts import render
from .forms import SignupForm

# Create your views here.

def signup(request):
    if request.method=='POST':
        s=SignupForm(request.POST)
        if s.is_valid():
            s.save()
            return redirect('login')
    else:s=SignupForm()

    return render(request, 'accounts/signup.html', {'form':s})