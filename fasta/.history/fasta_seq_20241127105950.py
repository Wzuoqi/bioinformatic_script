#!/usr/bin/env python3
import sys
import argparse

def extract_sequences(input_file, output_file, keyword, case_sensitive=False):
    """
    从FASTA文件中提取包含指定关键词的序列

    参数:
        input_file (str): 输入FASTA文件的路径
        output_file (str): 输出FASTA文件的路径
        keyword (str): 用于筛选的关键词
        case_sensitive (bool): 是否区分大小写，默认为False
    """

    try:
        with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
            write_sequence = False
            sequence_count = 0

            for line in fin:
                if line.startswith('>'):
                    # 处理序列标题行
                    header = line.strip()
                    if not case_sensitive:
                        write_sequence = keyword.lower() in header.lower()
                    else:
                        write_sequence = keyword in header

                    if write_sequence:
                        fout.write(header + '\n')
                        sequence_count += 1

                elif write_sequence:
                    # 写入序列行
                    fout.write(line)

            return sequence_count

    except FileNotFoundError:
        print(f"错误：找不到输入文件 '{input_file}'")
        return 0
    except Exception as e:
        print(f"处理文件时发生错误：{str(e)}")
        return 0

def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='从FASTA文件中提取包含指定关键词的序列')
    parser.add_argument('-i', '--input', required=True, help='输入FASTA文件路径')
    parser.add_argument('-o', '--output', required=True, help='输出FASTA文件路径')
    parser.add_argument('-k', '--keyword', required=True, help='要搜索的关键词')
    parser.add_argument('-c', '--case-sensitive', action='store_true',
                        help='是否区分大小写（默认不区分）')

    # 解析命令行参数
    args = parser.parse_args()

    # 执行序列提取
    count = extract_sequences(args.input, args.output, args.keyword,
                            case_sensitive=args.case_sensitive)

    # 输出结果
    if count > 0:
        print(f"成功提取了 {count} 条包含关键词 '{args.keyword}' 的序列")
        print(f"结果已保存到文件：{args.output}")
    else:
        print(f"未找到包含关键词 '{args.keyword}' 的序列")

if __name__ == "__main__":
    main()