from badi_utils.dynamic import *
from badi_user.ui.member_views import *
from badi_user.ui.views import *
from django.contrib.auth import get_user_model

User = get_user_model()
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='custom_login'),
    path('logout/', UserLogout.as_view(), name='user_logout'),
    path('change_password/', ChangePasswordForgot.as_view(), name="forgot_password"),
    path('forgot_password/<str:token_id>/<str:hash_code>', ChangePasswordForgot.as_view(),
         name="forgot_password"),
    generate_url(User(), create=UserCreateView),
    generate_url(User(), view=UserListView),
    generate_url(User(), update=UserUpdateView),
    path('member/list', MemberListView.as_view(), name='member_list'),
    path('member/create', MemberCreateView.as_view(), name='member_create'),
    path('member/update/<int:pk>', MemberUpdateView.as_view(), name='member_update'),
    path('member/update/self', MemberSelfUpdateView.as_view(), name='member_self'),
    path('edit', MemberSelfUpdateView.as_view(), name='edit_self'),
]
