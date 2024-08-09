import pandas as pd

# Parquet 파일 경로
parquet_file_path0 = r'C:\github\MathBridge\spoken_LaTex\Data\df_sampled_1000_cleaned_unique_eq_en_complete_0.parquet'

# Parquet 파일 불러오기
df = pd.read_parquet(parquet_file_path0, engine='pyarrow')

# 필요한 열만 선택
df_subset = df[['equation', 'equation_en']]

# CSV 파일로 저장
output_csv_path = r'C:\github\MathBridge\spoken_LaTex\Data\equation_conversion_0.csv'
df_subset.to_csv(output_csv_path, index=False)

print(f"CSV file saved to {output_csv_path}")

# Parquet 파일 경로
parquet_file_path1 = r'C:\github\MathBridge\spoken_LaTex\Data\df_sampled_1000_cleaned_unique_eq_en_complete_1.parquet'

# Parquet 파일 불러오기
df = pd.read_parquet(parquet_file_path1, engine='pyarrow')

# 필요한 열만 선택
df_subset = df[['equation', 'equation_en']]

# CSV 파일로 저장
output_csv_path = r'C:\github\MathBridge\spoken_LaTex\Data\equation_conversion_1.csv'
df_subset.to_csv(output_csv_path, index=False)

print(f"CSV file saved to {output_csv_path}")