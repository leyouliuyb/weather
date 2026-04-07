import streamlit as st
import requests

# 页面设置
st.set_page_config(page_title="江苏天气预报", page_icon="🌤️", layout="wide")
st.title("🌤️ 江苏省 7天天气预报")
st.subheader("支持全省城市 · 自动获取实时天气")

# 江苏城市列表
jiangsu_cities = {
    "南京": "Nanjing",
    "苏州": "Suzhou",
    "无锡": "Wuxi",
    "常州": "Changzhou",
    "镇江": "Zhenjiang",
    "扬州": "Yangzhou",
    "泰州": "Taizhou",
    "南通": "Nantong",
    "盐城": "Yancheng",
    "淮安": "Huai'an",
    "连云港": "Lianyungang",
    "徐州": "Xuzhou",
    "宿迁": "Suqian"
}

# 城市选择框
selected_city = st.selectbox("选择城市", list(jiangsu_cities.keys()))
city_en = jiangsu_cities[selected_city]

# 获取天气
def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=j1"
        res = requests.get(url, timeout=10)
        data = res.json()
        weather_list = []

        for i in range(7):
            day = data["weather"][i]
            date = day["date"]
            max_c = int(day["maxtempC"])
            min_c = int(day["mintempC"])
            desc = day["weatherDesc"][0]["value"]
            weather_list.append([date, max_c, min_c, desc])

        return weather_list

    except:
        return [["无网络",26,18,"晴"],["无网络",27,19,"多云"]]*4

# 拿到数据
weather_data = get_weather(city_en)

# 展示
st.subheader(f"📊 {selected_city} 近7天天气")
for item in weather_data:
    date, max_c, min_c, desc = item
    st.success(f"📅 {date} | 🌡 {max_c}℃ ~ {min_c}℃ | ☁️ {desc}")

# 图表
st.subheader("📈 气温趋势图")
max_list = [x[1] for x in weather_data]
min_list = [x[2] for x in weather_data]
chart_data = {"最高温":max_list, "最低温":min_list}
st.line_chart(chart_data)

# 底部信息
st.write("---")
st.write("✅ 数据来源：wttr.in ｜ 📱 手机/电脑通用 ｜ 🌍 免费云服务")
