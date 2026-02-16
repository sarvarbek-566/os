import os
import shutil

def clear_temp():
    temp_folder = os.path.expandvars("%temp%")
    
    if os.path.exists(temp_folder):
        print(f"Tozalanmoqda: {temp_folder}")
        for item in os.listdir(temp_folder):
            item_path = os.path.join(temp_folder, item)
            try:
                if os.path.isfile(item_path):
                    os.remove(item_path)  # Fayl uchirish
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path, ignore_errors=True)  # Papka o‘chirish
            except:
                pass
    else:
        print(f"Papka topilmadi: {temp_folder}")
    
    print("Tozalash yakunlandi!")

if __name__ == "__main__":
    clear_temp()