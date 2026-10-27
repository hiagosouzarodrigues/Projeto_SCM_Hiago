# CONVERSOR DE DOCX PARA PDF usando LibreOffice

import subprocess
import os
from tkinter import Tk, filedialog

# Caminho do LibreOffice (ajuste se instalou em outro lugar)
caminho_libreoffice = r"C:\Program Files\LibreOffice\program\soffice.exe"

# 1. Abre a janelinha para escolher o arquivo
print("Escolha o arquivo DOCX na janelinha que abriu...")

root = Tk()
root.withdraw()
caminho_docx = filedialog.askopenfilename(
    title="Escolha o arquivo DOCX",
    filetypes=[("Documentos Word", "*.docx")]
)

# 2. Verifica se escolheu algo
if not caminho_docx:
    print("Nenhum arquivo selecionado. Encerrando.")
else:
    print("Arquivo escolhido:", caminho_docx)

    # 3. Pasta de saída (mesma do arquivo)
    pasta = os.path.dirname(caminho_docx)

    # 4. Converte
    print("Convertendo... aguarde.")
    subprocess.run([
        caminho_libreoffice,
        "--headless",
        "--convert-to", "pdf",
        "--outdir", pasta,
        caminho_docx
    ])

    nome_base = os.path.splitext(os.path.basename(caminho_docx))[0]
    print("PDF criado em:", os.path.join(pasta, nome_base + ".pdf"))