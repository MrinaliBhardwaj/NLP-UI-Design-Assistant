import json
import re

print("UX Chatbot Ready!")


with open("corpus.json") as f:
    corpus = json.load(f)

def chatbot(query):
    
    query = re.sub(r'[^a-zA-Z0-9 ]', '', query.lower())

    
    if query in ["hi", "hello", "hey"]:
        return "Hello! Ask me anything about UX Design"

    
    stop_words = ["what", "is", "the", "a", "an", "are", "of"]

    
    keywords = []
    for word in query.split():
        if word not in stop_words and len(word) > 2:
            keywords.append(word)

   
    if len(keywords) == 0:
        return "Please ask a meaningful UX-related question."

    scored_sentences = []

    
    for doc in corpus:
        sentences = doc["content"].split(".")
        
        for sentence in sentences:
            score = 0
            for word in keywords:
                if word in sentence:
                    score += 1
            
            if score > 0:
                scored_sentences.append((score, sentence.strip()))

    
    if len(scored_sentences) == 0:
        return "Sorry, I can only answer questions related to UX Design."

    
    scored_sentences.sort(reverse=True)

   
    best = [s[1] for s in scored_sentences[:3]]

    answer = ". ".join(best)

   
    if "principle" in query:
        intro = "UX design principles focus on improving user experience. "
    elif "usability" in query:
        intro = "Usability refers to how easy and efficient a system is to use. "
    elif "ux" in query or "user experience" in query:
        intro = "User experience (UX) refers to how users interact with a product. "
    else:
        intro = ""

    return intro + answer + "."



while True:
    q = input("\nAsk UX Question: ")
    
    if q.lower() == "exit":
        print("Goodbye!")
        break
    
    print("\nAnswer:\n", chatbot(q))