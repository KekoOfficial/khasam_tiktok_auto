import os

def cortar_video(input_file, duracion=600):
    os.makedirs("../output", exist_ok=True)
    comando = f'ffmpeg -i "{input_file}" -c copy -map 0 -segment_time {duracion} -f segment ../output/parte_%03d.mp4'
    os.system(comando)
    print("✅ Video cortado automáticamente")