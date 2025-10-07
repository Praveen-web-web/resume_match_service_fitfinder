def score_candidate_resume(parsed_data: dict, required_skills: list[str]) -> float:
    text = parsed_data.get("text", "").lower()
    required_skills_lower = [skill.lower() for skill in required_skills]
    matched_skills = [skill for skill in required_skills_lower if skill in text]
    score = len(matched_skills) / len(required_skills) * 100  # simple match % score
    return score
