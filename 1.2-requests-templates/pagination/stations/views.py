from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))


CONTENT=[]
with open(BUS_STATION_CSV, encoding="utf-8") as file:
    reader= csv.DictReader(file)
    for row in reader:
        station={
            "Name":row["Name"],
            "Street":row["Street"],
            "District":row["District"]
        }
        CONTENT.append(station)

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_num=int(request.GET.get("page",1))
    paginator=Paginator(CONTENT, 10)
    page=paginator.get_page(page_num)
    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
