import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

st.set_page_config(
    page_title="LinkedIn Post Generator",
    layout="wide"
)
st.markdown("""
<style>
.main{
    padding-top:2rem;
}
.hero{
    background: linear-gradient(135deg,#0F172A,#1E40AF);
    color:white;
    padding:30px;
    border-radius:18px;
    text-align:center;
}
.post-box{
    background:#F8FAFC;
    padding:25px;
    border-radius:16px;
    border:1px solid #E2E8F0;
    white-space: pre-wrap;
    font-size:16px;
}
.metric-box{
    background:#F8FAFC;
    padding:12px;
    border-radius:12px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# options for length and language
length_options = ["Short","Medium","Long"]
language_options = ["English","Hinglish"]

def main():

    st.markdown("""
    <div class>
        <h1>LinkedIn Post Generator</h1>
        <p>Create engaging LinkedIn Post using Few-Shot Prompting + LLM </p>
        </div>
        """,unsafe_allow_html=True)
    st.write("")

    fs = FewShotPosts()
    tags = fs.get_tags()
    st.sidebar.header("Generation Settings")

    selected_tag = st.sidebar.selectbox("Topic", tags)
    selected_length = st.sidebar.selectbox("Length", length_options)
    selected_language = st.sidebar.selectbox("Language", language_options)
    col1, col2, col3 = st.columns(3)
    with col1: selected_tag = st.selectbox("Title", options=tags)
    with col2: selected_length = st.selectbox("Length", options=length_options)
    with col3: selected_language = st.selectbox("Language", options=language_options)


    st.markdown("Generate post")

    if st.button("Generate Post", use_container_width=True):
        with st.spinner("Generating your LinkedIn post..."):
            post = generate_post(
                selected_length,
                selected_language,
                selected_tag
            )

        st.success("Post Generated Successfully!")





        st.write("")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Words", len(post.split()))

        with col2:
            st.metric("Characters", len(post))

        st.write("")

        st.code(post, language="text")

        st.download_button(
            "Download Post",
            data=post,
            file_name="linkedin_post.txt",
            mime="text/plain",
            use_container_width=True
        )


if __name__=="__main__":
    main()
