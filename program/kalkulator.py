def kalkulator ():
     
    print("\n\t-----PROGRAM KALKULATOR SEDERHANA-----")
    print("\nPilih Operasi : ")
    print("\n\t1. Jumlah ")
    print("\n\t2. Kurang ")
    print("\n\t3. kali ")
    print("\n\t4. Bagi ")
    print("\n\tSilahkan pilih 1 - 4 : ")
    print(" ")
    pil = input("\t\nMasukkan Pilihan : ")
    if pil == '1' :
        tambah()
    elif pil == '2' :
        kurang()
    elif pil == '3' :
        kali()
    elif pil == '4' :
        bagi()
    else :
        print("maaf, input yang anda masukkan salah")
        print("coba ulangi lagi")
        tanya()
    


    
def tambah() :
    print("\n1. Penjumlahan")
    a = int(input("Masukkan nilai x = "))
    b = int(input("Masukkan nilay y = "))
    c = a+b
    print(" x + y = ", c)
    print(" ")
    tanya()
    
        
def kurang() :
    print("\n2. Pengurangan")
    a = int(input("Masukkan nilai x = "))
    b = int(input("Masukkan nilay y = "))
    c = a-b
    print(" x - y = ", c)
    print(" ")
    tanya()
            
def kali() :
    print("\n3. Perkalian")
    a = int(input("Masukkan nilai x = "))
    b = int(input("Masukkan nilay y = "))
    c = a*b
    print(" x . y = ", c)
    print(" ")
    tanya()
    
        

def bagi() :
    print("\n4. Pembagian")
    a = int(input("Masukkan nilai x = "))
    b = int(input("Masukkan nilay y = "))
    c = a/b
    print(" x / y = ", c)
    print(" ")
    tanya ()
   
        

def tanya() :
    pil = input("Apakah Anda ingin mengulang ( y / t ) ? ")
    if pil == 'y' :
        kalkulator ()
    else :
        print(" Terima kasih sudah menggunakan program ini ")



   

    
        
        
