from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Article
from .serializers import ArticleSerializers
from rest_framework.parsers import JSONParser

def articleList(request):

    if( request.method == 'GET' ) :
        articles = Article.objects.all()
        serializer = ArticleSerializers(articles , many = True)
        return JsonResponse(serializer.data , safe = False)

    elif(request.method == 'POST'):
        data = JSONParser().parser(request)
        serializer = ArticleSerializers(data = data)

        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data , status = 201)
        return JsonResponse(serializer.error , status = 400)

# Create your views here.