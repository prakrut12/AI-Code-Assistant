import streamlit as st


def ask_ai(prompt):
    prompt = prompt.lower()

    if "factorial" in prompt:
        return """def factorial(n):
    return 1 if n==0 else n*factorial(n-1)"""

    elif "fibonacci" in prompt:
        return """def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b"""

    elif "prime" in prompt:
        return """def is_prime(n):
    return all(n%i for i in range(2,n))"""

    elif "sum" in prompt and "natural" in prompt:
        return """def sum_n(n):
    return n * (n + 1) // 2"""

    else:
        return "Currently supports: factorial, fibonacci, prime, sum of natural numbers."

# UI
st.title("🤖 Agentic Coding Assistant")

problem = st.text_input("Enter your coding problem:")

if st.button("Generate Code"):
    if problem:
        st.write("⏳ Generating solution...")
        answer = ask_ai(problem)

        st.subheader("💻 Generated Code:")
        st.code(answer, language="python")

        improve = st.text_input("Improve / Debug this code:")

        if st.button("Improve Code"):
            improved = "✨ Optimized version of above code"
            st.subheader("✨ Improved Code:")
            st.code(improved, language="python")