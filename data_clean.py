import pandas as pd

def process_sales_data(input_file, output_file):
    """
    超市销售数据清洗与校验脚本
    """
    print(f"正在读取文件: {input_file} ...")
    try:
        # 1. 读取数据
        df = pd.read_csv(input_file)
        print(f"成功读取 {len(df)} 条原始数据。")

        # 2. 数据清洗：检查并填充缺失值
        missing_count = df['Quantity'].isnull().sum()
        if missing_count > 0:
            print(f"发现 {missing_count} 个缺失的数量值，正在进行均值填充...")
            df['Quantity'].fillna(df['Quantity'].mean(), inplace=True)

        # 3. 逻辑校验：重新计算总金额 (TotalPrice = Quantity * UnitPrice)
        # 假设原始数据可能存在计算错误，我们进行修正
        df['Calculated_Total'] = df['Quantity'] * df['UnitPrice']

        # 简单的差异检查
        diff = (df['TotalPrice'] - df['Calculated_Total']).abs().sum()
        if diff > 0.01:
            print("警告：发现金额计算不一致，已根据最新数量重新计算总额。")
            df['TotalPrice'] = df['Calculated_Total']
        else:
            print("金额校验通过，数据准确。")

        # 4. 统计汇总
        category_sales = df.groupby('Category')['TotalPrice'].sum()
        print("\n--- 各类别销售总额 ---")
        print(category_sales)

        # 5. 导出清洗后的数据
        df.to_csv(output_file, index=False)
        print(f"\n处理完成！清洗后的数据已保存至: {output_file}")

    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    # 运行脚本
    process_sales_data('sales_data.csv', 'cleaned_sales_data.csv')
