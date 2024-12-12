from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import QueryAPISerializer
import sys
from base.RagLlmImplemetation.query_data import Query
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    method='post',
    request_body=QueryAPISerializer,
    responses={
        200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'response': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='The LLM response to the anatomy question'
                )
            }
        )
    },
    operation_description="Endpoint to query the anatomy LLM with a question",
)
@api_view(['POST'])
def anatomy_llm(request):
    print(request.data, file=sys.stderr)
    serializer = QueryAPISerializer(data=request.data)
    que = Query()
    print("------------------------------------------",file=sys.stderr)
    result = que.runMain(query_text=serializer.initial_data['question'])
    return Response({"response":result})