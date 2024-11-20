import qrcode

# URL desejado
data = "https://www.twitch.tv/"

# Configuração do QR Code
qr = qrcode.QRCode(
    version=1,  # Tamanho do QR Code (1 é o menor)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erro
    box_size=10,  # Tamanho de cada "caixa" do QR Code
    border=4,  # Largura da borda (padrão é 4)
)

# Adiciona os dados ao QR Code
qr.add_data(data)
qr.make(fit=True)

# Gera a imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salva a imagem em um arquivo
img.save("twitch_qrcode.png")

# Confirma a criação do QR Code
print