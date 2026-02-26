"""
AnimaPromptFormatter - ComfyUI 自定义节点包

该包提供提示词格式化功能，用于处理图像生成模型的提示词。

使用方法:
1. 将此文件夹放置在 ComfyUI/custom_nodes/ 目录下
2. 重启 ComfyUI
3. 在节点菜单中找到 "prompt/formatter" 分类下的 "Anima Prompt Formatter" 节点
"""

from .nodes import AnimaPromptFormatter

# 节点类映射 - 用于ComfyUI加载节点
NODE_CLASS_MAPPINGS = {
    "AnimaPromptFormatter": AnimaPromptFormatter
}

# 节点显示名称映射 - 用于在UI中显示友好的名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "AnimaPromptFormatter": "Anima Prompt Formatter"
}

# 导出变量，供ComfyUI加载
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# 版本信息
__version__ = "1.0.0"
__author__ = "Anima"
__description__ = "A ComfyUI custom node for formatting image generation prompts"
