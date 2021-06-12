import sqlite3


def main():
    conn = sqlite3.connect("links.sqlite")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS links")
    cur.execute("CREATE TABLE links (link_id INT, link TEXT, title TEXT, tags TEXT) ")
    conn.close()


if __name__ == "__main__":
    main()
