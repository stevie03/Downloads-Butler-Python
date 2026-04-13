import os
import shutil
import time  

folder_path = r"C:\Users\steve\Downloads"

def rendezes():
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            
            try:
                file_extension = os.path.splitext(filename)[1].lower()
                
                if file_extension in ['.jpg', '.jpeg', '.png', '.gif']:
                    destination_folder = os.path.join(folder_path, 'Képek')
                elif file_extension in ['.pdf', '.docx', '.txt', ".doc"]:
                    destination_folder = os.path.join(folder_path, 'Dokumentumok')
                elif file_extension in ['.mp3', '.wav']:
                    destination_folder = os.path.join(folder_path, 'Zene')
                else:
                    destination_folder = os.path.join(folder_path, 'Egyéb')

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                shutil.move(file_path, os.path.join(destination_folder, filename))
                
            except Exception as e:
                print("Hiba történt a fájl rendezése közben:", e)

while True:
    rendezes()
    time.sleep(7200)