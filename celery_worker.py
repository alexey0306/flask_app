#!/usr/bin/env python
import os
from app import celery, create_app

app = create_app('app.config.DevelopmentConfig')
app.app_context().push()
