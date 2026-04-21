from pynput import keyboard
from keyDict import ruDict
import time

# Глобальные переменные для обмена данными
char = ""
ruSymbol = ""
ru = ""
source = "qwqwwqw"
final_string = ""

"""
def getKey(key):
    global char
    
    # Просто записываем символ нажатой клавиши
    if hasattr(key, 'char') and key.char is not None:
                char = key.char
    return char

                # Запуск прослушивания в фоновом потоке
listener = keyboard.Listener(on_press=getKey)
listener.start()
"""

def ruSerch(char):
    global ru
    ru = ruDict.get(char, char)
    return ru

for c in source:
        translated = ruSerch(c)
        final_string += translated

print(f"pressed: {source} in {final_string}")

"""
while True:
    if char != "":
        #ru = ruSerch(char)
        print(f"Pressed: {char} in {ru}")                                                    
        # ОЧИЩАЕМ переменную, чтобы цикл дождался следующего нажатия
        char = ""
    time.sleep(0.010)
"""

