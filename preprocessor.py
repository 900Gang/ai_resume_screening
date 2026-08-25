import re

def  clean_text(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = text.strip()
    return text

if __name__ == "__main__":
    from extractor import extract_pdf_text

    text = extract_pdf_text("uploads/ANAND_N_resume_ATS_New.pdf")
    cleaned_text = clean_text(text)

    print(cleaned_text)
    