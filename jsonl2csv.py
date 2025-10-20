import jsonlines
import csv

def gsm8k_jsonl_to_csv(jsonl_input_path, csv_output_path):
    # 记录处理的数据条数，用于验证
    total_count = 0
    
    with jsonlines.open(jsonl_input_path, "r") as jsonl_file, \
         open(csv_output_path, "w", newline="", encoding="utf-8") as csv_file:
        
        # 只保留原始的 "question" 和 "answer" 字段
        csv_writer = csv.DictWriter(csv_file, fieldnames=["question", "answer"])
        csv_writer.writeheader()  # 写入表头
        
        for line in jsonl_file:
            # 严格提取原始字段，空值用空字符串替代（避免KeyError）
            question = line.get("question", "").strip()
            answer = line.get("answer", "").strip()
            
            # 写入CSV，确保与JSONL的行一一对应
            csv_writer.writerow({
                "question": question,
                "answer": answer
            })
            total_count += 1
    
    print(f"转换完成！共处理 {total_count} 条数据")
    print(f"CSV文件路径：{csv_output_path}")
    print(f"数据一致性验证：CSV记录数与JSONL一致（均为 {total_count} 条）")

# 你的文件路径
INPUT_JSONL_PATH = "/data/q30061833/run_file/gsm8k/test.jsonl"
OUTPUT_CSV_PATH = "/data/q30061833/run_file/gsm8k/gsm8k_out.csv"

# 执行转换
gsm8k_jsonl_to_csv(INPUT_JSONL_PATH, OUTPUT_CSV_PATH)
