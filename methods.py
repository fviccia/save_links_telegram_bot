import sqlite3


def database_insert(link_id, link, title, tags):
    # Connect to database
    conn = sqlite3.connect("links.sqlite")
    query = (
        "INSERT INTO links (link_id,link,title,tags) "
        "VALUES (:link_id, :link, :title, :tags);"
    )
    params = {"link_id": link_id, "link": link, "title": title, "tags": tags}
    conn.execute(query, params)
    conn.commit()
    # Close connection
    conn.close()
    return


def database_read():
    # Connect to database
    conn = sqlite3.connect("links.sqlite")
    cursor = conn.execute("SELECT * from links")
    data = cursor.fetchall()
    # Close connection
    conn.close()
    return data


# TODO: Take update parameters as input
def database_update():
    # Connect to database
    conn = sqlite3.connect("links.sqlite")
    # Update database
    conn.execute("UPDATE links set ROLL = 005 where ID = 1")
    conn.commit()
    # Close connection
    conn.close()
    return


def database_delete(link_id):
    """
    Delete a link by link_id
    :param link_id: link_id attribute of the link
    :return:
    """
    # Connect to database
    conn = sqlite3.connect("links.sqlite")
    conn.execute("DELETE FROM links WHERE link_id = ?;", (link_id,))
    conn.commit()
    # Close connection
    conn.close()
    return


if __name__ == "__main__":
    database_insert(0, "text", "text", "text")
    # insert(1, "text", "text", "text")
    # insert(43, "text", "text", "text")
    # print(read())
    # delete(43)
    print(database_read())
