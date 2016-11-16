from flask import Flask, request, render_template
from random import randrange
from pathlib import Path

app = Flask('snow_leopard_tail')

def random_image():
    n = randrange(102)
    image_jpg = 'static/images/{}.jpg'.format(n)
    image_jpeg = 'static/images/{}.jpeg'.format(n)
    image_png = 'static/images/{}.png'.format(n)
    for img in (image_jpg, image_jpeg, image_png):
        if Path(img).is_file():
            return img


@app.route('/sltail', methods=['GET'])
def picture_page():
    return render_template('picture.html', picture=random_image())


if __name__ == '__main__':
    app.run()
