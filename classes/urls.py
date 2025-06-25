from django.urls import path
from .views import (
    ClassCreateView, ClassListView, ClassDetailView
)

urlpatterns = [
    path('', ClassListView.as_view(), name='class-list'),                    # GET /api/v1/classes/
    path('create/', ClassCreateView.as_view(), name='class-create'),         # POST /api/v1/classes/create/
    path('<int:pk>/', ClassDetailView.as_view(), name='class-detail'),       # GET/PUT/DELETE /api/v1/classes/<id>/
   ]