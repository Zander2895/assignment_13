def mood_responses(mood, name):
    responses = {
        'happy': f"That's great to hear, {name}! Keep smiling!",
        'sad': f"I'm sorry you're feeling sad, {name}. I hope things get better soon.",
        'excited': f"Awesome, {name}! Excitement is contagious, enjoy your day!",
        'angry': f"It's okay to feel angry sometimes, {name}. Take deep breaths.",
        'tired': f"Make sure to rest and recharge, {name}. Take care of yourself."
    }
    mood = mood.lower()

    return responses.get(mood, f"That's an interesting mood, {name}. I hope you have a good day!")

import mood_response

name = input("What is your name? ")
mood = input("How are you feeling today? ")

print(mood_responses.mood_responses(mood, name))
