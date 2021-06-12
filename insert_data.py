import sqlite3


def main():
    conn = sqlite3.connect("links.sqlite")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO links (link_id, link, title, tags) VALUES (?,?,?,?)",
        (1, "Ahmed", "Ahmed", "Instructor"),
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
