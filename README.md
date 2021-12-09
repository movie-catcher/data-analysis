# 데이터 분석

- [🎬 기본 영화 데이터 수집](#-기본-영화-데이터-수집)
    - [Features](#features)
    - [Code](#code)
- [💪 배우 영향력 계산](#-배우-영향력-계산)
    - [Code](#code-1)
- [🔥 EDA](#-eda)
    - [Features Selection](#features-selection)
    - [data transformation](#data-transformation)


* * * 
## ⚒ Stacks
![Python](https://img.shields.io/badge/-Python-306998?logo=python&logoColor=ffd43b&style=for-the-badge)
![Jupyter Notebook](https://img.shields.io/badge/-jupyter%20notebook-727272?logo=jupyter&logoColor=eb7633&style=for-the-badge)
![selenium](https://img.shields.io/badge/-selenium-08ad19?logo=jupyter&logoColor=ffffff&style=for-the-badge)
![beautifulsoup](https://img.shields.io/badge/-beautifulsoup4-000?logo=bs4&logoColor=ffffff&style=for-the-badge)

![numpy](https://img.shields.io/badge/-numpy-ffd43b?logo=numpy&logoColor=306998&style=for-the-badge)
![pandas](https://img.shields.io/badge/-pandas-150454?logo=pandas&logoColor=ffffff&style=for-the-badge)
![seaborn](https://img.shields.io/badge/-seaborn-454571?logo=seaborn&logoColor=ffffff&style=for-the-badge)
![matplotlib](https://img.shields.io/badge/-matplotlib-125277?logo=matplotlib&logoColor=ffffff&style=for-the-badge)

<br/>

# 🎬 기본 영화 데이터 수집
* [KOBIS](https://www.kobis.or.kr/kobis/business/main/main.do)에서 기본적인 영화 데이터를 스크래핑 수행
* 17~20년도, 총 4개년에서 개봉한 영화 중 누적 관람객수 상위 50개의 영화를 선정

### Features

|name|desc|
|---|---|
|movie_name|영화의 제목|
|release|영화의 개봉일|
|take|영화의 총 매출액|
|	audience|영화의 총 누적 관람객수
|	nation|영화가 제작된 나라|
|	distribution_company|영화의 배급사 리스트|
|	code|KOBIS 내의 영화 코드|
|	genre|영화의 장르
|	kind|영화의 종류
|	scale|영화의 스케일|
|	running_time|영화의 상영 시간|
|	age|영화의 연령 제한|
|	actor|영화의 주연 배우 리스트|

### Code
|file name|desc|
|---|---|
|[KOBIS_Webscraping.ipynb](./src/KOBIS_Webscraping.ipynb)|KOBIS 웹 사이트에서 기본적인 영화 데이터를 스크래핑|
|[DF_Configuration.ipynb](./src/DF_Configuration.ipynb)|영화 데이터와 바이럴 데이터를 통합 및 정제|

<br/>

# 💪 배우 영향력 계산
* 주연 배우의 경우 [기본 영화 데이터](#-1-기본-영화-데이터-수집)에서 수집된 형태는 **리스트**
* 리스트 자체로 데이터를 사용할 수 없기 때문에 데이터의 변환이 필요함
* 관람객수 예측을 주제로한 많은 논문을 참고하여 "해당 영화의 주연 배우 2명이 3년간 주연으로 출연한 영화의 누적 관람객 수 평균"을 사용

### Code
|file name|desc|
|---|---|
|[actor_power.ipynb](./src/actor_power.ipynb)|1. 기준으로 하는 영화에서 주연 배우 2명가 주연으로 출연한 영화 데이터를 모두 스크래핑 <br/> 2. 기준으로 하는 영화 개봉일 기준으로 이전 3년간 출연한 배우 2명의 누적 관람객수 평균 계산|

<br/>

# 🔥 EDA

### Features Selection

|name|desc|selected|reason|
|:---:|---|:---:|---|
|movie_name|영화명|||
|**release**|개봉일|✅|모델링 할 때 제외|
|**take**|수익(매출액)|✅|종속 변수로 사용될 수도 있음|
|audience|관객수|||
|nation|대표국가|||
|distribution_company|배급사|||
|code|KOBIS 기준 영화 코드|||
|genre|장르|||
|**kind**|영화종류 (일반영화/예술영화/예술,독립영화)|✅|대부분 일반영화(94개 중 91개)|
|**scale**|장편/단편|✅|모두 장편|
|running_time|상영시간 |||
|age|연령|||
|**actor**|주연배우|✅|actor power로 데이터 변환|
|youtube_comment_count|영화 관련 유튜브 컨텐츠 댓글 수|||
|**youtube_view_sum**|영화 관련 유튜브 컨텐츠 조회수 합|✅||
|youtube_view_mean|영화 관련 유튜브 컨텐츠 조회수 평균|||
|**mean_score**|댓글감성분석 score 평균|✅|평균/제곱합평균/절댒값평균 중 선택|
|**sqr_mean_score**|댓글감성분석 score 제곱 평균|✅|평균/제곱합평균/절댒값평균 중 선택|
|abs_mean_score|댓글감성분석 score 절댓값 평균|||
|actor_power|주연배우 2명의 영화 이전 3년간 영화 관객수 평균|||


### data transformation
1. 관람객 수, **Log** transformation

    ![image](https://user-images.githubusercontent.com/49540564/145380257-db7ffdf0-3149-40b7-9fcc-25274d5cb395.png) ![image](https://user-images.githubusercontent.com/49540564/145380287-8615b8b5-f24c-4062-917e-fbeb120ab84b.png)

2. 조회수 평균, **Log** transformation
    
    ![image](https://user-images.githubusercontent.com/49540564/145380327-7cb5aa12-5360-4d7d-b930-45f51dcf7301.png) ![image](https://user-images.githubusercontent.com/49540564/145380362-27b2b867-f46c-4234-8732-6435bea559c9.png)

3. 댓글 수, **Sqrt** transformation

    ![image](https://user-images.githubusercontent.com/49540564/145380633-2908d333-8190-4ecf-8f1b-12f312879a1c.png) ![image](https://user-images.githubusercontent.com/49540564/145380648-e4f4d133-3db4-43e2-a28c-b1adbcecc289.png)
    
5. 배우 영향력, **Sqrt** transformation

    ![image](https://user-images.githubusercontent.com/49540564/145380690-cdf22c03-41b0-451a-a160-ed0a17eeed78.png) ![image](https://user-images.githubusercontent.com/49540564/145380709-674e49d7-b996-4c7b-94c9-473ec2d8cd09.png)
    
    
7. 감성 점수 절댓값 평균, **Sqrt** transformation

    ![image](https://user-images.githubusercontent.com/49540564/145380734-fe09aa49-80d2-43e5-9ad4-ba604269238f.png) ![image](https://user-images.githubusercontent.com/49540564/145380770-3751c2e7-b065-4736-8ad8-08d726e33ebc.png)

