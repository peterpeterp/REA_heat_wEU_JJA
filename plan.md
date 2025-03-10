
# Current climate and pre-industrial hot summer ensembles 

## Aim:

* Generate two ensembles of extremely hot JJA periods...
    * ... one for current climate (2021-2031)
    * ... and one for pre-industrial climate (piControl)

## Technical implementation:

* importance sampling -> maximizing JJA average tas over Europe
* following previous work by Ragone & Bouchet et al.

## Potential usages

1) Analyze pre-condistionning conditions for hot summers (soil-moisture, SST patterns)
2) Analyze evolution of atmospheric circulation throughout the season 
3) Assess likelihoods of simultaneous heat waves at different locations (@Kai)
4) Benchmarking dataset for ML approaches trained on data with sparse representation of extreme summers (@Yinglin)
5) Compare between current and pre-industrial climate
    * events with similar return periods
    * results from (1-4)

## Novelty (?)

* Application with a different ESM
* Current climate and pre-industrial ensemble ()

## Technical questions

* Perturbation:
    * Which variable? (we used rel. humidity so far)
    * How strong is the perturbation? (we used a random field of 10^-3 <- very small)
* Strength of the 

* Initial conditions:
    * How problematic would it be to 


| knob      | Ragone et al. 2018    | Ragone & Bouchet 2021 | Boosting with CESM2 |
| --------- | --------------------- | ----- | ---- |
| perturbation variable           | surface pressure     | potential temperature (all levels) | relative humidity |
| relative perturbation magnitude | $7.5\cdot 10^{-5}$   | $10^{-4}$             | $10^{-13}$         |
| $\tau$                          | 8d                   | 5d                    |                  | 
| bias parameter $k$              | 10,20,40 K           | 30 K                  |
| number of trajectories $N$      | 512                  | 100                   |  |



$ w_n(i) = \frac{e^k \int_{t_{i-1}}^{t_i}A({X_n(t)})}{\frac{1}{N} \sum_{m=1}^{N} e^k \int_{t_{i-1}}^{t_i}A({X_m(t)})} $

$ r(a) = - \frac{1}{log(1 - \sum_{n=1}^N p_n s_n(a))} $

$ p_n = \frac{1}{N} \prod_{i=1}^{18} \frac{1}{w_n(i)} $

$ p0_n = \frac{1}{N} $  ?? 

Plot pdf and cdf of trajectories