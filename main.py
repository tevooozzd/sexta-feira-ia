import speech_recognition as sr
import time
import os
from second import SextaFeira






class SextaFeiraStart():

    def __init__(self, activate):
        self.limparw = os.system('cls')
        self.recog = sr.Recognizer()
        self.activate = activate

    def system(self):
        with sr.Microphone() as microphone:
            print("SISTEMA: Sistema ligando... Aguarde para iniciar a ativação!")
            self.recog.adjust_for_ambient_noise(microphone)
            print("SISTEMA: Sistema pronto e preparado para ativação!")
            time.sleep(1.5)
            while True:
                print("Ouvindo...")
                audio = self.recog.listen(microphone)
                try:
                    texto = self.recog.recognize_google(audio, language='pt-BR')
                    if any(word in texto.lower() for word in self.activate):
                        sexta = SextaFeira(timeout_limit=30, texto=texto.lower())
                        sexta.start_message()
                        break
                    else:
                        print(f"Você disse '{texto}' , pelo visto não está falando comigo! Ops, estou me entrometendo...")
                except sr.UnknownValueError:
                    print("Não entendi o que você disse. Tente novamente em 2 segundos!")
                    time.sleep(2)
                except sr.RequestError as e:
                    print(f"Erro no serviço de reconhecimento: {e}")
                    break


if __name__ == '__main__':
    activate = ['sexta', 'sexta-feira', 'cesta', 'sesta']
    start = SextaFeiraStart(activate=activate)
    start.system()





