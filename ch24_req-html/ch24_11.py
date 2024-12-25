# ch24_11.py
from requests_html import HTMLSession

session = HTMLSession()             # 定义Session
url = 'https://pypi.org/project/requests-html/'
r = session.get(url)                # 发起 GET 请求

# 渲染页面，等待 JS 运行并生成动态内容
r.html.render(timeout=20)

# 检查页面内容并搜索文本
try:
    txt = r.html.search('Python 2 will retire in only {months} months!')
    if txt:
        print(f"Months: {txt['months']}")
    else:
        print("Could not find the specified text on the page.")
except Exception as e:
    print(f"An error occurred: {e}")
