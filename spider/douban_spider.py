import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas
import os

# 构造对应于每一页的url_id
# inds = list(range(0, 250, 25))
inds = list(range(0, 25, 25))

# 创建书架
movie_info = []

# # 每本电影的信息
titles = ['中文片名','原片名','其他片名','上映时间','片长','类型','导演','主演','地区','评分','一句话评论','豆瓣链接']

# 构造headers信息
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

# 定义tag的搜索条件，下面会用到
def has_class_but_no_id(tag):
    return tag.name=='td' and tag.has_attr('valign') and not tag.has_attr('width')





# 遍历每一个网页
for ind in inds:
    # 得到每一页的url
    url =  'https://movie.douban.com/top250?start='+str(ind)

    # 获取每页的源代码
    contents = requests.get(url=url, headers=headers).content.decode(encoding='utf-8')
    soup = BeautifulSoup(contents)


    # 得到本页所有电影的各自的代码块
    all_items = soup.findAll('div', class_='item')

    # 遍历本页的所有电影
    for item in tqdm(all_items):

        # print('-'*100)
        # print(rank)
        # rank+=1
        # 创建一个电影
        movie = {}
        for i in titles:
            movie[i] = ' '

        movie['豆瓣链接'] = item.a['href']
        movie_soup = BeautifulSoup(requests.get(url=movie['豆瓣链接'], headers=headers).content.decode(encoding='utf-8'))


        # movie['片长'] = movie_soup.findAll('span',property="v:runtime")[0].string
        runtime_elements = movie_soup.findAll('span',property="v:runtime")
        movie['片长'] = runtime_elements[0].string if runtime_elements else '未知'

        pds = movie_soup.findAll('a', rel="v:directedBy")
        pd = []
        for i in pds:
            pd.append(i.string)
        movie['导演'] = '/'.join(pd)

        stars = movie_soup.findAll('a', rel="v:starring")
        star = []
        for i in stars:
            star.append(i.string)
        movie['主演'] = '/'.join(star)

        title = item.findAll('span', class_='title')
        movie['中文片名'] = title[0].string
        if len(title) == 2:
            movie['原片名'] = title[1].string.strip().split('/')[1].strip()
        other_title = [i.strip() for i in item.findAll('span', class_='other')[0].string.split('/')]
        movie['其他片名'] = '/'.join(other_title[1:])

        series_info = list(item.findAll('p', class_='')[0].descendants)

        movie['上映时间'] = series_info[2].strip().split('\xa0/\xa0')[0]
        movie['地区'] = series_info[2].strip().split('\xa0/\xa0')[1]
        movie['类型'] = series_info[2].strip().split('\xa0/\xa0')[2]

        movie['评分'] = item.findAll('span',class_="rating_num",property="v:average")[0].string

        if item.findAll('span', class_="inq"):
            movie['一句话评论'] = item.findAll('span', class_="inq")[0].string
        # print(movie['一句话评论'] )

        # 将书放入书架
        li = []
        for i in titles:
            li.append(movie[i])
        movie_info.append(li)
    # break
        
for movie in movie_info:
    print(movie)

df = pandas.DataFrame(data=movie_info,
                      columns=titles)


print(df)
# 获取当前文件所在目录
dir = os.path.dirname(__file__)
# 导出excel到当前文件所在目录
df.to_excel(os.path.join(dir, 'douban_top250_movie.xlsx'), index=False)
print('done!')