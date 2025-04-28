import os
from pydub import AudioSegment
import argparse
import traceback # 导入 traceback 模块以便打印更详细的错误信息

def batch_convert_to_m4a_lossless(input_folder, output_folder):
    """
    批量将指定文件夹中的音频文件无损转换为 M4A (ALAC) 格式。

    Args:
        input_folder (str): 包含源音频文件的文件夹路径。
        output_folder (str): 保存转换后 M4A 文件的文件夹路径。
    """
    # 确保输出文件夹存在，如果不存在则创建
    if not os.path.exists(output_folder):
        print(f"创建输出文件夹: {output_folder}")
        os.makedirs(output_folder)
    else:
        print(f"输出文件夹已存在: {output_folder}")

    print(f"开始扫描输入文件夹: {input_folder}")
    converted_count = 0
    skipped_count = 0
    error_count = 0

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        input_filepath = os.path.join(input_folder, filename)

        # 检查是否是文件而不是文件夹
        if os.path.isfile(input_filepath):
            # 构建输出文件的路径，替换扩展名为 .m4a
            base_name, _ = os.path.splitext(filename)
            output_filename = f"{base_name}.m4a"
            output_filepath = os.path.join(output_folder, output_filename)

            print(f"\n正在处理文件: {filename}")

            try:
                # 加载音频文件
                # pydub 会自动检测格式
                print("  正在加载音频...")
                # 增加 ffmpeg 的日志级别，有助于调试
                AudioSegment.converter = "ffmpeg" # 明确指定使用 ffmpeg
                AudioSegment.ffmpeg = "ffmpeg"
                audio = AudioSegment.from_file(input_filepath)

                # 导出为 M4A 格式，使用 ALAC 无损编解码器
                print(f"  正在无损转换为 M4A (ALAC) 并导出到: {output_filepath}")
                # 使用 'alac' 编解码器进行无损转换
                # format='ipod' 仍然适用，因为它指定了 M4A 容器
                audio.export(output_filepath, format="ipod", codec="alac")
                print(f"  成功无损转换: {filename} -> {output_filename}")
                converted_count += 1

            except Exception as e:
                # 捕获并打印转换过程中可能出现的任何错误
                print(f"  转换文件 {filename} 时出错: {e}")
                # 打印详细的错误堆栈信息
                # traceback.print_exc()
                print(f"  跳过文件: {filename}")
                error_count += 1
                # 可以在这里添加更详细的错误记录逻辑，例如记录到日志文件

        else:
            print(f"  跳过文件夹: {filename}")
            skipped_count += 1

    print("\n--------------------")
    print("批量无损转换完成!")
    print(f"成功转换文件数: {converted_count}")
    print(f"跳过非文件数: {skipped_count}")
    print(f"转换失败文件数: {error_count}")
    print(f"转换后的 M4A (ALAC) 文件保存在: {output_folder}")
    print("--------------------")

if __name__ == "__main__":
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="批量将音频文件无损转换为 M4A (ALAC) 格式。")
    parser.add_argument("input_dir", help="包含源音频文件的输入文件夹路径。")
    parser.add_argument("output_dir", help="用于保存转换后 M4A 文件的输出文件夹路径。")

    # 解析命令行参数
    args = parser.parse_args()

    # 调用转换函数
    batch_convert_to_m4a_lossless(args.input_dir, args.output_dir)

