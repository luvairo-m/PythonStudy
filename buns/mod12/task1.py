import sqlite3


def get_all_actors():
    query = """SELECT show_id, netflix_titles.cast 
                FROM netflix_titles
                WHERE netflix_titles.cast != ''"""

    output = dict()

    for cast in cursor.execute(query):
        show_id = int(cast[0])
        cast = str(cast[1]).split(', ')

        for actor in cast:
            if actor not in output:
                output[actor] = set()

            output[actor].add(show_id)

    return output


def create_actors_table():
    return """
            CREATE TABLE IF NOT EXISTS actors 
            (
                actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                actor_name TEXT UNIQUE NOT NULL
            );
            """


def create_actor_title_table():
    return """
            CREATE TABLE IF NOT EXISTS actor_title 
            (
                actor_id INTEGER NOT NULL,
                title_id INTEGER NOT NULL,
                PRIMARY KEY (actor_id, title_id),
                FOREIGN KEY (actor_id) REFERENCES actors (actor_id),
                FOREIGN KEY (title_id) REFERENCES netflix_titles (show_id)
            );
            """


def add_actor():
    return """
           INSERT INTO actors (actor_name)
           VALUES (?);
           """


def add_actor_title():
    return """
           INSERT INTO actor_title (actor_id, title_id)
           VALUES (?, ?);
           """


def actors_pair():
    return """
           WITH temp AS (
                SELECT 
                   actor_id AS actor1, 
                   title_id AS title1
                FROM actor_title 
                GROUP BY 1, 2
           )
           SELECT 
                (SELECT actor_name FROM actors WHERE actor_id = actor1) AS "1-st actor", 
                (SELECT actor_name FROM actors WHERE actor_id = actor2) AS "2-nd actor", 
                times_worked_together AS "Shared films"
           FROM (
           SELECT
               u1.actor1 AS actor1,
               u2.actor1 AS actor2,
               COUNT(*) AS times_worked_together,
               RANK() OVER (ORDER BY COUNT(*) DESC) Rnk
           FROM temp u1
               JOIN temp u2 ON u1.title1 = u2.title1 AND u1.actor1 < u2.actor1
           GROUP by 1, 2
           ) inner_1
           WHERE Rnk = 1;
           """


if __name__ == "__main__":
    connection = sqlite3.connect('netflix.sqlite')
    cursor = connection.cursor()

    cursor.execute(create_actors_table())
    cursor.execute(create_actor_title_table())

    all_actors = get_all_actors()

    for author_name in all_actors.keys():
        cursor.execute(add_actor(), (author_name,))

    id_counter = 1

    for movies in all_actors.values():
        for movie_id in movies:
            cursor.execute(add_actor_title(), (id_counter, movie_id))

        id_counter += 1

    print(cursor.execute(actors_pair()).fetchall())

    connection.commit()
    connection.close()
