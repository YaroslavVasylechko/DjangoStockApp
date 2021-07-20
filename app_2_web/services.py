from .models import FirmInfo
from django.db.models import Q


def get_data_from_form(firm, from_date, to_date):
    return FirmInfo.objects.filter(
        Q(name__name__contains=firm) & Q(date__gte=from_date) & Q(date__lte=to_date)).order_by('-date')
