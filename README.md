# Benchmark ISO 639

This project benchmarks the speed of various Python packages that implement the IS0 639 language representation standards.

## Usage

`tox` is required to set up an environment for each package.

```bash
$ tox -e iso-639
$ tox -e iso639-lang
$ tox -e python-iso639
```

## Results


| Package                                                           | part 3 → part 1      |
| :---------------------------------------------------------------- | :------------------: |
| [iso-639](https://pypi.org/project/iso-639/0.4.5/)                | 117,577              |
| [iso639-lang](https://pypi.org/project/iso639-lang/2.2.3/)        | **466,091**          |
| [python-iso639](https://pypi.org/project/python-iso639/2024.2.7/) | 1,228                |

*Table 1: Number of calls processed per second. The benchmark consists in 10,000 iterations on a Linux machine running Python 3.8.*