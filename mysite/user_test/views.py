from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from .models import Member
from rest_framework import viewsets
from .serializers import userSerializer
from django.http import HttpRequest
import json
request = HttpRequest()
request.method = 'POST'
request.content_type = 'application/json'
def index(request):
    context = {}
    # context['m_id'] = request.session['m_id']
    # context['m_name'] = request.session['m_name']

    # m_id 세션변수 값이 없다면 '' 을 넣어라
    context['m_id'] = request.session.get('m_id', '')
    context['m_name'] = request.session.get('m_name', '')

    return render(request, 'user_test/index.html', context)


def member_reg(request):
    if request.method == "GET":
        return render(request, 'user_test/member_reg.html')
    elif request.method == "POST":
        context = {}
        member_id = request.POST["member_id"]
        passwd = request.POST["passwd"]
        name = request.POST["name"]
        email = request.POST["email"]
        height = request.POST["height"]
        weight = request.POST["weight"]
        gender = request.POST["gender"]
        purpose = request.POST["purpose"]
        age = request.POST["age"]




        # 회원가입 중복체크
        rs = Member.objects.filter(member_id=member_id)
        if rs.exists():
            context['message'] = member_id + "가 중복됩니다."
            return render(request, 'user_test/member_reg.html', context)

        else:
            Member.objects.create(
                member_id=member_id, passwd=passwd, name=name, email=email, height=height,
                weight=weight, gender=gender, purpose=purpose, age=age)
            context['message'] = name + "님 회원가입 되었습니다."
            return render(request, 'user_test/index.html', context)



def member_login(request):
    if request.method == "GET":
        return render(request, 'user_test/login.html')
    elif request.method == "POST":
        context = {}

        member_id = request.POST.get('member_id')
        passwd = request.POST.get('passwd')

        # 로그인 체크하기
        rs = Member.objects.filter(member_id=member_id, passwd=passwd).first()
        print(member_id + '/' + passwd)
        print(rs)

        # if rs.exists():
        if rs is not None:

            # OK - 로그인
            request.session['m_id'] = member_id
            request.session['m_name'] = rs.name

            context['m_id'] = member_id
            context['m_name'] = rs.name
            context['message'] = rs.name + "님이 로그인하셨습니다."
            return render(request, 'user_test/index.html', context)

        else:

            context['message'] = "로그인 정보가 맞지않습니다.\\n\\n확인하신 후 다시 시도해 주십시오."
            return render(request, 'user_test/login.html', context)


def member_logout(request):
    request.session.flush()
    return redirect('/user')

def user_list(request):
    users = Member.objects.all().order_by('pk')

    return render(
        request,
        'user_test/list.html',
        {
            'users': users,
        }
    )

class userViewset(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = userSerializer
    data=serializer_class.data


@csrf_exempt
def userfind(request):
    if request.method == 'POST':
        # JSON 데이터를 가져옴
        json_data = request.body.decode('utf-8')

        try:
            # JSON 데이터를 파싱하여 필요한 처리 수행
            data = json.loads(json_data)
            id=data['id']
            members = Member.objects.get(member_id=id)

            name=members.name
            email=members.email
            height=members.height
            weight=members.weight
            gender=members.gender
            purpose=members.purpose
            age = members.age
            # 처리 결과를 JSON 응답으로 반환
            response_data = {
                'message': 'POST 요청이 성공적으로 처리되었습니다.',
                '이름': name,
                '이메일' : email,
                '키': height,
                '몸무게': weight,
                '성별':gender,
                '목적':purpose,
                '나이':age
            }
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            # JSON 데이터 파싱에 실패한 경우
            response_data = {
                'message': '잘못된 JSON 형식입니다.',
            }
            return JsonResponse(response_data, status=400)
    else:
        # POST 요청이 아닌 경우
        response_data = {
            'message': 'POST 요청이 아닙니다.',
        }
        return JsonResponse(response_data, status=405)