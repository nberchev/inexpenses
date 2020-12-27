import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages

from userpreferences.models import UserPreference

from .models import Source, UserIncome


@login_required(login_url='/authentication/login')
def index(request):
    income = UserIncome.objects.filter(owner=request.user)
    currency = UserPreference.objects.get(user=request.user).currency
    paginator = Paginator(income, 2)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)

    context = {
        'income': income,
        'page_obj': page_obj,
        'currency': currency,
    }
    return render(request, 'income/index.html', context)


@login_required(login_url='/authentication/login')
def add_income(request):
    sources = Source.objects.all()
    context = {
        'sources': sources,
        'values': request.POST,
    }
    if request.method == 'GET':
        return render(request, 'income/add_income.html', context)

    else:
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount field is required')
            return render(request, 'income/add_income.html', context)

        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']

        if not description:
            messages.error(request, 'Description field is required')
            return render(request, 'income/add_income.html', context)

        UserIncome.objects.create(owner=request.user, amount=amount, date=date, source=source, description=description)
        messages.success(request, 'Income saved successfully')
        return redirect('income')


@login_required(login_url='/authentication/login')
def edit_income(request, pk):
    income = UserIncome.objects.get(pk=pk)
    sources = Source.objects.all()
    context = {
        'income': income,
        'values': income,
        'sources': sources,
    }

    if request.method == 'GET':
        return render(request, 'income/edit_income.html', context)
    else:
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount field is required')
            return render(request, 'income/edit_income.html', context)

        description = request.POST['description']
        date = request.POST['income_date']
        source = request.POST['source']

        if not description:
            messages.error(request, 'Description field is required')
            return render(request, 'income/edit_income.html', context)

        income.amount = amount
        income.date = date
        income.source = source
        income.description = description
        income.save()

        messages.success(request, 'Income updated successfully')
        return redirect('income')


def delete_income(request, pk):
    income = UserIncome.objects.get(pk=pk)
    income.delete()
    messages.success(request, 'Income deleted successfully')
    return redirect('income')


def search_income(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')

        income = UserIncome.objects.filter(
            amount__istartswith=search_str, owner=request.user) | UserIncome.objects.filter(
            date__istartswith=search_str, owner=request.user) | UserIncome.objects.filter(
            description__icontains=search_str, owner=request.user) | UserIncome.objects.filter(
            source__icontains=search_str, owner=request.user)

        data = income.values()

        return JsonResponse(list(data), safe=False)
