# Pillow 6.0.0
# importation du module Image de la librairie Pillow
from PIL import Image

# ouverture de l'image
img = Image.open('Socotra_dragon_tree.png')
# affichage de l'image
img.show()
# affichage de la taille de l'image (en pixels)
print(img.size)
# conversion au format PPM (en couleur) et enregistrement de l'image
img.save('Socotra_dragon_tree.ppm','PPM')
img.show()
# conversion en niveau de gris (pour obtenir le format PGM)
img0 = img.convert('L')
# enregistrement dans le fichier Socotra_dragon_tree.pgm
img0.save('Socotra_dragon_tree.pgm')
img0.show()

# retournement de l'image
img1 = img0.rotate(180)
# affichage et enregistrement de l'image retournée
img1.show()
img1.save('image_retourne.pgm')

# miroir horizontal
img2 = img0.transpose(Image.FLIP_LEFT_RIGHT)
img2.show()
img2.save('image_miroir_horizontal.pgm')

# miroir vertical
img3 = img0.transpose(Image.FLIP_TOP_BOTTOM)
img3.show()
img3.save('image_miroir_vertical.pgm')
