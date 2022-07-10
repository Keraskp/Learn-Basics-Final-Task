import pandas as pd

def Format(df): #DataFrame to be passed as arguement
    
    data_output = []
    
    # Output DataFrame Columns
    columns_output = ['Name','Username','Chapter Tag','Test_Name','score','time-taken (seconds)','answered','correct','wrong','skipped']
    
    n_names = df.shape[0]      # No of rows in input file
    n_columns = df.shape[1]    # No of columns in input file
    
    # Iterate through each row and append data in data_output
    
    for i in range(n_names):
        Name = df['Name'][i]
        Username = df['id'][i]
        ChapterTag = df['Chapter Tag'][i]
        
        j=3
        while j<n_columns:
            Data = [Name,Username,ChapterTag]
            if df.iloc[i][j]=='-':
                j+=6
                continue
            Data.append(df.columns[j].replace(' - score',''))
            Data.extend([df.iloc[i][j], df.iloc[i][j+1], df.iloc[i][j+2], df.iloc[i][j+3], df.iloc[i][j+4], df.iloc[i][j+5]])
            print(Data)
            data_output.append(Data)
            j+= 6
    
    # Creating output DataFrame
    df_output = pd.DataFrame(data_output,columns=columns_output)
    
    # Rearranging columns to match given file :
    df_output = df_output[['Name','Username','Chapter Tag','Test_Name','answered','correct','score','skipped','time-taken (seconds)','wrong']]
    
    return df_output

def read_file():
	
	while 1 :
		choice = int(input('\nEnter file extension : \n 1.csv \t2.xlsx\n'))

		if choice == 1 :
			file_path = input('Enter file path : ')
			df = pd.read_csv(file_path)
			return df
		elif choice == 2:
			file_path = input('Enter file path : ')
			sheet_name = input('Enter sheet name : ')
			df = pd.read_excel(file_path, sheet_name=sheet_name)
			return df
		else : 
			print('Wrong Choice') 


if __name__ == '__main__':

	df1 = read_file()
	df2 = read_file()

	print(df1.head())
	print(df2.head())

	df_output1 = Format(df1)
	print(df_output1)
	df_output2 = Format(df2)
	print(df_output2)


	output1_path = './output/output1.csv'
	df_output1.to_csv(output1_path, index=False,header=True)
	print(f'Generated csv file at {output1_path}')

	output2_path = './output/output2.csv'
	df_output2.to_csv(output2_path, index=False,header=True)
	print(f'Generated csv file at {output1_path}')