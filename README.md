# ADHD Classification with Reliable RELIEF

This repo contains the RRelief implementation that I researched and implemented during the time of my internship at Indian Statistical Institute, Kolkata. 

<p  align="center"><img width = "900" height=350" src = "https://raw.githubusercontent.com/Bhard27/ADHD-Classification-with-Reliable-RELIEF/main/assets/paper.png?token=AMFAV34ZV4XNFXJ67D4B2Y3BNHJPW"></p>

## My work

Implemented the research paper, 'Classification of ADHD Individuals and Neurotypicals Using Reliable RELIEF' where I wrote the code for an improved Reliable RELIEF algorithm from scratch. Also, I implemented several classifiers for ADHD classification models. Final goal of this project is to classify ADHD where the feature extraction process uses the Reliable RELIEF algorithm. 

<p  align="center"><img width = "650" height=300" src = "https://raw.githubusercontent.com/Bhard27/ADHD-Classification-with-Reliable-RELIEF/main/assets/ADHD-thumbnail.png?token=AMFAV36ACLI5QUP55LWJUN3BNHK2S"></p>

    
### Relief algorithm    

The core idea behind Relief algorithms is to estimate the quality of attributes on the basis of how well the attribute can distinguish between instances that are near to each other.


There are three Algorithms in the Relief Family:
- Basic Relief algorithm: It is limited to classification problems with two classes.
- ReliefF : Extension of Relief . Which can deal with multiclass problems.
- RReliefF : Then ReliefF was adapted for continuous class (regression) problems resulting in RReliefF algorithm.


<p  align="center"><img width = "550" height=300" src = "https://raw.githubusercontent.com/Bhard27/ADHD-Classification-with-Reliable-RELIEF/main/assets/relief-algo.png?token=AMFAV3ZK4CVVDL24NBWRD2DBNHG6E"></p>

- The results on other datasets show that this algorithm can perform better than other feature extraction methods. The implemented algorithm will be eventually deployed as a web application to detect ADHD individuals with higher accuracy in comparison to automatic state-of-the-art classsifiers.

<p  align="center"><img width = "750" height=400" src = "https://raw.githubusercontent.com/Bhard27/ADHD-Classification-with-Reliable-RELIEF/main/assets/fMRI-output.jpg?token=AMFAV33JXHZFOOCO5PXRB2DBNHKTQ"></p>

<pre>

├── LICENSE
├── Notebooks
│   ├── ADHD\ Classification.ipynb
│   ├── ADHD-classification.ipynb
│   └── ADHD.ipynb
├── README.md
└── src
    ├── Amprion.csv
    ├── R-Relieff.py
    ├── computePCA.py
    ├── relief.py
    └── rrelief.py
</pre>
