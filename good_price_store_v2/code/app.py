# https://blog.zarathu.com/posts/2023-02-01-streamlit/

import streamlit as st
import pandas as pd

# Streamlit 앱 제목 설정
st.title('착한 가격 가게🏘️')

# 데이터를 파케이에서 가져와서 표현한다.
# from import_files._variable import *


data_dir='https://github.com/khm9888/web_page_moonight/tree/master/good_price_store_v2/data_small/'
input_csv_name = "good_price_store_info_3.csv"
# st.write(f"test")
# st.write(f"{data_dir}")
# st.write(f"{input_csv_name}")

df = pd.read_csv(f"{data_dir}{input_csv_name}")
# df_b = df.copy()


# df=df[(df["latitude_v_world"]!=0)]
# df.drop(df[(df['latitude_v_world'] == 0)].index, inplace=True)
# # #난수 발생 하여 1000개의 값을 출력하는 코드

# # version2_1- insert를 모두 주석처리

# # 그 데이터를 활용하여 필터링을 걸어준다.
# st.sidebar.title('Good_Price_Store🌸')

# # city_province_dict = {}

# province_list= list(df["city_province"].unique())
# # select_one 변수에 사용자가 선택한 값이 지정됩니다
# add_one = "시/도"
# # province_list.insert(0,add_one)
# select_city_province = st.sidebar.selectbox(
#     add_one,
#     province_list
# )
# sentence = "옵션반영"+" "+add_one
# checkbox_btn_1 = st.sidebar.checkbox(sentence,True,1)
# if checkbox_btn_1:
#     df = df[(df['city_province'] == select_city_province)]

# county_district_list= list(df["city_county_district"].unique())
# add_one = '시/군/구'
# # county_district_list.insert(0,add_one)
# select_city_county_district = st.sidebar.selectbox(
#     add_one,
#     county_district_list
# )
# sentence = "옵션반영"+" "+add_one
# checkbox_btn_2 = st.sidebar.checkbox(sentence,True,2)
# if checkbox_btn_2:
#     df = df[(df['city_county_district'] == select_city_county_district)]

# large_sector_list= list(df["large_sector"].unique())
# add_one = '대분류'
# # large_sector_list.insert(0,add_one)
# select_large_sector_list = st.sidebar.selectbox(
#     add_one,
#     large_sector_list
# )
# sentence = "옵션반영"+" "+add_one
# checkbox_btn_3 = st.sidebar.checkbox(sentence,False,3)
# if checkbox_btn_3:
#     df = df[(df['large_sector'] == select_large_sector_list)]

# sector_list= list(df["sector"].unique())
# add_one = '소분류'
# # sector_list.insert(0,add_one)
# select_sector_list = st.sidebar.selectbox(
#     add_one,
#     sector_list
# )
# sentence = "옵션반영"+" "+add_one
# checkbox_btn_4 = st.sidebar.checkbox(sentence,False,4)
# if checkbox_btn_4:
#     df = df[(df['sector'] == select_sector_list)]

# store_name_list= list(df["store_name"].unique())
# add_one = '가게명'
# # store_name_list.insert(0,add_one)
# select_store_name_list = st.sidebar.selectbox(
#     add_one,
#     store_name_list
# )
# sentence = "옵션반영"+" "+add_one
# checkbox_btn_5 = st.sidebar.checkbox(sentence,False,5)
# if checkbox_btn_5:
#     df = df[(df['store_name'] == select_store_name_list)]

# # 예시 데이터 생성
# data = pd.DataFrame({
#     'lat': df["latitude_v_world"],
#     'lon': df["longitude_v_world"]
# })

# # 지도에 데이터 표시
# st.map(data)

# for i in [1,2,3]:
#     try:
#     # print(len(df.iloc[0]))
#         name = df.iloc[0].index[i]
#         content = df.iloc[0][df.iloc[0].index[i]] 
#         sentence = f"{name} : {content}"
#         st.write(sentence)
#     except:
#         name = df_b.iloc[0].index[i]
#         content = df_b.iloc[0][df_b.iloc[0].index[i]] 
#         sentence = f"{name} : {content}"
#         st.write(sentence)
# # 선택한 종의 맨 처음 5행을 보여줍니다 
# # st.table(df.head())

# # print(df.iloc[0])
