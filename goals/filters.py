from django_filters import rest_framework

from goals.models import Goals


class GoalFilter(rest_framework.FilterSet):
    class Meta:
        model = Goals
        fields = {
            "due_date": ["lte", "gte"],
            "category": ["in"],
            "status": ["in"],
            "priority": ["in"],
        }