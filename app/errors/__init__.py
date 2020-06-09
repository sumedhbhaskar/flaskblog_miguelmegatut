from flask import Blueprints

bp = Blueprints('errors',__name__)

from app.errors import handlers
