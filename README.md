# 🎨 Branded QR Asset Generator

A professional utility for creative technologists to generate brand-aligned QR codes. Unlike standard generators, this tool allows for precise hexadecimal color mapping and high error-correction density.

## 🔗 Live Demo
Check out the live app here: [https://your-qr-app-link.streamlit.app/](https://your-qr-app-link.streamlit.app/)

## 🚀 Project Overview
In modern advertising (like your work with **ACL or BOC**), consistency is key. This tool automates the creation of QR assets that integrate seamlessly into TVCs, social media banners, and print material.

### Key Features:
* **Brand-Specific Hex Mapping:** Input any brand color for the foreground and background.
* **Production-Ready Output:** High-resolution PNG exports.
* **High Error Correction (Level H):** Ensures the QR remains scannable even if partially obscured or printed on textured surfaces.
* **Interactive UI:** Built with Streamlit for a fast, iterative design process.



## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Engine:** qrcode (PIL-based rendering)
* **Frontend:** Streamlit
* **Image Processing:** Pillow (PIL)

## 🧠 The Logic
The generator uses a matrix-based encoding algorithm:
1. **Data Encoding:** Converts the URL string into binary data.
2. **Matrix Generation:** Maps data into a 21x21 grid (Version 1).
3. **Color Substitution:** Replaces standard black/white pixels with user-defined Hex colors.
4. **Padding:** Applies a specific 'Quiet Zone' (Border) to ensure scanner recognition.

---
Developed by **Rukshan Weerasekara** *Creative Technologist | Animator | AI Developer*
