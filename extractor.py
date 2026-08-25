import pdfplumber


def extract_pdf_text(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text

if __name__ == "__main__":
    text = extract_pdf_text("uploads/ANAND_N_resume_ATS_New.pdf")
    print('--------------------Extracted  Text-----------------------------------------')
    print(text)
    print('------------------------------------------END--------------------------------------')
    print("Characters:",len(text))