# script camembert.py
# Python 2.7 & Python 3
# Pillow 6.0.0
from PIL import Image,ImageDraw

# création d'une image 400x400 (fond blanc)
img = Image.new("RGB",(400,400),"#FFFFFF")

# création d'un objet Draw
dessin = ImageDraw.Draw(img)

# dessine un arc partiel et le remplit
dessin.pieslice((50,50,350,350),0,60,fill="blue")
dessin.pieslice((50,50,350,350),60,150,fill="gray")
dessin.pieslice((50,50,350,350),150,360,fill="red")

# dessine du texte
dessin.text((50,20),"camembert 2D",fill="red")

img.save("camembert.png","PNG")
img.show()
