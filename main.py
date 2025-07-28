import json, os, time
from pdf_parser import parse_documents
from ranker import rank_sections
from summarizer import summarize_sections

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"
    os.makedirs(output_dir, exist_ok=True)

    persona_file = os.path.join(input_dir, "persona.json")
    with open(persona_file, "r", encoding="utf-8") as f:
        persona_data = json.load(f)
    
    parsed_sections = parse_documents(input_dir)
    ranked_sections = rank_sections(parsed_sections, persona_data)
    subsection_analysis = summarize_sections(ranked_sections)

    output_json = {
        "metadata": {
            "input_documents": [f for f in os.listdir(input_dir) if f.endswith(".pdf")],
            "persona": persona_data["persona"],
            "job": persona_data["job"],
            "processing_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        },
        "extracted_sections": ranked_sections,
        "subsection_analysis": subsection_analysis
    }

    with open(os.path.join(output_dir, "output.json"), "w", encoding="utf-8") as f:
        json.dump(output_json, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
