import streamlit as st
from generate_post import generate_post

st.set_page_config(page_title="تحليل محتوى لينكدن", layout="centered")

st.title("📊 بروتوكول تحليل محتوى لينكدن الخاص بك")

st.markdown("""
👋 أدخل منشورك، وسنساعدك في زيادة التفاعل عليه من خلال تحليل متكامل واقتراحات جاهزة للنشر.
""")

with st.form("linkedin_single_post"):
    st.subheader("✍️ أدخل المنشور")
    content = st.text_area("محتوى المنشور", height=200, placeholder="انسخ منشورك هنا...")

    submitted = st.form_submit_button("🔍 تحليل المنشور")

if submitted:
    if not content.strip():
        st.warning("يرجى إدخال محتوى المنشور.")
    else:
        with st.spinner("⏳ جاري التحليل..."):
            # الهدف ثابت: زيادة التفاعل، اللهجة: العربية الفصحى
            report = generate_post(content, goal="زيادة التفاعل", dialect="العربية الفصحى")
            st.success("✅ تم التحليل بنجاح")

            st.markdown("### 📄 التقرير الكامل")
            st.markdown(report, unsafe_allow_html=True)

            st.download_button(
                "📥 تحميل التقرير",
                report,
                file_name="linkedin_post_analysis.md",
                mime="text/markdown"
            )
