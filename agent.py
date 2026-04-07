import openai

openai.api_key = "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"   # paste your key here

def ask_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']