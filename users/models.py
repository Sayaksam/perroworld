from email.policy import default
from enum import auto
from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid

# Create your models here.


class Users(models.Model):
    first_name = models.CharField(max_length=2000)
    last_name = models.CharField(max_length=500)
    email = models.EmailField(null=True)
    password = models.CharField(null=True, max_length=2000)
    number = models.CharField(null=True, max_length=20)
    country_code = models.CharField(null=True, max_length=6)
    location = models.CharField(null=True, max_length=2000)
    birth_day = models.DateField(null=True)
    # follower_ids = ArrayField(models.IntegerField(), null=True, default=list())
    # post_ids = ArrayField(models.IntegerField(), null=True, default=list())
    # following_ids = ArrayField(models.IntegerField(), null=True, default=list())
    # community_ids = ArrayField(models.IntegerField(), null=False, default=list())

    class Meta:
        db_table = "Users"


class UserFollowers(models.Model):
    user = models.ForeignKey("Users", on_delete=models.CASCADE, blank=True)
    follower_id = models.IntegerField(blank=True)

    class Meta:
        db_table = "UserFollowers"


class Topics(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)

    class Meta:
        db_table = "Topics"


class Communities(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    topics = ArrayField(models.CharField(max_length=2000))
    creator = models.ForeignKey("Users", on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = "Communities"


class UserCommunity(models.Model):
    user = models.ForeignKey("Users", on_delete=models.CASCADE, blank=True)
    community = models.ForeignKey("Communities", on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = "UserCommunity"


class UserTopics(models.Model):
    user = models.ForeignKey("Users", on_delete=models.CASCADE, blank=True)
    topic = models.ForeignKey("Topics", on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = "UserTopics"


class Posts(models.Model):
    subject = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True)
    creator = models.ForeignKey("Users", on_delete=models.CASCADE, blank=True)
    topic_ids = ArrayField(models.IntegerField(), null=True, default=list())
    community_ids = ArrayField(models.IntegerField(), null=True, default=list())
    appreciator_ids = ArrayField(models.IntegerField(), null=True, default=list())
    comment_ids = ArrayField(models.IntegerField(), null=True, default=list())
    created_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "Posts"


class Comments(models.Model):
    creator = models.ForeignKey("Users", on_delete=models.CASCADE, blank=True)
    description = models.TextField(null=True)
    appreciator_ids = ArrayField(models.IntegerField(), null=True, default=list())
    thread_id = models.TextField(null=True)
    post = models.ForeignKey("Posts", on_delete=models.CASCADE, blank=True, null=True)
    isNestedComment = models.BooleanField(default=False)
    parentComment = models.ForeignKey(
        "Comments", on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        db_table = "Comments"
