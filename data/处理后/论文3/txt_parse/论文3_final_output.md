DOI: 10.1016/j.addma.2024.104149

# The impact of surface orientation on surface roughness and fatigue life of laser-based powder bed fusion Ti-6Al-4V

Jason Rogers $ ^{a} $, Joe Elambasseril $ ^{a} $, Chris Wallbrink $ ^{b} $, Beau Krieg $ ^{b} $, Ma Qian $ ^{a} $, Milan Brandt $ ^{a} $, Martin Leary $ ^{a,*} $

 $ ^{a} $ RMIT Centre for Additive Manufacturing, School of Engineering, RMIT University, Carlton, VIC, 3053, Australia

 $ ^{b} $ Platforms Division, Defence Science and Technology Group, 3207, VIC, Australia

## ARTICLE INFO

## Keywords

Microstructure

Additive manufacturing

Titanium

Hot isostatic pressing

Inclined

Equivalent defect area

## Abstract

As-manufactured surface roughness is detrimental to the fatigue life of laser-based powder bed fusion (LB-PBF) Ti-6Al-4V components. Despite the criticality of surface roughness to the fatigue failure mode, the relevant test data is incomplete, for example with regard to the distinct effects of upward and downward-facing surfaces. This research characterises the relationship between the manufactured inclination angle, surface roughness and associated fatigue performance of LB-PBF Ti-6Al-4V. Unique to this research is the quantified difference in fatigue performance due to either or upward or downward-facing surface roughness; an outcome made possible by isolating the as-manufactured surface roughness of upward and downward-facing surfaces of inclined specimens prior to fatigue testing. Experimental results confirm the criticality of downward-facing surface roughness, and for the first time characterises the impact of surface orientation (upward and downward) on observed fatigue life. In addition to providing robust design data for LB-PBF Ti-6Al-4V, the underlying test method developed can be applied in future research to characterise the effect of orientation on fatigue.

## 1. Introduction

The inherent surface roughness of laser-based powder bed fusion (LB-PBF) is detrimental to fatigue strength [1–6]; with as-manufactured LB-PBF surfaces providing inferior fatigue performance to traditionally manufactured components with machined or processed surfaces [7]. The reduction in fatigue life is attributed to stress concentrations caused by surface notches, leading to local plastic deformations [8], facilitating early fatigue crack initiation [9]. The criticality of surface notches is related to both their depth and sharpness [10].

The surface roughness of LB-PBF components comprises of both primary and secondary roughness [11]. Primary roughness is generated via melt pool solidification and develops notch-like geometries, its formation being dependent on process parameters, including layer thickness and laser-powder interaction [12,13]. This primary roughness creates stress concentrations and facilitates crack initiation under fatigue loading [5,14]. Secondary roughness includes adhered powder particles [15]; and is less critical to fatigue response than primary roughness [14,16,17]. The as-manufactured surface roughness of LB-PBF specimens is influenced by: powder size distribution (PSD) of the material feedstock [3,18]; the manufactured angle of the component relative to the build plate [19,20]; and, associated laser manufacturing parameters and trajectory [15]. Build orientation is a determining factor to the criticality of surface roughness as downward-facing or over-hanging surfaces exhibit higher primary surface roughness than upward-facing surfaces due to gravitational effects on the solidifying melt pool [21] and intimate contact between powder bed and melt pool region [22]. Consequently, downward-facing surfaces are more likely to initiate failure during fatigue loading [19]. To aid heat transfer and reduce part distortion, downward-facing surfaces may require support structures at acute inclination angles [23], often defined as those being less than 45^\circ [24]. The use of support material increases the scope for robust manufacture, however, surfaces in contact with support material will exhibit substantial geometric defects associated with support structure interaction [21]. Even if surface processing is applied to these surfaces, there is evidence that insufficient machining depth will not yield significant fatigue life benefits due to deep surface notches being exposed to the surface [6,7]. Internal defects are shown to be far less influential to the fatigue strength of LB-PBF materials [25,26].

As surface roughness degrades the fatigue life of PBF components,

Fatigue test conditions of laser-based (LB) and electron-beam (EB) PBF Ti-6Al-4V with fatigue test method defined as: rotating beam bending (RBB), four-point bending (4PB) and three-point bending (3PB). Surface identified as: as-built (AB), sandblasted (SB), machined (M), tribofinished (TB), polished (P), electro-discharge machining (EDM), shot peened (SP), laser peened (LP), etched (E), vibratory ground surface (VG). Heat treatment defined as: stress relieved (SR), Hot Isostatic Pressing (HIP), CASE (C). Stress ratio (R) and data not reported (-).

| Ref. | PBF method | Specimen type | Fatigue test method | Build angle | Surface | HT | R | Frequency (Hz) | Runout limit (cycles) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [7] | LB | Cylindrical | Axial | 90^\circ | AB, SB, M, VG | SR, HIP | 0.1 | 110 | 3.00E+07 |
| [6] | LB, EB | Cylindrical | RBB | 0^\circ, 90^\circ | AB, TB | AB, SR, HIP | -1 | 85-96 | 1.00E+07 |
| [32] | LB, EB | Cylindrical | Axial | 0^\circ, 90^\circ | M | AB, HIP | 0.1 | 30 | 1.00E+07 |
| [33] | EB | Cylindrical | Axial | 0^\circ, 45^\circ, 90^\circ | AB | AB | 0.1 | 10 | 1.00E+07 |
| [25] | LB | Cylindrical | Axial | 90^\circ | SB | SR | 0.1 | 50 | 1.00E+07 |
| [34] | LB | Cylindrical | Axial | 90^\circ | AB, TB, P, SP | SR, HIP | -1 | 150 | 5.00E+07 |
| [11] | LB, EB | Flat | Axial | 0^\circ | AB | SR | 0.1 | 150 | 1.00E+07 |
| [35] | LB | Cylindrical | Axial | 0^\circ, 90^\circ | M | SR | -1 | 20 | 1.00E+07 |
| [36] | LB | Prismatic | 4PB | 90^\circ | SB, SP, LP | SR, C | 0.1 | 8 | 5.00E+06 |
| [26] | LB, EB | Cylindrical | Axial | 90^\circ | M, P | SR, HIP | -1 | 10, 19E3 | 2E6, 3E9 |
| [37] | EB | Cylindrical | Axial | 90^\circ | AB, E, M | AB, HIP | 0.1 | 10 | 1.00E+06 |
| [10] | LB | Cylindrical | Axial | 90^\circ | AB, E, M | AB, HIP | 0.1 | 10 | 1.00E+06 |
| [38] | LB | Flat + Arch | Plane bending | 0^\circ, 90^\circ | AB | SR | 0 | 20 | 2.00E+06 |
| [39] | LB | Arch | Plane bending | 0^\circ, 90^\circ | AB | SR | 0 | 15 | 2.00E+06 |
| [40] | LB | Flat | Axial | 0^\circ, 90^\circ | AB, M | AB | -0.2 | 20 | 1.00E+06 |
| [41] | LB | Cylindrical | Axial | 90^\circ | AB | HIP | -1 | 82 | 1.00E+07 |
| [42] | LB | Flat | Axial | 0^\circ, 90^\circ | P | AB | 0.2 | 10 | - |
| [43] | LB | Cylindrical | Axial | 90^\circ | AB, SP, P | SR, HIP | 0.1 | 150 | 5.00E+07 |
| [44] | LB | Cylindrical | RBB | 0^\circ, 90^\circ | AB, M, P | AB | -1 | 20-25 | 1.00E+07 |
| [45] | LB, EB | Cylindrical | Axial | 90^\circ | SB, P | HIP | 0.1 | 20 | 5.00E+06 |
| [46] | LB, EB | Flat | Axial | 0^\circ | AB, M | SR, HIP | 0.1 | - | 1.00E+07 |
| [47] | LB | Cylindrical | Axial | 90^\circ | P | HIP | 0.1, -1 | 50, 2E4 | 1.00E+07 |
| [3] | LB, EB | Cylindrical | RBB | 90^\circ | AB, P, | AB, SR, HIP | -1 | 60 | 1.00E+07 |
| [48] | LB | Prismatic | 4PB | 90^\circ | AB, SB, SP, LP | AB, SR, HIP, C | 0.1 | 8 | 5.00E+06 |
| [49] | LB | Cylindrical | Axial | 45^\circ, 90^\circ | AB | AB | 0.1 | 50 | 1.00E+07 |
| [50] | LB, EB | Prismatic | 3PB | 0^\circ | AB, EDM | AB | 0.1 | 10 | - |
| [51] | LB | Cylindrical | Axial strain | 90^\circ | AB, M | SR | -1 | Variable | 2.00E+07 |
| [52] | LB | Cylindrical | Axial strain | 90^\circ | M | AB, SR | -1 | Variable | 4.00E+06 |
| [53] | LB | Cylindrical | Axial | 0^\circ, 90^\circ | M | AB | 0.1 | 10 | - |
| [54] | LB | Flat | Axial | 90^\circ | SB | SR | 0 | 10 | 1.00E+06 |
| [55] | LB | Flat | Axial | 90^\circ | SB | SR | 0 | 10 | 1.00E+06 |
| [56] | LB | Lattice | Axial | 45^\circ | AB, SB | SR, HIP | -1 | 120 | - |

existing roughness metrics and fracture mechanics approaches have been used to connect roughness with fatigue life. Vaysette et al. suggest total roughness profile height,  $ R_{t} $, as an indicator for notch-like defects which are critical to fatigue performance [27]. Gockel et al. demonstrate that areal arithmetic mean roughness of as-manufactured specimens,  $ S_{a} $, does not correlate with fatigue life, however areal valley roughness,  $ S_{v} $, shows an inverse trend with fatigue life [28]. Other studies are in agreeance, stating that profile arithmetic mean roughness,  $ R_{a} $, did not correlate with the observed fatigue life of PBF Ti-6Al-4V [2,5,29]. Where Ednie et al. observe the highest correlation between profile peak roughness,  $ R_{p} $, and fatigue life [29]. Du Plessis et al. used stress intensity factor to predict fatigue failure initiation sites in order to prove the relevance of fracture mechanics approaches and successfully predicted surface defect failure sites for 64 % of examined cases [5].

Despite an extensive literature search, none of the available PBF Ti-6Al-4V data quantifies the distinct effect of upward and downward-facing surface roughness on fatigue life. A portion (32 papers) of the explored literature has been presented in Table 1 containing recent (2012 onwards) research that have published fatigue data of PBF Ti-6Al-4V. It was found that cylindrical hourglass specimens are typically used for uniaxial testing (Table 1), where cylindrical specimens do not exhibit flat surfaces and are therefore not directly compatible with the acquisition of specifically upward and downward roughness effects. Furthermore, available fatigue data includes only limited build orientations. Only 0^\circ (horizontal), 45^\circ and 90^\circ (vertical) build orientations are available in the summarised data (Table 1). More than 60 % of this data includes as-built surfaces, highlighting the importance of surface roughness. However, most of this data (>90 %) includes vertical build orientation, with <10 % of these papers including 45^\circ build orientation, and none of the existing data includes characterisation of the distinct effect of upward and downward-facing surfaces.

For reference, more than 60 % of published PBF Ti-6Al-4V fatigue papers presented (Table 1) include experimental data for HIP, and stress relieving heat treatments are also commonly adopted for PBF Ti-6Al-4V specimens, being included in 47 % and 59 % of papers respectively, highlighting the detrimental effects of internal defects and residual stresses. The fatigue life enhancement of HIP, particularly for machined and/or polished specimens, was highlighted in a recent study where it is also indicated that fatigue datasets are commonly missing essential supporting documentation, restricting their utility for further applications [30]; an extension of earlier research which reaches a similar conclusion [31].

Due to the increased severity of primary surface roughness for downward-facing surfaces compared to upward-facing surfaces, primary roughness dominates the effects of roughness on fatigue life [9]. Therefore, in standard specimens with as-manufactured surfaces, the distinct impact of upward-facing surface roughness cannot be directly quantified as it is less critical than the associated downward-facing surfaces. This research proposes a unique test procedure to overcome this limitation: flat fatigue specimens are manufactured to capture the fatigue life reduction resulting from surface roughness associated with varying build orientations. For these specimens, the downward and upward-facing surfaces are alternately polished to remove their effect from the observed fatigue life. This test procedure thereby allows the distinct effect of upward and downward-facing surface roughness to be characterised. To the authors’ knowledge, this method has not appeared in the literature and provides a unique dataset for the design optimisation of full-scale, fatigue resistant components which exhibit distinct loaded surfaces with multiple orientations, both upward and downward-facing.
Fig. 1. Technical drawings for (a) fatigue specimens manufactured according to ASTM E466 and (b) tensile specimens manufactured according to ASTM E8. All units in mm.

Design of experiments for fatigue testing.

<table border="1" style="margin: auto; word-wrap: break-word;"><tr><td style="text-align: center; word-wrap: break-word;">Inclination angle</td><td style="text-align: center; word-wrap: break-word;">Polished face</td><td style="text-align: center; word-wrap: break-word;">Applied force (kN)</td><td style="text-align: center; word-wrap: break-word;">Repetitions</td><td style="text-align: center; word-wrap: break-word;">Tests per condition</td></tr><tr><td rowspan="2">0^\circ</td><td style="text-align: center; word-wrap: break-word;">Upward-facing</td><td style="text-align: center; word-wrap: break-word;">5.4, 6.2, 7.7, 9.3</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">8</td></tr><tr><td style="text-align: center; word-wrap: break-word;">Downward-facing</td><td style="text-align: center; word-wrap: break-word;">5.4, 6.2, 7.7, 9.3</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">8</td></tr><tr><td rowspan="2">10^\circ</td><td style="text-align: center; word-wrap: break-word;">Upward-facing</td><td style="text-align: center; word-wrap: break-word;">5.4, 6.2, 7.7, 9.3</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">8</td></tr><tr><td style="text-align: center; word-wrap: break-word;">Downward-facing</td><td style="text-align: center; word-wrap: break-word;">5.4, 6.2, 7.7, 9.3</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">8</td></tr><tr><td rowspan="2">30^\circ</td><td style="text-align: center; word-wrap: break-word;">Upward-facing</td><td style="text-align: center; word-wrap: break-word;">5.4, 6.2, 7.7, 9.3</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">8</td></tr><tr><td style="text-align: center; word-wrap: break-word;">Downward-facing</td><td style="text-align: center; word-wrap: break-word;">5.4, 6.2, 7.7, 9.3</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">8</td></tr><tr><td rowspan="2">50^\circ</td><td style="text-align: center; word-wrap: break-word;">Upward-facing</td><td style="text-align: center; word-wrap: break-word;">5.4, 6.2, 7.7, 9.3</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">8</td></tr><tr><td style="text-align: center; word-wrap: break-word;">Downward-facing</td><td style="text-align: center; word-wrap: break-word;">5.4, 6.2, 7.7, 9.3</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">8</td></tr><tr><td rowspan="2">70^\circ</td><td style="text-align: center; word-wrap: break-word;">Upward-facing</td><td style="text-align: center; word-wrap: break-word;">5.4, 6.2, 7.7, 9.3</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">8</td></tr><tr><td style="text-align: center; word-wrap: break-word;">Downward-facing</td><td style="text-align: center; word-wrap: break-word;">5.4, 6.2, 7.7, 9.3</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">8</td></tr><tr><td rowspan="2">90^\circ</td><td style="text-align: center; word-wrap: break-word;">Side-facing</td><td style="text-align: center; word-wrap: break-word;">5.4, 6.2, 7.7, 9.3</td><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">16</td></tr><tr><td style="text-align: center; word-wrap: break-word;"></td><td style="text-align: center; word-wrap: break-word;"></td><td style="text-align: center; word-wrap: break-word;">Total</td><td style="text-align: center; word-wrap: break-word;">96</td></tr></table>

## 2. Method

To overcome the identified knowledge gap regarding the isolated influence of upward and downward-facing surface roughness on fatigue performance of LB-PBF Ti-6Al-4V, a formal experimental research program was developed.

## 2.1. Manufacturing

Fatigue and tensile specimens were produced using LB-PBF (SLM Solutions 250) with Ti-6Al-4V powder. Before using virgin Ti-6Al-4V powder, two drying runs were completed to remove any moisture present. After drying, the powder is sieved (-100\mum) resulting in a Dv90 powder size distribution of 65.8 \mum and Dv50 of 44.5 \mum. Applied process parameters are: 30 \mum layer height, 100 W laser power, 425 mm/s scan speed on borders and 375 mm/s scan speed on hatching. Fatigue specimens dimensions (Fig. 1a) conform to subsize specimens in ASTM E466 [57] and tensile specimens (Fig. 1b) conform to subsize specimens specified in ASTM E8 [58]. Fatigue specimens were manufactured at six inclination angles from 90^\circ (vertical) down to 0^\circ (horizontal) as detailed in Table 2. Specimens manufactured at or above 40^\circ did not require supports in the gauge section, only on the lower grip section (Fig. 2a). Specimens manufactured below 40^\circ required supports for the gauge section (Fig. 2b). The support method adopted a thin-wall, edge support in contact with the perimeter of the gauge section and column supports separated by 100 \mum from the downward-facing surface of the specimen gauge section to avoid mutual contact thus, no machining was required and an as-manufactured surface was achieved. HIP was applied to all fatigue specimens and half of the tensile specimens. HIP conditions were 820 ^\circC, 200 MPa and 2 h hold time in a pure argon atmosphere. All specimens were ultrasonically cleaned using de-ionised water prior to HIP to remove loose powder.

According to the replication guidelines stated in ASTM-E739 [59], the experimental fatigue testing in this research has sufficient samples per test condition (Table 2) to be classified as “Research and development testing of components and specimens” (50 % replication). If the additional control factor of upward and downward facing specimens is ignored, the experimental test program would have sufficient samples per condition to be classified as “Design allowables data” according to ASTM-E739 (75 % replication), thus representing a comprehensive test program.

## 2.2. Microstructure

Fatigue specimens manufactured at 0^\circ, 30^\circ and 90^\circ were cut parallel to the loading axis for microstructure evaluation before and after HIP to understand the microstructural changes relative to inclination angle and HIP. Samples were mechanically and chemically polished to yield a mirror finish and reveal the microstructure for backscatter electron (BSE) and electron backscatter diffraction (EBSD) analysis (JEOL-7200 F scanning electron microscope).

## 2.3. Surface roughness

Surface roughness of Ti-6Al-4V fatigue specimens was characterised using focus variation microscopy (Alicona Infinite Focus microscope) with a vertical resolution of 0.5  $ \mu $m, lateral resolution of 3.5  $ \mu $m and a sample length of 2 mm. Roughness results were assessed (N=3) for the upward and downward-facing surfaces to provide mean and standard deviation of selected roughness measures ( $ R_{a}, R_{p}, R_{v}, R_{t}, R_{q}, R_{sm} $) for each inclination angle.

## 2.4. Mechanical testing

Uniaxial tensile testing (Instron, 50 kN load cell) was conducted on 0^\circ and 10^\circ specimens under displacement control with a crosshead velocity of 1 mm/min and a strain rate of  $ 5.2 \times 10^{-4} \, s^{-1} $. Both HIP and non-HIP specimens were tested with as-manufactured surfaces. Fully tensile, uniaxial fatigue testing was conducted according to the proposed design of experiments (Table 2), with a stress ratio (R) of 0.1 and test frequency (f) of 20 Hz (hydraulic MTS universal testing machine, 100 kN load cell). End of test was triggered by either complete specimen fracture or runout at  $ 1.5 \times 10^{6} $ cycles. All specimens were tested with as-manufactured surface conditions however, either the upward or downward-facing surface was polished to remove all visible surface defects. Specimens were polished parallel to the loading direction to avoid lateral scratching according to a defined polishing process (Table 3) resulting in a surface finish of  $ R_{a} = 0.7 \, \mu m \pm 0.1 \, \mu m $. On average, approximately 260  $ \mu $m was removed from the downward-facing surface and approximately 210  $ \mu $m was removed from the upward-facing surface to achieve a defect-free surface. Applied stress amplitude during fatigue loading was determined using external cross-section measurements obtained using digital vernier calipers. Where rough surfaces existed, the maximum roughness height ( $ R_{t} $) was subtracted from external cross-section measurements. All mechanical testing was conducted at room temperature in a laboratory
Fig. 2. (a) Fatigue specimens arranged on the build plate, manufactured at 50^\circ inclination angle. (b) Non-contact, columnar supports with thin-wall, edge support used for flat specimens manufactured at inclination less than 40^\circ.

Polishing process applied to fatigue specimens.

| Grit | Polishing method | Test condition |
| --- | --- | --- |
| 120 | linisher w/water | Polished until no surface asperities visible. |
| 240 | linisher w/water | 20 seconds per direction. |
| 320 | manual polish w/water | 20 strokes each direction. |
| 600 | manual polish w/water | 20 strokes each direction. |

environment.

## 3. Results

Microstructural analysis and the results of mechanical testing are presented here to support the outcomes of this research.

## 3.1. Microstructure

All EBSD images were subjected to an auto-clean step within post-processing software (Aztec crystal) and conform to cleanup guidelines stated in ASTM E2627. Minimum solve rate for unprocessed EBSD information is 83.95 % (Fig. 3c), maximum solve rate for unprocessed EBSD information is 97.7 % (Fig. 4c). When using auto-clean function, the minimum resolved percentage change is 2.2 % (Fig. 4) and the maximum resolved percentage change is 8.37 % (Fig. 3c).

The  $ \alpha' $ martensite, typical of LB-PBF Ti-6Al-4V is observed before HIP (Fig. 3a & c). Needle-like alpha laths are observed within the prior beta grains; prior beta grains exhibit epitaxial growth parallel to the build direction of the specimens. The effect of grain coarsening after HIP is visually evident in the backscatter and EBSD images (Fig. 3). Based on approximations derived from EBSD data in Fig. 3c and d, using equivalent ellipse fitting method, after HIP, the lath length and breadth increase by approximately two times (Table 4). These statistics provide insights into the changes occurring in grain morphology and size due to the HIP treatment. The increase in area, length, breadth, and aspect ratio after HIP indicates grain coarsening, with larger and more elongated laths formed during the treatment. Such changes have implications for the material's mechanical properties, as discussed in Section 3.3.

Approximate average lath statistics for specimens manufactured at 0^\circ, 30^\circ and 90^\circ are presented in Table 5, characterised from EBSD data presented in Fig. 4. For all angles, the average length and breadth is larger in the bulk region by <7 %. The average lath area is larger in the bulk region by <19 %. Average lath length for 30^\circ specimens is less than for 0^\circ and 90^\circ in both the bulk and edge regions. Average lath breadth for 30^\circ specimens is greater than 0^\circ and 90^\circ specimens in the bulk region. IPF figures obtained using EBSD for specimens manufactured at 0^\circ, 30^\circ and 90^\circ are presented in Fig. 4. In regions close to the side and downward-facing surfaces, columnar growth of prior-beta grains parallel to build direction is not obvious (Fig. 4d, e, f). However, clear bands of similarly oriented laths can be seen within columnar prior beta grains in the bulk region (Fig. 4a, b, c).
Fig. 3. Backscatter images of vertically built (90^\circ) specimens a) before HIP and b) after HIP. EBSD images of vertically built specimens c) before and d) after HIP. IPF colour key for HCP phase is shown along with build direction (BD).
Fig. 4. IPF figures for bulk region after HIP of a) 0^\circ specimen, b) 30^\circ specimen, and c) 90^\circ specimen. IPF figures for regions close to the downward-facing surface after HIP of d) 0^\circ specimen and e) 30^\circ specimen, as well as the side-facing surface of f) 90^\circ specimen. IPF colour key for HCP phase is supplied at the bottom, build direction and scale is indicated in each image.

Table 4

Approximate average lath statistics calculated from EBSD data of 90^\circ specimens.

|  | Before HIP (Fig. 3c) | After HIP (Fig. 3d) |
| --- | --- | --- |
| Area ( $ \mu m^{2} $) | 3.25  $ \pm $ 7.72 | 10.7  $ \pm $ 18.4 |
| Length ( $ \mu m $) | 4.04  $ \pm $ 5.03 | 7.86  $ \pm $ 8.02 |
| Breadth ( $ \mu m $) | 1.19  $ \pm $ 0.71 | 2.16  $ \pm $ 1.46 |
| Aspect ratio ( $ \mu m $) | 3.07  $ \pm $ 1.73 | 3.60  $ \pm $ 2.12 |

Table 5

Approximate average lath size statistics after HIP, calculated from EBSD data.

|  | 0^\circ (Bulk) | 0^\circ (Edge) | 30^\circ (Bulk) | 30^\circ (Edge) | 90^\circ (Bulk) | 90^\circ (Edge) |
| --- | --- | --- | --- | --- | --- | --- |
| Area ( $ \mu m^{2} $) | 10.8 | 9.94 | 10.9 | 9.23 | 10.7 | 9.56 |
| Length ( $ \mu m $) | 7.92 | 7.66 | 7.39 | 7.00 | 7.86 | 7.46 |
| Breadth ( $ \mu m $) | 2.14 | 2.13 | 2.23 | 2.10 | 2.16 | 2.11 |
| Aspect ratio | 3.66 | 3.68 | 3.23 | 3.35 | 3.60 | 3.49 |

## 3.2. Surface roughness

The average surface roughness for upward-facing surfaces is lower than for downward-facing surfaces for all roughness metrics assessed (Fig. 5). Upward-facing, horizontal surfaces have the lowest surface roughness for all analysed metrics, except  $ R_{v} $. The upward-facing surface of  $ 50^{\circ} $ inclined specimens has a lower value for  $ R_{v} $. Compared to all the inclined specimens, the upward-facing surface of  $ 50^{\circ} $ specimens has the lowest surface roughness across all analysed metrics. However, the polished faces were characterised with  $ R_{a} = 0.7 \, \mu m \pm 0.1 \, \mu m $, which is significantly lower than horizontal, upward-facing surfaces ( $ R_{a} = 6.4 \, \mu m \pm 1.1 \, \mu m $); the lowest value of all as-manufactured surfaces in this research.

The upward-facing surface of  $ 10^{\circ} $ inclined specimens has the highest surface roughness across all analysed metrics compared to all other upward or side-facing surfaces. Furthermore, the downward-facing surface of  $ 10^{\circ} $ inclined specimens has the highest surface roughness across all analysed metrics compared to all other characterised surfaces. The difference in surface morphology between upward and downward-facing surfaces, and inclined versus horizontal surfaces, is further illustrated in Fig. 6.

## 3.3. Mechanical testing

The results of uniaxial tensile testing (Table 6) indicate that HIP specimens have lower strength but higher ductility than non-HIP specimens; this is a common observation for LB-PBF Ti-6Al-4V [41,60]. The 10^\circ inclined specimens also showed greater ductility and slightly higher yield strength compared to horizontally built specimens, both before and after HIP.

The results of all fatigue testing for upward and downward-facing roughness are plotted on an S-N curve (Fig. 7, Top). Fitting statistics for upward and downward-facing regression curves are detailed in Fig. 10. The discrepancy between the fatigue performance of upward and downward-facing specimens is characterised for  $ 1 \times 10^{4} $ ( $ \Delta E4 $),  $ 1 \times 10^{5} $ ( $ \Delta E5 $) and  $ 1 \times 10^{6} $ ( $ \Delta E6 $) cycles. Based on exponential regression curves, the stress amplitude at which upward specimens reach 1E6 cycles before failure, equivalent downward specimens only achieve 6.4E5 cycles ( $ \Delta E6=3.6E5 $). Similarly, the stress amplitude at which upward specimens reach 1E5 cycles before failure, equivalent downward specimens only achieve 6.1E4 cycles ( $ \Delta E5=3.9E4 $). Similarly, the stress amplitude at which upward specimens reach 1E4 cycles before failure, equivalent downward specimens only achieve 5.8E3 cycles ( $ \Delta E4=4.2E3 $).

The  $ 10^{\circ} $ specimens had a significant influence on regression curves and were therefore omitted from a supplementary S-N curve to analyse their impact on the overall data set (Fig. 7, Bottom). This supplementary analysis revealed the stress amplitude at which upward specimens reach 1E6 cycles before failure, equivalent downward specimens only achieve 5.0E5 cycles ( $ \Delta E6_{10}=5.0E5 $). Similarly, the stress amplitude at which upward specimens reach 1E5 cycles before failure, equivalent downward specimens only achieve 6.9E4 cycles ( $ \Delta E5_{10}=3.1E4 $). Similarly, the stress amplitude at which upward specimens reach 1E4 cycles before failure, downward specimens only achieve 9.6E3 cycles ( $ \Delta E4_{10}=0.4E3 $).

Only 50^\circ, 70^\circ and 90^\circ specimens reached runout for stress amplitudes below 300 MPa. Fatigue failure initiation commonly originated at

☐ Downward Facing ☐ Upward Facing ☐ Side facing

☑ Downward Facing ☐ Upward Facing ☐ Side Facing
Fig. 5. Surface roughness characterisation results for both the upward and downward-facing surface of each inclination angle. Side-facing surface roughness is reported for the vertically built specimens (90^\circ). Error bars denote +/- one standard deviation away from the average result for each series.
Fig. 6. Region of interest for both upward and downward-facing surfaces (a)-(d), with associated surface profile (e)-(h), magnified inset (i)-(l) and false colour focus variation data (m)-(p).

## Table 6

Tensile data for specimens with as-manufactured surfaces before and after HIP with standard deviation indicated.

|  | YS_{0.2\%} (MPa) | UTS (MPa) | Max. Elongation (%) |
| --- | --- | --- | --- |
| 0^\circ (No-HIP) | 1093 \pm 7.5 | 1226 \pm 3 | 2.09 \pm 0.7 |
| 10^\circ (No-HIP) | 1175 \pm 15 | 1382 \pm 21 | 3.60 \pm 1.1 |
| 0^\circ (HIP) | 1020 \pm 10 | 1060 \pm 13 | 3.21 \pm 0.2 |
| 10^\circ (HIP) | 1063 \pm 35 | 1129 \pm 33 | 5.13 \pm 0.9 |

or near the corners of specimens due to the geometry-induced stress concentration (Fig. 8c). In almost all cases, failure initiated at the rough, as-manufactured surface, not the polished surface (Fig. 8b).

The experimental results are used to link the contributing factors of roughness and inclination angle to the observed fatigue response of LB-PBF Ti-6Al-4V.

## 4. Discussion

## 4.1. Impact of orientation on observed fatigue response

As depicted in Fig. 5, surface orientation is highly influential to surface roughness. Focus variation microscopy is also a capable surface roughness characterisation technique, with results that are in strong agreement with high-resolution (5  $ \mu $m) computed tomography (CT) surface characterisation data presented in [61]. Single fatigue test specimens from this research were previously characterised using CT, and then the CT data was processed to obtain surface roughness values. For example, for the 50^\circ upward-facing surface, focus variation quantified the surface with  $ R_t = 62.1 $  $ \mu $m, high resolution CT quantified the surface with  $ R_t = 60.4 $  $ \mu $m. Even though focus variation is a line-of-sight characterisation method, it can still obtain reliable results in agreement with CT-derived roughness metrics.

When evaluating the cycles to failure for upward-facing specimens compared to downward-facing specimens at  $ 1 \times 10^{4} $ ( $ \Delta E4 $),  $ 1 \times 10^{5} $ ( $ \Delta E5 $) and  $ 1 \times 10^{6} $ ( $ \Delta E6 $) cycles, an average improvement of 63 % in cycles to failure is observed by removing downward-facing surface roughness (Fig. 7, Top). When evaluating the stress amplitude at these three cycles
Fig. 7. (Top) S-N curve for all samples and (Bottom) all samples excluding  $ 10^{\circ} $. Triangle markers represent specimens with an as-manufactured, upward-facing surface. Hollow circle markers represent specimens with an as-manufactured, downward-facing surface. Arrows depict runout specimens. Regression lines are generated using power fitting, no runout data was used for regression analysis according to ASTM E739 [59]. Yellow shaded regions illustrate the difference in fatigue life between upward and downward-facing specimens at 1E6 cycles ( $ \Delta E6 $,  $ \Delta E6_{10} $), 1E5 cycles ( $ \Delta E5 $,  $ \Delta E5_{10} $) and 1E4 cycles ( $ \Delta E4 $,  $ \Delta E4_{10} $).

to failure, upward-facing specimens can withstand 50 MPa, 30 MPa and 17 MPa more load than downward-facing specimens respectively. This represents an average improvement in stress amplitude of 10 % for the same number of cycles to failure.

Due to the strong influence of the  $ 10^{\circ} $ specimen data, it was removed from a supplementary S-N curve (Fig. 7, bottom) to analyse the influence of the  $ 10^{\circ} $ specimens on the overall fatigue response. The updated regression lines still highlight the positive effect of removing the downward-facing surface roughness however, this effect is much more prominent at higher fatigue lives, in agreeance with other literature sources [62]. The difference in fatigue cycles to failure highlighted by  $ \Delta E6_{10} $ in Fig. 7, Bottom is 5.0E5 cycles, thus representing a reduction in fatigue life of 50 % in the presence of downward-facing surface roughness. Whereas the fatigue strength of as-built and machined specimens has also been shown to be similar in the low to mid-life fatigue regime [25]. Generally, fatigue life at higher cycles is dominated by crack initiation i.e. many non-propagating cracks [62], whereas fatigue life at lower cycles is dominated by crack growth i.e. material properties. Considering that the main impact of downward-facing roughness is seen in the high cycle range when omitting poor performing  $ 10^{\circ} $ specimen data, where cracks are forming from surface defects, the regression model that omits poor performing  $ 10^{\circ} $ specimen data appears to be reasonable. These results verify the fatigue performance advantage obtained by removing the downward-facing surface roughness of as-manufactured components. Yadollahi et al. reported a surface defect layer of approximately 200  $ \mu $m [62] and in this research >200  $ \mu $m was removed on average in the polishing process (Section 2.4), thus suggesting the improvement in fatigue performance is truly attributed to the elimination of surface defects.

10^\circ specimens demonstrated the worst fatigue performance, consistent with the worst surface roughness (Fig. 5). These findings are consistent with other research [22,63,64] and relate to stair stepping. The stair step edge distance, h, can be predicted according to Eq. 1, using layer thickness,  $ L_{t} $, and inclination angle,  $ \alpha $. For  $ L_{t}=30 $  $ \mu $m and  $ \alpha=10^{\circ} $,
Fig. 8. SEM images of observed fracture. a) SEM images of 30^\circ specimen. Inset indicates i) and ii) secondary cracks in the region of primary failure. b) Fracture surface of 10^\circ specimen with crack growth direction and transition to shear lip [4] indicated. c) Fatigue cracks initiating close to failure location of 90^\circ specimen with observed iii) secondary cracks. Loading direction (LD) is indicated.
Fig. 9. a) Representation of the radius (r) of the equivalent defect area (A), and the calculation of A relative to applied load (F). b) Definition of surface roughness parameters  $ R_{v} $,  $ R_{p} $,  $ R_{z} $ relative to loading direction (LD). c) Definition of surface roughness parameters  $ R_{a} $ and  $ R_{q} $ relative to LD.

h~173  $ \mu $m, and for  $ \alpha=30^{\circ} $, h=60  $ \mu $m. Powder particles tend to adhere at layer edges, and when their size is comparable to  $ L_{t} $ and h, they will have a significant impact on surface roughness characterisations [63].

 $$ h=\frac{L_{t}}{\sin\alpha} $$ 

This unique dataset and findings can help assist build orientation optimisation decisions where fatigue performance is a priority and not all part surfaces can be post-processed by allowing for the distinct effect of both upward and downward-facing in design.

## 4.2. Correlation between inclination angle, surface roughness, and fatigue life

Murakami et al. developed the equivalent defect area,  $ A \, (\mathrm{m}^{2}) $ (Fig. 9a), approach to determine the stress intensity factor,  $ K \, (\mathrm{MPa/m}^{1/2}) $, of a notch (Eq. 2) [65], which has also been extended to predict the fatigue strength [66]. If the surface roughness (Fig. 9b and 9c) is used as the radius of a semi-circle (r) to determine  $ A \, (\mathrm{Eq.~2}) $, then the modified stress intensity factor,  $ \Delta K_{R} $, accounts for both applied load ( $ \sigma $) and largest, or highest, surface roughness. This can then be used for regression analysis to correlate roughness with fatigue life.

Table 7 ANOVA for response variable cycles to failure,  $ N_{f} $, with regressors stress,  $ \sigma $, arithmetic mean roughness,  $ R_{a} $, and upward/downward-facing rough surface indicator variable.

|  | $ \sigma $ | $ R_{a} $ | Up |
| --- | --- | --- | --- |
| F-Stat. | 380.9 | 87.60 | 5.252 |
| P-Value | <.001 | <.001 | 0.02 |
| $ R^{2} $ | 0.841 |  |  |

 $$ \Delta K_{R}=\mathbf{0.65}\Delta\sigma\sqrt{\pi\sqrt{A}} $$ 

 $$ A=0.5\pi r^{2} $$ 

Regression analysis was used to assess the relationship between  $ \Delta K_{R} $ and the number of cycles to failure,  $ N_{f} $, to quantify which surface roughness parameter is most capable of predicting the fatigue response of specimens with as-manufactured surfaces. Regression analysis was conducted using the groupings of all data (Fig. 11), downward-facing data (Fig. 12) and upward-facing data (Fig. 13). Runout data was excluded from regression analysis as directed by ASTM E739 [59].

To verify the applicability of stress, roughness and upward or downward-facing surface roughness in predicting  $ N_{f} $, an ANOVA test was performed. As shown in Table 7, all three regressors are statistically significant (P-value<0.05) in their ability to account for the variability of the response variable,  $ N_{f} $. When analysing the F-statistic, a measure of how well the variability is explained by each variable, applied stress is most significant, followed by roughness and then upward definition; a binary variable defining whether fatigue specimens had rough upward or downward-facing surfaces.

Regression analysis was then conducted on experimental fatigue data, grouped by upward-facing, downward-facing and all data combined (Fig. 10). All three cases show statistical significance in their correlation, based on the reported p-value. When comparing adjusted  $ R^{2} $ for all cases, regression of upward-facing data has the highest value. This suggests that the fatigue life of specimens with rough as-manufactured surfaces on upward-facing surfaces only can be predicted with greater certainty using this model as opposed to specimens with rough downward-facing surfaces. However, the F-statistic suggests that the fitting model grouping all data together is able to explain the variability in the data most adequately.

Regression analysis was then conducted on  $ \Delta K_{R} $ versus  $ N_{f} $, using six common roughness parameters to determine A (Eq. 3). The best and worst fits for all data, downward-facing data and upward-facing data are plotted in Fig. 11, Fig. 12 and Fig. 13 respectively.

When conducting regression analysis on  $ \Delta K_{R} $ versus  $ N_{f} $ for all fatigue data (Fig. 11), using  $ R_{t} $ to determine A resulted in the best fit and using  $ R_{a} $ resulted in the worst fit, with adjusted  $ R^{2} $ values of 0.68 and 0.61 respectively (Fig. 11). The adjusted  $ R^{2} $ and F-statistic is very close to that

All data

|  | $ \sigma @ 1e+04 $ cycles (MPa) | $ \sigma @ 1e+05 $ cycles (MPa) | $ \sigma @ 1e+06 $ cycles (MPa) |
| --- | --- | --- | --- |
| Up | 518 | 334 | 215 |
| Down | 468 | 304 | 198 |
|  | $ N_{f} @ 250 \text{MPa} $ | $ N_{f} @ 350 \text{MPa} $ | $ N_{f} @ 450 \text{MPa} $ |
| Up | 4.6E5 | 7.8E4 | 2.1E4 |
| Down | 2.9E5 | 4.7E4 | 1.2E4 |
|  | P-value | F-stat. | Adj.  $ R^{2} $ |
| Up | <.001 | 160.5 | 0.76 |
| Down | <.001 | 72.95 | 0.65 |
| All | <.001 | 184.4 | 0.67 |
Fig. 10. Regression analysis between maximum applied stress and cycles to failure. Data was grouped by upward or downward-facing data, and all data. P-value, F-statistic and adjusted  $ R^{2} $ values are presented. Runout data is excluded from regression analysis.

All data

<table border="1" style="margin: auto; word-wrap: break-word;"><tr><td rowspan="2"></td><td colspan="3">All data</td></tr><tr><td style="text-align: center; word-wrap: break-word;">P-value</td><td style="text-align: center; word-wrap: break-word;">F-stat.</td><td style="text-align: center; word-wrap: break-word;">Adj.  $ R^{2} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ R_{a} $</td><td style="text-align: center; word-wrap: break-word;">&lt;.001</td><td style="text-align: center; word-wrap: break-word;">138.9</td><td style="text-align: center; word-wrap: break-word;">0.61</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ R_{q} $</td><td style="text-align: center; word-wrap: break-word;">&lt;.001</td><td style="text-align: center; word-wrap: break-word;">149.3</td><td style="text-align: center; word-wrap: break-word;">0.62</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ R_{t} $</td><td style="text-align: center; word-wrap: break-word;">&lt;.001</td><td style="text-align: center; word-wrap: break-word;">190.2</td><td style="text-align: center; word-wrap: break-word;">0.68</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ R_{p} $</td><td style="text-align: center; word-wrap: break-word;">&lt;.001</td><td style="text-align: center; word-wrap: break-word;">172.2</td><td style="text-align: center; word-wrap: break-word;">0.66</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ R_{v} $</td><td style="text-align: center; word-wrap: break-word;">&lt;.001</td><td style="text-align: center; word-wrap: break-word;">155.3</td><td style="text-align: center; word-wrap: break-word;">0.63</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ R_{sm} $</td><td style="text-align: center; word-wrap: break-word;">&lt;.001</td><td style="text-align: center; word-wrap: break-word;">182.1</td><td style="text-align: center; word-wrap: break-word;">0.67</td></tr></table>
Fig. 11. Regression analysis for all data between  $ \Delta K_{R} $ and cycles to failure. Five roughness parameters are used to calculate the equivalent defect area in order to determine  $ \Delta K_{R} $. P-value, F-statistic and adjusted  $ R^{2} $ values are presented for all cases. Runout data is excluded from regression analysis.
Fig. 12. Regression analysis for downward-facing data between  $ \Delta K_{R} $ and cycles to failure. Five roughness parameters are used to calculate the equivalent defect area in order to determine  $ \Delta K_{R} $. P-value, F-statistic and adjusted  $ R^{2} $ values are presented for all cases. Runout data is excluded from regression analysis.

<table border="1" style="margin: auto; word-wrap: break-word;"><tr><td rowspan="2"></td><td colspan="3">Upward-facing data</td></tr><tr><td style="text-align: center; word-wrap: break-word;">P-value</td><td style="text-align: center; word-wrap: break-word;">F-stat.</td><td style="text-align: center; word-wrap: break-word;">Adj.  $ R^{2} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ R_{a} $</td><td style="text-align: center; word-wrap: break-word;">&lt;.001</td><td style="text-align: center; word-wrap: break-word;">156.7</td><td style="text-align: center; word-wrap: break-word;">0.76</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ R_{q} $</td><td style="text-align: center; word-wrap: break-word;">&lt;.001</td><td style="text-align: center; word-wrap: break-word;">164.9</td><td style="text-align: center; word-wrap: break-word;">0.77</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ R_{t} $</td><td style="text-align: center; word-wrap: break-word;">&lt;.001</td><td style="text-align: center; word-wrap: break-word;">166.3</td><td style="text-align: center; word-wrap: break-word;">0.77</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ R_{p} $</td><td style="text-align: center; word-wrap: break-word;">&lt;.001</td><td style="text-align: center; word-wrap: break-word;">77.2</td><td style="text-align: center; word-wrap: break-word;">0.60</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ R_{v} $</td><td style="text-align: center; word-wrap: break-word;">&lt;.001</td><td style="text-align: center; word-wrap: break-word;">338.1</td><td style="text-align: center; word-wrap: break-word;">0.87</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ R_{sm} $</td><td style="text-align: center; word-wrap: break-word;">&lt;.001</td><td style="text-align: center; word-wrap: break-word;">85.3</td><td style="text-align: center; word-wrap: break-word;">0.63</td></tr></table>
Fig. 13. Regression analysis for upward-facing data between  $ \Delta K_{R} $ and cycles to failure. Five roughness parameters are used to calculate the equivalent defect area in order to determine  $ \Delta K_{R} $. P-value, F-statistic and adjusted  $ R^{2} $ values are presented for all cases. Runout data is excluded from regression analysis.

obtained when conducting regression analysis between stress amplitude and  $ N_{f} $ for all data (Fig. 10), suggesting that using  $ \Delta K_{R} $ to correlate surface roughness with fatigue life does not yield significant benefits when ignoring the effects of upward and downward-facing surface roughness.

For the downward-facing data (Fig. 12), using  $ R_p $ to determine A resulted in the best fit for  $ \Delta K_R $ versus  $ N_f $ however, using  $ R_v $ resulted in the worst fit, with adjusted  $ R^2 $ values of 0.85 and 0.68 respectively. This contradicts the understanding that surface notches cause stress concentrations [29], thus facilitating crack initiation (Fig. 14). Meanwhile, the surface profile peaks carry no load according to finite element analysis displayed in Fig. 14, these results are in agreement with Kantzos et al. [14]. However, based on the results of this regression analysis,  $ R_p $ is able to describe the critical surface features more adequately for downward-facing surfaces. It is expected this is due to dross formation and adhered particles obscuring the surface notches (Fig. 6b, d, j, l, n, p). The difference in scatter when plotting  $ \Delta K_R $ against  $ N_f $ is visually evident (Fig. 12). The adjusted  $ R^2 $ is also improved over regression analysis between stress amplitude and  $ N_f $ of downward-facing data, in this case having an  $ R^2 $ of 0.65 (Fig. 10). This suggests that incorporating surface roughness measurements into fatigue modelling improves predictions for  $ N_f $, particularly when defining surface orientation i.e. upward or downward facing.

For the upward-facing data (Fig. 13), using  $ R_{v} $ to determine A resulted in the best fit for  $ \Delta K_{R} $ versus  $ N_{f} $ however, using  $ R_{p} $ resulted in the worst fit, with adjusted  $ R^{2} $ values of 0.87 and 0.60 respectively. The difference in scatter is also clearly visible when plotting  $ \Delta K_{R} $ against  $ N_{f} $ (Fig. 13). Furthermore, adjusted  $ R^{2} $ is improved over regression analysis between stress amplitude and fatigue life of upward-facing data, in this case having an  $ R^{2} $ of 0.76 (Fig. 10).  $ R_{V} $ quantifies the depth of surface notches which serve as crack initiation sites (Fig. 14), therefore it is intuitive that  $ R_{v} $ will provide the strongest correlation to fatigue failure.

## 4.3. Microstructural evolution of Ti-6Al-4V at varying build orientations: insights from EBSD analysis

The difference in microstructure between inclination angles is demonstrated in Fig. 4. It is understood that columnar prior beta grains will grow parallel to the build direction of AM specimens [40] and this is reinforced in the bulk material regions shown in Fig. 4a), b) and c). However, this phenomenon is less obvious in the regions close to the edge of the specimens in Fig. 4d), e) and f) where smaller grains are present. There is a trend in the approximate average lath size data Table 5 that lath length, breadth and area are larger in the bulk region than edge region. The increase in length and breadth is less than 7 % for all inclination angles and the increase in the area is less than 19 % for all inclination angles. Furthermore, these differences are less than one standard deviation in the measurement error and are not considered to be significant. The same is true for the differences in lath size between inclination angles.
Fig. 14. Left: SEM images of secondary fatigue cracks initiating from downward-facing surface notches (50^\circ specimen). The specimen was tested to failure according to the method described in 2.4. Right: FE analysis results showing high stress regions correlating with secondary fatigue crack initiation sites. Loading direction (LD) of the real component and the simulated geometry is indicated in the figure.

## 4.4. Implications for optimising fatigue-limited designs

To maximise the utility of the findings of this research, topology optimisation may be used to avoid inclination angles which may result in poor surface roughness. This would be relevant for components which are intended for use with as-manufactured surfaces. For components with as-manufactured surfaces, topology optimisation can be done so that surfaces with unfavourable orientation relative to roughness are avoided. High stress regions can be favoured for roughness reduction orientations i.e. high stress zone has surfaces with  $ >40^{\circ} $ orientation.

Overall build orientation of a component can be optimised to minimise overall surface roughness or minimise roughness on difficult to access surfaces. This type of optimisation algorithm may also assist the development of biomedical implants which may desire more or less surface roughness depending on the functional requirements. The inherent surface roughness of LB-PBF components is favourable for osseointegration [67]. Therefore, the quantified relationship between surface roughness and inclination angle can be utilised.

There is also potential for the relationship between surface roughness and inclination angle to be implemented into AM planning and topology optimisation software. An indication of the optimal build orientation to minimise surface roughness on regions which cannot be post-processed may be able to enhance the fatigue performance of components that are intended to be used in their as-manufactured state or with partial surface processing.

This research fills a gap in currently available fatigue data, assisting predictions for fatigue performance based on the surface condition. Approaches to certification may be improved with the knowledge that currently available surface roughness parameters are able to assist with the prediction of fatigue failure for components with as-manufactured surfaces. However, it is also clear that downward-facing surfaces are more detrimental to the fatigue performance of components with as-manufactured surfaces. Therefore, separate surface roughness definitions may become a requirement for upward and downward faces of relevant geometry. A proposal for documentation requirements of AM fatigue data, in order to facilitate data utility, have been highlighted in a previous publication by Rogers et al. [30] and this research has conformed to all requirements. The correlations between fatigue life and surface quality provided in the current research should be considered for future documentation guidelines in order to assist certification pathways.

## 5. Conclusions

The inherent surface roughness of LB-PBF Ti-6Al-4V is detrimental to fatigue life, as the rough surface provides favourable crack initiation sites. For inclined specimens, the surface roughness of downward-facing surfaces is more severe than upward-facing surfaces. However, there is an identified lack of knowledge on the effects of upward-facing surface roughness on fatigue life due to the dominant behaviour of the more severe downward-facing surface roughness. This research addresses this identified limitation using a novel methodology to isolate the effects of upward or downward-facing surface roughness on fatigue life of Ti-6Al-4V after HIP based on six manufactured inclination angles.

• On average, specimens manufactured at inclination angles  $ 50^{\circ}-90^{\circ} $ had longer fatigue lives than specimens manufactured at inclination angles  $ 0^{\circ}-30^{\circ} $, which had significant support structures and higher downward-facing surface roughness. Furthermore, the observed fatigue life of downward-facing samples is lower than upward-facing samples during fatigue loading.

• According to regression data, at the same stress amplitude that specimens with rough upward-facing surfaces could reach  $ 1 \times 10^{6} $ cycles, specimens with rough downward-facing surfaces could only reach  $ 6.4 \times 10^{5} $ cycles ( $ \Delta E6 $). At the same stress amplitude that specimens with rough upward-facing surfaces could reach  $ 1 \times 10^{4} $ cycles, specimens with rough downward-facing surfaces could only reach  $ 5.8 \times 10^{3} $ cycles ( $ \Delta E4 $). These results represent more than 35 % in fatigue life reduction in both cases due to the presence of downward-facing surface roughness alone.

- Stress intensity factor was correlated with fatigue life, using multiple surface roughness parameters to determine the equivalent defect area. Stress intensity factor yielded a stronger correlation with fatigue life than stress when the data was grouped by upward and downward-facing roughness.

- Using  $ R_{v} $ to determine the stress intensity factor provided the strongest correlation with the fatigue life of specimens with rough upward-facing surfaces. Using  $ R_{p} $ to determine the stress intensity factor provided the strongest correlation with the fatigue life of specimens with rough downward-facing surfaces, despite the link between surface notches and stress concentrations. This result is expected to be related to the limitations in line-of-sight surface roughness characterisation for re-entrant features on downward-facing surfaces.

This research is expected to enhance the optimisation of fatigue limited components with an array of inclined surfaces, intended to operate in an as-manufactured surface state. While the initial focus of this study is on Ti-6Al-4V, the established correlation can serve as a foundation for understanding the fatigue behaviour of other materials in additive manufacturing and drive advancements in optimising their performance.

## Funding

This project was funded by the Australian Defence Science and Technology Group.

## CRediT Authorship

Ma Qian: Supervision, Methodology, Funding acquisition, Conceptualization. Milan Brandt: Writing – review & editing, Supervision, Funding acquisition, Conceptualization. Jason Rogers: Writing – review & editing, Writing – original draft, Visualization, Methodology, Investigation, Formal analysis. Joe Elambasseril: Writing – review & editing, Supervision, Formal analysis. Chris Wallbrink: Writing – review & editing, Supervision, Methodology, Funding acquisition, Conceptualization. Beau Krieg: Writing – review & editing, Validation, Investigation, Formal analysis. Martin Leary: Writing – review & editing, Supervision, Data curation, Conceptualization.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data Availability

Data will be made available on request.

## Acknowledgements

The authors acknowledge the facilities, and the scientific and technical assistance of the RMIT Centre for Additive Manufacture and the RMIT Microscopy and Microanalysis Facility.

## References

[1] R. Molaei, A. Fatemi, N. Phan, Notched fatigue of additive manufactured metals under axial and multiaxial loadings, Part I: effects of surface roughness and HIP and comparisons with their wrought alloys, Int. J. Fatigue 143 (2021).

[2] J. Pegues, et al., Surface roughness effects on the fatigue strength of additively manufactured Ti-6Al-4V, Int. J. Fatigue 116 (2018) 543–552.

[3] M. Nakatani, et al., Effect of surface roughness on fatigue strength of Ti-6Al-4V alloy manufactured by additive manufacturing, Procedia Struct. Integr. 19 (2019) 294–301.

[4] R.I.A. Stephens, H.O. Fuchs, R.R. Stephens, Metal Fatigue in Engineering, in: H.O. C. Fuchs, R.R.C. Stephens (Eds.), Metal Fatigue in Engineering, Wiley Interscience Imprint, 2000.

[5] A. du Plessis, S. Beretta, Killer notches: the effect of as-built surface roughness on fatigue failure in AlSi10Mg produced by laser powder bed fusion, Addit. Manuf. 35 (2020) 101424.

[6] V. Chastand, et al., Comparative study of fatigue properties of Ti-6Al-4V specimens built by electron beam melting (EBM) and selective laser melting (SLM), Mater. Charact. 143 (2018) 76–81.

[7] S. Bagehorn, J. Wehr, H.J. Maier, Application of mechanical surface finishing processes for roughness reduction and fatigue improvement of additively manufactured Ti-6Al-4V parts, Int. J. Fatigue 102 (2017) 135–142.

[8] T.H. Becker, P. Kumar, U. Ramamurty, Fracture and fatigue in additively manufactured metals, Acta Mater. 219 (2021).

[9] S. Lee, et al., Surface roughness parameter and modeling for fatigue behavior of additive manufactured parts: a non-destructive data-driven approach, Addit. Manuf. 46 (2021).

[10] T. Persenot, et al., Fatigue performances of chemically etched thin struts built by selective electron beam melting: experiments and predictions, Materialia 9 (2020) 100589.

[11] D. Greitemeier, et al., Effect of surface roughness on fatigue performance of additive manufactured Ti–6Al–4V, Mater. Sci. Technol. (United Kingdom) 32 (7) (2016) 629–634.

[12] J. Elambasseril, et al., Laser powder bed fusion additive manufacturing (LPBF-AM): the influence of design features and LPBF variables on surface topography and effect on fatigue properties, Crit. Rev. Solid State Mater. Sci. 48 (2022) 132–168.

[13] W.E. Frazier, Metal additive manufacturing: a review, J. Mater. Eng. Perform. 23(6) (2014) 1917–1928.

[14] C.A. Kantzos, et al., Characterization of metal additive manufacturing surfaces using synchrotron X-ray CT and micromechanical modeling, Comput. Mech. 61 (5) (2018) 575–580.

[15] B. Whip, L. Sheridan, J. Gockel, The effect of primary processing parameters on surface roughness in laser powder bed additive manufacturing, Int. J. Adv. Manuf. Technol. 103 (9) (2019) 4411–4422.

[16] R. Konečná, et al., As-built surface layer characterization and fatigue behavior of DMLS Ti6Al4V, Procedia Struct. Integr. 7 (2017) 92–100.

[17] A. Yadollahi, et al., Fatigue life prediction of additively manufactured material: effects of surface roughness, defect size, and shape, Fatigue Fract. Eng. Mater. Struct. 41 (7) (2018) 1602–1614.

[18] L.N. Carter, et al., Exploring the duality of powder adhesion and underlying surface roughness in laser powder bed fusion processed Ti-6Al-4V, J. Manuf. Process. 81 (2022) 14–26.

[19] A. Cutolo, et al., On the role of building orientation and surface post-processes on the fatigue life of Ti-6Al-4V coupons manufactured by laser powder bed fusion, Mater. Sci. Eng. A 840 (2022).

[20] R. Shrestha, J. Simsiriwong, N. Shamsaei, Fatigue behavior of additive manufactured 316L stainless steel parts: effects of layer orientation and surface roughness, Addit. Manuf. 28 (2019) 23–38.

[21] A. Triantaphyllou, et al., Surface texture measurement for additive manufacturing, Surf. Topogr. Metrol. Prop. 3 (2) (2015) 24002.

[22] M. Leary, et al., 7 - Surface roughness, in: I. Yadroitsev, et al. (Eds.), Fundamentals of Laser Powder Bed Fusion of Metals, Elsevier, 2021, pp. 179–213.

[23] F. Calignano, Design optimization of supports for overhanging structures in aluminum and titanium alloys by selective laser melting, Mater. Des. 64 (2014) 203–213.

[24] A. Charles, et al., A Study of the Factors Influencing Generated Surface Roughness of Downfacing Surfaces in Selective Laser Melting, Proceedings of the World Congress on Micro and Nano Manufacturing (WCMNM), Portorož, Slovenia (2018).

[25] H. Gong, et al., Effect of defects on fatigue tests of as-built Ti-6Al-4V parts fabricated by selective laser melting. Solid freeform fabrication symposium, University of Texas Austin, Texas, 2012.

[26] J. Günther, et al., Fatigue life of additively manufactured Ti–6Al–4V in the very high cycle fatigue regime, Int. J. Fatigue 94 (2017) 236–245.

[27] B. Vayssette, et al., Surface roughness effect of SLM and EBM Ti-6Al-4V on multiaxial high cycle fatigue, Theor. Appl. Fract. Mech. 108 (2020) 102581.

[28] J. Gockel, et al., The influence of additive manufacturing processing parameters on surface roughness and fatigue life, Int. J. Fatigue 124 (2019) 380–388.

[29] L. Ednie, et al., The effects of surface finish on the fatigue performance of electron beam melted Ti–6Al–4V, Mater. Sci. Eng. A 857 (2022).

[30] J. Rogers, et al., Fatigue test data applicability for additive manufacture: a method for quantifying the uncertainty of AM fatigue data, Mater. Des. (2023) 111978.

[31] M. Leary, C. Burvill, Applicability of published data for fatigue-limited design, Qual. Reliab. Eng. Int. 25 (8) (2009) 921–932.

[32] X. Zhao, et al., Comparison of the microstructures and mechanical properties of Ti–6Al–4V fabricated by selective laser melting and electron beam melting, Mater. Des. 95 (2016) 21–31.

[33] T. Persenot, et al., Effect of build orientation on the fatigue properties of as-built Electron Beam Melted Ti-6Al-4V alloy, Int. J. Fatigue 118 (2019) 65–76.

[34] M. Benedetti, et al., The effect of post-sintering treatments on the fatigue and biological behavior of Ti-6Al-4V ELI parts made by selective laser melting, J. Mech. Behav. Biomed. Mater. 71 (2017) 295–306.

[35] W. Sun, et al., Effects of build direction on tensile and fatigue performance of selective laser melting Ti6Al4V titanium alloy, Int. J. Fatigue 130 (2020) 105260.

[36] S. Aguado-Montero, et al., Fatigue behaviour of PBF additive manufactured TI6AL4V alloy after shot and laser peening, Int. J. Fatigue 154 (2022) 106536.

[37] Y.Y. Sun, et al., Fatigue performance of additively manufactured Ti-6Al-4V: surface condition vs. internal defects, JOM (1989) 72 (3) (2020) 1022–1030.

[38] G. Nicoletto, Anisotropic high cycle fatigue behavior of Ti–6Al–4V obtained by powder bed laser fusion, Int. J. Fatigue 94 (2017) 255–262.

[39] G. Nicoletto, Directional and notch effects on the fatigue behavior of as-built DMLS Ti6Al4V, Int. J. Fatigue 106 (2018) 124–131.

[40] P. Edwards, M. Ramulu, Fatigue performance evaluation of selective laser melted Ti–6Al–4V. Mater. Sci. Eng. A Struct. Mater.: Prop. Microstruct. Process. 598 (2014) 327–337.

[41] G. Kasperovich, J. Hausmann, Improvement of fatigue resistance and ductility of TiAl6V4 processed by selective laser melting, J. Mater. Process. Technol. 220 (2015) 202–214.

[42] G. Qian, et al., In-situ investigation on fatigue behaviors of Ti-6Al-4V manufactured by selective laser melting, Int. J. Fatigue 133 (2020) 105424

[43] M. Benedetti, et al., Low- and high-cycle fatigue resistance of Ti-6Al-4V ELI additively manufactured via selective laser melting: mean stress and defect sensitivity, Int. J. Fatigue 107 (2018) 96–109.

[44] T.M. Mower, M.J. Long, Mechanical behavior of additive manufactured, powder-bed laser-fused materials, Mater. Sci. Eng. A Struct. Mater.: Prop. Microstruct. Process. 651 (2016) 198–213.

[45] M. Kahlin, H. Ansell, J.J. Moverare, Fatigue behaviour of notched additive manufactured Ti6Al4V with as-built surfaces, Int. J. Fatigue 101 (2017) 51–60.

[46] D. Greitemeier, et al., Fatigue performance of additive manufactured TiAl6V4 using electron and laser beam melting, Int. J. Fatigue 94 (2017) 211–217.

[47] E. Wycisk, et al., Fatigue Performance of Laser Additive Manufactured Ti–6Al–4V in Very High Cycle Fatigue Regime up to 109 Cycles, Front. Mater. 2 (2015).

[48] C. Navarro, et al., Effect of surface treatment on the fatigue strength of additive manufactured TI6AL4V alloy, Frat. Integrita Strutt. 14 (53) (2020) 337–344.

[49] E. Wycisk, et al., Effects of defects in laser additive manufactured Ti-6Al-4V on fatigue properties, Phys. Procedia 56 (2014) 371–378.

[50] K.S. Chan, et al., Fatigue life of titanium alloys fabricated by additive layer manufacturing techniques for dental implants, Metall. Mater. Trans. A Phys. Metall. Mater. Sci. 44 (2) (2012) 1010–1022.

[51] P.E. Carrion, et al., Powder recycling effects on the tensile and fatigue behavior of additively manufactured Ti-6Al-4V parts, JOM (1989) 71 (3) (2018) 963–973.

[52] A.J. Sterling, et al., Fatigue behavior and failure mechanisms of direct laser deposited Ti–6Al–4V. Mater. Sci. Eng. A Struct. Mater.: Prop. Microstruct. Process. 655 (2016) 100–112.

[53] K.F. Walker, Q. Liu, M. Brandt, Evaluation of fatigue crack propagation behaviour in Ti-6Al-4V manufactured by selective laser melting, Int. J. Fatigue 104 (2017) 302–308.

[54] S.M.J. Razavi, et al., Fatigue strength of blunt V-notched specimens produced by selective laser melting of Ti-6Al-4V, Theor. Appl. Fract. Mech. 97 (2018) 376–384.

[55] S.M.J. Razavi, P. Ferro, F. Berto, Fatigue assessment of Ti–6Al–4V circular notched specimens produced by selective laser melting, Metals 7 (8) (2017).

[56] M. Dallago, et al., Fatigue and biological properties of Ti-6Al-4V ELI cellular structures with variously arranged cubic cells made by selective laser melting, J. Mech. Behav. Biomed. Mater. 78 (2018) 381–394.

[57] E466-15, A, Standard Practice for Conducting Force Controlled Constant Amplitude Axial Fatigue Tests of Metallic Materials, ASTM International, West Conshohocken, PA, 2015.

[58] A. E8/E8M-15a, Standard Test Methods for Tension Testing of Metallic Materials, ASTM International, West Conshohocken, PA, 2015.

[59] 10, A.E.-, Standard Practice for Statistical Analysis of Linear or Linearized Stress-Life (S-N) and Strain-Life (\epsilon-N) Fatigue Data, ASTM International, West Conshohocken, PA, 2015, p. 7.

[60] S. Leuders, et al., On the mechanical behaviour of titanium alloy TiAl6V4 manufactured by selective laser melting: Fatigue resistance and crack growth performance, Int. J. Fatigue 48 (2013) 300–307.

[61] D. Downing, et al., A virtual stylus method for non-destructive roughness profile measurement of additive manufactured lattice structures, Int. J. Adv. Manuf. Technol. (2023).

[62] A. Yadollahi, N. Shamsaei, Additive manufacturing of fatigue resistant materials: Challenges and opportunities, Int. J. Fatigue 98 (2017) 14–31.

[63] G. Strano, et al., Surface roughness analysis, modelling and prediction in selective laser melting, J. Mater. Process. Technol. 213 (4) (2013) 589–597.

[64] A. Jones, et al., Effect of surface geometry on laser powder bed fusion defects, J. Mater. Process. Technol. 296 (2021) 117179.

[65] Y. Murakami, Chapter 2 - Stress Concentration, in: Y. Murakami (Ed.), Metal Fatigue, Elsevier Science Ltd, Oxford, 2002, pp. 11–24.

[66] H. Masuo, et al., Influence of defects, surface roughness and HIP on the fatigue strength of Ti-6Al-4V manufactured by additive manufacturing, Int. J. Fatigue 117 (2018) 163–179.

[67] N. Singh, et al., Selective laser manufacturing of Ti-based alloys and composites: impact of process parameters, application trends, and future prospects, Mater. Today Adv. 8 (2020).

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

Additive Manufacturing 85 (2024) 104149

$ ^{a} $ RMIT Centre for Additive Manufacturing, School of Engineering, RMIT University, Carlton, VIC, 3053, Australia
 $ ^{b} $ Platforms Division, Defence Science and Technology Group, 3207, VIC, Australia

## Keywords

Microstructure
Additive manufacturing
Titanium
Hot isostatic pressing
Inclined
Equivalent defect area

## ABSTRACT

https://doi.org/10.1016/j.addma.2024.104149

2214-8604/© 2024 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

Fatigue specimens manufactured at 0^\circ, 30^\circ and 90^\circ were cut parallel to the loading axis for microstructure evaluation before and after HIP to understand the microstructural changes relative to inclination angle and HIP. Samples were mechanically and chemically polished to yield a mirror finish and reveal the microstructure for backscatter electron (BSE) and electron backscatter diffraction (EBSD) analysis (JEOL-7200 F scanning electron microscope).

The results of uniaxial tensile testing (Table 6) indicate that HIP specimens have lower strength but higher ductility than non-HIP specimens; this is a common observation for LB-PBF Ti-6Al-4V [41,60]. The 10^\circ inclined specimens also showed greater ductility and slightly higher yield strength compared to horizontally built specimens, both before and after HIP.

Only 50^\circ, 70^\circ and 90^\circ specimens reached runout for stress amplitudes below 300 MPa. Fatigue failure initiation commonly originated at

10^\circ specimens demonstrated the worst fatigue performance, consistent with the worst surface roughness (Fig. 5). These findings are consistent with other research [22,63,64] and relate to stair stepping. The stair step edge distance, h, can be predicted according to Eq. 1, using layer thickness,  $ L_{t} $, and inclination angle,  $ \alpha $. For  $ L_{t}=30 $  $ \mu $m and  $ \alpha=10^{\circ} $,

This unique dataset and findings can help assist build orientation optimisation decisions where fatigue performance is a priority and not all part surfaces can be post-processed by allowing for the distinct effect of both upward and downward-facing in design.

## 4.2. Correlation between inclination angle, surface roughness, and fatigue life

## CRediT Authorship

## Data Availability

[59] 10, A.E.-, Standard Practice for Statistical Analysis of Linear or Linearized Stress-Life (S-N) and Strain-Life (\epsilon-N) Fatigue Data, ASTM International, West Conshohocken, PA, 2015, p. 7.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

ELSEVIER

Contents lists available at ScienceDirect

journal homepage: www.elsevier.com/locate/addma

Keywords:
Microstructure
Additive manufacturing
Titanium
Hot isostatic pressing
Inclined
Equivalent defect area

A B S T R A C T

* Corresponding author.

E-mail address: martin.leary@rmit.edu.au (M. Leary).

Received 3 December 2023; Received in revised form 9 April 2024; Accepted 15 April 2024

Available online 16 April 2024

J. Rogers et al.

Fatigue specimens manufactured at 0°, 30° and 90° were cut parallel to the loading axis for microstructure evaluation before and after HIP to understand the microstructural changes relative to inclination angle and HIP. Samples were mechanically and chemically polished to yield a mirror finish and reveal the microstructure for backscatter electron (BSE) and electron backscatter diffraction (EBSD) analysis (JEOL-7200 F scanning electron microscope).

The results of uniaxial tensile testing (Table 6) indicate that HIP specimens have lower strength but higher ductility than non-HIP specimens; this is a common observation for LB-PBF Ti-6Al-4V [41,60]. The 10° inclined specimens also showed greater ductility and slightly higher yield strength compared to horizontally built specimens, both before and after HIP.

Only 50°, 70° and 90° specimens reached runout for stress amplitudes below 300 MPa. Fatigue failure initiation commonly originated at

10° specimens demonstrated the worst fatigue performance, consistent with the worst surface roughness (Fig. 5). These findings are consistent with other research [22,63,64] and relate to stair stepping. The stair step edge distance, h, can be predicted according to Eq. 1, using layer thickness,  $ L_{t} $, and inclination angle,  $ \alpha $. For  $ L_{t}=30 $  $ \mu $m and  $ \alpha=10^{\circ} $,

This unique dataset and findings can help assist build orientation optimisation decisions where fatigue performance is a priority and not all part surfaces can be post-processed by allowing for the distinct effect of both upward and downward-facing in design.
4.2. Correlation between inclination angle, surface roughness, and fatigue life

CRediT authorship contribution statement

Data availability

[59] 10, A.E.-, Standard Practice for Statistical Analysis of Linear or Linearized Stress-Life (S-N) and Strain-Life (ε-N) Fatigue Data, ASTM International, West Conshohocken, PA, 2015, p. 7.