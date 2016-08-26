Please test on jasmin-sci1/2 so that you don't have to install dependencies.

Example usage:

 What's in a file?

$ python2.7 whats_in_na_1001.py na_files/js970523.nx7

Time GMT hhmmss                85149.0              154040.0
NOx ppbv                       -4.8                 216.7
NO ppbv                        -6.5                 99.9
NO2 (NOx-NO) ppbv              -5.2                 133.3
ERROR FLAG NOx/NO/NO2(NOx)     0.0                  2.0
NO2(Scintrex) ppbv             -0.27                99.99
ERROR FLAG NO2(LMA3)           1.0                  2.0

$ python2.7 plot_na_1001.py na_files/js970523.nx7 'Time GMT hhmmss' 'NOx ppbv' 100000,130000 0,500

...writes a plot.

