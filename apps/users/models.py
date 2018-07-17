from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class UserProfile(AbstractUser):
    """
    用户信息
    """
    birthday = models.DateField(_('birthday'), null=True, blank=True)
    gender = models.SmallIntegerField(_('gender'), choices=((0, _('male')), (1, _('female'))), default=0)
    mobile = models.CharField(_('mobile number'), max_length=11, null=True, blank = True, help_text = _('Please enter your mobile phone number.'))
    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(_('code'),max_length=10, )
    mobile = models.CharField(_('mobile number'),max_length=11)
    add_time = models.DateTimeField(_('add date'),default=datetime.now)

    class Meta:
        verbose_name = _("SMS code")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
