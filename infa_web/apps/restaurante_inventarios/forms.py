# -*- coding: utf-8 -*-
from django import forms
from infa_web.apps.restaurante_inventarios.models import *
from django.core.exceptions import ValidationError
from django.db.models import Max
