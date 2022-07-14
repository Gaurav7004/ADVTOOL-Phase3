import os
import pandas as pd

HERE = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.abspath(os.path.join(HERE, '..', 'data'))

def make_df_from_excel(file_name, nrows):
    """Read from an Excel file in chunks and make a single DataFrame.

    Parameters
    ----------
    file_name : str
    nrows : int
        Number of rows to read at a time. These Excel files are too big,
        so we can't read all rows in one go.
    """
    file_path = os.path.abspath(os.path.join(DATA_DIR, file_name))
    xl = pd.ExcelFile(file_path)

    # In this case, there was only a single Worksheet in the Workbook.
    sheetname = xl.sheet_names[0]

    print(sheetname)

    # Read the header outside of the loop, so all chunk reads are
    # consistent across all loop iterations.
    df_header = pd.read_excel(file_path, sheet_name=sheetname, nrows=1)
    print(f"Excel file: {file_name} (worksheet: {sheetname})")

    chunks = []
    i_chunk = 0
    # The first row is the header. We have already read it, so we skip it.
    skiprows = 4
    while True:
        df_chunk = pd.read_excel(
            file_path, sheet_name=sheetname,
            nrows=nrows, skiprows=skiprows, header=None)

        print(df_chunk[1])

        skiprows += nrows
        # When there is no data, we know we can break out of the loop.
        if not df_chunk.shape[0]:
            break
        else:
            print(f"  - chunk {i_chunk} ({df_chunk.shape[0]} rows)")
            chunks.append(df_chunk)
        i_chunk += 1

    df_chunks = pd.concat(chunks)
    # Rename the columns to concatenate the chunks with the header.
    columns = {i: col for i, col in enumerate(df_header.columns.tolist())}
    df_chunks.rename(columns=columns, inplace=True)
    df = pd.concat([df_header, df_chunks])
    return df


if __name__ == '__main__':
    df = make_df_from_excel('C:\\Users\\gaurav\\Desktop\\ADVTool\\ADVTOOL_14thJune2022\\Data Item wise report of Telangana as on 7th June 2022 at 14_54_54 PM.xlsx' , nrows=3)
    print(df)