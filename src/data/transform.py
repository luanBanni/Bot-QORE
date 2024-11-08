import os
from fpdf import FPDF
from PIL import Image
import tempfile
import shutil

def transformPDF(imagens, pdf_path):
  pdf = FPDF()
  temp_dir = tempfile.mkdtemp()

  for index, imagem in enumerate(imagens):
    pdf.add_page()
    temp_image_path = os.path.join(temp_dir, f"temp_image_{index}.png")
    imagem.save(temp_image_path, format='PNG')
    width, height = imagem.size
    pdf.image(temp_image_path, 0, 0, width / 5, height / 5 )
    os.remove(temp_image_path)
  pdf.output(pdf_path)

  shutil.rmtree(temp_dir)