#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: YungLeChao
# @Date:   2016-02-20 15:13:05
# @Last Modified by:   YungLeChao
# @Last Modified time: 2016-02-21 22:06:38
# @Email: zhaoyongle77@gmail.com

from __future__ import print_function
from django import forms
from django.core.exceptions import ValidationError
from lists.models import Item

EMPTY_LIST_ERROR = "You can't have an empty list item"
DUPLICATE_ITEM_ERROR = "You've already got this in your list"


class ItemForm(forms.models.ModelForm):
    """docstring for ItemForm"""
    class Meta:
        model = Item
        fields = ('text',)
        widgets = {'text': forms.fields.TextInput(
            attrs={'placeholder': 'Enter a to-do item', 'class': 'form-control input-lg', }), }
        error_messages = {
            'text': {'required': EMPTY_LIST_ERROR}}

    def save(self, for_list):
        self.instance.list = for_list
        return super().save()


class ExistingListItemForm(ItemForm):
    """docstring for ExistingListItemForm"""

    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.list = for_list

    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict = {'text': [DUPLICATE_ITEM_ERROR]}
            self._update_errors(e)

    def save(self):
        return forms.models.ModelForm.save(self)
