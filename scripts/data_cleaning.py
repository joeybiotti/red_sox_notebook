import pandas as pd 

def clean_data(file_path, output_path):
    data = pd.read_csv(file_path)
   
    # Handle non-numeric values in 'Yrs' column
    data['Yrs']=pd.to_numeric(data['Yrs'], errors='coerce').fillna(0).astype(int)
    
    # Normalize formats
    data['Season'] = data['Season'].astype(int)
    data['Flag'] = data['Flag'].astype(str).str.lower().str.strip()

    # Handle missing values in 'Age' column
    data['Age']=data['Age'].fillna(data['Age'].mean())
    
    # Saved cleaned data to output path
    data.to_csv(output_path, index=False)
    
    print('Data cleaned & saved to', output_path)

input_file = 'data/raw/Boston_Red_Sox_Roster_Data.csv'
output_file = 'data/cleaned/Boston_Red_Sox_Roster_Data_cleaned.csv'
clean_data(input_file, output_file)