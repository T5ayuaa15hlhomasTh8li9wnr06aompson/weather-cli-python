
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=zh_cn&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data['name']
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        print(f"城市：{name}")
        print(f"天气：{weather}")
        print(f"气温：{temp}°C")
        print(f"风速：{wind_speed} m/s")
    else:
        print("查询失败，请检查城市名或 API 密钥")

if __name__ == '__main__':
    city = input("请输入城市名：")
    api_key = "你的API_KEY"  # 👈 替换成你自己的
    get_weather(city, api_key)
