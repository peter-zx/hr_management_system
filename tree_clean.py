import os

EXCLUDE = {"venv", "__pycache__", ".git", ".idea", ".vscode"}

def print_tree(start_path, prefix=""):
    items = sorted(os.listdir(start_path))
    for i, name in enumerate(items):
        path = os.path.join(start_path, name)
        if name in EXCLUDE or name.startswith("."):
            continue
        is_last = (i == len(items) - 1)
        print(f"{prefix}{'└── ' if is_last else '├── '}{name}")
        if os.path.isdir(path):
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(path, new_prefix)

print_tree(".")



#✅ 方式 B：用 Python 脚本输出干净的结构树（推荐）
#⚙️ 你只需运行下面这个 Python 脚本，它会自动排除 venv、pycache、.git、.idea 等垃圾目录，并打印结构：
