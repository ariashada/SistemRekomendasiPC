from AMDprocessor import cari_amd_produktivitas, cari_amd_game
from INTELprocessor import cari_intel_produktivitas, cari_intel_game

def cari_vga_nvdia(
    vga, 
    list_vga_nvidia,
    database
):
    found_vga = False
    
    harga_processor_amd, harga_motherboard_amd = cari_amd_produktivitas()
    harga_processor_amd_game, harga_motherboard_amd_game = cari_amd_game()
    harga_processor_intel, harga_motherboard_intel = cari_intel_produktivitas()
    harga_processor_intel_game, harga_motherboard_intel_game = cari_intel_game()
    
    harga_processor = harga_processor_amd + harga_processor_amd_game + harga_processor_intel + harga_processor_intel_game
    harga_motherboard = harga_motherboard_amd + harga_motherboard_amd_game + harga_motherboard_intel + harga_motherboard_intel_game

    harga_tambahan_1 = harga_motherboard - harga_processor
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
