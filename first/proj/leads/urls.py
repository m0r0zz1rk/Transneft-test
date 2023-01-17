from django.urls import path

from leads.views import LeadsChangeStatusViewSet

urlpatterns = [
    path('lead_worked/<int:pk>/', LeadsChangeStatusViewSet.as_view({'get': 'lead_worked'})),
    path('lead_paused/<int:pk>/', LeadsChangeStatusViewSet.as_view({'get': 'lead_paused'})),
    path('lead_complete/<int:pk>/', LeadsChangeStatusViewSet.as_view({'get': 'lead_complete'})),
    path('lead_continue/<int:pk>/', LeadsChangeStatusViewSet.as_view({'get': 'lead_continue'})),
    path('lead_stop_complete/<int:pk>/', LeadsChangeStatusViewSet.as_view({'get': 'lead_stop_complete'})),
]