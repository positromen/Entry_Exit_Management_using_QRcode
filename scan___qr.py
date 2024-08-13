import cv2
from pyzbar.pyzbar import decode
import sqlite3
from datetime import datetime
import time

def mark_attendance(enrollment_no):
    conn = sqlite3.connect('freshers_party.db')
    cursor = conn.cursor()

    cursor.execute('SELECT entry_time, exit_time FROM attendees WHERE enrollment_no = ?', (enrollment_no,))
    record = cursor.fetchone()

    if record:
        if record[0] is None:
            cursor.execute('''
            UPDATE attendees 
            SET entry_time = ? 
            WHERE enrollment_no = ?
            ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), enrollment_no))
            print(f"Entry marked for enrollment number {enrollment_no}.")
        elif record[1] is None:
            cursor.execute('''
            UPDATE attendees 
            SET exit_time = ? 
            WHERE enrollment_no = ?
            ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), enrollment_no))
            print(f"Exit marked for enrollment number {enrollment_no}.")
        else:
            print(f"Already exited: enrollment number {enrollment_no}.")

    conn.commit()
    conn.close()

def scan_qr():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        decoded_objects = decode(frame)

        if decoded_objects:
            for obj in decoded_objects:
                enrollment_no = obj.data.decode("utf-8")
                mark_attendance(enrollment_no)

            # Buffer time before scanning the next QR code
            print("QR code processed. Waiting to scan the next QR code...")
            time.sleep(3)  # 3 seconds buffer time

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr()
