def hitung_diskon(harga, persen):
    """Hitung harga setelah diskon"""
    return harga * (1 - persen / 100)

def hitung_pajak(harga_total):
    """Hitung pajak 10% dari total harga"""
    return harga_total * 0.10

def format_rupiah(angka):
    """Format angka ke Rupiah Indonesia"""
    return f"Rp{angka:,.0f}"