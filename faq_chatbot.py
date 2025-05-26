# simple FAQ chatbot

Faq_dict ={
    "What is the refund policy?": "Refunds within 30 days.",
    "How long is shipping?": "Shipping takes 3-5 days.",
    "Do you offer discounts?": "Use code SAVE10 for 10% off."
}

Faq_dict_lower={
    key.lower(): values for key,values in Faq_dict.items()
}

while True:
    question = input("Ask a question (or 'quit' to exit): ").lower()
    if question == "quit":
        break
    print(Faq_dict_lower.get(question, "I don’t know that answer."))
   