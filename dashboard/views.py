from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from users.models import User  # use your actual user model import

@login_required
def dashboard_redirect_view(request):
    user = request.user
    if user.role == 'admin':
        return redirect('admin_dashboard')
    elif user.role == 'coach':
        return redirect('coach_dashboard')
    elif user.role == 'member':
        return redirect('member_dashboard')
    else:
        return render(request, 'dashboard/unknown_role.html')

@login_required
def admin_dashboard_view(request):
    return render(request, 'dashboard/admin_dashboard.html')

@login_required
def coach_dashboard_view(request):
    return render(request, 'dashboard/coach_dashboard.html')

@login_required
def member_dashboard_view(request):
    return render(request, 'dashboard/member_dashboard.html')
