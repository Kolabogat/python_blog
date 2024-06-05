from .models import UserProfile


def user_additional_models(request):
    profile_user = UserProfile.objects.filter(user=request.user).exists()

    if not profile_user:
        profile_user = UserProfile()
        profile_user.user = request.user
        profile_user.save()

    return 'Models Created'
