#!/usr/bin/env bash

egrep -o -e '-?[0-9]+' input | paste -sd+ | bc
