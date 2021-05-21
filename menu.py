import glob
import pygame

def muat_gambar(nama_animasi):
    # Muat gambar (bisa lebih dari satu) yang terdapat pada folder "assets"
    return [ pygame.image.load(gambar).convert_alpha() for gambar in glob.glob(f"assets/{nama_animasi}*.png") ]

class Menu:
    def __init__(self):
        # Status game mula-mula
        self.status = "TAMAT"

        # Posisi judul dari tengah layar
        self.judul_pos_y = -130
        # Posisi pilihan pertama pada menu
        self.menu_pos_y = self.judul_pos_y + 70
        # Jarak untuk pilihan selanjutnya
        self.gap_pilihan = 40

        # Gambar yang dibutuhkan pada menu (hemat proses)
        self.teks_judul = muat_gambar("title")
        self.teks_main_baru = muat_gambar("menu_start")
        self.teks_lanjutkan = muat_gambar("menu_continue")
        self.teks_keluar = muat_gambar("menu_exit")

        # Judul dan pilihan menu mula-mula
        self.judul = self.teks_judul[0] # Bellatrix's dino game
        self.menu = [ self.teks_main_baru, self.teks_keluar]
    
        # Indeks pilihan yang sedang dipilih pada menu
        self.pilihan = 0 # Permainan baru

    def perbarui(self, layar):
        if self.status != "BERMAIN":
            # Kalkulasikan posisi judul berdasarkan lebar layar, tinggi layar, dan jarak dari tengah layar
            # Perlu diingat bahwa koordinat awal (0, 0) pada layar dimulai dari pojok kiri atas, bukan pojok kiri bawah
            area_judul = self.judul.get_rect(center = (layar.get_width() // 2, layar.get_height() // 2 + self.judul_pos_y))
            # Tampilkan gambar judul pada koordinat tertentu dalam layar game
            layar.blit(self.judul, area_judul)

            # Variabel "menu_pos_y" hanya digunakan sebagai konstan
            # Gunakan variabel sementara untuk mengubah nilainya
            temp_pos = self.menu_pos_y

            for indeks, pilihan in enumerate(self.menu):
                # Kalkulasikan posisi pilihan berdasarkan lebar layar, tinggi layar, dan jarak dari tengah layar
                area_pilihan = pilihan[0].get_rect(center = (layar.get_width() // 2, layar.get_height() // 2 + temp_pos))

                # Tampilkan tiap-tiap pilihan pada menu
                # 1) pilihan[0] = bila pilihan menu tersebut tidak sedang dipilih, teks berwarna putih
                # 2) pilihan[1] = bila pilihan menu tersebut sedang dipilih, teks berwarna hitam
                # Keduanya harus memiliki ukuran yang sama karena posisinya diperhitungkan
                if self.pilihan == indeks:
                    layar.blit(pilihan[1], area_pilihan)
                else: layar.blit(pilihan[0], area_pilihan)

                # Tambah jarak untuk pilihan selanjutnya
                temp_pos += self.gap_pilihan

    def reset(self):
        # Lanjutkan game dari posisi terakhir
        self.status = "BERMAIN"
        self.pilihan = 0

    def berhenti(self):
        # Hentikan game untuk sementara
        self.status = "BERHENTI"
        self.judul = self.teks_judul[1] # Permainan berhenti
        self.menu = [ self.teks_lanjutkan, self.teks_main_baru, self.teks_keluar ]

    def tamat(self):
        # Hentikan game karena menabrak musuh
        self.status = "TAMAT"
        self.judul = self.teks_judul[2] # Permainan berakhir
        self.menu = [ self.teks_main_baru, self.teks_keluar ]

    def berikutnya(self):
        # Memilih pilihan menu berikutnya
        if self.pilihan + 1 < len(self.menu):
            self.pilihan += 1

    def sebelumnya(self):
        # Memilih pilihan menu sebelumnya
        if self.pilihan - 1 >= 0:
            self.pilihan -= 1

    def pilih(self):
        # Memilih pilihan menu saat ini
        if self.menu[self.pilihan] == self.teks_lanjutkan:
            return "LANJUTKAN"
        elif self.menu[self.pilihan] == self.teks_main_baru:
            return "MAIN_BARU"
        elif self.menu[self.pilihan] == self.teks_keluar:
            return "KELUAR"