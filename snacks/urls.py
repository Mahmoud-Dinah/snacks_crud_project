from django.urls import path
from .views import SnackCreatetView, SnackDeleteView, SnackDetailView, SnackListView, SnackUpdateView

urlPatterns = [
path('', SnackListView.as_view(),name ='snack_list' ),
path('<int:pk>/',SnackDetailView.as_view() ,name = 'snack_detail'),
path('new/',SnackCreatetView.as_view() ,name = 'snack_create'),
path('<int:pk>/edit',SnackUpdateView.as_view ,name = 'snack_update'),
path('<int:pk>/delete',SnackDeleteView.as_view(),name = 'snack_delete'),
]