import random

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.utils.timezone import now
from django.views.generic import CreateView, UpdateView

from config.settings import CODE_EXPIRATION
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User, ConfirmationCode


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:verification')

    def form_valid(self, form):
        self.object = form.save()
        if form.is_valid():
            verification_code = ''.join([str(random.randint(0, 9)) for _ in range(12)])
            self.object.verification_code = verification_code
            self.object.is_active = False
            self.object.save()
            send_mail(
                subject='Поздравляем с регистрацией',
                message=f'Вы зарегистрировались на нашей платформе, ваш код авторизации {verification_code}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.object.email],
                fail_silently=False
            )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ващ новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('shop:list'))


def verify_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        user = request.user
        confirmation_code = ConfirmationCode.objects.filter(user=user, code=code).first()
        if confirmation_code and now() - confirmation_code.created_at < CODE_EXPIRATION:
            # Процесс успешной аутентификации пользователя
            confirmation_code.delete()
            return redirect('success')
    return render(request, 'users/verification.html')
