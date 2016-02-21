#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: YungLeChao
# @Date:   2016-02-20 15:13:05
# @Last Modified by:   YungLeChao
# @Last Modified time: 2016-02-20 22:39:49
# @Email: zhaoyongle77@gmail.com

from __future__ import print_function
from django import forms
from lists.models import Item

EMPTY_LIST_ERROR = "You can't have an empty list item"


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
