from PIL import Image
import numpy as np
import cv2
import random

def detect_wrinkles(image):
    open_cv_image = np.array(image.convert('L'))
    edges = cv2.Canny(open_cv_image, 100, 200)
    return edges

def get_color_score(image):
    image = image.resize((100, 100))
    data = np.array(image).reshape((-1, 3))
    std_dev = np.std(data, axis=0)
    color_balance = np.mean(std_dev)
    return round(color_balance, 2)

def get_fit_estimate():
    return random.choice(["Tight Fit", "Loose Fit", "Perfect Fit"])

def get_fix_suggestions(wrinkle_level, color_score, fit_estimation):
    suggestions = []
    if wrinkle_level > 30000:
        suggestions.append("🧺 Iron your clothes to remove wrinkles.")
    if color_score > 80:
        suggestions.append("🎨 Try harmonizing colors. Avoid extreme contrasts.")
    if fit_estimation != "Perfect Fit":
        suggestions.append(f"📏 Consider tailoring. Detected: {fit_estimation}")
    return suggestions
