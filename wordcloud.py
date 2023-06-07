from collections import Counter
from konlpy.tag import Twitter
import pytagcloud

filename = input('사용된 단어 빈도수를 분석 할 파일 이름을 입력하세요.(확장자이름 포함) : ')

f = open(filename,encoding='UTF8')
data = f.read()
twt = Twitter()
nouns = twt.nouns(data)
count = Counter(nouns)

tag = count.most_common(40)
taglist = pytagcloud.make_tags(tag, maxsize=80)

pytagcloud.create_tag_image(taglist, 'wordcloud'.jpg, size=(900,600), fontname='Korean', rectangular=False)
