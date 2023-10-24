import os
from app import db, app, Image


image_folder = './images'  # Replace with the path to your image folder


def add_images(session, Image):
    for filename in os.listdir(image_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            with open(os.path.join(image_folder, filename), 'rb') as f:
                image = Image(rating=800, image=f.read())
                session.add(image)
                session.commit()


with app.app_context():
    add_images(session=db.session, Image=Image)
