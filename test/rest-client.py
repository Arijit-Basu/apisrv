#!/usr/bin/env python3
#
# Copyright (c) 2016 "Jonathan Yantis"
#
#    This program is free software: you can redistribute it and/or  modify
#    it under the terms of the GNU Affero General Public License, version 3,
#    as published by the Free Software Foundation.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    As a special exception, the copyright holders give permission to link the
#    code of portions of this program with the OpenSSL library under certain
#    conditions as described in each individual source file and distribute
#    linked combinations including the program with the OpenSSL library. You
#    must comply with the GNU Affero General Public License in all respects
#    for all of the code used other than as permitted herein. If you modify
#    file(s) with this exception, you may extend this exception to your
#    version of the file(s), but you are not obligated to do so. If you do not
#    wish to do so, delete this exception statement from your version. If you
#    delete this exception statement from all source files in the program,
#    then also delete it in the license file.
#
#
"""
REST API Sample Client
"""
import requests
import json

user = 'testuser'
passwd = 'testpass'
url = 'http://localhost:5000'

# Make a request (don't verify cert if SSL)
r = requests.get(url + '/test/api/v1.0/info?var=testvar', auth=(user, passwd), verify=False)

# Check for proper response
if r.status_code == 200:

    # JSON Dict
    response = r.json()

    # Dump JSON in pretty format
    print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))
else:
    print("Request Error:", r.status_code, r.text)
