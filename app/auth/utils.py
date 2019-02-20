import secrets
import os
from flask import url_for, current_app
from PIL import Image

def save_picture(pic_form):
    """
    This function will generate a Hash code for the saved pic in order
    avoid having multiple files inside the db with the same name that would generate potential
    overwriting of the original files. Then the pic file will be saved in
    the designated folder path.
    """
    random_hex = secrets.token_hex(8)

    _ , file_ext = os.path.splitext(pic_form.filename)

    picture_filename = random_hex +file_ext
    picture_path= os.path.join(current_app.root_path,
                'static/img/profile_pics',picture_filename)

    output_size = (200,200)
    img = Image.open(pic_form)
    img.thumbnail(output_size)
    img.save(picture_path)

    return picture_filename
