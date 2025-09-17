from PIL import ImageGrab, Image, ImageTk
from google import genai
import os
import platform
from dotenv import load_dotenv
import pygame
import tkinter as tk
from elevenlabs.client import ElevenLabs
from elevenlabs import play, save
import time

load_dotenv()
elevenlabs_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

PROMPT = """
You are josh :)'s best friend. You are watching him 
play a game of chess, and you are going to support him
with encouraging words. Don't give advice, just encourage him.
Be positive, and spread the love. Don't be too long winded, 
just a few sentences. Josh was black and just won!

SPECIFICALLY MENTION WHAT YOU SEE IN THE SCREENSHOT.
"""

llm_client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
model = "gemini-2.0-flash-exp"

def call_llm(prompt, screenshot) -> str:
    response = llm_client.models.generate_content(
        model=model,
        contents=[
            prompt,
            {
                "inline_data": {
                    "mime_type": "image/png",
                    "data": screenshot
                }
            }
        ]
    )
    return response.text

def capture_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")

def show_character():
    global character_window, character_image
    
    character = Image.open("pip.png")
    
    character_window = tk.Toplevel()
    character_window.title("Happy Little Robot")
    character_window.overrideredirect(True)
    
    character_window.attributes('-topmost', True)
    character_window.lift()
    character_window.focus_force()
    character_window.attributes('-alpha', 0.9)
    character_window.configure(bg='systemTransparent')

    screen_width = character_window.winfo_screenwidth()
    screen_height = character_window.winfo_screenheight()
    
    img_width, img_height = character.size
    
    padding = 50
    x = screen_width - img_width - padding
    y = screen_height - img_height - padding
    
    character_window.geometry(f"{img_width}x{img_height}+{x}+{y}")
    
    character_image = ImageTk.PhotoImage(character)
    
    label = tk.Label(character_window, image=character_image, bd=0, highlightthickness=0)
    label.pack(fill='both', expand=True)
    
    character_window.bind('<Escape>', lambda e: close_character())
    character_window.focus_set()
    
    character_window.after(100, lambda: character_window.lift())
    character_window.after(100, lambda: character_window.attributes('-topmost', True))

def close_character():
    global character_window
    if 'character_window' in globals() and character_window:
        try:
            character_window.destroy()
            character_window = None
        except tk.TclError:
            character_window = None

def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    show_character()
    
    while pygame.mixer.music.get_busy():
        if character_window and character_window.winfo_exists():
            character_window.update()
            character_window.lift()
            character_window.attributes('-topmost', True)
        pygame.time.wait(100)

    close_character()

def tts(text):
    audio_generator = elevenlabs_client.text_to_speech.convert(
            text=text,
            voice_id="KTPVrSVAEUSJRClDzBw7",
            model_id="eleven_flash_v2",
            output_format="mp3_44100_128",
        )
    save(audio_generator, "response.mp3")
    
    play_audio()

def main():
    # Initialize tkinter root window (hidden)
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    try:
        capture_screenshot()
        screenshot = open("screenshot.png", "rb").read()
        response = call_llm(PROMPT, screenshot)
        print(response)
        tts(response)
    except Exception as e:
        print(f"Error: {e}")
        close_character()
    finally:
        # Clean up and exit
        root.quit()
        root.destroy()

if __name__ == "__main__":
    while True:
        time.sleep(3)
        main()
        time.sleep(30)
