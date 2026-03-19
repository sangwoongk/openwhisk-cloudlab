#!/bin/bash

wsk -i action update imgr __main__.py --docker sangroad/imgr:1.0.1 --web false --timeout 300000 --memory 512
