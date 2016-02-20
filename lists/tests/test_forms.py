#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: YungLeChao
# @Date:   2016-02-20 15:09:19
# @Last Modified by:   YungLeChao
# @Last Modified time: 2016-02-20 16:58:00
# @Email: zhaoyongle77@gmail.com

from __future__ import print_function
from django.test import TestCase

from lists.forms import EMPTY_LIST_ERROR, ItemForm


class ItemFormTest(TestCase):
    def test_form_renders_item_input_has_placeholder_and_css_classes(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'], [EMPTY_LIST_ERROR])
