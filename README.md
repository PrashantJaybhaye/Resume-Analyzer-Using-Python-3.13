# AI Resume Analyzer

AI Resume Analyzer is a web application built with Streamlit and Python that analyzes uploaded resumes, provides smart recommendations for skills and courses, and gives resume improvement tips. It also offers resume and interview preparation videos, and sends personalized feedback via email if the resume score is low.

## Features

- **Resume Upload & Analysis:** Upload your resume in PDF format and get an instant analysis.
- **Skill & Course Recommendations:** Get personalized skill and course suggestions based on your resume content.
- **Resume Score:** Receive a score based on resume content and structure, with actionable tips for improvement.
- **Video Resources:** Watch curated videos for resume writing and interview preparation.
- **Email Feedback:** Automatically receive resume improvement tips via email if your score is below a threshold.
- **Admin Panel:** View and download user analytics and reports (admin access required).

## Installation

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd ai-analyze
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Download NLTK data:**
   ```
   python nltk_setup.py
   ```

4. **Set up MySQL database:**
   - Ensure MySQL is running and update credentials in `app.py` if needed.
   - The app will create the required database and tables automatically.

## Usage

Start the Streamlit app:
```
streamlit run app.py
```

- **User Mode:** Upload your resume and receive analysis and recommendations.
- **Admin Mode:** Log in with admin credentials to view user data and download reports.

## Project Structure

- `app.py` - Main Streamlit application.
- `Courses.py` - Contains course and video recommendation lists.
- `nltk_setup.py` - Downloads required NLTK data.
- `Logo/` - Contains logo images.
- `Uploaded_Resumes/` - Stores uploaded resumes.

## Requirements

- Python 3.8+
- Streamlit
- NLTK
- PyResparser
- pdfminer
- pymysql
- plotly
- streamlit-tags
- yt-dlp
- Pillow

(See `requirements.txt` for the full list.)

## Credits

Developed by Prashant Jaybhaye.

## License

This project is for educational purposes.
