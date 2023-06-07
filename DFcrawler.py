from bs4 import BeautifulSoup
import requests
 
sel = input('1. 직업게시판\n2. 전체게시판\n데이터를 수집 할 게시판을 선택하세요. : ')

if sel == '1':

    print('직업게시판 데이터 수집')
    job = input('직업군 종류 : ')
    gtype = input('전직 종류 : ')
    page = int(input('시작 페이지 : '))
    maxpage = int(input('마지막 페이지 : '))
    filename = input('저장할 파일 이름을 입력하세요. : ')
    
    f = open(filename,"w")

    while page < maxpage:

        print(page)

        URL = 'http://df.nexon.com/df/community/dnfboard?mode=list&job='+str(job)+'&grow_type='+str(gtype)+'&page='+str(page)
        code = requests.get(URL)

        html = code.text
        soup = BeautifulSoup(html, 'lxml')
        a = soup.find_all('a')

        for s in a:
            c = s.get('class')
            if c != None and c[0] == 'ellipsis_line':
                title = s.get('title')
                print(title)
                f.write(title+' ')
            
        page = page+1

    f.close()
    
elif sel == '2':
    
    print('전체게시판 데이터 수집\n')

    page = int(input('시작 페이지 : '))
    maxpage = int(input('마지막 페이지 : '))
    filename = input('저장할 파일 이름을 입력하세요. : ')

    f = open(filename,"w",encoding="UTF8")
    
    while page < maxpage:

        print(page)

        URL = 'http://df.nexon.com/df/community/dnfboard?mode=list&page='+str(page)
        code = requests.get(URL)

        html = code.text
        soup = BeautifulSoup(html, 'lxml')
        a = soup.find_all('a')

        for s in a:
            c = s.get('class')
            if c != None and c[0] == 'ellipsis_line':
                title = s.get('title')
                print(title)
                f.write(title+' ')
            
        page = page+1

    f.close()
    
elif sel != '1' and sel != '2':
    print('1 또는 2를 입력해 주세요.')
