# Dioptas-Lambda-Pipeline user instructions

The documentation  presented below provides a user with code installation instructions, links to the compiled Win executable and the instructions how to setup links for using the special Dioptas distribution at DESY Maxwell cluster.

## Windows statically built distribution

The most recent compilation of the windows distributive can be found [here](https://github.com/karnevskiy/Dioptas/releases/tag/0.5.1-05).

## Quick installation on Maxwell Cluster
The [code](https://github.com/lorcat/Dioptas-Lambda-Pipeline/blob/main/maxwell_installer/install_dioptas.py) provided inside the folder **[maxwell_installer](https://github.com/lorcat/Dioptas-Lambda-Pipeline/tree/main/maxwell_installer)** can be downloaded and executed via
    
    wget https://raw.githubusercontent.com/lorcat/Dioptas-Lambda-Pipeline/main/maxwell_installer/install_dioptas.py
	python3 install_dioptas.py

A more difficult way would be:

    cd ~/Downloads
    git clone https://github.com/lorcat/Dioptas-Lambda-Pipeline
    cd Dioptas-Lambda-Pipeline/maxwell_installer
    python3 install_dioptas.py

It will setup user links to the /gpfs data and the Dioptas on the virtual desktop of the user run.

## Installation of special Dioptas version via conda
This dioptas version is developed by Mikhail Karnevsky. The code can be installed via [Anaconda](https://www.anaconda.com/). At the moment installation channels for Windows and Linux are available. The following lines indicate code which should be run on the command line.

	conda create -n dioptas_lambda_pipeline integration_pipeline -c karnevskiy -c cprescher --yes
	conda activate dioptas_lambda_pipeline
	dioptas

These are the channels which will be updated on a faster pace than the Windows static builds.