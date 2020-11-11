# tiger-calculator

A simple Python3 program to calculate TIGER rates (Cummins & McInerney 2011). Currently supported formats: FASTA, CLDF, harvest-style CSV. Use `tiger-calculator.py` or `tiger-calculator.py --help` to see available options.

usage: tiger-calculator.py [-h] [-f FORMAT] [-i IGNORED_CHARS]
                           [-x EXCLUDED_TAXA] [-p N_PROCESSES] [-n]
                           [-s SYNONYM_STRATEGY]
                           IN_FILE

Simple TIGER rates calculator.

positional arguments:
  IN_FILE               Input file to analyze.

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        Specify input format. Available formats: fasta, cldf,
                        harvest
  -i IGNORED_CHARS, --ignored-characters IGNORED_CHARS
                        A comma-separated list of ignored characters. Missing
                        characters should be included here.
  -x EXCLUDED_TAXA, --excluded-taxa EXCLUDED_TAXA
                        A comma-separated list of taxa excluded from the
                        calculations.
  -p N_PROCESSES, --processes N_PROCESSES
                        Number of processes (threads) to use. Default: 4 (the
                        detected number of logical CPUs).
  -n, --named-characters
                        Include a column identifying which TIGER rate belongs
                        to which aligned character.
  -s SYNONYM_STRATEGY, --synonym-strategy SYNONYM_STRATEGY
                        Strategy for resolving synonyms. Available strategies:
                        random, minimum, maximum.
