import win32print

# プリンタの一覧を取得
printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)

# プリンタ名を出力
for printer in printers:
    print(printer[2])