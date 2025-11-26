import openpyxl
import os

def create_full_daftarsaldo():
    bee_the_one_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(bee_the_one_dir, 'BeeTheOne', 'daftarsaldo.xlsx')

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "daftar saldo awal"

    # Write header
    ws.append(['No Akun', 'Nama Akun'])

    # Provided account list as tuples (code, name)
    accounts = [
        ('1-1100', 'Kas'),
        ('1-1200', 'Piutang usaha'),
        ('1-1300', 'Persediaan barang dagang'),
        ('1-1310', 'Persediaan stok madu gudang'),
        ('1-1400', 'Perlengkapan toko'),
        ('1-1500', 'Tanah'),
        ('1-1510', 'Bangunan'),
        ('1-1511', 'Akumulasi penyusutan bangunan'),
        ('1-1600', 'Kendaraan'),
        ('1-1610', 'Akumulasi penyusutan kendaraan'),
        ('1-1700', 'Peralatan'),
        ('1-1710', 'Akumulasi penyusutan peralatan'),
        ('2-2100', 'Hutang dagang'),
        ('3-3000', 'Modal'),
        ('4-4000', 'Penjualan barang dagang'),
        ('4-4100', 'Retur penjualan'),
        ('5-5000', 'Harga pokok penjualan'),
        ('6-6100', 'Beban telepon, air, dan listrik'),
        ('6-6200', 'Beban perlengkapan'),
        ('6-6300', 'Beban pemeliharaan'),
        ('6-6400', 'Beban gaji produksi'),
        ('6-6500', 'Beban gaji pemeliharaan lebah'),
        ('6-6600', 'Beban transportasi pemeliharaan lebah'),
        ('6-6700', 'Beban transportasi penjualan lebah'),
        ('6-6800', 'Beban depresiasi aktiva tetap'),
    ]

    for acc in accounts:
        ws.append(acc)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    wb.save(file_path)
    print(f"daftarsaldo.xlsx created at {file_path}")

if __name__ == "__main__":
    create_full_daftarsaldo()
