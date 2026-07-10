import os
import sys

# Definisi Kode Warna ANSI Termux
GREEN = '\033[92m'
RED = '\033[91m'
WHITE = '\033[97m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
ORANGE = '\033[38;5;208m'
RESET = '\033[0m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_interface():
    clear_screen()
    
    # Logo ASCII FERIXXYZ dengan gradasi warna ANSI
    print(f"{GREEN}███████╗███████╗██████╗ ██╗██╗  ██╗██╗   ██╗██████╗██████╗ {RESET}")
    print(f"{GREEN}██╔════╝██╔════╝██╔══██╗██║╚██╗██╔╝╚██╗ ██╔╝╚════██╗╚════██╗{RESET}")
    print(f"{CYAN}█████╗  █████╗  ██████╔╝██║ ╚███╔╝  ╚███╔╝  █████╔╝ █████╔╝{RESET}")
    print(f"{ORANGE}██╔══╝  ██╔══╝  ██╔══██╗██║ ██╔██╗  ██╔██╗  ╚═══██╗ ╚═══██╗{RESET}")
    print(f"{RED}██║     ███████╗██║  ██║██║██╔╝ ██╗██╔╝ ██╗██████╔╝██████╔╝{RESET}")
    print(f"{RED}╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ {RESET}")
    print()
    
    # Bagian Header Notifikasi
    print(f"{GREEN}========================================================{RESET}")
    print(f"{MAGENTA}                       NOTIFIKASI                       {RESET}")
    print(f"{GREEN}========================================================{RESET}")
    
    # Metadata teks disesuaikan dengan identitas baru
    print(f"{GREEN}➔ Host :{RESET} {WHITE}u0_a410@localhost{RESET}")
    print(f"{GREEN}➔ Hallo :{RESET} {WHITE}FERIXXYZ 👋{RESET}")
    print(f"{GREEN}➔ Layer :{RESET} {RED} FX {RESET}")
    print(f"{GREEN}➔ Skrg hari :{RESET} {WHITE}Rabu{RESET}")
    print(f"{GREEN}➔ Skrg tanggal :{RESET} {WHITE}01{RESET}")
    print(f"{GREEN}➔ Skrg bulan :{RESET} {WHITE}Juli{RESET}")
    print(f"{GREEN}➔ Selamat :{RESET} {WHITE}Siang 🌅{RESET}")
    print(f"{GREEN}➔ Rilis :{RESET} {WHITE}17 / 12 / 2024{RESET}")
    print(f"{GREEN}➔ Jumlah pengguna :{RESET} {WHITE}043{RESET}")
    print(f"{GREEN}➔ QR donasi admin 👇👇{RESET}")
    print(f"{RED}Link{RESET} : {CYAN}https://j.top4top.io/p_3812kyzmd1.jpg{RESET}")
    print()
    
    # Kotak List Menu / Lemari Tools
    print(f"{WHITE}┌───────────────────────────────────────────────────────┐{RESET}")
    print(f"{WHITE}│{RESET}               {RED}LEMARI TOOLS ADA DIBAWAH{RESET}                {WHITE}│{RESET}")
    print(f"{WHITE}├───────────────────────────────────────────────────────┤{RESET}")
    print(f"{WHITE}│{RESET} [{RED} AL {RESET}] {CYAN}MENU HACKING MEDIA{RESET}                                 {WHITE}│{RESET}")
    print(f"{WHITE}│{RESET} [{RED} PS {RESET}] {CYAN}MENU PSHING MEDIA{RESET}                                  {WHITE}│{RESET}")
    print(f"{WHITE}│{RESET} [{RED} DO {RESET}] {CYAN}MENU DOWNLOAD MEDIA{RESET}                                {WHITE}│{RESET}")
    print(f"{WHITE}│{RESET} [{RED} EN {RESET}] {CYAN}MENU ENCRIPSY CODER FILE{RESET}                           {WHITE}│{RESET}")
    print(f"{WHITE}│{RESET} [{RED} TM {RESET}] {CYAN}MENU SC+ TAMBAHAN{RESET}                                  {WHITE}│{RESET}")
    print(f"{WHITE}│{RESET} [{RED} DK {RESET}] {CYAN}MENU PRODAK SC{RESET}                                     {WHITE}│{RESET}")
    print(f"{WHITE}└───────────────────────────────────────────────────────┘{RESET}")
    print()
    
    # Prompt Input Pengguna
    try:
        pilihan = input(f"{MAGENTA}>>> {GREEN}Masukkan pilihan anda {RESET}[ {RED}TOOLSLV{RESET} ] : ")
        print(f"\n{GREEN}[+] Pilihan anda: {pilihan}{RESET}")
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Keluar...{RESET}")
        sys.exit(0)

if __name__ == "__main__":
    display_interface()