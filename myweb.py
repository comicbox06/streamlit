import streamlit as st


st.set_page_config(
    page_title="리로스쿨"

)
st.header('TEST')

option = st.selectbox(
    '학년',
    ('1', '2', '3'))
option1 = st.selectbox(
    '반',
    ('1', '2', '3', '4', '5', '6', '7', '8', '9'))
title = st.text_input('이름')
if title:
    st.write(option,"학년", option1,"반", title,"이 맞습니까?")
else:
    st.write(option, "학년", option1, "반 이 맞습니까?")
if st.button('네'):
    st.write('인증완료')
    st.image('OIP.jpg', width=300)
else:
    st.write('')

st.header("주요과목 선택")
genre = st.radio(".", ("수학1", "실용영어", "언어와 매체"), label_visibility='hidden')

if genre == "수학1":
    st.write('수학1을 선택하셨습니다.')


if genre == "실용영어":
    st.write('실용영어를 선택하셨습니다.')

if genre == "언어와 매체":
        st.write('언어와 매체를 선택하셨습니다.')



# st.header("선택과목")
#
# genre1 = st.checkbox(
#         ("물리"))
#
# if genre1:
#         st.write('물리를 선택하셨습니다.')
#
# genre2 = st.checkbox(
#         ("화학"))
# if genre2:
#         st.write('화학을 선택하셨습니다.')
#
# genre3 = st.checkbox(
#         ("생명과학"))
# if genre3:
#         st.write('생명과학을 선택하셨습니다.')
#
# genre4 = st.checkbox(
#         ("지구과학"))
# if genre4:
#         st.write('지구과학을 선택하셨습니다.')
#
# genre5 = st.checkbox(
#         ("과학문제탐구"))
# if genre5:
#         st.write('과학문제탐구를 선택하셨습니다.')


st.subheader("이과")
물리 = st.checkbox('물리')
지구과학 = st.checkbox('지구과학')
화학 = st.checkbox('화학')
생명과학 = st.checkbox('생명과학')
과학문제탐구 = st.checkbox('과학문제탐구')
과목 = ''
if 물리:
    과목 = 과목 + '물리,'
if 지구과학:
    과목 = 과목 + '지구과학,'
if 생명과학:
    과목 = 과목 + '생명과학,'
if 화학:
    과목 = 과목 + '화학,'
if 과학문제탐구:
    과목 = 과목 + '과학문제탐구'


if 과목 == '':
    st.write("신청한 과목이 없습니다.")
else:
    st.write(과목+"를 선택하셨습니다.")

st.subheader("문과")
options = st.multiselect(
    '',
    ["윤리와 사상", "정치와 법", "한국지리", "사회문제탐구"])
if options:
    st.write(options, "을/를 선택하셨습니다.")
else:
    st.write("을/를 선택하셨습니다.")



