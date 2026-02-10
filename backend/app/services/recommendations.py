import re

def tokenize(text: str):
    text = text.lower()
    text = re.sub(r"[^a-z0-9 ]", "", text)
    return set(text.split())

def match_score(resume_text: str, job_text: str):
    resume_tokens = tokenize(resume_text)
    job_tokens = tokenize(job_text)

    if not resume_tokens or not job_tokens:
        return 0

    matched = resume_tokens & job_tokens
    score = len(matched) / len(job_tokens)

    return round(score * 100, 2)
