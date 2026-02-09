def match_job(resume_skills: list[str], job_skills: list[str]) -> dict:
    if not resume_skills or not job_skills:
        return {
            "match_percentage": 0,
            "matched_skills": [],
            "missing_skills": job_skills or []
        }

    resume = {s.lower().strip() for s in resume_skills}
    job = {s.lower().strip() for s in job_skills}

    matched = set()
    partial = set()

    for j in job:
        for r in resume:
            if j == r:
                matched.add(j)
                break
            elif j in r or r in j:
                partial.add(j)
                break

    score = len(matched) + (0.5 * len(partial))
    percentage = (score / len(job)) * 100

    return {
        "match_percentage": round(min(percentage, 100), 2),
        "matched_skills": list(matched | partial),
        "missing_skills": list(job - matched - partial)
    }
