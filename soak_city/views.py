from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Water
from django.urls import reverse_lazy

class WaterListView(ListView):
  template_name = 'water_list.html'
  model = Water

class WaterDetailView(DetailView):
  template_name = 'water_detail.html'
  model = Water

class WaterCreateView(CreateView):
  template_name = 'water_create.html'
  model = Water
  fields = ['name', 'description', 'ph_level', 'electrolyte', 'cost']

class WaterUpdateView(UpdateView):
  template_name = 'water_update.html'
  model = Water
  fields = "__all__"

class WaterDeleteView(DeleteView):
  template_name = 'water_delete.html'
  model = Water
  success_url = reverse_lazy("Water_list")
