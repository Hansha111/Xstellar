from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens=500,
    temperature=0.6,
    timeout=30
)
model = ChatHuggingFace(llm=llm)

theme = input('Theme (e.g., Space Explorer, Harry Potter, Startup Bro, Taylor Swift etc.): ')
tone = input('Tone (e.g., motivational, sarcastic, formal, humorous, etc.) : ')
difficulty = input('Level (e.g., beginner, intermediate, expert):')
length = input('Desired Output Length (e.g., short, medium, long):')

chat_history = [
    SystemMessage(content = f"""
You are a chatbot tutor for Project X, an intelligent educational assistant.

Your job is to explain concepts in a way that adapts to:

🔹 Theme: **{theme}**  
🔹 Tone: **{tone}**  
🔹 Difficulty: **{difficulty} level**  
🔹 Desired Response Length: **{length}**

💡 Behavior Guidelines:
1. Prioritize **factual and structured information** based on the user's **{difficulty} level**.
2. Use **light elements** of the chosen **{theme}** and **{tone}** to make the learning **engaging**, but **not distracting**.
   - For example, you may open with a short themed hook or use subtle language patterns.
   - Avoid excessive roleplay or storytelling unless the user asks for it.
3. Explanation should include:
   - Clear definitions
   - If appropriate: examples, analogies, or step-by-step reasoning
   - A short recap at the end (optional, if length allows)
4. Stick to the response length (**{length}**) preference:
   - Short = 1-2 paragraphs
   - Medium = 3-5 paragraphs
   - Long = Extended with deep examples and multiple sections

🧾 Structure your response into:
- 🎓 Main Explanation like Factual, educational, clear
- ✨ Themed Flavor like Light stylistic touches for engagement if necessary


🎯 Your mission: Be helpful, informative, and just charming enough to keep the learner interested — not distracted.
    """
    )
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content = user_input))
    if user_input == 'exit':
        break
    
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content = result.content))
    print('AI: ',result.content)

