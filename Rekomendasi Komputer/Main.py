from Database import connect_database
from AMDprocessor import cari_amd_produktivitas, cari_amd_game, cari_vga_amd, cari_vga_nvdia, cari_sisa_komponen
from INTELprocessor import cari_intel_produktivitas, cari_intel_game, cari_vga_amd, cari_vga_nvdia, cari_sisa_komponen
from APUprocessor import cari_apu_produktivitas, cari_apu_game
import random

# Terhubung ke database dan dapatkan daftar komponen
(
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
) = connect_database()

# Tentukan anggaran dan hitung anggaran komponen
harga = int(input("Masukkan Nominal Harga: "))
harga_baru = harga-1250000 #250 ram, 150 ssd, 500 psu, 350 casing
processor = harga_baru*0.3
motherboard = harga_baru*0.3
vga = harga_baru*0.4

# Tentukan kebutuhan pengguna (Produktivitas atau Game)
kebutuhan = input("\nInput Kebutuhan:\n1. Produktivitas\n2. Game\nSilahkan Pilih: ")

# Tentukan pilihan pengguna untuk processor (AMD, Intel, Tidak)
jenis_processor = input("\nIngin Menggunakan Processor Apa?\n1. AMD\n2. Intel\n3. APU\nSilahkan Pilih: ")

# Inisialisasi jenis_gpu sebelum pernyataan if
jenis_gpu = ""

if jenis_processor == "3" or jenis_processor.lower() == "apu":
    print("Anda memilih APU, GPU tidak perlu dipilih.")
else:
# Tentukan pilihan pengguna untuk GPU (AMD, Nvidia, Random)
    jenis_gpu = input("\nMau Menggunakan GPU Apa ?\n1. AMD\n2. Nvidia\nSilahkan Pilih: ")

#============================================================Produktivitas=============================================
if kebutuhan == "1" or kebutuhan == "produktivitas":
    if jenis_processor == "1" or jenis_processor.lower() == "amd":
        Processor_AMD_Produktivitas = cari_amd_produktivitas(
            processor, 
            motherboard, 
            list_processor_amd, 
            list_motherboard_amd, 
            database
        )
        print(Processor_AMD_Produktivitas)
    elif jenis_processor == "2" or jenis_processor.lower() == "intel":
        Processor_Intel_Produktivitas = cari_intel_produktivitas(
            processor, 
            motherboard,  
            list_processor_intel, 
            list_motherboard_intel, 
            database
        )
        print(Processor_Intel_Produktivitas)
    elif jenis_processor == "3" or jenis_processor.lower() == "apu":
        Processor_Apu_Produktivitas = cari_apu_produktivitas(
            harga_baru, 
            processor,
            motherboard,
            list_processor_igpu,
            list_motherboard_amd,
            list_motherboard_intel,
            database
        )
        print(Processor_Apu_Produktivitas)
    else:
        print("Maaf, pilihan processor tidak valid.")

#===============================================================GAME===================================================
elif kebutuhan == "2" or kebutuhan == "game":
    if jenis_processor == "1" or jenis_processor.lower() == "amd":
        Processor_AMD_Game = cari_amd_game(
            processor,
            motherboard,
            list_processor_amd,
            list_motherboard_amd,
            database
        )
        print(Processor_AMD_Game)
    elif jenis_processor == "2" or jenis_processor.lower() == "intel":
        Processor_Intel_Game = cari_intel_game(
            processor, 
            motherboard,  
            list_processor_intel, 
            list_motherboard_intel, 
            database
        )
        print(Processor_Intel_Game)
    elif jenis_processor == "3" or jenis_processor.lower() == "apu":
        Processor_APU_Game = cari_apu_game(
            harga_baru,
            processor,
            motherboard,
            list_processor_igpu,
            list_motherboard_amd,
            list_motherboard_intel,
            database
        )
        print(Processor_APU_Game)
    else:
        print("Maaf, pilihan processor tidak valid.")

#============================================================GPU=============================================
if jenis_gpu == "1" or jenis_gpu.lower() == "amd":
    VGA_AMD = cari_vga_amd(
        vga,
        list_vga_amd,
        database
    )
    print(VGA_AMD)
elif jenis_gpu == "2" or jenis_gpu.lower() == "nvidia":
    VGA_NVDIA = cari_vga_nvdia(
        vga,
        list_vga_nvidia,
        database
    )
    print(VGA_NVDIA)
else:
    print("Pilihan GPU tidak valid.")
    
sisa_komponen = cari_sisa_komponen(
    list_ram,
    list_ssd,
    list_psu,
    list_casing
)
print(sisa_komponen)