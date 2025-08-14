# office/urls.py
from django.urls import path
from .views import kyc_bulk_delete
from . import views
app_name = 'kyc'

urlpatterns = [
    path('', views.home, name='home'),
    path('kyc_form/', views.kyc_create_view, name='kyc_create'),
    path('kyc_success/', views.kyc_success_view, name='kyc_success'),
    path('kyc_form/<int:kyc_id>/', views.kyc_update_view, name='kyc_form_update'),
    path('kyc_list/', views.kyc_list_view, name='kyc_list'),
    path('kyc/<int:kyc_id>/delete/', views.kyc_delete_view, name='kyc_delete'),
    path('kyc_lists/', views.kyc_lists_view, name='kyc_lists'),
    path('<int:kyc_id>/update/', views.kyc_update_view, name='kyc_update'), 
    path('bulk-delete/', kyc_bulk_delete, name='kyc_bulk_delete'),
    path('kyc_detail/<int:kyc_id>/', views.kyc_detail_view, name='kyc_detail'),
]