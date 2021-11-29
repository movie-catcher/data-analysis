#!/usr/bin/env python
# coding: utf-8

# # KOBIS Webscraping
# - https://www.kobis.or.kr/kobis/business/stat/boxs/findYearlyBoxOfficeList.do
# 
# 
# > 코드 -> id
# - 20204117
# 
# > 요약정보
# - 장편/단편 | 종류 | 장르 | runtime | 연령 | 국가
# - 장편 | 일반영화 | 액션, 드라마 | 121분 2초 | 15세이상관람가 | 한국
# 
# > 배우 [주연]
# - 김윤석(한신성 대사) | 조인성(강대진 참사관) | 허준호(림용수 대사) | 구교환(태준기 참사관) | 김소진(김명희) | 정만식(공수철 서기관)

# In[3]:


# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import time

# browser = webdriver.Chrome()
# # browser.maximize_window()

# url = 'https://www.kobis.or.kr/kobis/business/stat/boxs/findYearlyBoxOfficeList.do'
# browser.get(url)


# ## Function

# In[45]:


# 연도 선택 후 조회
def select_year(year):
    # select by value 
    select = Select(browser.find_element_by_id('sSearchYearFrom'))
    # 2019년 선택
    select.select_by_value(str(year))
    # 조회 버튼 클릭
    browser.find_element_by_class_name('btn_blue').click()
    
    return


# In[46]:


# # 영화명 추출
# def movie_name_extract():
#     soup = BeautifulSoup(browser.page_source, 'lxml')
#     movies = soup.find_all('td', attrs = {'class':'tal'})

#     movie_title = []
#     for movie in movies:
#         title = movie.find('span', attrs={'class':'ellip per90'}).get_text()
#         movie_title.append(title)

#     return movie_title


# In[47]:


# 불러올 tr_id 생성하는 함수
# 가져오고 싶은 영화 갯수
def make_id(num):
    lst = []
    for i in range(num):
         lst.append('tr_' + str(i))
    return lst


# In[90]:


# 필요한 영화 정보 가져오는 함수
def extract_movie_info(soup):
    movie_contents = soup.find('dl',{'class':'ovf cont'}).find_all('dd')
    movie_info_lst = []
    for movie_content in movie_contents:
        movie_info = movie_content.get_text(strip = True)
        movie_info_lst.append(movie_info)

    movie_info_dic = {}
    movie_info_dic['movie_name'] = soup.find('div',{'class':'hd_layer'}).find('strong').get_text()
    movie_info_dic['code'] = movie_info_lst[0]
    movie_info_dic['summary'] = movie_info_lst[3]
    movie_info_dic['release'] = movie_info_lst[4]

    movie_info_dic['summary'] = movie_info_dic['summary'].replace('\n',"").replace('\t',"").split('|')

    movie_info_dic['scale'] = movie_info_dic['summary'][0].strip()
    movie_info_dic['kind'] = movie_info_dic['summary'][1].strip()
    
    movie_genre = [genre.strip() for genre in movie_info_dic['summary'][2].strip().split(',')]
    movie_info_dic['genre'] = movie_genre
    
    movie_info_dic['running_time'] = movie_info_dic['summary'][3].strip()
    movie_info_dic['age'] = movie_info_dic['summary'][4].strip()
    
    del movie_info_dic['summary']
    
    actors_pre = soup.find('dl',{'class':'desc_info'}).find('td').find_all('a')
    actors = []
    for actor in actors_pre:
        idx = actor.get_text().rfind('(')
        if idx != -1:
            actors.append(actor.get_text()[:idx])
        else:
            actors.append(actor.get_text())
    movie_info_dic['actor'] = actors
    
    return movie_info_dic


# In[91]:


# 영화 클릭해서 필요 정보 가져오고 창 닫는 함수
def movie_click(ids):
    movie_info = []
    for id in ids:
        print("Scrapping movie_id : {}".format(id))
        movie_tr_id = browser.find_element_by_id(id)
        movie_click = movie_tr_id.find_element_by_css_selector('#td_movie > span > a')
        movie_click.click()
        
        html = browser.page_source
        soup = BeautifulSoup(html,'lxml')

        movie = extract_movie_info(soup)
        movie_info.append(movie)
        
        time.sleep(1) # 벤 안먹기위해서

        # 창 닫기
        browser.find_element_by_css_selector('body > div.ui-dialog.ui-corner-all.ui-widget.ui-widget-content.ui-front.ui-draggable.ui-resizable > div.ui-dialog-titlebar.ui-corner-all.ui-widget-header.ui-helper-clearfix.ui-draggable-handle > div.hd_layer > a:nth-child(3) > span').click()

    return movie_info


# ## 2020~2019

# In[92]:


import warnings
warnings.filterwarnings("ignore") 

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
# browser.maximize_window()

url = 'https://www.kobis.or.kr/kobis/business/stat/boxs/findYearlyBoxOfficeList.do'
browser.get(url)


# ### 2020

# In[112]:


select_year(2020) # 2020 선택 후 조회 버튼 클릭

# movie_title_2020 = movie_name_extract() # 영화명 list

movie_ids = make_id(50) # 영화 50개 id
movie_info_20 = movie_click(movie_ids)


# ### 2019

# In[113]:


select_year(2019) # 2020 선택 후 조회 버튼 클릭

# movie_title_2020 = movie_name_extract() # 영화명 list

movie_ids = make_id(50) # 영화 50개 id
movie_info_19 = movie_click(movie_ids)


# ## DataFrame Configuration

# In[98]:


import pandas as pd


# In[114]:


movie_df = pd.DataFrame()
movie_df_idx = ['movie_name','code','genre','kind','release','scale','running_time','age', 'actor']
movie_df = movie_df.reindex(columns=movie_df_idx)

for movie_info in movie_info_20:
    movie_df = movie_df.append(movie_info, ignore_index = True)
for movie_info in movie_info_19:
    movie_df = movie_df.append(movie_info, ignore_index = True)


# In[115]:


movie_df

