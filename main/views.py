from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render

def landing_page(request):
    return render(request, 'main/landingpage.html')


@login_required
def dashboard_view(request):
    # Pass any required context for the dashboard
    return render(request, 'main/dashboard.html')
