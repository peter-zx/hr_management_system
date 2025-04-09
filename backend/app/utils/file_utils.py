import os

# 检查文件是否存在
def file_exists(filepath):
    return os.path.exists(filepath)

# 获取文件大小
def get_file_size(filepath):
    if file_exists(filepath):
        return os.path.getsize(filepath)
    return None

# 读取文件内容（如文本文件）
def read_file(filepath):
    if file_exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return None

# 删除文件
def delete_file(filepath):
    if file_exists(filepath):
        os.remove(filepath)
        return True
    return False
