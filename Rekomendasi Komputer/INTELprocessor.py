harga_tambahan_1 = 0
motherboard_intel = 0
# ==========================================================Produktivitas===============================================================
def cari_intel_produktivitas(
    processor,
    motherboard,
    list_processor_intel,
    list_motherboard_intel,
    database
):
    global harga_tambahan_1, motherboard_intel
    
    found_processor = False
    found_motherboard = False
    
    database.execute("SELECT MAX(Score_Produktivitas) AS Max_Score FROM processor_intel WHERE Harga <= %s", (processor,))
    max_score_produktivitas1 = database.fetchone()[0]

    for list_intel in list_processor_intel:
        if processor >= list_intel[7]:
            score_proci = float(list_intel[4])

            if score_proci >= max_score_produktivitas1:
                print(f"\n\nProcessor \t : {list_intel[1]} - {list_intel[7]}")
                found_processor = True

                harga_tambahan = processor - list_intel[7]
                harga_motherboard = motherboard + harga_tambahan

                for motherboard_intel in list_motherboard_intel:
                    if list_intel[2] == motherboard_intel[2] and harga_motherboard >= motherboard_intel[5]:
                        database.execute("SELECT * FROM motherboard_intel WHERE Soket = %s AND Harga <= %s", (list_intel[2], harga_motherboard))
                        list_motherboard = database.fetchall()

                        max_harga_motherboard = max([mb[5] for mb in list_motherboard], default=0)
                        harga_tambahan_1 = harga_motherboard - motherboard_intel[5]

                        if max_harga_motherboard == motherboard_intel[5]:
                            print(f"Motherboard \t : {motherboard_intel[1]} - {motherboard_intel[5]}")
                            found_motherboard = True
                            print(f"Score Processor : {score_proci}")

                if not found_motherboard:
                    print("Maaf, data motherboard tidak ditemukan.")

    if not found_processor:
        print("Maaf, data processor tidak ditemukan.")

# ==========================================================Game===============================================================
def cari_intel_game(
    processor,
    motherboard,
    list_processor_intel,
    list_motherboard_intel,
    database
):
    global harga_tambahan_1, motherboard_intel
    
    found_processor = False
    found_motherboard = False
    
    database.execute("SELECT MAX(Score_Game) AS Max_Score FROM processor_intel WHERE Harga <= %s", (processor,))
    max_score_game1 = database.fetchone()[0]

    for list_intel in list_processor_intel:
        if processor >= list_intel[7]:
            score_proci = float(list_intel[5])

            if score_proci >= max_score_game1:
                print(f"\n\nProcessor \t : {list_intel[1]} - {list_intel[7]}")
                found_processor = True

                harga_tambahan = processor - list_intel[7]
                harga_motherboard = motherboard + harga_tambahan

                for motherboard_intel in list_motherboard_intel:
                    if list_intel[2] == motherboard_intel[2] and harga_motherboard >= motherboard_intel[5]:
                        database.execute("SELECT * FROM motherboard_intel WHERE Soket = %s AND Harga <= %s", (list_intel[2], harga_motherboard))
                        list_motherboard = database.fetchall()

                        max_harga_motherboard = max([mb[5] for mb in list_motherboard], default=0)
                        harga_tambahan_1 = harga_motherboard - motherboard_intel[5]

                        if max_harga_motherboard == motherboard_intel[5]:
                            print(f"Motherboard \t : {motherboard_intel[1]} - {motherboard_intel[5]}")
                            found_motherboard = True
                            print(f"Score Processor : {score_proci}")

                if not found_motherboard:
                    print("Maaf, data motherboard tidak ditemukan.")

    if not found_processor:
        print("Maaf, data processor tidak ditemukan.")
        
# ==========================================================AMD===============================================================
def cari_vga_amd(
    vga,
    list_vga_amd,
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
        
# ==========================================================Nvidia===============================================================
def cari_vga_nvdia(
    vga, 
    list_vga_nvidia,
    database
):
    found_vga = False

    harga_vga = vga + harga_tambahan_1

    for list_nvidia_vga in list_vga_nvidia:
        if harga_vga >= list_nvidia_vga[3]:
            database.execute("SELECT MAX(Harga) AS Max_Harga FROM vga_nvidia WHERE Harga <= %s", (harga_vga,))
            max_harga_vga = database.fetchone()[0]

            if max_harga_vga == list_nvidia_vga[3]:             
                print(f"VGA \t\t : {list_nvidia_vga[1]} - {list_nvidia_vga[3]}")
                found_vga = True
                
    if not found_vga:
        print("Maaf, data vga tidak ditemukan.")
        
# ==========================================================Sisa Komponen===============================================================
def cari_sisa_komponen(
    list_ram,
    list_ssd,
    list_psu,
    list_casing
):
    # RAM
    for ram in list_ram:
        if motherboard_intel[3] == ram[2]:
            if ram[5] == 250000:
                print(f"RAM \t\t : {ram[1]} - {ram[5]}")

    # SSD
    for ssd in list_ssd:
        if ssd[4] == 150000:
            print(f"SSD \t\t : {ssd[1]} - {ssd[4]}")

    # PSU
    for psu in list_psu:
        if psu[4] == 500000:
            print(f"PSU \t\t : {psu[1]} - {psu[2]} - {psu[4]}")

    # Casing
    for casing in list_casing:
        if casing[3] == 350000:
            print(f"CASING \t\t : {casing[1]} - {casing[2]} - {casing[3]}")