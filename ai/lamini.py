from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="MBZUAI/LaMini-Flan-T5-248M"
)

def ask_lamini(prompt):
    response = generator(prompt, max_length=200)
    return response[0]["generated_text"]