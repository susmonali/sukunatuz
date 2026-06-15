from datetime import date

from django.shortcuts import render
from hijridate import Hijri, Gregorian

def dashboard(request):
    today = date.today()
    gregorian_date = Gregorian(today.year, today.month, today.day)
    hijri_date = gregorian_date.to_hijri()
    context = {
        'hijri_date': hijri_date,
        'hijri_month': hijri_date.month_name(),
        'hijri_day': hijri_date.day,
        'hijri_year': hijri_date.year,
               }
    return render(request, "home.html", context)