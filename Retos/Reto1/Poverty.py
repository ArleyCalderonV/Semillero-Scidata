def leerArchivo():
    archivo = open("Poverty.csv", "r")
    linea = archivo.readline()
    primerRegistro = True
    numeroMenor = [0, 0, 0, 0, 0]
    numeroMayor = [0, 0, 0, 0, 0]
    countryMayor = [0, 0, 0, 0, 0]
    countryMenor = [0, 0, 0, 0, 0]
    while linea != "":

        linea = archivo.readline()
        linea = linea.rstrip()

        lista = linea.split(",")
        if len(lista) == 6:
            lista.insert(1,0)
        try:

            if primerRegistro:
                numeroMenor[0] = int(lista[2])
                numeroMayor[0] = int(lista[2])
                numeroMenor[1] = int(lista[3])
                numeroMayor[1] = int(lista[3])
                numeroMenor[2] = int(lista[4])
                numeroMayor[2] = int(lista[4])
                numeroMenor[3] = int(lista[5])
                numeroMayor[3] = int(lista[5])
                numeroMenor[4] = int(lista[6])
                numeroMayor[4] = int(lista[6])
                countryMayor[0] = lista[0]
                countryMayor[1] = lista[0]
                countryMayor[2] = lista[0]
                countryMayor[3] = lista[0]
                countryMayor[4] = lista[0]

                primerRegistro = False
            else:
                if numeroMenor[0] > int(lista[2]):
                    numeroMenor[0] = int(lista[2])
                    countryMenor[0] = lista[0]

                if numeroMayor[0] < int(lista[2]):
                    numeroMayor[0] = int(lista[2])

                if numeroMenor[1] > int(lista[3]):
                    numeroMenor[1] = int(lista[3])
                    countryMenor[1] = lista[0]

                if numeroMayor[1] < int(lista[3]):
                    numeroMayor[1] = int(lista[3])

                if numeroMenor[2] > int(lista[4]):
                    numeroMenor[2] = int(lista[4])
                    countryMenor[2] = lista[0]

                if numeroMayor[2] < int(lista[4]):
                    numeroMayor[2] = int(lista[4])

                if numeroMenor[3] > int(lista[5]):
                    numeroMenor[3] = int(lista[5])
                    countryMenor[3] = lista[0]

                if numeroMayor[3] < int(lista[5]):
                    numeroMayor[3] = int(lista[5])

                if numeroMenor[4] > int(lista[6]):
                    numeroMenor[4] = int(lista[6])
                    countryMenor[4] = lista[0]

                if numeroMayor[4] < int(lista[6]):
                    numeroMayor[4] = int(lista[6])

        except exception:
            print("Validar")
        linea = archivo.readline()

    print(countryMenor[0], numeroMenor[0], countryMayor[0], numeroMayor[0])
    print(countryMenor[1], numeroMenor[1], countryMayor[1], numeroMayor[1])
    print(countryMenor[2], numeroMenor[2], countryMayor[2], numeroMayor[2])
    print(countryMenor[3], numeroMenor[3], countryMayor[3], numeroMayor[3])
    print(countryMenor[4], numeroMenor[4], countryMayor[4], numeroMayor[4])

    archivo.close()


leerArchivo()
