from PIL import Image
import os

def convert_webp_to_png():
    input_folder = os.path.join(os.getcwd(), "input")
    output_folder = os.path.join(os.getcwd(), "output")

    if not os.path.exists(input_folder):
        os.makedirs(input_folder)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".webp"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".png")

            try:
                with Image.open(input_path) as img:
                    if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
                        img.save(output_path, "PNG")
                        print(f"Converted: {filename} -> {output_path}")
                    else:
                        img = img.convert("RGB")
                        img.save(output_path, "JPEG")
                        print(f"Converted: {filename} -> {output_path}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

convert_webp_to_png()
