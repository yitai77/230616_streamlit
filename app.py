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

# 마크다운
# https://heropy.blog
# st.write ->


# 제목 마크다운
st.write("""
# 가장 큰 제목 (h1 - headline1 - st.title)
## 그 다음 큰 제목 (h2 - headline2 - st.header)
### 그것보단 작은 제목 <- 대부분 여기까지만 씀 (h3 - headline3 - st.subheader)
#### 좀 더 작은 제목 (h4)
##### 이건 없겠지? (h5)
###### 이것도 있나? (h6)
####### 이건 없어.
""")# 문자열을 넣으면 마크다운

# 서식
text = """
기울임 : *별표*를 또는 _언더바_ 하나씩 써주면

진하게(bold) : **별표**를 __언더바__두개씩 써주면

기울임 + 진하게(bold) : ***별표***를 또는 ___언더바___ 세개씩 써주면

취소선 : ~물결표~

밑줄 : <u>밑줄</u>

형광펜 : <mark>형광펜</mark>
"""
st.write(text)
st. markdown(text, unsafe_allow_html=True)
