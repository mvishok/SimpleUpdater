<br/>
<p align="center">
  <h3 align="center">Simple Updater</h3>

  <p align="center">
    A simple updater module for seamless updates
    <br/>
    <br/>
    <a href="https://github.com/mvishok/SimpleUpdater/issues">Report Bug</a>
    .
    <a href="https://github.com/mvishok/SimpleUpdater/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/mvishok/SimpleUpdater/total) ![Contributors](https://img.shields.io/github/contributors/mvishok/SimpleUpdater?color=dark-green) ![Forks](https://img.shields.io/github/forks/mvishok/SimpleUpdater?style=social) ![Stargazers](https://img.shields.io/github/stars/mvishok/SimpleUpdater?style=social) ![Issues](https://img.shields.io/github/issues/mvishok/SimpleUpdater) ![License](https://img.shields.io/github/license/mvishok/SimpleUpdater) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
* [Roadmap](#roadmap)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

![Screen Shot](https://raw.githubusercontent.com/mvishok/SimpleUpdater/master/screenshot.png)

SimpleUpdater is a lightweight Python library designed to simplify the process of updating software applications. It provides a seamless and efficient way for programmers to integrate automatic updates into their projects.

With SimpleUpdater, developers can easily incorporate version checking and update functionality into their applications. The library allows checking for the availability of new updates by comparing the current version with a specified version URL. If an update is available, SimpleUpdater facilitates the download and installation of the update, ensuring that users have the latest features and bug fixes.

Key Features:
- Seamless integration: SimpleUpdater can be effortlessly integrated into existing Python projects, enabling smooth and hassle-free updates.
- Version checking: The library compares the current version of the application with the version obtained from a specified URL, allowing for efficient update detection.
- Update management: SimpleUpdater simplifies the process of downloading and installing updates, ensuring a streamlined user experience.
- Customizable behavior: Developers have the flexibility to define the actions to be taken before and after the update process, providing control over the update flow.

SimpleUpdater is particularly suitable for Windows applications, providing support and convenience for software running on the Windows operating system.

License: SimpleUpdater is released under the MIT license, which allows for open-source use, modification, and distribution of the library.

Please feel free to modify the description to best represent your project, highlighting its unique features and benefits.


## Built With

- Python: SimpleUpdater is written in [Python](https://www.python.org/), a versatile and powerful programming language.
- [requests](https://pypi.org/project/requests/): The `requests` library is used for making HTTP requests to fetch version information and download updates.
- [EasyGUI](https://pypi.org/project/easygui/): The `EasyGUI` library is utilized for creating user-friendly graphical interfaces, including message boxes and dialogs.
- [setuptools](https://pypi.org/project/setuptools/): The `setuptools` library is used for packaging and distributing the SimpleUpdater library.
- [PyPI](https://pypi.org/): The Python Package Index (PyPI) is the repository where the SimpleUpdater library is hosted and made available for installation.


## Getting Started

To get started with SimpleUpdater, follow the steps below:

1. **Installation**: Install SimpleUpdater library using pip:
```sh
pip install SimpleUpdater
```

2. **Importing**: Import the SimpleUpdater module in your Python script:
```py
from SimpleUpdater import SimpleUpdater
```

3. **Usage**: Utilize the SimpleUpdater functionality in your application. Here's a simple example:

`example.py`:
```py
from SimpleUpdater import SimpleUpdater

# Current version of the application
CURRENT_VERSION = '0.0.1'

# URL to fetch the latest version information
VERSION_URL = 'http://localhost/file/ver.txt'

SimpleUpdater.checkForUpdates(CURRENT_VERSION, VERSION_URL)

#...
```

`ver.txt`:
```text
1.5.0
normal
http://localhost/file/updater.exe
```


### Prerequisites

Before using SimpleUpdater, ensure that you have the following prerequisites installed:

- Python: SimpleUpdater requires Python 3.x. You can download Python from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python installed, you can proceed with installing SimpleUpdater and incorporating it into your Python projects.


## Roadmap

See the [open issues](https://github.com/mvishok/SimpleUpdater/issues) for a list of proposed features (and known issues).

## License

Distributed under the MIT License. See [LICENSE](https://github.com/mvishok/SimpleUpdater/blob/main/LICENSE.md) for more information.

## Authors

* **Vishok M** - *Student* - [Vishok M](https://github.com/mvishok/) - *Built SimpleUpdater*