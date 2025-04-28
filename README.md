# 音频文件转换为M4A (ALAC)工具

这是一个用Python编写的批量音频文件转换工具，可以将各种音频格式无损转换为M4A (ALAC)格式。ALAC是Apple开发的无损音频编解码器，特别适合在Apple设备上使用。

## 功能特点

- 批量转换音频文件为M4A (ALAC)格式
- 保持音频质量的无损转换
- 自动跳过处理失败的文件
- 详细的转换进度和结果报告

## 环境要求

- Python 3.x
- FFmpeg（需要预先安装）

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

```bash
python m4a.py 输入文件夹路径 输出文件夹路径
```

### 示例

```bash
python m4a.py ./input_music ./output_m4a
```

## 注意事项

1. 确保系统已安装FFmpeg
2. 输入文件夹可以包含多种音频格式
3. 输出文件夹会自动创建（如果不存在）
4. 转换过程中会显示详细进度

## 许可证

MIT License