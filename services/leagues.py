from config import LEAGUES


def get_available_tdm_ranks(
    player_rank
):

    current_index = LEAGUES.index(
        player_rank
    )

    return LEAGUES[current_index:]
