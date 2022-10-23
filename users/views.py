from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import CreateUserSerializer, PostSerializer
from rest_framework.response import Response
from .models import Users
from datetime import datetime

# Create your views here.


@api_view(["POST"])
def createUsers(request):
    f_name = request.data.get("first_name", None)
    l_name = request.data.get("last_name", None)
    email = request.data.get("email", None)
    number = request.data.get("number", None)
    country_code = request.data.get("country_code", None)
    location = request.data.get("location", None)
    birth_day = request.data.get("birth_day", None)

    user_data = {
        "first_name": f_name,
        "last_name": l_name,
        "email": email,
        "number": number,
        "country_code": country_code,
        "location": location,
        "birth_day": birth_day,
    }

    serializer = CreateUserSerializer(data=user_data)
    if serializer.is_valid():
        serializer.save()

        return Response(data={"Status": "User Created"})
    else:
        return Response(data={"status": "Error"})


@api_view(["POST"])
def createPost(request):
    sub = request.data.get("subject", None)
    desc = request.data.get("description", None)
    creator = request.data.get("creator", None)
    topics = request.data.get("topic_ids", None)
    communities = request.data.get("community_ids", None)
    appreciators = request.data.get("appreciator_ids", None)
    comments = request.data.get("comment_ids", None)
    created_at = datetime.utcnow()

    post_data = {
        "subject": sub,
        "description": desc,
        "creator": creator,
        "topic_ids": topics,
        "community_ids": communities,
        "appreciator_ids": appreciators,
        "comment_ids": comments,
        "created_at": created_at,
    }

    print(post_data)
    serializer = PostSerializer(data=post_data)

    if serializer.is_valid():
        serializer.save()
        return Response(data={"Status": "Post Created"})
    else:
        return Response(serializer.errors)
