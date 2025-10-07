from PyPDF2 import PdfReader
import docx
import os
import json

def parse_pdf_resume(file_path: str) -> dict:
    text = ""
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return {"text": text}

def parse_docx_resume(file_path: str) -> dict:
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return {"text": "\n".join(full_text)}

def parse_resume(file_path: str) -> dict:
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return parse_pdf_resume(file_path)
    elif ext == ".docx":
        return parse_docx_resume(file_path)
    else:
        # fallback: read as text file
        with open(file_path, "r", encoding="utf-8") as f:
            return {"text": f.read()}
