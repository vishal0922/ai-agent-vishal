import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="Yor-Api-Key")

model = genai.GenerativeModel("gemini-2.5-flash")

# Notes generator
def make_notes(topic):
    prompt = f"Make exam-ready notes for: {topic}. Use headings, points, and examples."
    return model.generate_content(prompt).text

# MCQ generator
def make_mcq(topic):
    prompt = f"Generate 10 MCQs with answers for: {topic}"
    return model.generate_content(prompt).text

# Topic explainer
def explain(topic):
    prompt = f"Explain '{topic}' in very simple language with examples."
    return model.generate_content(prompt).text

# Summary maker
def summarize(text):
    prompt = f"Summarize this for exam preparation:\n{text}"
    return model.generate_content(prompt).text

def agent(user):
    u = user.lower()

    # Notes
    if "notes" in u:
        topic = user.replace("notes", "").strip()
        return make_notes(topic)

    # MCQ
    if "mcq" in u:
        topic = user.replace("mcq", "").strip()
        return make_mcq(topic)

    # Summary
    if "summary" in u:
        text = user.replace("summary", "").strip()
        return summarize(text)

    # Explain
    if "explain" in u:
        topic = user.replace("explain", "").strip()
        return explain(topic)

    # Default AI reply
    return model.generate_content(user).text

while True:
    msg = input("\nYou: ")
    if msg.lower() == "exit":
        break
    print("\nAI:", agent(msg))
