# 超市销售数据处理与校验脚本 (Supermarket Data Validation)

## 📖 项目简介
这是一个基于 Python Pandas 的数据处理小工具，主要用于对零售销售数据进行自动化清洗与逻辑校验。该项目旨在解决原始数据中常见的缺失值问题，并验证交易金额的准确性。

## 🛠️ 技术栈
- **Python 3.x**
- **Pandas**: 用于数据读取、清洗和聚合分析。

## 📂 包含文件
- `data_clean.py`: 核心处理脚本，包含缺失值填充和金额校验逻辑。
- `sales_data.csv`: 示例原始销售数据（包含模拟的异常数据）。

## 🚀 如何运行
确保已安装 pandas 库：
pip install pandas

然后在终端运行：
python data_clean.py
