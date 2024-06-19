from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from services.models import Order
from .models import Review, Article, Works
from .serializer import ReviewCreateSerializer, ReviewReadSerializer, ArticleReadSerializer, WorksReadSerializer


class ReviewViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ReviewReadSerializer

    def create(self, request, *args, **kwargs):
        self.serializer_class = ReviewCreateSerializer
        user_order = Order.objects.filter(customer=self.request.user, status=2).first()
        if user_order is None:
            return Response({'non_field_errors': "Чтобы оставить отзыв, нужно сделать заказ"}, status=403)
        user_reviews = Review.objects.filter(user=self.request.user).first()
        if user_reviews is not None:
            return Response({'non_field_errors': "Можно оставить только один отзыв"}, status=403)
        data = request.data
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleReadSerializer
    lookup_field = 'slug'

class WorksViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Works.objects.all()
    serializer_class = WorksReadSerializer

    def get_queryset(self):
        if 'l' in self.request.query_params is not None:
            queryset = self.queryset.all()[:int(self.request.query_params['l'])]
            if 'e' in self.request.query_params is not None:
                queryset = queryset.exclude(id=self.request.query_params['e'])
            return queryset
        return self.queryset
