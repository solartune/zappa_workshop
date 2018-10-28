from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'main.html'

    def dispatch(self, request, *args, **kwargs):
        # hidden bug ^_^
        # raise ValueError()
        return super().dispatch(request, *args, **kwargs)
