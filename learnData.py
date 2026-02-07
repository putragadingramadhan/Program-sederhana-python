import pandas as pd # untuk membuat dan mengeloal DataFrame
import numpy as np # untuk menghitung numerik
from scipy import stats # untuk mode, skew, IQR, dll
import matplotlib.pyplot as pplt # untuk visualisasi
import seaborn as sns # untuk visulisasi lanjutan
from rich.console import Console
from rich.table import Table


df = pd.DataFrame({
    "Order_Amount" : [250, 400,140, 150, 500, 350, 420, 310, 280, 390, 450],
    "Num_Items"    : [3, 5, 2, 6,7, 4, 5, 4, 3, 5, 6],
    "Customer_Age" : [25, 33,34, 22, 45, 31, 37, 29, 28, 33, 40],
    "Discount"     : [5,6, 10, 0, 15, 10, 12, 8, 5, 10, 15],
    "Delivery_Time" : [29,34, 45, 20, 60, 40, 50, 35, 30, 45, 55 ]
})
console = Console()
table = Table(show_header=True, header_style="bold magenta")

#tambah colom
table.add_column("Index", style="dim")
for col in df.columns:
    table.add_column(col)
#tambah baris
for index, row in df.iterrows():
    table.add_row(
        str(index),
        *[str(val) for val in row.values]
    )
console.print(table)

mean_ = df.mean()
print("Mean :\n",mean_) #cari mean
median_ = df.median()
print('\nMedian : \n',median_)# cari median
#mode, nilai paling sering muncul
mode_ = df.mode().iloc[0]
print("\nMode : \n",mode_)

# Range, selilih max-min tiap kolom
range_ = df.max()-df.min()
print("\nRange : \n",range_)

#Interquartile Range (IQR tiap kolom)
iqr_ = df.apply(stats.iqr)
print("\nIQR : \n",iqr_)

#Variance (variasi sampel tiap colom)
variance_ = df.var()
print("\nVariance : \n",variance_)

# Standart Deviation (standar deviasi tiap colom)
std_dev_value = df.std()
print("\nStandart Deviation :\n",std_dev_value)

"""Measuring Asymmentry"""
# Skewness (kemiringan distribusi tiap colom)
skew_value = df.skew()
print("\nSkweness :\n",skew_value)
# Interpretasi distribusi tiap colom
for col in df.columns:
    if skew_value[col]>0:
        print(f"{col} : Right-skewed") #tail ke kanan
    elif skew_value[col]<0:
        print(f"{col}: Left-skewed")
    else:
        print(f"{col}: Symmetric")
"""Grafik distribusi tiap colom"""
for col in df.columns:
    pplt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True, color='skyblue', bins=10) #histogram + density plot
    pplt.title(f"Distribusi kolom : {col}")
    pplt.xlabel(col)
    pplt.ylabel("Frekuensi")
    pplt.show()

# pplt.figure(figsize=(8,4))
# sns.lineplot(data=df, x="Customer_Age", y="Discount", markers='o')
# pplt.title("Pola diskon berdasarkan umur pelanggan")
# pplt.grid(True)
# pplt.show()