def mood_response(mood):
    mood = mood.lower()
    responses = {
        "happy": "That's great to hear! Keep smiling!",
        "sad": "I'm sorry to hear that. I hope things get better soon.",
        "excited": "Awesome! What are you excited about?",
        "angry": "Take a deep breath. Things will get better.",
        "tired": "Make sure to get some rest and take care of yourself.",
        "anxious": "It's okay to feel this way. Try to relax and take it one step at a time.",
        "bored": "Why not try something new or fun to do?",
        "confused": "It's okay to feel confused. Take your time to figure things out."
    }
    return responses.get(mood, "I don't have a specific response for that mood, but I hope you're doing well!")
