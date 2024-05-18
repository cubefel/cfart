from mcpi.minecraft import Minecraft
from mcpi import block
from PIL import Image


mc = Minecraft.create()
playerPos = mc.player.getTilePos()


image_path = "CHANGEIT.png"
image = Image.open(image_path)


image = image.resize((100, 100))


pixels = list(image.getdata())


color_mapping = {
    (0, 0, 0): 234,  # Black
    (0, 0, 255): 230,  # Blue
    (0, 255, 0): 224,  # Lime
    (0, 255, 255): 222,  # Light Blue
    (255, 0, 0): 233,  # Red
    (255, 0, 255): 221,  # Pink
    (255, 255, 0): 223,  # Yellow
    (255, 255, 255): 219,  # White
}

for y in range(image.height):
    for x in range(image.width):
        r, g, b = pixels[y * image.width + x]
        closest_color = min(color_mapping, key=lambda c: sum(abs(x - y) for x, y in zip(c, (r, g, b))))
        block_color = color_mapping[closest_color]
        mc.setBlock(playerPos.x + x, playerPos.y, playerPos.z + y, block_color,1)
