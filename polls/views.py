from django.http import HttpResponse


def indexFunction(request):
    return HttpResponse("Hello, world. You're at the polls index.")