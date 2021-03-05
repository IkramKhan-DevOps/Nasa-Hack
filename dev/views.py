from django.shortcuts import render, HttpResponse


def home(request):
    v = 2 + 2
    return HttpResponse(f'HELLO ALI HOME = {v}')


def about(request):
    return HttpResponse('HELLO ALI ABOUT')


def contact(request):
    return HttpResponse('HELLO ALI CONTACT')


def blog(request):
    return HttpResponse('HELLO ALI BLOG')


def sum(request):
    return HttpResponse('HELLO ALI BLOG')


def security(request):
    message = "User is Not authenticated"
    if request.user.is_authenticated:
        message = f"Welcome MR {request.user.username}"

    return HttpResponse(message)
