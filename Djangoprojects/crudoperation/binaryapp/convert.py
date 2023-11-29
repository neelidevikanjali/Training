import base64


def im(img):
    img = open('/home/vfy8/PycharmProjects/project20/crudoperation/imgs/test.jpg', "rb")
    data = base64.b64encode(img.read())
    return data
