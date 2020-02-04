from os import listdir,system
def encode ():
    try:
        r1 = "\x1b[31;1;"
        r2 = "\x1b[32;1;"
        r3 = "\x1b[33;1;"
        r4 = "\x1b[34;1;"
        r5 = "\x1b[35;1;"
        r6 = "\x1b[36;1;"
        r0 = "\x1b[30;1;"
        o = "\x1b[0m"
        ss = ""
        tt = [ff for ff in listdir () if not ff.startswith (".") and ff.endswith (".py")]
        tt.remove ("start.py")
        uu = "\t"+r1+"7mfile tidak ditemukan"+o
        d = (KeyboardInterrupt,EOFError)
        d1 = "\n"+r2+"4;3mthanks gan"+o
        if len (tt) == 0:
            exit (r1+";3mtidak terdapat file python disini\nsilahkan tambahkan file dulu"+o)
        for ii in range (len (tt)):
            if ii < 9:
                ss = "0"
            else:
                ss = ""
            print (r0+"m# "+r4+"m["+r6+"m"+ss+str (ii+1)+r4+"m] "+r2+"m"+tt[ii]+o)
        print ()
        while True:
            try:
                fil = str (input (r3+"7mnama file :"+o+r6+"m "))
            except d:
                exit (d1)
            if fil.isnumeric ():
                if not int (fil)-1 in range (len (tt)):
                    print (uu)
                    continue
                else:
                    fil = tt [int (fil)-1]
                    with open (fil,"r") as aa:
                        f1 = aa.read ()
                    break
            elif fil in tt:
                with open (fil,"r") as aa:
                    f1 = aa.read ()
                break
            else:
                print (uu)
                continue
        # fil adalah nama file
        # f1 adalah isi file
        # uu , aa , tt , ss
        # >>>>>> method
        vv = ""
        met = "base16 base32 base64 base85 ascii85 bz2 zlib lzma lzma2 combo1 combo2".split ()
        for ii in range (len (met)):
            if ii < 9:
                vv = "0"
            else:
                vv = ""
            print (r0+"m# "+r5+"m["+r3+"m"+vv+str (ii+1)+r5+"m] "+r6+"m"+met [ii]+o)
        print ()
        while True:
            try:
                print (r0+";7m>>>"+o+r2+";7m"+fil+o)
                m1 = int (input (r3+";7mpilih method :"+o+r6+"m "))
            except d:
                exit (d1)
            except (ValueError):
                print ("\t"+r1+";7mmasukan angka cuk"+o)
                continue
            else:
                if not m1-1 in range (len (met)):
                    print ("\t"+r1+";7mpilih sesuai pilihan cuk"+o)
                    continue
                else:
                    try:
                        o1 = str (input (r3+";7moutput file :"+o+r6+"m "))
                        if o1 == fil:
                            exit (r1+";7mtidak bisa mengencrypt file yang sama"+o)
                        elif o1 in tt:
                            try:
                                print (r3+";3mfile itu sudah ada sebelumnya\napakah kamu ingin melanjutkan [y/n]"+o)
                                o2 = str (input (r3+";7m>>>"+o+r6+"m ")).lower ()
                                if o2 != "y":
                                    exit (d1)
                            except d:
                                exit (d1)
                    except d:
                        exit (d1)
                    m2 = "b16 b32 b64 b85 a85 z2 zlib lzma lzma1 allb allc".split ()
                    system ("python .en.py "+m2 [m1-1]+" "+fil+" > "+o1)
                    print (r6+";7m done bosku"+r2+";7m output "+o1+o)
                    break
                    
                    
    except d:
        exit (d1)
system ("clear")
print (b'\x1b[32;1m \xe2\x96\x88\xe2\x96\x80\xe2\x96\x84 \xe2\x96\x80\xe2\x96\x84\xe2\x96\x91\xe2\x96\x84\xe2\x96\x80 \xe2\x96\x80\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x91 \xe2\x96\x84\xe2\x96\x80\xe2\x96\x84 \xe2\x96\x88\xe2\x96\x84\xe2\x96\x91\xe2\x96\x88\n \xe2\x96\x88\xe2\x96\x91\xe2\x96\x88 \xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x91\xe2\x96\x91 \xe2\x96\x91\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x88\xe2\x96\x80\xe2\x96\x84 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x91\xe2\x96\x80\xe2\x96\x88\n \xe2\x96\x88\xe2\x96\x80\xe2\x96\x91 \xe2\x96\x91\xe2\x96\x91\xe2\x96\x80\xe2\x96\x91\xe2\x96\x91 \xe2\x96\x91\xe2\x96\x80\xe2\x96\x91 \xe2\x96\x80\xe2\x96\x91\xe2\x96\x80 \xe2\x96\x91\xe2\x96\x80\xe2\x96\x91 \xe2\x96\x80\xe2\x96\x91\xe2\x96\x91\xe2\x96\x80\x1b[0m\x1b[36;1m\n==============================\x1b[0m\x1b[35;1m\n# \x1b[33;1mauthor   : \x1b[32;1mgumball watterson\x1b[35;1m\n# \x1b[33;1mcountry  : \x1b[32;1mindonesia\x1b[35;1m\n# \x1b[33;1mreligion : \x1b[32;1mislam\x1b[0m\n\x1b[36;1m==============================\x1b[0m'.decode ())
encode ()
