# ComfyUI-AnimaPromptFormatter

A ComfyUI custom node for formatting [Anima](https://huggingface.co/circlestone-labs/Anima) prompts.

Unlike SDXL models like IllustrousXL or NoobAI XL, [Anima is sensitive to whitespaces, commas and line breaks](https://huggingface.co/circlestone-labs/Anima/discussions/57#6997ae1d9ab163d4a7a5121e). I create this custom node so I can keep my prompting habits on NoobAI models.

## Formatting Rules

1. Removes all line breaks (`\n`, `\r`)
2. Ensures exactly one space after each comma
3. Removes spaces before commas
4. Filters empty tags from consecutive commas

## Example

**Input**:
```
tag1,tag2,  tag3
,tag4,,tag5
```

**Output**:
```
tag1, tag2, tag3, tag4, tag5
```
