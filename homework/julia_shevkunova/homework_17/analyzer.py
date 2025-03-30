import os
import argparse


def search_text_in_files(directory, search_text):
    if not os.path.isdir(directory):
        print("Ошибка: Указанная папка не существует!")
        return
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r') as file:
                    for line_number, line in enumerate(file, start=1):
                        if search_text in line:
                            words = line.strip().split()
                            index = words.index(search_text) if search_text in words else -1
                            before = " ".join(words[max(0, index - 5):index]) if index > 0 else ""
                            after = " ".join(words[index + 1:index + 6]) if index >= 0 else ""

                            print(f"Файл: {filename}, строка {line_number}: ... {before} {search_text} {after} ...")
            except Exception as e:
                print(f"Ошибка при чтении файла {filename}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", "-d", help="Полный путь к папке с файлами")
    parser.add_argument("--text", "-t", help="Текст, который нужно найти")

    args = parser.parse_args()
    search_text_in_files(args.directory, args.text)
