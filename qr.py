import qrcode


def makeQR(link,name):
    url = ("{}")
    qrname = ("{}.png")
    code = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=7,
        border=2
                        )
    link=url.format(link)
    code.add_data(link)
    code.make(fit=True)
    image = code.make_image(fill_color="#ffdf00",back_color="#1e2328")
    name=qrname.format(name)
    image.save(name)
















