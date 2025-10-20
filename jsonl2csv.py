import jsonlines
import csv

def gsm8k_jsonl_to_csv(jsonl_input_path, csv_output_path):
    # 1. 打开 JSONL 文件和 CSV 文件
    with jsonlines.open(jsonl_input_path, "r", encoding="utf-8") as jsonl_file, \
         open(csv_output_path, "w", newline="", encoding="utf-8") as csv_file:
        
        # 2. 定义 CSV 列名（对应上述结构）
        csv_writer = csv.DictWriter(csv_file, fieldnames=["question", "answer", "final_answer"])
        csv_writer.writeheader()  # 写入列名
        
        # 3. 逐行处理数据
        for line in jsonl_file:
            # 提取核心字段
            question = line.get("question", "").strip()  # 问题（空值默认空字符串）
            answer = line.get("answer", "").strip()      # 完整解答
            
            # 提取 final_answer：拆分 answer 中 "#### " 后的内容（如示例中的 45）
            if "#### " in answer:
                final_answer = answer.split("#### ")[-1].strip()
            else:
                final_answer = ""  # 若格式异常，默认空值
            
            # 4. 写入 CSV 行
            csv_writer.writerow({
                "question": question,
                "answer": answer,
                "final_answer": final_answer
            })

# -------------------------- 请修改这里的文件路径 --------------------------
# 输入：你的 gsm8k.jsonl 文件路径（如本地文件放在同文件夹，直接写文件名）
INPUT_JSONL_PATH = "gsm8k.jsonl"  
# 输出：你想保存的 CSV 文件名（如 gsm8k_output.csv）
OUTPUT_CSV_PATH = "gsm8k_output.csv"  
# --------------------------------------------------------------------------

# 执行转换
gsm8k_jsonl_to_csv(INPUT_JSONL_PATH, OUTPUT_CSV_PATH)
print(f"转换完成！CSV 文件已保存到：{OUTPUT_CSV_PATH}")
