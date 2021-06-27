```
Microsoft Windows [Version 10.0.19042.1052]
(c) Microsoft Corporation. All rights reserved.

C:\Users\DELL>cd Opendiagram

C:\Users\DELL\openDiagram>git pull
remote: Enumerating objects: 29, done.
remote: Counting objects: 100% (29/29), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 20 (delta 14), reused 16 (delta 10), pack-reused 0
Unpacking objects: 100% (20/20), 26.65 KiB | 16.00 KiB/s, done.
From https://github.com/petermr/openDiagram
   96e060761..7235fb9ad  master     -> origin/master
Updating 96e060761..7235fb9ad
Fast-forward
 physchem/python/pyami.py                     | 263 ++++++++---
 physchem/python/xml_lib.py                   |   5 +-
 physchem/resources/oil26/files/xml_files.txt | 677 ++++++++++++++++++++++++++-
 3 files changed, 889 insertions(+), 56 deletions(-)

C:\Users\DELL\openDiagram>cd..

C:\Users\DELL>cd CEVOpen

C:\Users\DELL\CEVOpen>git pull
remote: Enumerating objects: 30, done.
remote: Counting objects: 100% (30/30), done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 23 (delta 12), reused 5 (delta 4), pack-reused 0
Unpacking objects: 100% (23/23), 1.16 MiB | 78.00 KiB/s, done.
From https://github.com/petermr/CEVOpen
   4d3a8f811b..90713de5eb  master     -> origin/master
Updating 4d3a8f811b..90713de5eb
Fast-forward
 classification/MLcode.ipynb              |   5882 +
 classification/README.md                 |     29 +
 dictionary/eoCompound/plant_compound.xml |    105 +-
 dictionary/eoGene/eo_Gene_identifier.xml | 159795 ++++++++++++++++++++++++++++
 4 files changed, 165707 insertions(+), 104 deletions(-)
 create mode 100644 classification/MLcode.ipynb
 create mode 100644 dictionary/eoGene/eo_Gene_identifier.xml

C:\Users\DELL\CEVOpen>
C:\Users\DELL\CEVOpen>
C:\Users\DELL\CEVOpen>
C:\Users\DELL\CEVOpen>
C:\Users\DELL\CEVOpen>
C:\Users\DELL\CEVOpen>
C:\Users\DELL\CEVOpen>
C:\Users\DELL\CEVOpen>
C:\Users\DELL\CEVOpen>
C:\Users\DELL\CEVOpen>cd ..

C:\Users\DELL>cd Dcitionary
The system cannot find the path specified.

C:\Users\DELL>cd dcitionary
The system cannot find the path specified.

C:\Users\DELL>cd dictionary

C:\Users\DELL\dictionary>git pull
remote: Enumerating objects: 24, done.
remote: Counting objects: 100% (24/24), done.
remote: Compressing objects: 100% (14/14), done.
remote: Total 24 (delta 13), reused 21 (delta 10), pack-reused 0
Unpacking objects: 100% (24/24), 129.17 KiB | 73.00 KiB/s, done.
From https://github.com/petermr/dictionary
   0087444b..cb09f20d  main       -> origin/main
Updating 0087444b..cb09f20d
Fast-forward
 ...s_committee_frontiers_spacy_entities_column.csv | 479 ++++++++++++++++++++
 .../ethics_statement_frontiers_1000_spacy.csv      | 489 +++++++++++++++++++++
 ...cs_statement_frontiers_10_labelled_entities.csv |   1 -
 ...s_statement_frontiers_frontiers_50_scispacy.csv |  50 +++
 ...hics_statement_frontiers_frontiers_50_spacy.csv |  50 +++
 .../ethics_statement_generic.ipynb                 |  17 +-
 .../ethics_statement_generic.py                    |  39 +-
 .../ethics_statement_ngram.ipynb                   | 217 +++++++++
 .../ethics_statement_project.md                    |  98 +++--
 9 files changed, 1396 insertions(+), 44 deletions(-)
 create mode 100644 ethics_statement_project/ethics_committee_frontiers_spacy_entities_column.csv
 create mode 100644 ethics_statement_project/ethics_statement_frontiers_1000_spacy.csv
 delete mode 100644 ethics_statement_project/ethics_statement_frontiers_10_labelled_entities.csv
 create mode 100644 ethics_statement_project/ethics_statement_frontiers_frontiers_50_scispacy.csv
 create mode 100644 ethics_statement_project/ethics_statement_frontiers_frontiers_50_spacy.csv
 create mode 100644 ethics_statement_project/ethics_statement_ngram.ipynb

C:\Users\DELL\dictionary>cd
C:\Users\DELL\dictionary

C:\Users\DELL\dictionary>cd..

C:\Users\DELL>cd pygetpapers

C:\Users\DELL\pygetpapers>git pull
remote: Enumerating objects: 69, done.
remote: Counting objects: 100% (69/69), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 48 (delta 34), reused 47 (delta 33), pack-reused 0
Unpacking objects: 100% (48/48), 87.97 KiB | 17.00 KiB/s, done.
From https://github.com/petermr/pygetpapers
   5cbf751..d72c62c  main       -> origin/main
Updating 5cbf751..d72c62c
Fast-forward
 build/lib/pygetpapers/arxiv.py                     |  24 +-
 build/lib/pygetpapers/config.ini                   |   2 +-
 build/lib/pygetpapers/crossref.py                  |   1 -
 build/lib/pygetpapers/download_tools.py            |  28 +-
 build/lib/pygetpapers/europe_pmc.py                | 403 +++++++++++++++
 build/lib/pygetpapers/pygetpapers.py               | 550 ++++-----------------
 dist/pygetpapers-0.0.4.5-py3.7.egg                 | Bin 38447 -> 0 bytes
 dist/pygetpapers-0.0.4.6-py3.7.egg                 | Bin 38556 -> 0 bytes
 dist/pygetpapers-0.0.4.7-py3.7.egg                 | Bin 38501 -> 0 bytes
 dist/pygetpapers-0.0.4.8-py3.7.egg                 | Bin 0 -> 39465 bytes
 dist/pygetpapers-0.0.4.9-py3.7.egg                 | Bin 0 -> 39493 bytes
 docs/source/arxiv.rst                              |   7 +
 docs/source/conf.py                                |   2 +-
 docs/source/crossref.rst                           |   7 +
 docs/source/index.rst                              |   2 +
 pygetpapers.egg-info/PKG-INFO                      |   2 +-
 .../__pycache__/download_tools.cpython-37.pyc      | Bin 12664 -> 13705 bytes
 pygetpapers/__pycache__/europe_pmc.cpython-37.pyc  | Bin 4330 -> 17633 bytes
 pygetpapers/__pycache__/pygetpapers.cpython-37.pyc | Bin 22595 -> 9910 bytes
 pygetpapers/arxiv.py                               |  24 +-
 pygetpapers/config.ini                             |   2 +-
 pygetpapers/crossref.py                            |   1 -
 pygetpapers/download_tools.py                      |  28 +-
 pygetpapers/europe_pmc.py                          | 403 +++++++++++++++
 pygetpapers/pygetpapers.py                         | 550 ++++-----------------
 25 files changed, 1090 insertions(+), 946 deletions(-)
 delete mode 100644 dist/pygetpapers-0.0.4.5-py3.7.egg
 delete mode 100644 dist/pygetpapers-0.0.4.6-py3.7.egg
 delete mode 100644 dist/pygetpapers-0.0.4.7-py3.7.egg
 create mode 100644 dist/pygetpapers-0.0.4.8-py3.7.egg
 create mode 100644 dist/pygetpapers-0.0.4.9-py3.7.egg
 create mode 100644 docs/source/arxiv.rst
 create mode 100644 docs/source/crossref.rst

C:\Users\DELL\pygetpapers>


```





