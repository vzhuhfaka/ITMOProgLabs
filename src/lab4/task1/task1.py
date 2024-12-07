from src.lab4.utils import read_lines_split_comma as read_lines


def count_common_films(user_history, common_films_):
    return (len(common_films_) / len(user_history)).__round__(1)


def get_common_elements(array1, array2):
    common_els = []
    for i in array1:
        for j in array2:
            if i == j:
                common_els.append(i)
    return common_els


def diff_arrays(array1, array2):
    if len(array2) > len(array1):
        array1, array2 = array2, array1

    diff_array = []
    for i in array1:
        for j in array2:
            if i not in array2 and i != j and diff_array.count(i) < array1.count(i):
                diff_array.append(i)

    return diff_array


class OnlineCinema:
    def __init__(self, history_all_users, user_history):
        self.history_all_users = history_all_users
        self.user_history = user_history

    def recommend_film(self):
        user_history = self.user_history
        dict_with_recommended_films = {}

        # Перебираем историю всех пользователей
        for other_user_history in self.history_all_users:
            common_films = get_common_elements(user_history, other_user_history)

            if len(common_films) >= len(user_history) / 2:

                # Убираем фильмы, которые пользователь уже посмотрел
                not_viewed_films = diff_arrays(other_user_history, common_films)

                # Считаем вес рекомендаций в зависимости от количества общих фильмов
                weight = count_common_films(other_user_history, common_films)

                # Считаем количество просмотренных фильмов другими людьми
                for i in not_viewed_films:
                    if i in dict_with_recommended_films:
                        dict_with_recommended_films[i] += weight
                    else:
                        dict_with_recommended_films[i] = weight

        # Сортируем словарь по количеству просмотренных фильмов
        sorted_rec_dict = sorted(dict_with_recommended_films.items(), key=lambda item: item[1], reverse=True)

        # Возвращаем первый фильм с наибольшим количеством просмотров
        return sorted_rec_dict[0][0]


class User:
    def __init__(self, user_history, list_of_all_movie, online_cinema):
        self.user_history = user_history
        self.list_of_all_movie = list_of_all_movie
        self.online_cinema = online_cinema

    def choose_rec_movie(self):
        return self.online_cinema.recommend_film()


if __name__ == '__main__':
    # Входные данные
    history_all_users_ = read_lines('history.txt')
    list_all_movie_ = read_lines('movies.txt')
    user_history_ = input().split(',')
    dict_all_movie = dict(list_all_movie_)

    online_cinema_ = OnlineCinema(history_all_users_, user_history_)
    user = User(user_history_, list_all_movie_, online_cinema_)

    number_of_rec_movie = user.choose_rec_movie()
    recommended_movie = dict_all_movie[number_of_rec_movie]
    print(recommended_movie)
