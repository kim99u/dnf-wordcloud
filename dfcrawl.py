from bs4 import BeautifulSoup as BS
import requests
from user_agent import generate_user_agent, generate_navigator

from tqdm.auto import tqdm

from konlpy.tag import Okt
from collections import Counter
import pytagcloud

okt = Okt()

def titles_crawler(endpage):
    title_list = []
    for page in tqdm(range(endpage)):
        url = f'https://df.nexon.com/df/community/dnfboard?mode=list&page={page}'
        ranheaders = {'User-Agent': generate_user_agent(os='win', device_type='desktop')}
        html = requests.get(url, headers=ranheaders).text
        soup = BS(html, 'html.parser')
        titles = soup.find('table', class_='tbl').find_all('a', class_='ellipsis_line')
        for title in titles:
            temp = title.text.strip()
            index = temp.find(']')
            title_str = temp[index+2:]
            title_list.append(title_str)
    return title_list

def cloud_maker(title_list):
    words = []
    for title in title_list:
        words += okt.nouns(title)
    counts = Counter(words)
    tag = counts.most_common(40)
    taglist = pytagcloud.make_tags(tag, maxsize=80)

    wc = pytagcloud.create_tag_image(taglist, 'C:/Users/rladb/workspace/data/dfcrawl/wc.png', size=(900,600), fontname='Korean', rectangular=False)

title_list = titles_crawler(1000)

cloud_maker(title_list)