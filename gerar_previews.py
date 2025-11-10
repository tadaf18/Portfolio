# gerar_previews.py

import fitz  # Importa o PyMuPDF
import os
from pathlib import Path

# --- CONFIGURAÇÃO ---
# 1. Pasta onde estão seus PDFs originais
pdf_dir = "certificados/"

# 2. Pasta onde você quer salvar as imagens PNG
img_dir = "imagens/certificados/"
# --------------------

# Cria a pasta de imagens se ela não existir
os.makedirs(img_dir, exist_ok=True)

print(f"Iniciando conversão de PDFs da pasta: '{pdf_dir}'")
print(f"Salvando imagens em: '{img_dir}'")

# Lista todos os arquivos na pasta de PDFs
try:
    pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith(".pdf")]
except FileNotFoundError:
    print(f"ERRO: A pasta '{pdf_dir}' não foi encontrada.")
    print("Por favor, crie a pasta e adicione seus PDFs.")
    exit()

if not pdf_files:
    print("Nenhum arquivo PDF encontrado na pasta.")
    exit()

# Loop por cada arquivo PDF encontrado
for filename in pdf_files:
    pdf_path = os.path.join(pdf_dir, filename)
    
    # Define o nome do arquivo de imagem (ex: "meu_cert.pdf" -> "meu_cert.png")
    img_name = Path(filename).stem + ".png"
    img_path = os.path.join(img_dir, img_name)

    try:
        # Abre o documento PDF
        doc = fitz.open(pdf_path)
        
        # Pega a primeira página (índice 0)
        page = doc.load_page(0)  
        
        # Renderiza a página como uma imagem (pixmap)
        # O zoom aumenta a resolução. zoom=2 é 200% (boa qualidade)
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2)) 
        
        # Salva a imagem como PNG
        pix.save(img_path)
        
        print(f"  [OK] '{filename}' -> '{img_name}'")
        
        # Fecha o documento
        doc.close()
        
    except Exception as e:
        print(f"  [ERRO] Falha ao converter '{filename}': {e}")

print("\nConversão concluída!")