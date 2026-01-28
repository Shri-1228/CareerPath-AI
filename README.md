[# 🚀 CareerPath AI | Smart Resume Architect

**CareerPath AI** isn't just a builder; it's a strategic career tool. Designed specifically to bridge the gap for students and professionals, it uses the **Google Gemini 1.5 Flash** engine to turn simple text into high-impact, professional narratives.

---

## 🌟 Why CareerPath AI?

Traditional resume builders just give you a template. **CareerPath AI** provides the *content*. It analyzes your raw input and rephrases it to sound more professional, ensuring your first impression is powerful.

### ✨ Exclusive Features:
* **ATS-Optimized Formatting:** Generates structure that is easily readable by Applicant Tracking Systems.
* **Smart Experience Detection:** If you're a **fresher**, the AI automatically shifts focus to your academic excellence and technical projects.
* **Instant Markdown-to-PDF:** Uses `markdown-pdf` to ensure your resume looks exactly the same on every device.
* **Minimalist Interface:** Built with Streamlit for a fast, clutter-free user experience.

---

## 🛠️ The Engine Under the Hood

| Component | Technology |
| :--- | :--- |
| **Brain** | Google Gemini 1.5 Flash API |
| **Interface** | Streamlit (Python-based) |
| **Document Engine** | Markdown-PDF |
| **Deployment** | Dockerized on Hugging Face Spaces |

---

## 📂 Project Blueprint

* `app.py` → The core logic and AI prompt engineering.
* `requirements.txt` → Essential Python libraries (GenAI, Streamlit).
* `Dockerfile` → The environment instructions for the cloud.

---

## 🛡️ Security & Privacy
This app is built with security in mind. Your **Google API Key** is never hardcoded; it is retrieved via `os.getenv` from Hugging Face's secure vault, ensuring your credentials stay private.
](https://huggingface.co/spaces/Shri1228/CareerPath-AI)
