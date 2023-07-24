from typing import Type, Dict, Optional

from django.http import HttpResponse
from django_components.component_registry import registry as component_registry
from django_components.component import Component
from django.template.context import Context
from django.urls import path


def component_render_view(request, component_id: str):
    component_cls: Type[Component] = component_registry.all().get(component_id)
    component: Component = component_cls()
    try:
        storybook_parameters = {
            param: request.GET.get(param) for param in component.storybook_parameters
        }
    except AttributeError:
        storybook_parameters = {}
    component_context: Dict[str, Optional[str]] = component.get_context_data(
        **storybook_parameters
    )
    rendered_component = component.render(Context(component_context))
    return HttpResponse(rendered_component, headers={"Access-Control-Allow-Origin": "*"})


component_urls = [
    path("<str:component_id>", component_render_view),
]
