from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import TeamMember


# Create your views here.
class TeamMemberListView(ListView):
    model = TeamMember
    paginate_by = 10
    template_name = "team_member_list.html"


class TeamMemberCreateView(CreateView):
    model = TeamMember
    fields = ["first_name", "last_name", "email", "phone", "role"]
    template_name = "team_member_create.html"
    success_url = reverse_lazy("team-member-list")


class TeamMemberUpdateView(UpdateView):
    model = TeamMember
    fields = ["first_name", "last_name", "email", "phone", "role"]
    template_name = "team_member_update.html"
    success_url = reverse_lazy("team-member-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_id"] = self.object.id
        return context


class TeamMemberDeleteView(DeleteView):
    model = TeamMember
    template_name = "team_member_delete.html"
    success_url = reverse_lazy("team-member-list")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_id"] = self.object.id
        return context
