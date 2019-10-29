from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from project.models import Dealer, Distributor
from django.db.models import Q

class RoleView(LoginRequiredMixin, View):

    def get(self, request):

        dealers = Dealer.objects.filter(Q(author=request.user) | Q(staff=request.user))
        distributors = Distributor.objects.filter(Q(author=request.user) | Q(staff=request.user))

        context = {
            'dealers': dealers,
            'distributors' : distributors,
        }

        return render(request=request, template_name='project/accounts/role.html', context=context)

