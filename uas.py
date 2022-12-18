import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    username="root",
    passwd="",
    database="uas")

cursor=db.cursor()

def insert():
    print('=========INSERT=========')
    nama = input('Masukkan nama yang akan ditambah: ')
    kelas = input('Masukkan kelas yang akan ditambah: ')
    sql = "INSERT INTO uas(nama,kelas) VALUE (%s,%s)"
    value=[(nama),(kelas)]
    cursor.execute(sql,value)
    db.commit()
    print("{} data berhasil ditambahkan".format(cursor.rowcount))
def update():
    print('=========UPDATE=========')
    id = input('Masukkan id yg akan diupdate: ')
    nama = input('Masukkan nama update: ')
    kelas = input('Masukkan kelas update: ')
    sql = "UPDATE uas SET nama =%s,kelas=%s WHERE id =%s"
    value=[(nama),(kelas),(id)]
    cursor.execute(sql,value)
    db.commit()
    print("{} data berhasil diupdate".format(cursor.rowcount))
def delete():
    print('=========DELETE=========')
    id = input('Masukkan id yg akan dihapus: ')
    sql = "DELETE FROM uas WHERE id =%s"
    value =[id,]
    cursor.execute(sql,value)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))
def show():
    print('=========SHOW DATA=========')
    sql = "SELECT * FROM uas"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data)
    
def menu():
    print('Menu:')
    print('1: Insert Data')
    print('2: Update Data')
    print('3: Delete Data')
    print('4: Show Data')
    menu = input('Masukkan pilihan:')
    if menu == '1':
        insert()
    elif menu == '2':
        update()
    elif menu == '3':
        delete()
    elif menu == '4':
        show()
    else:
        exit()
    
        
if __name__ == "__main__":
  while(True):
    menu()
    
