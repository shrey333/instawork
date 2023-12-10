from django.urls import path

from .views import (
    TeamMemberCreateView,
    TeamMemberListView,
    TeamMemberUpdateView,
    TeamMemberDeleteView,
)

urlpatterns = [
    path("", TeamMemberListView.as_view(), name="team-member-list"),
    path("create", TeamMemberCreateView.as_view(), name="team-member-create"),
    path("update/<pk>", TeamMemberUpdateView.as_view(), name="team-member-update"),
    path("delete/<pk>", TeamMemberDeleteView.as_view(), name="team-member-delete"),
]
