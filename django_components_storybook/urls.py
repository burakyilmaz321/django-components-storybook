from django.urls import path

from .views import component_render_view

urlpatterns = [
    path("<str:component_id>", component_render_view),
]
