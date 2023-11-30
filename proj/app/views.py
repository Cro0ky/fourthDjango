from django.http import HttpResponse
from django.shortcuts import render

clients = [
    {
        'id': 1,
        'name': 'Tom',
        'lang': 'C++'
    },
    {
        'id': 2,
        'name': 'Evgeny',
        'lang': 'Python'
    },
    {
        'id': 3,
        'name': 'Sasha',
        'lang': 'JS'
    },
    {
        'id': 4,
        'name': 'Masha',
        'lang': 'C#'
    },
    {
        'id': 5,
        'name': 'Dima',
        'lang': 'Paskal'
    },
]


def index(request):
    header = 'Данные пользователя'
    langs = ['python', 'C', 'C#', 'C++', 'JS']
    user = {'name': 'Евгений', 'age': 16}
    address = ("Октябрьская", 12, 213)
    text = '<p>My Text</p>'

    data = {
        'header': header,
        'langs': langs,
        'user': user,
        'address': address,
        'text': text,
        'clients': clients,
    }

    return render(request, 'index.html', context=data)


def about(request):
    return render(request, 'about.html', context={'clients': clients})


def contacts(request):
    return render(request, 'contacts.html', context={'clients': clients})


def client(request, id):
    return render(request, 'client.html', context={'id': id, 'clients': clients})


def clientView(request):
    return render(request, 'clients.html', context={'clients': clients})
