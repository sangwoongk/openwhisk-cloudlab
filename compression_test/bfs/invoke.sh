#!/bin/bash

wsk -i action invoke bfs -p size 500000 $@
