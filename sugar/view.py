# Copyright (C) 2009 One Laptop per Child
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
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA

import os
import gtk
import gobject
import gettext

from sugar.graphics import style
from sugar.graphics.icon import Icon

from jarabe.controlpanel.sectionview import SectionView
from jarabe.controlpanel.inlinealert import InlineAlert
from jarabe.model.session import get_session_manager
from jarabe import config

_ = lambda msg: gettext.dgettext('olpc-switch-desktop', msg)

class SwitchDesktop(SectionView):
    def __init__(self, model, alerts):
        SectionView.__init__(self)
        self._model = model
        self._switch_button_handler = None
        self._undo_button_handler = None
        self._fix_unknown_button_handler = None
        self._restart_button_handler = None

        self.set_border_width(style.DEFAULT_SPACING * 2)
        self.set_spacing(style.DEFAULT_SPACING)

        self._active_desktop_label = gtk.Label()
        self.pack_start(self._active_desktop_label, False)

        self._sugar_desc_label = gtk.Label(
            _("Sugar is the graphical user interface that you are looking at. "
              "It is a learning environment designed for children."))
        self._sugar_desc_label.set_size_request(gtk.gdk.screen_width() / 2, -1)
        self._sugar_desc_label.set_line_wrap(True)
        self.pack_start(self._sugar_desc_label, False)

        self._gnome_opt_label = gtk.Label(
            _("As an alternative to Sugar, you can switch to the GNOME "
              "desktop environment by clicking the button below."))
        self._gnome_opt_label.set_line_wrap(True)
        self._gnome_opt_label.set_size_request(gtk.gdk.screen_width() / 2, -1)
        self.pack_start(self._gnome_opt_label, False)

        self._restart_label = gtk.Label(
            _("Restart your computer to complete the change to the GNOME "
              "desktop environment."))
        self._restart_label.set_line_wrap(True)
        self._restart_label.set_size_request(gtk.gdk.screen_width() / 2, -1)
        self.pack_start(self._restart_label, False)

        self._undo_return_label = gtk.Label()
        self._undo_return_label.set_markup(
            _("Remember, you can return to Sugar later by clicking on the "
              "<b>Switch to Sugar</b> icon on the GNOME desktop. Or, click "
              "the <b>Cancel changes</b> button below if you would like to "
              "continue using Sugar as your desktop environment."))
        self._undo_return_label.set_line_wrap(True)
        self._undo_return_label.set_size_request(gtk.gdk.screen_width() / 2, -1)
        self.pack_start(self._undo_return_label, False)


        self._switch_align = gtk.Alignment(xalign=0.5, yalign=0.5)
        self.pack_start(self._switch_align)

        self._switch_button = gtk.Button(_("Switch to GNOME"))
        self._switch_button.set_image(Icon(icon_name="module-switch-desktop"))
        self._switch_align.add(self._switch_button)


        self._undo_align = gtk.Alignment(xalign=0.5, yalign=0.5)
        self.pack_start(self._undo_align)

        hbox = gtk.HButtonBox()
        hbox.set_layout(gtk.BUTTONBOX_END)
        hbox.set_spacing(style.DEFAULT_SPACING)
        self._undo_align.add(hbox)

        self._undo_button = gtk.Button(_("Cancel changes"))
        self._undo_button.set_image(Icon(icon_name="dialog-cancel"))
        hbox.add(self._undo_button)

        self._restart_button = gtk.Button(_("Restart now"))
        self._restart_button.set_image(Icon(icon_name="system-restart"))
        hbox.add(self._restart_button)

        self._unknown_align = gtk.Alignment(xalign=0.5, yalign=0.5)
        self.pack_start(self._unknown_align)

        self._fix_unknown_button = gtk.Button(_("Set Sugar as active desktop"))
        self._fix_unknown_button.set_image(Icon(icon_name="computer-xo"))
        self._unknown_align.add(self._fix_unknown_button)

        self._return_label = gtk.Label()
        self._return_label.set_markup(
            _("You can return to Sugar later, by clicking on the <b>Switch "
              "to Sugar</b> icon on the GNOME desktop. This is also available "
              "from the GNOME <b>Applications</b> menu."))
        self._return_label.set_line_wrap(True)
        self._return_label.set_size_request(gtk.gdk.screen_width() / 2, -1)
        self.pack_start(self._return_label, False)

        self._img_table = gtk.Table(rows=2, columns=2)
        self.pack_start(self._img_table, False);

        img_path = os.path.join(config.ext_path, 'cpsection', 'switchdesktop')

        img = gtk.image_new_from_file(os.path.join(img_path, 'sugar.png'));
        self._img_table.attach(img, 0, 1, 0, 1)
        label = gtk.Label("Sugar")
        self._img_table.attach(label, 0, 1, 1, 2)

        img = gtk.image_new_from_file(os.path.join(img_path, 'gnome.png'));
        self._img_table.attach(img, 1, 2, 0, 1)
        label = gtk.Label("GNOME")
        self._img_table.attach(label, 1, 2, 1, 2)

        self.setup()
        self._update()

    def setup(self):
        self._switch_button_handler =  \
                self._switch_button.connect('clicked', self._switch_button_cb)
        self._undo_button_handler = \
                self._undo_button.connect('clicked', self._undo_button_cb)
        self._fix_unknown_button_handler = \
                self._fix_unknown_button.connect('clicked', self._undo_button_cb)
        self._restart_button_handler = \
                self._restart_button.connect('clicked', self._restart_button_cb)
        # FIXME: disconnect anywhere?

    def undo(self):
        self._do_undo()
        self._update()

    def _update(self):
        self.hide_all()
        self.show()

        active = self._model.get_active_desktop()
        self._active_desktop_label.set_markup("<big>" + _("Active desktop environment: ")
            + "<b>" + active + "</b></big>")
        self._active_desktop_label.show()
        
        if active == "Sugar":
            self._sugar_desc_label.show()
            self._gnome_opt_label.show()
            self._switch_align.show_all()
            self._return_label.show()
        elif active == "GNOME":
            self._restart_label.show()
            self._undo_return_label.show()
            self._undo_align.show_all()
        elif active == "Unknown":
            self._unknown_align.show_all()

        self._img_table.show_all()

    def _do_undo(self):
        self._model.undo_switch()

    def _switch_button_cb(self, widget):
        self._model.switch_to_gnome()
        self._update()

    def _undo_button_cb(self, widget):
        self._do_undo()
        self._update()

    def _restart_button_cb(self, widget):
        get_session_manager().logout()

