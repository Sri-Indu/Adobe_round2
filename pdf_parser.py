import fitz
import os

def parse_pdf(file_path):
    doc = fitz.open(file_path)
    sections = []
    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("blocks")
        for block in blocks:
            text = block[4].strip()
            if len(text.split()) < 20 and len(text) > 3:  # potential heading
                sections.append({
                    "document": os.path.basename(file_path),
                    "page": page_num,
                    "section_title": text,
                    "text": text
                })
    return sections

def parse_documents(input_dir):
    parsed_sections = []
    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            parsed_sections.extend(parse_pdf(os.path.join(input_dir, file)))
    return parsed_sections
