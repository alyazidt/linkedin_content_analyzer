import streamlit as st
from generate_post import generate_post
from analyzer import analyze_posts

st.set_page_config(page_title="تحليل محتوى لينكدن", layout="centered")

st.title("📊 بروتوكول تحليل محتوى لينكدن الخاص بك")

with st.form("linkedin_form"):
    st.write("أدخل منشور لك في لينكدن")
    posts = [st.text_area(f"منشور {i+1}", height=150) for i in range(5)]
    goal = st.selectbox("🎯 الهدف", ["زيادة التفاعل"])
    dialect = st.selectbox("🗣️ اللهجة المفضلة", ["العربية الفصحى", "الانجليزية"])
    submitted = st.form_submit_button("تحليل المنشور")

if submitted:
    with st.spinner("جاري التحليل..."):
        filtered_posts = [p for p in posts if p.strip() != ""]
        report = analyze_posts(filtered_posts, goal, dialect)
        st.success("✅ تم التحليل")
        st.markdown(report)

        st.download_button("📥 تحميل التقرير", report, file_name="linkedin_report.md")
