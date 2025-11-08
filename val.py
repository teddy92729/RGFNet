from ultralytics import YOLO

# Load a model
model = YOLO("ultralytics/cfg/mamba_end_obb/yolov8s_MBVSS2x3_add_malign_refrgb_new.yaml").load("runs/obb/DV_MBVSS2x3_add_malign_refrgb/weights/best.pt")

# Validate with a custom dataset  NMS非极大抑制的阈值
metrics = model.val(data="/root/RGFNet/datasets/yolo-mif/data.yaml", imgsz=640, batch=8, conf=0.05, iou=0.5, ch=4,
                    device=0, name="DV_MBVSS2x3_add_malig_refrgb", project = 'runs/val')

print('\n' + f"MAP50: {metrics.box.map50:.3f}   ", f"MAP75: {metrics.box.map75:.3f}   ", f"MAP: {metrics.box.map:.3f}" + '\n')