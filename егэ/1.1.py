# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
# Первый трек
# Разбиваем строку на массив (list) по запятым
songs_list = my_favorite_songs.split(', ')

# Первый трек
print(songs_list[0])

# Последний трек
print(songs_list[-1])

# Второй трек
print(songs_list[1])

# Второй с конца трек
print(songs_list[-2])
