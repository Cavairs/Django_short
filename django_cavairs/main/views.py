from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def omlet(request, servings=1):
    if request.method == 'POST':
        servings = int(request.POST.get("servings", 1))
        ingredients = {}
        for k, v in DATA['omlet'].items():
            ingredients[k] = v * servings
        return render(request, 'main/omlet.html', {'Ingredients': ingredients})
    else:
        return render(request, 'main/omlet.html')


def pasta(request):

    if request.method == 'POST':
        servings = int(request.POST.get("servings", 1))
        ingredients = {}
        for k, v in DATA['pasta'].items():
            ingredients[k] = v * servings
        return render(request, 'main/pasta.html', {'Ingredients': ingredients})
    else:
        return render(request, 'main/pasta.html')


def buter(request):

    if request.method == 'POST':
        servings = int(request.POST.get("servings", 1))
        ingredients = {}
        for k, v in DATA['buter'].items():
            ingredients[k] = v * servings
        return render(request, 'main/buter.html', {'Ingredients': ingredients})
    else:
        return render(request, 'main/buter.html')
