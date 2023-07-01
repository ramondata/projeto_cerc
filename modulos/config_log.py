#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import logging
from datetime import date
from os import chdir

chdir("/Users/ramon/projeto_cerc/projeto_cerc/log/")

class log:

    hoje = date.today()

    def __init__(self):
        self._log = None
        self._name_file = "bikeshare_%s.log" % __class__.hoje
        self._path_log = "/Users/ramon/projeto_cerc/projeto_cerc/log/"
        self.set_basic()


    def set_basic(self):
        logging.basicConfig(filename='%s' % self._name_file,
                            filemode='w',
                            format='%(asctime)s - %(message)s')
        self._log = logging.getLogger()
        self._log.setLevel(logging.INFO)