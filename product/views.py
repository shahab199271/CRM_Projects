from django.views.generic import ListView
from product import models


class ProductListView(ListView):
    """
    view for List of Products
    """
    model = models.Product
    template_name = 'list-products.html'
    paginate_by = 10

    def get_queryset(self):
        """
        search on Product list
        """
        search = self.request.GET.get('search', None)
        mode = self.request.GET.get('mode', None)
        if mode == 'name':
            products = models.Product.objects.filter(name__contains=search)
        elif mode == 'technical_specification':
            products = models.Product.objects.filter(technical_specification__contains=search)
        else:
            products = models.Product.objects.all()
        return products.order_by('-id')
