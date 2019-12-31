# script inversion_image_pgm.py
import imghdr, struct

print("Inversion d'une image PGM en mode binaire à 256 niveaux de gris\n")

NomFichierSource = 'Socotra_dragon_tree.pgm'
NomFichierDestination = 'imageInverse.pgm'

print('Fichier source :',NomFichierSource)
print('Fichier destination :',NomFichierDestination)

def Inversion(octet):
    # cette fonction fait une inversion du niveau de gris
    # 0 (noir)    -> 255 (blanc)
    # 255 (blanc) -> 0 (noir)
    return 255-octet

if imghdr.what(NomFichierSource)=='pgm':	# test du format de l'image
    FichierSource = open(NomFichierSource,'rb')
    TailleFichier = len(FichierSource.read())
    print('\nTaille du fichier (en octets) :',TailleFichier)

    Largeur = int(input('Largeur de l\'image (en pixels) ? '))
    Hauteur = int(input('Hauteur de l\'image (en pixels) ? '))
    NbPixel = Largeur*Hauteur

    TailleEntete = TailleFichier - Largeur*Hauteur

    FichierSource.seek(0)

    # extraction de l'en-tête
    # la variable Entete est une chaîne d'octets (type bytes)
    Entete = FichierSource.read(TailleEntete)

    # extraction des données
    # Data est une liste de nombre entiers (type list)
    # la fonction int() retourne le contenu d'un octet sous forme d'un entier
    
    Data = [int(i) for i in FichierSource.read()]	# compréhension de listes

    FichierSource.close()

    if NbPixel == len(Data):
        print('Nombre de pixels :',Largeur*Hauteur)
        print("Nombre d'octets de données :",len(Data))
        print("Taille de l'en-tête :",TailleEntete)

        FichierDestination = open(NomFichierDestination,'wb')
        # écriture de l'en-tête du fichier destination
        FichierDestination.write(Entete)

        # écriture des données du fichier destination
        for i in Data:
            # conversion de type : int en bytes            
            FichierDestination.write(struct.pack('B',Inversion(i)))

        FichierDestination.close()
        print('Travail terminé !')

    else:
        print('Erreur dans la saisie des données !')

else:
    print("Ce n'est pas une image PGM !")
