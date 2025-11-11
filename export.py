from ultralytics import YOLO
import torch

model = YOLO("runs/obb/DV_MBVSS2x3_add_malign_refrgb/weights/best.pt")

model.export(format="torchscript", ch=4, dynamic=True, simplify=True)
model.export(format="onnx", ch=4, simplify=True, opset=24)

# torch.onnx.export(
#     model.model,
#     (torch.randn(1, 4, 640, 640),),
#     "./best.onnx",
#     verbose=True,
#     opset_version=24,
# )
