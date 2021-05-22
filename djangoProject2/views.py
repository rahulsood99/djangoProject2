from django.http import HttpResponse, JsonResponse
# from djangoProject2.books.models import Book
from djangoProject2.books.serializers import BookSerializer
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def index(request):
    if request.method == 'GET':
        return HttpResponse("Welcome ! %s" % request.method)
    elif request.method == 'POST':
        # print(request)
        # image = request.FILES['image']
        # mystr = request.data['str1']
        # print(mystr)
        return JsonResponse({"text": "text", "method": request.method,
                             "success_message": "Sample Success Message"},
                            status=200)
    else:
        pass

# def api(request, question_id):


# def detail(request, question_id):
#     # books = Book.objects.all()
#     books = Book.objects.filter(id=question_id)
#     serializer = BookSerializer(books, many=True)
#     return JsonResponse(serializer.data, safe=False)
#     # return HttpResponse({})
#     # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
