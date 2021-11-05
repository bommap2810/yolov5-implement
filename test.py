from models.common import *
from models.experimental import *
from models.yolo import *

model = Model('models/yolov5s.yaml', ch=3, nc=None, anchors=None)
a = sum(p.numel() for p in model.parameters())
print(model)
print(a)