import pyttsx3
import time

# Function to read lengthy text
def read_long_text(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Set voice and adjust speech rate (speed)
    engine.setProperty('voice', voices[1].id)  # Change this to select the voice
    engine.setProperty('rate', 150)  # Adjust rate to control speech speed

    # Break the text into smaller chunks (you may need to adjust chunk size as needed)
    chunk_size = 500  # Number of characters per chunk
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    # Read each chunk
    for chunk in chunks:
        engine.say(chunk)
        engine.runAndWait()
        time.sleep(0.9)  # Adjust the pause time as needed

if __name__ == "__main__":

    #ENTER YOUR CUSTOM PHARAGRAPH

# ENTER HEAR        
    lengthy_text = """
    
                 Artificial Intelligence (AI) is increasingly prevalent in the software applications we use every day; including digital assistants in our homes and cellphones, automotive technology in the vehicles that take us to work, and smart productivity applications that help us do our jobs when we get there.

So what actually is artificial intelligence?

There are many definitions; some technical, some philosophical; but in general terms, we tend to think of AI as software that exhibits one or more human-like capabilities, as shown in the following table:

    """

    # Read the text
    read_long_text(lengthy_text)

'''import pyttsx3
# Initialize the text-to-speech engine
engine = pyttsx3.init()
# Get the available voices
voices = engine.getProperty('voices')
print("Available Voices:")
for idx, voice in enumerate(voices):
    print(f"Voice {idx}: {voice.name}")'''

'''# Select a voice (replace index with the desired voice index)
# For example, to select the second voice:
selected_voice_index = 1
engine.setProperty('voice', voices[selected_voice_index].id)

# Synthesize speech
engine.say("Hello, world!")
engine.runAndWait()'''
