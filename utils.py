"""
AnimaPromptFormatter - 格式化工具函数

该模块提供提示词格式化功能，用于处理图像生成模型的提示词。
"""


def format_prompt(prompt: str) -> str:
    """
    格式化提示词字符串
    
    处理步骤:
    1. 移除所有换行符 (\\n 和 \\r)
    2. 按逗号分割标签
    3. 清理每个标签（去除首尾空格）
    4. 过滤空标签
    5. 用标准格式重新连接（逗号+单空格）
    
    Args:
        prompt: 原始提示词字符串，可能包含多行和格式不一致的逗号分隔
        
    Returns:
        格式化后的单行提示词字符串，逗号后有且仅有一个空格
        
    Examples:
        >>> format_prompt("tag1,tag2,  tag3\\n,tag4")
        'tag1, tag2, tag3, tag4'
        
        >>> format_prompt("tag1 , tag2,,tag3")
        'tag1, tag2, tag3'
        
        >>> format_prompt("")
        ''
    """
    # 处理空字符串或None
    if not prompt:
        return ""
    
    # 步骤1: 移除所有换行符
    text = prompt.replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ')
    
    # 步骤2: 按逗号分割
    tags = text.split(',')
    
    # 步骤3: 清理每个标签（去除首尾空格）
    cleaned_tags = [tag.strip() for tag in tags]
    
    # 步骤4: 过滤空标签
    non_empty_tags = [tag for tag in cleaned_tags if tag]
    
    # 步骤5: 用标准格式重新连接（逗号+单空格）
    formatted_text = ', '.join(non_empty_tags)
    
    return formatted_text
