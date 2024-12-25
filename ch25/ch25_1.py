import requests
import bs4

# 目标URL
url = 'https://www.104.com.tw/jobs/search/?ro=0&keyword=Python&jobsource=2018indexpoc'

# 请求网页内容
htmlFile = requests.get(url)

# 解析HTML
objSoup = bs4.BeautifulSoup(htmlFile.text, 'lxml')

# 找到所有职位信息容器
jobs = objSoup.find_all('div', class_='info-container')

# 输出找到的职位信息
print("找到的职位数量:", len(jobs))
for job in jobs:
    # 提取职位名称
    job_name_element = job.find('a', class_='info-job__text jb-link jb-link-blue jb-link-blue--visited h2')
    job_name = job_name_element.get_text(strip=True) if job_name_element else "未找到职务名称"

    # 提取公司名称
    company_name_element = job.find('div', class_='info-company mb-1')
    company_name = company_name_element.find('a').get_text(strip=True) if company_name_element else "未找到公司名称"

    # 提取工作地点
    location_tags = job.find('div', class_='info-tags gray-deep-dark')
    location = location_tags.find('span', class_='info-tags__text font-weight-bold').get_text(strip=True) if location_tags else "未找到位置"

    # 提取薪资和学历要求等信息（可选）
    experience_tag = location_tags.find_all('span', class_='info-tags__text font-weight-bold')[1].get_text(strip=True) if location_tags else "未找到经验要求"

    # 提取职位描述
    description_element = job.find('div', class_='info-description text-gray-darker t4 text-break mt-2 position-relative info-description__line2')
    description = description_element.get_text(strip=True) if description_element else "未找到职位描述"

    # 打印提取的信息
    print("公司名稱 : ", company_name)
    print("職務名稱 : ", job_name)
    # print("工作地點 : ", location)
    # print("經驗要求 : ", experience_tag)
    # print("職位描述 : ", description)
    print("-" * 30)  # 分隔线
