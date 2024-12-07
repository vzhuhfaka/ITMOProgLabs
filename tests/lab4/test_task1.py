import unittest
from src.lab4.task1.task1 import OnlineCinema, User

class TestOnlineCinema(unittest.TestCase):
    def test_should_recommend_movie(self):
        history_all_users_ = [[1, 2, 3, 6, 7, 3, 3], [2, 4, 3, 5, 6], [5, 7, 1, 5], [1, 3, 2, 2, 2]]
        list_all_movie_ = {1: 'Avengers: Endgame', 2: 'Avengers: Infinity War', 3: 'Avengers: Age of Ultron', 4: 'Iron Man', 5: 'Captain America: Civil War', 7: 'Captain America: The Winter Soldier'}
        user_history_ = [1, 4, 5, 5]

        online_cinema_ = OnlineCinema(history_all_users_, user_history_)
        user = User(user_history_, list_all_movie_, online_cinema_)

        number_of_rec_movie = user.choose_rec_movie()
        recommended_movie = list_all_movie_[number_of_rec_movie]

        self.assertEqual(recommended_movie, 'Avengers: Infinity War')

