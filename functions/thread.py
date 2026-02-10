import os
import time
from PySide6.QtCore import QThread, Signal
from concurrent.futures import ThreadPoolExecutor
from urllib import request
from PIL import Image
from .config import Config


class DownloadThread(QThread):
  progress = Signal(int)

  def __init__(self, image_list, download_path):
    super().__init__()

    self.image_list = image_list
    self.download_path = download_path
    self.config = Config("setting.ini")

    if os.path.exists(self.download_path):
      return
    else:
      os.makedirs(self.download_path)

  def run(self):
    image_list_length = len(self.image_list)
    max_workers = int(self.config["SETTING"]["Dowload"]["max_workers"])

    with ThreadPoolExecutor(max_workers=max_workers) as executor:

      def download_image(image_url):
        opener = request.build_opener()
        opener.addheaders = [(
            "User-Agent",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ), ("Referer", "https://nhentai.net/")]

        request.install_opener(opener)

        full_name = os.path.basename(image_url)
        base_name, ext = os.path.splitext(full_name)

        image_name = f"{base_name.zfill(len(str(image_list_length)))}{ext}"
        image_path = os.path.join(self.download_path, image_name)

        if image_url.startswith("//"):
          image_url = "https:" + image_url

        try:
          request.urlretrieve(image_url, image_path)
        except request.HTTPError as e:
          print(f"HTTP Error {e.code}: {image_url}")

          return
        except Exception as e:
          print(f"Error downloading {image_url}: {e}")

          return
        time.sleep(int(self.config["SETTING"]["Dowload"]["delay"]))

      for index, _ in enumerate(executor.map(download_image, self.image_list)):
        self.progress.emit(index + 1)


class PDFThread(QThread):

  def __init__(self, mange_path):
    self.mange = []

    if os.path.exists(mange_path):
      self.mange_path = mange_path
      self.base_path = os.path.abspath(os.path.join(mange_path, ".."))
      self.mange_name = os.path.basename(mange_path)
    else:
      return

  def filter_manga_image(self):
    for image in os.listdir(self.mange_path):
      try:
        if Image.open(os.path.join(self.mange_path, image)):
          self.mange.append(os.path.join(self.mange_path, image))
      except Exception:
        pass

  def save_as_pdf(self):
    save_path = os.path.join(self.base_path, f"{self.mange_name}.pdf")

    def open_image(file):
      return Image.open(file).convert("RGB")

    with ThreadPoolExecutor(max_workers=5) as executor:
      sources = list(executor.map(open_image, self.mange))

    sources[0].save(save_path, "pdf", save_all=True, append_images=sources[1:])

  def run(self):
    self.filter_manga_image()
    self.save_as_pdf()
