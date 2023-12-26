# ==========================================================Produktivitas===============================================================
def cari_amd_produktivitas(
    processor,
    motherboard,
    list_processor_amd,
    list_motherboard_amd,
    database
):
    found_processor = False
    found_motherboard = False
    
    database.execute("SELECT MAX(Score_Produktivitas) AS Max_Score FROM processor_amd WHERE Harga <= %s", (processor,))
    max_score_produktivitas = database.fetchone()[0]

    for list_amd in list_processor_amd:
        if processor >= list_amd[7]:
            score_proci = float(list_amd[4])

            if score_proci >= max_score_produktivitas:
                print(f"Processor \t : {list_amd[1]} - {list_amd[7]}")
                found_processor = True

                harga_tambahan = processor - list_amd[7]
                harga_motherboard = motherboard + harga_tambahan

                for motherboard_amd in list_motherboard_amd:
                    if list_amd[2] == motherboard_amd[2] and harga_motherboard >= motherboard_amd[5]:
                        database.execute("SELECT * FROM motherboard_amd WHERE Soket = %s AND Harga <= %s", (list_amd[2], harga_motherboard))
                        list_motherboard = database.fetchall()

                        max_harga_motherboard = max([mb[5] for mb in list_motherboard], default=0)

                        if max_harga_motherboard == motherboard_amd[5]:
                            print(f"Motherboard \t : {motherboard_amd[1]} - {motherboard_amd[5]}")
                            found_motherboard = True

                harga_tambahan_1 = harga_motherboard - motherboard_amd[5]

                if not found_motherboard:
                    print("Maaf, data motherboard tidak ditemukan.")

    if not found_processor:
        print("Maaf, data processor tidak ditemukan.")
        
    print(f"Score Processor : {score_proci}")

# ==========================================================Game===============================================================
def cari_amd_game(
    processor,
    motherboard,
    list_processor_amd,
    list_motherboard_amd,
    database
):
    found_processor = False
    found_motherboard = False
    
    database.execute("SELECT MAX(Score_Game) AS Max_Score FROM processor_amd WHERE Harga <= %s", (processor,))
    max_score_game= database.fetchone()[0]

    for list_amd in list_processor_amd:
        if processor >= list_amd[7]:
            score_proci = float(list_amd[5])

            if score_proci >= max_score_game:
                print(f"Processor \t : {list_amd[1]} - {list_amd[7]}")
                found_processor = True

                harga_tambahan = processor - list_amd[7]
                harga_motherboard = motherboard + harga_tambahan

                for motherboard_amd in list_motherboard_amd:
                    if list_amd[2] == motherboard_amd[2] and harga_motherboard >= motherboard_amd[5]:
                        database.execute("SELECT * FROM motherboard_amd WHERE Soket = %s AND Harga <= %s", (list_amd[2], harga_motherboard))
                        list_motherboard = database.fetchall()

                        max_harga_motherboard = max([mb[5] for mb in list_motherboard], default=0)

                        if max_harga_motherboard == motherboard_amd[5]:
                            print(f"Motherboard \t : {motherboard_amd[1]} - {motherboard_amd[5]}")
                            found_motherboard = True
                            
                harga_tambahan_1 = harga_motherboard - motherboard_amd[5]

                if not found_motherboard:
                    print("Maaf, data motherboard tidak ditemukan.")

    if not found_processor:
        print("Maaf, data processor tidak ditemukan.")
        
    print(f"Score Processor : {score_proci}")

# ==========================================================Game===============================================================
def cari_vga_amd(
    vga,
    list_vga_amd,
    harga_tambahan_1,
    database
):
    found_vga = False

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
