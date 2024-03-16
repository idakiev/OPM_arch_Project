from django.urls import path, include

from OPM_arch_Project.clients_app.views import ClientDetailView, ClientCreateView, ClientUpdateView

urlpatterns = [
    path('', include([
        path('details/', ClientDetailView.as_view(), name='client_details'),
        path('create/', ClientCreateView.as_view(), name='client_create'),
        path('<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    ])),
    # path('municipality/', include([
    #     path('create/', name='municipality_create'),
    #     path('<int:pk>/update/', name='municipality_update')
    # ])),
    # path('city/', include([
    #     path('create/', name='city_create'),
    #     path('<int:pk>/update/', name='city_update')
    # ]))
]
