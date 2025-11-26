import openpyxl

def main():
    file_path = '../BeeTheOne/tests/daftarsaldo.xlsx'
    sheet_name = 'saldo awal'

    try:
        wb = openpyxl.load_workbook(file_path, data_only=True)
        ws = wb[sheet_name]
    except Exception as e:
        print(f"Error loading {file_path} sheet {sheet_name}: {e}")
        return

    print(f"Reading first 5 rows from '{sheet_name}' sheet in {file_path}")
    for i, row in enumerate(ws.iter_rows(values_only=True), start=1):
        print(row)
        if i >= 5:
            break

if __name__ == "__main__":
    main()
