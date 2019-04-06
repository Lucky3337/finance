from .models import Index


def get_categories(request):
    return {
        'categories': Index.get_categories()
    }