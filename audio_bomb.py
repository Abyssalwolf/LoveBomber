import simpleaudio as sa
import threading
import os

def play_audio(file_path):
    try:
        wave_obj = sa.WaveObject.from_wave_file(file_path)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    except Exception as e:
        print(f"Error playing audio: {e}")

def play_audio_in_thread(file_path):
    thread = threading.Thread(target=play_audio, args=(file_path,))
    thread.start()

# Paths to audio files
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
titanic_theme_path = os.path.join(ASSETS_DIR, "titanic_theme.wav")
ai_voice_love_path = os.path.join(ASSETS_DIR, "ai_voice_love.wav")
error_sound_path = os.path.join(ASSETS_DIR, "error_sound.wav")
lb_sound_path = os.path.join(ASSETS_DIR, "love_bomber.wav")

# Play all sounds
play_audio_in_thread(titanic_theme_path)
play_audio_in_thread(ai_voice_love_path)
play_audio_in_thread(lb_sound_path)