import os
import shutil

def clear_temp():
    # Faqat %temp% papkasi
    temp_folder = os.path.expandvars("%temp%")  # C:\Users\User\AppData\Local\Temp
    
    if os.path.exists(temp_folder):
        print(f"Tozalanmoqda: {temp_folder}")
        for item in os.listdir(temp_folder):
            item_path = os.path.join(temp_folder, item)
            try:
                if os.path.isfile(item_path):
                    os.remove(item_path)  # Fayl o‘chirish
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path, ignore_errors=True)  # Papka o‘chirish
            except:
                pass  # Xato bo‘lsa, e’tiborsiz o‘tamiz
    else:
        print(f"Papka topilmadi: {temp_folder}")
    
    print("Tozalash yakunlandi!")

if __name__ == "__main__":
    clear_temp()