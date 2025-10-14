import os#импорт модуля os для работы с ОС
import shutil#импорт модуля shutil для перемещения файла
from PIL import Image#импорт модуля Pil для рабооты с изображением
source_folder = input("Введите путь к папке с фотографиями: ")
move_folder = input("Введите путь к папке для перемещения фотографий: ")
bw_folder = input("Введите путь к папке для черно-белых изображений: ")
#эти три строки отвечают за нахождение файла с фотографиями а две последующих для перемещения и сохранения фотографии
os.makedirs(move_folder, exist_ok=True)
os.makedirs(bw_folder, exist_ok=True)
#создавание папок если их нет
for filename in os.listdir(source_folder):#перебираем все файлы в папке
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):#проверяем расширение файла, чтобы обрабатывать только изображения
        src_path = os.path.join(source_folder, filename)#полный путь к исходному картинке
        dest_path = os.path.join(move_folder, filename)#полный путь куда переместить картинку
        shutil.move(src_path, dest_path)#перенос картинки
        print(f"Переместили {filename}") #вывод сообщения, что картинка перемещена
        with Image.open(dest_path) as img:#открывает изображение по пути
            bw_img = img.convert('L')#конвертирует изображение в чб
            bw_img.save(os.path.join(bw_folder, filename))#cохраняет чб картинку с тем же именем
            print(f"Создали черно-белое {filename}")#вывод сообщения что чб картинка создана 
print("Готово!")