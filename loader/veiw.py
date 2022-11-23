import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import save_picture, save_post

post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')


@post_blueprint.route('/post')
def post_page():
    """Страница с постами"""
    return render_template("post_form.html")


@post_blueprint.route('/post', methods=['POST'])
def add_post_page():
    """Страница добавления новых постов"""
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return "Нет картинки или текста"
    if picture.filename.split(".")[-1] not in ['jpg', 'png']:
        logging.info("загруженный файл не верного формата")
        return "неверный формат файла"
    try:
        picture_path: str = "/" + save_picture(picture)
    except FileNotFoundError:
        logging.error("Файл не найден")
        return 'Файл не найден'
    except JSONDecodeError:
        return "Невалидный файл"
    post: dict = save_post({'pic': picture_path, 'content': content})

    return render_template('post_uploaded.html', post=post)
