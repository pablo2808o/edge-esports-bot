async def get_free_team_number(
    session
):

    used_numbers = []

    result = await session.execute(
        "SELECT team_number FROM edge_teams"
    )

    rows = result.fetchall()

    for row in rows:

        used_numbers.append(row[0])

    for i in range(2, 51):

        if i not in used_numbers:

            return i
