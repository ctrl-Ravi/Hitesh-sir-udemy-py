"""
 Challenge: Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
  I love to code and drink tea when I'm happy.

Output:
  I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)

"""




# get a dictionary 
emoji_map_fun ={
    "love": "💖",
    "happy": "😀",
    "code": "👩‍💻",
    "tea": "☕",
    "music": "🎶",
    "food": "🍕",
    "videos": "🎥"
}

# Get user message
Message= input("Enter Your Message: ")

updated_words =[]

# proccess each word
for word in Message.split():
    cleaned = word.lower().strip(".,!?") # strip by default remove white spaces but if you provide character its remove that characters
    emoji = emoji_map_fun.get(cleaned, "") #Return the value for key if key is in the dictionary, else default.
    if emoji:
        updated_words.append(f"{word}{emoji}")
        # updated_words.append(f"{emoji}") # its replace word with emoji
    else:
        updated_words.append(word)

updated_message= " ".join(updated_words)
print("\n Enhanced Message: ")
print(updated_message)