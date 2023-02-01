import pandas as pd
import time


workbook_main = pd.read_excel('ALL_LAT.xlsx', engine='openpyxl', sheet_name='H')
workbook_temp = pd.read_excel('N24Q0003.xlsx',
                         engine='openpyxl',
                         sheet_name='All',
                         header=4,
                         usecols="D, I:Q, Z:AQ, AX:AZ, BK:CE, CO:DK, DT:DW, EE:EF, EM:EW, EZ:FC, FF, FH:FK, FN")

empty = workbook_temp.iloc[3]
empty['Barcode'] = 'SKIPPED BUDDY'
skipped_buddy_counter = 0
actual_workbook_path = 'empty'
final = pd.DataFrame()

for i in range(len(workbook_main)):
    start = time.time()
    try:
        if str(workbook_main.iloc[i]['nr lotu']+'.xlsx') != actual_workbook_path:
            actual_workbook_path = str(workbook_main.iloc[i]['nr lotu']+'.xlsx')
            workbook_temp = pd.read_excel(actual_workbook_path,
                                          engine='openpyxl',
                                          sheet_name='All',
                                          header=4,
                                          usecols="D, I:Q, Z:AQ, AX:AZ, BK:CE, CO:DK, DT:DW, EE:EF, EM:EW, EZ:FC, FF, FH:FK, FN")
        ds = workbook_temp[workbook_temp['Barcode'] == workbook_main.iloc[i]['nr seryjny']]
        final = final.append(ds, ignore_index=True)
        print('Finished step..', len(final))
        print('Skipped buddy counter..', skipped_buddy_counter)
    except:
        final = final.append(empty, ignore_index=True)
        skipped_buddy_counter += 1
    finally:
        if i % 10 == 0:
            with pd.ExcelWriter('combinedH.xlsx') as writer:
                final.to_excel(writer)
        end = time.time()
        print('This loop took.. ', end - start)
