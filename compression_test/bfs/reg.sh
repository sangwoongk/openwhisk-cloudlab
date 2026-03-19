#!/bin/bash

wsk -i action update bfs __main__.py --docker sangroad/graph:1.0.0 --web false --timeout 300000 --memory 512
