from django.shortcuts import render
from main.models import Phone


def index(request):
    sort_by = request.GET.get('sort_by', 'name')
    sort_order = request.GET.get('order', 'asc')
    #  минус для убывающей сортировки
    if sort_order == 'desc':
        sort_by = f"-{sort_by}"
    # выполняяем сортировку если sort_by й есть запрашиваемые ключи то вернем order_by(sort_by)
    if sort_by.lstrip('-') in ['name', 'price', 'release_date']:
        catalog = Phone.objects.all().order_by(sort_by)
    else:
        catalog = Phone.objects.all()
        sort_by = 'name'
    # список словарей
    phone_details = [
        {'name': phone.name, 'image': phone.image, 'price': phone.price,
         'release_date': phone.release_date, 'lte_exists': phone.lte_exists}
        for phone in catalog
    ]
    context = {
        'phone_details': phone_details,
        'current_sort': sort_by,
        'current_order': sort_order
    }

    return render(request, 'main/index.html', context)

    # def omlet(request, servings=1):
    #     if request.method == 'POST':
    #         servings = int(request.POST.get("servings", 1))
    #         ingredients = {}
    #         for k, v in DATA['omlet'].items():
    #             ingredients[k] = v * servings
    #         return render(request, 'main/omlet.html', {'Ingredients': ingredients})
    #     else:
    #         return render(request, 'main/omlet.html')

    # def pasta(request):

    #     if request.method == 'POST':
    #         servings = int(request.POST.get("servings", 1))
    #         ingredients = {}
    #         for k, v in DATA['pasta'].items():
    #             ingredients[k] = v * servings
    #         return render(request, 'main/pasta.html', {'Ingredients': ingredients})
    #     else:
    #         return render(request, 'main/pasta.html')

    # def buter(request):

    #     if request.method == 'POST':
    #         servings = int(request.POST.get("servings", 1))
    #         ingredients = {}
    #         for k, v in DATA['buter'].items():
    #             ingredients[k] = v * servings
    #         return render(request, 'main/buter.html', {'Ingredients': ingredients})
    #     else:
    #         return render(request, 'main/buter.html')
