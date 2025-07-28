<<<<<<< HEAD
# Adobe India Hackathon Round 2: Persona-Driven Document Intelligence

## 🚀 What this project does
This project processes 3-10 related PDFs, takes a persona and job-to-be-done, and outputs:
- Relevant ranked sections
- Refined subsection summaries
- Metadata for the run

All **offline, CPU-only, under 60 seconds**, ready for submission.

## 📂 Folder Structure
- `main.py`: Orchestrates parsing, ranking, summarization
- `pdf_parser.py`: Extracts potential headings/sections from PDFs
- `ranker.py`: Ranks sections using offline embeddings
- `summarizer.py`: Generates summaries for subsections
- `input/`: Place your PDFs and `persona.json` here
- `output/`: Outputs `output.json` here
- `requirements.txt`, `Dockerfile`: For environment and containerization

## 🛠️ Build
```bash
docker build --platform linux/amd64 -t adobe_r2_solution:latest .
=======
# Adobe_round2
>>>>>>> f78251bf1ff468424f8e91d1b5bf06ebd19956a8
