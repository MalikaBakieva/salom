import sqlite3

conn = sqlite3.connect('simple.db')  # agar shu fayl mavjud bo'lsa
# boglan, aks holda yaratadi keyin boglan

cursor = conn.cursor()  # so'rov jo'natish uchun yo'lak ochdik

# yo'lak ochishdan maqsad  -> bazaga sorov jonatish uchun
# so'rov turlari -> create, read, update, delete

# Jadval yaratish
cursor.execute("""CREATE TABLE IF NOT EXISTS contacts (
                  id INTEGER PRIMARY KEY,
                  first_name TEXT NOT NULL,
                  last_name TEXT ,
                  phone_number TEXT NOT NULL    
                  );""")
conn.commit()  # !eslatma commit faqat malumot qoshilganda ishlatamiz
# print("Contacts table created successfully")
# INSERT DATA
# first_name = input("Ism kiriting: ")
# last_name = input("Familya kiriting: ")
# phone_number = input("Nomer kiriting: ")
#
# cursor.execute(
#     """
#     INSERT INTO contacts (first_name, last_name, phone_number)
#     VALUES(?, ?, ?);
#     """, (first_name, last_name, phone_number)
# )
# conn.commit()
# print(f"success")
# bu sorovimiz vazifasi berilgan jadvalga bitta qator malumot qoshishdir
# READ -> SELECT -> qaysi jadavalni va qaysi ustunga tegishla malumotni olish ucun
contacts = cursor.execute("SELECT * FROM contacts;")
print(contacts.fetchall())
conn.close()
