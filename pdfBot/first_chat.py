from pdfBot.rag import generate_answer
from pdfBot.memory import update_memory, get_history


print("AI PDF Chatbot (type 'exit' to quit)\n")

while True:
    query = input("You: ")

    if query.lower() == ["exit","quit"]:
        break

    history = get_history()

    answer, sources = generate_answer(query, history)

    print("\nAI:", answer)
    print("\nSources:\n", sources)

    update_memory(query, answer)
