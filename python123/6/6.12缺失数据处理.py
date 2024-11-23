import csv

def replace_missing_values(file_path, replacement):
    result = []
    with open(file_path, mode='r', encoding='GBK') as file:
        reader = csv.reader(file)
        for row in reader:
            # 按照您的要求处理缺失值
            cleaned_row = [
                col if col.strip() else replacement for col in row
            ]
            result.append(cleaned_row)
    return result

def main():
    file_path =r"filldata.csv"
    replacement = input().strip()
    try:
        processed_data = replace_missing_values(file_path, replacement)
        print(processed_data)
    except FileNotFoundError:
        print("文件未找到，请检查路径是否正确。")
    except Exception as e:
        print(f"文件处理失败，错误信息：{e}")

if __name__ == "__main__":
    main()
