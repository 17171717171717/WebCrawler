# ch2_9.py
import csv

fn = 'out2_9.csv'
with open(fn, 'w', newline = '') as csvFile:            # 開啟csv檔案
    csvWriter = csv.writer(csvFile, delimiter='O')     # 建立Writer物件   
    csvWriter.writerow(['Name', 'Age', 'City'])
    csvWriter.writerow(['Hung', '35', 'Taipei'])
    csvWriter.writerow(['James', '40', 'Chicago'])


