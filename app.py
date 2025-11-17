import os
import shutil
from flask import Flask, render_template, request, send_from_directory
import PyPDF2
from docx import Document

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
SHORTLIST_FOLDER = "shortlisted_resumes"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(SHORTLIST_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["SHORTLIST_FOLDER"] = SHORTLIST_FOLDER

# Required skills for shortlisting
REQUIRED_SKILLS = ["python", "matplotlib", "pandas", "machine learning", "sql"]

def extract_text(file_path):
    """Extract text from PDF or DOCX"""
    if file_path.endswith(".pdf"):
        text = ""
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
        return text.lower()

    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        return " ".join([p.text for p in doc.paragraphs]).lower()
    else:
        return ""

def shortlist_resume(text):
    """Return matched skills from text"""
    return [skill for skill in REQUIRED_SKILLS if skill in text]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["resume"]
        if uploaded_file.filename != "":
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
            uploaded_file.save(file_path)

            # Extract text and check skills
            text = extract_text(file_path)
            matched_skills = shortlist_resume(text)

            # Calculate percentage match
            total = len(REQUIRED_SKILLS)
            matched = len(matched_skills)
            percentage = (matched / total) * 100

            shortlisted = percentage >= 75

            # If shortlisted → move to shortlisted_resumes folder
            if shortlisted:
                dest_path = os.path.join(app.config["SHORTLIST_FOLDER"], uploaded_file.filename)
                shutil.copy(file_path, dest_path)

            return render_template(
                "results.html",
                filename=uploaded_file.filename,
                skills=matched_skills,
                total=total,
                matched=matched,
                percentage=percentage,
                shortlisted=shortlisted
            )

    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    """Show all shortlisted resumes"""
    files = os.listdir(app.config["SHORTLIST_FOLDER"])
    return render_template("dashboard.html", files=files)

@app.route("/download/<filename>")
def download_file(filename):
    """Allow HR to download shortlisted resumes"""
    return send_from_directory(app.config["SHORTLIST_FOLDER"], filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
