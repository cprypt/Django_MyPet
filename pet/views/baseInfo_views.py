from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import BaseInfoForm
from ..models import BaseInfo


@login_required(login_url='common:login')
def baseInfo_create(request):
    if request.method == 'POST':
        form = BaseInfoForm(request.POST)
        if form.is_valid():
            baseInfo = form.save(commit=False)
            baseInfo.author = request.user  # author 속성에 로그인 계정 저장
            baseInfo.create_date = timezone.now()
            baseInfo.save()
            return redirect('pet:index')
    else:
        form = BaseInfoForm()
    context = {'form': form}
    return render(request, 'pet/baseInfo_form.html', context)


@login_required(login_url='common:login')
def baseInfo_modify(request, baseInfo_id):
    baseInfo = get_object_or_404(BaseInfo, pk=baseInfo_id)
    if request.user != baseInfo.author:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('pet:detail', baseInfo_id=baseInfo.id)
    if request.method == "POST":
        form = BaseInfoForm(request.POST, instance=baseInfo)
        if form.is_valid():
            baseInfo = form.save(commit=False)
            baseInfo.modify_date = timezone.now()  # 수정일시 저장
            baseInfo.save()
            return redirect('pet:detail', baseInfo_id=baseInfo.id)
    else:
        form = BaseInfoForm(instance=baseInfo)
    context = {'form': form}
    return render(request, 'pet/baseInfo_form.html', context)


@login_required(login_url='common:login')
def baseInfo_delete(request, baseInfo_id):
    baseInfo = get_object_or_404(BaseInfo, pk=baseInfo_id)
    if request.user != baseInfo.author:
        messages.error(request, '삭제 권한이 없습니다')
        return redirect('pet:detail', baseInfo_id=baseInfo.id)
    baseInfo.delete()
    return redirect('pet:index')


@login_required(login_url='common:login')
def baseInfo_vote(request, baseInfo_id):
    baseInfo = get_object_or_404(BaseInfo, pk=baseInfo_id)
    if request.user == baseInfo.author:
        messages.error(request, '본인이 등록한 펫은 추천할 수 없습니다')
    else:
        baseInfo.voter.add(request.user)
    return redirect('pet:detail', baseInfo_id=baseInfo.id)