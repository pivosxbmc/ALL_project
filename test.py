# -*- coding: utf-8 -*-
from multiprocessing import Process
from pptx import Presentation
from docx import Document
import sys
import importlib
#master更新
def test(aa):
	test = {'test':''.join((aa,"@qqqq.com")),'bb':'bb'}
	print(test['test'])
test('yzc')