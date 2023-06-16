# pip install streamlit
# streamlit hello
# ctrl + c: 실행종료

import streamlit as st # streamlit -> import(가져오기) -> as (st 이름)
# st라는 변수명으로 streamlit의 기능들을 사용하겠다

# streamlit run app.py

st.title("제목")
st.header("헤더")
st.subheader("그래도 잘 만들었죠?")
st.write("내가 만든 streamlit 페이지, 너를 위해 구웠지")
# 여러 가지 옵션을 넣어서 세부 기능들을 차이
st.video("https://youtu.be/VlGaMV64F4s")
st.image(image="img/space.jpeg", use_column_width=True) # 인터넷 사진 주소
st.image(image="img/space.jpeg", width=100) # 인터넷 사진 주소


st.title("components")
# 위-아래로 한 줄로만....
st.write("👨🏿‍🔬")
cols = st.columns(2)  # 컬럼 리스트
cols[0].write("👨🏿‍🔬")
cols[1].write("👨🏿‍🔬")
cols = st.columns(3)
# 🐦 -> n등분 -> 3등분
cols[0].write("🐦")
cols[1].write("🐦")
cols[-1].write("🐦")
cols = cols[0].columns(3) # 열의 열인 거임
cols[0].write("🐦")
cols[1].write("🐦")
cols[-1].write("🐦")

col1, col2 = st.columns(2) # 리스트 언패킹
col1.write("왼쪽 열")
col2.write("오른쪽 열")

with col1: # col1을 기준으로 streamlit을 써주겠다
    # 블록 (:) 을 열면 -> 이 안에서는 streamlit 기능 실행시 col1에 종속
    st.write("왼쪽")
with col2:  # col2을 기준으로 streamlit을 써주겠다
# 블록 (:) 을 열면 -> 이 안에서는 streamlit 기능 실행시 col2에 종속
    st.write("오른쪽")