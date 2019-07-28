from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from indian.serializers import WordsSerializer
from .models import  Words

# Create your views here.
def indian(request):
    india = India.objects
    return render(request,'indian/indian.html',{'india':india})


@api_view(['GET'])
def words_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    word = request.query_params.get("search")
    if request.method == 'GET':
        words_objs = Words.objects.filter(name__icontains=word).order_by("-frequency", "word_length")[:25]
        serializer = WordsSerializer(words_objs, many=True)
        return Response(serializer.data)
