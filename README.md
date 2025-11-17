# 📄 Resume Shortlister using Python (NLP + Automation)

The **Resume_Shortlister** is an automated system built with **Python, NLP, and Web Technologies** that analyzes resumes and compares them with a job description. It calculates a **match percentage** using text similarity techniques and automatically shortlists candidates who meet the required threshold set by HR.

This tool saves HR teams countless hours by eliminating manual resume screening.

---

## ⭐ Features

### 🔍 **Automated Resume Screening**
- Uses NLP to extract text from resumes.
- Compares resume content with the job description.
- Calculates a similarity score using ML/NLP techniques.

### ✔️ **Smart Shortlisting**
- HR sets a cutoff match percentage.
- Resumes above the threshold are saved in the `shortlisted/` folder.
- Automatically organizes shortlisted resumes as PDFs.

### 🖥️ **HR Dashboard**
- Displays all shortlisted candidates.
- Shows match scores for each candidate.
- Allows HR to download resumes directly.
- Simple, clean, and user-friendly design.

### 📁 **File Upload System**
- Upload resumes (PDF format recommended).
- Upload job descriptions.
- System processes files in real-time.

---

## 🚀 Working Process

1. HR uploads the **job description**.
2. HR uploads one or multiple **resumes**.
3. NLP extracts text from each resume.
4. System compares each resume with the job description.
5. A match percentage is calculated for every resume.
6. If the match ≥ threshold, the resume is **shortlisted**.
7. The resume PDF is saved to the `shortlisted/` folder.
8. HR dashboard displays:
   - Candidate name  
   - Match percentage  
   - Download button  

This automated pipeline helps HR quickly identify top candidates without manually reading each resume.

---

## 🧠 Technologies Used

- **Python**
- **Flask** (Backend Web Framework)
- **NLP (Natural Language Processing)**
  - TF-IDF Vectorizer
  - Cosine Similarity
- **HTML / CSS**
- **PDF Miner / PyPDF2** (for extracting text from PDFs)
- **Werkzeug** (File handling)
- **Jinja2 Templates**

---

## 📂 Project Structure

