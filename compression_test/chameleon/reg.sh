#!/bin/bash

wsk -i action update cham __main__.py --docker sangroad/chameleon:1.0.0 --web false --timeout 300000 --memory 512
