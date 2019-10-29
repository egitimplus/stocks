from django.urls import path
from . import views

urlpatterns = [
    path('accounts/role/', views.RoleView.as_view(), name='role-list'),
    path('accounts/distributor/<int:pk>', views.DistributorRoleView.as_view(), name='distributor-home'),
    path('accounts/dealer/<int:pk>', views.DealerRoleView.as_view(), name='dealer-home')

]

