import sys
from core.security import get_my_device_id

# المفتاح السري الذي لا يعرفه إلا جهازك
MY_AUTHORIZED_ID = "9817113392610"

def start_secure_system():
    current_id = get_my_device_id()
    
    if current_id != MY_AUTHORIZED_ID:
        print("Error: System Access Denied.")
        sys.exit()
    else:
        print("System Verified. SecureTrade Active.")
        # هنا سنضع لاحقاً منطق التحليل المشفّر

if __name__ == "__main__":
    start_secure_system()