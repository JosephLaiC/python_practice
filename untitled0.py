#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 23:53:20 2022

@author: chiehyulai
"""

import pandas
import pybedtools

root_dir="/Users/chiehyulai/Documents/Figure/6mA/output/1.origin/"
out_dir="Promoter/protein_coding_ENSG00000004455_AK2_Region_11169/"

with open(root_dir + out_dir + "fasta/background.fa") as f:
    lines = [line for line in f]
fasta=lines[1]


fasta[0:6] = print
