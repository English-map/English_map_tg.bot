from db import get_connection

# --------------------------
# LANGUAGE
# --------------------------

def set_user_lang(user_id: int, lang: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO users (user_id, lang)
    VALUES (?, ?)
    ON CONFLICT(user_id)
    DO UPDATE SET lang = excluded.lang
    """, (user_id, lang))

    conn.commit()
    conn.close()


def get_user_lang(user_id: int) -> str:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT lang FROM users WHERE user_id = ?", (user_id,))
    row = cur.fetchone()
    conn.close()

    return row[0] if row else "en"


# --------------------------
# LEVEL
# --------------------------

def set_user_level(user_id: int, level: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO users (user_id, level)
    VALUES (?, ?)
    ON CONFLICT(user_id)
    DO UPDATE SET level = excluded.level
    """, (user_id, level))

    conn.commit()
    conn.close()


def get_user_level(user_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT level FROM users WHERE user_id = ?", (user_id,))
    row = cur.fetchone()
    conn.close()

    return row[0] if row else None

# --------------------------
# VOCAB (SQLite)
# --------------------------

def add_vocab_word(user_id: int, list_name: str, word: str, meaning: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO vocab_lists (user_id, list_name, word, meaning)
    VALUES (?, ?, ?, ?)
    """, (user_id, list_name, word, meaning))

    conn.commit()
    conn.close()


def get_vocab_lists(user_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT DISTINCT list_name
    FROM vocab_lists
    WHERE user_id = ?
    """, (user_id,))

    rows = cur.fetchall()
    conn.close()

    return [r[0] for r in rows]


def get_vocab_words(user_id: int, list_name: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT id, word, meaning
    FROM vocab_lists
    WHERE user_id = ? AND list_name = ?
    ORDER BY id
    """, (user_id, list_name))

    rows = cur.fetchall()
    conn.close()

    return rows  # [(id, word, meaning)]


def delete_vocab_word(user_id: int, list_name: str, word: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    DELETE FROM vocab_lists
    WHERE user_id = ? AND list_name = ? AND word = ?
    """, (user_id, list_name, word))

    conn.commit()
    conn.close()

def delete_vocab_word_by_id(word_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM vocab_lists WHERE id = ?",
        (word_id,)
    )

    conn.commit()
    conn.close()
