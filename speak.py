from gtts import gTTS
import pygame
import os

def speak_text(text):
    """Convert Tamil text to speech and play it"""
    try:
        # Save the audio file to a safe path
        file_path = "tamil_reply.mp3"
        tts = gTTS(text=text, lang='ta')
        tts.save(file_path)

        # Play the saved file
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass

        # Optionally remove the file after playback
        os.remove(file_path)

    except Exception as e:
        print("❌ Speech error:", e)
