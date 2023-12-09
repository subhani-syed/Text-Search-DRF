from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.postgres.search import SearchVector,SearchRank
from rest_framework import status
from .models import Paragraph
from .serializers import ParagraphSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_paragraph(request):
    """
    Stores each paragraph in the payload with a unique key in the DB

    Returns:
    - Response: Uploaded Paragraph data 
    """
    if request.method == "POST":
        try:
            # Extracting paragraphs from the payload and saving them individually
            payload = request.POST['payload']
            paragraphs = payload.split("\n\n")

            for paragraph_text in paragraphs:
                paragraph = Paragraph(description = paragraph_text)
                paragraph.save()
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        response = {
            "message": "Paragraphs uploaded successfully",
            "description": "Uploaded paragraphs successfully"
        }
        return Response(response,status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def search_text(request):
    """
    Searches for paragraphs containing the specified search text

    Returns:
    - Response: List of relevant paragraphs
    """
    if request.method == "POST":
        try:
            # Extracting the search text and performing full-text search on the paragraphs
            search_text = request.POST['search_text']
            payload = None

            if search_text:
                # Searching for relevant paragraphs based on the provided text
                vector = SearchVector('description')
                query = search_text
                match_paras = Paragraph.objects.annotate(rank=SearchRank(vector,query)).filter(rank__gte=0.001).order_by('-rank')           
                serializer = ParagraphSerializer(match_paras,many=True)
                payload = serializer.data

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        response = {
            "message": "Paragraphs fetched successfully",
            "description": "Fetched paragraphs containing the search text",
            "results": payload
        }
        return Response(response,status=status.HTTP_200_OK)
