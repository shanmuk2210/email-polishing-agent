import streamlit as st

from main import polish_email
from config.settings import (
    APP_NAME,
    APP_ICON,
    MODEL_NAME,
    TEMPERATURE,
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background: #f6f7fb;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* ---------- SIDEBAR ---------- */

    section[data-testid="stSidebar"] {
        background: #111827;
    }

    section[data-testid="stSidebar"] * {
        color: #f9fafb;
    }

    .sidebar-logo {
        text-align: center;
        padding: 1rem 0 1.5rem 0;
    }

    .sidebar-icon {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }

    .sidebar-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: white;
    }

    .sidebar-subtitle {
        font-size: 0.85rem;
        color: #9ca3af;
        margin-top: 0.3rem;
    }

    .sidebar-section {
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #9ca3af !important;
    }

    .sidebar-step {
        padding: 0.7rem 0;
        border-bottom: 1px solid #374151;
    }

    .sidebar-step-number {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 25px;
        height: 25px;
        border-radius: 50%;
        background: #4f46e5;
        color: white;
        font-size: 0.75rem;
        font-weight: 700;
        margin-right: 0.5rem;
    }

    /* ---------- HEADER ---------- */

    .header {
        margin-bottom: 1.5rem;
    }

    .header-title {
        font-size: 2.7rem;
        font-weight: 800;
        letter-spacing: -0.04em;
        color: #111827;
        margin: 0;
    }

    .header-subtitle {
        color: #6b7280;
        font-size: 1.05rem;
        margin-top: 0.4rem;
    }

    /* ---------- FEATURE CARDS ---------- */

    .feature-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 1rem 1.1rem;
        height: 100%;
        box-shadow: 0 2px 7px rgba(0,0,0,0.025);
    }

    .feature-icon {
        font-size: 1.5rem;
    }

    .feature-title {
        font-weight: 700;
        color: #111827;
        margin-top: 0.35rem;
    }

    .feature-description {
        color: #6b7280;
        font-size: 0.85rem;
        line-height: 1.4;
        margin-top: 0.2rem;
    }

    /* ---------- EDITOR ---------- */

    .editor-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #111827;
        margin-bottom: 0.2rem;
    }

    .editor-description {
        color: #6b7280;
        font-size: 0.85rem;
        margin-bottom: 1rem;
    }

    /* ---------- TEXT AREA ---------- */

    textarea {
        border-radius: 10px !important;
        border-color: #d1d5db !important;
        font-size: 0.95rem !important;
        line-height: 1.6 !important;
    }

    textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 1px #6366f1 !important;
    }

    /* ---------- BUTTONS ---------- */

    .stButton > button {
        border-radius: 9px;
        font-weight: 600;
        min-height: 42px;
    }

    .stDownloadButton > button {
        border-radius: 9px;
        font-weight: 600;
        min-height: 42px;
    }

    /* ---------- RESULT ---------- */

    .result-empty {
        height: 400px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        background: #fafafa;
        border: 1px dashed #d1d5db;
        border-radius: 12px;
        color: #9ca3af;
    }

    .result-empty-icon {
        font-size: 2.8rem;
        margin-bottom: 0.5rem;
    }

    .result-empty-title {
        font-weight: 600;
        color: #6b7280;
    }

    .result-empty-description {
        font-size: 0.85rem;
        margin-top: 0.25rem;
    }

    /* ---------- STATUS ---------- */

    .success-badge {
        display: inline-block;
        background: #ecfdf5;
        color: #047857;
        border: 1px solid #a7f3d0;
        border-radius: 999px;
        padding: 0.25rem 0.7rem;
        font-size: 0.75rem;
        font-weight: 600;
        margin-bottom: 0.7rem;
    }

    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 0.8rem;
        padding: 2rem 0 1rem 0;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SESSION STATE
# =========================================================

if "polished_email" not in st.session_state:
    st.session_state.polished_email = ""

if "email_input" not in st.session_state:
    st.session_state.email_input = ""


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-logo">
            <div class="sidebar-icon">✉️</div>
            <div class="sidebar-title">EmailCraft AI</div>
            <div class="sidebar-subtitle">
                Professional email rewriting
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-section">How it works</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="sidebar-step">
            <span class="sidebar-step-number">1</span>
            Write your rough email
        </div>

        <div class="sidebar-step">
            <span class="sidebar-step-number">2</span>
            AI understands your intent
        </div>

        <div class="sidebar-step">
            <span class="sidebar-step-number">3</span>
            Email is professionally polished
        </div>

        <div class="sidebar-step">
            <span class="sidebar-step-number">4</span>
            Copy or download the result
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-section">AI Configuration</div>',
        unsafe_allow_html=True,
    )

    st.caption("Model")
    st.code(MODEL_NAME)

    st.caption("Temperature")
    st.code(str(TEMPERATURE))

    st.markdown(
        '<div class="sidebar-section">Built with</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="
            color:#d1d5db;
            font-size:0.85rem;
            line-height:1.8;
        ">
            ✦ CrewAI<br>
            ✦ Ollama<br>
            ✦ Gemma 2<br>
            ✦ Streamlit
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="header">
        <div class="header-title">
            ✉️ EmailCraft AI
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# FEATURE CARDS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">✨</div>
            <div class="feature-title">Professional</div>
            <div class="feature-description">
                Fix grammar, structure, clarity and tone
                without making your email sound robotic.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Intent Preserved</div>
            <div class="feature-description">
                Your original meaning and important facts
                remain intact.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🤝</div>
            <div class="feature-title">Human Sounding</div>
            <div class="feature-description">
                No unnecessary buzzwords, corporate jargon
                or exaggerated formality.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.write("")


# =========================================================
# MAIN EDITOR
# =========================================================

left_col, right_col = st.columns(
    [1, 1],
    gap="large",
)


# =========================================================
# LEFT: ORIGINAL EMAIL
# =========================================================

with left_col:

    st.markdown(
        """
        <div class="editor-title">
            📝 Your Email
        </div>

        <div class="editor-description">
            Write naturally. Don't worry about grammar or formatting.
        </div>
        """,
        unsafe_allow_html=True,
    )

    original_email = st.text_area(
        "Original email",
        height=400,
        key="email_input",
        placeholder="""Example:

hey team,

just wanted to let you know that the demo is kind of ready,
but there are still some things left.

maybe we can show what we have and mention that the rest is
still work in progress.

let me know what you think.

thanks""",
        label_visibility="collapsed",
    )

    # Character count
    char_count = len(original_email)

    st.caption(
        f"{char_count:,} characters"
    )

    button_col1, button_col2 = st.columns(
        [2, 1],
        gap="small",
    )

    with button_col1:

        polish_button = st.button(
            "✨ Polish Email",
            type="primary",
            use_container_width=True,
        )

    with button_col2:

        clear_button = st.button(
            "🗑️ Clear",
            use_container_width=True,
        )


# =========================================================
# CLEAR
# =========================================================

if clear_button:

    st.session_state.email_input = ""
    st.session_state.polished_email = ""

    st.rerun()


# =========================================================
# POLISH
# =========================================================

if polish_button:

    if not original_email.strip():

        st.warning(
            "Please write or paste an email first."
        )

    else:

        with st.spinner(
            "✨ Understanding your email and polishing it..."
        ):

            try:

                result = polish_email(
                    original_email.strip()
                )

                st.session_state.polished_email = result

                st.success(
                    "Your email has been polished successfully!"
                )

            except Exception as e:

                st.error(
                    "Something went wrong while generating "
                    "the email."
                )

                with st.expander("Show technical error"):

                    st.code(str(e))


# =========================================================
# RIGHT: RESULT
# =========================================================

with right_col:

    st.markdown(
        """
        <div class="editor-title">
            ✨ Polished Email
        </div>

        <div class="editor-description">
            Your professional version will appear here.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.session_state.polished_email:

        polished_email = st.session_state.polished_email

        st.markdown(
            """
            <div class="success-badge">
                ✓ Email ready
            </div>
            """,
            unsafe_allow_html=True,
        )

        # -------------------------------------------------
        # DISPLAY POLISHED EMAIL ONLY ONCE
        # -------------------------------------------------

        st.text_area(
            "Polished email",
            value=polished_email,
            height=400,
            key="generated_email",
            label_visibility="collapsed",
        )

        # -------------------------------------------------
        # ACTION BUTTONS
        # -------------------------------------------------

        download_col, copy_col = st.columns(
            [1, 1],
            gap="small",
        )

        with download_col:

            st.download_button(
                label="⬇️ Download",
                data=polished_email,
                file_name="polished_email.txt",
                mime="text/plain",
                use_container_width=True,
            )

        with copy_col:

            # Copy button using HTML + JavaScript
            import streamlit.components.v1 as components

            copy_button_html = f"""
            <button
                onclick="copyEmail()"
                style="
                    width:100%;
                    height:42px;
                    border:none;
                    border-radius:9px;
                    background:#ffffff;
                    color:#111827;
                    border:1px solid #d1d5db;
                    font-size:14px;
                    font-weight:600;
                    cursor:pointer;
                "
            >
                📋 Copy
            </button>

            <script>
                function copyEmail() {{
                    const email = {polished_email!r};

                    navigator.clipboard.writeText(email).then(() => {{
                        const button = document.querySelector("button");
                        button.innerHTML = "✓ Copied!";
                        
                        setTimeout(() => {{
                            button.innerHTML = "📋 Copy";
                        }}, 1500);
                    }});
                }}
            </script>
            """

            components.html(
                copy_button_html,
                height=50,
            )

    else:

        st.markdown(
            """
            <div class="result-empty">
                <div class="result-empty-icon">
                    ✉️
                </div>
                <div class="result-empty-description">
                    Write your email on the left and click
                    "Polish Email".
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        EmailCraft AI · CrewAI · Ollama · Gemma 2
    </div>
    """,
    unsafe_allow_html=True,
)