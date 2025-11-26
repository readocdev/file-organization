from organizer import FileOranizer
from config import CATEGORIES
import pyfiglet
from colorama import Fore, init
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

init(autoreset=True)
console = Console()

def main():
    create_banner()

    while True:
        print_menu()
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            path_input = input("Введите путь к папке: ").strip()
            folder_path = Path(path_input)

            if not folder_path.exists() or not folder_path.is_dir():
                print(Fore.RED + "Путь некорректен. Попробуйте снова.")
                continue
            
            organizer = FileOranizer(folder_path, CATEGORIES)
            organizer.organize()
            print(Fore.GREEN + "Организация файлов завершена!")
        
        elif choice == "2":
            print(Fore.CYAN + "Выход из программы...")
            break

        else:
            print(Fore.RED + "Неверный выбор. Попробуйте снова.")


def create_banner():
    banner = pyfiglet.figlet_format("readocdev")
    print(Fore.GREEN + banner)

def print_menu():
    console = Console()
    console.print(Panel.fit("[1] Организовать файлы\n[2] Выйти", title="МЕНЮ", style="cyan"))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        print("Произошла ошибка: \n")
        traceback.print_exc()
