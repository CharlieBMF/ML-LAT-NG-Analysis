import pandas as pd


workbook_main = pd.read_excel('ALL_LAT.xlsx', engine='openpyxl', sheet_name='A')
workbook_temp = pd.read_excel('N24Q0003.xlsx',
                         engine='openpyxl',
                         sheet_name='All',
                         header=4,
                         usecols="D, I:Q, Z:AQ, AX:AZ, BK:CE, CO:DK, DT:DW, EE:EF, EM:EW, EZ:FC, FF, FH:FK, FN")
print(len(workbook_main))
final = pd.DataFrame()

for i in range(len(workbook_main)):
    try:
        workbook_temp = pd.read_excel(str(workbook_main.iloc[i]['nr lotu']+'.xlsx'),
                                      engine='openpyxl',
                                      sheet_name='All',
                                      header=4,
                                      usecols="D, I:Q, Z:AQ, AX:AZ, BK:CE, CO:DK, DT:DW, EE:EF, EM:EW, EZ:FC, FF, FH:FK, FN")
        ds = workbook_temp[workbook_temp['Barcode'] == workbook_main.iloc[i]['nr seryjny']]
        print(ds)
        final = final.append(ds, ignore_index=True)
        print('Finished step..', len(final))
    except:
        continue
