import re

SKILLS_DB = [
    "python", "java", "fastapi", "django",
    "sql", "mysql", "postgresql",
    "docker", "kubernetes",
    "aws", "azure",
    "git", "github",
    "javascript", "react", "node"
]

def extract_skills(text: str):
    text = text.lower()
    found_skills = set()

    for skill in SKILLS_DB:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.add(skill)

    return list(found_skills)
