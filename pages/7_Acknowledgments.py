import streamlit as st
from utils import create_navigation_buttons

st.set_page_config(layout="wide",
                   initial_sidebar_state="collapsed")

# Custom CSS for larger font size
st.markdown("""
<style>
    /* Global font size increase for all text */
    body {
        font-size: 1.5em; /* Base font size. You can adjust this value (e.g., 1.1em, 1.2em, 1.3em) */
        line-height: 1; /* Improve readability with more line spacing */
    }

    /* Adjust specific Streamlit elements to inherit or have slightly different sizes */
    .stMarkdown, .stText, .stAlert, .stInfo, .stSuccess, .stWarning {
        font-size: inherit; /* Inherit the global font size */
    }

    /* Headings */
    h1 {
        font-size: 2.2em !important; /* For main titles */
        line-height: 1 !important;
    }
    h2 {
        font-size: 2em !important; /* For section titles */
    }
    h3 {
        font-size: 1.8em !important; /* For sub-sections */
    }
    p {
        font-size: 1.2em !important;
        line-height: 1.5em !important;
    }
    /* 针对顶级列表项 (直接位于 div.stMarkdown ul 或 div.stMarkdown ol 下) */
    li {
        font-size: 1em !important;
        line-height: 1.5em !important;
    }

    /* 针对所有更深层嵌套的列表项，让它们恢复 Streamlit 默认的相对大小 */
    /* 或者明确指定它们相对父级的大小 */
    div.stMarkdown ul ul li,
    div.stMarkdown ol ol li,
    div.stMarkdown ul ol li,
    div.stMarkdown ol ul li {
        font-size: 0.9em !important; /* 强制嵌套列表项更小，例如 0.9em */
        /* 或者可以尝试：font-size: inherit !important; 让它们继承 */
        line-height: 1.5em !important;
    }



    /* Code blocks - often benefit from being slightly smaller than body text for readability of code itself */
    pre, code {
        font-size: 0.8em !important; /* Slightly smaller than body text for code snippets */
        line-height: 1;
    }

    /* For the sidebar navigation links */
    .st-emotion-cache-1f8d951 a { /* Target sidebar links */
        font-size: 1.1em; /* Make sidebar links slightly larger */
    }
    .st-emotion-cache-vk33as { /* Target sidebar text elements */
        font-size: 1.1em;
    }


</style>
""", unsafe_allow_html=True) # Important: This allows injecting HTML/CSS

create_navigation_buttons(__file__, 'upper')
st.markdown("---") # Add a separator below the buttons

st.title("7. ACKNOWLEDGMENTS")

from streamlit_extras.stylable_container import stylable_container
with stylable_container(
    key="acknowledgments",
    css_styles="""
        {
            background: linear-gradient(90deg, #e7f2ff 0%, #ffffff 100%);
            border-radius: 0.5rem;
            padding: 1.2rem;
            border: 1px solid #b3d7ff;
        }
    """,
):
    st.markdown("""
        #### 🎈 The author would like to sincerely thank:
        *   **Menghao Xu**, statistician at AstraZeneca, and **Houmin Xing**, then an intern, and **Yibin Xiong**, then an FSP
                    
        *   for their invaluable contributions to the initial stages of this work. 
                    
        #### 🎊 Special thanks are also extended to:
        *   **Kevin Huang**, programmer at AstraZeneca, and my supervisor **Yiwen Wang** 
                    
        *   for their thoughtful review and constructive support on this manuscript. 
        
        #### 👾 The author also gratefully acknowledges the assistance of **AI-based writing tools** during the preparation of this article.
    """)

st.markdown("---") # Add a separator below the buttons
create_navigation_buttons(__file__, 'lower')