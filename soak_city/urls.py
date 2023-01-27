from django.urls import path

from .views import WaterCreateView, WaterDeleteView, WaterListView, WaterDetailView, WaterUpdateView

urlpatterns = [
  path('', WaterListView.as_view(), name="water_list"),
  path('water/<int:pk>/', WaterDetailView.as_view(), name="water_detail"),
  path('water/create/', WaterCreateView.as_view(), name="water_create"),
  path('water/<int:pk>/update/', WaterUpdateView.as_view(), name="water_update"),
  path('water/<int:pk>/delete/', WaterDeleteView.as_view(), name="water_delete"),
]
