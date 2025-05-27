import json
import os

FAQ_FILE = "faqs.json"

def load_faqs(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

def save_faqs(logs, filename):
    with open(filename, "w") as file:
        json.dump(logs, file, indent=2)

def find_answer(faqs, question):
    question_lower = question.lower()
    for q, a in faqs.items():
        if q.lower() == question_lower:
            return a
    return None

def main():
    
    faq_log = load_faqs(FAQ_FILE)
    print(faq_log)

    while True:
        question = input("Ask a question: ").strip()
        if question.lower() == "quit":
            print("Goodbye!")
            break
        
        answer = find_answer(faq_log, question)

        if answer:
            print("Answer:", answer)
        else:
            print("I don't know that answer.")
            add = input("Would you like to add the answer? (yes/no): ").strip().lower()
            if add == "yes":
                existing_key = None
                for q in faq_log:
                    if q.lower() == question.lower():
                        existing_key = q
                        break

                if existing_key:
                    continue  
                new_answer = input("Please provide the answer: ").strip()
                if new_answer:
                    faq_log[question] = new_answer
                    save_faqs(faq_log, FAQ_FILE)
                    print("Thank you! I've added it to the FAQs.")
                else:
                    print("No answer entered. Not adding.")
            else:
                print("Okay, no problem.")
    
        print("[INFO] Interaction saved to faqs.json")

if __name__ == "__main__":
    main()
