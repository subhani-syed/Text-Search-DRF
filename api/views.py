from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Paragraph
from django.contrib.postgres.search import SearchVector,SearchRank
from .serializers import ParagraphSerializer
from rest_framework import status

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_paragraph(request):
    if request.method == "POST":
        
        payload = request.POST['payload']
        paragraphs = payload.split("\n\n")

        for paragraph_text in paragraphs:
            paragraph = Paragraph(description = paragraph_text)
            paragraph.save()

        response = {
            "message" : "Paragraph(s) uploaded",
            "description": "Successfully uploaded paragraphs"
        }
        return Response(response,status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def search_text(request):
    if request.method == "POST":
        
        search_text = request.POST['search_text']
        print(search_text)

        payload = None
        if search_text:
            vector = SearchVector('description')
            query = search_text
            match_paras = Paragraph.objects.annotate(rank=SearchRank(vector,query)).filter(rank__gte=0.001).order_by('-rank')            
            serializer = ParagraphSerializer(match_paras,many=True)
            payload = serializer.data
        else:
            pass

        response = {
            "message":"Paragraph(s) fetched",
            "body":payload,
            "description":"Fetched the paragraphs"
        }
        return Response(response,status=status.HTTP_200_OK)

