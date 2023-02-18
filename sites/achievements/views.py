from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count
from django.utils import timezone

from .models import Achievement, UserAchievement


@login_required
def achievements_list(request):
    achievements = Achievement.objects.all()
    user_achievements = UserAchievement.objects.filter(user=request.user)
    return render(request, 'achievements/achievements_list.html', {'achievements': achievements, 'user_achievements': user_achievements})

@login_required
def achievement_detail(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    user_achievement = UserAchievement.objects.filter(user=request.user, achievement=achievement).first()
    return render(request, 'achievements/achievement_detail.html', {'achievement': achievement, 'user_achievement': user_achievement})

@login_required
def achievement_delete(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    if request.method == 'POST':
        achievement.delete()
        return redirect('achievements_list')
    return render(request, 'achievements/achievement_confirm_delete.html', {'achievement': achievement})

@login_required
def user_achievements_stats(request):
    user_achievements = UserAchievement.objects.filter(user=request.user).values('achievement__title').annotate(count=Count('achievement')).order_by('-count')
    return JsonResponse({'data': list(user_achievements)})