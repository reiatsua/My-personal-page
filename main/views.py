import requests
from django.shortcuts import render, get_object_or_404
from .models import *
from datetime import datetime

def about(request):
    return render(request,'about.html',{'about':AboutMe.objects.first()})
def achievements(request):
    return render(request,'achievements.html',{'achievements':Achievement.objects.all()})
def achievement_detail(request,pk):
    return render(request,'achievement_detail.html',{'achievement':get_object_or_404(Achievement,pk=pk)})
def school(request):
    return render(request,'school.html',{'school':School.objects.first()})

def weather(request):
    lat, lon = 54.86, 69.14
    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
        f"&daily=temperature_2m_max,temperature_2m_min,wind_speed_10m_max,weather_code"
        f"&wind_speed_unit=ms"
        f"&timezone=auto&forecast_days=10"
    )
    
    try:
        response = requests.get(url).json()
        daily = response.get('daily', {})
        
        weather_codes = {
            0: "Ясно ☀️", 1: "Почти ясно 🌤️", 2: "Облачно ⛅", 3: "Пасмурно ☁️",
            45: "Туман 🌫️", 61: "Дождь 🌧️", 71: "Снег ❄️", 95: "Гроза 🌩️"
        }

        # месяцы
        months_ru = {
            1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня',
            7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
        }

        forecast_list = []
        time_data = daily.get('time', [])
        t_max_data = daily.get('temperature_2m_max', [])
        t_min_data = daily.get('temperature_2m_min', [])
        wind_data = daily.get('wind_speed_10m_max', [])
        code_data = daily.get('weather_code', [])

        for i in range(len(time_data)):
            # строка жисона в дату
            dt = datetime.strptime(time_data[i], '%Y-%m-%d')
            
            # дата
            if i == 0:
                date_display = "Сегодня"
            elif i == 1:
                date_display = "Завтра"
            else:
                date_display = f"{dt.day} {months_ru[dt.month]}"

            forecast_list.append({
                'date': date_display,
                't_max': t_max_data[i] if t_max_data[i] is not None else "?",
                't_min': t_min_data[i] if t_min_data[i] is not None else "?",
                'wind': wind_data[i] if wind_data[i] is not None else 0,
                'status': weather_codes.get(code_data[i], "Осадки") if code_data[i] is not None else "Нет данных"
            })
    except Exception as e:
        print(f"Ошибка получения погоды: {e}")
        forecast_list = []

    return render(request, 'weather.html', {'forecast': forecast_list})


def hive_access_granted(request):
    return render(request, 'hive.html')