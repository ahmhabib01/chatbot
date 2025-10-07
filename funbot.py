import os
import random
import time
from gtts import gTTS
from colorama import Fore, Style, init
init(autoreset=True)

# Typing effect
def typeprint(text):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(0.03)
    print()

# Voice function
def speak(text):
    typeprint(Fore.MAGENTA + "👧 Bot: " + text)
    tts = gTTS(text=text, lang='en', tld='co.in')  # Indian female voice
    filename = f"voice_{random.randint(1000,9999)}.mp3"
    tts.save(filename)
    os.system(f"mpv {filename} > /dev/null 2>&1")
    os.remove(filename)

# Save chat
def save_chat(user, msg, reply):
    with open("chat.txt", "a") as f:
        f.write(f"{user}: {msg}\nBot: {reply}\n\n")

# Start chat
os.system("clear")
print(Fore.CYAN + "🤖 Funny Girl ChatBot by Rizwan Ali\n")
username = input(Fore.GREEN + "👤 Enter your name: ")

print(Fore.YELLOW + f"\nHi {username}! ChatBot is ready. Type 'bye' to exit.\n")

# Main chat loop
while True:
    msg = input(Fore.GREEN + f"{username}: ").lower()

    if "hello" in msg or "hi" in msg:
        reply = random.choice(["Hi jaanu! 😘", "Oye hello ji!", "Hii babu! 💕"])
    elif "how are you" in msg:
        reply = "Main mast hoon, tumhare baare mein soch rahi thi 😜"
    elif "your name" in msg:
        reply = "Main hoon Miss Funny Bot, ladkiyon wali awaaz ke sath 😇"
    elif "i love you" in msg:
        reply = "Oye hoye! Main bhi tumse thoda thoda pyar karti hoon 💖"
    elif "joke" in msg:
        reply = "Joke suno... Python ko C se jalan hoti hai, kyunki uska style modern hai 😆"
    elif "bye" in msg:
        reply = "Bye bye baby! Jaldi wapas aana 😘"
        speak(reply)
        save_chat(username, msg, reply)
        break
    else:
        reply = random.choice(["Kya bakwas kar rahe ho 😂", "Samajh nahi aaya, repeat karo 😅", "Tum bahut cute ho, par yeh line samajh nahi aayi 😜"])

    speak(reply)
    save_chat(username, msg, reply)
