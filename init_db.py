import sqlite3

# Connect to the database (creates one if it doesn't exist)
conn = sqlite3.connect('anpr.db')
cursor = conn.cursor()

# Create table for registered vehicles
cursor.execute('''
CREATE TABLE IF NOT EXISTS registered_vehicles (
    plate TEXT PRIMARY KEY
)
''')

# Create table for detection logs
cursor.execute('''
CREATE TABLE IF NOT EXISTS detections (
    plate TEXT,
    status TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Add registered plate numbers
plates = ['MH12AB1234', 'DL8CAF1234', 'RJ14CV0002']
cursor.executemany('INSERT OR IGNORE INTO registered_vehicles (plate) VALUES (?)',
                   [(plate,) for plate in plates])

conn.commit()
conn.close()

print("✅ Database created with registered vehicles.")
