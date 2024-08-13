import qrcode
import sqlite3

def generate_qr_code(enrollment_no):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(enrollment_no)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(f"{enrollment_no}.png")
    print(f"QR Code generated for enrollment number {enrollment_no}.")

def generate_qr_for_all():
    conn = sqlite3.connect('database_entry-exit.db')
    cursor = conn.cursor()

    cursor.execute('SELECT enrollment_no FROM attendees')
    rows = cursor.fetchall()

    for row in rows:
        generate_qr_code(row[0])

    conn.close()

if __name__ == "__main__":
    generate_qr_for_all()
