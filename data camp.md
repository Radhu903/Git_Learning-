```
1. The Bioconductor Project
Hi! I'm Paula Martinez, and I'll be your instructor. I am a data scientist and I train people on how to analyze their data more efficiently. Also, I am a bioinformatician, interested in genomic variation that leads to diversity. For these kinds of analyses, I love using R and Bioconductor, particularly because of the possibilities to work with different datasets and to collaborate within the community. During this introduction, you will discover the most commonly used Bioconductor packages. We will start with installation and at the end of this chapter, you will be able to retrieve whole genome sequences, using Bioconductor.

2. Bioconductor
The Bioconductor project is an open source repository for R packages, datasets and workflows that are specific for analyzing biological data. The Bioconductor project is a useful extension on CRAN, the R Archive, because it provides us with the software tools to explore, understand, and solve simple and complex molecular biology questions. Hence, Bioconductor's tagline is "open source software for bioinformatics".

1 Bioconductor (www.bioconductor.org)
3. What do we measure and why?
Molecular biology questions are usually about either the structure or the function of each of the building blocks of an organism, and very often how they interconnect to one another. In this course, you will learn commonly used packages that will help you understand the structure of biological data. That is, you will find out more about the elements, their regions, their size and order, and how they relate to other data. Other Bioconductor courses on DataCamp will teach you more about the functions of the building blocks, such as gene expression and regulation, and how these affect phenotypes such as health/disease, evolution, and much more.

4. How to install Bioconductor packages?
The Bioconductor package collection forms its own repository and has a release schedule different from the R Archive. Because Bioconductor has it's own base functions and updates, packages are installed differently. To install Bioconductor packages you need two lines of code, as shown on the slide. First, use the function source on the script, BiocLite-dot-R, from Bioconductor-dot-org This script will install the BiocInstaller package. Then, use the function biocLite() with the name of the package you want to install. Once you source the BiocLite, you will be informed if any new versions of Bioconductor are available, and will also see a prompt to update your R version if needed. Updating packages, regularly, is important to get the new features. In case there are upgrades on packages or dependencies, you will be asked to update all, some, or none of the packages.

5. Bioconductor version and package version
Because Bioconductor is in constant development, you can check the version of Bioconductor using the syntax BiocInstaller::bioVersion() or if you already loaded the BiocInstaller package you can call the function biocVersion() directly. To load a package use the function library like with CRAN packages. It's important for reproducibility to always check the versions of your packages. You can use the function sessionInfo() which gives you a list of all the loaded packages and their versions, or you can inquire the version of each package using packageVersion() and the packageName. Finally, if you are interested to know if you have out-of-date packages, use the function biocValid().

6. Let's practice!
Now it's your turn to use Bioconductor.

```
