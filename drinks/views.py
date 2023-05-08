from django.views.generic import TemplateView

from drinks.models import Beer


class BeerView(TemplateView):
    template_name = 'drinks/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            'beers': Beer.objects.filter(is_publish=True),
        })
        return context
