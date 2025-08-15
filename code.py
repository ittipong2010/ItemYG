import pyautogui
import time

# โหลด serial codes จากไฟล์ txt (บรรทัดละ 1 โค้ด)
def load_serial_codes(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

# คลิกที่ปุ่มเมนูด้วยภาพ (menu_image.png ต้องเตรียมไว้เอง)
def click_menu_by_image(image_path, timeout=10):
    start = time.time()
    while time.time() - start < timeout:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
        if location:
            pyautogui.click(location)
            return True
        time.sleep(0.5)
    print("ไม่พบเมนูตามภาพ")
    return False

# --- MAIN LOGIC ---
def main():
    # โหลด serial codes
    serial_codes = load_serial_codes("serial_codes.txt")

    print("คุณมีเวลา 5 วินาทีในการยืนข้าง NPC...")
    time.sleep(5)

    for code in serial_codes:
        print(f"ส่งโค้ด: {code}")

        # 1. กดปุ่มกลางเมาส์เพื่อเปิดเมนู NPC
        screenWidth, screenHeight = pyautogui.size()
        pyautogui.click(screenWidth // 2, screenHeight // 2, button='middle')
        time.sleep(1.5)

        # 2. คลิกเมนูที่ 2 จากภาพ (เช่น menu2.png)
        if not click_menu_by_image("menu2.png"):
            print("ข้ามโค้ดนี้เนื่องจากไม่พบเมนู")
            continue

        time.sleep(1.2)  # รอหน้ากรอกโค้ด

        # 3. พิมพ์โค้ดและกด Enter
        pyautogui.typewrite(code)
        time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(1.5)

        # 4. ปิดเมนูหรือพร้อมส่งโค้ดถัดไป
        pyautogui.press('esc')
        time.sleep(1)

# Run
if __name__ == "__main__":
    main()
