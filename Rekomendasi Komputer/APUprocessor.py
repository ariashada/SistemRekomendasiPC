# ==========================================================Produktivitas===============================================================
def cari_apu_produktivitas(
    harga_baru, 
    processor,
    motherboard,
    list_processor_igpu,
    list_motherboard_amd,
    list_motherboard_intel,
    database
):
    processor = harga_baru*0.5
    motherboard = harga_baru*0.5
    
    found_processor = False
    found_motherboard = False
    
    database.execute("SELECT MAX(Score_Produktivitas) AS Max_Score FROM processor_igpu WHERE Harga <= %s", (processor,))
    max_score_produktivitas2 = database.fetchone()[0]
    
    for list_igpu in list_processor_igpu:
        if processor >= list_igpu[9]:
            score_proci = float(list_igpu[5])
            score_igpu = list_igpu[7]

            if score_proci >= max_score_produktivitas2:
                print(f"\n\nProcessor \t : {list_igpu[1]} - {list_igpu[9]}")
                found_processor = True

                harga_tambahan = processor - list_igpu[9]
                harga_motherboard = motherboard + harga_tambahan
                
                for motherboard_amd in list_motherboard_amd:
                    if list_igpu[2] == motherboard_amd[2] and harga_motherboard >= motherboard_amd[5]:
                        database.execute("SELECT * FROM motherboard_amd WHERE Soket = %s AND Harga <= %s", (list_igpu[2], harga_motherboard))
                        list_motherboard_amd = database.fetchall()
                        
                        max_harga_motherboard_amd = max([mb[5] for mb in list_motherboard_amd], default=0)
                        
                        if max_harga_motherboard_amd == motherboard_amd[5]:              
                            print(f"Motherboard \t : {motherboard_amd[1]} - {motherboard_amd[5]}")
                            found_motherboard = True
                
                for motherboard_intel in list_motherboard_intel:
                    if list_igpu[2] == motherboard_intel[2] and harga_motherboard >= motherboard_intel[5]:
                        database.execute("SELECT * FROM motherboard_intel WHERE Soket = %s AND Harga <= %s", (list_igpu[2], harga_motherboard))
                        list_motherboard_intel = database.fetchall()
                            
                        max_harga_motherboard_intel = max([mb[5] for mb in list_motherboard_intel], default=0)
                        
                        if max_harga_motherboard_intel == motherboard_intel[5]:
                            print(f"Motherboard \t : {motherboard_intel[1]} - {motherboard_intel[5]}")
                            found_motherboard = True
                
                if not found_motherboard:
                    print("Maaf, data motherboard tidak ditemukan.")

    if not found_processor:
        print("Maaf, data processor tidak ditemukan.")
        
    print(f"Score Processor : {score_proci}")

# ==========================================================Game===============================================================
def cari_apu_game(
    harga_baru,
    processor,
    motherboard,
    list_processor_igpu,
    list_motherboard_amd,
    list_motherboard_intel,
    database
):
    processor = harga_baru*0.5
    motherboard = harga_baru*0.5
    
    found_processor = False
    found_motherboard = False
    
    database.execute("SELECT MAX(Score_Game) AS Max_Score FROM processor_igpu WHERE Harga <= %s", (processor,))
    max_score_game2 = database.fetchone()[0] 
    
    for list_igpu in list_processor_igpu:
        if processor >= list_igpu[9]:
            score_proci = float(list_igpu[5])
            score_igpu = list_igpu[7]

            if score_proci >= max_score_game2:
                print(f"\n\nProcessor \t : {list_igpu[1]} - {list_igpu[9]}")
                found_processor = True

                harga_tambahan = processor - list_igpu[9]
                harga_motherboard = motherboard + harga_tambahan
                
                for motherboard_amd in list_motherboard_amd:
                    if list_igpu[2] == motherboard_amd[2] and harga_motherboard >= motherboard_amd[5]:
                        database.execute("SELECT * FROM motherboard_amd WHERE Soket = %s AND Harga <= %s", (list_igpu[2], harga_motherboard))
                        list_motherboard_amd = database.fetchall()
                        
                        max_harga_motherboard_amd = max([mb[5] for mb in list_motherboard_amd], default=0)
                        
                        if max_harga_motherboard_amd == motherboard_amd[5]:              
                            print(f"Motherboard \t : {motherboard_amd[1]} - {motherboard_amd[5]}")
                            found_motherboard = True
                
                for motherboard_intel in list_motherboard_intel:
                    if list_igpu[2] == motherboard_intel[2] and harga_motherboard >= motherboard_intel[5]:
                        database.execute("SELECT * FROM motherboard_intel WHERE Soket = %s AND Harga <= %s", (list_igpu[2], harga_motherboard))
                        list_motherboard_intel = database.fetchall()
                            
                        max_harga_motherboard_intel = max([mb[5] for mb in list_motherboard_intel], default=0)
                        
                        if max_harga_motherboard_intel == motherboard_intel[5]:
                            print(f"Motherboard \t : {motherboard_intel[1]} - {motherboard_intel[5]}")
                            found_motherboard = True
                
                if not found_motherboard:
                    print("Maaf, data motherboard tidak ditemukan.")

    if not found_processor:
        print("Maaf, data processor tidak ditemukan.")
        
    print(f"Score Processor : {score_proci}")
