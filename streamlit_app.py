import streamlit as st

# 페이지 설정 (웹 브라우저 탭에 표시될 타이틀과 아이콘)
st.set_page_config(page_title="나의 자기소개 페이지", page_icon="👋", layout="centered")

# --- 헤더 섹션 ---
st.title("안녕하세요! 저를 소개합니다")
st.subheader("지속적으로 성장하는 개발자, [이유나 ]입니다.")
st.write("새로운 기술을 배우고 문제를 해결하는 과정에서 즐거움을 느낍니다.")

st.markdown("---")

# --- 프로필 섹션 (레이아웃 나누기) ---
col1, col2 = st.columns([1, 2])

with col1:
    # 프로필 이미지 (이미지 파일이 있다면 'profile.jpg' 등으로 대체 가능)
    # 여기서는 샘플 이미지를 사용했습니다.
    st.image("https://via.placeholder.com/150", caption="[당신의 이름]", use_container_width=True)

with col2:
    st.markdown("###  About Me")
    st.write(" **위치:** 대한민국 서울")
    st.write(" **이메일:** your_email@example.com")
    st.write(" **GitHub:** [github.com/your-profile](https://github.com)")
    st.write(" **한 줄 다짐:** 내일의 나는 오늘의 나보다 더 나은 개발자가 되자!")

st.markdown("---")

# --- 기술 스택 섹션 ---
st.markdown("### 🛠️ Tech Stacks")

# 태그 형태로 보여주기 위해 컬럼 활용
badge_col1, badge_col2, badge_col3 = st.columns(3)
with badge_col1:
    st.success("Language: Python, SQL")
with badge_col2:
    st.info("Framework: Streamlit, FastAPI")
with badge_col3:
    st.warning("Tools: Git, Docker")

st.markdown("---")

# --- 프로젝트 / 경력 섹션 ---
st.markdown("### 🚀 Projects")
with st.expander("1. 스트림릿을 활용한 포트폴리오 웹 제작"):
    st.write("- **설명:** 자신을 소개하는 웹 애플리케이션을 Streamlit으로 빠르고 쉽게 구현")
    st.write("- **주요 기능:** 프로필 표시, 기술 스택 시각화, 방문자 메시지 받기")
    st.write("- **성과:** 파이썬 코드 몇 줄만으로 반응형 웹 페이지 배포 완료!")

with st.expander("2. 기타 프로젝트 제목"):
    st.write("- **설명:** 프로젝트에 대한 간단한 설명을 적어보세요.")

st.markdown("---")

# --- 방문자 방명록 섹션 (인터랙션 기능) ---
st.markdown("### 💬 방명록")
st.write("저에게 응원의 한 마디나 궁금한 점을 남겨주세요!")

# 간단한 입력 폼
with st.form(key="guestbook_form", clear_on_submit=True):
    visitor_name = st.text_input("이름/닉네임")
    visitor_message = st.text_area("메시지")
    submit_button = st.form_submit_button(label="남기기")

if submit_button:
    if visitor_name and visitor_message:
        st.success(f"🎉 {visitor_name}님, 소중한 메시지 감사합니다!")
        # 실제 서비스에서는 이 데이터를 DB나 파일에 저장하도록 확장할 수 있습니다.
    else:
        st.warning("이름과 메시지를 모두 입력해주세요!")