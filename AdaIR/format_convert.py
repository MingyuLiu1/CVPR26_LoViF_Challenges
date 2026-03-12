import os
from PIL import Image

input_dir = "/workspace/AdaIR/vis_results/training_from_scratch_epoch140zaio/"  
output_dir = "/workspace/AdaIR/vis_results/training_from_scratch_epoch140_converted/" 
os.makedirs(output_dir, exist_ok=True)

save_kwargs = dict(format="JPEG", quality=96, subsampling=0, optimize=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff")):
        img_path = os.path.join(input_dir, filename)

        img = Image.open(img_path)

        if img.mode != "RGB":
            img = img.convert("RGB")

        # 输出统一为 jpg
        out_name = os.path.splitext(filename)[0] + ".jpg"
        out_path = os.path.join(output_dir, out_name)

        img.save(out_path, **save_kwargs)

        print("Saved:", out_path)
