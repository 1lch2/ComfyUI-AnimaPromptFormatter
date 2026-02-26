"""
AnimaPromptFormatter - ComfyUI 节点实现

该模块定义了提示词格式化节点，用于在ComfyUI中格式化图像生成模型的提示词。
"""

from .utils import format_prompt


class AnimaPromptFormatter:
    """
    提示词格式化节点
    
    该节点接收多行字符串输入，按照特定规则格式化后输出。
    
    格式化规则:
    1. 移除所有换行符
    2. 逗号后必须有且仅有一个空格
    3. 逗号前不能有空格
    4. 过滤空标签（连续逗号产生的空内容）
    
    Attributes:
        INPUT_TYPES: 定义节点的输入类型
        RETURN_TYPES: 定义节点的输出类型
        FUNCTION: 指定执行的方法名
        CATEGORY: 节点在菜单中的分类
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        定义节点的输入类型
        
        Returns:
            dict: 包含必需输入参数的字典
        """
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "display": "prompt"
                }),
            }
        }
    
    # 定义返回类型（输出一个字符串）
    RETURN_TYPES = ("STRING",)
    
    # 定义输出名称
    RETURN_NAMES = ("formatted_text",)
    
    # 指定执行的方法名
    FUNCTION = "format"
    
    # 节点在菜单中的分类
    CATEGORY = "prompt/formatter"
    
    # 节点输出不使用张量
    OUTPUT_NODE = False
    
    def format(self, text):
        """
        执行提示词格式化
        
        Args:
            text: 原始提示词字符串
            
        Returns:
            tuple: 包含格式化后字符串的元组
        """
        formatted_text = format_prompt(text)
        return (formatted_text,)
