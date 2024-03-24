from django.urls import path, include

from OPM_arch_Project.accounts_app.views import LoginUserView, ProfileUserView, RegisterUserView, LogOutUserView, \
    ProfileEditUserView, check_auth_user, ProfileDetailsUserView, ChangePasswordUserView

urlpatterns = [
    path('auth/', check_auth_user, name='auth'),
    path("login/", LoginUserView.as_view(), name="login_user"),
    path("logout/", LogOutUserView.as_view(), name="logout_user"),
    path("register/", RegisterUserView.as_view(), name="register_user"),
    path("profile/", include([
        path("", ProfileUserView.as_view(), name="profile_user"),
        path("<int:pk>/", include([
            path("details/", ProfileDetailsUserView.as_view(), name="profile_details"),
            path("edit/", ProfileEditUserView.as_view(), name="profile_edit"),
        ])),
    ]),
         ),
    path('user/', include([
        path("password/", ChangePasswordUserView.as_view(), name="user_change_password"),
    ])),
]
