#!/usr/bin/env python3

import argparse
from dmriprep.utils import vectors
from dipy.io import gradients as io

def normalize_bvecs(bvecs_path,bvals_path):
    
    bvals,bvecs = io.read_bvals_bvecs(bvals_path,bvecs_path)
    
    bvecs, _ = vectors.normalize_gradients(bvecs,bvals)
    
    fname_out = bvecs_path+'_norm'
    
    fid = open(fname_out, 'w')
    for iLine in range(bvecs.shape[0]):
        fid.write(' '.join(str(i) for i in bvecs[iLine, :])+'\n')
    fid.close()
    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('bvecs_path',help='file path to bvectors file')
    parser.add_argument('bvals_path',help='file path to bvalues file')
    args = parser.parse_args()

    normalize_bvecs(args.bvecs_path,args.bvals_path)


    ### example on how to run in shell
    # python normalize_bvecs.py ./bvec ./bval