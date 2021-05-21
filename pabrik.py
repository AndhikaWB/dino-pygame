import papan
import random

class Pabrik:
    def __init__(self, tinggi_jalan):
        # Ketinggian jalan
        self.tinggi_jalan = tinggi_jalan

        # Jarak antar musuh
        self.jarak_min = 450
        self.jarak_maks = 600
        self.gap_jarak = 25
        
        # Jumlah musuh maksimal
        self.jumlah_maks = 2
        # List musuh mula-mula
        self.list_musuh = []

    def reset(self):
        # Hapus semua musuh yang ada
        self.list_musuh.clear()

    def tambah(self, layar):
        # Acak tipe musuh yang akan ditampilkan
        tipe_musuh = random.randint(0, 3)
        if tipe_musuh == 0:
            Musuh = papan.Siput
        elif tipe_musuh == 1:
            Musuh = papan.Simerah
        elif tipe_musuh == 2:
            Musuh = papan.Lalat
        elif tipe_musuh == 3:
            Musuh = papan.Lebah

        # Acak jarak antar musuh yang akan ditampilkan
        # Misalkan jarak min = 450, jarak maks = 600, dan gap jarak = 25
        # Maka kemungkinan yang dihasilkan yaitu 450, 475, ..., 575, 600
        jarak_musuh = random.randrange(self.jarak_min, self.jarak_maks, self.gap_jarak)

        # Jika tidak ada musuh sebelumnya
        if len(self.list_musuh) == 0:
            # Jarak setara dengan lebar layar
            jarak_musuh = layar.get_width()
            # Tambahkan musuh baru ke dalam list
            self.list_musuh.append(Musuh(self.tinggi_jalan, jarak_musuh))
        # Jika sudah ada musuh sebelumnya
        elif len(self.list_musuh) < self.jumlah_maks:
            # Tambah jarak dengan jarak musuh terakhir
            jarak_musuh += self.list_musuh[-1].pos_x
            # Tambahkan musuh baru ke dalam list
            self.list_musuh.append(Musuh(self.tinggi_jalan, jarak_musuh))

    def perbarui(self, layar, frame, menu, nilai, dino):
        # Tambah musuh bila memungkinkan
        self.tambah(layar)

        # Gunakan list salinan [:] karena ada operasi penghapusan
        # Mencegah kemungkinan adanya anggota yang tidak terhapus
        for musuh in self.list_musuh[:]:
            # Perbarui posisi tiap-tiap musuh
            musuh.perbarui(layar, frame, menu)

            # Game tidak sedang berhenti/tamat
            if menu.status == "BERMAIN":
                # Game berakhir jika dino menabrak musuh
                if dino.area_anim.colliderect(musuh.area_anim):
                    dino.mati()
                    menu.tamat()
                # Nilai skor bertambah jika berhasil melewati musuh
                elif musuh.status == "DILEWATI":
                    # Hapus musuh yang tidak terpakai
                    self.list_musuh.remove(musuh)
                    nilai.tambah()