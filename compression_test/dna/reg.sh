#!/bin/bash

wsk -i action update dna __main__.py --docker sangroad/dna:1.0.0 --web false --timeout 300000 --memory 512
