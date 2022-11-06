# dmri-normalize-bvectors
This script (normalize_bvectors.py) will normalize the bvecs to be between -1 and 1.

This script first loads the bvectors and bvalues files (given to the function as the arguments bvecs_path and bvals_path) using dipy, then will invoke the "normalize_vectors" function found within dmriprep.utils.vectors class to normalize the bvectors.

The normalized bvectors will then be saved as a new file to the same location as the intput bvectors file, but with a '_norm' suffix.

## Dependencies
dipy (pip install dipy)
dmriprep (pip install dmriprep)

## How to run
python3 normalize_bvectors.py <path-to-bvecs_file> <path-to-bvals_file>
