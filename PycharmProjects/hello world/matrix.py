row1=['😇','😇','😇']
row2=['😇','😇','😇']
row3=['😇','😇','😇']
matrix=[row1,row2,row3]#to access rows
print(f"{row1}\n{row2}\n{row3}")
position=input("Enter the position where u wanna hide the money?")
#32
row_number=int(position[0])
column_number=int(position[1])
row_selected=matrix[row_number-1]#access row 3
row_selected[column_number-1]='X'#index within the row
print(f"{row1}\n{row2}\n{row3}")

