def cari_sisa_komponen(
    harga_baru, 
    harga_processor, 
    harga_motherboard, 
    harga_vga,
    list_ram,
    list_ssd,
    list_psu,
    list_casing
):
    # RAM
    for ram in list_ram:
        if harga_motherboard == ram[2] and ram[5] == 250000:
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

    harga_sisa = harga_baru - harga_processor - harga_motherboard - harga_vga
    print(f"Sisa Uang\t : {harga_sisa}")
