from shop.models import category
def links(request):
    ca = category.objects.all()
    return {'ca':ca}