# ComfyUI-AnimaPromptFormatter

一个用于格式化 [Anima模型](https://huggingface.co/circlestone-labs/Anima) 提示词的 ComfyUI 自定义节点。

与 SDXL 模型（如 IllustrousXL 或 NoobAI XL）不同，[Anima模型 对空格、逗号和换行符非常敏感](https://huggingface.co/circlestone-labs/Anima/discussions/57#6997ae1d9ab163d4a7a5121e)。我弄这个节点是为了保持在 NoobAI 模型上的敲提示词习惯。

## 格式化规则

1. 移除所有换行符（`\n`、`\r`）
2. 保证每个逗号后面只有一个空格
3. 移除逗号前面的空格
4. 过滤连续逗号中的空标签

示例:

**输入**：
```
tag1,tag2,  tag3
,tag4,,tag5
```

**输出**：
```
tag1, tag2, tag3, tag4, tag5
```

## 用法
这就是个文本输入节点，把输出连到CLIPTextEncode就好了
