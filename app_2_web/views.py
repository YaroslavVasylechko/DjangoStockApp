from django.shortcuts import render
from .forms import *
from .services import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def home_page(request):
    return render(request, 'app2/home.html')


@login_required
def get_firm_info(request):
    submitbutton = request.POST.get("submit")
    queryset_with_firm_data = ''
    firm = ''
    valid_data = False
    form = GetData(request.POST or None)

    if form.is_valid():
        valid_data = True
        firm = form.cleaned_data.get('name')
        queryset_with_firm_data = get_data_from_form(firm, form.cleaned_data.get('from_date'),
                                                     form.cleaned_data.get('to_date'))

    context = {
        'form': form, 'firm': firm,
        'submitbutton': submitbutton,
        'firm_data': queryset_with_firm_data,
        'valid_data': valid_data,
    }

    return render(request, 'app2/get_firm_info.html', context)


@login_required
def add_firm_info(request):
    submitbutton = request.POST.get("submit")

    valid_data = False
    firm = ''
    price = ''
    date = ''

    form = FirmNames(request.POST or None)
    if form.is_valid():
        data = form.save()
        firm = form.cleaned_data.get("name")
        price = form.cleaned_data.get("price")
        date = form.cleaned_data.get("date")
        valid_data = True

    context = {
        'firmnames': form, 'submitbutton': submitbutton,
        'firm': firm, 'price': price, 'date': date, 'valid_data': valid_data
    }
    if request.user.is_superuser or request.user.is_staff:
        return render(request, 'app2/add_firm_info.html', context)
    else:
        return HttpResponseForbidden()
