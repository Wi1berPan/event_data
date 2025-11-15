import json
import os

def add_event_boundary_frames():
    """
    为timerft.json文件中的每个视频添加event_boundary_frames关键字
    """
    json_file_path = '/data/P_Yih/event_data/videoespresso.json'
    
    # 检查文件是否存在
    if not os.path.exists(json_file_path):
        print(f"错误：找不到文件 {json_file_path}")
        return False
    
    try:
        # 读取JSON文件
        print("正在读取JSON文件...")
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 检查数据是否为列表
        if not isinstance(data, list):
            print("错误：JSON文件内容不是列表格式")
            return False
        
        # 处理每个视频对象
        total_items = len(data)
        print(f"找到 {total_items} 个视频对象")
        
        for i, item in enumerate(data):
            # 检查是否为字典
            if isinstance(item, dict):
                # 添加event_boundary_frames关键字，值为空列表
                item['event_boundary_frames'] = []
            
            # 显示进度
            if (i + 1) % 100 == 0 or (i + 1) == total_items:
                print(f"已处理 {i + 1}/{total_items}")
        
        # 保存修改后的数据
        print("正在保存修改后的JSON文件...")
        # 为了安全，先保存到临时文件
        temp_file = json_file_path + '.temp'
        with open(temp_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        # 替换原文件
        os.replace(temp_file, json_file_path)
        
        print(f"成功完成！已为 {total_items} 个视频添加了event_boundary_frames关键字")
        return True
        
    except json.JSONDecodeError:
        print("错误：JSON文件格式无效")
        return False
    except Exception as e:
        print(f"处理过程中发生错误：{str(e)}")
        return False

if __name__ == "__main__":
    add_event_boundary_frames()