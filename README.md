<a name="readme-top"></a>

<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url] -->
[![MIT License][license-shield]][license-url]
<!-- [![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/efstratios97/ltep_athena_api">
    <img src="https://www.ltep-technologies.com/wp-content/uploads/2022/06/LTEP_LOGO_21-3.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">EasyFileWatcher</h3>

  <p align="center">
    The official API
    <br />
    <a href="https://github.com/efstratios97/EasyFileWatcher/tree/main/docs"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/efstratios97/EasyFileWatcher">View Demo</a>
    -
    <a href="https://github.com/efstratios97/EasyFileWatcher/issues">Report Bug</a>
    -
    <a href="https://github.com/efstratios97/EasyFileWatcher/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://www.ltep-technologies.com/wp-content/uploads/2022/06/ATHINA_LOGO-3.png) -->

This is yet another FileWatcher. Developed to run smoothier, without sideffects and give more control to the developer in comparison to common packages for such purpose.
<table>
<tr>
<th>Features</th>
<th>EasyFileWatcher</th>
<th>Others (Watchdog etc.)</th>
</th>
<tr>
<td><strong>Schedule Start & End Time</strong></td>
<td><img src="https://img.icons8.com/emoji/48/000000/check-mark-emoji.png"/></td>
<td><img src="https://img.icons8.com/external-bearicons-flat-bearicons/46/000000/external-block-essential-collection-bearicons-flat-bearicons.png"/></td>
</tr>
<tr>
<td><strong>Pause & Resume</strong></td>
<td><img src="https://img.icons8.com/emoji/48/000000/check-mark-emoji.png"/></td>
<td><img src="https://img.icons8.com/external-bearicons-flat-bearicons/46/000000/external-block-essential-collection-bearicons-flat-bearicons.png"/></td>
</tr>
<tr>
<td><strong>By default runs in Background</strong></td>
<td><img src="https://img.icons8.com/emoji/48/000000/check-mark-emoji.png"/></td>
<td><img src="https://img.icons8.com/external-bearicons-flat-bearicons/46/000000/external-block-essential-collection-bearicons-flat-bearicons.png"/></td>
</tr>
<tr>
<td><strong>Configurable Pooling Time</strong></td>
<td><img src="https://img.icons8.com/emoji/48/000000/check-mark-emoji.png"/></td>
<td><img src="https://img.icons8.com/external-bearicons-flat-bearicons/46/000000/external-block-essential-collection-bearicons-flat-bearicons.png"/></td>
</tr>
<td><strong>Persist FileWatcher Tasks</strong></td>
<td><img src="https://img.icons8.com/emoji/48/000000/check-mark-emoji.png"/></td>
<td><img src="https://img.icons8.com/external-bearicons-flat-bearicons/46/000000/external-block-essential-collection-bearicons-flat-bearicons.png"/></td>
</tr>
</table>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][Python]][Python-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
```python
from easyfilewatcher.EasyFileWatcher import EasyFileWatcher


def print_msg(msg: str):
    print(msg)


if __name__ == "__main__":
    filewatcher = EasyFileWatcher()
    filewatcher.add_directory_to_watch(directory_path="your\\directory",
                                       directory_watcher_id="my_id", callback=print_msg, 
                                       callback_param={'msg': 'hi'}, event_on_deletion=False)
    while(True):
        pass
```

### Prerequisites

Python >=3.8


### Installation


pip install EasyFileWatcher

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The Documentation you can find here [docs](https://easyfilewatcher.readthedocs.io/en/latest/index.html)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



ROADMAP
## Roadmap

- [x] Add Changelog

See the [open issues](https://github.com/efstratios97/EasyFileWatcher/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Efstratios Pahis - [@ltepTechnologies](https://ltep-technologies.com) - 

Project Link: [https://github.com/efstratios97/EasyFileWatcher](https://github.com/efstratios97/EasyFileWatcher)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

LTEP Technologies UG (haftungsbeschränkt)
www.ltep-technologies.com


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: https://www.ltep-technologies.com/wp-content/uploads/2022/06/ATHINA_LOGO-3.png
[Python]: https://www.python.org/static/community_logos/python-powered-w-100x40.png
[Python-url]: https://www.python.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 