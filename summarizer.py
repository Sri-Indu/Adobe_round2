from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

def summarize_text(text, sentence_count=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join([str(sentence) for sentence in summary])

def summarize_sections(ranked_sections):
    summarized = []
    for sec in ranked_sections:
        refined_text = summarize_text(sec["section_title"])
        summarized.append({
            "document": sec["document"],
            "refined_text": refined_text,
            "page": sec["page"]
        })
    return summarized
