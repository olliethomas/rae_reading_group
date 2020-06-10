# Active Learning

[![Paper](http://img.shields.io/badge/paper-arxiv.1001.2234-B31B1B.svg)](https://www.nature.com/articles/nature14539)
[![Conference](http://img.shields.io/badge/NeurIPS-2019-4b44ce.svg)](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018)
[![Conference](http://img.shields.io/badge/ICLR-2019-4b44ce.svg)](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018)
[![Conference](http://img.shields.io/badge/AnyConference-year-4b44ce.svg)](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018)
<!--
ARXIV
[![Paper](http://img.shields.io/badge/arxiv-math.co:1480.1111-B31B1B.svg)](https://www.nature.com/articles/nature14539)
-->



<!--
Conference
-->
</div>

## Description
What it does

## How to run
First, install dependencies
```bash
# clone project
git clone git@github.com:olliethomas/active_learning.git
cd active_learning

# install project
pip install -e .

# to contribute
pip install -e .[dev]
pre-commit install
 ```
 Next, navigate to `src/experiments/no_active_learning/mnist_baseline` and run it.
 ```bash
# module folder
cd research_seed/mnist/

# run module (example: mnist as your main contribution)
python mnist_trainer.py
```

## Main Contribution
List your modules here. Each module contains all code for a full system including how to run instructions.
- [MNIST](https://github.com/olliethomas/active_learning/tree/master/src/experiments/mnist)

## Baselines
List your baselines here.
- [MNIST_baseline](https://github.com/olliethomas/active_learning/tree/master/src/experiments/no_active_learning/mnist_baseline)

### Citation
```
@article{YourName,
  title={Your Title},
  author={Your team},
  journal={Location},
  year={Year}
}
```
