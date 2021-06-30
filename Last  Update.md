```
C:\Users\DELL>cd OpenDiagram

C:\Users\DELL\openDiagram>git pull
remote: Enumerating objects: 18, done.
remote: Counting objects: 100% (18/18), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 12 (delta 9), reused 8 (delta 5), pack-reused 0
Unpacking objects: 100% (12/12), 2.91 KiB | 3.00 KiB/s, done.
From https://github.com/petermr/openDiagram
   34fbf70eb..b7a39375c  master     -> origin/master
Updating 34fbf70eb..b7a39375c
Fast-forward
 physchem/python/pyami.py                     | 276 ++++++++---
 physchem/resources/oil26/files/xml_files.txt | 676 ---------------------------
 2 files changed, 214 insertions(+), 738 deletions(-)
 delete mode 100644 physchem/resources/oil26/files/xml_files.txt

C:\Users\DELL\openDiagram>cd..

C:\Users\DELL>cd CEVOpen

C:\Users\DELL\CEVOpen>git pull
remote: Enumerating objects: 73, done.
remote: Counting objects: 100% (73/73), done.
remote: Compressing objects: 100% (50/50), done.
remote: Total 60 (delta 43), reused 8 (delta 6), pack-reused 0
Unpacking objects: 100% (60/60), 185.01 KiB | 34.00 KiB/s, done.
From https://github.com/petermr/CEVOpen
   fb34c2a7fa..299675b02d  master     -> origin/master
Updating fb34c2a7fa..299675b02d
Fast-forward
 .../Invasive_species/Plant_invasive (1).xlsx       |    Bin 0 -> 18552 bytes
 .../eo_activity/Summary of Activity dictionary.md  |      4 +-
 dictionary/eoCompound/plant_compound.xml           |      2 -
 ...t_compounds.xml => plant_compound_synonyms.xml} |      0
 dictionary/eoGene/eo_Gene.xml                      |  35508 +++-
 dictionary/eoGene/eo_Gene_identifier.xml           | 159795 ------------------
 minicorpora/invasive.md                            |      4 +-
 7 files changed, 35503 insertions(+), 159810 deletions(-)
 create mode 100644 dictionary/Invasive_species/Plant_invasive (1).xlsx
 rename dictionary/eoCompound/work/{plant_compounds.xml => plant_compound_synonyms.xml} (100%)
 delete mode 100644 dictionary/eoGene/eo_Gene_identifier.xml

C:\Users\DELL\CEVOpen>cd..

C:\Users\DELL>cd dictionary

C:\Users\DELL\dictionary>git pull
remote: Enumerating objects: 88, done.
remote: Counting objects: 100% (88/88), done.
remote: Compressing objects: 100% (61/61), done.
remote: Total 88 (delta 48), reused 65 (delta 25), pack-reused 0
Unpacking objects: 100% (88/88), 112.64 KiB | 25.00 KiB/s, done.
From https://github.com/petermr/dictionary
   cb09f20d..665825bc  main       -> origin/main
Updating cb09f20d..665825bc
Fast-forward
 .../e_cancer_clinical_trial_30.csv                 |  21 ++
 .../e_cancer_clinical_trial_50_20210629.csv        |  70 ++++++
 .../e_cancer_clinical_trial_50_20210629_2.csv      |   6 +
 .../e_cancer_clinical_trial_50_20210629_cancer.csv |   6 +
 .../e_cancer_clinical_trial_50_spacy.csv           |   5 +
 .../e_cancer_trial_30_spacy.csv                    |   1 +
 .../ethics_statement_Hindawi_50_spacy.csv          |   2 +
 ...ics_statement_elsivier_10_labelled_entities.csv |  26 +++
 .../ethics_statement_frontiers_100.csv             |   0
 .../ethics_statement_frontiers_100_20210629.csv    | 101 +++++++++
 .../ethics_statement_frontiers_100_20210629_2.csv  | 101 +++++++++
 .../ethics_statement_frontiers_100_intro_spacy.csv | 184 ++++++++++++++++
 ...thics_statement_frontiers_100_methods_spacy.csv |  32 +++
 .../ethics_statement_frontiers_100_spacy.csv       |  32 +++
 ...hics_statement_frontiers_100_spacy_20210625.csv | 101 +++++++++
 .../ethics_statement_frontiers_20_spacy.csv        |  20 ++
 .../ethics_statement_frontiers_30.csv              |  79 +++++++
 .../ethics_statement_frontiers_30_20210630.csv     |  79 +++++++
 .../ethics_statement_frontiers_30_spacy.csv        |  30 +++
 ...s_statement_frontiers_frontiers_50_scispacy.csv |   0
 ...hics_statement_frontiers_frontiers_50_spacy.csv |   0
 ...ics_statement_frontiers_springer_nature_100.csv |   1 +
 .../ethics_statement_clustering.py                 |  79 +++++++
 ...s_statement_frontiers_100_labelled_entities.csv |   9 -
 .../ethics_statement_generic.py                    | 244 ++++++++++++++-------
 .../ethics_statement_project.md                    |  46 ++--
 .../ethics_statement_project/ethics_commitee.xml   |  18 ++
 .../ethics_statement_workflow.PNG                  | Bin 0 -> 52508 bytes
 ethics_statement_project/project_workflow.md       |  23 ++
 ethics_statement_project/prototype.py              |   5 +
 ethics_statement_project/requirements.txt          |   6 +
 ethics_statement_project/testing_pke.py            |  23 ++
 32 files changed, 1244 insertions(+), 106 deletions(-)
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/e_cancer_clinical_trial_30.csv
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/e_cancer_clinical_trial_50_20210629.csv
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/e_cancer_clinical_trial_50_20210629_2.csv
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/e_cancer_clinical_trial_50_20210629_cancer.csv
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/e_cancer_clinical_trial_50_spacy.csv
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/e_cancer_trial_30_spacy.csv
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/ethics_statement_Hindawi_50_spacy.csv
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/ethics_statement_elsivier_10_labelled_entities.csv
 rename ethics_statement_project/{ => __ethics_statement_generic_results_csv}/ethics_statement_frontiers_100.csv (100%)
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/ethics_statement_frontiers_100_20210629.csv
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/ethics_statement_frontiers_100_20210629_2.csv
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/ethics_statement_frontiers_100_intro_spacy.csv
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/ethics_statement_frontiers_100_methods_spacy.csv
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/ethics_statement_frontiers_100_spacy.csv
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/ethics_statement_frontiers_100_spacy_20210625.csv
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/ethics_statement_frontiers_20_spacy.csv
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/ethics_statement_frontiers_30.csv
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/ethics_statement_frontiers_30_20210630.csv
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/ethics_statement_frontiers_30_spacy.csv
 rename ethics_statement_project/{ => __ethics_statement_generic_results_csv}/ethics_statement_frontiers_frontiers_50_scispacy.csv (100%)
 rename ethics_statement_project/{ => __ethics_statement_generic_results_csv}/ethics_statement_frontiers_frontiers_50_spacy.csv (100%)
 create mode 100644 ethics_statement_project/__ethics_statement_generic_results_csv/ethics_statement_frontiers_springer_nature_100.csv
 create mode 100644 ethics_statement_project/ethics_statement_clustering.py
 delete mode 100644 ethics_statement_project/ethics_statement_frontiers_100_labelled_entities.csv
 create mode 100644 ethics_statement_project/ethics_statement_project/ethics_commitee.xml
 create mode 100644 ethics_statement_project/ethics_statement_workflow.PNG
 create mode 100644 ethics_statement_project/project_workflow.md
 create mode 100644 ethics_statement_project/prototype.py
 create mode 100644 ethics_statement_project/requirements.txt
 create mode 100644 ethics_statement_project/testing_pke.py

C:\Users\DELL\dictionary>cd..

C:\Users\DELL>cd pygetpapers

C:\Users\DELL\pygetpapers>git pull
remote: Enumerating objects: 32, done.
remote: Counting objects: 100% (32/32), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 20 (delta 14), reused 18 (delta 12), pack-reused 0
Unpacking objects: 100% (20/20), 39.89 KiB | 28.00 KiB/s, done.
From https://github.com/petermr/pygetpapers
   d72c62c..42505a5  main       -> origin/main
Updating d72c62c..42505a5
Fast-forward
 .idea/.gitignore                               |   3 --
 .idea/getpaper.iml                             |  12 --------
 .idea/inspectionProfiles/profiles_settings.xml |   6 ----
 .idea/misc.xml                                 |   4 ---
 .idea/modules.xml                              |   8 -----
 .idea/vcs.xml                                  |   6 ----
 build/lib/pygetpapers/config.ini               |   2 +-
 build/lib/pygetpapers/pygetpapers.py           |  41 +++++++++++++------------
 dist/pygetpapers-0.0.5.0-py3.7.egg             | Bin 0 -> 39699 bytes
 pygetpapers.egg-info/PKG-INFO                  |   2 +-
 pygetpapers/config.ini                         |   2 +-
 pygetpapers/crossref.py                        |  33 ++++++++++----------
 pygetpapers/europe_pmc.py                      |  18 +++++------
 pygetpapers/pygetpapers.py                     |  41 +++++++++++++------------
 14 files changed, 73 insertions(+), 105 deletions(-)
 delete mode 100644 .idea/.gitignore
 delete mode 100644 .idea/getpaper.iml
 delete mode 100644 .idea/inspectionProfiles/profiles_settings.xml
 delete mode 100644 .idea/misc.xml
 delete mode 100644 .idea/modules.xml
 delete mode 100644 .idea/vcs.xml
 create mode 100644 dist/pygetpapers-0.0.5.0-py3.7.egg

C:\Users\DELL\pygetpapers>

```
