#!/usr/bin/env python3

import requests
import datetime

# ✅ 配置信息
URLS = [
    ("数字苏豪", "https://gw.meetsoho.cn/"),
    ("jc6", "http://oa.meetsoho.cn/"),
]
TIMEOUT_SECONDS = 10
SERVER_CHAN_KEY = "SCT291245TtKrGuVTmcQMsgooTANCv3uTD"

def check_website(url):
    try:
        response = requests.get(url, timeout=TIMEOUT_SECONDS)
        if response.status_code == 200:
            return True, response.elapsed.total_seconds()
        else:
            return False, f"状态码：{response.status_code}"
    except Exception as e:
        return False, str(e)

def send_wechat_notification(title, content):
    requests.post(f"https://sctapi.ftqq.com/{SERVER_CHAN_KEY}.send", data={
        "title": title,
        "desp": content
    })

if __name__ == "__main__":
    print(f"🕓 脚本运行时间：{datetime.datetime.now()}")  # ✅ 运行日志（方便调试）

    today = datetime.date.today()
    title = f"🌐 数字苏豪和jc6访问性检测（{today}）"
    contents = []

    for site_name, url in URLS:
        success, info = check_website(url)
        if success:
            contents.append(f"✅ {site_name} 访问正常，响应时间：{info:.2f} 秒")
        else:
            contents.append(f"❌ {site_name} 访问失败，错误信息：{info}")

    content = "\n\n".join(contents)
    print(content)  # ✅ 控制台打印内容（将记录到日志）
    send_wechat_notification(title, content)
