from rag import autonomous_agent
# from rag import decide_tool, calculator , search_pdf , code , email_writer     # generate_answer

print("Intelligent AI Agent (type 'exit' to quit)\n")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    response = autonomous_agent(query)

    print("\nAI:", response)

