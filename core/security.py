import uuid

def get_my_device_id():
    return str(uuid.getnode())

if __name__ == "__main__":
    print(f"========================================")
    print(f"الرقم الفريد لجهازك هو: {get_my_device_id()}")
    print(f"========================================")