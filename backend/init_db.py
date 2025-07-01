import sqlite3

# ✅ Connect to SQLite DB (create if not exists)
conn = sqlite3.connect('calories.db')
c = conn.cursor()

# ✅ Create table
c.execute('''
CREATE TABLE IF NOT EXISTS food_calories (
    food TEXT PRIMARY KEY,
    calories INTEGER
)
''')

# ✅ Use Food-101 style labels (underscore format)
food_data = [
    ('pizza', 350),
    ('hamburger', 500),
    ('ice_cream', 200),
    ('pancake', 250),
    ('chocolate', 150),
    ('cheeseburger', 500),
    ('chicken_wings', 450),
    ('sushi', 200),
    ('sandwich', 300)
]

c.executemany('INSERT OR IGNORE INTO food_calories (food, calories) VALUES (?, ?)', food_data)

conn.commit()
conn.close()

print("✅ Database created with standardized food names (underscore style)!")
