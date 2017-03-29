# Exploring which licenses authors choose for their bioRxiv preprints

[![Latest Zenodo DOI](https://zenodo.org/badge/74924525.svg)](https://zenodo.org/badge/latestdoi/74924525)

This repository analyzes the licensing of [_bioRxiv_](http://biorxiv.org/ "The
Preprint Server for Biology") preprints. The _bioRxiv_ data was generated Omnes
Res for [PrePubMed](http://www.prepubmed.org/) — a search engine for biomedical
preprints.

The findings from this analysis are summarized in a blog post titled [The
licensing of _bioRxiv_ preprints](http://blog.dhimmel.com/biorxiv-licenses/
"Satoshi Village"), which analyzes preprints through but not past November 2016.

## Binder

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/dhimmel/biorxiv-licenses)

Click the badge above to launch this repository in binder, which allows you to
interact with the jupyter notebooks. Note that the mybinder.org build may be
outdated. You can [rebuild it
here](http://mybinder.org/status/dhimmel/biorxiv-licenses). Binder uses the
[`Dockerfile`](Dockerfile) in this repository to create a custom Docker image
with the environment for this analysis.

## Environment

This repository uses [conda](http://conda.pydata.org/docs/) to manage its environment as specified in [`environment.yml`](environment.yml).
Install the environment with:

```sh
conda env create --file=environment.yml
```

Then use `source activate biorxiv-licenses` and `source deactivate` to activate or deactivate the environment.

## Notebooks

The analysis is performed by running the following notebooks:

+ [`1.download.ipynb`](1.download.ipynb) retrieves _bioRxiv_ data from PrePubMed.
+ [`2.create-figure-data.ipynb`](2.create-figure-data.ipynb) creates JSON data
files for vega-lite.

[`execute.sh`](execute.sh) automates running the analysis for command line
usage.

## License

This repository is dual licensed as [BSD 3-Clause](LICENSE-BSD.md) and [CC0
1.0](LICENSE-CC0.md), meaning any repository content can be used under either
license. This licensing arrangement ensures source code is available under an
[OSI-approved License](https://opensource.org/licenses/alphabetical), while
non-code content — such as figures, data, and documentation — is maximally
reusable under a public domain dedication.
