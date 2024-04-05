from django.urls import path, include

from OPM_arch_Project.clients_app.views import ClientsDetailView, ClientsCreateView, ClientsUpdateView, ClientsListView

urlpatterns = [
    path('', include([
        path('list/', ClientsListView.as_view(), name='clients_list'),
        path('create/', ClientsCreateView.as_view(), name='clients_create'),
        path('<int:pk>/', include([
            path('details/', ClientsDetailView.as_view(), name='clients_details'),
            path('update/', ClientsUpdateView.as_view(), name='clients_update'),
        ])),
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
