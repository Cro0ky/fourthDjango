from django.shortcuts import render

data = {
    'school': 'Alabuga',
    'group': '3326',
    'work': 'Programmer',
    'future': 'xz',
    'fio': 'РЕД',
    'height': 173,
    'weight': 65,
    'age': 16,
    'phone': 86789087678,
    'tg': '@sfdfsfsdf',

}


def index(request):
    return render(request, 'sec_app/index.html', context=data)


def contacts(request):
    return render(request, 'sec_app/contacts.html', context=data)


def info(request):
    return render(request, 'sec_app/info.html', context=data)


def registrate(request):
    return render(request, 'sec_app/registrate.html', context=data)
