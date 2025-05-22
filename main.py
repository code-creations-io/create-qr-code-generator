from algorithm.qr import Generate

URL = "https://arungodwinpatel.com"
OUTPUT_FILE = "output.png"

if __name__ == "__main__":

    # Generate QR code
    generator = Generate()
    img_bytes = generator.qr_code(link=URL)

    # Write to local file
    with open(OUTPUT_FILE, "wb") as f:
        f.write(img_bytes)
    