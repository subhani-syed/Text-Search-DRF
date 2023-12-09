from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.postgres.search import SearchVector, SearchRank
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import ParagraphSerializer, ParagraphDTOSerializer
from .models import Paragraph


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@swagger_auto_schema(query_serializer=ParagraphDTOSerializer)
def upload_paragraph(request):
    """
    Stores each paragraph from the payload with a unique key in the DB

    Returns:
    - Response: If upload is successfull returns HTTP status 200,
                In case of any errors returns HTTP status 400
    """
    if request.method == "POST":
        try:
            # Extracting paragraphs from the payload and saving them individually
            payload = request.POST['payload']
            paragraphs = payload.split("\n\n")

            for paragraph_text in paragraphs:
                paragraph = Paragraph(description=paragraph_text)
                paragraph.save()

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        response = {
            "message": "Paragraphs uploaded successfully",
            "description": "Uploaded paragraphs successfully"
        }
        return Response(response, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@swagger_auto_schema(request_body=ParagraphSerializer)
def perform_search(request):
    """
    Searches for paragraphs containing the specified search text

    Returns:
    - Response: If search text is found returns HTTP status 200 and list of relevant paragraphs,
                If search text is not found returns HTTP status 200 and empty list as output,
                In case of any errors returns HTTP status 400
    """
    if request.method == "POST":
        try:
            # Extracting the search text and performing full-text search on the paragraphs
            search_text = request.POST['search_text']
            output = []

            if search_text:
                # Searching for relevant paragraphs based on the provided text
                vector = SearchVector('description')
                query = search_text

                # SearchRank searches the query in the vector and gives ranking
                # Filtering the result on given threshold rank and order by rank in descending order
                match_paras = Paragraph.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.001).order_by('-rank')
                serializer = ParagraphSerializer(match_paras, many=True)
                output = serializer.data

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        response = {
            "message": "Paragraphs fetched successfully",
            "description": "Fetched paragraphs containing the search text",
            "results": output
        }
        return Response(response, status=status.HTTP_200_OK)
