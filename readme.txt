# 🔬 BioLit Intelligence - AI Research Platform

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

**AI-powered research assistant for bioinformatics students and researchers with 9 advanced features.**

## ✨ Features (All Working)

| Feature | Description |
|---------|-------------|
| 📚 **Search Literature** | Search 30M+ PubMed papers with filters |
| 💡 **Paper Recommendations** | AI-powered intelligent suggestions |
| 🔬 **Research Gaps** | Identify unexplored research areas |
| 📊 **Citation Network** | Analyze paper relationships |
| 🏥 **Grant Matching** | Find funding opportunities |
| 📈 **Author Impact** | Track researcher influence |
| 🎯 **Credibility Detection** | Verify claims with AI |
| 📝 **Study Notes** | Auto-generate comprehensive notes |
| 📖 **Full Paper Reading** | Read papers with highlighting |

## 🛠️ Tech Stack

- **Backend**: Python 3.11 + Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **AI/ML**: Groq API (LLM integration)
- **APIs**: PubMed, Groq
- **Deployment**: Render, Gunicorn, GitHub Actions

## 🚀 Quick Start (2 minutes)

### Local Setup
```bash
git clone https://github.com/YOUR-USERNAME/biolit-platform.git
cd biolit-platform
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
pip install -r requirements.txt
python app.py
