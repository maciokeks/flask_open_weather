#Add all improtant values to the results website and make new request and reload website after 30 second
import requests
import configparser
from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)
def get_api_key():
    config = configparser.ConfigParser() #create object
    config.read('conf.ini') # read from file
    return config['openweathermap']['api'] # return from openweathermap api key
def weather_get(api,city,units):
    api_request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&mode=json&appid={api}" # api urlR
    print(api_request)
    r = requests.get(api_request) #get request and save to r
    return r.json() # parse data into json

@app.route('/')
def weather_info():
    return render_template('web.html')

@app.route('/results', methods=['POST'])
def weather_results():
    city_weather = request.form['city']
    units = request.form['units']
    api_key = get_api_key()

    data = weather_get(api_key,city_weather,units)

    cords_lon = format(data["coord"]["lon"])
    cords_lat = format(data["coord"]["lat"])
    id_weather = format(data["weather"][0]["id"])
    weather_main = format(data["weather"][0]["main"])
    weather_desc = format(data["weather"][0]["description"])
    weather_icon = format(data["weather"][0]["icon"])
    base = format(data["base"])

    temp = "{0:.2f}".format(data["main"]["temp"])  # get data from main  and value from temp
    temp_feel = "{0:.2f}".format(data["main"]["feels_like"])  # get data from main  and value from temp
    temp_min = "{0:.2f}".format(data["main"]["temp_min"])
    temp_max = "{0:.2f}".format(data["main"]["temp_max"])
    pressure = format(data["main"]["pressure"])
    humidity = format(data["main"]["humidity"])

    visibility = format(data["visibility"])

    wind_speed = format(data["wind"]["speed"])
    wind_deg = format(data["wind"]["deg"])
    wind_gust = format(data["wind"]["gust"])

    clouds = format(data["clouds"]["all"])

    dt = format(data["dt"])

    sys_type = format(data["sys"]["type"])
    sys_id = format(data["sys"]["id"])
    sys_country = format(data["sys"]["country"])
    sys_sunrise = format(data["sys"]["sunrise"])
    sys_sunset = format(data["sys"]["sunset"])

    timezone = format(data["timezone"])
    id = format(data["id"])
    name = format(data["name"])
    cod = format(data["cod"])
    sys_sunrise = datetime.utcfromtimestamp(int(sys_sunrise)).strftime('%Y-%m-%d %H:%M:%S')
    sys_sunset = datetime.utcfromtimestamp(int(sys_sunset)).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('web_results.html', temp = temp,temp_feel= temp_feel, temp_min = temp_min,temp_max = temp_max,pressure=pressure, humidity = humidity
    ,visibility = visibility, wind_speed = wind_speed, wind_deg = wind_deg, wind_gust = wind_gust,clouds = clouds, dt = dt, sys_country = sys_country, sys_sunset = sys_sunset
    , sys_sunrise = sys_sunrise, timezone = timezone, id=id,name=name, cords_lon = cords_lon, cords_lat= cords_lat)
    #return render_template('results.html') # show datsa in json format
if __name__ == '__main__':
    app.run()


