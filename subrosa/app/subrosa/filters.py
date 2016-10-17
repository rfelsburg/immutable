# -*- coding: utf-8 -*-
"""

    subrosa.filters
    ============

    Miscellaneous filters used in subrosa views

    :copyright: (c) 2014 by Konrad Wasowicz
    :license: MIT, see LICENSE for details.

"""

from jinja2 import Markup
from datetime import datetime
import calendar
import re


def timesince(dt, default="just now"):
    """
    Returns string representing "time since" e.g.
    3 days ago, 5 hours ago etc.
    """

    now = datetime.utcnow()
    diff = now - dt

    periods = (
        (diff.days / 365, "year", "years"),
        (diff.days / 30, "month", "months"),
        (diff.days / 7, "week", "weeks"),
        (diff.days, "day", "days"),
        (diff.seconds / 3600, "hour", "hours"),
        (diff.seconds / 60, "minute", "minutes"),
        (diff.seconds, "second", "seconds"),
    )
    for period, singular, plural in periods:
        if period:
            return "%d %s ago" % (period, singular if period == 1 else plural)
    return default


def get_month_name(month_number):
    """ Return month name based on integer """

    months = ("January", "February",
              "March", "April", "May",
              "June", "July", "August",
              "September", "October",
              "November", "December")

    return months[month_number - 1]


