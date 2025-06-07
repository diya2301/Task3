# chatbot.py

import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses
pairs = [
    [r"hi|hello|hey|hy", ["Hello!", "Hi there!", "Hey!"]],
    [r"how are you?", ["I'm good, thank you!", "Doing great. How can I help you?"]],
    [r"what is your name?", ["I'm Diya's AI Chatbot.", "You can call me diya."]],
    [r"what do you do?", ["I'm here to answer your questions.", "I assist users using NLP."]],
    [r"who created you?", ["I was created by a CodTech Intern using Python and NLTK."]],
    [r"bye|exit|quit|by", ["Goodbye!", "See you next time!", "Have a nice day!"]],
    [r"(.*)", ["I'm not sure I understand. Could you please rephrase?", "Sorry, I didn't get that."]]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("Hi! I am CodTech's AI Chatbot. Type 'bye' to exit.")
chatbot.converse()
