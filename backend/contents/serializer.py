from django.contrib.sites.models import Site
from rest_framework import serializers
from .models import Review, Article, Works, WorksTasks, WorksTags
from users.serializer import UserSerializer

SEARCH_PATTERN = '/media/uploads/fimg/'
REPLACE_WITH = '{scheme}{domain}/media/uploads/fimg/'.format(
    scheme="http://",
    domain=Site.objects.get_current().domain
)


class FixAbsolutePathSerializer(serializers.Field):

    def to_representation(self, value):
        text = value.replace(SEARCH_PATTERN, REPLACE_WITH)
        print(text)
        return text


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['title', 'text', 'user']


class ReviewReadSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Review
        fields = ['title', 'text', 'user', 'created_at']


class ArticleReadSerializer(serializers.ModelSerializer):
    description = FixAbsolutePathSerializer()

    class Meta:
        model = Article
        fields = ["title", "description", "image", "author", "created_at", "slug"]
        lookup_field = 'slug'


class WorksTagsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorksTags
        fields = ['title']


class WorkTasksReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorksTasks
        fields = ['title']


class WorksReadSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = Works
        fields = ['title', 'subtitle', 'imageA', 'imageB', 'tags', 'tasks']

    def get_tags(self, obj):
        data = []
        for i in WorksTagsReadSerializer(WorksTags.objects.filter(works__tags=obj.id), many=True).data:
            data.append(i['title'])
        return data

    def get_tasks(self, obj):
        tasks = WorksTasks.objects.filter(work=obj)
        data = []
        for i in WorkTasksReadSerializer(tasks, many=True).data:
            data.append(i['title'])
        return data
