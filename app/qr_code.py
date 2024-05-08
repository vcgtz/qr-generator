from pathlib import Path
import os.path

import segno


class QRCode:
    def __init__(self, file_name: str, border: int = 1, scale: int = 25):
        self.__folder_path = Path.home()
        self.__file_name = file_name
        self.__file_path = os.path.join(self.__folder_path, f"{self.__file_name}.png")
        self.__border = border
        self.__scale = scale
        self.__qr_code = None

    def generate(self, text: str) -> str:
        try:
            self.__qr_code = segno.make_qr(text)
            self.__qr_code.save(
                self.__file_path,
                scale=self.__scale,
                border=self.__border
            )

            return self.__file_path
        except Exception:
            print("There was an issue generating the QR")


if __name__ == "__main__":
    qr_code = QRCode("my_file")
    qr_code.generate("Hello World")
