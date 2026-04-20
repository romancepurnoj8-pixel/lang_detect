from pynput import keyboard
from keyDict import ruDict
import time

# Глобальные переменные для обмена данными
char = ""

def getKey(key):
    global char
    
    # Просто записываем символ нажатой клавиши
    if hasattr(key, 'char') and key.char is not None:
                char = key.char
    return char

                # Запуск прослушивания в фоновом потоке
listener = keyboard.Listener(on_press=getKey)
listener.start()

def press(char):
     # Поиск в словаре (возвращает сам символ, если ключа нет)
    return ruDict.get(char, char)

while True:
    if char != "":
        ru = press(char)
        print(f"Pressed: {char} in {ru}")                                                    
        # ОЧИЩАЕМ переменную, чтобы цикл дождался следующего нажатия
        char = ""
    time.sleep(0.01)
