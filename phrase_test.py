import spacy
from spacy.matcher import PhraseMatcher
#  Load spaCy
nlp = spacy.load("en_core_web_sm")
# Define SKILLS
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

# Create PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)

# Create patterns
patterns = [nlp.make_doc(skill) for skill in SKILLS]

# Add patterns
matcher.add("SKILL",patterns)

def extract_skills(text):
    detected_skills=[]
    # Create doc from text
    doc = nlp(text)
    
    # Run matcher
    matches = matcher(doc)
    
    # Loop through matches
    
    for match_id, start, end in matches:
        
        # Convert each match into span.text
        span = doc[start:end]
        
        # Add it to detected_skills
        detected_skills.append(span.text)
        
        # Return detected_skills
        return detected_skills
    
    if __name__ == "__main__":
        sample_text = """
    I have experience with Python, Django,
    Machine Learning and GitHub.
    """

        print(extract_skills(sample_text))
    
    
