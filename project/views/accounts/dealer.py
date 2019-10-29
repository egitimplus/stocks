from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.db.models import Q
from project.models import Dealer

class DealerRoleView(LoginRequiredMixin, View):

    def get(self, request, pk=None):
        role_page = request.session.get('role_page', False)

        if role_page == 'dealer':
            dealer = Dealer.objects.get(pk=pk)
        else:
            dealer = Dealer.objects.filter((Q(author=request.user) | Q(staff=request.user)) & Q(id=pk)).first()

            if dealer:
                request.session['role_page'] = 'dealer'
                request.session['role_id'] = pk
                request.session['role_name'] = dealer.name
            else:
                return redirect('role-list')

        context = {
            'dealer': dealer
        }

        return render(request=request, template_name='project/accounts/dealer.html', context=context)
