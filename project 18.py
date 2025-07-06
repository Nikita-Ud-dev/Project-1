def correct_sentence(text: str):
    if not text.endswith("."):
        text += "."
    return text[0].upper() + text[1:]


print(correct_sentence("greetings, friends"))
print(correct_sentence("hello"))
print(correct_sentence("Greetings. Friends"))
print(correct_sentence("Greetings, friends."))
print(correct_sentence("greetings, friends."))