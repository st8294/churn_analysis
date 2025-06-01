import pandas as pd
df= pd.read_excel(r"C:\Users\soura\Downloads\messy_healthcare_data_520_records.xlsx")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Prevent line breaks and show full text
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)

# Set high display width
pd.set_option('display.width', 2000)

df['Product_Name'] = df['Product_Name'].str.strip().str.title()

text_to_number = {
    'one hundred': 100,
    'six hundred': 600
}

df['Units_sold'] = df['Units_sold'].replace(text_to_number).fillna(0)
df['Units_sold'] = df['Units_sold'].fillna(0)

df['Sale$']= df['Sale$'].replace(text_to_number).fillna(0)
df['Sale$']=pd.to_numeric(df['Sale$'], errors='coerce')

df['Hospital Name'] = df['Hospital Name'].str.strip().replace({
    'Med-Care Hospitl': 'Med-Care Hospital',
    'City Medical Inst.': 'City Medical Institute'
})

df['Region']= df['Region'].str.strip().str.title()

df['StockLeft'] = df['StockLeft'].fillna(0).replace({'-': 0, 'N/A': 0})

df['Exp_Date'] = pd.to_datetime(df['Exp_Date'], errors='coerce')

df['Remarks'] = df['Remarks'].str.strip().replace({'Missng lot#': 'Missing lot#', 'Duplocate': 'Duplicate'})

print(df.head(15))

