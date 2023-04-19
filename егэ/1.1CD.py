import random
import datetime

# Список из возможных названий песен
song_names = ["Синий иней", "До свидания, мама", "Ночной каприз", "Синее платье", "Мой адрес - Советский Союз"]

# Генерируем случайную песню
random_song_name = random.choice(song_names)
random_song_minutes = random.randint(1, 5)
random_song_seconds = random.randint(0, 59)

# Переводим время из минут и секунд в формат времени
song_time = datetime.time(0, random_song_minutes, random_song_seconds)

# Выводим результат
print("Случайная песня: {}".format(random_song_name))
print("Длительность: {}".format(song_time.strftime("%M:%S")))