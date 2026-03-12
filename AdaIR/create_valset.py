import os
import random
import shutil

# ===== 路径配置 =====
train_root = "/data/CVPR26_AiO/Train"
val_root = "/data/CVPR26_AiO/Val"

# 每个任务抽取多少张
num_samples = 50

# 固定随机种子，保证可复现
random.seed(42)

# 任务列表：自动读取 Train 下所有子文件夹
tasks = [d for d in os.listdir(train_root) if os.path.isdir(os.path.join(train_root, d))]

for task in tasks:
    gt_dir = os.path.join(train_root, task, "GT")
    lq_dir = os.path.join(train_root, task, "LQ")

    if not os.path.exists(gt_dir) or not os.path.exists(lq_dir):
        print(f"Skip {task}: missing GT or LQ")
        continue

    # 获取 GT 和 LQ 共同拥有的文件名
    gt_files = set(f for f in os.listdir(gt_dir) if os.path.isfile(os.path.join(gt_dir, f)))
    lq_files = set(f for f in os.listdir(lq_dir) if os.path.isfile(os.path.join(lq_dir, f)))
    common_files = sorted(list(gt_files & lq_files))

    if len(common_files) < num_samples:
        print(f"Task {task}: only {len(common_files)} pairs found, less than {num_samples}")
        selected_files = common_files
    else:
        selected_files = random.sample(common_files, num_samples)

    # 创建 Val 目录结构
    val_gt_dir = os.path.join(val_root, task, "GT")
    val_lq_dir = os.path.join(val_root, task, "LQ")
    os.makedirs(val_gt_dir, exist_ok=True)
    os.makedirs(val_lq_dir, exist_ok=True)

    # 复制图片
    for fname in selected_files:
        shutil.move(os.path.join(gt_dir, fname), os.path.join(val_gt_dir, fname))
        shutil.move(os.path.join(lq_dir, fname), os.path.join(val_lq_dir, fname))

    print(f"{task}: copied {len(selected_files)} image pairs to Val")