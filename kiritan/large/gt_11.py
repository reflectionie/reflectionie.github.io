import os

# 获取当前脚本所在的文件夹路径
current_folder = os.path.dirname(os.path.abspath(__file__))

# 列出当前文件夹中的所有文件
all_files = [f for f in os.listdir(current_folder) if os.path.isfile(os.path.join(current_folder, f))]

# 遍历所有文件并重命名
i = 0
for old_filename in all_files:
    # 构建旧文件的完整路径
    old_file_path = os.path.join(current_folder, old_filename)
    
    # 构建新文件名（在文件名前面添加"new_"前缀）
    new_filename = f"gt_{i}.wav"
    i += 1
    # 构建新文件的完整路径
    new_file_path = os.path.join(current_folder, new_filename)
    
    # 重命名文件
    os.rename(old_file_path, new_file_path)
    print(f"重命名文件: {old_filename} -> {new_filename}")
