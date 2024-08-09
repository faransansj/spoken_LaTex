import pandas as pd

# Parquet 파일 경로
parquet_file_path = r'C:\github\MathBridge\spoken_LaTex\Data\df_not_len_5_cleaned_unique_eq_en.parquet'

# Parquet 파일 불러오기
df = pd.read_parquet(parquet_file_path, engine='pyarrow')

# 필요한 열만 선택
df_subset = df[['equation', 'equation_en']]

# CSV 파일로 저장
output_csv_path = r'C:\github\MathBridge\spoken_LaTex\Data\equation_conversion.csv'
df_subset.to_csv(output_csv_path, index=False)

print(f"CSV file saved to {output_csv_path}")