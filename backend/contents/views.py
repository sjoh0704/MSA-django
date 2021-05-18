from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from .models import Content, FollowRelation

@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    # login_required와 동시에 settings에서 LOGIN_URL추가 
    # @method_decorator(login_required,)
    # def dispatch(self, request, *args, **kargs):
    #     return super(HomeView, self).dispatch(request, *args, **kargs)


    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        user = self.request.user
        # context['contents'] = Content.objects.select_related('user').prefetch_related('image_set').filter(user__id__in=lookup_user_ids)
        
        # Content.objects
        # context['contents'] = Content.objects.select_related('user').filter(user=user)
        # -> contents의 오브젝트 중에서 user와 관련된 항목들 중에 user=user인 항목들을 필터링하겠다. 

        followees = FollowRelation.objects.filter(follower=user).values_list('followee__id', flat=True)
        print(followees)
        lookup_user_ids = [user.id] + list(followees) # 본인 + 팔로우 한 사람들

        context['contents'] = Content.objects.select_related('user').prefetch_related('image_set').filter(
            user__id__in = lookup_user_ids
        )
        
        
        return context

    template_name = "home.html"


    



class NonUserTemplateView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect('contents_home')
        return super(NonUserTemplateView, self).dispatch(request, *args, **kwargs)


class LoginView(NonUserTemplateView):
    template_name = 'login.html'


class RegisterView(NonUserTemplateView):
    template_name = 'register.html'

