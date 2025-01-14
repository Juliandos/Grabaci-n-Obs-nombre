import speech_recognition as sr
from googletrans import Translator

def transcribe_audio():
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    translator = Translator()

    print("Calibrando micrófono...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
    print("Calibración completa. Iniciando transcripción...")

    try:
        while True:
            with mic as source:
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=20)

            try:
                text_en = recognizer.recognize_google(audio, language="en-EN")
                print(f"Inglés: {text_en}")

                translation = translator.translate(text_en, src="en", dest="es")
                print(f"Traducción al español: {translation.text}\n")

            except sr.UnknownValueError:
                print("No se pudo entender el audio.")
            except sr.RequestError as e:
                print(f"Error del servicio de reconocimiento: {e}")
    except KeyboardInterrupt:
        print("\nTranscripción finalizada.")

if __name__ == "__main__":
    transcribe_audio()
