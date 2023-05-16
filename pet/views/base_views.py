from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import BaseInfo


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    baseInfo_list = BaseInfo.objects.order_by('-create_date')
    if kw:
        baseInfo_list = baseInfo_list.filter(
            Q(name__icontains=kw) |  # 이름 검색
            Q(species__icontains=kw) |  # 종류 검색
            Q(detailinfo__content__icontains=kw) |  # 상세 정보 검색
            Q(author__username__icontains=kw)  # 펫 작성자 검색
        ).distinct()
    paginator = Paginator(baseInfo_list, 5)  # 페이지당 5개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'baseInfo_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pet/baseInfo_list.html', context)


def detail(request, baseInfo_id):
    baseInfo = get_object_or_404(BaseInfo, pk=baseInfo_id)
    context = {'baseInfo': baseInfo}
    return render(request, 'pet/baseInfo_detail.html', context)