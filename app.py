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
st.image(image="img/img.jpeg", use_column_width=True) # 인터넷 사진 주소
st.image(image="img/img.jpeg", width=100) # 인터넷 사진 주소


