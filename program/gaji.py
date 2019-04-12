def gaji() :
    print("\n\t-----PROGRAM GAJI KARYAWAN-----")
    from texttable import Texttable
    
    table = Texttable ()
    jawab = "y"
    no = 0
    nama = []
    jabatan = []
    gaji = []
    

    while (jawab == 'y'):
        nama.append(input("\n Masukkan Nama : "))
        jab = input("\n Jabatan : ")
        jabatan.append(jab)

        if (jab == 'Programmer'):
            (jabatan == 'Programmer')
            gaji.append(7000000)
            jawab = input("\n tambah lagi? ")
            no+=1
            
        elif (jab == 'Direktur'):
            (jabatan == 'Direktur')
            gaji.append(10000000)
            jawab = input("\n tambah lagi? ")
            no+=1

        elif (jab == 'Operator'):
            (jabatan == 'Operator')
            gaji.append(4000000)
            jawab = input("\n tambah lagi? ")
            no+=1

        else:
            break

    for i in range (no):
        
        table.set_cols_dtype(['i','t','t','t'])    
        table.add_rows([['No','Nama','Jabatan','Gaji'],[i+1,nama[i],jabatan[i],gaji[i]]])


    print (table.draw())
    tanya()

def tanya():
     pil = input("\nApakah Anda ingin mengulang ( y / t ) ? ")
     if pil == 'y' :
        gaji()
     else :
        print("\n\tTERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI")




