from config import LEAGUES


def find_match(player, queue):

    player_league = player.league

    for opponent in queue:

        if opponent.league == player_league:

            return opponent

    current_index = LEAGUES.index(
        player_league
    )

    near_leagues = []

    if current_index > 0:

        near_leagues.append(
            LEAGUES[current_index - 1]
        )

    if current_index < len(LEAGUES) - 1:

        near_leagues.append(
            LEAGUES[current_index + 1]
        )

    for opponent in queue:

        if opponent.league in near_leagues:

            return opponent

    return None
