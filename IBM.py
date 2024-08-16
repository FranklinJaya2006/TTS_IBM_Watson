import speech_recognition  as srec
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound
import os
import  openai
import time


openai.api_key='Bayar coeg'

api_key = 'Masukkan Api Key dari website IBM Watsons setelah membuat akun'
url = 'Dibawah API Key ada url isi disini'

authenticator = IAMAuthenticator(api_key)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)           
            

def speak_text(text):
        try:
            audio_file_path = 'bicara.mp3'
            with open(audio_file_path, 'wb') as audio_file:
                response = tts.synthesize(
                    text=text,
                    voice='en-US_EmmaExpressive',  # Ganti dengan nama model suara yang valid
                    accept='audio/mp3'
                ).get_result()
                audio_file.write(response.content)
            print("Audio berhasil disimpan")
            os.system('afplay bicara.mp3')
            # Memutar file audio setelah disimpan
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
    
    
def dengar() :
    tangkap = srec.Recognizer() #mengenali audio

    with srec.Microphone() as source : #microphone
        print("Mendengarkan..........")
        
        audio = tangkap.listen(source,phrase_time_limit=5) #phrase_time_limit berapa lama didengar #listen mendengar
        
        try :
            print("Mengerti..............")
            text=tangkap.recognize_google(audio,language='en-EN')
            speak_text(text)
            return text
        except srec.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            return None
    
running = True

while running :
    speak_text("Hi, im Ganyu how can i assist you today ? ")
    user_input = dengar()
    if user_input is None :
        speak_text("So, you want to continue ? (yes/no)")
        user_input = dengar()
        if user_input == "no" :
            speak_text("Okay, close")
            running = False
            time.sleep(5)
            break
        elif user_input == "no, thanks" :
            speak_text("Okay, close")
            running = False
            time.sleep(5)
            break
        else :
            speak_text("Continue")
            continue
    elif user_input == "close" :
        print("User wants to stop")
        speak_text("Thank you")
        running = False
        time.sleep(5)
    else :
        user_input
        time.sleep(2)
    