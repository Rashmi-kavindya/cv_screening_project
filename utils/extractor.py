import fitz  # PyMuPDF
import docx2txt

def extract_text(file):
    filename = file.filename.lower()
    if filename.endswith('.pdf'):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return " ".join([page.get_text() for page in doc])
    elif filename.endswith('.docx'):
        return docx2txt.process(file)
    else:
        return ""
