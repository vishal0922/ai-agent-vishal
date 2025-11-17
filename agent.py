import google.generativeai as genai

# Step 1: API Key add karo (main bata dunga kahan se milegi)
genai.configure(api_key="AIzaSyAD4Mq8GwWXdtgiXNKWa9bBZio53-SgWyM")

# Step 2: Model choose karo
model = genai.GenerativeModel("gemini-2.5-flash")

# Step 3: Agent loop
while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    reply = model.generate_content(user)
    print("AI:", reply.text)