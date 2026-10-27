from PIL import Image
from tkinter import Tk, filedialog
import os

pasta_imagens = os.path.join(os.path.expanduser("~"), "Pictures")
print("Pasta de destino:", pasta_imagens)

print("Escolha a imagem PNG na janelinha...")

root = Tk()
root.withdraw()
caminho_png = filedialog.askopenfilename(
    title="Escolha a imagem",
    filetypes=[("Imagens", "*.png *.jpg *.jpeg")]
)

if not caminho_png:
    print("Nenhum arquivo selecionado.")
else:
    imagem = Image.open(caminho_png).convert("RGB")
    nome_pdf = os.path.join(pasta_imagens, "imagem_convertida.pdf")
    imagem.save(nome_pdf)
    print("PDF salvo em:", nome_pdf)