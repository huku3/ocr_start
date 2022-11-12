from PIL import Image
import pyocr

tools = pyocr.get_available_tools()
tool = tools[0]


# toolがtessract
# print(tool)
# print(tool.get_name())


# img = Image.open("sparta_camp_en.png")
# img.show()
img = Image.open("sparta_camp_jp.png")

txt = tool.image_to_string(img, lang="eng+jpn", builder=pyocr.builders.TextBuilder())
# lang=engで英語

print(txt)
