import os
from huggingface_hub import snapshot_download

# 設定下載目錄 (專案底下的 models 資料夾)
MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")

print(f"🚀 開始下載模型至: {MODEL_DIR}")
print("這可能需要一些時間，取決於您的網速...")

# 1. 下載 SDXL-Turbo
print("\n⬇️ [1/2] 下載 StabilityAI/SDXL-Turbo...")
sdxl_path = snapshot_download(
    repo_id="stabilityai/sdxl-turbo",
    local_dir=os.path.join(MODEL_DIR, "sdxl-turbo"),
    local_dir_use_symlinks=False,  # 確保是真實檔案，不是連結
    # allow_patterns=["*.fp16.safetensors", "*.json", "model_index.json", "scheduler_config.json", "vocab.json", "merges.txt"]
)
print("✅ SDXL-Turbo 下載完成。")

# 2. 下載 LTX-Video
print("\n⬇️ [2/2] 下載 Lightricks/LTX-Video...")
ltx_path = snapshot_download(
    repo_id="Lightricks/LTX-Video",
    local_dir=os.path.join(MODEL_DIR, "ltx-video"),
    local_dir_use_symlinks=False,
    # allow_patterns=["*.safetensors", "*.json", "*.txt"]
)
print("✅ LTX-Video 下載完成。")

print("\n🎉 所有模型準備就緒！")