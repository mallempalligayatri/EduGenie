from ai.gemini import ask_gemini



def answer_question(question):
    return ask_gemini(question)


def explain_concept(topic):
    prompt = f"""
    Explain the following concept in simple language with examples.

    Topic:
    {topic}
    """

    return ask_gemini(prompt)


def generate_quiz(topic):
    prompt = f"""
    Generate 5 multiple choice questions on:

    {topic}

    Each question should contain:

    A)
    B)
    C)
    D)

    Mention the correct answer.
    """

    return ask_gemini(prompt)


def summarize_text(text):
    prompt = f"""
    Summarize the following text in simple bullet points.

    {text}
    """

    return ask_gemini(prompt)

    return ask_lamini(prompt)


def learning_recommendation(topic):
    prompt = f"""
    Recommend a learning roadmap for

    {topic}

    Include:

    1. Prerequisites
    2. Topics to Learn
    3. Resources
    4. Practice Ideas
    """

    return ask_gemini(prompt)