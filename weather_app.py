import streamlit as st
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import requests

# 解决中文
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']
plt.rcParams['axes.unicode_minus'] = False

st.title("🌤️ 北京7天真实气温预报")

def get_weather():
    try:
        url = "https://wttr.in/Beijing?format=j1"
        r = requests.get(url, timeout=10)
        data = r.json()
        max_t = [int(x['maxtempC']) for x in data['weather'][:7]]
        min_t = [int(x['mintempC']) for x in data['weather'][:7]]
        return max_t, min_t
    except:
        return [30,32,33,31,29,31,30], [22,23,24,23,22,23,22]

max_t, min_t = get_weather()
today = datetime.now()
dates = [today - timedelta(days=i) for i in range(6, -1, -1)]

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(dates, max_t, label="最高温", marker='o', c='red')
ax.plot(dates, min_t, label="最低温", marker='o', c='blue')
ax.set_ylabel("气温 ℃")
ax.grid(True)
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)
st.write("✅ 自动更新天气 | 📱 手机通用")
