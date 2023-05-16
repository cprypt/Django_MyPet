from django.urls import path

from .views import base_views, baseInfo_views, detailInfo_views

app_name = 'pet'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:baseInfo_id>/', base_views.detail, name='detail'),

    # baseInfo_views.py
    path('baseInfo/create/', baseInfo_views.baseInfo_create, name='baseInfo_create'),
    path('baseInfo/modify/<int:baseInfo_id>/', baseInfo_views.baseInfo_modify, name='baseInfo_modify'),
    path('baseInfo/delete/<int:baseInfo_id>/', baseInfo_views.baseInfo_delete, name='baseInfo_delete'),
    path('baseInfo/vote/<int:baseInfo_id>/', baseInfo_views.baseInfo_vote, name='baseInfo_vote'),

    # detailInfo_views.py
    path('detailInfo/create/<int:baseInfo_id>/', detailInfo_views.detailInfo_create, name='detailInfo_create'),
    path('detailInfo/modify/<int:detailInfo_id>/', detailInfo_views.detailInfo_modify, name='detailInfo_modify'),
    path('detailInfo/delete/<int:detailInfo_id>/', detailInfo_views.detailInfo_delete, name='detailInfo_delete'),
]