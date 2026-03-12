import torch
from fvcore.nn import FlopCountAnalysis, parameter_count_table
from net.model import BioIR

device = "cuda" if torch.cuda.is_available() else "cpu"

model = BioIR().to(device)
model.eval()

# 这里要换成你真实的输入尺寸
# 例如 batch=1, channel=3, H=256, W=256
dummy_input = torch.randn(1, 3, 256, 256).to(device)

with torch.no_grad():
    flops = FlopCountAnalysis(model, dummy_input)

print("Total FLOPs:", flops.total())
print(parameter_count_table(model))
print(flops.by_module())