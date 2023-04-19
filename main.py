def z1():
    from PIL import Image, ImageFilter
    import os
    p = "pictures"
    os.makedirs("resultat")
    for file in os.listdir(p):
        o = os.path.join(p,file)
        img = Image.open(o)
        n_img = img.filter(ImageFilter.CONTOUR)
        result1 = os.path.join("resultat",file)
        n_img.save(result1)

    print("сделано")

def z2():
    from PIL import Image, ImageFilter
    import os
    p = "pictures"
    os.makedirs("resultat_1")
    for file in os.listdir(p):
         if file.endswith(".jpg") or file.endswith(".png"):
            o = os.path.join(p,file)
            img = Image.open(o)
            n_img = img.filter(ImageFilter.CONTOUR)
            result1 = os.path.join("resultat_1",file)
            n_img.save(result1)

    print("сделано")

def z3():
    import csv
    with open('задача.csv', newline='') as cvsfile:
        reader = csv.reader(cvsfile,delimiter=';')
        next(reader)
        k = 0
        l = []
        for row in reader:
            product = row[0]
            kolvo = int(row[1])
            pr = int(row[2])
            stoim = kolvo * pr
            k += stoim
            l.append(f"{product} - {kolvo} шт.за {pr} руб.")
        print("Нужно купить:")
        for item in l:
            print(item)
        print(f"Итоговая сумма: {k} руб.")

