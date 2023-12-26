def cari_vga_amd(
    vga,
    harga_processor,
    harga_motherboard, 
    list_vga_amd,
    database
):
    found_vga = False

    harga_tambahan_1 = harga_motherboard - harga_processor
    harga_vga = vga + harga_tambahan_1

    for list_amd_vga in list_vga_amd:
        if harga_vga >= list_amd_vga[3]:
            database.execute("SELECT MAX(Harga) AS Max_Harga FROM vga_amd WHERE Harga <= %s", (harga_vga,))
            max_harga_vga = database.fetchone()[0]

            if max_harga_vga == list_amd_vga[3]:             
                print(f"VGA \t\t : {list_amd_vga[1]} - {list_amd_vga[3]}")
                found_vga = True

    if not found_vga:
        print("Maaf, data vga tidak ditemukan.")