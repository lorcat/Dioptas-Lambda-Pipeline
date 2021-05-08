#!/usr/bin/python3
import os
import sys
import subprocess
import re


class Installer(object):
    DESKTOP_FILE_BATCHFIT = """
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=/usr/bin/bash -i /asap3/fs-sc/gpfs/common/scdd01/conda_env/batchfit/bin/activate_batchfit.sh
Name=P02.2 batch fit
Icon=/asap3/fs-sc/gpfs/common/scdd01/conda_env/batchfit/bin/batch_fit.png"
Categories=Science;
    """

    DESKTOP_FILE_DIOPTAS = """
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=/usr/bin/bash -i /asap3/fs-sc/gpfs/common/scdd01/conda_env/batchfit/bin/activate_batchfit.sh
Name=P02.2 batch fit
Icon=/asap3/fs-sc/gpfs/common/scdd01/conda_env/batchfit/bin/dioptas_pipeline.png
Categories=Science;
        """

    LINK_NAME_DIOPTAS = "Dioptas_mkarnevsky.desktop"
    LINK_NAME_BATCHFIT = "Batchfit_mkarnevsky.desktop"

    KEY_USERHOME = "HOME"

    def __init__(self):
        """
        Initialization
        """
        object.__init__(self)
        self.user_id = None

        setup = {self.LINK_NAME_DIOPTAS: self.DESKTOP_FILE_DIOPTAS, self.LINK_NAME_BATCHFIT: self.DESKTOP_FILE_BATCHFIT}

        for (link, file_content) in setup.items():
            self.create_desktop_link(link, file_content)

        # creates a link to users data
        self.create_data_link()

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
            print("Creating a desktop link ({})..".format(fn))
            with open(fn, "w") as fh:
                fh.write(content)

        except IOError as e:
            print("Error: {}".format(e))

    def create_data_link(self):
        """
        Creates a link to user's data simplifying navigation
        :return:
        """

        fn = os.path.join(os.getenv(self.KEY_USERHOME), 'Desktop', 'P02.2_data')
        start = "/asap3/petra3/gpfs/p02.2"
        print("Creating a data link ({} -> {})..".format(start, fn))
        subprocess.run(["ln", "-s", start, fn])


def main():
    i = Installer()

if __name__ == "__main__":
    main()
