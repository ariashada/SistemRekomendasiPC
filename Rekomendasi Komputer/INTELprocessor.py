# ==========================================================Produktivitas===============================================================
def cari_intel_produktivitas(
    processor,
    motherboard,
    list_processor_intel,
    list_motherboard_intel,
    database
):
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

                        if max_harga_motherboard == motherboard_intel[5]:
                            print(f"Motherboard \t : {motherboard_intel[1]} - {motherboard_intel[5]}")
                            found_motherboard = True

                if not found_motherboard:
                    print("Maaf, data motherboard tidak ditemukan.")

    if not found_processor:
        print("Maaf, data processor tidak ditemukan.")
        
    print(f"Score Processor : {score_proci}")

# ==========================================================Game===============================================================
def cari_intel_game(
    processor,
    motherboard,
    list_processor_intel,
    list_motherboard_intel,
    database
):
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

                        if max_harga_motherboard == motherboard_intel[5]:
                            print(f"Motherboard \t : {motherboard_intel[1]} - {motherboard_intel[5]}")
                            found_motherboard = True

                if not found_motherboard:
                    print("Maaf, data motherboard tidak ditemukan.")

    if not found_processor:
        print("Maaf, data processor tidak ditemukan.")
        
    print(f"Score Processor : {score_proci}")