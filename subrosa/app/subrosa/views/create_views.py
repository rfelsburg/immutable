﻿# -*- coding: utf-8 -*-
"""

    subrosa.views.create_views
    ===============

    Implements class-based views related to creating projects and articles

    :copyright: (c) 2014 by Konrad Wasowicz
    :license: MIT, see LICENSE for details.

"""

from __future__ import print_function
from flask import render_template, request, session, url_for, redirect, flash
from subrosa import app, cache
from subrosa.models.UsersModel import Users
from subrosa.models.ArticlesModel import Articles, Categories
from subrosa.models.UserProjectsModel import UserProjects
from subrosa.helpers import logger
from subrosa.views.base_views import ScratchpadView, ArticleView


class CreateView(ScratchpadView):

    """
    Base view needed for creating
    articles and projects
    """

    def get_get_model(self):
        raise NotImplementedError()

    def create_method(self):
        raise NotImplementedError()

    def get(self):
        return self.render_template()

    def post(self):
        title = request.form.get("title").strip()
        body = request.form.get("body").strip()
        user = Users.get_user_by_username(session["user"])
        context = dict(title=title, body=body, author=user)
        additional = self.get_context()
        context.update(additional)
        if not title or not body:
            error = "Entry can\'t have empty title or body"
            context.update(dict(error=error))
            return self.render_template(context)
        model = self.get_model()
        check = model.check_exists(title)
        if check:
            error = "Entry with that title already exists, choose a new one.."
            context.update(dict(error=error))
            return self.render_template(context)
        else:
            context.update(self.process_additional_fields())
            try:
                func = getattr(model, self.create_method())
                func(**context)
                with app.app_context():
                    cache.clear()
                flash("Created")
                return redirect(url_for("account", username=session["user"]))
            except Exception as e:
                logger.debug(e)
                error = "Processing error see error.log for details"
                context.update(dict(error=error))
                return self.render_template(context)


class CreateArticleView(ArticleView, CreateView):

    def get_model(self):
        return Articles

    def create_method(self):
        return "create_article"

    def get_context(self):
        existing_categories = Categories.select()
        return dict(draft=True,
                    additional_controls=True,
                    existing_categories=existing_categories,
                    title_placeholder="Title of your Article",
                    body_placeholder="and content here...")


class CreateProjectView(CreateView):

    def get_model(self):
        return UserProjects

    def create_method(self):
        return "create_project"

    def get_context(self):
        return dict(additional_controls=False,
                    title_placeholder="Title of the project..",
                    body_placeholder="and content here...")
