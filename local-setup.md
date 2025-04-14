# 🛠️ Local Setup Guide

Follow these steps to run the AI Engagement Accelerator Kit locally.

## 1. Clone the Repo

```bash
git clone https://github.com/stanchat/AIEngagementAcceleratorKit.git
cd AIEngagementAcceleratorKit
```

## 2. Set Up Environment (Windows)

```bash
setup.bat
```

## 3. Activate Virtual Environment

```bash
.\venv\Scripts\activate
```

## 4. Run Streamlit Demo

```bash
cd streamlit_apps
streamlit run agentic_pdf_assistant.py
```

Ensure you have an `.env` file with:
```env
OPENAI_API_KEY=your_key_here
```
