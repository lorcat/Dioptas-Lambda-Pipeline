# Dioptas-Lambda-Pipeline user instructions

The documentation  presented below provides a user with code installation instructions, links to the compiled Win executable and the instructions how to setup links for using the special Dioptas distribution at DESY Maxwell cluster.

## Windows statically built distribution

The most recent compilation of the windows distributive can be found [here](https://github.com/karnevskiy/Dioptas/releases/tag/0.5.1-05).

## Quick installation on Maxwell Cluster - code from Mikhail Karnevsky
The [code](https://github.com/lorcat/Dioptas-Lambda-Pipeline/blob/main/maxwell_installer/install_dioptas.py) provided inside the folder **[maxwell_installer](https://github.com/lorcat/Dioptas-Lambda-Pipeline/tree/main/maxwell_installer)** can be downloaded and executed via
    
    module load anaconda3/5.2
    conda init bash
    wget https://raw.githubusercontent.com/lorcat/Dioptas-Lambda-Pipeline/main/maxwell_installer/install_dioptas.py
	python3 install_dioptas.py

A more difficult way would be:

    module load anaconda3/5.2
    conda init bash
    cd ~/Downloads
    git clone https://github.com/lorcat/Dioptas-Lambda-Pipeline
    cd Dioptas-Lambda-Pipeline/maxwell_installer
    python3 install_dioptas.py

It will setup user links to the /gpfs data and the Dioptas on the virtual desktop of the user run.

## Quick installation on Maxwell Cluster - precompiled Dioptas from Clemens Prescher

[Clemens Prescher ](http://www.clemensprescher.com/programs/dioptas) made the high pressure community a huge favor and presented an updated version of his  Dioptas, precompiled for different OS.
Within the operations of scientific computing group of DESY (FS-SC) we placed a copy on Maxwell cluster. The following code helps with installation of a Desktop icon on Maxwell cluster.

    wget https://raw.githubusercontent.com/lorcat/Dioptas-Lambda-Pipeline/main/maxwell_installer/install_dioptas_cprescher.py
	python3 install_dioptas_cprescher.py