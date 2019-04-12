def nilai() :
    print("\n\tPROGRAM PENILAIAN MAHASISWA ")
    print("\n\tKAMPUS PELITA BANGSA ")
    
    from texttable import Texttable
    
    table = Texttable ()
    jawab = "y"
    no = 0
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []

    while (jawab =="y") :
        nama.append(input("\nMasukkan Nama : "))
        nim.append(input("\nMasukkan NIM : "))
        nilai_tugas.append(input("\nNilai Tugas : "))
        nilai_uts.append(input("\nNilai UTS : "))
        nilai_uas.append(input("\nNilai UAS : "))
        jawab = input("\nTambah data ( y / t )? ")
        no +=1
        


    for i in range (no) :
        tugas = int(nilai_tugas[i])
        uts = int(nilai_uts[i])
        uas = int(nilai_uas[i])
        akhir = int(tugas*30/100)+(uts*35/100)+(uas*35/100)
        table.set_cols_dtype(['i','t','t','t','t','t','t'])
        table.add_rows([['No','Nama','NIM','TUGAS','UTS','UAS','AKHIR'],[i+1,nama[i],nim[i],nilai_tugas[i],nilai_uts[i],nilai_uas[i],akhir]])

    print (table.draw())
    tanya()

def tanya():
     pil = input("\nApakah Anda ingin mengulang ( y / t ) ? ")
     if pil == 'y' :
         nilai()
     else :
        print(" TERIMA KASIH ")








       








