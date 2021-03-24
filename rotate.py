from PIL import Image

coin = Image.open('Image/SingleCoinTest.png')
cn = coin.rotate(10)
cn.show()