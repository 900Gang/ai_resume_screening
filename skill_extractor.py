SKILLS = {
    "python",
    "sql",
    "html",
    "css",
    "javascript",
    "django",
    "flask",
    "postgresql",
    "docker",
    "git",
    "github",
    "firebase",
    "linux",
    "jenkins",
    "machine learning",
    "data science",
    "natural language processing"
}


def extract_skills(text):

    detected_skills = []

    text = text.lower()

    for skill in SKILLS:

        if skill in text:
            detected_skills.append(skill)
            
    return detected_skills


