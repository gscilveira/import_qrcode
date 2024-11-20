<h1>Olá, me chamo Guilherme Cavalieri, este trabalho foi desenvolvido para a faculdade, espero que gostem</h1>
<h2>Primeiramente, este codigo foi feito 100% em python, desenvolvi um gerador de QR Code, onde vou mostrar como é facil poder usar o mesmo</h2>
<h3>Em seu computador, instale o <a href="https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe" target="_blank">Python</a></h3>
<p>Após intalado, devemos rodar mais dois códigos para instalarmos as bibliotecas, que fazem com que o nosso gerador de QR Code possa funcionar</p>
<p>Clique no logo do windows, no canto inferior da tela, pesquise por "CMD", abra como administrador</p>
<p>Após abrir o cmd, rode o comando <code>py -3 -m ensurepip</code></p>
<p>Em seguida, roda mais dois comandos para instalarmos as bibliotecas <code>pip install qrcode[pil]</code></p>
<p>Agora o segundo e ultimo comando <code>pip install Pillow
</code></p>
<p>Após isso, o ambiente estará pronto para ser usado</p>
<p>Abra o aplicativo de sua preferencia que rode python, pode ser o aplicativo do mesmo, ou ate mesmo alguma KDE de desenvolvimento</p>
<p>Rode o comando abaixo:</p>

```
import qrcode 

data = "https://www.twitch.tv/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("twitch_qrcode.png") 

print
```
