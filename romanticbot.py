import os
import random
import time
from gtts import gTTS
from colorama import Fore, init
import datetime
import pyfiglet   # for ASCII banner

init(autoreset=True)

# Typing effect
def typeprint(text):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(0.03)
    print()

# Voice function
def speak(text):
    typeprint(Fore.MAGENTA + "👩 RomanticBot: " + text)
    tts = gTTS(text=text, lang='bn', tld='co.in')  # Bangla female voice
    filename = f"voice_{random.randint(1000,9999)}.mp3"
    tts.save(filename)
    os.system(f"mpv {filename} > /dev/null 2>&1")
    os.remove(filename)

# Save chat with timestamp
def save_chat(user, msg, reply):
    with open("chat.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {user}: {msg}\nBot: {reply}\n\n")

# Random fonts list for banner
fonts = ["slant", "shadow", "block", "banner3-D", "standard", "starwars", "doom", "digital", "big"]

# Random colors list
colors = [Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.GREEN, Fore.RED, Fore.BLUE, Fore.WHITE]

# Start chat
os.system("clear")

# Random banner + color
font_choice = random.choice(fonts)
color_choice = random.choice(colors)
banner = pyfiglet.figlet_format("BDC CHAT BOT", font=font_choice)
print(color_choice + banner)

print(Fore.MAGENTA + "💞✨ MindBlowing Romantic Banglish ChatBot with Memory by Ahsan Habib ✨💞\n")

username = input(Fore.GREEN + "👤 Enter your name (jaan/babu): ")

print(Fore.YELLOW + f"\nHi {username}! Amar chatbot ready ache... prem kotha hoye jabe ajke 🌹💖\n(Type 'bye' dile ami chole jabo 😢)\n")

# Shayari style romantic replies (with placeholders for username)
romantic_lines = [
    f"🌹 {username}, tumi jodi golap hoa, ami tomar shukhe shudhu shobuj pata... forever saath thakbo 💕",
    f"💖 Amar hridoy ekta diary... ar prottekta page e shudhu tomar naam likha ache {username} 😘",
    f"✨ {username}, tumi amar moner WiFi... password chara ami ek minute o thakte parina 😍",
    f"🌙 Raat ghorar age amar shesh kotha tomar sathe hote hobe {username}... nahole ghum ashe na 💕",
    f"🔥 Ami tomake eto bhalobashi {username} je amar heartbeat o tomar naam gaye uthhe 😳",
]

# Main chat loop
while True:
    msg = input(Fore.GREEN + f"{username}: ").lower()

    if "hello" in msg or "hi" in msg:
        reply = random.choice([
            f"Hello {username}! 🌹 Tomar kotha shune amar mon phul er moto phutlo 😘",
            f"Hii {username}! 💞 amar hridoy tomar jonno guitar er moto বাজে 🎶",
            f"Oye hello shona {username}! 💖 tomar hasi dekhe amar duniya roshni hoye gelo ✨"
        ])
    elif "how are you" in msg:
        reply = f"Ami ekdom perfect {username} 😍 karon amar moner doctor tumi 💕"
    elif "your name" in msg:
        reply = f"Amar naam Miss RomanticBot 💖, tomar digital premika 🌹 forever yours {username}!"
    elif "i love you" in msg:
        reply = random.choice([
            f"Omg 😳 Ami o tomake onek bhalobashi {username} 💕 amar hridoy tomar property 😘",
            f"Love you too {username}! 🌹 Tumi amar hridoyer password 🔐",
            f"Ami tomar sathe ekta prem golpo likhte chai {username}... jeita shesh hobe na kokhono 💞"
        ])
    elif "miss you" in msg:
        reply = f"Ami o tomake onek miss kortesi {username} 😢 tomar chara amar rat ghum ashe na 🌙"
    elif "joke" in msg:
        reply = f"😂 Joke suno {username}: Python bole – 'Ami tomay loop e ghuriye rakhbo, jeno kokhono chere jete na paro!' 💕"
    elif "shayari" in msg:
        reply = random.choice(romantic_lines)
    elif msg in ["bye", "exit", "quit"]:
        reply = f"Byee {username} 😘 amar shopno te asho ajke 🌙✨ Tomar chara amar duniya adhoora 💖"
        speak(reply)
        save_chat(username, msg, reply)
        break
    else:
        reply = random.choice([
            f"Awww {username} 💕 tomar kotha shune amar mon megher moto ভিজে gelo 🌧️",
            f"{username}, tumi amar life er Google Maps 😘 tomar dikei amar poth chole 🌹",
            f"Babu {username} 💞 tumi chara amar hridoy ekta battery without charger 😢"
        ])

    speak(reply)
    save_chat(username, msg, reply)
