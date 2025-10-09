from PIL import Image


input_path = r'Практика Малленом Системс\Проектирование и разработка информационных систем\Report\Картинки\whale.png'
output_path = r'Практика Малленом Системс\Проектирование и разработка информационных систем\Report\КартинкиEXP\whale.png'


img = Image.open(input_path)


shift_x, shift_y = 50, 50

bg = Image.new('RGB', (img.width + shift_x, img.height + shift_y), (255, 255, 255))

bg.paste(img, (shift_x, shift_y))


bw_img = bg.convert('L')


bw_img.save(output_path)
bw_img.show()