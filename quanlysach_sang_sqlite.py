import sqlite3, SapXepSach
from SapXepSach import *
books = Read_data()
try:
	conn = sqlite3.connect("Dulieusach.db")
	cursor = conn.cursor()

	for book in books:
		query = """INSERT INTO Sach VALUES(?,?,?,?,?,?);"""
		cursor.execute(query, (book.stt, book.name, book.author, book.date, book.month, book.year))
		conn.commit()
	print(cursor.rowcount)
	cursor.close()
except sqlite3.Error as error:
	print('Error SQLite', error)
finally:
	if conn:
		conn.close()