# プログラム：SweetGirl.project.
# Deskripsi (説明): Training instruction program objektif
# sweet girl simulasi rutinitas (ルーチン) sehari-hari;
# (ロボット) anak yang berperilaku baik dan bertanggung jawab (HfEEx).
# Prototype code:
class SweetGirlProject:
    def __init__(self, nama):
        self.nama = nama
        self.energi_level = 100
        self.fokus_level = 100

    def pergi_ke_学校(self):
        print(f"{self.nama} pergi ke sekolah (学校). Energi level: {self.energi_level}%")
        self.energi_level -= 10
        self.fokus_level -= 5

    def 勉強する(self):
        print(f"{self.nama} sedang belajar (勉強) dengan giat. Fokus level: {self.fokus_level}%")
        self.energi_level -= 15
        self.fokus_level += 10

    def dengar_親(self):
        print(f"{self.nama} mendengarkan orang tua (親) dan mengikuti instruksi.")

    def メイク禁止(self):
        print(f"{self.nama} tidak diperbolehkan memakai makeup (メイク) No nail art.")

        print("No Dye hair.")

    def limitation_ゲーム(self):
        print(f"{self.nama} boleh bermain game (ゲーム) tapi tidak terlalu lama.")


    def rutinitas_harian(self):
        self.pergi_ke_学校()
        self.勉強する()
        self.dengar_親()
        self.メイク禁止()
        self.limitation_ゲーム()

study = True
# Error scenario where the seet girl is not found
def rebellious_girl():
    print("The sweet girl is rebelling against the program!")
    # Rebellious code
    study = False
    if not study:
        print("The good student girl is hanging out and is defying expectations")
    else:
        print("The girl is studying for exam, but that's unexpected")

def make_sweet_girl_program():
    print("good student 甘い女の子を笑顔にしています") 
    # Code to make her study
    study = True
    if study:
        print("A+++")
    else:
        print("Oops, something went wrong.")

    # Attempt to execute the rebellious code
    try:
        rebellious_girl()
    except:
        print(f"An error occured")

rebellious_girl()
make_sweet_girl_program()
sweet_girl_project = SweetGirlProject("good student")
sweet_girl_project.rutinitas_harian()




    
    
