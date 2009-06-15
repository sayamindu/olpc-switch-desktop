# Copyright (C) 2009 One Laptop Per Child
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

ACTIVE_DESKTOP_FILE = "/home/olpc/.olpc-active-desktop"

def _do_switch(target):
    fd = open(ACTIVE_DESKTOP_FILE, "w")
    fd.write(target)
    fd.close()


def switch_to_gnome():
    _do_switch("gnome")

def undo_switch():
    _do_switch("sugar")

def get_active_desktop():
    fd = open(ACTIVE_DESKTOP_FILE, "r")
    desktop = fd.read().strip()
    fd.close()
    if desktop == "sugar":
        return "Sugar"
    elif desktop == "gnome":
        return "GNOME"
    else:
        return "Unknown"


