import copy

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

QUESTIONS = [
    {
        'title': f"Как работает Python? {i}",
        'id': i,
        'text': f'Можете объяснить, как выполняется код на Python? {i}'
    }for i in range(30)
]

ANSWERS = [
    {
        'avatar': "../static/img/ava2.png",
        'id': 0,
        'like': 8,
        'text': 'Python — интерпретируемый язык программирования. Он не конвертирует свой код в машинный, который понимает железо (в отличие от С и С++). Вместо этого, Python-интерпретатор переводит код программы в байт-код, который запускается на виртуальной машине Python (PVM).',
        'correct': False
    }
]
for i in range(1, 10):
    ANSWERS.append({
        'avatar': f"../static/img/ava3.png",
        'id': i,
        'like': 8,
        'text': 'Работает и слава богу!',
        'correct': True
    })
def paginate(objects_list, request, per_page=10):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(objects_list, per_page)
    page = paginator.page(page_num)
    return page

# Create your views here.
def index(request):
    page = paginate(QUESTIONS,request,5)
    return render(request, 'index.html', context={'questions': page.object_list, 'page_obj':page })

def hot(request):
    q = list(reversed(copy.deepcopy(QUESTIONS)))
    page = paginate(q,request,5)
    return render(request, 'hot.html', context={'questions': page.object_list, 'page_obj': page})

def question(request, question_id):
    page = paginate(ANSWERS, request, 3)
    return render(request, 'question.html',context={"question" : QUESTIONS[question_id],'answers': page.object_list, 'page_obj': page})

def log(request):
    return render(request, 'login.html')

def reg(request,):
    return render(request, 'register.html')

def ask(request):
    return render(request, 'ask.html')
