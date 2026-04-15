import streamlit as st

st.set_page_config(page_title="AI Landing Page Personalizer", layout="centered")

st.title("🚀 AI Landing Page Personalizer")

# Inputs
ad_input = st.text_area("Enter Ad Text")
url_input = st.text_input("Enter Landing Page URL")

# Dummy landing page content
def get_page_content(url):
    return {
        "headline": "Welcome to our platform",
        "subheadline": "Learn skills online",
        "cta": "Get Started",
        "sections": ["Courses", "Pricing", "Testimonials"]
    }

# --- MOCK AGENTS ---

def ad_analyzer(ad_text):
    ad_text_lower = ad_text.lower()

    audience = "General Audience"
    if "student" in ad_text_lower:
        audience = "Students"

    offer = "Special Offer"
    if "50%" in ad_text_lower or "discount" in ad_text_lower:
        offer = "50% Discount"

    tone = "Promotional"
    if "limited" in ad_text_lower:
        tone = "Urgent"

    return {
        "audience": audience,
        "offer": offer,
        "tone": tone,
        "message": "Save money and learn faster",
        "keywords": ["discount", "offer", "learning"]
    }


def page_analyzer(page_content):
    return page_content


def personalize(ad_json, page_json):
    headline = f"{ad_json['offer']} for {ad_json['audience']} – Start Learning Today!"
    cta = "Claim Your Offer Now"

    return {
        "improved_headline": headline,
        "improved_subheadline": "Upskill with personalized courses designed for you",
        "improved_cta": cta
    }


def validate(ad_json, improved_json):
    return {
        "alignment_score": "High",
        "issues": [],
        "is_valid": True,
        "suggestions": ["Ensure consistency across all sections"]
    }

# --- MAIN FLOW ---

if st.button("✨ Generate Personalized Page"):

    if not ad_input or not url_input:
        st.warning("Please enter both inputs.")
    else:
        page_data = get_page_content(url_input)

        ad_data = ad_analyzer(ad_input)
        page_data = page_analyzer(page_data)
        improved = personalize(ad_data, page_data)
        validation = validate(ad_data, improved)

        st.divider()

        # 🔥 VISUAL OUTPUT

        st.subheader("🌐 Personalized Landing Page Preview")
        st.caption("🔄 Personalized based on ad input • Optimized for higher conversion")

        st.markdown(f"""
        <div style="padding:20px; border-radius:10px; background-color:#f8fafc;">
        <h1 style="color:#2c3e50;">
        {improved['improved_headline']}
        </h1>

        <p style="font-size:18px; color:#555;">
        {improved['improved_subheadline']}
        </p>

        <button style="
        margin-top:15px;
        background-color:#ff4b4b;
        color:white;
        padding:12px 20px;
        border:none;
        border-radius:8px;
        font-size:16px;
        cursor:pointer;
        ">
        {improved['improved_cta']}
        </button>

        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # 🔍 Show comparison (this is powerful)

        st.subheader("🔍 Before vs After")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Original")
            st.write("**Headline:**", page_data["headline"])
            st.write("**CTA:**", page_data["cta"])

        with col2:
            st.markdown("### 🟢 Improved")
            st.write("**Headline:**", improved["improved_headline"])
            st.write("**CTA:**", improved["improved_cta"])

        st.divider()

        # 🧠 Validation

        st.subheader("🧠 AI Validation")
        st.write("Alignment Score:", validation["alignment_score"])
        st.write("Valid Output:", validation["is_valid"])
        st.write("Suggestions:")
        for s in validation["suggestions"]:
            st.write(f"• {s}")