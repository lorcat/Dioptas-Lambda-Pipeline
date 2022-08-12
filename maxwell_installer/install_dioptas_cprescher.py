#!/usr/bin/python3
import os
import sys
import subprocess
import re


class Installer(object):
    DESKTOP_FILE_DIOPTAS = """
[Desktop Entry]
Version=0.5.3
Type=Application
Terminal=false
Exec=/asap3/fs-sc/gpfs/common/scdd01/dioptas/latest/Dioptas
Name=Original Dioptas
Icon=/asap3/fs-sc/gpfs/common/scdd01/dioptas/latest/dioptas/resources/icons/icon.png
Categories=Science;
        """

    LINK_NAME_DIOPTAS = "Dioptas_cprescher.desktop"

    KEY_USERHOME = "HOME"

    def __init__(self):
        """
        Initialization
        """
        object.__init__(self)
        self.user_id = None

        setup = {self.LINK_NAME_DIOPTAS: self.DESKTOP_FILE_DIOPTAS}

        for (link, file_content) in setup.items():
            self.create_desktop_link(link, file_content)

    def create_desktop_link(self, link, content):
        """
        Creates desktop links using a filename and content
        :param link:
        :param content:
        :return:
        """
        try:
            base_dir = os.path.join(os.getenv(self.KEY_USERHOME), 'Desktop')

            if not os.path.exists(base_dir):
                os.makedirs(base_dir)

            fn = os.path.join(base_dir, link)

            breate = True
            if os.path.exists(fn) and (os.path.isfile(fn) or os.path.islink(fn)):
                print("Deleting an old link ({})".format(fn))
                self.delete_link(fn)
            elif os.path.exists(fn) and os.path.isdir(fn):
                print("Error: ({}) exists and it is not a file/link".format(fn))
                bcreate = False

            if breate:
                print("Creating a desktop link ({})..".format(fn))
                with open(fn, "w") as fh:
                    fh.write(content)


        except IOError as e:
            print("Error: {}".format(e))

    def delete_link(self, link_path):
        """
        Deletes a link path
        :param link_path:
        :return:
        """
        try:
            os.unlink(link_path)
        except IsADirectoryError:
            pass


def main():
    i = Installer()

if __name__ == "__main__":
    main()
