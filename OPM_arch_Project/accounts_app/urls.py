from django.urls import path, include

from OPM_arch_Project.accounts_app.views import LoginUserView, ProfileUserView, LogOutUserView, \
    ProfileEditUserView, check_auth_user, ProfileDetailsUserView, ChangePasswordUserView, check_auth_success

urlpatterns = [
    path('auth/', include([
        path("", check_auth_user, name='auth'),
        path("success/", check_auth_success, name="auth_success"),
    ])),
    path("login/", LoginUserView.as_view(), name="login_user"),
    path("logout/", LogOutUserView.as_view(), name="logout_user"),

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
