from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'RoundTable/base/index.html'