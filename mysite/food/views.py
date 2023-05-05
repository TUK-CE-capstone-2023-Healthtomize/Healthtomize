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
        rate = int(serving_size)/int(foods.serving_size)

        if amount is '':
            context['list'] = str(food_name)+str(serving_size)+'g '
            context['amount'] = int(serving_size)
            context['calories'] = round(int(foods.calories)*rate,2)
            context['carbon'] = round(int(foods.carbon)*rate,2)
            context['protein'] = round(int(foods.protein)*rate,2)
            context['fat'] = round(int(foods.fat)*rate,2)
            context['cholesterol'] = round(int(foods.cholesterol)*rate,2)

        else:
            context['list'] = str(list)+str(food_name)+str(serving_size)+'g '
            context['amount'] = int(amount)+int(serving_size)
            context['calories'] = round(float(calories)+int(foods.calories)*rate,2)
            context['carbon'] = round(float(carbon)+int(foods.carbon)*rate,2)
            context['protein'] = round(float(protein)+int(foods.protein)*rate,2)
            context['fat'] = round(float(fat)+int(foods.fat)*rate,2)
            context['cholesterol'] = round(float(cholesterol)+int(foods.cholesterol)*rate,2)



        return render(request, 'food/food_input.html',context)
        # if rs.exists():

def feedback(request):
    if request.method == "GET":
        return render(request, 'food/feedback.html')

    elif request.method == "POST":
        context = {}

        recommend_calories = request.POST.get('recommend_calories')
        used_calories = request.POST.get('used_calories')
        calories = request.POST.get('calories')
        base_calories = request.POST.get('base_calories')



        context['calories'] = calories


        context['feedback'] = ' '
        if used_calories is not None:
            context['feedback'] = round(float(recommend_calories)-float(used_calories)+float(calories)-float(base_calories),2)
            context['used_calories'] = int(used_calories) + int(base_calories)
            context['recommend_calories'] = recommend_calories
        return render(request, 'food/feedback.html',context)