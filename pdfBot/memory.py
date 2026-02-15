history = []


def update_memory(question, answer):
    global history

    history.append(f"User: {question}")
    history.append(f"AI: {answer}")


def get_history():
    return "\n".join(history)
