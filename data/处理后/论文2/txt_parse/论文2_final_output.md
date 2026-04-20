DOI: 10.1016/j.addma.2024.104151

# Microstructural evolution and formation of fine grains during fatigue crack initiation process of laser powder bed fusion Ni-based superalloy

Tao Shi $ ^{a,D} $, Jianghua Li $ ^{a,D} $, Guhui Gao $ ^{c} $, Jingyu Sun $ ^{a,b} $, Zhigang Yang $ ^{d} $, Jiayi Yan $ ^{d} $, Guian Qian $ ^{a,b,*} $

 $ ^{a} $ State Key Laboratory of Nonlinear Mechanics (LNM), Institute of Mechanics, Chinese Academy of Sciences, Beijing 100190, China

 $ ^{b} $ School of Engineering Science, University of Chinese Academy of Sciences, Beijing 100049, China

 $ ^{c} $ School of Mechanical, Electronic, and Control Engineering, Beijing Jiaotong University, Beijing 100044, China

 $ ^{d} $ School of Material Science and Engineering Key Laboratory of Advanced Materials of Ministry of Education, Tsinghua University, Beijing 100084, China

## ARTICLE INFO

## Keywords

Microstructure

Competitive fatigue failure mechanism

Laser powder bed fusion (LPBF)

Grain refinement

Precipitate dissolution

## Abstract

This study reports the fatigue failure mechanism at very-high-cycle fatigue (VHCF) regime of laser powder bed fusion (LPBF) GH4169 superalloy through a series of detailed microstructural characterizations, including scanning electron microscopy (SEM), transmission electron microscopy (TEM), electron backscatter diffraction (EBSD), and energy dispersive spectrometer (EDS). Microstructural characterization of the solution and double-aging post-treated initial material exhibits process-induced imperfections (mainly pores), as well as  $ \gamma' $,  $ \gamma'' $ and  $ \delta $ precipitates, and carbide. The fatigue tests were performed using an ultrasonic fatigue tester (20 kHz). Fatigue fracture analysis suggests there exists a competitive fatigue failure mechanism with surface flaw initiation and internal pore initiation, corresponding to high-cycle fatigue (HCF) and VHCF regime, respectively. Focused ion beam (FIB) samples taken within the fatigue initiation area (FIA) revealed grain refinement and precipitate dissolution behavior. Based on the characterization results, the fatigue crack initiation mechanism was hypothesized: During numerous cyclic loading, the mobile dislocations shear  $ \gamma' $ and  $ \gamma'' $ precipitates, causing their dissolution and local chemical and mechanical alterations near internal pores. This enables twinning and promotes sub-grains formation. Sub-grains refine via localized continuous dynamic recrystallization (CDRX), forming a fine-grained layer that leads to crack initiation. This work reveals how precipitate dissolution contributes to VHCF crack initiation in LPBF GH4169 superalloy, highlighting the potential for extending alloy lifespan by adjusting precipitates and LPBF defects and incorporating these factors into fatigue life predictions for enhanced accuracy.

## 1. Introduction

GH4169 is a Ni-based superalloy renowned for its outstanding mechanical properties at high temperatures, fatigue resistance and corrosion resistance, thus making it an ideal material for aero-engine turbine disks, blades and many other aerospace components [1,2]. Regrettably, this specific characteristic poses a challenge to machining the alloy into desirable as-built products [3]. Nevertheless, advanced additive manufacturing (AM) technology is able to avoid traditional design constraints and achieve a higher degree of geometric freedom with its digital design and layer-by-layer manufacturing strategy [4,5]. Recently, LPBF has been utilized for the production of GH4169 superalloy parts. However, during the AM process, the high dynamic melting pools, ultra-high cooling and solidification rates, and significant thermal gradients can lead to internal defects (e.g., lack of fusions (LOFs), gas pores, keyholes, etc.) and microstructural heterogeneity, which can degrade the fatigue performance of GH4169 parts [5,6]. Consequently, researchers have directed their attention towards fatigue failures stemming from defects and microstructural heterogeneity of additively manufactured (AMed) Ni-based superalloys [7–15]. Yang et al. [16] conducted fatigue tests on AMed IN718 superalloy, revealing that surface and internal crack initiation have a competitive relationship. Both observed defects arising from the manufacturing process (e.g., gas pore, LOFs) and matrix columnar grains may initiate primitive fatigue micro-cracks. Due to the intimate connection between defects and fatigue life, numerous researchers aim to quantify this relationship.

Table 1

Nominal chemical composition of the tested GH4169 snecimen powders (wt%).

| Element | Fe | Ni | Cr | Nb | Mo | Ti | Al | Co | C | Si | Cu |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| wt% | Balance | 52.08 | 20.12 | 5.33 | 3.24 | 0.99 | 0.54 | 0.056 | 0.036 | 0.038 | 0.013 |

Table 2

LPBF manufacturing parameters of the investigated GH4169 specimens.

| Laser power [W] | Scanning speed [mm/s] | Scanning spacing [mm] | Layer thickness [mm] | Printing direction [^\circ] | Laser profile |
| --- | --- | --- | --- | --- | --- |
| 240 | 980 | 0.1 | 0.04 | 90 | Linear |

fracture mechanics-based,  $ \sqrt{area} $ parameter model, proposed by Murakami and Endo [17], has been widely used for the quantitative evaluation of the fatigue strength of materials containing small defects. Kevinsanny et al. [9] performed fully-reversed, uniaxial fatigue tests using wrought Alloy 718 with different grain sizes and a variety of artificial small defects. As a result, they confirmed that in a small-crack regime, the predicted fatigue limits were in good agreement with the experimental results. Yu et al. [18] found that the fatigue resistance of laser powder bed fusion (LPBF) IN718 is related to the pore size and the location for the pore-induced fatigue failure. Sheridan et al. [19] explored the porosity produced during the AM process of IN718 super-alloy, and predicted the fatigue life of the experimental samples based on the size and location of pore. To obtain higher service quality and durability, it is necessary to understand the role of defects in fatigue failure of LPBF GH4169.

The mechanical properties of AM GH4169 are linked to the primary manufacturing parameters as well as post-treatments such as solid solution and aging. The extraordinary properties of GH4169 are attributed to the strengthening effect of coherently ordered precipitates, mainly the  $ \gamma'' $ phase ( $ D0_{22} $ body-centered tetragonal (bct),  $ Ni_{3}Nb $), and  $ \gamma' $ phase ( $ L1_{2} $ face-centered cubic (fcc),  $ Ni_{3}(Al, Ti) $) [20–22]. The organized precipitates raise both antiphase boundary (APB) and stacking fault energies (SFEs), leading to improved material strength. Nevertheless, prolonged exposure to high temperatures or excessive aging during heat treatment can cause the transformation of  $ \gamma'' $ into incoherent  $ \delta $ precipitates (D0a orthorhombic,  $ Ni_{3}Nb $), thereby diminishing the material strength [23]. There have been some studies focusing on the behavior of precipitates during cyclic loading. Observations revealed that for wrought IN718 superalloy, dislocations moving along slip planes sheared  $ \gamma'' $ and  $ \gamma' $ precipitates under cyclic deformation process, leading to notable cyclic softening and the formation of planar deformation bands [24,25]. The AMed IN718 samples showed an initial cyclic hardening behavior in the initial several cycles followed by a regime of saturation and softening. The pronounced cyclic softening was attributed to repeated shear and size reduction of  $ \gamma'' $ precipitated during cyclic loading, as very small precipitates offered little resistance to the cyclic movement of dislocations [26]. Furthermore, the growing crack was frequently blocked by  $ \delta $ precipitates and thus changed direction in LPBF IN718 specimens [27]. Existing work has shown that the presence of precipitates will affect dislocation motion and fatigue crack growth during cyclic loading. Although these studies dealt with some behaviors of the precipitates during fatigue, there is no systematic study for the microstructural evolution during VHCF process, including the evolution of grain structure and precipitates. Therefore, the present work focuses on the changes of grain structure and precipitates during the initiation of very-high-cycle fatigue (VHCF) cracks in LPBF GH4169 superalloy at room temperature.

Considering the increasing fatigue life requirements for structures and components in the aerospace field, which are required to reach  $ 10^{7} $ to  $ 10^{10} $ cycles (defined as VHCF) [28], it is necessary and urgent to study the VHCF properties of AMed Ni-based superalloys to enable further widespread application. Prior research indicates that crack initiation constitutes over 95% of the total fatigue life under VHCF conditions. That is to say, the crack initiation process occupies the majority of the VHCF process, so the study of the VHCF crack initiation process is crucial for engineering safety. The mechanism behind crack initiation has garnered significant interest [29]. Crack initiating mechanisms of high-strength steels [29–31], aluminum alloys [32–34] and titanium alloys [35–39] during VHCF process have been widely investigated. Under VHCF conditions, inclusions are the main contributor to cracking in high-strength steels, whereas the main causes of cracking in LPBF aluminum and titanium alloys are internal defects such as LOFs and gas pores. It is noteworthy that all these three materials formed nanograin layers in the fine-grained area (FGA) during VHCF process. However, the order of formation of fine grains and cracks remains controversial. In wrought and cast Ni-based superalloys, cracks are initiated primarily by grain facets and non-metallic inclusions (NMIs) [1,13,40,41]. However, for AM Ni-based superalloys, current research has focused on the low cycle fatigue (LCF) and high cycle fatigue (HCF) regimes [7,9,19,42,43]. Fatigue failures mainly originate from surface and subsurface pores and internal LOFs for AM Ni-based superalloys. However, the fatigue behavior of LPBF Ni-based superalloy in the VHCF regime is quite different from that of LCF or HCF. Thus, it’s necessary to clearly elucidate the VHCF failure modes, the presence or absence of fine grains in the fatigue crack initiation area (FIA), the crack initiation mechanism, the effects of precipitation and chemical heterogeneity on crack initiation, etc. of LPBF Ni-based superalloys.

In the present work, the HCF and VHCF failure modes and crack initiation mechanism of the LPBF GH4169 superalloy were investigated. A competing fatigue failure mode originating from surface flaws and internal pores was discovered. In addition, a fine-grained layer with precipitate dissolution was found in the FIA of VHCF failure specimens for the first time. Multi-scale characterization techniques were employed to investigate the structural and chemical properties of the fine grain. Possible formation mechanisms are discussed, encompassing dislocation movement, precipitate dissolution, element redistribution, and local continuous dynamic recrystallization (CDRX). The results of this work can help in the design of longer fatigue life LPBF GH4169 superalloy and improve the fatigue life prediction accuracy of subsequent simulations.

## 2. Experimental procedures

## 2.1. Materials

The EP-M250 system was employed to fabricate cylindrical blocks measuring 11 cm in height and 1.5 cm in diameter using pre-alloyed GH4169 powder with nominal chemical composition depicted in Table 1. The manufacturing parameters shown in Table 2 comprised laser power of 240 W, scanning speed of 980 mm/s, scanning spacing of 0.1 mm and layer thickness of 40  $ \mu $m. This configuration yielded a volumetric energy density ( $ E_{d} $) of approximately 61.22 J/mm $ ^{3} $.

The schematic of LPBF fabrication is shown in Fig. 1a. Throughout the manufacturing process, the laser systematically scans the powder layer, inducing melting followed by rapid solidification. After completing a layer, the laser’s scanning direction is adjusted by  $ 45^{\circ} $ to initiate the scanning of the subsequent powder layer as shown in Fig. 1b. This cyclic process continues until the fabrication of the entire sample is accomplished, yielding the as-built sample. The adoption of this scanning strategy effectively mitigates residual thermal stress and minimizes potential defects within the final part. The vertically printed samples are
Fig. 1. Manufacturing of LPBF specimens. (a) LPBF system; (b) Scanning strategy; (c) Vertical cylindrical blocks. (d) Standard tensile specimen. (e) Fatigue specimen diagram. (f) Ultrasonic fatigue test system.

shown in Fig. 1c.

Upon acquiring the as-built samples, a post heat treatment procedure was meticulously chosen to improve the mechanical properties. The heat treatment regimen encompasses both solution annealing and thermal aging. Solution annealing was performed at 980 ^\circC for 1 hour, then cooled with argon gas. This was followed by a first thermal aging stage at 720 ^\circC for 8 hours, cooling in the furnace at 50 ^\circC/h to 620 ^\circC, then a second stage at 620 ^\circC for 8 hours, and finally, cooling to room temperature using argon gas.

## 2.2. Tensile and fatigue test procedure

The tensile properties of LPBF GH4169 were assessed through a quasi-static tension test (with a strain rate of  $ 2.5 \times 10^{-4} $) conducted at room temperature. Standard tensile specimens, shown in Fig. 1d, featuring a gage diameter of 5 mm and a length of 27 mm, were employed for these tests.

The machined hourglass shaped fatigue test specimen is illustrated in Fig. 1e. The fatigue specimens are machined on a cutting machine with a processing accuracy of 2\mum. After the machining, no obvious machining traces along the tangential direction of the specimen were seen under the optical microscope. The effect of surface treatment on fatigue performance will be further studied in future work. The HCF and VHCF tests were conducted using a 20 kHz ultrasonic fatigue tester simply illustrated in Fig. 1f. Tensile-compression cyclic loading with a stress ratio (R) of -1 was applied. It is essential to acknowledge that such high-frequency loading may induce severe self-heating phenomenon in specimens, potentially influencing the microstructure and test results. To mitigate this, dry, compressed cold air is used to cool the fatigue specimen during the test in the center area where the temperature rise is most pronounced. In addition, the ultrasonic fatigue test frequency will be reduced if fatigue cracks appear in the specimen during the experiment. To ensure result accuracy and consistency, the test is automatically halted if the frequency drops below 19.5 kHz, indicating potential specimen failure even if complete fracture has not occurred. Additionally, if the test specimen does not fail after  $ 1 \times 10^9 $ fatigue cycles, the test concludes, and the fatigue life is defined as runout.

## 2.3. Microstructure characterization methods

Various analytical techniques were employed to characterize the initial microstructure of the LPBF GH4169 superalloy. X-ray diffraction (XRD), electron backscattering microscopy (EBSD), computed tomography (CT), transmission electron microscopy (TEM), and energy-dispersive spectroscopy (EDS) were utilized for this purpose. The all-encompassing micro-nano CT system, diondo d2 at Shanghai ND Inspection & Control Solution Co., Ltd, was specifically employed to capture three-dimensional images and assess the initial porosity. The EBSD analysis was conducted using a Zeiss GeminiSEM 300 machine with a 0.5  $ \mu $m step size and a 20 kV accelerating voltage. Sections measuring 3 mm in diameter were extracted from a plane oriented perpendicular to the building direction, thinned, and subsequently subjected to TEM observation. For the identification of chemical heterogeneity within the materials, EDS was employed to perform elemental distribution analysis.

Following the fatigue failure of the specimens, they were pulled off in the loading direction, and the fracture surfaces were meticulously examined using scanning electron microscopes (SEM) at various magnifications. Additionally, samples measuring approximately 6  $ \mu $m in length and 5  $ \mu $m in width were precisely sectioned using the focused ion beam (FIB)/SEM dual-beam system within the FIA. The FIB-prepared samples underwent comprehensive characterization employing transmission Kikuchi diffraction (TKD), EDS, and TEM. TEM observations were conducted using a high-resolution Thermofisher Talos F200X. This instrument, leveraging multi-channel merging technology and differential phase contrast (DPC) imaging technology, facilitated rapid and accurate EDS data processing along with quantitative analysis. Further crystallographic orientation mapping of the FIB samples was executed through TKD with a scan step size of 15 nm. Subsequently, the acquired EBSD and TEM data underwent post-processing using the HKL Channel5 and DigitalMicrograph software, respectively.
Fig. 2. (a) 3-dimensional schematic diagram and (b) Statistical analysis of the defects measured by CT technology. (c) XRD diffractograms; Inverse pole figure (IPF) color maps, pole figures (PFs), grain boundary (GB) maps and geometrically necessary dislocation (GND) maps of (d-f) x-y plane, (g-i) y-z plane for heat-treated samples; (j) TEM DF image showing cellular substructure; (k) TEM DF image showing lamellar substructure; (l) TEM DF image showing the precipitates of blocky  $ \gamma' $ and needle-like  $ \gamma'' $ phases; (m) TEM BF image showing precipitates at the lamellar substructure boundary, and SAED patterns of green boxed area and red boxed area; (n) TEM BF image showing the precipitates of spherical carbide and needle-like  $ \gamma'' $, and Fast Fourier Transform (FFT) images; (o) TEM BF image showing the  $ \sigma $ phase.

Table 3

Observed secondary phases in initial LPBF GH4169 materials.

| Phase label | Crystal structure | Formula | Morphology |
| --- | --- | --- | --- |
| $ \gamma' $ | Cubic (FCC) | Ni3(Ti, Al) | Spherical, globular, blocky, or cuboidal shape |
| $ \gamma'' $ | Tetragonal (BCT) | Ni3Nb | Disc or plate shape |
| $ \delta $ | Orthorhombic | Ni3Nb | Needle or plate shape |
| MC | Cubic (FCC) | (Nb, Ti)(C, N) | Globular or blocky shape |
| $ \sigma $ | Tetragonal | FeCr | Irregular shape |

Table 4

Nominal chemical composition of the EDS observed points in Fig. 2.

<table border="1" style="margin: auto; word-wrap: break-word;"><tr><td style="text-align: center; word-wrap: break-word;">Points</td><td style="text-align: center; word-wrap: break-word;">Phase</td><td colspan="6">Element at%</td></tr><tr><td style="text-align: center; word-wrap: break-word;"></td><td style="text-align: center; word-wrap: break-word;"></td><td style="text-align: center; word-wrap: break-word;">C</td><td style="text-align: center; word-wrap: break-word;">Ti</td><td style="text-align: center; word-wrap: break-word;">Cr</td><td style="text-align: center; word-wrap: break-word;">Fe</td><td style="text-align: center; word-wrap: break-word;">Ni</td><td style="text-align: center; word-wrap: break-word;">Nb</td></tr><tr><td style="text-align: center; word-wrap: break-word;">A</td><td style="text-align: center; word-wrap: break-word;">$ \gamma $</td><td style="text-align: center; word-wrap: break-word;">\</td><td style="text-align: center; word-wrap: break-word;">1.02</td><td style="text-align: center; word-wrap: break-word;">26.01</td><td style="text-align: center; word-wrap: break-word;">22.75</td><td style="text-align: center; word-wrap: break-word;">49.55</td><td style="text-align: center; word-wrap: break-word;">0.64</td></tr><tr><td style="text-align: center; word-wrap: break-word;">B</td><td style="text-align: center; word-wrap: break-word;">$ \delta $</td><td style="text-align: center; word-wrap: break-word;">\</td><td style="text-align: center; word-wrap: break-word;">3.63</td><td style="text-align: center; word-wrap: break-word;">1.95</td><td style="text-align: center; word-wrap: break-word;">2.85</td><td style="text-align: center; word-wrap: break-word;">82.65</td><td style="text-align: center; word-wrap: break-word;">8.90</td></tr><tr><td style="text-align: center; word-wrap: break-word;">C</td><td style="text-align: center; word-wrap: break-word;">Carbide</td><td style="text-align: center; word-wrap: break-word;">39.75</td><td style="text-align: center; word-wrap: break-word;">17.32</td><td style="text-align: center; word-wrap: break-word;">6.49</td><td style="text-align: center; word-wrap: break-word;">4.30</td><td style="text-align: center; word-wrap: break-word;">17.88</td><td style="text-align: center; word-wrap: break-word;">14.22</td></tr><tr><td style="text-align: center; word-wrap: break-word;">D</td><td style="text-align: center; word-wrap: break-word;">$ \sigma $</td><td style="text-align: center; word-wrap: break-word;">\</td><td style="text-align: center; word-wrap: break-word;">0.62</td><td style="text-align: center; word-wrap: break-word;">89.22</td><td style="text-align: center; word-wrap: break-word;">6.49</td><td style="text-align: center; word-wrap: break-word;">3.31</td><td style="text-align: center; word-wrap: break-word;">0.34</td></tr></table>

## 3.1. Initial microstructure characteristic

## 3. Results

Defects significantly affect fatigue life. Therefore, in order to have an approximate distribution of the defects, CT technology was used for three-dimensional characterization of the defects. The overall distribution of defects is shown in the Fig. 2a. Fig. 2b illustrates the defects diameter and sphericity distribution of heat-treated LPBF GH4169 superalloy. The porosity of the sample is 0.0017% and there are no obvious LOFs but only a small amount of gas pores. This rather low porosity can be attributed to advanced AM equipment, optimal processing parameters, and suitable printing strategy.

In this work, the x-y-z coordinate system is used, where x represents build direction (BD), y represents longitudinal direction (LD), and z represents transverse direction (TD). The XRD diffractogram of the horizontal (y-z) plane is shown in Fig. 2c. The  $ \gamma(111)/\gamma'(111)/\gamma''(112) $ peak exhibits an almost precise match, along with corresponding matches for  $ \gamma(200)/\gamma'(200)/\gamma''(200)/\gamma'(220)/\gamma''(220)/\gamma'(311)/\gamma''(311)/\gamma''(033) $.

The microstructure along and perpendicular to the build direction is shown in the EBSD image in Fig. 2. The inverse pole figures (IPFs) in Fig. 2d and g demonstrate that the longitudinal section contains grains with an average diameter of 17.64 \mum, while the transverse section shows grains with an average diameter of 19.36 \mum. The pole figures (PFs) in Fig. 2d and g show that LPBF GH4169 has weak texture. In Fig. 2e, the grain boundary (GB) map of the x-y plane illustrates a predominant presence of low-angle grain boundaries (LAGBs, 2^\circ-15^\circ, 64.4%), accompanied by a smaller proportion of high-angle grain boundaries (HAGBs, >15^\circ, 35.6%). Similarly, the GB map of the y-z plane in Fig. 2 h exhibits a comparable distribution, with LAGBs (2^\circ-15^\circ, 67.6%) and HAGBs (>15^\circ, 32.4%). In addition, the average geometric necessary dislocation (GND) density calculated by HKL Channel5 software at both x-y and y-z planes is 0.55\times10¹⁴/m², as shown in Fig. 2 f and i.

In order to clarify the phases and their information found in the initial material (material before fatigue test), the observed results are
Fig. 3. HADDF micrographs and corresponding chemical elemental distribution maps of initial material.
Fig. 4. (a) Tensile curves. (b) S-N data of ultrasonic fatigue tests with stress ratio R = -1.

presented in Table 3. (1) The  $ \gamma' $ phase, characterized as an fcc-type  $ Ni_{3}(Al,Ti) $ ordered phase, can adopt various shapes such as spherical, globular, blocky, or cuboidal depending on the  $ \gamma/\gamma' $ lattice mismatch; (2) the  $ \gamma'' $ phase is identified as a body-centered tetragonal (bct) type  $ Ni_{3}Nb $ ordered phase, taking on a disk-shaped or plate-shaped morphology; (3) the  $ \delta $ phase is an orthorhombic  $ Ni_{3}Nb $ ordered intermetallic compound, exhibiting a needle or plate-shaped structure; (4) fcc-type carbide phases (MC) are present with either globular or blocky shapes; (5) the sigma ( $ \sigma $) phase is characterized by a tetragonal crystal structure. In conjunction with the matrix, these precipitates play a crucial role in defining the mechanical properties of the material.

TEM and EDS observations were conducted to characterize the microstructure unambiguously. Fig. 2j and k are TEM bright field (BF) image showing cellular and lamellar substructures in the grains, respectively. Needle-like precipitates can be clearly seen inside the substructures, some plate-like and circular precipitates appear near the boundaries. In a dark-field (DF) micrograph illustrated in Fig. 2 l, the near-cuboidal precipitates were  $ \gamma' $ precipitates, while the other elliptical precipitates were  $ \gamma'' $ precipitates. The BF image in Fig. 2 m shows a plate-like precipitate lying on the grain boundary and some needle-like precipitates near the boundary. For the SAED pattern in the region labeled 'A', reflections (111), (111), and (002) originate from  $ \gamma $ matrix, while reflections (110) and (002) are attributed to  $ \gamma'' $ precipitates. The orientation relationship between  $ \gamma'' $ and the  $ \gamma $ matrix is expressed as (110)[110] $ _{\gamma''} $ // (111)[110] $ _{\gamma} $. Moving on to the SAED pattern in the region labeled 'B', reflections (111), (002), and (111) stem from the  $ \gamma $ matrix, while (201) and (010) reflections are associated with  $ \delta $ precipitates. Consequently, the dark plate-like precipitate correspond to the  $ \delta $ phase, and the adjacent light area represents the  $ \gamma $ matrix. The orientation relationship between  $ \delta $ and the  $ \gamma $ matrix is articulated as (010)[102] $ _{\delta} $ // (111)[110] $ _{\gamma} $. To analyze the elemental composition at specific locations labeled 'A', 'B', 'C' and 'D', EDS point scanning was conducted. The findings are presented in Table 4. Notably, the 'C' phase depicted in Fig. 2 n exhibits a high concentration of carbon (C), confirmed by the SAED map, supporting its identification as a carbide. Furthermore, the 'D' phase depicted in Fig. 2 o displays an abundance of chromium (Cr), accompanied by some Fe and Ni elements, confirmed by the SAED map, leading to speculation that it corresponds to the  $ \sigma $ phase.

EDS area scanning was used to observe elemental distributions in Fig. 3a and b. The dark circular-like precipitate labelled ‘E’ and ‘F’ near the substructure boundary enriched in C, Nb and Ti, which indicates that precipitated phases are NbC and TiC. Both Fig. 3a and b show that there are lots of circular-like  $ \gamma' $ and needle-like  $ \gamma'' $ precipitates within the substructure, and  $ \delta $ precipitate on the cellular substructure boundary providing strengthening effect for LPBF GH4169.

## 3.2. Tensile and fatigue test results

Two standard tensile tests were performed, and the stress-strain curves are shown in Fig. 4a. The repeatability observed in the two tensile tests was remarkably high, underscoring the stability of the material's mechanical properties. The tensile test results reveal an elastic modulus of 197 GPa, a yield strength (at 0.2% plastic strain) of 1266 MPa, a tensile strength of 1414.5 MPa, and a uniform elongation of 16.4%.

The S-N curve of the ultrasonic fatigue test at room temperature is shown in Fig. 4b. According to the data, the fatigue life of the specimens is in the range of  $ 1.68 \times 10^{6} $ to  $ 1.03 \times 10^{9} $ cycles, corresponding to the HCF and VHCF regimes. In particular, at a stress amplitude of 518.79 MPa, the fatigue life has a large scatter. In addition, the SEM observations of fatigue fracture showed two different modes of crack initiation: surface flaw and internal pore. In the context of fatigue life, the initiation of cracks in the specimen primarily stems from surface flaws during the HCF regime. Conversely, in the VHCF regime, the predominant factor is the cracks initiated from internal pores. The runout case is illustrated by the presence of two black dots in Fig. 4b.

## 3.3. Fractography observation

Fig. 5 shows SEM observations of typical fracture surfaces. These images distinctly reveal the regions of early crack initiation, medium crack propagation, and eventual transient fracture. The location of fatigue cracking initiation is interrelated to the fatigue life. In specimens failed under the HCF condition, the fatigue cracks initiate from surface flaws. In contrast, for specimens failed under the VHCF condition, the primary sites of crack initiation are predominantly pores situated within the specimens.

In Fig. 5a, the microscopic fracture morphology depicts a crack initiated by a surface flaw under the HCF regime ( $ \sigma_{a} = 534MPa, N_{f} = 2.18 \times 10^{6} $). FIA can be easily found based on the direction of convergence of river patterns. To examine the origin pattern of fatigue cracks, the fracture morphology at the crack initiation site was further magnified, as depicted in Fig. 5b and c. These images reveal that the crack originated from a surface flaw and was accompanied by large-sized facets around it, suggesting rapid crack propagation along the slip planes.

In Fig. 5d, the fatigue cracks are observed to initiate from the gas pore within the specimen ( $ \sigma_{a} = 537MPa, N_{f} = 4.5 \times 10^{7} $). The fracture surface exhibits a pattern converging towards an internal pore. Upon closer examination, the surface surrounding the initiation site exhibits a rugged and uneven morphology. Stress concentration is notably present at the edges of the pores, creating a favorable environment for fatigue cracking under cyclic loading. The roughness surrounding the pore is likely associated with grain refinement. Abundant secondary cracks and
Fig. 5. (a) Fracture surface morphology of the Specimen I with fatigue life  $ N_{f} = 2.18 \times 10^{6} $. (b) and (c) Higher magnification of surface flaw fatigue nucleation site. (d) Fracture surface morphology of the Specimen II with fatigue life  $ N_{f} = 4.5 \times 10^{7} $. (e) and (f) Higher magnification of internal pore fatigue nucleation site. (g) Fracture surface morphology of the Specimen III with fatigue life  $ N_{f} = 1.73 \times 10^{8} $. (h) and (i) Higher magnification of subsurface pores cluster fatigue nucleation site.

facets are evident in the vicinity of this rugged zone.

Fatigue failures within the range of  $ 10^{8} $ to  $ 10^{9} $ cycles typically manifest as VHCF failures. Fig. 5g shows the comprehensive fracture morphology of a fatigue specimen failed under the VHCF condition ( $ \sigma_{a} = 508.5MPa, N_{f} = 1.73 \times 10^{8} $). The image reveals a clearly defined bright area at the subsurface, encircled by radiating ridges. Upon closer inspection, magnification unveils that the bright region comprises a cluster of small-sized pores, with a prominent large-sized facet interconnecting the pores within the cluster.

To investigate the mechanism behind fatigue crack initiation, FIB sampling analysis was conducted on Specimen II and Specimen III. These two samples are considered representative, showcasing the two prevalent forms of defects that lead to fatigue crack initiation within the samples, namely a single large-sized pore and a colony of small-sized pores.

## 3.4. Detailed observation of FIA caused by single pore

In order to comprehend the crack initiation mechanism in LPBF GH4169 superalloy under VHCF regime, the FIB-sample-A taken from the Specimen II failed by single pore induced crack initiation ( $ \sigma_a = 537MPa, N_f = 4.5 \times 10^7 $) was studied by TKD, TEM and EDS representation technologies. The position for preparation of the FIB-sample-A is shown in Fig. 5f.

The IPF map shown in Fig. 6a clearly shows the grain distribution of FIB-sample-A, with the right side close to the pore and the left side away from the pore. Notably, a fine-grained layer is discernible at the fracture surface. Close to the pore end, numerous lamellar grains arise from slipping, whereas cellular fine grains are more prevalent in regions distanced from the pore end. The measured average equivalent diameter of these fine grains is 120 nm. Besides, the misorientation angle is measured by EBSD analysis, and grain boundary plot is shown in Fig. 6b. HAGBs account for 63.2%, while LAGBs 36.8%. It is also worth noting that twin boundaries (TBs) account for a large proportion. TBs are categorized into two types: those induced by slip in the matrix and those caused by slip in coarser fine grains. In addition, the PF maps in Fig. 6d show that the maximum intensity of fine grain area is 4.91, and the orientation of fine grains are relatively random. Moreover, the GND map in Fig. 6c denotes that the GND is concentrated at LAGB sites, and the value of  $ \bar{\rho}_{GND} $ is  $ 15.2 \times 10^{14} / m^{2} $, which is much higher than the initial material. To delve deeper into the mechanism of fine grain formation and microstructural behavior, Schmid factors (SFs) for 12 slip systems, encompassing (111), (111), (111) and (111) slip planes with [110], [101] and [011] slip directions (FCC), were systematically calculated for each grain below the fracture surface using Python programming. SF is the effective coefficient of macroscopic tensile stress decomposition to a certain direction in the microscopic grain level, which indicates the effective degree of decomposition of unidirectional tensile stress in the crystal on the slip surface and in the slip direction, and it is a characteristic coefficient to measure the difficulty of initiating a certain slip coefficient in the grain. In Fig. 6a, slip traces for each grain, associated with four slip planes, are visually represented by four colored arrows.
Fig. 6. (a) IPF, (b) GB (c) GND maps of FIB-sample-A taken from Specimen II through FIB technology. (d) PF map of fine grains. (e) Statistical distribution of SFs for FIB-sample-A.

enclosed within a circle. The intersection line of the slip plane and the TKD coordinate x-y plane was defined as the slip trace in this paper. From the SF statistics shown in Fig. 6e, it is inferred that (111), (111) and (111) slip planes dominated easy-activated slip systems.

Fig. 7a displays the BF TEM image of FIB-sample-A, revealing the presence of a fine-grain layer in proximity to the crack surface. The SAED map of the matrix clearly shows the presence of the precipitated phase. What needs to be emphasized is that there is a crack originating from the pore very close to the fracture surface on the top end. A localized section of the sample situated above the crack and near the fracture surface exhibits a significant degree of grain refinement, as evidenced by the SAED pattern in Fig. 7c. Additionally, microcracks manifest at the interface between the fine-grain layer and the coarse-grain matrix. This may be due to the reduced crack initiation threshold along the fine-coarse grain interface. Fig. 7d presents a high-magnification BF TEM image of the region enclosed by the green box in Fig. 7b. The SAED map of a typical fine grain indicates that it is a single crystal with no precipitates. The DF TEM image depicted in Fig. 7e shows that the equivalent diameter of the fine grain is approximately 300 nm. Besides, in Fig. 7f, there are many parallel TBs inclined at 50 degrees to the loading direction near the pore. They may be caused by matrix slip.

The TEM image reveals a remarkably clean interior within the fine grain, prompting an investigation into the FGA from a chemical perspective. Firstly, EDS was used to conduct a more refined characterization of the matrix close to the fine grain area. The  $ \gamma' $ and  $ \gamma'' $ precipitates can be clearly distinguished in Fig. 8a. Then, the EDS map in Fig. 8b of a typical fine grain shows that the elements are evenly distributed, and the SAED map in Fig. 8b3 has only one set of spots, indicating that the ordered precipitates inside the fine grain are dissolved. In addition, Fig. 8c shows that chemical elemental homogenization has also occurred in the TBs and their nearby matrix. The apparent boundary between the fine grain region and the matrix can be clearly seen in Fig. 8d. Notably, the boundary in the EDS map differs from that in the TEM image, specifically positioning closer to the matrix. This implies that the ordered precipitate phase dissolves, and elemental homogenization occurs prior to grain refinement. However, it is noteworthy that carbide remains incompletely dissolved, likely attributed to its inherent stability.

## 3.5. Detailed observation of edge of FIA caused by pores colony

The same characterization techniques are used to analyze the FIB-sample-B taken from the interface between the porosity zone and the facets of Specimen III (pores cluster induce crack initiation), with the left side near the porosity zone and right side near the facets. As shown in Fig. 9a, the IPF map demonstrate that the end close to the pores has the formation of lamellar substructure, the end close to the facets remains faceted, and there is obvious grain refinement with an average diameter of 110 nm in the middle. The GB map in Fig. 9b indicates that LAGBs account for a large proportion. HAGBs are concentrated in the fine-grained region and the boundary between the lamellar substructure and the matrix, while LAGBs are concentrated inside the lamellar substructure and in the matrix close to the fracture surface. Similar to FIB-
Fig. 7. Microstructural characterizations of the fine-grain layer at the fatigue initiation site. (a) TEM BF image of FIB-sample-A ( $ \sigma_{a} = 537MPa $,  $ N_{f} = 4.5 \times 10^{7} $). (b) and (c) Higher magnification TEM BF images and SAED pattern of local area. (d) Higher magnification TEM BF image and SAED pattern of local fine grain area. (e) TEM DF image corresponding to (d). (f) Higher magnification TEM BF image and SAED pattern of twin grain in fine-grain layer.

sample-A, the GND map in Fig. 9c denotes that the GND is concentrated at LAGB sites, and the value of  $ \bar{\rho}_{\text{GND}} $ is  $ 23.7 \times 10^{14}/\text{m}^2 $, which is much higher than the initial material. In addition, the PF maps in Fig. 9d shows that the maximum intensity of fine grain area is 10.73, with a slightly higher than the initial material. This may be because there are fewer fine crystals here, which is not statistically significant. The SFs statistics have analogous results with Sample-I, and the lamellar substructure is produced by slip plane (111).

TEM images reveal more information. Typical  $ \delta $ phases on the grain boundary between two grains can be seen in the Fig. 10a. Fig. 10b, c and d show the lamellar substructure, facet and fine grain area, respectively. SAED plot in Fig. 10d indicate a high degree of grain refinement. In addition, the SAED plot of a single fine crystal in Fig. 10e shows that there is no other precipitated phase in the fine grain, and the corresponding dark-field diagram in Fig. 10f shows that the equivalent diameter of the fine grain is 200 nm.

Several typical locations were selected for EDS analysis. First of all, Fig. 11a depicts the precipitated phases in the lamellar substructure have dissolved and the elements are well distributed. The demarcation line of the elements in EDS is exactly the demarcation line of the structures in TEM. The SAED map in Fig. 11a3 shows that the lamellar substructure is the matrix  $ \gamma $ phase. The other location is at the junction of the fine grains and the matrix shown in Fig. 11b. There are no more precipitated phases in the fine grains and the elemental boundary is closer to the matrix than the structural boundary. The SAED map in Fig. 11b3 illustrates that the fine grain is matrix  $ \gamma $ phase. The third location is a bump near the facet, which is shown to be highly refined by the SAED diagram in Fig. 11c3, and the EDS diagram illustrates the uniform distribution of elements in the fine grain area. The last position is located on the faceted surface, and the TEM, SAED and EDS maps in Fig. 11d all show that there are precipitates in addition to matrix  $ \gamma $ phase.

## 4. Discussion

## 4.1. Competing failure modes

The S-N curve depicted in Fig. 4b and fracture surface morphologies in Fig. 5 reveal notable distinctions in fatigue initiation modes. These differences suggest the presence of a competing failure mode in the HCF and VHCF regimes, linked to a transition from surface flaws to internal pores as the initiation site. There seems to be a stress amplitude limit of about 518.79 MPa, with surface initiation above the limit and inner pore initiation below the limit. The considerable variability in fatigue life observed at a stress amplitude of 518.79 MPa can be attributed to a competition of surface and internal failures.

Under elevated stress amplitudes, surface flaws introduced during the specimen machining process can induce significant stress concentration at the defect’s edge, leading to the initiation of fatigue cracking. Following the formation of the initial crack, it propagates swiftly along the slip plane as it traverses through the grain. This process results in the formation of facets inclined at an angle to the loading direction, as illustrated in Fig. 5c.

During cyclic loading, the pore functions as a pre-existing crack or stress concentrator, inducing stress concentration in the microstructure surrounding the pore. However, pores have a lower degree of stress concentration due to their higher sphericity and it is well known that surface or subsurface defects are more detrimental to fatigue life than internal defects [44]. Consequently, specimens with internal pore initiation tend to exhibit longer fatigue life compared to those with surface initiation. In addition, a rough area can be seen around the pore and some facets appear outside the rough area. Based on more detailed observations, we can determine that the rough area is FGA. The FGA is formed after relatively long cycles (with extremely slow crack growth rate). The facets around the rough zone are evidence of crack propagation along the grain slip plane. Although the size of the pore is small, the localized high stresses it induces are sufficient to promote
Fig. 8. TEM, SAED and EDS images of FIB-sample-A: (a) matrix, (b) fine grain, (c) twin and (d) the junction between the fine grain area and the matrix.
Fig. 9. (a) IPF, (b) GB (c) GND maps of FIB-sample-B taken from Specimen III through FIB technology. (d) PF map of fine grains. (e) Statistical distribution of SFs for FIB-sample-B.

dislocation slip, generation and annihilation, and ultimately lead to the creation of micro-cracks.

Surface flaws generally have sharp edges, which have a tendency to induce a local concentration of stress at the tips of the sharp edges. Consequently, this form of defect proves more deleterious to the fatigue properties of AM materials compared to gas pore-type defects. According to the relationship developed by Murakami [45], fatigue limit,  $ \sigma_{w} $, defined as the threshold stress preventing the propagation of a crack originating from an initial defect, can be evaluated using the following equations:

Surface defect:

 $$ \sigma_{sur-w}=\frac{1.43(HV+120)}{\left(\sqrt{area_{eff}}\right)^{\frac{1}{6}}} $$ 

Interior defect:

 $$ \sigma_{int-w}=\frac{1.56(HV+120)}{\left(\sqrt{area_{eff}}\right)^{\frac{1}{6}}} $$ 

where  $ \sigma_{sur-w} $ is fatigue limit corresponding to fatigue failure caused by surface defect, while  $ \sigma_{int-w} $ corresponds to interior defect; 1.43 and 1.56 are factors corresponding to different defect location; HV is Vickers hardness of material;  $ \sqrt{area_{eff}} $ is effective area of the square root of the projection of the defect onto the plane perpendicular to the loading direction. The effective area estimation method for irregularly shaped cracks are summarized in Fig. 12a. For surface flaw initiation, effective area refers to effective size of surface flaw, while for internal pore initiation, effective area refers to the size of rough area (RA).

Surface defects with a high degree of irregularity are very detrimental to the fatigue life of the test specimen. However, specimens with internal defect initiation showed very high regularity of porosity. HV takes 452 kgf·mm $ ^{-2} $ here. The measured defect size, experimental stress amplitude, calculated fatigue limit are shown in Table 5. In the fracture mechanics point of view, fatigue strengths with small defects are frequently reviewed by the parameter,  $ \sigma_{a}/\sigma_{w} $, where  $ \sigma_{a} $ corresponds to experimental stress amplitude,  $ \sigma_{w} $ corresponds to calculated fatigue limit. The modified S-N data is presented in Fig. 12b. It can be seen that in most cases, experimental stress amplitude is greater than the calculated fatigue limit value, that is to say, in such experimental stress amplitude, the fatigue crack can grow. For Specimen I, the value of  $ \sigma_{sur-w} $ is evaluated to be about 504.60 MPa by surface flaw, compared with the experimental stress amplitude of 533.95 MPa, while for Specimen II, the value of  $ \sigma_{int-w} $ is evaluated to be about 499.59 MPa by RA, compared with the experimental stress amplitude of 536.78 MPa. As for Specimen III,  $ \sigma_{int-w} $ is calculated to be 485.38 MPa using the size of pore cluster, with the experimental stress amplitude of 508.53 MPa. Upon
Fig. 10. (a) TEM BF image of FIB-sample-B taken from Specimen III ( $ \sigma_a = 508.5 \text{MPa}, N_f = 1.73 \times 10^8 $). Higher magnification of (b) lamellar substructure, (c) facet, (d) fine grain area, (e) TEM BF and SAED images of typical fine grain (f) TEM DF image corresponding to (e).

analyzing and calculating all fatigue failure samples, it was observed that predictions made by the  $ \sqrt{area} $ parameter model exhibit an error within approximately 10% when estimating the fatigue limit. With the increase in fatigue life, this parameter gradually decreases. What’s more, this relationship does not consider the influence of defect irregularities. For internal pore induced fatigue failure, the gas pore is very regular, thus the predicted results without considering defect irregularities are more precise than surface flaw initiation.

If the experimental stress amplitude is greater than the calculated fatigue limit shows that with the observed fatal defect as the initial crack, the crack will propagate under the experimental stress amplitude. At higher stress amplitudes, the stress amplitude is greater than the calculated surface stress limit, and the surface flaw becomes the fatigue source. However, when the stress amplitude is reduced, the surface flaw does not have enough driving force to grow, so the crack initiation may start from internal micro-defects. This is to understand the competition mechanism from the perspective of fatigue limit. From the environmental perspective, in the case of surface flaw initiation, the speed of cracks growing is faster in the air and the corresponding fatigue life will be shorter; while in the case of internal pore initiation, the cracks will expand slower in vacuum and the corresponding fatigue life will be longer. That is one of the reasons why the fatigue life of specimens with surface flaw initiation is generally shorter than that of specimens with internal pore initiation.

## 4.2. Fine grain formation mechanism

Several studies have investigated the mechanism behind the formation of fine grains in the FIA during the VHCF process. For high-strength steels, Hong et al. [31] suggested a formation mechanism for FGA: the occurrence of numerous cyclic pressings (NCP) between the surfaces of the originated crack leads to grain refinement along the crack propagation path, thereby resulting in the formation of FGA. According to the observation in Fig. 6(a), parallel TBs are predominant near the pore, and TBs parallel to the slip surface are also present inside the large grain, indicating that lattice slip has occurred. In addition, the distribution of fine crystals is not uniform, and there are coarse and fine grains doping distribution. This phenomenon cannot be well explained by the NCP mechanism. It’s more inclined to think that the nanograin formation in fine granular area (FGA) is due to the dislocation interaction caused by the locally high strain during the cyclic loading. The nanograins cause the crack initiation, and then the formed crack induces the further nanograin formation and crack formation, and finally the FGA forms.

Furthermore, the LAGBs, primarily formed within regions of high dislocation density, were identified in large grains, signifying the occurrence of dynamic recovery (DRV). Additionally, the presence of equiaxed fine grains with low internal dislocation density suggests the onset of dynamic recrystallization (DRX). The crucial factor in discerning the DRX mechanism lies in determining whether the newly formed HAGBs, subsequent to severe plastic deformation, originate from LAGBs, micro-shear/deformation bands, or primitive HAGBs. The fundamental concept behind continuous dynamic recrystallization (CDRX) involves the gradual transformation of LAGBs into HAGBs following the creation of dislocation sub-boundaries with low misorientations. This transformation occurs due to the increased density of dislocations trapped by the sub-boundaries during the deformation process. The new grains featuring HAGBs may have formed through severe deformation characterized by the progressive rotation of subgrains. Within the highlighted regions in the white boxes of Fig. 6a and Fig. 9a, fragments of HAGBs are observed, connecting to dense LAGBs. This observation suggests that the HAGBs underwent transformation from the LAGBs. After this procedure, the occurrence of CDRX was noted. This is the typical feature of CDRX. The occurrence of discontinuous dynamic recrystallization (DDRX) generally requires higher temperatures, and since we used compressed air for cooling in the fatigue tests, the temperature rise effect was not considered for the time being, and the DDRX phenomenon was not considered either. No necklace structure of recrystallized grains and equiaxed grains were
Fig. 11. TEM, SAED and EDS images of FIB-sample-B: (a) lamellar, (b) the junction between the fine grain area and the matrix, (c) fine grain area near to facet and (d) facet.
Fig. 12. (a) Summary of the effective area estimation methods for irregularly shaped cracks during surface and interior crack initiation [8], (b) Modified S-N data:  $ \sigma_{a}/\sigma_{w} $ vs  $ N_{f} $, where  $ \sigma_{a} $ corresponds to experimental stress amplitude,  $ \sigma_{w} $ corresponds to calculated fatigue limit.

Table 5

Stress-life data and measured defect size for all failure specimens.

<table border="1" style="margin: auto; word-wrap: break-word;"><tr><td style="text-align: center; word-wrap: break-word;">Crack initiation location</td><td style="text-align: center; word-wrap: break-word;">Specimen number</td><td style="text-align: center; word-wrap: break-word;">Fatigue life [cycle]</td><td style="text-align: center; word-wrap: break-word;">Experimental stress amplitude [MPa]</td><td style="text-align: center; word-wrap: break-word;">Calculated fatigue limit [MPa]</td><td style="text-align: center; word-wrap: break-word;">Defect size [ $ \mu $m $ ^{2} $]</td></tr><tr><td rowspan="5">Surface</td><td style="text-align: center; word-wrap: break-word;">1</td><td style="text-align: center; word-wrap: break-word;">$ 1.68 \times 10^{6} $</td><td style="text-align: center; word-wrap: break-word;">536.78</td><td style="text-align: center; word-wrap: break-word;">492.32</td><td style="text-align: center; word-wrap: break-word;">442.38</td></tr><tr><td style="text-align: center; word-wrap: break-word;">3</td><td style="text-align: center; word-wrap: break-word;">$ 3.28 \times 10^{6} $</td><td style="text-align: center; word-wrap: break-word;">539.60</td><td style="text-align: center; word-wrap: break-word;">486.59</td><td style="text-align: center; word-wrap: break-word;">509.18</td></tr><tr><td style="text-align: center; word-wrap: break-word;">4</td><td style="text-align: center; word-wrap: break-word;">$ 2.18 \times 10^{6} $</td><td style="text-align: center; word-wrap: break-word;">533.95</td><td style="text-align: center; word-wrap: break-word;">504.60</td><td style="text-align: center; word-wrap: break-word;">329.19</td></tr><tr><td style="text-align: center; word-wrap: break-word;">6</td><td style="text-align: center; word-wrap: break-word;">$ 3.94 \times 10^{6} $</td><td style="text-align: center; word-wrap: break-word;">550.90</td><td style="text-align: center; word-wrap: break-word;">493.21</td><td style="text-align: center; word-wrap: break-word;">432.91</td></tr><tr><td style="text-align: center; word-wrap: break-word;">7</td><td style="text-align: center; word-wrap: break-word;">$ 3.25 \times 10^{6} $</td><td style="text-align: center; word-wrap: break-word;">570.69</td><td style="text-align: center; word-wrap: break-word;">490.48</td><td style="text-align: center; word-wrap: break-word;">462.75</td></tr><tr><td rowspan="6">Interior</td><td style="text-align: center; word-wrap: break-word;">8</td><td style="text-align: center; word-wrap: break-word;">$ 2.89 \times 10^{6} $</td><td style="text-align: center; word-wrap: break-word;">590.45</td><td style="text-align: center; word-wrap: break-word;">513.44</td><td style="text-align: center; word-wrap: break-word;">267.24</td></tr><tr><td style="text-align: center; word-wrap: break-word;">2</td><td style="text-align: center; word-wrap: break-word;">$ 4.50 \times 10^{7} $</td><td style="text-align: center; word-wrap: break-word;">536.78</td><td style="text-align: center; word-wrap: break-word;">499.59</td><td style="text-align: center; word-wrap: break-word;">1053.98</td></tr><tr><td style="text-align: center; word-wrap: break-word;">5</td><td style="text-align: center; word-wrap: break-word;">$ 1.48 \times 10^{7} $</td><td style="text-align: center; word-wrap: break-word;">528.30</td><td style="text-align: center; word-wrap: break-word;">521.16</td><td style="text-align: center; word-wrap: break-word;">634.81</td></tr><tr><td style="text-align: center; word-wrap: break-word;">9</td><td style="text-align: center; word-wrap: break-word;">$ 9.63 \times 10^{6} $</td><td style="text-align: center; word-wrap: break-word;">519.53</td><td style="text-align: center; word-wrap: break-word;">499.59</td><td style="text-align: center; word-wrap: break-word;">1054.18</td></tr><tr><td style="text-align: center; word-wrap: break-word;">10</td><td style="text-align: center; word-wrap: break-word;">$ 1.73 \times 10^{8} $</td><td style="text-align: center; word-wrap: break-word;">508.53</td><td style="text-align: center; word-wrap: break-word;">485.38</td><td style="text-align: center; word-wrap: break-word;">1490.17</td></tr><tr><td style="text-align: center; word-wrap: break-word;">11</td><td style="text-align: center; word-wrap: break-word;">$ 1.39 \times 10^{7} $</td><td style="text-align: center; word-wrap: break-word;">502.88</td><td style="text-align: center; word-wrap: break-word;">502.23</td><td style="text-align: center; word-wrap: break-word;">989.61</td></tr></table>

found at the grain boundaries, proving that no DDRX occurred.

Based on the observation in Fig. 8c and d that both the twins and the neighboring matrix have been elementally homogenized and the elemental demarcation line is closer to the matrix than the structural demarcation line, it is hypothesized that the precipitates dissolution and the elemental homogenization occur prior to TBs formation and grain refinement. There are some studies on the dissolution of precipitated phases during fatigue. Xiao et al. [24,46] uncovered that fatigue at room temperature in Inconel 718 led to the shearing of coherent and ordered  $ \gamma' $ and  $ \gamma'' $ precipitates by paired dislocations. As can be seen from the HAADF image in Fig. 8d2 and BF image in Fig. 8d3, the dissolution zone of the precipitates on the left side of the dividing line has relatively more dislocations, while the recrystallization zone on the right side has relatively few dislocations. This shows that dislocations interact with the precipitates during precipitation and dissolution, and the dislocation density increases, while dislocations are consumed during the recrystallization process. This phenomenon confirms our analysis of dislocation and precipitates behavior. The interactions between dislocations and precipitates will induce high local stress, which will trigger the formation of TBs. The SFE of GH4169 superalloy can be roughly estimated to 50 mJ/m $ ^{2} $ [47]. Accompanying the dissolution of the precipitated phase, local softening and increasement of SFE will occur. The critical stress for twinning ( $ \sigma_{t} $) can be estimated using a mean-field model [48]

 $$ \sigma_{t}=M\left(\frac{\Gamma}{b}+\frac{Gb}{D}\right) $$ 

where M represents the Taylor factor for a randomly textured polycrystal (M = 3.06 based on the Taylor model and M = 2.7 based on the crystal plasticity finite element model [49]),  $ \Gamma $ denotes the SFE (50 mJ/m $ ^{2} $), G stands for the polycrystal shear modulus (77.2 GPa) [50], b represents the magnitude of the Burgers vector of the partial dislocation (0.147 nm) [51,52], and D is the grain size (17.64  $ \mu $m). Upon computation, the critical twinning stress is approximately within the range of 0.97–1.10 GPa. The dissolution of precipitates leads to an increase in SFE, resulting in local stress levels higher than the calculated values. This elevated local stress can be attributed to stress concentration around the pore and hardening induced by dislocation interactions.

Elevated local stress and deformation incompatibility drive additional dislocation movement, fostering the formation of dislocation cells or walls. The formation of sub-grain boundaries will lead to local hardening, and the microstructural inhomogeneity promote the CDRX process. This may explain the staggered distribution of fine grains and twins in the Fig. 6a. The rearrangement of dislocations tends to establish a lower-energy configuration, specifically a cellular structure or sub-grain featuring alternating high and low density dislocation regions. The formation of nanograins induces local hardening and augments microstructural inhomogeneity in specific regions, thereby fostering crack initiation and early growth.

In comparison to the distinct fine grain layer proximate to the fatigue initiation pore in Specimen-II, Specimen-III exhibits a limited presence of fine grains at the boundary of the porous FIA. The fine grains in Specimen-III are primarily concentrated at the grain boundaries, with lamellar sub-grains observed within the facets of the FIA. Notably, there is an absence of grain refinement on the facets outside the FIA. This disparity can be attributed to the gradual expansion of cracks in the FIA, allowing ample time for dislocations to move and thereby inducing significant local plastic deformation. In contrast, cracks propagate rapidly across the facets outside the FIA, resulting in insufficient local plastic deformation to complete the grain refinement process.

Summarizing the aforementioned observations, the mechanism for fine grain formation and crack initiation in LPBF GH4169 under the VHCF regime is outlined below and the schematic diagram is presented in Fig. 13: (I) When the specimen is subjected to prolonged cyclic deformation, mobile dislocations move, shear the  $ \gamma' $ and  $ \gamma'' $ precipitates, cause the precipitates to dissolve and the elements to be uniformly distributed progressively. Simultaneously, the local high stress due to deformation incompatibility and interactions between dislocations and precipitates causes formation of TBs. (II) As cyclic loading proceeds, a high density of dislocations exhibits reciprocating movement within a defined range, leading to dislocation rearrangement. This
Fig. 13. The mechanism for fine grain formation and crack initiation of LPBF GH4169 in VHCF regime. (a) Initial state. (b) Paired dislocations shear the  $ \gamma' $ and  $ \gamma'' $ precipitates. (c) Precipitates dissolve. (d) Dislocations re-arrangement forms parallel TBs and cellular structure or sub-grains. (e) Grains rotate, LAGBs transform into HAGBs. (f) Micro crack forms along the boundaries between the nanograins and matrix or within nanograins.

rearrangement tends to create a lower-energy configuration, forming either a cellular or sub-granular structure. Dislocations with the same sign accumulate into dislocation walls and transform into LAGBs. Microstructural inhomogeneity promotes the newly formed sub-grains to rotate to form HAGBs. (III) Fine grains develop, and micro-cracks emerge along the boundaries between nanograins and the matrix, or within nanograins. These cracks progressively propagate, ultimately resulting in fatigue failure of the specimen.

## 5. Conclusions

In this study, we investigated the fatigue failure mechanism of LPBF GH4169 superalloy and fine grain formation mechanism in FIA by performing fatigue tests and multi-scale characterization techniques. This work uncovers the mechanism and role of precipitation dissolution promoting the formation of TBs and fine grains during VHCF process of LPBF GH4169 superalloy for the first time. This will enhance the understanding of fatigue crack initiation mechanism and have the significance for improving the fatigue properties of LPBF GH4169 superalloy. The main conclusions from the obtained results can be summarized as follows:

(1) There are cellular and lamellar substructures with strengthening  $ \gamma' $ and  $ \gamma'' $ precipitates in the grain,  $ \delta $ phase and carbide at the grain boundary for solid solution and double aging post-processing LPBF GH4169. Moreover, samples have extremely low porosity, and the internal defects have small size and regular shape.

(2) The LPBF GH4169 superalloy exhibits two competing fatigue crack initiation modes: surface flaw initiation associated with high cycle fatigue life and internal pore initiation corresponding to very high cycle fatigue life.

(3) Under sufficient cyclic loading, the stress concentration caused by internal defects causes dislocations to move and repeatedly shear the  $ \gamma' $ and  $ \gamma'' $ precipitates, resulting in dissolution of the precipitates and local high stress. The accumulation and annihilation of dislocations promote the formation of sub-grains and twins. As LAGBs become HAGBs, the grains are further refined. Ultimately, microcracks initiate either within the fine-grained layer or at the interface between the fine-grained layer and the matrix.

(4) Under cyclic tensile and compressive loading, cracks in the FIA expand slowly, and dislocations have sufficient time to move, accumulate and annihilate. The accumulation of dislocations leads to large local plastic deformation, promotes the occurrence of CDRX, and forms fine grains; while when the crack extends outside the FIA, it propagates along the slip surface at a fast speed to form facets, and it is difficult to accumulate large plastic deformation, which is necessary for the grain refinement process.

## CRediT Authorship

Zhigang Yang: Writing – review & editing, Validation, Formal analysis. Jiayi Yan: Writing – review & editing, Validation, Formal analysis. Guian Qian: Writing – review & editing, Supervision, Resources, Methodology, Funding acquisition, Conceptualization. Tao Shi: Writing – original draft, Visualization, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. Jianghua Li: Methodology, Investigation, Data curation. Guhui Gao: Writing – review & editing, Supervision, Formal analysis, Conceptualization. Jingyu Sun: Methodology, Formal analysis, Conceptualization.

## Declaration of Competing Interest

We hereby declare that there is no conflict of interest. This paper (or closely related research) has not been published or accepted for publication. It is not under consideration at another journal.

## Data Availability

Data will be made available on request.

## Acknowledgements

This work was supported by the National Natural Science Foundation of China (Fund nos. 12072345, 11932020, 12202444, 12272377), International Partnership Program for Grand Challenges of Chinese Academy of Sciences (025GJHZ2023092GC) and Science Center for Gas Turbine Project (P2022-B-III-008-001).

## References

[1] Z. Qin, B. Li, C. Chen, T. Chen, R. Chen, H. Zhang, H. Xue, C. Yao, L. Tan, Crack initiation mechanisms and life prediction of GH4169 superalloy in the high cycle and very high cycle fatigue regime, J. Mater. Res. Technol. 26 (2023) 720–736, https://doi.org/10.1016/j.jmrt.2023.07.196.

[2] E. Sadeghi, P. Karimi, R. Esmaeilizadeh, F. Berto, S. Shao, J. Moverare, E. Toyserkani, N. Shamsaei, A state-of-the-art review on fatigue performance of powder bed fusion-built alloy 718, Prog. Mater. Sci. 133 (2023) 101066, https://doi.org/10.1016/j.pmatsci.2022.101066.

[3] C. Panwisawas, Y.T. Tang, R.C. Reed, Metal 3D printing as a disruptive technology for superalloys, Nat. Commun. 11 (2020) 2327, https://doi.org/10.1038/s41467-020-16188-7.

[4] A. Mostafaei, R. Ghiaasiaan, I.-T. Ho, S. Strayer, K.-C. Chang, N. Shamsaei, S. Shao, S. Paul, A.-C. Yeh, S. Tin, A.C. To, Additive manufacturing of nickel-based superalloys: a state-of-the-art review on process-structure-defect-property relationship, Prog. Mater. Sci. 136 (2023) 101108, https://doi.org/10.1016/j.pmatsci.2023.101108.

[5] D. Herzog, V. Seyda, E. Wycisk, C. Emmelmann, Additive manufacturing of metals, Acta Mater. 117 (2016) 371–392, https://doi.org/10.1016/j.actamat.2016.07.019.

[6] T.H. Becker, P. Kumar, U. Ramamurty, Fracture and fatigue in additively manufactured metals, Acta Mater. 219 (2021) 117240, https://doi.org/10.1016/j.actamat.2021.117240.

[7] P.D. Nezhadfar, A.S. Johnson, N. Shamsaei, Fatigue behavior and microstructural evolution of additively manufactured Inconel 718 under cyclic loading at elevated temperature, Int. J. Fatigue 136 (2020) 105598, https://doi.org/10.1016/j.ijfatigue.2020.105598.

[8] Y. Yamashita, T. Murakami, R. Mihara, M. Okada, Y. Murakami, Defect analysis and fatigue design basis for ni-based superalloy 718 manufactured by additive manufacturing, Procedia Struct. Integr. 7 (2017) 11–18, https://doi.org/10.1016/j.prostr.2017.11.054.

[9] P. Kanagarajah, F. Brenne, T. Niendorf, H.J. Maier, Inconel 939 processed by selective laser melting: effect of microstructure and temperature on the mechanical properties under static and cyclic loading, Mater. Sci. Eng., A 588 (2013) 188–195, https://doi.org/10.1016/j.msea.2013.09.025.

[10] E. Hosseini, V.A. Popovich, A review of mechanical properties of additively manufactured Inconel 718, Addit. Manuf. 30 (2019) 100877, https://doi.org/10.1016/j.addma.2019.100877.

[11] A. Kaletsch, S. Qin, S. Herzog, C. Broeckmann, Influence of high initial porosity introduced by laser powder bed fusion on the fatigue strength of Inconel 718 after post-processing with hot isostatic pressing, Addit. Manuf. 47 (2021) 102331, https://doi.org/10.1016/j.addma.2021.102331.

[12] K.S. Stopka, A. Desrosiers, T. Nicodemus, N. Krutz, A. Andreaco, M.D. Sangid, Intentionally seeding pores in additively manufactured alloy 718: process parameters, microstructure, defects, and fatigue, Addit. Manuf. 66 (2023) 103450, https://doi.org/10.1016/j.addma.2023.103450.

[13] E. Sadeghi, P. Karimi, N. Israelsson, J. Shipley, T. Månsson, T. Hansson, Inclusion-induced fatigue crack initiation in powder bed fusion of alloy 718, Addit. Manuf. 36 (2020) 101670, https://doi.org/10.1016/j.addma.2020.101670.

[14] M. Prost, A. Köster, D. Missoum-Benziane, S. Dépinoy, L. Ferhat, M. Rambaudon, V. Maurel, Anisotropy in cyclic behavior and fatigue crack growth of IN718 processed by laser powder bed fusion, Addit. Manuf. 61 (2023) 103301, https://doi.org/10.1016/j.addma.2022.103301.

[15] J.-R. Poulin, A. Kreitcberg, V. Brailovski, Effect of hot isostatic pressing of laser powder bed fused Inconel 625 with purposely induced defects on the residual porosity and fatigue crack propagation behavior, Addit. Manuf. 47 (2021) 102324, https://doi.org/10.1016/j.addma.2021.102324.

[16] K. Yang, Q. Huang, Q. Wang, Q. Chen, Competing crack initiation behaviors of a laser additively manufactured nickel-based superalloy in high and very high cycle fatigue regimes, Int. J. Fatigue 136 (2020) 105580, https://doi.org/10.1016/j.ijfatigue.2020.105580.

[17] Y. Murakami, M. Endo, Effects of defects, inclusions and inhomogeneities on fatigue strength, Int. J. Fatigue 16 (1994) 163–182, https://doi.org/10.1016/0142-1123(94)90001-9.

[18] C. Yu, Z. Huang, Z. Zhang, J. Shen, J. Wang, Z. Xu, Influence of post-processing on very high cycle fatigue resistance of Inconel 718 obtained with laser powder bed fusion, Int. J. Fatigue 153 (2021) 106510, https://doi.org/10.1016/j.ijfatigue.2021.106510.

[19] L. Sheridan, O.E. Scott-Emuakpor, T. George, J.E. Gockel, Relating porosity to fatigue failure in additively manufactured alloy 718, Mater. Sci. Eng., A 727 (2018) 170–176, https://doi.org/10.1016/j.msea.2018.04.075.

[20] R. Lawitzki, S. Hassan, L. Karge, J. Wagner, D. Wang, J. Von Kobylinski, C. Krempaszky, M. Hofmann, R. Gilles, G. Schmitz, Differentiation of  $ \gamma' $- and  $ \gamma'' $-precipitates in Inconel 718 by a complementary study with small-angle neutron scattering and analytical microscopy, Acta Mater. 163 (2019) 28–39, https://doi.org/10.1016/j.actamat.2018.10.014.

[21] H. Sriram, S. Mukhopadhyay, K. Kadirvel, R. Shi, M.J. Mills, Y. Wang, Formation mechanisms of coprecipitates in Inconel 718 Superalloys, Acta Mater. 249 (2023) 118825, https://doi.org/10.1016/j.actamat.2023.118825.

[22] D.T. Ardi, L. Guowei, N. Maharjan, B. Mutiargo, S.H. Leng, R. Srinivasan, Effects of post-processing route on fatigue performance of laser powder bed fusion Inconel 718, Addit. Manuf. 36 (2020) 101442, https://doi.org/10.1016/j.addma.2020.101442.

[23] F. Theska, K. Nomoto, F. Godor, B. Oberwinkler, A. Stanojevic, S.P. Ringer, S. Primig, On the early stages of precipitation during direct ageing of Alloy 718, Acta Mater. 188 (2020) 492–503, https://doi.org/10.1016/j.actamat.2020.02.034.

[24] L. Xiao, D.L. Chen, M.C. Chaturvedi, Cyclic deformation mechanisms of precipitation-hardened Inconel 718 superalloy, Mater. Sci. Eng., A 483–484 (2008) 369–372, https://doi.org/10.1016/j.msea.2006.10.181.

[25] A.R. Balachandramurthi, J. Moverare, T. Hansson, R. Pederson, Anisotropic fatigue properties of Alloy 718 manufactured by Electron Beam Powder Bed Fusion, Int. J. Fatigue 141 (2020) 105898, https://doi.org/10.1016/j.ijfatigue.2020.105898.

[26] M.E. Aydinöz, F. Brenne, M. Schaper, C. Schaak, W. Tillmann, J. Nellesen, T. Niendorf, On the microstructural and mechanical properties of post-treated additively manufactured Inconel 718 superalloy under quasi-static and cyclic loading, Mater. Sci. Eng., A 669 (2016) 246–258, https://doi.org/10.1016/j.msea.2016.05.089.

[27] H. Choi, S. Kim, M. Goto, S. Kim, Effect of powder recycling on room and elevated temperature damage tolerability of Inconel 718 alloy fabricated by laser powder bed fusion, Mater. Charact. 171 (2021) 110818, https://doi.org/10.1016/j.matchar.2020.110818.

[28] Y. Hong, C. Sun, The nature and the mechanism of crack initiation and early growth for very-high-cycle fatigue of metallic materials – An overview, Theor. Appl. Fract. Mech. 92 (2017) 331–350, https://doi.org/10.1016/j.tafmec.2017.05.002.

[29] Y. Hong, Z. Lei, C. Sun, A. Zhao, Propensities of crack interior initiation and early growth for very-high-cycle fatigue of high strength steels, Int. J. Fatigue 58 (2014) 144–151, https://doi.org/10.1016/j.ijfatigue.2013.02.023.

[30] T. Sakai, N. Oguma, A. Morikawa, Microscopic and nanoscopic observations of metallurgical structures around inclusions at interior crack initiation site for a bearing steel in very high-cycle fatigue, Fatigue Fract. Eng. Mat. Struct. 38 (2015) 1305–1314, https://doi.org/10.1111/ffe.12344.

[31] Y. Hong, X. Liu, Z. Lei, C. Sun, The formation mechanism of characteristic region at crack initiation for very-high-cycle fatigue of high-strength steels, Int. J. Fatigue 89 (2016) 108–118, https://doi.org/10.1016/j.ijfatigue.2015.11.029.

[32] M. Awd, S. Siddique, J. Johannsen, C. Emmelmann, F. Walther, Very high-cycle fatigue properties and microstructural damage mechanisms of selective laser melted AlSi10Mg alloy, Int. J. Fatigue 124 (2019) 55–69, https://doi.org/10.1016/j.ijfatigue.2019.02.040.

[33] G. Qian, Z. Jian, Y. Qian, X. Pan, X. Ma, Y. Hong, Very-high-cycle fatigue behavior of AlSi10Mg manufactured by selective laser melting: effect of build orientation and mean stress, Int. J. Fatigue 138 (2020) 105696, https://doi.org/10.1016/j.ijfatigue.2020.105696.

[34] A. Du Plessis, S. Beretta, Killer notches: The effect of as-built surface roughness on fatigue failure in AlSi10Mg produced by laser powder bed fusion, Addit. Manuf. 35 (2020) 101424, https://doi.org/10.1016/j.addma.2020.101424.

[35] G. Brot, I. Koutiri, V. Bonnand, V. Favier, C. Dupuy, N. Ranc, P. Aimedieu, F. Lefebvre, R. Hauteville, Microstructure and defect sensitivities in the very high-cycle fatigue response of Laser Powder Bed Fused Ti–6Al–4V, Int. J. Fatigue 174 (2023) 107710, https://doi.org/10.1016/j.ijfatigue.2023.107710.

[36] C. Lavogiez, C. Dureau, Y. Nadot, P. Villechaise, S. Hémery, Crack initiation mechanisms in Ti-6Al-4V subjected to cold dwell-fatigue, low-cycle fatigue and high-cycle fatigue loadings, Acta Mater. 244 (2023) 118560, https://doi.org/10.1016/j.actamat.2022.118560.

[37] P. Kumar, U. Ramamurty, High cycle fatigue in selective laser melted Ti-6Al-4V, Acta Mater. 194 (2020) 305–320, https://doi.org/10.1016/j.actamat.2020.05.041.

[38] Z. Qu, Z.J. Zhang, Y.K. Zhu, R. Liu, S.L. Lu, S.J. Li, Q.Q. Duan, B.N. Zhang, M. X. Zhao, J. Eckert, Z.F. Zhang, Coupling effects of microstructure and defects on the fatigue properties of laser powder bed fusion Ti-6Al-4V, Addit. Manuf. 61 (2023) 103355, https://doi.org/10.1016/j.addma.2022.103355.

[39] L. Bhandari, V. Gaur, On study of process induced defects-based fatigue performance of additively manufactured Ti6Al4V alloy, Addit. Manuf. 60 (2022) 103227, https://doi.org/10.1016/j.addma.2022.103227.

[40] Y.-F. Yang, H.-Y. Hu, L. Min, Q.-T. Sun, M. Song, M.-L. Zhu, J.-F. Wen, S.-T. Tu, Failure mechanism and life correlation of Inconel 718 in high and very high cycle fatigue regimes, Int. J. Fatigue 175 (2023) 107764, https://doi.org/10.1016/j.ijfatigue.2023.107764.

[41] D. Texier, J. Cormier, P. Villechaise, J.-C. Stinville, C.J. Torbet, S. Pierret, T. M. Pollock, Crack initiation sensitivity of wrought direct aged alloy 718 in the very high cycle fatigue regime: the role of non-metallic inclusions, Mater. Sci. Eng., A 678 (2016) 122–136, https://doi.org/10.1016/j.msea.2016.09.098.

[42] J. Radhakrishnan, P. Kumar, S. Li, Y. Zhao, U. Ramamurty, Unnotched fatigue of Inconel 718 produced by laser beam-powder bed fusion at 25 and 600^\circC, Acta Mater. 225 (2022) 117565, https://doi.org/10.1016/j.actamat.2021.117565.

[43] S. Park, Y. Tanaka, S. Okazaki, Y. Funakoshi, H. Kawashima, H. Matsunaga, Inferior fatigue resistance of additively-manufactured Ni-based superalloy 718 and its dominating factor, Int. J. Fatigue 176 (2023) 107801, https://doi.org/10.1016/j.ijfatigue.2023.107801.

[44] J.C. Stinville, E. Martin, M. Karadge, S. Ismonov, M. Soare, T. Hanlon, S. Sundaram, M.P. Echlin, P.G. Callahan, W.C. Lenthe, V.M. Miller, J. Miao, A. E. Wessman, R. Finlay, A. Loghin, J. Marte, T.M. Pollock, Fatigue deformation in a polycrystalline nickel base superalloy at intermediate and high temperature: Competing failure modes, Acta Mater. 152 (2018) 16–33, https://doi.org/10.1016/j.actamat.2018.03.035.

[45] Y. Murakam, T. Nomoto, T. Ueda, Factors influencing the mechanism of superlong fatigue failure in steels: superlong fatigue failure in steels, Fatigue Fract. Eng. Mat. Struct. 22 (1999) 581–590, https://doi.org/10.1046/j.1460-2695.1999.00187.x.

[46] L. Xiao, D.L. Chen, M.C. Chaturvedi, Shearing of  $ \gamma^{\prime\prime} $ precipitates and formation of planar slip bands in Inconel 718 during cyclic deformation, Scr. Mater. 52 (2005) 603–607, https://doi.org/10.1016/j.scriptamat.2004.11.023.

[47] D. Fournier, A. Pineau, Low cycle fatigue behavior of inconel 718 at 298 K and 823 K, Metall. Trans., A 8 (1977) 1095–1105, https://doi.org/10.1007/BF02667395.

[48] Z. Wang, W. Lu, F. An, M. Song, D. Ponge, D. Raabe, Z. Li, High stress twinning in a compositionally complex steel of very high stacking fault energy, Nat. Commun. 13 (2022) 3598, https://doi.org/10.1038/s41467-022-31315-2.

[49] Y. Tadano, M. Kuroda, H. Noguchi, Quantitative re-examination of Taylor model for FCC polycrystals, Comp. Mater. Sci. 51 (2012) 290–302, https://doi.org/10.1016/j.commatsci.2011.07.024.

[50] V.P. Sabelkin, G.R. Cobb, B.M. Doane, R.A. Kemnitz, R.P. O'Hara, Torsional behavior of additively manufactured nickel alloy 718 under monotonic loading and low cycle fatigue, Mater. Today Commun. 24 (2020) 101256, https://doi.org/10.1016/j.mtcomm.2020.101256.

[51] S. Mahajan, Formation of annealing twins in f.c.c. crystals, Acta Mater. 45 (1997) 2633–2638, https://doi.org/10.1016/S1359-6454(96)00336-9.

[52] Y. Chen, B. Li, B. Chen, F. Xuan, High-cycle fatigue induced twinning in CoCrFeNi high-entropy alloy processed by laser powder bed fusion additive manufacturing, Addit. Manuf. 61 (2023) 103319, https://doi.org/10.1016/j.addma.2022.103319.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

Additive Manufacturing 85 (2024) 104151

Additive Manufacturing

## Keywords
Microstructure
Competitive fatigue failure mechanism
Laser powder bed fusion (LPBF)
Grain refinement
Precipitate dissolution
## ABSTRACT
## CRediT Authorship
## Data Availability

## ABSTRACT

https://doi.org/10.1016/j.addma.2024.104151 2214-8604/© 2024 Elsevier B.V. All rights reserved. [42] J. Radhakrishnan, P. Kumar, S. Li, Y. Zhao, U. Ramamurty, Unnotched fatigue of Inconel 718 produced by laser beam-powder bed fusion at 25 and 600^\circC, Acta Mater. 225 (2022) 117565, https://doi.org/10.1016/j.actamat.2021.117565.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

ELSEVIER

Contents lists available at ScienceDirect

journal homepage: www.elsevier.com/locate/addma

Keywords:
Microstructure
Competitive fatigue failure mechanism
Laser powder bed fusion (LPBF)
Grain refinement
Precipitate dissolution

A B S T R A C T

* Corresponding author at: State Key Laboratory of Nonlinear Mechanics (LNM), Institute of Mechanics, Chinese Academy of Sciences, Beijing 100190, China. E-mail address: qianguian@imech.ac.cn (G. Qian).

Received 14 January 2024; Received in revised form 9 April 2024; Accepted 19 April 2024

Available online 22 April 2024

T. Shi et al.

CRediT authorship contribution statement

Data availability

[42] J. Radhakrishnan, P. Kumar, S. Li, Y. Zhao, U. Ramamurty, Unnotched fatigue of Inconel 718 produced by laser beam-powder bed fusion at 25 and 600°C, Acta Mater. 225 (2022) 117565, https://doi.org/10.1016/j.actamat.2021.117565.