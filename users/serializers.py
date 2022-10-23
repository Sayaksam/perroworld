from rest_framework import serializers
from .models import Users, Posts


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "number",
            "country_code",
            "location",
            "birth_day",
        ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts

        fields = [
            "id",
            "subject",
            "description",
            "creator",
            "topic_ids",
            "community_ids",
            "appreciator_ids",
            "comment_ids",
            "created_at",
        ]
