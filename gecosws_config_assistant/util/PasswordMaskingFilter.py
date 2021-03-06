# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

# This file is part of Guadalinex
#
# This software is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this package; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

__author__ = "Jose Manuel Rodriguez Caro <jmrodriguez@solutia-it.es>"
__copyright__ = "Copyright (C) 2015, Junta de Andalucía" + \
    "<devmaster@guadalinex.org>"
__license__ = "GPL-2"

import logging

class PasswordMaskingFilter(logging.Filter):
    
    def filter(self, record):
        ''' Avoiding sending password in plain text to logs '''
        if isinstance(record.args, dict):
            for k in record.args.keys():
                record.args[k] = self.privatize(record.args[k])
        else:
            record.args = tuple(self.privatize(arg) for arg in record.args)

        return True

    def privatize(self, msg):
        ''' Hiding password with text '''

        if msg.startswith("net ads join") or msg.startswith("net ads leave"):
            index = msg.index('%')
            if index != -1:
                msg = msg.replace(msg[index+1:],"<*** PASSWORD ***>")
        return msg
