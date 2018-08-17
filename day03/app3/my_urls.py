from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r"^get_player_v1",get_player_avg_age),
    url(r"^teams$",get_teams),
    url(r"^players$",get_players_by_tid),
    url(r"^getcard$",get_idcard_by_person),
    url(r"getperson$",get_person_by_card),
    url(r"^delete$",delete_person),
    url(r"^deletec$",delete_card),
    url(r"^hehe$",get_player_by_team),
    url(r"^get_author$",get_author_by_book),
    url(r"^get_book$",get_book_by_author),
    # url(r"^language$",get_info),
    url(r"^test$",textpost)
]