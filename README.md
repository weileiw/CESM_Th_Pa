# CESM_Th_Pa
experiment log for CESM thorium protactinium model

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% scavenge equation
% Th230_scavenge = parm_Th230_scavenge * sinking_mass * Th230_loc * yps
%

## $$$$$ 1st run
Run thorium and practinium model after editting Keith's original code.
main changes are on thorium and practinium equations.
The first run is thorium.wlw.run.001

Key parameters used in the first run:

     parm_Th230_desorp_rate0  = 1.0e-6_r8,  & !
     parm_Th232_desorp_rate0  = 1.0e-6_r8,  & !
     parm_Pa231_desorp_rate0  = 1.0e-6_r8,  & !
     parm_Th234_desorp_rate0  = 1.0e-6_r8,  & !
      parm_Th230_scavenge = 10.0_r8,     & !
      parm_Th232_scavenge = 10.0_r8,        & !
      parm_Pa231_scavenge = 1.0_r8,         & !
      parm_Th234_scavenge = 10.0_r8,                 & !
      parm_Th232_solubility = 0.15,                  & !
      parm_Th230_solubility = 0.15,                  & !
      parm_Pa231_solubility = 0.15,                  & !

The model systematically underestimates 231Pa and 230Th. It may be
due to high scavenging rate constants and low desorption rate constant.

## $$$$$ 2nd run
In the 2nd run, scavenge rate constants are decreased from 10 to 2,
desorption rate constants are increased from 1.0e-6 to 5.0e-6.

     parm_Th230_desorp_rate0  = 5.0e-6_r8,  & !
     parm_Th232_desorp_rate0  = 5.0e-6_r8,  & !
     parm_Th234_desorp_rate0  = 5.0e-6_r8,  & !
     parm_Pa231_desorp_rate0  = 5.0e-6_r8,  & !
     parm_Th230_scavenge = 2.0_r8,          & !
     parm_Th232_scavenge = 2.0_r8,                 & !
     parm_Th234_scavenge = 2.0_r8,                 & !
     parm_Pa231_scavenge = 1.0_r8,                 & !
     parm_Th232_solubility = 0.15,                 & !
     parm_Th230_solubility = 0.15,                 & !
     parm_Pa231_solubility = 0.15,                 & !

Model versus observation thorium-230 is greatly improved.
However, the Pa-231 is still underestimated.

## $$$$$ 3rd run
In the 3rd run, scavenge rate constant for Pa231 is decreased from 1.0
to 0.5, and desorption rate constant for Pa231 is increased from 5.0e-6
to 7.5e-6.

     parm_Th230_desorp_rate0  = 5.0e-6_r8,  & !
     parm_Th232_desorp_rate0  = 5.0e-6_r8,  & !
     parm_Th234_desorp_rate0  = 5.0e-6_r8,  & !
     parm_Pa231_desorp_rate0  = 7.5e-6_r8,  & !
     parm_Th230_scavenge = 2.0_r8,          & !
     parm_Th232_scavenge = 2.0_r8,                 & !
     parm_Th234_scavenge = 2.0_r8,                 & !
     parm_Pa231_scavenge = 0.5_r8,                 & !
     parm_Th232_solubility = 0.15,                 & !
     parm_Th230_solubility = 0.15,                 & !
     parm_Pa231_solubility = 0.15,                 & !

Model versus observations for both thorium-230 and Pa-231 are improved.
However, both Pa231 and Th230 were underestimated in the surface,
and overestimated in the bottom.

## $$$$$ 4th run
In the 4th run, scavenge rate constant is decreased from 0.5 to 0.1 for
Pa231, and from 2.0 to 1.0 for Th230. Desorption rate constant is increased
from 7.5e-6 to 10.0e-6 for Pa231, from 5.0e-6 to 7.5. Solubility rate constant
is increased from 0.15 to 0.25 for both Pa231 and Th230.

     parm_Th230_desorp_rate0  = 7.5e-6_r8,  & !
     parm_Th232_desorp_rate0  = 7.5e-6_r8,  & !
     parm_Th234_desorp_rate0  = 7.5e-6_r8,  & !
     parm_Pa231_desorp_rate0  = 10.0e-6_r8,  & !
     parm_Th230_scavenge = 1.0_r8,         & !
     parm_Th232_scavenge = 1.0_r8,                 & !
     parm_Th234_scavenge = 1.0_r8,                 & !
     parm_Pa231_scavenge = 0.1_r8,                 & !
     parm_Th232_solubility = 0.25,                 & !
     parm_Th230_solubility = 0.25,                 & !
     parm_Pa231_solubility = 0.25,                 & !


Model versus observation thorium-230 and Pa-231 are improved  (R2>0.6
for both). However, both Pa231 and Th230 are still underestimated in
the surface, and overestimated in the bottom.

comparing previous experiments, it can be concluded that scavenging factors control
surface Th230 and Pa231 activities, and desorption control deep ocean (>3000m) activities.
The solubility factor could potentially increase overall water column activities. But
it is unclear how strong this feedback is, In the fifth run, desorption and scavenging
factors are kept unchanged from 4run, dust source for both Th230 and Pa231 are
completely shutoff according to Gu and Liu 2017.

## $$$$$ 5th run.

     parm_Th230_desorp_rate0  = 7.5e-6_r8,  & !
     parm_Th232_desorp_rate0  = 7.5e-6_r8,  & !
     parm_Th234_desorp_rate0  = 7.5e-6_r8,  & !
     parm_Pa231_desorp_rate0  = 10.0e-6_r8,  & !
     parm_Th230_scavenge = 1.0_r8,         & !
     parm_Th232_scavenge = 1.0_r8,                 & !
     parm_Th234_scavenge = 1.0_r8,                 & !
     parm_Pa231_scavenge = 0.1_r8,                 & !
     parm_Th232_solubility = 0.25,                 & !
     parm_Th230_solubility = 0.00,                 & !
     parm_Pa231_solubility = 0.00,                 & !

Comparison of run003 and run004 shows that run005 underestimates both Th230 and Pa231,
and run004 overestimates both Th230 and Pa231, especially Pa231. Therefore, in the sixth
run, desorption and scavenging rate constants are interpolated based on run003 and run004.

## $$$$$ 6th run.

     parm_Th230_desorp_rate0  = 6.0e-6_r8,  & !
     parm_Th232_desorp_rate0  = 6.0e-6_r8,  & !
     parm_Th234_desorp_rate0  = 6.0e-6_r8,  & !
     parm_Pa231_desorp_rate0  = 8.5e-6_r8,  & !
     parm_Th230_scavenge = 1.5_r8,          & !
     parm_Th232_scavenge = 1.5_r8,                 & !
     parm_Th234_scavenge = 1.5_r8,                 & !
     parm_Pa231_scavenge = 0.25_r8,                & !
     parm_Th232_solubility = 0.25,                 & !
     parm_Th230_solubility = 0.25,                 & !
     parm_Pa231_solubility = 0.25,                 & !

Surface Th230 is well constrained by the model, deep ocean is overestimated.
Pa231 is generally overestimated by the model, but overall pattern is better, compared to
run 004. Comparison between Run003 and run006 shows adsorption and desorption parameters
are between the two runs. In the seventh run, Th parameters are keep unchanged from Run006,
Pa parameters are adjusted based on Run006 and Run003.

## $$$$$ 7th run.

     parm_Th230_desorp_rate0  = 6.0e-6_r8,  & !
     parm_Th232_desorp_rate0  = 6.0e-6_r8,  & !
     parm_Th234_desorp_rate0  = 6.0e-6_r8,  & !
     parm_Pa231_desorp_rate0  = 8.0e-6_r8,  & !
     parm_Th230_scavenge = 1.5_r8,              & !
     parm_Th232_scavenge = 1.5_r8,              & !
     parm_Th234_scavenge = 1.5_r8,              & !
     parm_Pa231_scavenge = 0.4_r8,              & !
     parm_Th232_solubility = 0.25,                 & !
     parm_Th230_solubility = 0.25,                 & !
     parm_Pa231_solubility = 0.25,                 & !




