import os
import urllib
import requests
from lxml import etree, html

"""
模拟登陆安科oj
"""


def downloadFile(index, problem):
    if problem == "ac" or (not problem.endswith(".out") and not problem.endswith(".in")):
        return
    headers = {
        'Cookie': 'PHPSESSID=udai36sh4uhjvbvn5rbv4ve9n3; fm_current_root=%2Fhome%2Fjudge%2Fsrc%2Fweb%2F; order_dir_list_by=1A; resolveIDs=1; expanded_dir_list=%3A%3Ahome%3Ajudge%3Asrc%3Aweb%3AJudgeOnline%3Aadmin%3A%2Fhome%2Fjudge%2Fdata%2F1002%2F1002; loggedon=d41d8cd98f00b204e9800998ecf8427e',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'oj.ahstu.cc',
        'Referer': 'https://oj.ahstu.cc/JudgeOnline/admin/phpfm.php?frame=3&pid=' + str(index),
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    problemValue = requests.get(
        "https://oj.ahstu.cc/JudgeOnline/admin/phpfm.php?current_dir=/home/judge/data/" + str(
            index) + "/&filename=" + problem + "&action=3",
        headers=headers)
    path = "D:\Download\oj\\" + str(index)
    pathFile = "D:\Download\oj\\" + str(index) + "\\" + str(problem)

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)

    with open(pathFile, "wb") as f:
        f.write(problemValue.content)
    f.close()


def getEveryProblemFiles(index):
    url = "https://oj.ahstu.cc/JudgeOnline/admin/phpfm.php?frame=3&pid=" + str(index)
    headers = {
        'Cookie': 'PHPSESSID=udai36sh4uhjvbvn5rbv4ve9n3; fm_current_root=%2Fhome%2Fjudge%2Fsrc%2Fweb%2F; order_dir_list_by=1A; resolveIDs=1; expanded_dir_list=%3A%3Ahome%3Ajudge%3Asrc%3Aweb%3AJudgeOnline%3Aadmin%3A%2Fhome%2Fjudge%2Fdata%2F1002%2F1002; loggedon=d41d8cd98f00b204e9800998ecf8427e',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'oj.ahstu.cc',
        'Referer': 'https://oj.ahstu.cc/JudgeOnline/admin/phpfm.php?frame=3&pid=' + str(index),
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    problems = requests.get(url, headers=headers)
    tree = html.fromstring(problems.text)
    list = tree.xpath("//tr[@class='entryUnselected']/td[1]/nobr/a/text()")
    return list


def run():
    # 固定写死一个cookie
    cookie = {'PHPSESSID': 'udai36sh4uhjvbvn5rbv4ve9n3'}

    for index in range(1350, 3072):
        list = getEveryProblemFiles(index)
        for problem in list:
            downloadFile(index, problem)


if __name__ == '__main__':
    account = '1881180120'
    password = 'ylyy2311'
    run()
