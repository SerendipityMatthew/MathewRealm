import requests

zhipin_url = 'https://www.zhipin.com/'
response = requests.get(url=zhipin_url)

"""
https://www.zhipin.com/job_detail/?query=&scity=101020100&industry=100001&position=120101   上海 视觉设计 电子商务
https://www.zhipin.com/job_detail/?query=&scity=101020100&industry=100020&position=120101   上海 视觉设计 互联网
https://www.zhipin.com/job_detail/?query=&scity=101020100&industry=100020&position=100104   上海 数据挖掘 互联网
https://www.zhipin.com/job_detail/?query=&scity=101020100&industry=100001&position=100104   上海 数据挖掘 电子商务
scity        表示上海         例如:101020100     表示上海
industry     表示所在行业      例如:100020       表示互联网行业
position     表示职位名称      例如:100104       表示数据挖掘

"""

with open('zhipin_index.html', 'w') as f:
    f.write(response.text)