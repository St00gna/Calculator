import docx2txt
import pdfminer.high_level



def read_txt(filepath: str) -> str:
    with open(filepath, 'r') as text_file:
        text = text_file.read()

    return text


def read_docx(filepath: str) -> str:
    text = docx2txt.process(filepath)

    return text


def read_pdf(filepath: str) -> str:
    text = pdfminer.high_level.extract_text(filepath)
    return text




def check_file_format(filepath: str) -> str:
    if filepath.endswith(".txt"):
        text = read_txt(filepath)
    elif filepath.endswith(".docx"):
        text = read_docx(filepath)
    elif filepath.endswith(".pdf"):
        text = read_pdf(filepath)
    else:
        return "Wrong file path or Invalid format (valid formats are txt, docx, pdf)"
    return text



