from django.shortcuts import render, HttpResponse


def home(request):
    context = {
        'site_header': 'Exarth',
        'site_auther': 'Wolf',
    }
    return render(
        request=request, template_name='home.html',
        context=context
    )
