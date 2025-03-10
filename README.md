
# Hot summers over Europe simulated by a rare event algorithm

We reproduce the work by Ragone et al. 2018 using the fully coupled version of CESM2.

Ragone, F., Wouters, J., & Bouchet, F. (2018). Computation of extreme heat waves in climate models using a large deviation algorithm. Proceedings of the National Academy of Sciences of the United States of America, 115(1), Article 1. https://doi.org/10.1073/pnas.1712645115

## Experiments

### Current climate -> "ssp370-2025"
Initial conditions from the years 2024-2026 from a 42 member ensemble folowing the SSP370 scenario.

### Pre-industrial -> "piControl"
Initial conditions from a piControl simulation taking every third year until we have 126 years (same number as for the ssp370-2025 ensemble).

## Available output

|                | x1   | x2   | x3   | x4   | x5   |
|:---------------|:-----|:-----|:-----|:-----|:-----|
| EFLX_GNET      |      |      | x    | x    | x    |
| EFLX_LH_TOT    |      |      | x    | x    | x    |
| FAREA_BURNED   |      |      | x    | x    | x    |
| FIRE           | x    | x    |      |      |      |
| FLDS           |      | x    | x    | x    | x    |
| FLNS           |      | x    | x    | x    | x    |
| FSDS           |      | x    | x    | x    | x    |
| FSH            |      |      | x    | x    | x    |
| FSNO           |      |      | x    | x    | x    |
| FSNS           |      | x    | x    | x    | x    |
| GPP            | x    | x    | x    | x    | x    |
| HR             | x    | x    |      |      |      |
| ICEFRAC        | x    | x    | x    | x    | x    |
| LHFLX          |      | x    | x    | x    | x    |
| NBP            | x    | x    | x    | x    | x    |
| PBOT           |      |      | x    | x    | x    |
| PRECC          | x    | x    | x    | x    | x    |
| PRECL          | x    | x    | x    | x    | x    |
| PS             | x    | x    | x    | x    | x    |
| PSL            | x    | x    | x    | x    | x    |
| QFLX_EVAP_TOT  |      |      | x    | x    | x    |
| QREFHT         | x    | x    | x    | x    | x    |
| QRUNOFF        |      |      | x    | x    | x    |
| QVEGT          |      |      | x    | x    | x    |
| RH2M           |      |      | x    | x    | x    |
| RH2M_U         |      |      | x    | x    | x    |
| RHREFHT        | x    | x    | x    | x    | x    |
| SHFLX          |      | x    | x    | x    | x    |
| SOILWATER_10CM |      |      | x    | x    | x    |
| SST            | x    | x    | x    | x    | x    |
| TLAI           | x    | x    | x    | x    | x    |
| TOTFIRE        | x    | x    |      |      |      |
| TOTLITC        | x    | x    |      |      |      |
| TOTSOILLIQ     |      |      | x    | x    | x    |
| TOTVEGC        | x    | x    |      |      |      |
| TREFHT         | x    | x    | x    | x    | x    |
| TREFHTMN       | x    | x    | x    | x    | x    |
| TREFHTMX       | x    | x    | x    | x    | x    |
| TSOI_10CM      |      |      | x    | x    | x    |
| TWS            | x    | x    |      |      |      |
| U10            |      |      | x    | x    | x    |
| U200           |      | x    | x    | x    | x    |
| U500           |      | x    | x    | x    | x    |
| V200           |      | x    | x    | x    | x    |
| V500           |      | x    | x    | x    | x    |
| Z200           |      | x    | x    | x    | x    |
| Z500           | x    | x    | x    | x    | x    |
