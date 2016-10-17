# -*- coding: utf-8 -*-
"""

    main.default_config
    ============
    
    This is the default config used by Subrosa,
    it consists of all the options in Subrosa conf
    aswell as some more advanced one
    Typically this should not be changed by user.

    :copyright: (c) 2014 by Konrad Wasowicz
    :license: MIT, see LICENSE for details.

"""

# Set title of you site

TITLE = "Your awesome blog"

# ========== Database Configuration =================

# Define database connection

# Avaliable databases are:
# * sqlite
# * postrges
# * mysql

# Database type

DATABASE = None

# Database name

DATABASE_NAME = None

#This options apply only if you are using postgresql or mysql

DB_USERNAME = None 

DB_PASSWORD = None 

# ===================================================

# Set this variable to your === disqus shortname === to have comments on your blog

DISQUS = ""

# Set this variables to adress of your liking eg "http://www.facebook.com/johndoe"

EMAIL = ""

FACEBOOK = ""

TWITTER = ""

GITHUB = ""

GOOGLE_PLUS = ""

TWITTER_USERNAME = ""

# If you want gallery integrated with Imgur service put your Imgur user_id here

IMGUR_ID = ""

# Show different links on header

GALLERY = False

PROJECTS = False

ABOUT = False

ARCHIVES = False

# Number of pages that shows up on index page

ARTICLES_PER_PAGE = 5 

# Number of images showing on page

IMAGES_PER_PAGE = 10

# Your secret key

SECRET_KEY = "Change it"


# =======================================================================
# ======================== Advanced Settings ============================
# =========== Change them only if you know what you're doing ============
# =======================================================================

# Allowed filenames for image upload

ALLOWED_FILENAMES = ["jpg", "jpeg", "gif", "png", "JPG", "JPEG", "GIF", "PNG"]

# Switches in swttings panel

SETTINGS_SWITCHES = ("show_info", "show_projects", "show_archives", "show_gallery", "show_about")

# Field names in settings panel

SETTINGS_FIELDS = ("email", "github", "facebook", "twitter", "twitter_username", "google_plus", "disqus_shortname", "imgur_id", "site_title")

# Thumbnail size for imgur images

# Available sizes :
    # s -- 90x90 square
    # b -- 160x160 square
    # t -- 160x160
    # m -- 320x320
    # l -- 640x640
    # h -- 1024x1024

THUMBNAIL_SIZE = "l"


# Set it to True only for development purposes, outputs errors straight to the browser

DEBUG = False

# Cache options

CACHE_TYPE = "simple"

CACHE_KEY_PREFIX = "subrosa_"

CACHE_TIMEOUT = 50

