import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

def generar_titulo(titulo_base, cap, hashtags):
    return f"{titulo_base} #{cap} {hashtags}"

def subir_videos(titulo_base, config):
    hashtags = config["hashtags"]
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=../profile")  # Guarda sesión
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.tiktok.com/upload")
    time.sleep(10)

    videos = sorted(os.listdir("../output"))
    contador = 0
    limite = random.randint(config["min_videos_bloque"], config["max_videos_bloque"])

    for i, video in enumerate(videos):
        path = os.path.abspath(f"../output/{video}")
        cap = i + 1
        print(f"Subiendo {video}")

        upload = driver.find_element(By.XPATH, "//input[@type='file']")
        upload.send_keys(path)
        time.sleep(8)

        desc = driver.find_element(By.XPATH, "//div[@role='textbox']")
        desc.clear()
        desc.send_keys(generar_titulo(titulo_base, cap, hashtags))
        time.sleep(3)

        post = driver.find_element(By.XPATH, "//button[contains(., 'Post')]")
        post.click()
        print(f"Publicado #{cap}")

        espera = random.randint(config["min_delay"], config["max_delay"])
        time.sleep(espera)

        contador += 1
        if contador >= limite:
            descanso = random.randint(config["min_descanso"], config["max_descanso"])
            print(f"Descanso largo: {descanso} segundos")
            time.sleep(descanso)
            contador = 0
            limite = random.randint(config["min_videos_bloque"], config["max_videos_bloque"])