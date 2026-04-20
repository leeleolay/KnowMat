DOI: 10.1016/j.actamat.2025.121785

# Additively-manufactured Al-0.3Zr-0.2Ce-0.2Cu alloy with high creep resistance and electrical conductivity☆

Jovid Rakhmonov $ ^{a,\dagger} $, Jonathan Poplawsky $ ^{b} $, Lawrence Allard $ ^{a} $, James Burns $ ^{b} $, Jie Qi $ ^{d} $, Ismael Coello $ ^{d} $, David C. Dunand $ ^{d} $, Sumit Bahl $ ^{a} $, Alice Perrin $ ^{a} $, J. Allen Haynes $ ^{a} $, Alex Plotkowski $ ^{c} $, Amit Shyam $ ^{a} $

 $ ^{a} $ Materials Science and Technology Division, Oak Ridge National Laboratory, Oak Ridge, TN 37830, USA

 $ ^{b} $ Center for Nanophase Materials Sciences, Oak Ridge National Laboratory, USA

 $ ^{c} $ Computational Sciences & Engineering Division, Oak Ridge National Laboratory, USA

 $ ^{d} $ Department of Materials Science & Engineering, Northwestern University, Evanston, IL 60208, USA

## ARTICLE INFO

## Keywords

Al alloys

Additive manufacturing

Microstructure

Conductivity

Creep

Strength

## Abstract

A new, solute-lean Al-0.3Zr-0.2Ce-0.2Cu (wt.%) alloy is developed for additive manufacturing that overcomes the classical tradeoff between conductivity and creep resistance. The rapid-cooling-enabled supersaturation of Zr, and its uniform distribution in  $ \alpha $-Al matrix, along with formation of submicron (Ce,Cu)-rich intermetallic particles on solidification lead to unusually high creep resistance at 200 ^\circC. Near-zero secondary creep rates are achieved up to the alloy yield stress (YS) of 65 MPa at 200 ^\circC in as-fabricated state. The Zr-solute-induced dislocation-climb suppression mechanism underlying this improvement also restricts dynamic recovery above YS, as noted from appreciable primary creep and its transitioning to near-zero secondary creep rates. A combination of relatively coarse, epitaxially-grown  $ \alpha $-Al grains, low Zr concentration in  $ \alpha $-Al, and the impurity-scavenging effect of Ce to purify  $ \alpha $-Al matrix produces high electrical conductivity of  $ \sim $48 %IACS. Aging precipitation of L12-Al3Zr nanoprecipitates doubles the YS (to  $ \sim $150 MPa) at room temperature and increases alloy conductivity to  $ \sim $58 %IACS, but loss of solid-solution Zr out of  $ \alpha $-Al matrix leads to activation of dislocation climb, degrading the creep properties as compared to the supersaturated Al-Zr solid solution in the as-fabricated state. Compared to L12-Al3Zr nanoprecipitates, submicron (Ce,Cu)-rich particles formed on solidification are more effective at impeding dislocation climb, producing a threshold stress for dislocation creep of  $ \sim $ 50 MPa at 200 ^\circC. The new alloy design concepts, especially solute-induced dislocation-climb suppression for creep resistance, explored here may pave way for the design of new metallic alloys for thermal/electrical conductors and other high-temperature applications.

## 1. Introduction

Batteries for electric vehicles (EVs) have increased the demand for alloys with an optimal combination of electrical conductivity (EC) and mechanical properties [1,2]. Rotors, inverters, stators, and busbars are among the EV applications requiring an improved combination of mechanical properties (strength, creep resistance, etc.) and EC for enhanced power output and efficiency of electric motors [1,3,4]. Moreover, given the near-linear relationship between electrical and thermal conductivities for metallic systems, such as Al alloys, new high-performance alloys with improved thermal conductivity may replace heavier metallic alloys for heat exchangers/sinks, etc. [4]. The high specific strength of Al alloys offers advantages over Cu alloys for improved driving range through lightweighting. The maximum EC

achievable in pure Al is  $ \sim $65 % of that of coarse-grained pure Cu that has a resistivity of 58.1 MS/m at 20 ^\circC (defined as 100 % International Annealed Copper Standard (IASC) [4]). The density of Al is however only 30 % that of Cu. Achieving a combination of EC of 48 % IACS and a yield strength (YS) of 90–140 MPa is the current threshold for EV applications [3]. The widely used Al-Si based A356 alloy has an EC of 40 % IACS, with its YS reaching as high as 225 MPa [2]. All strengthening mechanisms, particularly solid-solution and precipitation hardening, affect the scattering of conducting electrons, producing an inverse relationship between strength and EC [5]. While some strengthening mechanisms, such as dislocation hardening, improve strength drastically with minimal conductivity loss – the approach well adopted for wrought Al conductor alloys – solutes in solid-solution reduce conductivity significantly with a marginal strength gain. The precipitation hardening is the most effective strengthening mechanism in cast/wrought Al alloys, but solutes retained in solid-solution alongside the precipitates substantially deteriorate alloy conductivity [2]. Overcoming this tradeoff to maximize mechanical properties while minimizing the conductivity reduction requires new alloy design approaches.

Research efforts aimed at designing new Al-based conductor alloys have increased steadily in recent years. Cast Al-2.7Ce-1.1Si-0.6Mg (wt. %) demonstrated a YS of 110 MPa and EC of 49 %IACS when heat treated to T5 or T6 temper [1]. Another study [2] showed higher values of YS and EC (~180 MPa and ~50 % IACS in T5, and ~250 MPa and ~50 % IACS in T6 state) for cast Al-3Ni-0.55Si-0.55Mg (wt. %). Both these alloys derive their strength from metastable precipitates that are precursors to Mg₂Si precipitates [1,2]. However, these precipitates coarsen rapidly at temperatures above 150 ^\circC [6], making them unsuitable even for intermediate-temperature creep-relevant environments. Resistive heating in electrical applications increases the temperature which, when combined with mechanical loading, leads to creep conditions [4]. Fine, equiaxed L1₂-Al₃X (X=Sc, Zr, etc.) nanoprecipitates, due to their high thermal stability, are popular candidates for improved thermal stability and creep resistance in Al alloys [7]. Extensive efforts have been made towards improving the creep resistance by increasing the threshold stress for dislocation climb – the mechanism that activates during creep of such alloys [8–11]. Many studies have considered dislocation creep in the temperature range of 300–400 ^\circC, but studies at lower temperatures (~200 ^\circC) relevant to Al conductors are scarce. Recent studies have shown the beneficial effect of high-aspect-ratio precipitates to suppress dislocation climb [12–16] or introducing slow-diffusing solutes to impede dislocation climb [17,18].

Additive manufacturing (AM) processes offer design freedom by enabling more complex geometries; it also presents unique solidification and cooling conditions that create opportunities for new alloy design strategies. High solidification rates in AM can cause solute trapping which increases super-saturation beyond that of conventional processes. Supersaturation of slow diffusing solutes may be used to impede dislocation climb. For example, in a cast Al-0.054Fe (wt. %) alloy,  $ \sim $0.04 wt.% Fe in solid solution achieved millionfold lower creep rates at 200 ^\circC compared to when the Fe concentration in the  $ \alpha $-Al matrix is only  $ \sim $0.01 wt.% [18]. Small additions of other slow-diffusing solutes (e.g., Mn, Fe, Ti) also strongly reduce creep rates compared to pure Al [19]. A recent study [17] underscored the high efficiency of Mn in slowing the rate of dislocation climb in cast Al-Mn-Zr alloy. However, Mn has a strong negative effect on electrical conductivity, almost twice that produced by Zr for a given concentration in the alloy [20]. AM processing enables extended Zr solute trapping in the  $ \alpha $-Al matrix along with uniform solute distribution [21], which is difficult to achieve by casting processes. This microstructure control strategy paves new pathways to retarding dislocation climb in solute-lean Al conductor alloys. Therefore, the feasibility of using Zr or other solute with slow diffusivity yet limited effect on conductivity to improve alloy creep resistance may be an effective design strategy.

Another advantage offered by rapid cooling in AM is refinement of intermetallic particles forming on solidification. Eutectic compositions with coarsening-resistant intermetallic particles have shown superior creep resistance to cast Al alloys in the 300–400 ^\circC range [16,22]. However, high fraction of such intermetallic particles alongside more solutes residing in \alpha-Al lattice can lead to significant EC deterioration. An attempt is made to balance this tradeoff in a recently introduced AM Al-1Fe-1Zr (wt. %) alloy to obtain a good combination of strength and thermal conductivity [23]. While this alloy achieves a YS of ~ 350 MPa, its EC is quite moderate, ~45 %IACS [23]. Among various slow-diffusing transition metals, cerium has a high potential to improving alloy strength and creep resistance by forming strengthening intermetallic precipitates on solidification [22]. Also, Ce is expected to contribute to improved EC by scavenging some common impurities such as Si [24] and Cu [25].

This study introduces a new, dilute Al-0.3Zr-0.2Ce-0.2Cu (wt. %) alloy, showing after rapid solidification via additive manufacturing (AM) an attractive combination of electrical conductivity and mechanical properties, especially creep resistance at intermediate temperatures. The alloy displays two types of precipitates: (i) aging-induced L1₂-Al₃Zr nanoprecipitates which are effective at strengthening at room temperature, and (ii) (Ce,Cu)-rich submicron particles formed on solidification, which are effective at retarding dislocation creep at 200 ^\circC. We also demonstrate for the first time that supersaturated Zr in the \alpha-Al matrix, without forming L1₂-Al₃Zr by aging, leads to a complete suppression of dislocation climb. This new strategy offers a new alloy design concept for breaking the tradeoff between conductivity and strength /creep resistance at intermediate temperatures (T/Tₘ ~ 0.5 for 473 K).

## 2. Experimental procedures

## 2.1. Alloy fabrication

The alloy studied here is labeled as Al-Zr-Ce-Cu alloy, which was additively manufactured (AM) using the laser powder-bed fusion (LPBF, EOS M290) process at Beehive Industries (Knoxville, TN). Table 1 lists the composition of a representative AM specimen, including impurities (Si and Fe), measured using inductively coupled plasma optical emission spectroscopy (ICP-OES). The ingots used for gas-atomization were cast at Loukus Technologies (Calumet, MI). The powder feedstock for the LPBF process was gas-atomized at Connecticut Engineering Associates Corporation (Sandy Hook, CT) under nitrogen atmosphere and sieved into 20–63  $ \mu $m size range. The mechanical coupons (115 mm long and 15 mm in diameter) were fabricated with their length aligned along the build direction (BD) under an Ar atmosphere using a laser power of 370 W, scanning speed of 1300 mm/s, hatch spacing of 0.21 mm, layer thickness of 30  $ \mu $m, and a beam size of 83  $ \mu $m. Stripe scanning strategy with a width of 10 mm and stripe-to-stripe overlap of 0.02 mm was used. Scan rotation angle of 67^\circ was used between layers. The substrate temperature was 150 ^\circC during printing to minimize residual stress. This parameter set resulted in relative density > 99.5 % and was selected out of initially investigated different parameter sets studied for process optimization.

Isothermal and isochronal aging studies were conducted to determine the peak-aging condition by measuring alloy hardness and conductivity. Isochronal aging was performed in the temperature range of 150–550 ^\circC, with a step size of 25 ^\circC and a dwell time of 3 h at each temperature. Isothermal aging was conducted at 375 ^\circC at various times up to 100 h. A separate disk with 6.35 mm thickness and 15 mm diameter was used for each individual aging temperature and time combination. Heat treatments were performed in a muffle furnace in air and specimens were air-cooled.

## Table 1

Composition of AM Al-0.3Zr-0.2Ce-0.2Cu alloy measured by ICP-OES (in wt. %).

|  | Zr | Ce | Cu | Si | Fe | Sn | Al |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Concentration (wt. %) | 0.34 | 0.19 | 0.19 | 0.09 | 0.05 | 0.07 | bal. |

## 2.2. Mechanical testing

Tensile tests were performed at 20 and 200 ^\circC on as-fabricated and peak-aged specimens machined with 6.3 mm diameter and 31.75 mm length gauge section with the sample axis aligned with the BD. Tests were carried out with fixed strain rates between 10⁻¹ and 10⁻⁵ s⁻¹. Strain was measured with an axial extensometer mounted on grooves in the grip section and connected to two linear variable differential transformers (LVDTs). Specimen temperature was controlled/monitored using three K-type thermocouples attached to the middle and near the two ends of gauge section. The temperature variation within the gauge length was below 5 ^\circC during all tensile tests. At least two replicates per alloy condition were tested at regular strain rates (i.e., 2 \times 10⁻⁴ s⁻¹ at 20 ^\circC and 10⁻⁴ s⁻¹ at 200 ^\circC). Tests at all other strain rates were performed with one replicate per alloy and test condition.

Creep tests were carried out on the as-fabricated and peak-aged specimens at 200 ^\circC in tension and compression to evaluate the creep response of the alloy. While tensile creep provides details related to all three creep stages, i.e., primary, secondary, and tertiary stages, compressive creep allows for the measurements of primary and secondary creep responses over a wide range of stresses.

For compressive creep tests, the specimens with 10 mm diameter and 22 mm length were machined with their central axis aligned along the BD. Except for one specimen, all other compressive creep tests were conducted under stress-jump mode to obtain multiple data points corresponding to different stresses from a single specimen. The stress level was then increased when the near-minimum creep strain rate was established for a given stress. Tests were interrupted upon reaching a total strain of  $ \sim $10 % to avoid specimen bulging. One compressive creep test was run under a single-load creep mode and interrupted upon reaching a certain strain in the specimen to investigate its dislocation structure. Strain was obtained from the displacement data collected using LVDT, possessing an accuracy of 10  $ \mu $m, mounted on the cold end of the compression fixture. The temperature of the specimen was controlled/monitored using a K-type thermocouple attached to the specimen.

Tensile creep tests were performed using the same specimen geometry as for the regular tensile tests. Tensile creep strain measurements were made using the same method as for the regular tensile tests. Creep experiments were carried out under single-load creep mode at a few selected stresses. While creep continued until rupture for aged specimens, creep experiments were interrupted for as-fabricated specimens due to the absence of any measurable creep strain following some initial primary creep. Specimen temperature was measured with the two K-type thermocouples mounted at one-third and two-third distances within the gauge section. The temperature variation within the gauge length was below 3 ^\circC during all tensile creep tests.

The Vickers microhardness tests were performed with a load of 200 g or 5 kg and a dwell time of 20 s on specimens subjected to isochronal and isothermal aging. The same specimen was used for both conductivity and microhardness measurements, with conductivity measured first, followed by the microhardness measurements. Measurements were made on the surfaces perpendicular to the BD and polished down to a surface finish of  $ \sim $0.15  $ \mu $m. A minimum of 12 indentations were made on each specimen to obtain the average hardness.

## 2.3. Electrical conductivity

Electrical conductivity (EC) of plate specimens (15 mm diameter and  $ \sim $6.35 mm thickness) subjected to isothermal and isochronal aging was measured at room temperature with 60 kHz frequency using a Sigma-scope SMP10 unit based on the eddy current method. The reported EC value is the average of 10 individual measurements on a single specimen.

## 2.4. Microstructure characterization

Microstructural analyses were made using a scanning electron microscope (SEM, TESCAN MIRA3) equipped with electron backscatter diffraction (EBSD) and a scanning transmission electron microscope (S/TEM, JEOL 2200FS and JEOL 2100F) equipped with energy dispersive spectroscopy (EDS). The specimen preparation for SEM/EBSD imaging involved mounting in conductive graphite and grinding followed by polishing to achieve the surface finish of 0.05 \mum. The final polishing step was performed using colloidal silica in a vibratory polishing machine. EBSD scans were made at 20 kV and a step size of 0.4 \mum. Subsequent EBSD data post-processing was performed using the OIM Analysis software. STEM foils were obtained by Twin-Jet electro-polishing of ~100-\mum-thick disks with 3 mm diameter at 20 kV in a nitric acid (25 %) plus methanol (75 %) solution maintained at −25 (\pm5) ^\circC. Measurement of precipitate characteristics on representative micrographs was carried out using ImageJ software. Atomic-scale compositional analyses were performed using atom probe tomography (APT, LEAP4000X HR, Cameca Instruments) at a specimen temperature of 50 K, 20 % pulse fraction, 0.2 % detection rate, and 200 kHz pulse rate. Post-processing of APT data was performed using IVAS v.3.8 software (Cameca Instruments). Tips for APT study were acquired using a focused ion beam (FIB, FEI Nova 200)-SEM by following a standard lift-out procedure [26]. A lamella with ~10 \mum thickness was first cut from the region of interest. Each lamella was then milled to produce four needles each with a diameter of ~170 nm and a tip radius <20 nm. The \alpha-Al matrix composition was quantified using the plateau region of manually background-corrected proximity histograms. The size of L1₂-Al₃Zr precipitates was calculated using the maximum separation method. First, the volume of each L1₂-Al₃Zr precipitate was calculated by multiplying the total number of Zr atoms in a cluster to the unit cell volume. The detection efficiency of 33 % of LEAP system was considered to determine the total number of atoms. Then, the L1₂-Al₃Zr precipitate radius was derived from its volume using the relationship for sphere. Calculations were made only on the L1₂-Al₃Zr precipitates fully enclosed within the APT tip.

X-ray diffraction (XRD) measurements were performed using a Bruker AXS 2nd gen. D2 Phaser. To maximize detection of minor phase peaks, measurements were carried out over a diffraction angle range of 18–55^\circ with a 2\theta step size of  $ \sim $0.002^\circ and exposure time of 2.25s/step. The CuK\alpha x-ray beam was generated at 30 kV/10 mA with a wavelength of  $ \lambda=1.5418 $ Å. Patterns were analyzed using Highscore Plus software.

## 3. Results

## 3.1. As-fabricated microstructure

Fig. 1 summarizes the typical as-fabricated microstructures of the AM Al-Zr-Ce-Cu alloy. Low-magnification optical micrograph (Fig. S_{1}) demonstrates the limited presence of pores in this alloy. No cracks were observed (Fig. S_{1}), demonstrating the LPBF processability of this alloy. Fig. 1a shows the typical grain structure of the alloy, which consists of elongated <001>Al and <101>Al grains aligned along the BD. These grains span multiple melt pool widths and no fine grains, often observed in Zr-containing Al alloys [14,16], were noted. A higher-magnification EBSD map in Fig. 1b and the corresponding grain-boundary distribution map in Fig. 1c show that the boundaries within the grains have a misorientation angle of  $ \sim2-8^{\circ} $

The SEM micrograph in Fig. 1d shows fine, submicron-sized precipitates distributed uniformly in the microstructure, yet a thin region ( $ \sim $1  $ \mu $m) just above melt pool boundaries is devoid of such precipitates (Fig. 1d). When viewed at higher magnification under STEM, each precipitate appears as a composite comprising several phases (Fig. 1e). The EDS maps corresponding to Fig. 1e indicate the presence of three different phases: (1) a Sn-rich phase, (2) a Ce-rich darker phase containing Ce, Cu, and Si, and (3) a phase residing between Sn-rich and Ce-rich.
Fig. 1. A summary of the as-fabricated microstructure of Al-Zr-Ce-Cu alloy: (a, b) EBSD inverse pole figure (IPF) -colored maps, aligned along build direction (BD), showing the typical grain morphology and orientation, (c) the misorientation angle distribution map, corresponding to (b), showing the distribution of low- and high-angle grain boundaries, (d) backscattered electron SEM micrograph showing the typical microstructure, with dotted line pointing to melt pool boundary, and (e) high-angle annular dark-field (HAADF) STEM micrograph showing agglomerated intermetallic particles, with the corresponding EDS maps showing the distribution of Sn, Ce, Fe, Si, and Cu. Dotted line in (d) indicates melt-pool boundaries.

rich precipitate that contains Fe and Ce. A lower-magnification STEM micrograph indicates that such agglomeration tendency was prevalent throughout (Fig. S_{2}). These microstructural observations are consistent with (i) XRD results revealing  $ \alpha $-Al,  $ Al_{8}Cu_{4}Ce $,  $ Al_{11}Ce_{3} $, and Sn precipitates (Fig. 2a), and (ii) Scheil solidification simulation (Fig. 2b), which also predicts the formation of binary and ternary Al-Ce(-Cu) phases in the alloy. The Scheil solidification curve predicting  $ Al_{8}(Ce, Cu)_{4} $ as opposed to the experimentally observed  $ Al_{8}Cu_{4}Ce $, may point to the preferential formation of the metastable phase over the equilibrium one during rapid solidification. Overall, these results indicate that Ce reacts with Cu, Si, and Fe impurities to form precipitates, and as further asserted by the APT analyses (Fig. 3 and Table 2), this reaction leads to purification of the  $ \alpha $-Al matrix from these elements, which are unwanted as they decrease EC. The  $ \alpha $-Al composition measured by APT also demonstrates supersaturation of all Zr available in the alloy in  $ \alpha $-Al matrix (Table 2). Average Zr concentration in  $ \alpha $-Al matrix measured by APT is slightly higher than the Zr concentration in the alloy provided in Table 1 ( $ \sim $0.40 vs. 0.34 wt. %). This is likely due to the overestimation of Zr by APT as earlier studies have also emphasized the more complicated quantification of Zr content due to its presence with five isotopes at two different charge states and other potential causes [10,27]. No substantial discrepancy is noted between melt-pool boundary and interiors in terms of Zr concentration of  $ \alpha $-Al matrix (Table 2). Small standard deviation corresponding to the measured Zr concentration (Table 2) which is the averaged value from three or four individual tips, also points to the more uniform distribution of Zr within the melt-pool. APT measurements revealed no Ce, Fe and Sn in  $ \alpha $-Al matrix (Table 2).

## 3.2. Hardness and electrical conductivity evolution with aging

The isochronal aging study (Fig. S_{3}) of the Al-Zr-Ce-Cu alloy indicates that a slight hardness increase ( $ \sim $10 HV) occurs at 350 ^\circC, with near-peak aging condition achieved at 375 ^\circC. An isothermal aging study was, therefore, performed at 375 ^\circC, as summarized in Fig. 4. Alloy hardness in as-fabricated state is  $ \sim $40 HV. Aging for 30 h produces near peak hardness of  $ \sim $62 HV, which then remains unchanged with
Fig. 2. (a) The XRD spectra showing the identified phases in as-fabricated Al-Zr-Ce-Cu alloy and (b) the Scheil solidification curve (PanAl2024c database) for Al-Zr-Ce-Cu alloy composition excluding Fe and Si impurities from analysis.
Fig. 3. (a) The 3D reconstruction of APT tip with (Ce,Cu)-rich particle indicated by arrow and (b) the proxigram showing the distribution of various solutes from the surface (at zero distance) towards interior (positive direction) of (Ce,Cu)-rich particle.

Table 2

The composition of  $ \alpha $-Al matrix in as-fabricated state, as measured by APT. The elemental concentration is the average of three individual APT tips, and the corresponding standard deviation is given in parenthesis.

|  | Al | Zr | Ce | Cu | Si | Sn | Fe |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Melt pool core | Bal. | 0.41 ( $ \pm $0.07) | - | 0.08 ( $ \pm $0.01) | 0.06 ( $ \pm $0.02) | - | - |
| Melt pool boundary | Bal. | 0.43 ( $ \pm $0.06) | - | 0.06 ( $ \pm $0.02) | 0.05 ( $ \pm $0.01) | - | - |

further aging up to 100 h (Fig. 4a). The as-fabricated alloy has an EC value of 47.5 % IACS which significantly increases to ~58 % IACS after aging for 70 h (Fig. 4b). The peak hardness for the isochronally aged sample was higher than for the isothermally aged sample (~77 vs. ~62 HV). This difference reflects the beneficial effect of low-temperature aging during isochronal aging in providing a higher driving force for precipitate nucleation [28]. To further understand this distinction, some specimens were subjected to two-step aging, with the first step at 350 ^\circC for 5 h and the second step at 375 ^\circC for 100 h; as summarized in Table 3, this produces much higher hardness compared with the single-step aged sample (~71 vs. ~62 HV), while exhibiting comparable EC values of ~58 % IACS.

## 3.3. Aged microstructures

Fig. 5 summarizes the microstructural changes in the Al-Zr-Ce-Cu alloy after peak aging (375 ^\circC/100 h). As displayed in Fig. 5a, the (Ce, Cu)-rich submicron precipitates formed on solidification show no notable coarsening tendency during aging, as their size is comparable to that in an as-fabricated state (Fig. 5a vs. Fig. 1d). The Sn precipitates are again observed adjacent to (Ce,Cu)-rich precipitates (Fig. S_{4}). As noted in Fig. 5b and its inset, aging-induced L12-Al3Zr nanoprecipitates are finely distributed throughout the \alpha-Al matrix interiors. These precipitates are ~7.5 nm in diameter. Given that all Zr in the alloy remained in solid solution upon solidification, and assuming that all excess Zr (i.e., those beyond its solubility in \alpha-Al) at 375 ^\circC is precipitated out as L12-Al3Zr, its volume fraction (in %) is estimated as 0.25 %. The APT data from the alloy aged at a single step show that L12-precipitates also contain minor amounts of Si (Fig. 5c and Table 4).

Two-step aging (350 ^\circC for 5 h + 375 ^\circC/100 h) was applied to provide a higher driving force for the nucleation of L12-precipitates. As noted from the APT data from the specimen after initial 350 ^\circC/5 h aging, more numerous L12-precipitates sized ~2.6 nm in diameter were observed, with Si distributed in their interiors (Fig. 5d). The subsequent
Fig. 4. Temporal evolution of (a) hardness and (b) EC with aging at 375 ^\circC for Al-Zr-Ce-Cu. Dashed lines indicate the minimum electrical conductivity needed for some EV applications [3] and the measured EC for commercially pure (CP) Al (99.9 %).

Table 3 Electrical conductivity and hardness of Al-Zr-Ce-Cu alloy in as-fabricated state as well as after single-step aging (at 375 ^\circC for 100 h) or two-step aging (at 350 ^\circC for 5 h plus 375 ^\circC for 100 h). The corresponding standard deviations are provided in parentheses.

|  | EC, \%IACS | Hardness, HV |
| --- | --- | --- |
| As-fabricated | 47.5 ( $ \pm $0.1) | 40.9 ( $ \pm $1.0) |
| Single-step aged | 58.2 ( $ \pm $0.1) | 62.5 ( $ \pm $1.3) |
| Two-step aged | 58.5 ( $ \pm $0.1) | 70.8 ( $ \pm $0.8) |

aging at 375 ^\circC/100 h produced finer (~5.1 nm in diameter) and more numerous L12-precipitates compared with single-step aging (Fig. 5e vs. Fig. 5b,c).

## 3.4. Mechanical properties

## 3.4.1. Tensile properties

Tensile properties at 20 and 200 ^\circC were measured, as summarized in Fig. 6, for the Al-Zr-Ce-Cu alloy in both the as-fabricated state and after direct aging at 375 ^\circC for 100 h (single-step aging) or at 350 ^\circC for 5 h and then 375 ^\circC for 100 h (two-step aging). As displayed in Fig. 6a, yield strength (YS) at room temperature in the as-fabricated state was ~75 (\pm0.3) MPa, which increases to ~125 (\pm0.4) MPa after 375 ^\circC/100 h aging. Two-step aging produced a larger strengthening effect as the YS doubles to ~150 MPa. Strain hardening was pronounced for both as-fabricated and aged samples, which yielded ultimate tensile strength
Fig. 5. (a,b) High-angle annular dark-field (HAADF) STEM micrographs showing the distribution of (a) (Ce,Cu)-rich submicron particles and (b) L1₂-Al₃Zr nanoprecipitates, and (c) APT results showing the distribution of L1₂-Al₃Zr precipitates and their composition in Al-Zr-Ce-Cu alloy aged at 375 ^\circC for 100 h; (d,e) APT results showing the distribution of L1₂-Al₃Zr precipitates and their composition in Al-Zr-Ce-Cu alloy after (d) initial pre-ageing at 350 ^\circC for 5 h and (e) two-step aging at 350 ^\circC/5 h and 375 ^\circC/100 h.

The composition (in wt. %) of  $ \alpha $-Al matrix in single-step and two-step aged Al-Zr-Ce-Cu alloy measured by APT. The elemental concentration is the average of three individual APT tips, and the corresponding standard deviation is given in parenthesis.

|  | Al | Zr | Ce | Cu | Si | Sn | Fe |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Single-step aged | Bal. | 0.05 ( $ \pm $0.01) | - | 0.07 ( $ \pm $0.02) | 0.05 ( $ \pm $0.01) | - | - |
| Two-step aged | Bal. | 0.03 ( $ \pm $0.01) | - | 0.12 ( $ \pm $0.01) | 0.03 ( $ \pm $0.01) | - | - |

(UTS) values  $ \sim $25 MPa higher than the respective YS. Across all alloy conditions tested at ambient temperature, the elongation at break was around 20 %, with uniform elongation of roughly 11 %, demonstrating high ductility.

At 200 ^\circC (Fig. 6b), the YS in the as-fabricated state was ~65 (\pm0.2) MPa – a decrease of ~10 MPa relative to the room-temperature measurement. Unexpectedly, the YS of aged samples, regardless of aging condition, was only marginally affected by the microstructural changes induced by aging: the YS for the single-step-aged sample was comparable to the as-fabricated state, while a slightly higher YS by 5 MPa was noted for the sample subjected to two-step aging. Strain hardening was minimal. While the elongation at break increased to around 30–40 % depending on alloy condition, the uniform elongation dropped to ~2–5 %.

Given the unexpected YS values obtained for aged samples at 200 ^\circC, further tensile tests were conducted at various strain rates to determine strain-rate sensitivity m, defined as:

 $$ m=\frac{\partial l n(\sigma_{T})}{\partial l n(\dot{\varepsilon}_{T})} $$ 

where,  $ \sigma_{T} $ and  $ \varepsilon_{T} $ are true stress and true strain-rate, respectively. As-

fabricated samples tested at 200 ^\circC showed limited strain rate sensi-

tivity (m = 0.01, Table 5) as the YS remains constant at ~65 MPa within

four orders of magnitude strain rate range studied here (Fig. 6c).

Increasing the strain rate improves alloy ductility (Fig. 6c). The two-

step-aged sample, by contrast, shows a higher strain rate sensitivity (m

= 0.08) when tested at 200 ^\circC (Table 5). In other words, the YS is ~125

MPa at a high strain rate of 0.1 s $ ^{-1} $ at 200 ^\circC, as compared to ~65 MPa

when tested at a much lower strain rate of 2 \times 10 $ ^{-4} $ s $ ^{-1} $ (Fig. 6d). The

two-step-aged sample when tested at room temperature at various strain

rates, shows a very low strain rate sensitivity of 0.01 (Table 5).

## 3.4.2. Creep performance

Fig. 7a,b displays the temporal creep strain evolution curves of Al-Zr-Ce-Cu alloy at 200 ^\circC in compression in the as-fabricated and two-step-aged states (Fig. 7). Distinctly different creep performance is noted for as-fabricated and aged conditions. The aged alloy is characterized by the development of typical primary and secondary creep at any given stress during multi-load compressive creep (Fig. 7a). The dislocation storage and dynamic recovery are balanced following the primary creep that produces a measurable minimum secondary creep strain rate (Fig. 7a). By contrast, the as-fabricated specimen shows some primary creep, but
Fig. 6. (a,b) Tensile stress and strain curves at (a) 20 ^\circC and (b) 200 ^\circC for Al-Zr-Ce-Cu alloy in as-fabricated and after two different aging heat treatments; (c) tensile stress and strain curves at 200 ^\circC and various strain rates for as-fabricated Al-Zr-Ce-Cu alloy and (d) tensile stress and strain curves at 20 and 200 ^\circC, and various strain rates for Al-Zr-Ce-Cu alloy in as-fabricated and two-step aging heat treatment.

Table 5 Strain rate sensitivity m values at yield point estimated for Al-Zr-Ce-Cu alloy in as-fabricated and aged states at 20 and 200 ^\circC. The m value for aged alloy at 200 ^\circC was measured for strain rates of  $ 2 \times 10^{-4} \, s^{-1} $ and above.

|  | 20 ^\circC | 200 ^\circC |
| --- | --- | --- |
| As-fabricated | - | 0.01 |
| Two-step aged | 0.01 | 0.09 |

no measurable secondary creep (Fig. 7b). The extent of primary creep is low up to  $ \sim $65 MPa (i.e., up to alloy’s yield point, Fig. 6b), but it becomes pronounced at higher stresses (Fig. 7b). This observation indicates that the as-fabricated alloy has no, or limited, dynamic recovery, thus leading to the saturation of dislocation density for a given stress followed by complete suppression of dislocation creep.

Further creep experiments were carried out in tension at 200 ^\circC (Fig. 7c) to reveal the differences between the as-fabricated and aged states of Al-Zr-Ce-Cu alloy in terms of their creep resistance and creep lifetime. For the aged alloy, the minimum strain rate increased, while creep lifetime decreased with stress. At an applied stress of 55 MPa, the aged alloy has a creep lifetime of ~18 h, which increased to ~115 and ~560 h as stress decreases to 52.5 and 50 MPa, respectively. By contrast, and quite remarkably, the as-fabricated alloy showed no measurable (near-zero) tensile creep rate at 55 MPa and remained unruptured for ~860 h, after which the creep test was discontinued (Fig. 7c). Even when tested at 200 ^\circC and 60 MPa, which is ~5 MPa lower than its YS, the as-fabricated alloy showed no sign of measurable creep deformation (Fig. S_{5}). When the applied stress was increased to 70 MPa (5 MPa above the measured YS) after near-zero tensile creep at 60 MPa for ~500 h, the specimen ruptured (Fig. S_{5}).

## 3.4.3. Post-creep microstructures

Post-creep microstructures were characterized using TEM to gain insight into the precipitate-dislocation interaction nature and the dynamic recovery processes. For comparison, representative bright-field STEM micrographs of Al-Zr-Ce-Cu alloy in the as-fabricated state as well as after single-step aging are provided in Fig. 8, which show a low density of matrix dislocations prior to creep.

The dislocation structures formed during creep in aged and as-fabricated Al-Zr-Ce-Cu alloy are summarized in Fig. 9. Some differences in the process of dislocation entanglement and dynamic recovery are noted between the two different alloy conditions. Here, the term ‘sub-grain boundary’ refers to the well-defined, regular network of dislocations which stems from dynamic recovery. The tangled dislocation walls with no sign of well-defined, regularly arranged dislocation network are referred to as ‘cell boundaries’.

The crept specimen of the aged alloy, whose creep history is displayed in Fig. 7a, reveals dislocation entanglement leading to the development of subgrain structures, with multiple mobile dislocations within the subgrains (Fig. 9a). This subgrain structure development is likely facilitated by dislocation climb as such boundaries are primarily formed by this process [29]. Also, some regions display a hexagonal network of perfect dislocations,  $ b = 1/2 < 110> $ on  $ \{111\} $ planes (the SADP corresponding to Fig. 9b is provided as inset in Fig 9a), and this type of dislocation structure stems from the cross-slip of screw dislocations [29,30]. Subgrain interiors have a high density of edge dislocations which interact strongly with (Ce,Cu)-rich particles, and there is no sign of dislocations being pinned by, or bowing around, L12-Al3Zr precipitates, indicating a weak interaction between dislocations and the L12-Al3Zr precipitates (Fig. 9c). This observation is also consistent with the tensile tests of aged alloy at 200 ^\circC (Fig. 6d), in that dislocations tend to overcome L12-precipitates by climb relatively easily at  $ < 10^{-4} $ s $ ^{-1} $ strain rates. The strong dislocation interaction with (Ce,Cu)-rich particles is particularly visible in Fig. 9d, which also shows the absence of such interaction between dislocations and L12-Al3Zr precipitates.

The dislocation structures developed during creep of the as-fabricated alloy were investigated at two different stages of compressive creep: (i) after a single-load creep at 55 MPa for  $ \sim $ 48 h, which had  $ \sim $0.3 % total strain accumulated during primary creep (see creep data in
Fig. 7. Temporal creep strain evolution curves for AM Al-Zr-Ce-Cu alloy at 200 ^\circC: (a,b) stress-jump compressive creep tests on specimens in (a) aged and (b) as-fabricated states, and (c) single-load tensile creep tests on as-fabricated and aged states. The specimen from as-fabricated alloy showed near-zero creep at 55 MPa (as well as at 60 MPa, Fig. S_{5}), and the test was interrupted after ~860 h creep exposure. The dotted line along with the arrow points to the projected creep response of this condition at even longer creep exposures. All axes are in linear scales, except for the x axis in (c) that is in logarithmic scale.
Fig. 8. Bright-field STEM micrographs, acquired along (a) [001]Al and (b) [101]Al zone axes, showing a low density of dislocations in \alpha-Al matrix containing (Ce, Cu)-rich particles in AM Al-Zr-Ce-Cu alloy in (a) as-fabricated and (b) aged states.

Fig. S_{6}), and (ii) after a stress-jump creep at various stresses which led to the accumulation of  $ \sim $12 % creep strain in the specimen (the creep curve is displayed in Fig. 7b). As-fabricated specimen crept at 55 MPa, which had a primary creep leading to  $ \sim $ 0.3 % strain and no measurable secondary creep, shows numerous dislocations in the grain interiors (Fig. 9e). While no clear sign of creep-induced subgrain development is found, entangled dislocations are noted (Fig. 9f). A strong dislocation interaction with (Ce,Cu)-rich particles is obvious in Fig. 9f and its inset. The atomic-resolution TEM micrograph (Fig. 9g) and the associated inverse fast-Fourier transform (iFFT) map (Fig. 9h) reveal the presence of multiple edge dislocations in  $ \alpha $-Al matrix. The as-fabricated specimen that underwent  $ \sim $12 % compressive creep deformation (see Fig. 7b for creep history) also reveals multiple dislocations in the grain interiors with highly entangled dislocations as well as a hexagonal network of dislocations (b = 1/2 < 110> on {111} planes), with such dislocations known to have a pure screw character [29]. Unlike in the aged alloy, where subgrain growth likely involving dislocation climb is notable (Fig. 9a), the as-fabricated alloy shows no such characteristic dislocation (subgrain) structure evolution (Fig. 9i–k), consistent with the slow, or absence of, climb-assisted dynamic recovery during creep (Fig. 7b). Cell walls consisting of entangled dislocations likely formed during work hardening (primary creep) were also noted (Fig. 9i).

The as-fabricated specimen crept to 12 % compressive strain was characterized using APT to determine the resultant compositional

Aged (350 ^\circC/8h) and crept in compression (40-63 MPa, ~12% strain)

As-fabricated and crept in compression (55 MPa, ~0.3% strain)

As-fabricated and crept in compression (50-69 MPa, ~12% strain)
Fig. 9. A summary of dislocation structures in post-creep specimens from (a-d) single-step-aged alloy crept at 40–63 MPa stresses until 12 % strain, (e-h) as-fabricated alloy crept at 55 MPa for 48 h, and (i-k) as-fabricated alloy crept at 50–69 MPa stresses until 12 % strain. All bright-field TEM micrographs were acquired with zone axis (ZA) aligned along [101]Al and selected area diffraction patterns (SADPs) provided as insets in (a), (e), and (i) correspond to (a-d), (e,f), and (i-k), respectively. An inverse fast-Fourier transform (iFFT) map in (h) corresponds to the region within the marked square in (g) and was acquired using {111}. Al planes circled in the FFT (an inset in (g)).

changes in the matrix interiors. Fig. S_{7} shows one of the several analyzed APT tips, revealing fine Sn precipitates and no Zr-rich precipitates. All Zr remained fully in solid solution, as the temperature is too low for its precipitation during creep (Table 6).

## 4. Discussion

## 4.1. Alloy composition selection and microstructure evolution

The rationale behind the composition selection for this new Al-0.3Zr-0.2Ce-0.2Cu (wt. %) alloy is as follows. Slow-diffusing Zr is known to improve alloy creep resistance through L12-Al3Zr precipitation [7,31,32], while its limited solid solubility upon aging contributes to preserving the conductivity of the pure \alpha-Al matrix. Although the rapid solidification resulting from laser additive manufacturing allows for Zr supersaturation higher than 0.34 wt. % Zr (equivalent to 0.10 at. % Zr), this level of Zr addition was selected to study the feasibility of retarding dislocation climb (the mechanism that activates at elevated temperatures in Al alloys) while producing minimal conductivity loss. Cerium also displays slow diffusivity and low solubility in \alpha-Al. Because Ce tends

## Table 6

The  $ \alpha $-Al matrix composition measured by APT in as-fabricated Al-Zr-Ce-Cu alloy specimen crept in compression at 200 ^\circC and 50–69 MPa stresses to 12 % strain. The elemental concentration is the average of three individual APT tips, and the corresponding standard deviation is given in parenthesis.

|  | Al | Zr | Ce | Cu | Si | Sn | Fe |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Wt. | Bal. | 0.40 | - | 0.13 | 0.03 | - | - |
| % |  | $  (\pm0.020)  $ |  | $  (\pm0.020)  $ | $  (\pm0.003)  $ |  |  |

to react with Cu, Fe, Si and other typical impurities in Al alloys [33,34], Ce is expected to form, under rapid solidification conditions, highly refined intermetallic particles which also improve alloy strength and creep resistance as well as contributing to the higher level of conductivity of  $ \alpha $-Al by scavenging impurities in solid solution.

The high solidification rates intrinsic to AM completely suppressed the formation of primary Al₃Zr particles, which were expected from Scheil simulation of the alloy (Fig. 2b). Grains were elongated over multiple melt pools (Fig. 1a), indicating that strong epitaxial grain growth dominated during solidification. The regions right above the melt pool boundaries showed no (Ce,Cu)-rich intermetallic particles (Fig. 1c), forming particle-free zones consistent with initial epitaxial planar grain growth. High thermal gradient (G) and low solidification (growth) rate (R), coupled with limited constitutional supercooling from low solute content in the alloy, are responsible for initial planar solidification [35,36]. As solidification proceeds, solutes (i.e., Ce and Cu) are being rejected to the liquid, which eventually produces a degree of constitutional supercooling with protrusions sufficient to destabilize planar growth front and promote cellular grain growth [36]. Solute rejection during cellular grain growth also encourages formation of (Ce, Cu)-rich particles, evident from SEM and STEM observations (Fig. 1), and consistent with the Scheil solidification model (Fig. 2b). Aging causes no changes in the characteristics of these (Ce,Cu)-rich particles but leads to L1₂-Al₃Zr precipitation (Fig. 5). Discussion on solid-state precipitation kinetics of L1₂-Al₃Zr precipitates, and the role of impurities, such as Si, in Al alloys can be found elsewhere [33].

## 4.2. Electrical resistivity

Matthiessen’s rule is often utilized to describe the electrical resistivity of aluminum alloys. According to this rule, the electrical resistivity of dilute alloys is the sum of two independent contributions arising from the established temperature and microstructure [5,37,38]. The total electrical resistivity,  $ \rho_{Total} $, combining the contributions of various microstructural features at a given temperature is then given by:

where,  $ \rho_{Al} $ is the electrical resistivity of a defect-free pure Al (2.7  $ \mu\Omega\cdot cm $ at  $ \sim20\ ^{\circ}C $ [37]), and  $ \rho_{SS} $,  $ \rho_{ppt} $,  $ \rho_{vac} $,  $ \rho_{disl} $, and  $ \rho_{GB} $ are the contributions from the solutes in solid solution, precipitates, vacancies, dislocations, and grain boundaries, respectively. The respective models for estimating the contribution of each factor are provided in Appendix A. Results are listed in Table 7.

Among various microstructural factors, Zr in solid solution produces the greatest contribution to resistivity: 0.34 wt. % Zr in the as-fabricated state results in  $ \sim $0.58  $ \mu\Omega\cdot $cm, while the presence of  $ \sim $0.06 wt. % Zr in solid solution after aging (according to APT data, Table 7) translates into  $ \sim $0.1  $ \mu\Omega\cdot $cm. The increment due to the precipitates is relatively minor:  $ \sim $0.06  $ \mu\Omega\cdot $cm in as-fabricated state (due to (Ce,Cu)-rich particles) vs. 0.11  $ \mu\Omega\cdot $cm in the aged state (due to a combination of (Ce,Cu)-rich and Al $ _3 $Zr particles). The increment due to cell boundaries is  $ \sim $0.08  $ \mu\Omega\cdot $cm, pointing to the minor effect of cell size on the electrical resistivity. The contribution of vacancies and dislocations can be ignored given their limited effect on electrical resistance [5,37].

The theoretically estimated electrical resistivity of alloy shows good agreement with the experimental data in both as-fabricated and aged states. The somewhat higher resistivity obtained experimentally as compared to estimated theoretically (3.63 vs. 3.46 \mu\Omega·cm) may reflect the contribution of other solutes, such as Sn, Cu, Si, that are present at minor levels in \alpha-Al matrix (Table 2) but were ignored in estimating alloy resistivity. While aged alloy has the conductivity equivalent to ~90 % of pure Al (65 %IACS [39]), the conductivity of ~48 %IACS achieved in the as-fabricated state is still higher than that of other Al alloys: ~22 % higher compared to Al-7Si-0.3Mg in T6 state [39] and ~5 % higher compared to the recently introduced AM Al-1Fe-1Zr (wt. %) conductor alloy in aged state [36].

## 4.3. Strengthening mechanisms

The yield stress of 75 MPa measured for the as-fabricated alloy is a combination of grain-boundary, solid-solution, and dispersion strengthening mechanisms through the following general equation:

 $$ \sigma_{Y S}=\sigma_{0}+\Delta\sigma_{O r}+\Delta\sigma_{S S}+\Delta\sigma_{G B}, $$ 

where  $ \sigma_{YS} $ is the theoretically estimated YS,  $ \sigma_{0} $ is the Peierls-Nabarro stress (which is equal to 20 MPa for Al),  $ \Delta\sigma_{Or} $ is the Orowan strengthening contribution of (Ce,Cu)-rich particles,  $ \Delta\sigma_{SS} $ is the solid-solution, and  $ \Delta\sigma_{GB} $ is the grain-boundary strengthening contributions. The equations describing each of these mechanisms are provided in Appendix B, and the estimated results are displayed in Fig. 10.

The Orowan strengthening contribution from the intermetallic particles is estimated as  $ \sim $45 MPa. Zr in solid solution produces 4.4 MPa for as-fabricated alloy. For grain boundaries,  $ \Delta\sigma_{GB}=6 $ MPa is estimated. As summarized in Fig. 10a, the sum of all strengthening contributions is  $ \sim $76 MPa which is similar to the experimentally measured YS of 75 MPa. These results indicate the (Ce,Cu)-rich intermetallic particles are the dominant strengthening factor in the as-fabricated alloy.

For aged alloys, additional strengthening originates from L1₂-Al₃Zr precipitates at the expense of the loss of the solid-solution strengthening effect of Zr. Since L1₂-Al₃Zr precipitates are coarser than the critical diameter of 4 nm above which Orowan looping (rather than precipitate shearing) dominates [8], the same equation holds for both L1₂-Al₃Zr and (Ce,Cu)-rich precipitates.  $ \Delta\sigma_{Or}^{Al3Zr}=102 $ and 132 MPa are obtained for single- and double-step aged alloy, respectively. These values are more than twice the contribution from Orowan strengthening of (Ce,Cu)-rich precipitates. Given that the matrix dislocations bypass Al₃(Sc,Zr) nanoprecipitates and (Ce,Cu)-rich sub-micron precipitates sequentially, the group of precipitates producing the greater resistance to dislocation dictates the Orowan strengthening contribution [33]. Thus, considering the strengthening contribution of L1₂-Al₃Zr precipitates and ignoring that of (Ce,Cu)-rich intermetallic particles result in  $ \sigma_{YS} $ values of 126 and 154 MPa for 375 ^\circC/100 h and 350 ^\circC/5 h, 375 ^\circC/100 h aged alloys, respectively. These values are roughly comparable to the measured YS values, as displayed in Fig. 10a, thus confirming that L1₂-Al₃Zr precipitates are the dominant strengthening microstructural feature in aged alloys at ambient temperature.

To estimate the yield stress at 200 ^\circC, a shear modulus value  $ \mu = 23 $ GPa for Al is taken at 200 ^\circC [40], for which Eq. (2) gives  $ \sigma_{YS} = 72 $ MPa for the as-fabricated alloy, and 117 and 144 MPa after single- and double step aging, respectively. While good agreement is achieved for the as-fabricated alloy (the sum of all contributions from various mechanisms equals 72 MPa vs. the measured YS at 200 ^\circC of 65 MPa), the discrepancy between experimental and modeling results for aged conditions is significant (Fig. 10b), with Eq. (2) predicting a YS which is >50 MPa higher than the experimental measurements. The aged alloy, however, displayed a high strain rate sensitivity m of 0.08 at 200 ^\circC (Table 5), with the YS reaching 120 MPa when measured at  $ 10^{-1} $ s $ ^{-1} $ strain rate (Fig. 6d). The as-fabricated alloy, by contrast, displayed a low m value of 0.01 at 200 ^\circC. The high m values in the aged alloy are consistent with the activation of dislocation climb over L12-Al3Zr precipitates at 200 ^\circC. Because dislocation climb requires appreciable vacancy diffusion [41,42], higher strain rates increasingly suppress climb over L12-Al3Zr precipitates by restricting the time for vacancy diffusion. The effectiveness of L12-Al3Zr and (Ce,Cu)-rich particles in restricting dislocation climb is further discussed in the following section. It is noted that when the theoretically estimated YS of the aged alloy is compared against its experimentally measured YS obtained at the higher strain rate of  $ 10^{-1} $ s $ ^{-1} $, the discrepancy diminishes and there is closer agreement between the modelling and experimental results (Fig. 10c).

The strain rate sensitivity m of 0.08 at 200 ^\circC for aged alloy is the obtained value for a studied range of strain rates, which in fact is as m = 0.03 for the two strain rates of  $ 2 \times 10^{-4} $ and  $ 10^{-5} $ s $ ^{-1} $ and m = 0.09 for higher strain rates. We have demonstrated that activation of dislocation climb explains the high m value. This study does not necessarily seek to model alloy YS at different strain rates, but rather to demonstrate how, when dislocation climb over L12-Al3Zr is suppressed at higher strain rates, model estimated values are in rough agreement with the YS measured at high strain rate. This model is valid only when dislocations bypass L12-Al3Zr precipitates by Orowan looping mechanism. Although strain rate variation may affect to a certain extent the process of

Experimentally measured and theoretically estimated electrical resistivity (in  $ \mu\Omega\cdot cm $) and the corresponding EC of Al-Zr-Ce-Cu alloy in as-fabricated and aged states.

<table border="1" style="margin: auto; word-wrap: break-word;"><tr><td style="text-align: center; word-wrap: break-word;">Alloy state</td><td colspan="6">Estimated</td><td colspan="2">Experimental</td></tr><tr><td style="text-align: center; word-wrap: break-word;"></td><td style="text-align: center; word-wrap: break-word;">$ \rho_{Al} $</td><td style="text-align: center; word-wrap: break-word;">$ \rho_{SS} $</td><td style="text-align: center; word-wrap: break-word;">$ \rho_{ppt} $</td><td style="text-align: center; word-wrap: break-word;">$ \rho_{GB} $</td><td style="text-align: center; word-wrap: break-word;">$ \rho_{Total} $</td><td style="text-align: center; word-wrap: break-word;">%IACS $ _{Total} $</td><td style="text-align: center; word-wrap: break-word;">$ \rho $</td><td style="text-align: center; word-wrap: break-word;">%IACS</td></tr><tr><td style="text-align: center; word-wrap: break-word;">As-fabricated</td><td style="text-align: center; word-wrap: break-word;">2.7</td><td style="text-align: center; word-wrap: break-word;">0.6</td><td style="text-align: center; word-wrap: break-word;">0.06</td><td style="text-align: center; word-wrap: break-word;">~0.08</td><td style="text-align: center; word-wrap: break-word;">3.46</td><td style="text-align: center; word-wrap: break-word;">49.8</td><td style="text-align: center; word-wrap: break-word;">3.63</td><td style="text-align: center; word-wrap: break-word;">47.5</td></tr><tr><td style="text-align: center; word-wrap: break-word;">Peak-aged</td><td style="text-align: center; word-wrap: break-word;">2.7</td><td style="text-align: center; word-wrap: break-word;">0.1</td><td style="text-align: center; word-wrap: break-word;">0.11</td><td style="text-align: center; word-wrap: break-word;">~0.08</td><td style="text-align: center; word-wrap: break-word;">3.01</td><td style="text-align: center; word-wrap: break-word;">57.2</td><td style="text-align: center; word-wrap: break-word;">2.96</td><td style="text-align: center; word-wrap: break-word;">58.2</td></tr></table>
Fig. 10. A comparison of the theoretically estimated and experimentally measured YS values for Al-Zr-Ce-Cu alloy in as-fabricated state and after single- and two-step heat treatments at test temperatures of (a) 20 and (b,c) 200 ^\circC, with (b) and (c) providing experimental YS values from the tests conducted at 10⁻¹ and 10⁻⁴ s⁻¹ strain rates, respectively. Theoretically estimated individual contribution of various strengthening mechanisms is indicated for each alloy state and test temperature.

dislocations bypassing precipitates by Orowan looping, this aspect of strength modeling is beyond the scope of this work.

## 4.4. Creep mechanisms

 $$ L1_{2}Al_{3}Zr $$ 

Insight into the rate-limiting creep mechanisms can be inferred from the plot of the minimum strain rate  $ \varepsilon_{m} $ against stress  $ \sigma $ following Norton's power law:

where A is a dimensionless material constant,  $ n_{a} $ is the apparent stress exponent. As shown in Fig. 11a, pure Al displays  $ n_{a} = 5 $ at 200 ^\circC (as well as at 300 ^\circC, Fig. 11b), which is indicative of dislocation climb

 $$ \stackrel{\cdot}{\varepsilon}_{m}=A\sigma^{n_{a}} $$ 

being the rate-limiting mechanism [40]. The very high apparent stress exponent  $ n_{a} \sim 22 $ obtained for Al-Zr-Ce-Cu alloy is well above that for the five power-law creep. Precipitation-strengthened Al alloys, such as L12-strengthened ones [17,43], consistently show high  $ n_{a} $ values that stem from the presence of the threshold stress  $ \sigma_{th} $ for dislocation climb. Incorporation of  $ \sigma_{th} $ into Eq. (3) gives [44]:

 $$ \dot{\varepsilon}_{m}=A^{\prime}(\sigma-\sigma_{th})^{n} $$ 

where,  $ A' $ is a dimensionless material constant, n is the  $ \alpha $-Al matrix stress exponent (with n = 4.4 for pure Al [40]). By plotting  $ \dot{\varepsilon}_{m}^{1/n} $ vs.  $ \sigma $ (with n = 4.4 for pure Al [40]), as displayed in Fig. S_{8}, the threshold stress is determined as  $ \sigma_{th}=50 $ MPa, implying that dislocation creep at lower stresses is practically immeasurable. The question arises as to which group of precipitates – the (Ce,Cu)-rich particles, the L12-Al3Zr
Fig. 11. A logarithmic plot of (a) the minimum strain rate against applied stress and (b) minimum strain rate normalized with the aluminum self-diffusivity ( $ D_{L} $) against applied stress normalized with the aluminum shear modulus ( $ \mu $) for aged Al-Zr-Ce-Cu alloy, pure Al and other relevant Al alloys. The creep data for high-purity cast Al crept at 200 ^\circC [47], high-purity cast Al crept at 300 ^\circC [40], cast/aged Al-Zr [32], and Al-Zr-Sc [8] alloys. Tensile and compressive creep data for aged Al-Zr-Ce-Cu alloy are indicated by full and open symbols, respectively. The creep test temperatures are provided in parenthesis in (b). Approximate precipitate radii  $ \langle R \rangle $ in various alloys is also provided in (b) for comparison. Temperature-dependent  $ \mu $ and  $ D_{L} $ values for Al are from Ref. [40].

nanoprecipitates or combination of both - is responsible for such high creep resistance. The TEM analyses of dislocation structures after creep revealed strong interaction of dislocations with (Ce,Cu)-rich precipitates, but not with L12-Al3Zr precipitates (Fig. 9a–d). These results are consistent with the tensile tests in that L12-Al3Zr precipitates show no or limited contribution to the measured yield strength at relatively lower strain rates of  $ 10^{-4} - 10^{-5} $ s $ ^{-1} $ (Fig. 6d).

To further assert this point, creep data on pure Al, cast L12-strengthened Al-Zr(-Sc) alloys and our AM Al-Zr-Ce-Cu alloy are plotted in Fig. 11b after normalizing with temperature-dependent parameters, allowing comparison between creep tests carried out at various temperatures. Creep data for pure Al measured at 200 and 300 ^\circC overlaps, which is consistent with dislocation climb dictating its creep behavior. A cast/aged Al-Zr alloy [32] has comparable Zr concentration and L12-Al3Zr precipitate size to our AM Al-Zr-Ce-Cu alloy, but its creep resistance is lower (Fig. 11b). Cast/aged Al-Sc-Zr [8] has relatively higher fraction of larger L12-Al3Zr precipitates than cast/aged Al-Zr alloy which is responsible for their higher creep resistance. However, both cast/aged Al(-Sc)-Zr alloys have lower creep resistance than aged AM Al-Zr-Ce-Cu alloy. Relatively coarser (Ce,Cu)-rich particles require higher stresses for dislocations to climb as they require greater dislocation line length increase [45]. The measured  $ \sigma_{th}=50 $ MPa value is close to the theoretically estimated stress of  $ \sim67 $ MPa at 200 ^\circC for aged alloy when only considering the combined contribution of Orowan strengthening effect of (Ce,Cu)-rich particles and grain-size hardening (Appendix B). This is also consistent with the fact that the strain rate sensitivity  $ m = 0.03 $ for the two strain rates of  $ 2 \times 10^{-4} $ and  $ 10^{-5} s^{-1} $, compared to  $ m = 0.09 $ obtained for higher strain rates (Fig. 6d and Table 5). At strain rates below  $ 10^{-4} s^{-1} $, the time and stress needed for the dislocation climb over L12-Al3Zr particles are both sufficiently high at any strain rate. Lower strain rates provide sufficient time for dislocations to climb over submicron (Ce,Cu)-rich particles. Thus, although climb occurs over (Ce,Cu)-rich particles, the threshold stress  $ \sigma_{th}=50 $ MPa is high, relative to the measured alloy YS at 200 ^\circC and a strain rate of  $ 10^{-5} s^{-1} $ (which is  $ \sim65 $ MPa, Fig. 6d). This observation is consistent with previous experimental studies showing increased ratio of threshold stress to Orowan stress for alloys with larger precipitates [8,41]. Moreover, other mechanisms, such as dislocation detachment for incoherent precipitates [46], may come into play too; however, understanding the exact nature of dislocation interaction with (Ce,Cu)-rich precipitates during climb is beyond the scope of this study.

## 4.4.2. Zr-solute-induced dislocation creep suppression

The fact that as-fabricated Al-Zr-Ce-Cu alloy with Zr-solute-strengthened  $ \alpha $-Al matrix shows no measurable secondary creep both below and above alloy yield point at 200 ^\circC (T/Tm ~ 0.5), as schematically illustrated in Fig. 12a, is surprising given the established fundamental knowledge on creep of Al alloys. As noted for pure Al as well as for L12-Al3Zr-strengthened cast Al-Zr(-Sc) and aged AM Al-Zr-Ce-Cu alloys, dislocation climb becomes a rate-limiting mechanism, with its rate highly sensitive to the characteristics (size, etc.) of precipitates for Al alloys (Fig. 10b) [8,32,40]. The process by which dislocation climb becomes rate-limiting is through either the control of dynamic recovery (e.g., in pure Al) or the resistance of strengthening precipitates for dislocation climb. The effectiveness of dislocation climb is sensitive to the nature of dislocation – precipitate interactions [48]. Limited primary creep and near-zero secondary creep below alloy’s yield point vs. large primary creep still with near-zero secondary creep (implying restricted dynamic recovery) above alloy’s yield point (Fig. 7b) indicates complete suppression of dislocation climb during creep of the as-fabricated alloy. Post-creep dislocation structures of as-fabricated alloy (Fig. 9e–k) are consistent with the absence of dislocation climb and related subgrain development during creep. Large primary-creep strain is obtained above alloy’s yield point (Fig. 7b) because the moving dislocations tend to initially surmount (Ce,Cu)-rich particles by Orowan looping. However, due to the imbalance between dislocation storage and dynamic recovery, creep strain rate becomes again near-zero once dislocation density saturates for a given applied stress (i.e., produces additional dislocation hardening contribution) (Fig. 7b).

Some solutes in  $ \alpha $-Al matrix are known to have a strong effect on dislocation climb process [17]. Sherby et al. [18] have shown that retaining  $ \sim $0.04 wt. % Fe in  $ \alpha $-Al matrix of cast Al-0.054Fe alloy leads to  $ 10^{6} $ times slower creep rates at 200 ^\circC compared to when the Fe concentration in  $ \alpha $-Al matrix is only  $ \sim $0.01 wt. %. Another study by Sherby et al. [19] also demonstrated that slow diffusing solutes (e.g., Mn, Fe, Ti) produce creep rates lower than that of pure Al, while those with diffusion coefficients higher than that of Al self-diffusion (e.g., Bi, Zn, Cu) produce comparably higher creep rates. Supersaturation of Mn in a L12-strengthened cast Al-Zr-Mn alloy leads to significantly lower creep rates at 300–400 ^\circC compared to its Mn-free variant due to Mn-induced suppression of dislocation climb [17]. Our as-fabricated Al-Zr-Ce-Cu alloy has supersaturated Zr in  $ \alpha $-Al matrix, which remained fully in solid solution (Table 6) and showed no sign of L12-Al3Zr precipitation during creep at 200 ^\circC (Figs. 9e,i and Fig. S_{7}). Based on these observations, we can infer that slow-diffusing Zr solutes in the  $ \alpha $-Al matrix are most likely responsible for the suppression of dislocation climb in as-fabricated Al-Zr-Ce-Cu alloy.

The AI self-diffusivity is barely affected by minor Zr additions [49], which cannot account for the observed dislocation climb suppression. More notable tracer diffusivity reduction requires much higher Zr
Fig. 12. (a) A schematic illustrating the observed temporal creep strain evolution curves for our Al-Zr-Ce-Cu alloy in as-fabricated and aged states and (b) Zr solute enhancement (10x the far-field concentration) around an edge dislocation in Al, redrawn from Ref. [17], with calculations made using combined quantum mechanical and continuum isotropic elasticity approach [17,55]. The dislocation core at (0,0) in (b) is represented by the dashed circle (radius  $ \approx $ Burgers vector magnitude).

concentration in solid solution than in our alloy (0.34 wt. % Zr). A 2–3x tracer diffusivity reduction has been estimated using Molecular Dynamics modelling for Al-17 wt. % Zr solid-solution alloy relative to pure Al [49]. However, the free energy reduction by solute diffusion to the core of edge dislocations can produce environments (i.e., Cottrell, Suzuki, and other types) that not only affect the gliding of dislocation on a slip plane, but also its climb [42]. Given the absence of dissociated dislocations (Fig. 9g,h), the Suzuki-type segregation to the stacking faults and the resulting chemical interaction to stabilize stacking faults is ruled out. Because dislocation glide occurs for our alloy when the stress level is high enough, as noted from high primary-creep strains (Fig. 7b) and the presence of numerous matrix dislocations (Fig. 9e–k), the near-zero secondary creep both below and above alloy’s yield strength points towards complete suppression of dislocation climb via the formation of a Cottrell atmosphere. Supersaturated Mn in  $ \alpha $-Al matrix leading to the suppression of dislocation climb has been attributed to its Cottrell dragging effect on the dislocations [17]. The high interaction energy of 0.54 eV between Mn solute and edge dislocation is believed to drive such segregation [17]. Although Zr solute has lower interaction energy of 0.14 eV with dislocation [17], increased Zr supersaturation due to rapid cooling enables Zr diffusion to the core of edge dislocation. Based on the first-principles calculations in Ref. [17] and reproduced in Fig. 11b, Zr tends to segregate to the tensile-deformed region of the edge dislocation. The necessity to move dislocation with its solute atmosphere may lead to an increase in the required stresses [50]. However, dislocation glide occurs with relative ease, as noted by high primary-creep strains and high initial strain-hardening rates (Fig. 7b), and complete suppression of dislocation climb may result from the altered vacancy diffusion conditions at/near dislocation cores.

According to recent first-principles density functional calculations [51,52], Zr prefers to form Zr-Zr pair in the second nearest neighbor (2NN) position rather than in the first nearest neighbor (1NN). When a Zr-Zr pair is formed in 2NN, the Zr-Zr-vacancy binding energy becomes 0.28 eV [51] – much higher than 0.05 eV for Zr-vacancy pair in 2NN [53]. These results indicate that it is energetically favorable for vacancy to form Zr – vacancy pair, particularly Zr – Zr – vacancy pair. Trapping of vacancies by Zr atoms near the core of edge dislocations is another possible explanation for the dislocation-climb-restricted creep behavior of our as-fabricated Al-Zr-Ce-Cu alloy. A plausible explanation for how such pairing can affect dislocation climb is the entrapment of vacancies by Zr near or at the core of dislocations, thus restricting vacancy flow (at a level) required for the positive or negative climb process to occur. In an earlier study [54], a favorable Zr solute - vacancy binding energy measured experimentally in Al-Zr alloy has, indeed, led to the conclusion that Zr traps vacancies by forming pairs and prevents vacancy condensation into dislocation loops. When such Zr solute - vacancy pairs control the climb rate, diffusivity of Zr in the Al lattice, rather than self-diffusion, becomes the rate limiting step that controls vacancy diffusion at or near dislocation cores. This hypothesis is also consistent with the findings of Sherby et al. [18] on cast Al-0.054Fe alloy, where retaining  $ \sim $0.04 wt. % Fe in  $ \alpha $-Al matrix leads to a dramatically slower creep rates at 200 ^\circC (by a factor  $ 10^{6} $) compared to when the Fe concentration in  $ \alpha $-Al matrix is only  $ \sim $0.01 wt. % and that the activation energy for creep equals that of Fe diffusion in  $ \alpha $-Al matrix only for the former alloy condition.

Not all solutes that form pairs with vacancies for energetic reasons may lead to this dislocation-climb suppressing effect. Energetically favorable solute interaction with dislocations, along with limited solute diffusivity in Al matrix and a sufficiently high concentration in Al matrix all must be fulfilled for the solute to be effective at suppressing dislocation climb in a certain temperature range [17]. Molecular Dynamics and other dedicated modelling efforts may be valuable to explore the underlying processes of Zr interaction with vacancies and edge dislocations and all the factors leading to climb suppression.

## 4.5. Implications for alloy design

A solute-lean Al-0.3Zr-0.2Ce-0.2Cu (wt. %) alloy composition was designed in this study to maximize the solubility of Zr in \alpha-Al, while avoiding primary Al₃Zr phase formation because extended solid solubility of Zr ensures improved combination of strength and conductivity. The benefits of adding Ce to the alloy is twofold. It scavenges common impurities in Al alloys, such as Cu, Fe, and Si, and it forms fine, numerous (Ce,Cu)-rich intermetallic particles with high strengthening effects. Owing to the limited solubility and slow diffusivity of Ce in \alpha-Al, these intermetallic particles remain coarsening-resistant during alloy aging at 375 ^\circC (which is performed to produce L1₂-Al₃Zr precipitates), hence maintaining the compatibility between Zr and Ce for maximized contribution of each component. Indeed, the aged Al-Zr-Ce-Cu alloy exhibits attractive properties: with a YS of ~150 MPa, a conductivity of ~58 %IACS, and a high creep resistance at 200 ^\circC with limited dislocation creep below ~40 MPa, this alloy shows promise for conductor applications.

A new strategy of fully suppressing dislocation creep at stresses up to alloy’s YS, which we achieve here by supersaturating slow-diffusing Zr in  $ \alpha $-Al matrix, represents a conceptual change in conductor alloy design for creep-relevant environments. A conductivity of  $ \sim $48 %IACS even when all Zr remains in solid solution and the feasibility of achieving such unprecedented creep resistance at even lower Zr levels (which translates into higher EC values) provide new pathways for designing highly creep resistant Al conductor alloys needed in a wide variety of applications, such as rotors, inverters, busbars, windings, heat exchangers/sinks. Although such improvement may be expected by adding other slow-diffusing transition metals (e.g., Ti, Mn, and V), Zr stands out among these elements due to its least negative effect on alloy conductivity, on a wt. % basis.

The other key feature of as-fabricated microstructure is the more homogeneous distribution of Zr in  $ \alpha $-Al grain interiors enabled by the rapid solidification capability of additive manufacturing. Such homogeneity is intrinsically challenging to achieve in cast alloys due to heavy Zr segregation to  $ \alpha $-Al grain cores due to its peritectic reaction and the large equilibrium partitioning coefficient for  $ \alpha $-Al solidification [32,56]. The extent of heterogeneity in Zr distribution leading to Zr-free/lean regions near the grain boundaries in cast Al-Zr alloy can be seen in Ref. [32]. Homogeneous Zr distribution in AM Al-Zr-Ce-Cu alloy enables the suppression of dislocation climb throughout the grain interiors and avoids the formation of locally weak regions (links) which otherwise limit the creep resistance and lifetime in this alloy system [12,13,15].

## 5. Summary and conclusions

A new Al-0.3Zr-0.2Ce-0.2Cu (wt. %) alloy was additively manufactured via laser powder-bed fusion. The microstructure, electrical conductivity, and mechanical properties (tensile properties at 20 and 200 ^\circC, and creep resistance at 200 ^\circC) in as-fabricated and aged states were measured to establish microstructure-property relationships. The following conclusions were drawn from this study.

- Limited solute content and high thermal gradient at/near melt pool boundaries caused strong epitaxial planar  $ \alpha $-Al grain growth in the early stage of solidification, which then transitioned to the cellular  $ \alpha $-Al growth mode, with multiple cells formed within each coarse  $ \alpha $-Al grain elongated across several melt pools. High cooling rate during solidification completely suppressed the formation of primary  $ Al_{3}Zr $ particles and led to the formation of fine, numerous (Ce,Cu)-rich intermetallic particles which scavenge Cu, Fe, and Si, thus producing and  $ \alpha $-Al matrix with much reduced impurity levels in solid solution in the as-fabricated state, thus contributing to reduced electrical resistivity.

• Two-step aging (350 ^\circC/5 h + 375 ^\circC/100 h) produces L12-Al3Zr nanoprecipitates which are finer and more numerous as compared to

single-step peak-aging (375 ^\circC/100 h); these nanoprecipitates, when combined with extended Zr solute trapping in the \alpha-Al matrix, confers to the alloy an excellent strength-conductivity combination (a yield strength of ~150 MPa and electrical conductivity of ~58 % IACS). The aged alloy, compared to as-fabricated one, shows high strain-rate sensitivity at 200 ^\circC consistent with dislocation climb occurring over L12-Al3Zr nanoprecipitates at strain rates as high as 10⁻³–10⁻² s⁻¹.

• Aged alloy shows excellent creep resistance at 200 ^\circC, with limited dislocation creep below 40 MPa and activated dislocation climb with the threshold stress at higher stresses. The as-fabricated alloy with supersaturated Zr in \alpha-Al matrix has near-zero creep rates, implying very long creep lifetimes, as opposed to aged (L12-strengthened) alloy with creep lifetimes of 18–450 h at equivalent stresses.

Jovid Rakhmonov: Writing – original draft, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. Jonathan

• The solute-induced dislocation-creep suppression mechanism is attributed to the interaction of Zr solute with dislocations, which makes them immobile likely by forming Cottrell atmospheres. This finding offers new avenues for designing novel lightweight alloys for electrical conductors and other applications given the feasibility of achieving such performance with limited Zr supersaturation, thus, with minimal negative impact on alloy conductivity.

Poplawsky: Investigation, Data curation. Lawrence Allard: Investigation. James Burns: Data curation, Investigation. Jie Qi: Investigation, Data curation. Ismael Coello: Investigation, Data curation. David C. Dunand: Writing – review & editing, Supervision. Sumit Bahl: Writing – review & editing. Alice Perrin: Writing – review & editing, Investigation, Data curation. J. Allen Haynes: Writing – review & editing, Project administration, Funding acquisition, Conceptualization. Alex Plotkowski: Writing – review & editing, Funding acquisition, Conceptualization. Amit Shyam: Writing – review & editing, Supervision, Resources, Funding acquisition, Conceptualization.

## CRediT Authorship

The authors declare the following financial interests/personal relationships which may be considered as potential competing interests:

## Declaration of Competing Interest

David c. Dunand discloses a financial interest in NanoAl, LLC (a part of Aluminum Dynamics, LLC and Steel Dynamics, Inc.) which is active in the field of aluminum alloys.

## Acknowledgments

The research was sponsored by the U.S. Department of Energy, Vehicle Technologies Office, Powertrain Materials Core Program (PMCP). The authors thank Sarah Grahams, Brian Long, Caitlin Duggan, Dana McClurg, Bryce Abbot, and Kelsey Epps for technical assistance with metallography, heat treatments, and mechanical testing.

## Supplementary Materials

## Supplementary Material

## Appendix A. Rationalization of electrical resistivity performance

Matthiessen’s rule is often utilized to describe the electrical resistivity of aluminum alloys. According to this rule, the electrical resistivity of dilute alloys is the sum of two independent contributions arising from the established temperature and microstructure [5,37,38]. The total electrical resistivity,  $ \rho_{Total} $, combining the contributions of various microstructural features at a given temperature is then given by:

 $$ \rho_{T o t a l}=\rho_{A l}+\rho_{S S}+\rho_{p p t}+\rho_{v a c}+\rho_{d i s l}+\rho_{G B}, $$ 

where,  $ \rho_{Al} $ is the electrical resistivity of a defect-free pure Al (2.7  $ \mu\Omega $.cm at  $ \sim $20  $ ^{\circ} $C [37]), and  $ \rho_{SS} $,  $ \rho_{ppt} $,  $ \rho_{vac} $,  $ \rho_{disl} $, and  $ \rho_{GB} $ are the contributions from the solutes in solid solution, precipitates, vacancies, dislocations, and grain boundaries, respectively.

The resistivity increment due to the Zr solutes in solid solution is given by:

 $$ \rho_{S S}=C_{Z r}^{S S}\Delta\rho_{Z r}^{S S}, $$ 

where,  $ C_{Zr}^{SS} $ is the concentration of Zr in solid solution and  $ \Delta\rho_{Zr}^{SS} $ is the resistivity per unit contribution of Zr in solid solution (1.7  $ \mu\Omega $.cm.wt. % $ ^{-1} $ [57]). Because all Zr in the alloy was trapped in solid solution upon solidification, 0.35 wt. % Zr in the as-fabricated state results in  $ \sim $0.6  $ \mu\Omega $.cm. The APT data of the peak-aged alloy indicates the presence of  $ \sim $0.06 wt. % Zr in solid solution after aging, which translates into  $ \sim $0.1  $ \mu\Omega $.cm.

The increment due to the precipitates can be described by [38,58]:

 $$ \rho_{p p t}(n\Omega m)=\frac{12}{\lambda^{\frac{1}{2}}}, $$ 

which, for the interprecipitate spacing  $ \lambda = 350 $ nm measured for the (Ce,Cu)-rich intermetallics in the as-fabricated state, gives  $ \sim 0.06 $  $ \mu\Omega $.cm, indicating a limited effect of intermetallic particles on electrical resistivity. Aging caused L12-Al3Zr precipitation, with  $ \lambda $ decreasing to  $ \sim 115 $ nm, which produces  $ \rho_{ppt} \sim 0.11\mu\Omega $.cm.

The increment due to grain boundaries is given by [59]:

 $$ \rho_{G B}=S_{G B}\Delta\rho^{G B}, $$ 

where,  $ S_{GB} $ ( $ m^{-1} $) \approx 3/d is the bulk density of grain boundaries for a given grain size  $ d $ and  $ \Delta\rho^{GB} $ is the resistivity per unit concentration of grain boundaries, which is  $ 2.6 \times 10^{-16} \Omega m^2 $ for Al [59]. A  $ d $ value of  $ 1 \mu m $ that is the approximate size of cells on surfaces perpendicular to BD gave the increment of  $ \sim 0.08 \mu\Omega.cm $, pointing to the minor effect of grain size or low-angle grain boundaries on the electrical resistivity. The contribution of vacancies and dislocations can be ignored given their limited effect on electrical resistance [5,37].

## Appendix B. Strengthening mechanisms

The YS of as-fabricated Al-Zr-Ce-Cu alloy is dictated by a combination of grain-boundary, solid-solution, and dispersion strengthening mechanisms through the following general equation:

 $$ \sigma_{Y S}=\Delta\sigma_{0}+\Delta\sigma_{O r}+\Delta\sigma_{S S}+\Delta\sigma_{G B}, $$ 

where  $ \sigma_{YS} $ is the theoretically estimated YS,  $ \Delta\sigma_{0} $ is the Peierls-Nabarro stress (which is equal to 2U MPa for Al),  $ \Delta\sigma_{Or} $ is the Orowan strengthening contribution of Ce-rich particles and,  $ \Delta\sigma_{SS} $ is the solid-solution, and  $ \Delta\sigma_{GB} $ is the grain-boundary strengthening contributions.

The Orowan strengthening contribution of (Ce,Cu)-rich intermetallics can be estimated using [60]:

 $$ \Delta\sigma_{O r}=M\frac{0.4\mu b}{\pi\sqrt{1-\nu}}\frac{\ln\left((2R)/b\right)}{\lambda}, $$ 

where M is the Taylor factor for FCC metals ( $ M < 100 \geq 2.45 $ and  $ M < 110 \geq 3.67 $, and given the near-equal fraction of  $ <100 >_{\text{Al}} // \text{BD and } <101 >_{\text{Al}} // \text{BD textures} $, the averaged M value of 3.06 is used),  $ \mu $ is the shear modulus of  $ \alpha-\text{Al} $ ( $ G = 25 \text{ GPa} $ at room temperature [40]),  $ \nu $ is the Poisson ratio ( $ \nu = 0.245 $ for Al [60]), and b is the magnitude of the Burgers vector in Al ( $ b = 0.286 \text{ nm} [40] $),  $ \lambda $ is the average interparticle spacing, determined from SEM micrographs as 350 nm for Ce-rich intermetallic particles and R is the precipitate radii approximated from the following equation [61]:

 $$ \lambda=\left(\sqrt{\frac{3\pi}{4\mathrm{f}}}-1.64\right)R $$ 

where f is the volume fraction of second phase in the alloy (estimated for (Ce,Cu)-rich intermetallics as f = 0.004 from the thermodynamic Scheil-based calculations using Thermo-Calc software, TCal5 database given the consistency between experimental and simulation observations). The Orowan strengthening contribution from the (Ce,Cu)-rich intermetallic particles is estimated as ~45 MPa.

Solid-solution strengthening contribution of Zr is given by [62]:

 $$ \Delta\sigma_{S S}=H_{A l-Z r}c_{Z r}^{2/3}, $$ 

where $H$ is the solid-solution hardening coefficient determined by the elastic modulus and atomic radius mismatch ($H_{Al-Zr}=9\mathrm{MPa/wt.}\%^{\mathrm{m}}$ at yield point) and $c_{Zr}$ is the content of Zr in the $\alpha$-Al matrix ($c_{Zr}=0.34$ wt.% since all Zr remained in solid solution). Eq. 8 yields 4.4 MPa for as-fabricated alloy.

Grain-size hardening  $ \Delta\sigma_{GS} $ is expressed by Hall-Petch equation [63]:

 $$ \Delta\sigma_{G B}=\frac{k_{y}}{\sqrt{d}}, $$ 

where $d$ is the average grain diameter taken as $100\,\mu\mathrm{m}$ (which is the approximate grain size on the surface perpendicular to the build/loading direction), $k_y$ is the Hall-Petch slope $(0.06\,\mathrm{MPa}\cdot\sqrt{\mathrm{m}}$, Ref. [64]).

For aged alloys, additional strengthening originates from L1₂-Al₃Zr precipitates at the expense of the loss of the solid-solution strengthening effect of Zr. Since L1₂-Al₃Zr precipitates are coarser than the critical diameter of 4 nm above which Orowan looping, and not shearing, dominates [8], Eq. 6 holds for both L1₂-Al₃Zr and (Ce,Cu)-rich precipitates. L1₂-Al₃Zr precipitates are sized 7.5 and 5.1 nm in diameter for the alloy aged at 375 ^\circC/100 h (single-step aging) and 350 ^\circC/5 h + 375 ^\circC/100 h (two-step aging), respectively. It is non-trivial to experimentally quantify the volume fraction of L1₂-Al₃Zr precipitates due to their potentially non-uniform distribution. However, it is reasonable to assume that all Zr in excess of that remaining as-solute in \alpha-Al matrix of aged alloy (which is determined by the APT results) is formed as L1₂-Al₃Zr precipitates. The volume fraction of L1₂-Al₃Zr is then estimated as 0.25 %. The interprecitate spacing for L1₂-Al₃Zr precipitates was determined using Eq. 7 as 115 and 75 nm for single-step and double-step aged alloy conditions, respectively. Eq. 6 then gives \Delta\sigmaₒₜ=102 and 132 MPa for single- and double-step aged alloy, respectively. These values each are over twice the contribution from Orowan strengthening of (Ce,Cu)-rich precipitates. The matrix dislocations surmount Al₃(Sc,Zr) nanoprecipitates and (Ce,Cu)-rich sub-micron precipitates sequentially. Whichever group of precipitates produces greater resistance to dislocation, that group of precipitates dictates the Orowan strengthening contribution [33]. Considering the strengthening contribution of L1₂-Al₃Zr precipitates and ignoring that of (Ce,Cu)-rich intermetallic particles bring about \sigmaₑₜₜₜ values of 126 and 154 MPa for 375 ^\circC/100 h and 350 ^\circC/5 h, 375 ^\circC/100 h aged alloys, respectively, according to Eq. 6.

To estimate YS at 200 ^\circC, G must be adjusted for temperature. Using  $ \mu = 23 $ GPa for Al at 200 ^\circC [40], Eq. 5 gives  $ \sigma_{total} = 72 $ MPa for the as-fabricated alloy, and 117 and 144 MPa after single and double step aging, respectively.

## References

[1] A. Lombardi, G. Byczynski, A. Dmitrienko, M. Dao, V.N. Vukotic, Analysis of aluminum–Cerium based conductor die-casting alloys for high performance electric vehicle powertrain applications, Metall. Mat. Trans. A (2024).

[2] A.Y. Algendy, M. Javidani, S.N. Khangholi, L. Pan, X.-G. Chen, Enhanced mechanical strength and electrical conductivity of Al–Ni-based conductor cast alloys containing Mg and Si, Adv. Eng. Mater. 26 (1) (2024) 2301241.

[3] P. Sivanesh, C. Kuehmann, P. Edwards, E. Filip, Casting Aluminum Alloys for High-Performance Applications, Tesla Inc., US, 2022. USPTO (Ed.).

[4] F. Czerwinski, Aluminum alloys for electrical engineering: a review, J. Mater. Sci. 59 (32) (2024) 14847–14892.

[5] J.P. Hou, R. Li, Q. Wang, H.Y. Yu, Z.J. Zhang, Q.Y. Chen, H. Ma, X.M. Wu, X.W. Li, Z.F. Zhang, Breaking the trade-off relation of strength and electrical conductivity in pure Al wire by controlling texture and grain boundary, J. Alloys. Compd. 769 (2018) 96–109.

[6] J. Rakhmonov, K. Liu, P. Rometsch, N. Parson, X.G. Chen, Effects of Al(MnFe)Si dispersoids with different sizes and number densities on microstructure and ambient/elevated-temperature mechanical properties of extruded Al-Mg-Si AA6082 alloys with varying Mn content, J. Alloys. Compd. (2020) 157937.

[7] K.E. Knipling, D.C. Dunand, D.N. Seidman, Criteria for developing castable, creep-resistant aluminum-based alloys - A review, Int. J. Mater. Res. 97 (3) (2006) 246–265.

[8] C.B. Fuller, D.N. Seidman, D.C. Dunand, Mechanical properties of Al(Sc,Zr) alloys at ambient and elevated temperatures, Acta Mater. 51 (16) (2003) 4803–4814.

[9] K.E. Knipling, D.C. Dunand, D.N. Seidman, Precipitation evolution in Al-Zr and Al-Zr-Ti alloys during isothermal aging at 375-425 degrees C, Acta Mater. 56 (1) (2008) 114–127.

[10] K.E. Knipling, R.A. Karnesky, C.P. Lee, D.C. Dunand, D.N. Seidman, Precipitation evolution in Al–0.1Sc, Al–0.1Zr and Al–0.1Sc–0.1Zr (at.%) alloys during isochronal aging, Acta Mater. 58 (15) (2010) 5184–5195.

[11] N.Q. Vo, D.C. Dunand, D.N. Seidman, Improving aging and creep resistance in a dilute Al–Sc alloy by microalloying with Si, Zr and Er, Acta Mater. 63 (2014) 73–85.

[12] J.U. Rakhmonov, S. Bahl, A. Shyam, D.C. Dunand, Cavitation-resistant intergranular precipitates enhance creep performance of  $ \theta' $-strengthened Al-Cu based alloys, Acta Mater. 228 (2022) 117788.

[13] J.U. Rakhmonov, B. Milligan, S. Bahl, D. Ma, A. Shyam, D.C. Dunand, Progression of creep deformation from grain boundaries to grain interior in Al-Cu-Mn-Zr alloys, Acta Mater. 250 (2023) 118886.

[14] S. Bahl, T. Wu, R. Michi, K. An, D. Yu, L.F. Allard, J.U. Rakhmonov, J. Poplawsky, C. Fancher, D.C. Dunand, A. Plotkowski, A. Shyam, An additively manufactured near-eutectic Al-Ce-Ni-Mn-Zr alloy with high creep resistance, Acta Mater. 268 (2024) 119787.

[15] J.U. Rakhmonov, J. Qi, S. Bahl, D.C. Dunand, A. Shyam, Co-, Ni- and Fe-rich grain-boundary phases enhance creep resistance in  $ \theta' $-strengthened Al-Cu alloys, Mater. Sci. Eng.: A 913 (2024) 147052.

[16] J.U. Rakhmonov, N.Q. Vo, J.R. Croteau, J. Dorn, D.C. Dunand, Laser-melted Al-3.6Mn-2.0Fe-1.8Si-0.9Zr (wt%) alloy with outstanding creep resistance via formation of \alpha-Al(FeMn)Si precipitates, Addit. Manuf. 60 (2022) 103285.

[17] A.R. Farkoosh, D.C. Dunand, D.N. Seidman, Solute-induced strengthening during creep of an aged-hardened Al-Mn-Zr alloy, Acta Mater. 219 (2021) 117268.

[18] O.D. Sherby, A. Goldberg, O.A. Ruano, Solute-diffusion-controlled dislocation creep in pure aluminium containing 0.026 at.% Fe, Philos. Mag. 84 (23) (2004) 2417–2434.

[19] O.D. Sherby, O.A. Ruano, Rate-controlling processes in creep of subgrain containing aluminum materials, Mater. Sci. Eng.: A 410-411 (2005) 8–11.

[20] Z. Li, A.E.W. Jarfors, P. Jansson, Sustainable choices of alloying element for aluminium for thermal conductivity in circular manufacturing, Sustain. Mater. Technol. 40 (2024) e00854.

[21] J.R. Croteau, S. Griffiths, M.D. Rossell, C. Leinenbach, C. Kenel, V. Jansen, D. N. Seidman, D.C. Dunand, N.Q. Vo, Microstructure and mechanical properties of Al-Mg-Zr alloys processed by selective laser melting, Acta Mater. 153 (2018) 35–44.

[22] S. Bahl, T. Wu, R.A. Michi, K. An, D. Yu, L.F. Allard, J.U. Rakhmonov, J. D. Poplawsky, C.M. Fancher, D.C. Dunand, A. Plotkowski, A. Shyam, An additively manufactured near-eutectic Al-Ce-Ni-Mn-Zr alloy with high creep resistance, Acta Mater. 268 (2024) 119787.

[23] C. Pauzon, M. Buttard, A. Després, B. Chehab, J.-J. Blandin, G. Martin, A novel laser powder bed fusion Al-Fe-Zr alloy for superior strength-conductivity trade-off, Scripta Mater. 219 (2022) 114878.

[24] L. Pengfei, W. Zhigang, W. Yunli, G. Xizhu, W. Zaiyun, L. Zhiqiang, Effect of cerium on mechanical performance and electrical conductivity of aluminum rod for electrical purpose, J. Rare Earths 24 (1) (2006) 355–357. Supplement 1.

[25] Z.C. Sims, H.B. Henderson, M.J. Thompson, R.P. Chaudhary, J.A. Hammons, J. Ilavsky, D. Weiss, K. Anderson, R. Ott, O. Rios, Application of Ce for scavenging Cu impurities in A356 Al alloys, Eur. J. Mater. 1 (1) (2022) 3–18.

[26] M.K. Miller, K.F. Russell, G.B. Thompson, Strategies for fabricating atom probe specimens with a dual beam FIB, Ultramicroscopy 102 (4) (2005) 287–298.

[27] I. Amedeo, N. Kirby, P.M. Santiago, F. De Geuser, M. Perez, S. Cazottes, T. Dorin, Anomalous SAXS and APT investigation of core–shell precipitation in Al–Mg–Sc–Zr alloys, Acta Mater. 301 (2025) 121593.

[28] D.D.A. Porter, K.E. Easterling, M. Sherif, Phase Transformations in Metals and Alloys, Taylor & Francis, London, 2008.

[29] D. Hull, D.J. Bacon, Chapter 9 - dislocation arrays and crystal boundaries, in: D. Hull, D.J. Bacon (Eds.), Introduction to Dislocations, 5th Edition, Butterworth-Heinemann, Oxford, 2011, pp. 171–204.

[30] E.U. Lee, H.H. Kranzlein, E.E. Underwood, Dynamic recovery in aluminum, Mater. Sci. Eng. 7 (6) (1971) 348–356.

[31] S. Griffiths, J.R. Croteau, M.D. Rossell, R. Erni, A. De Luca, N.Q. Vo, D.C. Dunand, C. Leinenbach, Coarsening- and creep resistance of precipitation-strengthened Al–Mg–Zr alloys processed by selective laser melting, Acta Mater. 188 (2020) 192–202.

[32] K.E. Knipling, D.C. Dunand, Creep resistance of cast and aged Al–0.1Zr and Al–0.1Zr–0.1Ti (at.%) alloys at 300–400 ^\circC, Scripta Mater. 59 (4) (2008) 387–39

[33] J.U. Rakhmonov, D. Weiss, D.C. Dunand, Comparing evolution of precipitates and strength upon aging of cast and laser-remelted Al–8Ce-0.2Sc-0.1Zr (wt.%), Mater. Sci. Eng.: A 840 (2022) 142990.

[34] C.N. Ekaputra, J.U. Rakhmonov, E. Senvardarli, D. Weiss, J.-E. Mogonye, D. C. Dunand, Combining solution-, precipitation- and load-transfer strengthening in a cast Al-Ce-Mn-Sc-Zr alloy, Acta Mater. 266 (2024) 119683.

[35] Weld Metal Solidification II: microstructure within grains, Weld. Metall. (2002) 199–215.

[36] C. Pauzon, M. Buttard, A. Després, F. Charlot, M. Fivel, B. Chehab, J.-J. Blandin, G. Martin, Direct ageing of LPBF Al-1Fe-1Zr for high conductivity and mechanical performance, Acta Mater. 258 (2023) 119199.

[37] F.R. Fickett, Aluminum—1. A review of resistive mechanisms in aluminum, Cryogenics 11 (5) (1971) 349–367.

[38] A. Mohammadi, N.A. Enikeev, M.Y. Murashkin, M. Arita, K. Edalati, Developing age-hardenable Al-Zr alloy by ultra-severe plastic deformation: significance of supersaturation, segregation and precipitation on hardening and electrical conductivity, Acta Mater. 203 (2021) 116503.

[39] K.F. Lunn, D. Apelian, Thermal and electrical conductivity of aluminum alloys: fundamentals, structure-property relationships, and pathways to enhance conductivity, Mater. Sci. Eng.: A 924 (2025) 147766.

[40] H.J. Frost, M.F. Ashby, Deformation-mechanism Maps : the Plasticity and Creep of Metals and Ceramics, Pergamon Press, New York, 1982.

[41] M.E. Krug, D.C. Dunand, Modeling the creep threshold stress due to climb of a dislocation in the stress field of a misfitting precipitate, Acta Mater. 59 (13) (2011) 5125–5134.

[42] D. Hull, D.J. Bacon, Chapter 3 - movement of dislocations, in: D. Hull, D.J. Bacon (Eds.), Introduction to Dislocations, 5th Edition, Butterworth-Heinemann, Oxford, 2011, pp. 43–62.

[43] A. De Luca, D.N. Seidman, D.C. Dunand, Effects of Mo and Mn microadditions on strengthening and over-aging resistance of nanoprecipitation-strengthened Al-Zr-Sc-Er-Si alloys, Acta Mater. 165 (2019) 1–14.

[44] M. McLean, On the threshold stress for dislocation creep in particle strengthened alloys, Acta Metall. 33 (4) (1985) 545–556.

[45] J. Rösler, Back-stress calculation for dislocation climb past non-interacting particles, Mater. Sci. Eng.: A 339 (1) (2003) 334–339.

[46] M.E. Kassner, Fundamentals of Creep in Metals and Alloys, 3rd Edition, Butterworth-Heinemann, Boston, 2015.

[47] S. Ueda, T. Kameyama, T. Matsunaga, K. Kitazono, E. Sato, Re-examination of creep behaviour of high purity aluminium at low temperature, J. Phys.: Conf. Ser. 240 (1) (2010) 012073.

[48] M.E. Kassner, M.T. Pérez-Prado, Five-power-law creep in single phase metals and alloys, Prog. Mater. Sci. 45 (1) (2000) 1–102.

[49] Y. Osetskiy, A. Plotkowski, Y. Yang, Diffusion, atomic transport, and ordering in Al-Zr alloys: FCC and liquid phases, Acta Mater. 260 (2023) 119306.

[50] S. Takeuchi, A.S. Argon, Glide and climb resistance to the motion of an edge dislocation due to dragging a Cottrell atmosphere, Philos. Mag. A 40 (1) (1979) 65–75.

[51] J. Peng, S. Bahl, A. Shyam, J.A. Haynes, D. Shin, Solute-vacancy clustering in aluminum, Acta Mater. 196 (2020) 747–758.

[52] J. Meier, D. Shin, J.D. Poplawsky, L.F. Allard, H. Cheng, I. Ohnishi, S. Bahl, J. A. Haynes, N.Q. Vo, A. Shyam, Effect of Sn microalloying on the nucleation of L12 Al3Zr precipitates in a dilute aluminum-zirconium alloy, J. Alloys. Compd. 1027 (2025) 180433.

[53] C. Wolverton, Solute-vacancy binding in aluminum, Acta Mater. 55 (17) (2007) 5867–5872.

[54] S. Özbilen, H.M. Flower, Zirconium-vacancy binding and its influence on S' precipitation in an Al-Cu-Mg alloy, Acta Metall. 37 (11) (1989) 2993–3000.

[55] S. Vannarat, M.H.F. Sluiter, Y. Kawazoe, First-principles study of solute-dislocation interaction in aluminum-rich alloys, Phys. Rev. B 64 (22) (2001) 224203.

[56] J. Rakhmonov, G. Timelli, F. Bonollo, Characterization of the solidification path and microstructure of secondary Al-7Si-3Cu-0.3Mg alloy with Zr, V and Ni additions, Mater. Charact. 128 (2017) 100–108.

[58] B. Raeisinia, W.J. Poole, D.J. Lloyd, Examination of precipitation in the aluminum alloy AA6111 using electrical resistivity measurements, Mater. Sci. Eng.: A 420 (1) (2006) 245–249.

[59] A.S. Karolik, A.A. Luhvich, Calculation of electrical resistivity produced by dislocations and grain boundaries in metals, J. Phys.: Condens.. Matter. 6 (4) (1994) 873.

[60] J.F. Nie, B.C. Muddle, Strengthening of an Al–Cu–Sn alloy by deformation-resistant precipitate plates, Acta Mater. 56 (14) (2008) 3490–3501.

[61] E.A. Marquis, D.N. Seidman, D.C. Dunand, Precipitation strengthening at ambient and elevated temperatures of heat-treatable Al(Sc) alloys [Acta Materialia 50(16), pp. 4021–4035], Acta Mater. 51 (1) (2003) 285–287.

[62] F.R.N. Nabarro, Theory of Crystal Dislocations, Clarendon Press, Oxford, 1967.

[63] K. Ma, H. Wen, T. Hu, T.D. Topping, D. Isheim, D.N. Schoenung, Mechanical behavior and strengthening mechanisms in ultrafine grain precipitation-strengthened aluminum alloy, Acta Mater. 62 (2014) 141–155.

[64] S. Thangaraju, M. Heilmaier, B.S. Murty, S.S. Vadlamani, On the estimation of true Hall–Petch constants and their role on the superposition law exponent in Al alloys, Adv. Eng. Mater. 14 (10) (2012) 892–897.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

Acta Materialia 304 (2026) 121785

## Keywords

Al alloys
Additive manufacturing
Microstructure
Conductivity
Creep
Strength

## ABSTRACT

https://doi.org/10.1016/j.actamat.2025.121785

1359-6454/© 2025 Published by Elsevier Inc. on behalf of Acta Materialia Inc.

Creep tests were carried out on the as-fabricated and peak-aged specimens at 200 ^\circC in tension and compression to evaluate the creep response of the alloy. While tensile creep provides details related to all three creep stages, i.e., primary, secondary, and tertiary stages, compressive creep allows for the measurements of primary and secondary creep responses over a wide range of stresses.

X-ray diffraction (XRD) measurements were performed using a Bruker AXS 2nd gen. D2 Phaser. To maximize detection of minor phase peaks, measurements were carried out over a diffraction angle range of 18–55^\circ with a 2\theta step size of  $ \sim $0.002^\circ and exposure time of 2.25s/step. The CuK\alpha x-ray beam was generated at 30 kV/10 mA with a wavelength of  $ \lambda=1.5418 $ Å. Patterns were analyzed using Highscore Plus software.

The isochronal aging study (Fig. S_{3}) of the Al-Zr-Ce-Cu alloy indicates that a slight hardness increase ( $ \sim $10 HV) occurs at 350 ^\circC, with near-peak aging condition achieved at 375 ^\circC. An isothermal aging study was, therefore, performed at 375 ^\circC, as summarized in Fig. 4. Alloy hardness in as-fabricated state is  $ \sim $40 HV. Aging for 30 h produces near peak hardness of  $ \sim $62 HV, which then remains unchanged with

Two-step aging (350 ^\circC for 5 h + 375 ^\circC/100 h) was applied to provide a higher driving force for the nucleation of L12-precipitates. As noted from the APT data from the specimen after initial 350 ^\circC/5 h aging, more numerous L12-precipitates sized ~2.6 nm in diameter were observed, with Si distributed in their interiors (Fig. 5d). The subsequent

aging at 375 ^\circC/100 h produced finer (~5.1 nm in diameter) and more numerous L12-precipitates compared with single-step aging (Fig. 5e vs. Fig. 5b,c).

Given the unexpected YS values obtained for aged samples at 200 ^\circC, further tensile tests were conducted at various strain rates to determine strain-rate sensitivity m, defined as:

changes in the matrix interiors. Fig. S_{7} shows one of the several analyzed APT tips, revealing fine Sn precipitates and no Zr-rich precipitates. All Zr remained fully in solid solution, as the temperature is too low for its precipitation during creep (Table 6).

where A is a dimensionless material constant,  $ n_{a} $ is the apparent stress exponent. As shown in Fig. 11a, pure Al displays  $ n_{a} = 5 $ at 200 ^\circC (as well as at 300 ^\circC, Fig. 11b), which is indicative of dislocation climb

where,  $ A' $ is a dimensionless material constant, n is the  $ \alpha $-Al matrix stress exponent (with n = 4.4 for pure Al [40]). By plotting  $ \dot{\varepsilon}_{m}^{1/n} $ vs.  $ \sigma $ (with n = 4.4 for pure Al [40]), as displayed in Fig. S_{8}, the threshold stress is determined as  $ \sigma_{th}=50 $ MPa, implying that dislocation creep at lower stresses is practically immeasurable. The question arises as to which group of precipitates – the (Ce,Cu)-rich particles, the L12-Al3Zr

A new Al-0.3Zr-0.2Ce-0.2Cu (wt. %) alloy was additively manufactured via laser powder-bed fusion. The microstructure, electrical conductivity, and mechanical properties (tensile properties at 20 and 200 ^\circC, and creep resistance at 200 ^\circC) in as-fabricated and aged states were measured to establish microstructure-property relationships. The following conclusions were drawn from this study.

• Two-step aging (350 ^\circC/5 h + 375 ^\circC/100 h) produces L12-Al3Zr nanoprecipitates which are finer and more numerous as compared to

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

ELSEVIER

Contents lists available at ScienceDirect

journal homepage: www.elsevier.com/locate/actamat

Keywords:
Al alloys
Additive manufacturing
Microstructure
Conductivity
Creep
Strength

A B S T R A C T

* Corresponding author.

E-mail address: rakhmonovj@ornl.gov (J. Rakhmonov).

https://doi.org/10.1016/j.actamat.2025.121785

Received 4 August 2025; Received in revised form 19 November 2025; Accepted 30 November 2025

Available online 3 December 2025

1359-6454/© 2025 Published by Elsevier Inc. on behalf of Acta Materialia Inc.

J. Rakhmonov et al.

Creep tests were carried out on the as-fabricated and peak-aged specimens at 200 °C in tension and compression to evaluate the creep response of the alloy. While tensile creep provides details related to all three creep stages, i.e., primary, secondary, and tertiary stages, compressive creep allows for the measurements of primary and secondary creep responses over a wide range of stresses.

X-ray diffraction (XRD) measurements were performed using a Bruker AXS 2nd gen. D2 Phaser. To maximize detection of minor phase peaks, measurements were carried out over a diffraction angle range of 18–55° with a 2θ step size of  $ \sim $0.002° and exposure time of 2.25s/step. The CuKα x-ray beam was generated at 30 kV/10 mA with a wavelength of  $ \lambda=1.5418 $ Å. Patterns were analyzed using Highscore Plus software.

The isochronal aging study (Fig. S3) of the Al-Zr-Ce-Cu alloy indicates that a slight hardness increase ( $ \sim $10 HV) occurs at 350 °C, with near-peak aging condition achieved at 375 °C. An isothermal aging study was, therefore, performed at 375 °C, as summarized in Fig. 4. Alloy hardness in as-fabricated state is  $ \sim $40 HV. Aging for 30 h produces near peak hardness of  $ \sim $62 HV, which then remains unchanged with

Two-step aging (350 °C for 5 h + 375 °C/100 h) was applied to provide a higher driving force for the nucleation of L12-precipitates. As noted from the APT data from the specimen after initial 350 °C/5 h aging, more numerous L12-precipitates sized ~2.6 nm in diameter were observed, with Si distributed in their interiors (Fig. 5d). The subsequent

aging at 375 °C/100 h produced finer (~5.1 nm in diameter) and more numerous L12-precipitates compared with single-step aging (Fig. 5e vs. Fig. 5b,c).

Given the unexpected YS values obtained for aged samples at 200 °C, further tensile tests were conducted at various strain rates to determine strain-rate sensitivity m, defined as:

changes in the matrix interiors. Fig. S7 shows one of the several analyzed APT tips, revealing fine Sn precipitates and no Zr-rich precipitates. All Zr remained fully in solid solution, as the temperature is too low for its precipitation during creep (Table 6).

where A is a dimensionless material constant,  $ n_{a} $ is the apparent stress exponent. As shown in Fig. 11a, pure Al displays  $ n_{a} = 5 $ at 200 °C (as well as at 300 °C, Fig. 11b), which is indicative of dislocation climb

where,  $ A' $ is a dimensionless material constant, n is the  $ \alpha $-Al matrix stress exponent (with n = 4.4 for pure Al [40]). By plotting  $ \dot{\varepsilon}_{m}^{1/n} $ vs.  $ \sigma $ (with n = 4.4 for pure Al [40]), as displayed in Fig. S8, the threshold stress is determined as  $ \sigma_{th}=50 $ MPa, implying that dislocation creep at lower stresses is practically immeasurable. The question arises as to which group of precipitates – the (Ce,Cu)-rich particles, the L12-Al3Zr

A new Al-0.3Zr-0.2Ce-0.2Cu (wt. %) alloy was additively manufactured via laser powder-bed fusion. The microstructure, electrical conductivity, and mechanical properties (tensile properties at 20 and 200 °C, and creep resistance at 200 °C) in as-fabricated and aged states were measured to establish microstructure-property relationships. The following conclusions were drawn from this study.

• Two-step aging (350 °C/5 h + 375 °C/100 h) produces L12-Al3Zr nanoprecipitates which are finer and more numerous as compared to