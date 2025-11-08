from ultralytics import YOLO
import torch

# device = 'cuda' if torch.cuda.is_available() else 'cpu'
# m = m.to(device)

model = YOLO(
    "ultralytics/cfg/mamba_end_obb/yolov8s_MBVSS2x3_add_malign_refrgb_new.yaml"
)
# build from YAML and transfer weights   通过模型配置和预训练模型将预训练模型权重转到模型上

model.model = torch.compile(model.model, "max-autotune")

# Train the model
results = model.train(
    data="/root/RGFNet/datasets/yolo-mif/data.yaml",
    epochs=150,
    imgsz=640,
    device=0,
    workers=16,
    batch=8,
    scale=0.0,
    mosaic=0.0,
    save_period=25,
    cache="ram",
    deterministic=False,
    name="DV_MBVSS2x3_add_malign_refrgb",
)


# 开始训练，注意data参数是我们的数据集配置，imgsz在训练和测试时都需要指定6363  save_period=5,
