import mysql.connector

def connect_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python1"
    )

    database = mydb.cursor()

    database.execute("SELECT * FROM processor_amd")
    list_processor_amd = database.fetchall()

    database.execute("SELECT * FROM processor_intel")
    list_processor_intel = database.fetchall()

    database.execute("SELECT * FROM processor_igpu")
    list_processor_igpu = database.fetchall()

    database.execute("SELECT * FROM motherboard_amd")
    list_motherboard_amd = database.fetchall()

    database.execute("SELECT * FROM motherboard_intel")
    list_motherboard_intel = database.fetchall()

    database.execute("SELECT * FROM vga_amd")
    list_vga_amd = database.fetchall()

    database.execute("SELECT * FROM vga_nvidia")
    list_vga_nvidia = database.fetchall()

    database.execute("SELECT * FROM ram")
    list_ram = database.fetchall()

    database.execute("SELECT * FROM ssd")
    list_ssd = database.fetchall()

    database.execute("SELECT * FROM psu")
    list_psu = database.fetchall()

    database.execute("SELECT * FROM casing")
    list_casing = database.fetchall()

    # return variabelnya disini agar terdaftar saat di importnya
    return (
        mydb,
        database,
        list_processor_amd,
        list_processor_intel,
        list_processor_igpu,
        list_motherboard_amd,
        list_motherboard_intel,
        list_vga_amd,
        list_vga_nvidia,
        list_ram,
        list_ssd,
        list_psu,
        list_casing
    )