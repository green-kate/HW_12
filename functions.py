import json


def load_posts() -> list[dict]:
    """Загрузка всех постов"""
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_word(word: str) -> list[dict]:
    """Поиск постов по слову"""
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def save_picture(picture) -> str:
    """Сохранение картинки нового поста"""
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path


def save_post(post: dict) -> dict:
    """Сохранение нового поста"""
    posts: list[dict] = load_posts()
    posts.append(post)

    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)

    return post
