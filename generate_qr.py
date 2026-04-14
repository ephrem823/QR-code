import qrcode

def generate_qr(data: str, filename: str = "qrcode.png"):
    img = qrcode.make(data)
    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    data = input("Enter text or URL: ")
    generate_qr(data)
