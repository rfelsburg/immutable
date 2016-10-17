﻿# -*- coding: utf-8 -*-
"""

    subrosa.models.ArticlesModel
    =========================

    Implements model and methods related to subrosa images

    :copyright: (c) 2014 by Konrad Wasowicz
    :license: MIT, see LICENSE for details.


"""

import datetime
from peewee import *
from subrosa.models.BaseModel import BaseModel
from subrosa.models.UsersModel import Users
from subrosa.helpers import handle_errors
from subrosa import db


class UserImages(BaseModel):

    image_link = TextField()
    date_added = DateTimeField(default=datetime.datetime.utcnow())
    delete_hash = TextField(null=True)
    description = TextField(null=True)
    is_vertical = IntegerField(null=True)
    gallery = BooleanField(default=False)
    imgur_img = BooleanField(default=False)
    owner = ForeignKeyField(Users, related_name="images")

    @staticmethod
    def get_image(id):
        return UserImages.get_single("id", id)

    @staticmethod
    def check_exists(image_link):
        return (UserImages.select()
                .where(UserImages.image_link == image_link)
                .exists())

    @staticmethod
    def get_gallery_images(page, per_page, username=None, gallery=False):
        q = UserImages.select()
        if username:
            q = q.join(Users).where(Users.username == username)
        if gallery:
            return q.where(UserImages.gallery == True).paginate(page, per_page)
        return q.paginate(page, per_page)

    @staticmethod
    @db.commit_on_success
    def gallerify(image):

        try:
            is_gallerified = image.gallery
            image.gallery = not is_gallerified
            image.save()

        except Exception as e:
            handle_errors("Error updating image")

    @staticmethod
    @db.commit_on_success
    def add_image(image_link,
                  description,
                  owner,
                  is_vertical=True,
                  imgur_img=False,
                  delete_hash=None):
        try:
            UserImages.create(
                image_link=image_link,
                description=description,
                is_vertical=is_vertical,
                owner=owner,
                imgur_img=imgur_img,
                delete_hash=delete_hash,
            )
            return 1
        except Exception as e:
            handle_errors("Error creating image")
            raise

    @staticmethod
    @db.commit_on_success
    def delete_image(image):
        try:
            image.delete_instance()
            return 1
        except Exception as e:
            handle_errors("Error deleting image")
            raise

    def __repr__(self):
        return "<Image: {0}>".format(self.image_link)
