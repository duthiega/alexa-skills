# -*- coding: utf-8 -*-

# Resolving gettext as _ for module loading.

# TODO add planets and anything to see, like metor showers, comets, etc 
from gettext import gettext as _

SKILL_NAME = "Space Explorer"

WELCOME = _("Welcome to Space Explorer!")
HELP = _("Say about, to hear more about the city, or say coffee, breakfast, lunch, or dinner, to hear local restaurant suggestions, or say recommend an attraction, or say, go outside. ")
ABOUT = _("Gloucester Massachusetts is a city on the Atlantic Ocean. A popular summer beach destination, Gloucester has a rich history of fishing and ship building.")
STOP = _("Okay, see you next time!")
FALLBACK = _("The {} can't help you with that. It can help you learn about Gloucester if you say tell me about this place. What can I help you with?")
GENERIC_REPROMPT = _("What can I help you with?")

POSTCODE = "IV30 6GP"
LATITUDE =  57.639818
LONGITUDE = -3.28589
QUERY_DATE = "2019-01-31"
WEATHER_API_KEY = "27f92a5d9fc3a37873569ba8c6092d14"
        

ISS_API = {
    "host":"http://api.open-notify.org/iss-pass.json?lat={LATITUDE}&lon={LONGITUDE}&alt=20&n=5"
}


WEATHER_API = {
    "host":"http://api.openweathermap.org/data/2.5/forecast?zip={postcode},gb&APPID={WEATHER_API_KEY}"

}

SUNRISE_SUNSET_API = {
    "host":"https://api.sunrise-sunset.org/json?lat={LATITUDE}&lng={LONGITUDE}&date={QUERY_DATE}&formatted=0"
}

POSTCODE_API = {
    "host":"api.postcodes.io/postcodes/{POSTCODE}"
}

SUNRISE_SUNSET_DATA = {
  "results": {
    "sunrise": "2019-01-31T07:20:05+00:00",
    "sunset": "2019-01-31T17:42:11+00:00",
    "solar_noon": "2019-01-31T12:31:08+00:00",
    "day_length": 37326,
    "civil_twilight_begin": "2019-01-31T06:52:55+00:00",
    "civil_twilight_end": "2019-01-31T18:09:21+00:00",
    "nautical_twilight_begin": "2019-01-31T06:21:56+00:00",
    "nautical_twilight_end": "2019-01-31T18:40:20+00:00",
    "astronomical_twilight_begin": "2019-01-31T05:51:28+00:00",
    "astronomical_twilight_end": "2019-01-31T19:10:48+00:00"
  },
  "status": "OK"
}

ISS_DATA = {
  "message": "success", 
  "request": {
    "altitude": 100, 
    "datetime": 1548928377, 
    "latitude": 57.639818, 
    "longitude": -3.28589, 
    "passes": 5
  }, 
  "response": [
    {
      "duration": 460, 
      "risetime": 1548948907
    }, 
    {
      "duration": 592, 
      "risetime": 1548954577
    }, 
    {
      "duration": 617, 
      "risetime": 1548960321
    }, 
    {
      "duration": 591, 
      "risetime": 1548966091
    }, 
    {
      "duration": 454, 
      "risetime": 1548971894
    }
  ]
}

WEATHER_FORECAST_DATA = {
  "cod": "200",
  "message": 0.0046,
  "cnt": 40,
  "list": [
    {
      "dt": 1548936000,
      "main": {
        "temp": 270.4,
        "temp_min": 270.4,
        "temp_max": 272.724,
        "pressure": 990.44,
        "sea_level": 1006.19,
        "grnd_level": 990.44,
        "humidity": 100,
        "temp_kf": -2.33
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01d"
        }
      ],
      "clouds": { "all": 0 },
      "wind": {
        "speed": 3.27,
        "deg": 227.004
      },
      "snow": { "3h": 0.002 },
      "sys": { "pod": "d" },
      "dt_txt": "2019-01-31 12:00:00"
    },
    {
      "dt": 1548946800,
      "main": {
        "temp": 271.95,
        "temp_min": 271.95,
        "temp_max": 273.504,
        "pressure": 990.21,
        "sea_level": 1005.89,
        "grnd_level": 990.21,
        "humidity": 100,
        "temp_kf": -1.55
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01d"
        }
      ],
      "clouds": { "all": 8 },
      "wind": {
        "speed": 2.81,
        "deg": 234.503
      },
      "snow": { "3h": 0.003 },
      "sys": { "pod": "d" },
      "dt_txt": "2019-01-31 15:00:00"
    },
    {
      "dt": 1548957600,
      "main": {
        "temp": 270.47,
        "temp_min": 270.47,
        "temp_max": 271.245,
        "pressure": 990.26,
        "sea_level": 1006.12,
        "grnd_level": 990.26,
        "humidity": 100,
        "temp_kf": -0.78
      },
      "weather": [
        {
          "id": 600,
          "main": "Snow",
          "description": "light snow",
          "icon": "13n"
        }
      ],
      "clouds": { "all": 56 },
      "wind": {
        "speed": 2.86,
        "deg": 222.003
      },
      "snow": { "3h": 0.0315 },
      "sys": { "pod": "n" },
      "dt_txt": "2019-01-31 18:00:00"
    },
    {
      "dt": 1548968400,
      "main": {
        "temp": 271.837,
        "temp_min": 271.837,
        "temp_max": 271.837,
        "pressure": 990.61,
        "sea_level": 1006.42,
        "grnd_level": 990.61,
        "humidity": 100,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 600,
          "main": "Snow",
          "description": "light snow",
          "icon": "13n"
        }
      ],
      "clouds": { "all": 76 },
      "wind": {
        "speed": 2.57,
        "deg": 235.502
      },
      "snow": { "3h": 0.184 },
      "sys": { "pod": "n" },
      "dt_txt": "2019-01-31 21:00:00"
    },
    {
      "dt": 1548979200,
      "main": {
        "temp": 272.827,
        "temp_min": 272.827,
        "temp_max": 272.827,
        "pressure": 991.13,
        "sea_level": 1007.02,
        "grnd_level": 991.13,
        "humidity": 100,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10n"
        }
      ],
      "clouds": { "all": 88 },
      "wind": {
        "speed": 1.96,
        "deg": 233.003
      },
      "rain": { "3h": 0.0225 },
      "snow": { "3h": 0.126 },
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-01 00:00:00"
    },
    {
      "dt": 1548990000,
      "main": {
        "temp": 273.148,
        "temp_min": 273.148,
        "temp_max": 273.148,
        "pressure": 991.66,
        "sea_level": 1007.62,
        "grnd_level": 991.66,
        "humidity": 100,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10n"
        }
      ],
      "clouds": { "all": 88 },
      "wind": {
        "speed": 1.56,
        "deg": 258.002
      },
      "rain": { "3h": 0.03 },
      "snow": { "3h": 0.13 },
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-01 03:00:00"
    },
    {
      "dt": 1549000800,
      "main": {
        "temp": 273.08,
        "temp_min": 273.08,
        "temp_max": 273.08,
        "pressure": 992.6,
        "sea_level": 1008.49,
        "grnd_level": 992.6,
        "humidity": 100,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10n"
        }
      ],
      "clouds": { "all": 80 },
      "wind": {
        "speed": 0.72,
        "deg": 289.009
      },
      "rain": { "3h": 0.05 },
      "snow": { "3h": 0.0585 },
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-01 06:00:00"
    },
    {
      "dt": 1549011600,
      "main": {
        "temp": 272.961,
        "temp_min": 272.961,
        "temp_max": 272.961,
        "pressure": 994.46,
        "sea_level": 1010.28,
        "grnd_level": 994.46,
        "humidity": 100,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10d"
        }
      ],
      "clouds": { "all": 80 },
      "wind": {
        "speed": 0.32,
        "deg": 315.507
      },
      "rain": { "3h": 0.12 },
      "snow": { "3h": 0.0825 },
      "sys": { "pod": "d" },
      "dt_txt": "2019-02-01 09:00:00"
    },
    {
      "dt": 1549022400,
      "main": {
        "temp": 274.536,
        "temp_min": 274.536,
        "temp_max": 274.536,
        "pressure": 995.61,
        "sea_level": 1011.43,
        "grnd_level": 995.61,
        "humidity": 100,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10d"
        }
      ],
      "clouds": { "all": 8 },
      "wind": {
        "speed": 1.86,
        "deg": 251.004
      },
      "rain": { "3h": 0.01 },
      "snow": { "3h": 0.0775 },
      "sys": { "pod": "d" },
      "dt_txt": "2019-02-01 12:00:00"
    },
    {
      "dt": 1549033200,
      "main": {
        "temp": 274.881,
        "temp_min": 274.881,
        "temp_max": 274.881,
        "pressure": 996,
        "sea_level": 1011.91,
        "grnd_level": 996,
        "humidity": 100,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10d"
        }
      ],
      "clouds": { "all": 56 },
      "wind": {
        "speed": 2.76,
        "deg": 267.004
      },
      "rain": { "3h": 0.01 },
      "snow": { "3h": 0.03 },
      "sys": { "pod": "d" },
      "dt_txt": "2019-02-01 15:00:00"
    },
    {
      "dt": 1549044000,
      "main": {
        "temp": 274.453,
        "temp_min": 274.453,
        "temp_max": 274.453,
        "pressure": 997.95,
        "sea_level": 1013.83,
        "grnd_level": 997.95,
        "humidity": 100,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10n"
        }
      ],
      "clouds": { "all": 88 },
      "wind": {
        "speed": 5.91,
        "deg": 351.501
      },
      "rain": { "3h": 0.32 },
      "snow": { "3h": 0.8875 },
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-01 18:00:00"
    },
    {
      "dt": 1549054800,
      "main": {
        "temp": 275.111,
        "temp_min": 275.111,
        "temp_max": 275.111,
        "pressure": 999.96,
        "sea_level": 1015.76,
        "grnd_level": 999.96,
        "humidity": 98,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10n"
        }
      ],
      "clouds": { "all": 80 },
      "wind": {
        "speed": 5.97,
        "deg": 349.509
      },
      "rain": { "3h": 0.245 },
      "snow": { "3h": 1.155 },
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-01 21:00:00"
    },
    {
      "dt": 1549065600,
      "main": {
        "temp": 274.817,
        "temp_min": 274.817,
        "temp_max": 274.817,
        "pressure": 1001.76,
        "sea_level": 1017.57,
        "grnd_level": 1001.76,
        "humidity": 93,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10n"
        }
      ],
      "clouds": { "all": 68 },
      "wind": {
        "speed": 5.71,
        "deg": 338.001
      },
      "rain": { "3h": 0.0049999999999999 },
      "snow": { "3h": 0.0125 },
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-02 00:00:00"
    },
    {
      "dt": 1549076400,
      "main": {
        "temp": 273.582,
        "temp_min": 273.582,
        "temp_max": 273.582,
        "pressure": 1003.34,
        "sea_level": 1019.13,
        "grnd_level": 1003.34,
        "humidity": 92,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02n"
        }
      ],
      "clouds": { "all": 12 },
      "wind": {
        "speed": 5.12,
        "deg": 328.003
      },
      "rain": {},
      "snow": {},
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-02 03:00:00"
    },
    {
      "dt": 1549087200,
      "main": {
        "temp": 271.716,
        "temp_min": 271.716,
        "temp_max": 271.716,
        "pressure": 1004.89,
        "sea_level": 1020.69,
        "grnd_level": 1004.89,
        "humidity": 91,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01n"
        }
      ],
      "clouds": { "all": 0 },
      "wind": {
        "speed": 3.96,
        "deg": 303.003
      },
      "rain": {},
      "snow": {},
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-02 06:00:00"
    },
    {
      "dt": 1549098000,
      "main": {
        "temp": 270.133,
        "temp_min": 270.133,
        "temp_max": 270.133,
        "pressure": 1006.42,
        "sea_level": 1022.36,
        "grnd_level": 1006.42,
        "humidity": 92,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01d"
        }
      ],
      "clouds": { "all": 0 },
      "wind": {
        "speed": 2.82,
        "deg": 275.003
      },
      "rain": {},
      "snow": {},
      "sys": { "pod": "d" },
      "dt_txt": "2019-02-02 09:00:00"
    },
    {
      "dt": 1549108800,
      "main": {
        "temp": 274.375,
        "temp_min": 274.375,
        "temp_max": 274.375,
        "pressure": 1007.49,
        "sea_level": 1023.37,
        "grnd_level": 1007.49,
        "humidity": 89,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "02d"
        }
      ],
      "clouds": { "all": 8 },
      "wind": {
        "speed": 3.46,
        "deg": 228.505
      },
      "rain": {},
      "snow": {},
      "sys": { "pod": "d" },
      "dt_txt": "2019-02-02 12:00:00"
    },
    {
      "dt": 1549119600,
      "main": {
        "temp": 274.231,
        "temp_min": 274.231,
        "temp_max": 274.231,
        "pressure": 1007.95,
        "sea_level": 1023.87,
        "grnd_level": 1007.95,
        "humidity": 97,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10d"
        }
      ],
      "clouds": { "all": 56 },
      "wind": {
        "speed": 4.16,
        "deg": 255.001
      },
      "rain": { "3h": 0.055 },
      "snow": { "3h": 0.235 },
      "sys": { "pod": "d" },
      "dt_txt": "2019-02-02 15:00:00"
    },
    {
      "dt": 1549130400,
      "main": {
        "temp": 271.821,
        "temp_min": 271.821,
        "temp_max": 271.821,
        "pressure": 1009.28,
        "sea_level": 1025.26,
        "grnd_level": 1009.28,
        "humidity": 96,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01n"
        }
      ],
      "clouds": { "all": 0 },
      "wind": {
        "speed": 3.57,
        "deg": 275.005
      },
      "rain": {},
      "snow": {},
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-02 18:00:00"
    },
    {
      "dt": 1549141200,
      "main": {
        "temp": 271.098,
        "temp_min": 271.098,
        "temp_max": 271.098,
        "pressure": 1010.62,
        "sea_level": 1026.52,
        "grnd_level": 1010.62,
        "humidity": 95,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 600,
          "main": "Snow",
          "description": "light snow",
          "icon": "13n"
        }
      ],
      "clouds": { "all": 64 },
      "wind": {
        "speed": 3.96,
        "deg": 259.505
      },
      "rain": {},
      "snow": { "3h": 0.0425 },
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-02 21:00:00"
    },
    {
      "dt": 1549152000,
      "main": {
        "temp": 270.434,
        "temp_min": 270.434,
        "temp_max": 270.434,
        "pressure": 1012.08,
        "sea_level": 1028.19,
        "grnd_level": 1012.08,
        "humidity": 100,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 600,
          "main": "Snow",
          "description": "light snow",
          "icon": "13n"
        }
      ],
      "clouds": { "all": 0 },
      "wind": {
        "speed": 2.97,
        "deg": 244
      },
      "rain": {},
      "snow": { "3h": 0.17 },
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-03 00:00:00"
    },
    {
      "dt": 1549162800,
      "main": {
        "temp": 267.983,
        "temp_min": 267.983,
        "temp_max": 267.983,
        "pressure": 1013.44,
        "sea_level": 1029.57,
        "grnd_level": 1013.44,
        "humidity": 100,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01n"
        }
      ],
      "clouds": { "all": 0 },
      "wind": {
        "speed": 2.62,
        "deg": 247.006
      },
      "rain": {},
      "snow": {},
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-03 03:00:00"
    },
    {
      "dt": 1549173600,
      "main": {
        "temp": 267.377,
        "temp_min": 267.377,
        "temp_max": 267.377,
        "pressure": 1014.56,
        "sea_level": 1030.68,
        "grnd_level": 1014.56,
        "humidity": 100,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01n"
        }
      ],
      "clouds": { "all": 0 },
      "wind": {
        "speed": 3.14,
        "deg": 228.503
      },
      "rain": {},
      "snow": {},
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-03 06:00:00"
    },
    {
      "dt": 1549184400,
      "main": {
        "temp": 267.904,
        "temp_min": 267.904,
        "temp_max": 267.904,
        "pressure": 1015.94,
        "sea_level": 1032.13,
        "grnd_level": 1015.94,
        "humidity": 100,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01d"
        }
      ],
      "clouds": { "all": 0 },
      "wind": {
        "speed": 4.1,
        "deg": 219
      },
      "rain": {},
      "snow": {},
      "sys": { "pod": "d" },
      "dt_txt": "2019-02-03 09:00:00"
    },
    {
      "dt": 1549195200,
      "main": {
        "temp": 272.938,
        "temp_min": 272.938,
        "temp_max": 272.938,
        "pressure": 1016.03,
        "sea_level": 1032.1,
        "grnd_level": 1016.03,
        "humidity": 98,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01d"
        }
      ],
      "clouds": { "all": 0 },
      "wind": {
        "speed": 4.16,
        "deg": 215.501
      },
      "rain": {},
      "snow": {},
      "sys": { "pod": "d" },
      "dt_txt": "2019-02-03 12:00:00"
    },
    {
      "dt": 1549206000,
      "main": {
        "temp": 273.666,
        "temp_min": 273.666,
        "temp_max": 273.666,
        "pressure": 1014.85,
        "sea_level": 1030.89,
        "grnd_level": 1014.85,
        "humidity": 97,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "02d"
        }
      ],
      "clouds": { "all": 8 },
      "wind": {
        "speed": 3.07,
        "deg": 198.501
      },
      "rain": {},
      "snow": {},
      "sys": { "pod": "d" },
      "dt_txt": "2019-02-03 15:00:00"
    },
    {
      "dt": 1549216800,
      "main": {
        "temp": 270.767,
        "temp_min": 270.767,
        "temp_max": 270.767,
        "pressure": 1012.89,
        "sea_level": 1028.99,
        "grnd_level": 1012.89,
        "humidity": 98,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02n"
        }
      ],
      "clouds": { "all": 24 },
      "wind": {
        "speed": 3.77,
        "deg": 155.502
      },
      "rain": {},
      "snow": {},
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-03 18:00:00"
    },
    {
      "dt": 1549227600,
      "main": {
        "temp": 273.295,
        "temp_min": 273.295,
        "temp_max": 273.295,
        "pressure": 1009.53,
        "sea_level": 1025.68,
        "grnd_level": 1009.53,
        "humidity": 99,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01n"
        }
      ],
      "clouds": { "all": 80 },
      "wind": {
        "speed": 7.47,
        "deg": 167.001
      },
      "rain": {},
      "snow": { "3h": 0.02 },
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-03 21:00:00"
    },
    {
      "dt": 1549238400,
      "main": {
        "temp": 275.657,
        "temp_min": 275.657,
        "temp_max": 275.657,
        "pressure": 1005.31,
        "sea_level": 1021.44,
        "grnd_level": 1005.31,
        "humidity": 99,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10n"
        }
      ],
      "clouds": { "all": 88 },
      "wind": {
        "speed": 8.62,
        "deg": 178.501
      },
      "rain": { "3h": 1.33 },
      "snow": { "3h": 0.9375 },
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-04 00:00:00"
    },
    {
      "dt": 1549249200,
      "main": {
        "temp": 276.869,
        "temp_min": 276.869,
        "temp_max": 276.869,
        "pressure": 1002.51,
        "sea_level": 1018.47,
        "grnd_level": 1002.51,
        "humidity": 90,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01n"
        }
      ],
      "clouds": { "all": 0 },
      "wind": {
        "speed": 8.62,
        "deg": 199.002
      },
      "rain": {},
      "snow": {},
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-04 03:00:00"
    },
    {
      "dt": 1549260000,
      "main": {
        "temp": 277.263,
        "temp_min": 277.263,
        "temp_max": 277.263,
        "pressure": 1001.49,
        "sea_level": 1017.26,
        "grnd_level": 1001.49,
        "humidity": 92,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10n"
        }
      ],
      "clouds": { "all": 0 },
      "wind": {
        "speed": 7.02,
        "deg": 220.5
      },
      "rain": { "3h": 0.0099999999999998 },
      "snow": {},
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-04 06:00:00"
    },
    {
      "dt": 1549270800,
      "main": {
        "temp": 277.399,
        "temp_min": 277.399,
        "temp_max": 277.399,
        "pressure": 1000.49,
        "sea_level": 1016.3,
        "grnd_level": 1000.49,
        "humidity": 93,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10d"
        }
      ],
      "clouds": { "all": 76 },
      "wind": {
        "speed": 9.16,
        "deg": 213.506
      },
      "rain": { "3h": 0.19 },
      "snow": {},
      "sys": { "pod": "d" },
      "dt_txt": "2019-02-04 09:00:00"
    },
    {
      "dt": 1549281600,
      "main": {
        "temp": 278.698,
        "temp_min": 278.698,
        "temp_max": 278.698,
        "pressure": 1000.89,
        "sea_level": 1016.5,
        "grnd_level": 1000.89,
        "humidity": 88,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10d"
        }
      ],
      "clouds": { "all": 24 },
      "wind": {
        "speed": 10.11,
        "deg": 228.501
      },
      "rain": { "3h": 0.01 },
      "snow": {},
      "sys": { "pod": "d" },
      "dt_txt": "2019-02-04 12:00:00"
    },
    {
      "dt": 1549292400,
      "main": {
        "temp": 278.61,
        "temp_min": 278.61,
        "temp_max": 278.61,
        "pressure": 1000.57,
        "sea_level": 1016.32,
        "grnd_level": 1000.57,
        "humidity": 87,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02d"
        }
      ],
      "clouds": { "all": 20 },
      "wind": {
        "speed": 10.62,
        "deg": 229.007
      },
      "rain": {},
      "snow": {},
      "sys": { "pod": "d" },
      "dt_txt": "2019-02-04 15:00:00"
    },
    {
      "dt": 1549303200,
      "main": {
        "temp": 277.946,
        "temp_min": 277.946,
        "temp_max": 277.946,
        "pressure": 1000.54,
        "sea_level": 1016.37,
        "grnd_level": 1000.54,
        "humidity": 89,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01n"
        }
      ],
      "clouds": { "all": 0 },
      "wind": {
        "speed": 11.12,
        "deg": 228.504
      },
      "rain": {},
      "snow": {},
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-04 18:00:00"
    },
    {
      "dt": 1549314000,
      "main": {
        "temp": 277.89,
        "temp_min": 277.89,
        "temp_max": 277.89,
        "pressure": 1001.9,
        "sea_level": 1017.59,
        "grnd_level": 1001.9,
        "humidity": 91,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10n"
        }
      ],
      "clouds": { "all": 24 },
      "wind": {
        "speed": 9.26,
        "deg": 239
      },
      "rain": { "3h": 0.32 },
      "snow": {},
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-04 21:00:00"
    },
    {
      "dt": 1549324800,
      "main": {
        "temp": 278.254,
        "temp_min": 278.254,
        "temp_max": 278.254,
        "pressure": 1004.47,
        "sea_level": 1020.01,
        "grnd_level": 1004.47,
        "humidity": 91,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10n"
        }
      ],
      "clouds": { "all": 76 },
      "wind": {
        "speed": 9.03,
        "deg": 257.004
      },
      "rain": { "3h": 0.31 },
      "snow": {},
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-05 00:00:00"
    },
    {
      "dt": 1549335600,
      "main": {
        "temp": 278.33,
        "temp_min": 278.33,
        "temp_max": 278.33,
        "pressure": 1007.33,
        "sea_level": 1023.01,
        "grnd_level": 1007.33,
        "humidity": 91,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10n"
        }
      ],
      "clouds": { "all": 44 },
      "wind": {
        "speed": 8.31,
        "deg": 266
      },
      "rain": { "3h": 0.03 },
      "snow": {},
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-05 03:00:00"
    },
    {
      "dt": 1549346400,
      "main": {
        "temp": 278.092,
        "temp_min": 278.092,
        "temp_max": 278.092,
        "pressure": 1009.76,
        "sea_level": 1025.41,
        "grnd_level": 1009.76,
        "humidity": 91,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": { "all": 44 },
      "wind": {
        "speed": 7.11,
        "deg": 266.502
      },
      "rain": {},
      "snow": {},
      "sys": { "pod": "n" },
      "dt_txt": "2019-02-05 06:00:00"
    },
    {
      "dt": 1549357200,
      "main": {
        "temp": 277.514,
        "temp_min": 277.514,
        "temp_max": 277.514,
        "pressure": 1012.03,
        "sea_level": 1027.82,
        "grnd_level": 1012.03,
        "humidity": 93,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10d"
        }
      ],
      "clouds": { "all": 24 },
      "wind": {
        "speed": 5.37,
        "deg": 256.5
      },
      "rain": { "3h": 0.01 },
      "snow": {},
      "sys": { "pod": "d" },
      "dt_txt": "2019-02-05 09:00:00"
    }
  ],
  "city": {
    "id": 580023313,
    "name": "Inverness",
    "coord": {
      "lat": 57.6448,
      "lon": -3.3684
    },
    "country": "GB"
  }
}

CITY_DATA = {
    "city": "Gloucester",
    "state": "MA",
    "postcode": "01930",
    "restaurants": [
        {
            "name": "Zeke's Place",
            "address": '66 East Main Street',
            "phone": '978-283-0474',
            "meals": 'breakfast, lunch',
            "description": 'A cozy and popular spot for breakfast.  Try the blueberry french toast!',
        },
        {
            "name": 'Morning Glory Coffee Shop',
            "address": '25 Western Avenue',
            "phone": '978-281-1851',
            "meals": 'coffee, breakfast, lunch',
            "description": 'A homestyle diner located just across the street from the harbor sea wall.',
        },
        {
            "name": 'Sugar Magnolias',
            "address": '112 Main Street',
            "phone": '978-281-5310',
            "meals": 'breakfast, lunch',
            "description": 'A quaint eatery, popular for weekend brunch.  Try the carrot cake pancakes.',
        },
        {
            "name": 'Seaport Grille',
            "address": '6 Rowe Square',
            "phone": '978-282-9799',
            "meals": 'lunch, dinner',
            "description": 'Serving seafood, steak and casual fare.  Enjoy harbor views on the deck.',
        },
        {
            "name": 'Latitude 43',
            "address": '25 Rogers Street',
            "phone": '978-281-0223',
            "meals": 'lunch, dinner',
            "description": 'Features artsy decor and sushi specials.  Live music evenings at the adjoining Minglewood Tavern.',
        },
        {
            "name": "George's Coffee Shop",
            "address": '178 Washington Street',
            "phone": '978-281-1910',
            "meals": 'coffee, breakfast, lunch',
            "description": 'A highly rated local diner with generously sized plates.',
        },
    ],
    "attractions": [
        {
            "name": 'Whale Watching',
            "description": 'Gloucester has tour boats that depart twice daily from Rogers street at the harbor.  Try either the 7 Seas Whale Watch, or Captain Bill and Sons Whale Watch. ',
            "distance": '0',
        },
        {
            "name": 'Good Harbor Beach',
            "description": 'Facing the Atlantic Ocean, Good Harbor Beach has huge expanses of soft white sand that attracts hundreds of visitors every day during the summer.',
            "distance": '2',
        },
        {
            "name": 'Rockport',
            "description": 'A quaint New England town, Rockport is famous for rocky beaches, seaside parks, lobster fishing boats, and several art studios.',
            "distance": '4',
        },
        {
            "name": 'Fenway Park',
            "description": 'Home of the Boston Red Sox, Fenway park hosts baseball games From April until October, and is open for tours. ',
            "distance": '38',
        },
    ],
}

MY_API = {
    "host": "https://query.yahooapis.com",
    "port": 443,
    "path": "/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{city}%2C%20{state}%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys",
}
