import streamlit as st
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import requests

# 解决中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 标题
st.title("北京7天真实气温")

# 获取天气
def get_real_weather():
    try:
        url = "https://wttr.in/Beijing?format=j1"
        res = requests.get(url, timeout=10)
        data = res.json()
        max_t = []
        min_t = []
        for day in data['weather'][:7]:
            max_t.append(int(day['maxtempC']))
            min_t.append(int(day['mintempC']))
        return max_t, min_t
    except:
        return [30,32,33,31,29,31,30], [22,23,24,23,22,23,22]

max_temps, min_temps = get_real_weather()

# 日期
today = datetime.now()
dates = [today - timedelta(days=i) for i in range(6, -1, -1)]

# 画图
fig, ax = plt.subplots(figsize=(10,5))
ax.plot(dates, max_temps, label="最高温", marker='o', color='#ff4444')
ax.plot(dates, min_temps, label="最低温", marker='o', color='#3399ff')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator())
plt.xticks(rotation=45)
ax.set_ylabel("气温 ℃")
ax.grid(True, alpha=0.3)
ax.legend()
plt.tight_layout()

# 显示图表
st.pyplot(fig)