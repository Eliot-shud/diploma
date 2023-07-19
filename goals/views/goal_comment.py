from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters, generics
from rest_framework.pagination import LimitOffsetPagination

from goals.models import GoalComment
from goals.permissions import GoalCommentPermission
from goals.serializers import GoalCommentSerializer, GoalCommentWithUserSerializer


class GoalCommentCreateView(generics.CreateAPIView):
    serializer_class = GoalCommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class GoalCommentListView(generics.ListAPIView):
    serializer_class = GoalCommentWithUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["goal"]
    ordering = ["-created"]

    def get_queryset(self):
        return GoalComment.objects.filter(goal__category__board__participants__user=self.request.user)


class GoalCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoalCommentWithUserSerializer
    permission_classes = [GoalCommentPermission]

    def get_queryset(self):
        return GoalComment.objects.select_related('user').filter(
            goal__category__board__participants__user=self.request.user
        )
