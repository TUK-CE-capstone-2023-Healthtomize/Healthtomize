from django.shortcuts import render
from .models import food
# Create your views here.
def index(request):

    return render(request, 'food/index.html')

def food_info_input(request):
    if request.method == "GET":
        return render(request, 'food/food_info_input.html')
    elif request.method == "POST":
        context = {}
        food_name = request.POST["food_name"]
        serving_size = request.POST["serving_size"]
        carbon = request.POST["carbon"]
        calories = request.POST["calories"]
        protein = request.POST["protein"]
        fat = request.POST["fat"]
        cholesterol = request.POST["cholesterol"]

        # 회원가입 중복체크
        rs = food.objects.filter(food_name=food_name)
        if rs.exists():
            context['message'] = food_name + "가 중복됩니다."
            return render(request, 'food/food_info_input.html', context)

        else:
            food.objects.create(
                food_name=food_name, serving_size=serving_size, calories=calories,carbon=carbon,
                protein=protein, fat=fat, cholesterol=cholesterol)
            context['message'] = food_name + "입력완료."
            return render(request, 'food/food_info_input.html', context)
    return render(request, 'food_info_input.html')


def food_list(request):
    foods = food.objects.all().order_by('pk')

    return render(
        request,
        'food/food_list.html',
        {
            'foods': foods,
        }
    )

def food_input(request):
    if request.method == "GET":
        return render(request, 'food/food_input.html')

    elif request.method == "POST":
        context = {}

        food_name = request.POST.get('food_name')
        serving_size = request.POST.get('serving_size')

        list = request.POST.get('list')
        amount = request.POST.get('amount')
        calories = request.POST.get('calories')
        carbon = request.POST.get('carbon')
        protein = request.POST.get('protein')
        fat = request.POST.get('fat')
        cholesterol = request.POST.get('cholesterol')
        foods = food.objects.get(food_name=food_name)

        if amount is '':
            context['list'] = str(food_name)+str(serving_size)+'g '
            context['amount'] = int(serving_size)
            context['calories'] = int(foods.calories)
            context['carbon'] = int(foods.carbon)
            context['protein'] = int(foods.protein)
            context['fat'] = int(foods.fat)
            context['cholesterol'] = int(foods.cholesterol)

        else:
            context['list'] = str(list)+str(food_name)+str(serving_size)+'g '
            context['amount'] = int(amount)+int(serving_size)
            context['calories'] = int(calories)+int(foods.calories)
            context['carbon'] = int(carbon)+int(foods.carbon)
            context['protein'] = int(protein)+int(foods.protein)
            context['fat'] = int(fat)+int(foods.fat)
            context['cholesterol'] = int(cholesterol)+int(foods.cholesterol)



        return render(request, 'food/food_input.html',context)
        # if rs.exists():
