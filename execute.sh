# Exit on error
set -o errexit

# Execute notebooks in order
jupyter nbconvert --inplace --execute --ExecutePreprocessor.timeout=-1 --ExecutePreprocessor.kernel_name=python *.ipynb

