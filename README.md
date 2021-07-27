# ![Icon](figures/rsz_psi_logo.png)<!-- .element height="10%" width="10%" -->  Applications of the Heliospheric Upwind eXtrapolation (HUX) Technique to a variety of heliospheric in situ datasets

Evaluating the Heliospheric Upwind eXtrapolation (HUX) Technique developed by Riley et al. [1, 2] to map solar wind streams radially between different regions in the heliosphere.
This study leverages observations from Helios (A and B) and Earth based spacecrafts (OMNI/ACE/WIND) to test the HUX technique with in situ data. Moreover, in an attempt to enhance the standard HUX method, we propose flux-limiter numerical schemes that accurately capture compression and rarefaction waves.

# References
[1] [Riley, P. and Lionello, Roberto. Mapping solar wind streams from the Sun to 1 AU: A comparison of techniques. Solar Physics, 270(2), 575–592, 2011.](https://www.researchgate.net/publication/226565167_Mapping_Solar_Wind_Streams_from_the_Sun_to_1_AU_A_Comparison_of_Techniques)

[2] [Riley P and Issan O (2021) Using a Heliospheric Upwinding eXtrapolation Technique to Magnetically Connect Different Regions of the Heliosphere. Front. Phys. 9:679497. doi: 10.3389/fphy.2021.679497](https://www.frontiersin.org/articles/10.3389/fphy.2021.679497/full?&utm_source=Email_to_authors_&utm_medium=Email&utm_content=T1_11.5e1_author&utm_campaign=Email_publication&field=&journalName=Frontiers_in_Physics&id=679497)

# Dependencies
1. [Python >= 3.7](https://www.python.org/downloads/)
1. [numpy >= 1.19.1](https://numpy.org/install/)
3. [matplotlib >= 3.3.1](https://matplotlib.org/users/installing.html)
4. [scipy >= 1.5.0](https://www.scipy.org/install.html)
5. [pyhdf >= 0.10.2](https://pypi.org/project/pyhdf/)
6. [psipy >= 0.1.1](https://psipy.readthedocs.io/en/stable/guide/installing.html)
7. [heliopy >= 0.15.3](https://docs.heliopy.org/en/stable/index.html)

# Data 
All data from in-situ spacecraft observations and MHD model results 
can be downloaded using [PsiPy](https://psipy.readthedocs.io/en/stable/auto_examples/sampling/plot_in_situ_comparison.html#sphx-glr-auto-examples-sampling-plot-in-situ-comparison-py) and [HelioPy](https://docs.heliopy.org/en/stable/index.html). 

# Authors
[Predictive Science Inc.](https://www.predsci.com/portal/home.php)

- Pete Riley, pete@predsci.com

- Opal Issan, oissan@predsci.com


**Correspondence**:

Pete Riley, Predictive Science, Inc., San Diego, California, USA. pete@predsci.com

# License
MIT

