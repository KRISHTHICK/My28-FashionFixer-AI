import streamlit as st
from PIL import Image
import numpy as np
from image_utils import detect_wrinkles, get_color_score, get_fit_estimate, get_fix_suggestions

st.set_page_config(page_title="🧳 FashionFixer AI", layout="wide")
st.title("🧳 FashionFixer AI – Outfit Repair & Enhancement Advisor")

st.markdown("Upload an outfit photo to analyze wrinkles, colors, and fit. Get smart suggestions to fix your look.")

uploaded_file = st.file_uploader("📸 Upload Outfit Image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=300)

    st.subheader("🔍 Wrinkle Detection")
    wrinkles = detect_wrinkles(image)
    wrinkle_level = np.sum(wrinkles > 0)
    st.write(f"Detected wrinkle intensity: {wrinkle_level}")
    st.image(wrinkles, caption="Wrinkle Highlight", use_column_width=True, clamp=True)

    st.subheader("🎨 Color Harmony Analysis")
    color_score = get_color_score(image)
    st.write(f"Color Harmony Score: {color_score}")
    if color_score > 80:
        st.warning("⚠️ Colors may clash. Try softer blends.")
    else:
        st.success("✅ Color scheme looks balanced!")

    st.subheader("📐 Fit Estimation")
    fit_estimation = get_fit_estimate()
    st.write(f"Estimated Fit: {fit_estimation}")

    st.subheader("🛠 Fix Suggestions")
    suggestions = get_fix_suggestions(wrinkle_level, color_score, fit_estimation)
    if suggestions:
        for tip in suggestions:
            st.write(tip)
    else:
        st.success("👌 No fixes needed. You're stylish!")

    st.info("Tips are generated using basic visual cues. For best results, use a clear full-body outfit image.")
