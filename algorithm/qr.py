import io
import qrcode


class Generate:

    def __init__(self):
        pass
    
    def qr_code(self, link: str = None):
            
        if link is None:
            raise Exception("link cannot be None")

        # Create an instance of qrcode
        qr = qrcode.QRCode(version=1, box_size=10, border=1)
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")

        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format="PNG")
        img_byte_arr = img_byte_arr.getvalue()
        return img_byte_arr
    