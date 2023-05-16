from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import DetailInfoForm
from ..models import BaseInfo, DetailInfo


@login_required(login_url='common:login')
def detailInfo_create(request, baseInfo_id):
    """
    pet 상세 정보 등록
    """
    baseInfo = get_object_or_404(BaseInfo, pk=baseInfo_id)
    if request.method == "POST":
        form = DetailInfoForm(request.POST)
        if form.is_valid():
            detailInfo = form.save(commit=False)
            detailInfo.author = request.user  # author 속성에 로그인 계정 저장
            detailInfo.create_date = timezone.now()
            detailInfo.baseInfo = baseInfo
            detailInfo.save()
            return redirect('{}#detailInfo_{}'.format(resolve_url('pet:detail', baseInfo_id=baseInfo.id), detailInfo.id))
    else:
        form = DetailInfoForm()
    context = {'baseInfo': baseInfo, 'form': form}
    return render(request, 'pet/baseInfo_detail.html', context)


@login_required(login_url='common:login')
def detailInfo_modify(request, detailInfo_id):
    detailInfo = get_object_or_404(DetailInfo, pk=detailInfo_id)
    if request.user != detailInfo.author:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('pet:detail', baseInfo_id=detailInfo.baseInfo.id)
    if request.method == "POST":
        form = DetailInfoForm(request.POST, instance=detailInfo)
        if form.is_valid():
            detailInfo = form.save(commit=False)
            detailInfo.modify_date = timezone.now()
            detailInfo.save()
            return redirect('{}#detailInfo_{}'.format(resolve_url('pet:detail', baseInfo_id=detailInfo.baseInfo.id), detailInfo.id))
    else:
        form = DetailInfoForm(instance=detailInfo)
    context = {'detailInfo': detailInfo, 'form': form}
    return render(request, 'pet/detailInfo_form.html', context)


@login_required(login_url='common:login')
def detailInfo_delete(request, detailInfo_id):
    detailInfo = get_object_or_404(DetailInfo, pk=detailInfo_id)
    if request.user != detailInfo.author:
        messages.error(request, '삭제 권한이 없습니다')
    else:
        detailInfo.delete()
    return redirect('pet:detail', baseInfo_id=detailInfo.baseInfo.id)