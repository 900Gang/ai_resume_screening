import spacy
from spacy.matcher import PhraseMatcher
#  Load spaCy
nlp = spacy.load("en_core_web_sm")
# Define SKILLS
SKILLS = {
    "python": "Python",
    "sql": "SQL",
    "html": "HTML",
    "css": "CSS",
    "javascript": "JavaScript",
    "django": "Django",
    "flask": "Flask",
    "postgresql": "PostgreSQL",
    "docker": "Docker",
    "git": "Git",
    "github": "GitHub",
    "firebase": "Firebase",
    "linux": "Linux",
    "jenkins": "Jenkins",
    "machine learning": "Machine Learning",
    "data science": "Data Science",
    "natural language processing": "Natural Language Processing"
}

# Create PhraseMatcher
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

# creatng matchid
# skill_keys = list(SKILLS.keys())

# Create patterns
patterns = [nlp.make_doc(skill) for skill in SKILLS]
# Add patterns
matcher.add("SKILL",patterns)

def extract_skills(text):
    detected_skills = set()

    doc = nlp(text)

    matches = matcher(doc)

    for match_id, start, end in matches:
        span = doc[start:end]
        skill_key = span.text.lower()
        canonical_skill = SKILLS[skill_key]
        detected_skills.add(canonical_skill)

    return list(detected_skills)


    
if __name__ == "__main__":
        sample_text = """
    I have experience with Python, Django,
    Machine Learning and GitHub.
    """

        print(extract_skills(sample_text))
    
    
