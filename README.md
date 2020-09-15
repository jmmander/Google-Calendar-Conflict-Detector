<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Google Calendar Conflict Detector</h3>

  <p align="center">
    A simple script that reads your google calender for the next day and checks for conflicts. In the case of a conflict an imessage will be sent to alert you of the conflict.
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)




<!-- GETTING STARTED -->
## Getting Started

### Compatibility

At this time the Conflict Detector is only compatible with iOS.

### Prerequisites

Python 2
An iCloud account
Access to imessage
A google account and calender
Google Python API Client

### Installation

1. Clone the repo
```sh
git clone https://github.com/jmmander/Google-Calendar-Conflict-Detector.git
```
2. Install Python if you don't have it already
```sh
yum install python
```
3. Open cal.py and update the phoneno variable to your phone number associated with your imessage account. It should be in the following format:
```sh
phoneno = "+15555555555" 
```
4. Go to https://developers.google.com/calendar/quickstart/python and follow the instructions in Step 1: Turn on the Google Calendar API. This should give you a credentials.json file. Save the file in the same folder as cal.py.

5. Go to the directry that holds cal.py. Run cal.py, this should open a browser window and prompt you to authorise the app to access your google calendar. Ensure you select the google account that your calendar is associated with.
```sh
> cd Users/Me/CalApp/
> python cal.py 
```
6. Update the file location in the schedule.sh file. This should point to the folder that holds cal.py.


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/jmmander/Google-Calendar-Conflict-Detector/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - Jacqueline Mander

Project Link: [https://github.com/jmmander/Google-Calendar-Conflict-Detector](https://github.com/+/Google-Calendar-Conflict-Detector)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Google Calendar API](https://developers.google.com/calendar/quickstart/python)
* [imessage](https://gist.github.com/24601/3482866d855bc5a62f5073120c154b93)






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jmmander/repo.svg?style=flat-square
[contributors-url]: https://github.com/jmmander/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jmmander/repo.svg?style=flat-square
[forks-url]: https://github.com/jmmander/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/jmmander/repo.svg?style=flat-square
[stars-url]: https://github.com/jmmander/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/jmmander/repo.svg?style=flat-square
[issues-url]: https://github.com/jmmander/repo/issues
[license-shield]: https://img.shields.io/github/license/jmmander/repo.svg?style=flat-square
[license-url]: https://github.com/jmmander/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jacqueline-m-4452911a4/
[product-screenshot]: images/screenshot.png