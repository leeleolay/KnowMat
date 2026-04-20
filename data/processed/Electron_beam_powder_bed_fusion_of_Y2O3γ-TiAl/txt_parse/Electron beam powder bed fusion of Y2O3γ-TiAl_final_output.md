DOI: 10.1016/j.addma.2023.103650

# Electron beam powder bed fusion of Y₂O₃/\gamma-TiAl nanocomposite with balanced strength and toughness

B. Gao $ ^{a} $, H. Peng $ ^{b,*} $, H. Yue $ ^{c} $, H. Guo $ ^{a} $, C. Wang $ ^{d} $, B. Chen $ ^{e,*} $

 $ ^{a} $ School of Materials Science and Engineering, Beihang University, Beijing 100191, China

 $ ^{b} $ Research Institute for Frontier Science, Beihang University, Beijing 100191, China

 $ ^{c} $ School of Materials Science and Engineering, Jiangsu University of Science and Technology, Zhenjiang 212003, China

 $ ^{d} $ GE Additive Technology (China) Co., LTD, Beijing 100040, China

 $ ^{e} $ School of Engineering, University of Leicester, Leicester LE1 7RH, UK

## ARTICLE INFO

## Keywords

Gamma-TiAl

Additive manufacturing

Electron beam powder bed fusion

Microstructure

Mechanical properties

## Abstract

This paper reports the use of multi-spot melt strategy coupled with smaller layer thickness to additively manufacture Y₂O₃/\gamma-TiAl nanocomposite. In contrast to the hatch melt, the multi-spot melt strategy results in a lower fraction of \gamma and B_{2}-phase, a smaller lamellar spacing of 208 \pm 72 nm with straight interface between \alpha₂/\gamma, and a uniformly distributed nanoparticles with a finer size of 90 \pm 38 nm. Twins can form in the equiaxed \gamma grains and within \gamma lamellae; this applies to both the multi-spot and hatch melt samples. Twins within the \gamma lamellae can propagate across the twin interface but terminate at the \gamma/\alpha₂ interface. A good combination of 556 \pm 11 MPa (tensile strength) and 17.0 \pm 3.1 % (ductility) at 800 ^\circC with 16.5 \pm 0.3 MPa\sqrtm (room-temperature fracture toughness) is achieved in the as-built condition. Quantitative microscopy confirms a homogeneous microstructure within the x-y plane for the multi-spot sample, whilst the use of smaller layer thickness helps to reduce the microstructure degradation due to thermal cycling. In terms of the Y₂O₃ nanoparticles, both the rod-like Y₂O₃ with monoclinic and the near spherical Y₂O₃ with cubic crystal system are identified using transmission electron microscopy (TEM). High-resolution TEM reveals that the Y₂O₃/TiAl interface is clean, free of interfacial reactions, and with a semi-coherent or coherent type, suggesting a strong bonding.

## 1. Introduction

Electron beam powder bed fusion (PBF-EB) is an effective additive manufacturing method to process  $ \gamma $-TiAl intermetallic compound [1,2]. However, limited progress was made in obtaining a balanced room-temperature fracture toughness ( $ K_{IC} $) and high-temperature strength, which hinders its wider engineering applications. Additionally manufactured oxide-dispersion-strengthened (ODS) alloy is a fast growing area of interest, and certain success has been achieved on material systems such as Ni- [3,4], Fe- [5], Ti- [6], Al-based alloys [7]. Addition of nanoparticles can affect powder sintering behaviour [8,9], reduce cracking susceptibility [4] and contribute to grain refinement [3].

In terms of the TiAl-based nanocomposite, ultimate tensile strength (UTS) of casting  $ Y_{2}O_{3}/TiAl $ increased by 44 % at room temperature and 29 % at 800 ^\circC when compared to the pure alloy, due to the grain refinement, obstruction of dislocation motion and grain boundary pinning by  $ Y_{2}O_{3} $ dispersoids [10]. The ductility increase by 60 % and 74 % was attributed to cross-slip of ordinary 1/2 < 110] dislocations and the removal of interstitial oxygen by Y [11]. However, due to the long melt time,  $ Y_{2}O_{3} $ nanoparticles agglomerated and distributed along the Al segregation, deteriorating high-temperature strength [10]. The yield strength (YS) and UTS of powder metallurgy  $ Y_{2}O_{3}/TiAl $ increased by 34 % and 14 % at room temperature, and the UTS at 800 ^\circC increased by 24 %, but at the sacrifice of the premature sample fracture.

The distinctive features of PBF-EB process including the rapid melt and cooling in vacuum, local melt pool, and high build temperature may help decrease particle agglomeration and limit element segregation. Y₂O₃ is chosen for present PBF-EB TiAl nanocomposite because: (i) its good stability in TiAl melt, owing to its lowest standard free energy for Y₂O₃ formation among other compounds (e.g. Al₂O₃, ZrO₂, MgO₂, SiO₂) [12]; (ii) its similar lattice parameter and coefficient of thermal expansion to TiAl, potentially leading to a strong interface bonding; and (iii) its density of 5 g/cm³ is similar to TiAl of 4 g/cm³, which helps to avoid the slag floating on the melt pool top, potentially causing the

## Nomenclature

<table border="1" style="margin: auto; word-wrap: break-word;"><tr><td style="text-align: center; word-wrap: break-word;">A. Stress</td><td style="text-align: center; word-wrap: break-word;">Yield strength, MPa</td><td style="text-align: center; word-wrap: break-word;">K_{IC}</td><td style="text-align: center; word-wrap: break-word;">Volume fraction of nanoparticles</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \Delta\sigma_{Hall-Pitch} $</td><td style="text-align: center; word-wrap: break-word;">Strength increment by grain boundary strengthening, MPa</td><td style="text-align: center; word-wrap: break-word;">V_{p}</td><td style="text-align: center; word-wrap: break-word;">Volume fraction of nanoparticles</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \Delta\sigma $</td><td style="text-align: center; word-wrap: break-word;">Yield strength increment, MPa</td><td style="text-align: center; word-wrap: break-word;">k</td><td style="text-align: center; word-wrap: break-word;">Constant</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \Delta\sigma_{load} $</td><td style="text-align: center; word-wrap: break-word;">Strength increment by load bearing effect, MPa</td><td style="text-align: center; word-wrap: break-word;">$ \Delta T $</td><td style="text-align: center; word-wrap: break-word;">Temperature difference between PBF-EB process and mechanical test, K</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \sigma_{y} $</td><td style="text-align: center; word-wrap: break-word;">Yield stress of matrix, MPa</td><td style="text-align: center; word-wrap: break-word;">T_{\alpha}</td><td style="text-align: center; word-wrap: break-word;">\alpha transus temperature, K</td></tr><tr><td style="text-align: center; word-wrap: break-word;">UTS</td><td style="text-align: center; word-wrap: break-word;">Ultimate tensile strength, MPa</td><td style="text-align: center; word-wrap: break-word;">d</td><td style="text-align: center; word-wrap: break-word;">Interparticle spacing,  $ \mu $m</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \Delta\sigma_{CET} $</td><td style="text-align: center; word-wrap: break-word;">Strength increment by thermal mismatch, MPa</td><td style="text-align: center; word-wrap: break-word;">$ \delta $</td><td style="text-align: center; word-wrap: break-word;">Level of lattice mismatch</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \Delta\sigma_{EM} $</td><td style="text-align: center; word-wrap: break-word;">Strength increment by elastic modulus, MPa</td><td style="text-align: center; word-wrap: break-word;">$ \rho $</td><td style="text-align: center; word-wrap: break-word;">Dislocation density, m^{-2} $ \mu $m^{-1}</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \Delta\sigma_{Orowan} $</td><td style="text-align: center; word-wrap: break-word;">Strength increment by Orowan strengthening, MPa</td><td style="text-align: center; word-wrap: break-word;">b</td><td style="text-align: center; word-wrap: break-word;">Burgers vector</td></tr><tr><td style="text-align: center; word-wrap: break-word;">G_{m}</td><td style="text-align: center; word-wrap: break-word;">Shear modulus of matrix, GPa</td><td colspan="2">E. Others</td></tr><tr><td colspan="2">B. Deformation</td><td style="text-align: center; word-wrap: break-word;">L90</td><td style="text-align: center; word-wrap: break-word;">90  $ \mu $m layer thickness</td></tr><tr><td style="text-align: center; word-wrap: break-word;">EL</td><td style="text-align: center; word-wrap: break-word;">Elongation to failure</td><td style="text-align: center; word-wrap: break-word;">SEM</td><td style="text-align: center; word-wrap: break-word;">Scanning electron microscopy</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \varepsilon $</td><td style="text-align: center; word-wrap: break-word;">Strain</td><td style="text-align: center; word-wrap: break-word;">SE2</td><td style="text-align: center; word-wrap: break-word;">Secondary electron</td></tr><tr><td colspan="2">C. Selected PBF-EB parameters</td><td style="text-align: center; word-wrap: break-word;">TEM</td><td style="text-align: center; word-wrap: break-word;">Transmission electron microscopy</td></tr><tr><td style="text-align: center; word-wrap: break-word;">I</td><td style="text-align: center; word-wrap: break-word;">Beam current, mA</td><td style="text-align: center; word-wrap: break-word;">SADP</td><td style="text-align: center; word-wrap: break-word;">Selected area diffraction pattern</td></tr><tr><td style="text-align: center; word-wrap: break-word;">v</td><td style="text-align: center; word-wrap: break-word;">Beam scanning speed, mm/s</td><td style="text-align: center; word-wrap: break-word;">HRTEM</td><td style="text-align: center; word-wrap: break-word;">High-resolution transmission electron microscopy</td></tr><tr><td style="text-align: center; word-wrap: break-word;">E_{L}</td><td style="text-align: center; word-wrap: break-word;">Line energy density, J/mm</td><td style="text-align: center; word-wrap: break-word;">HAADF</td><td style="text-align: center; word-wrap: break-word;">High-angle annular dark field</td></tr><tr><td style="text-align: center; word-wrap: break-word;">t</td><td style="text-align: center; word-wrap: break-word;">Spot time, ms</td><td style="text-align: center; word-wrap: break-word;">FFT</td><td style="text-align: center; word-wrap: break-word;">Fast Fourier transform</td></tr><tr><td style="text-align: center; word-wrap: break-word;">L_{off}</td><td style="text-align: center; word-wrap: break-word;">Line offset, mm</td><td style="text-align: center; word-wrap: break-word;">PBF-EB</td><td style="text-align: center; word-wrap: break-word;">Electron beam powder bed fusion</td></tr><tr><td style="text-align: center; word-wrap: break-word;">F_{O}</td><td style="text-align: center; word-wrap: break-word;">Focus offset, mA</td><td style="text-align: center; word-wrap: break-word;">L70</td><td style="text-align: center; word-wrap: break-word;">70  $ \mu $m layer thickness</td></tr><tr><td style="text-align: center; word-wrap: break-word;">n</td><td style="text-align: center; word-wrap: break-word;">Spot number</td><td style="text-align: center; word-wrap: break-word;">EBSD</td><td style="text-align: center; word-wrap: break-word;">Electron backscatter diffraction</td></tr><tr><td style="text-align: center; word-wrap: break-word;">l</td><td style="text-align: center; word-wrap: break-word;">Minimum distance per spot, mm</td><td style="text-align: center; word-wrap: break-word;">BSE</td><td style="text-align: center; word-wrap: break-word;">Backscattered electron</td></tr><tr><td style="text-align: center; word-wrap: break-word;"></td><td style="text-align: center; word-wrap: break-word;"></td><td style="text-align: center; word-wrap: break-word;">EDS</td><td style="text-align: center; word-wrap: break-word;">Energy dispersive X-ray spectroscopy</td></tr><tr><td colspan="2">D. Selected materials model parameters</td><td style="text-align: center; word-wrap: break-word;">GND</td><td style="text-align: center; word-wrap: break-word;">Geometrically necessary dislocations</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \eta $</td><td style="text-align: center; word-wrap: break-word;">Strengthening coefficient</td><td style="text-align: center; word-wrap: break-word;">STEM</td><td style="text-align: center; word-wrap: break-word;">Scanning transmission electron microscopy</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \Delta\alpha $</td><td style="text-align: center; word-wrap: break-word;">Thermal expansion coefficient difference between TiAl and Y_{2}O_{3}, K^{-1}</td><td style="text-align: center; word-wrap: break-word;">IFFT</td><td style="text-align: center; word-wrap: break-word;">Inverse fast Fourier transform</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \gamma $</td><td style="text-align: center; word-wrap: break-word;">Constant value of 0.5</td><td style="text-align: center; word-wrap: break-word;">ODS</td><td style="text-align: center; word-wrap: break-word;">Oxide dispersion strengthening</td></tr><tr><td style="text-align: center; word-wrap: break-word;"></td><td style="text-align: center; word-wrap: break-word;"></td><td style="text-align: center; word-wrap: break-word;">SENB</td><td style="text-align: center; word-wrap: break-word;">Single-edge notched bend</td></tr></table>

interlayer defects [13].

Previous work on the PBF-EB TiAl nanocomposite revealed two primary drawbacks [14,15]. First, pre-mixed powders decreased the sample densification and second, the microstructural degradation occurred during the PBF-EB process. The latter was characterised by the decomposition of  $ \alpha_{2} $ lamellae, coarsening of  $ \gamma $ lamellae, and nucleation and growth of equiaxed  $ \gamma $ grains, and with a greater extent found towards the sample build bottom [16]. Unfortunately, this means that post-processing treatment has to be employed to generate a uniform lamellar microstructure with full densification [17]. Alternatively, the melt strategy and process parameters could be optimised to meet the requirement of the first-time-right concept.

In terms of PBF-EB process parameters, Kan et al. [18] showed that fully lamellar microstructure in TiAl alloys can be achieved by using the higher preheat current as it helped to extend the time duration of the material passing through the single  $ \alpha $-phase region. During melting, the electron beam moves continuously from one end to the other in one pass and then hatch the whole layer line-by-line with the given line offset ( $ L_{off} $), so called hatch melt, which is a commonly used scan strategy as illustrated in Fig. 1a. The adjustable process parameters are mainly
Fig. 1. Schematics of (a) hatch melt and (b) multi-spot melt strategies.

scanning speed  $ \left(\nu\right) $, beam current  $ \left(I\right) $,  $ L_{off} $, beam focus offset  $ \left(FO\right) $, and speed function [2], which were investigated to understand their roles on the microstructure.

By comparison, another melt strategy which is comparatively less explored is the multi-spot melt. For this strategy, electron beam is turned on at a set of points for a short exposure time (t) of 0.05–2 ms [19], creating a series of micro-melt pools following the predefined sequence as shown in Fig. 1b. Once the entire layer is filled with the independent spots (e.g. 1–8), the next spot 9 is placed adjacent to the 1st spot, and the 10th spot is placed beside the 2nd spot, and so on. In fact, the spot can be set as a point or short line (Fig. 1b), which then affects the melt pool shape [19]. Also, the spot path can follow a closed loop, namely along the perimeter of the sample on the x-y plane, which is nevertheless used for printing the sample contour as it improves the geometric accuracy [20] and creates better surface roughness [21]. For multi-spot strategy, the adjustable parameters are mainly spot number (n), exposure time (t) and beam current (I). The multi-spot melt does not suffer from the complex interaction between scan lines as experienced by the hatch melt. Therefore, it is easier to control the solidification microstructure using the multi-spot melt, especially when printing a part with complex geometry [22].

By using the multi-spot melt strategy, Kirka et al. fabricated Inconel 718 sample with equiaxed grains and weak crystallographic texture [23]. The as-built Inconel 718 showed an isotropic tensile property at 650 ^\circC, which is comparable to the sample with columnar grains and strong texture along the build direction. The transition from the fine equiaxed to coarse columnar grains for Ni-based superalloys occurred at the region where the multi-spot melt switched to hatch melt scan strategy, indicating that multi-spot melt strategy led to faster solidification and lower thermal gradient [24,25]. Goel et al. observed a higher number density of fine carbides associated with the multi-spot melt strategy [26], However, to the best of the authors’ knowledge, no work has been done on TiAl using the multi-spot melt strategy.

The present work aims to understand the effect of multi-spot vs. hatch melt strategy and layer thickness on the microstructure and mechanical properties of PBF-EB TiAl-based nanocomposites. By changing the layer thickness, the additively manufactured part can have a different level of densification [27], dimensional accuracy [28] and surface roughness [29]. In addition, it can affect the columnar-to-equiaxed transition in Al alloy [30] and alter the solidification path [31]. It is worth noting that our goal is to achieve an excellent combination of high-temperature strength and room-temperature fracture toughness in PBF-EB  $ \gamma $-TiAl. With only a handful of work reporting the fracture toughness of additively manufactured  $ \gamma $-TiAl, this research endeavour is believed to be necessary, given the practical relevance to the industry.

## 2. Material and experimental

## 2.1. Electron beam powder bed fusion (PBF-EB)

PBF-EB samples ( $ 20 \times 20 \times 60 \, mm^{3} $) were processed on an Arcam A2XX machine using the electrode induction melting gas-atomised Ti-48Al-2Cr-2 Nb pre-alloyed powders (size of 45–150  $ \mu $m, Avimetal Co., Ltd.) mixed with 0.4 wt. %  $ Y_{2}O_{3} $ nanoparticles (size of  $ \sim $30 nm, Deke Daojin Co., Ltd.); henceforth abbreviated as  $ Y_{2}O_{3}/TiAl $. The mixing process was carried out on V-shaped three-dimensional blender (Mitr Instrument Equipment Co., Ltd.) in air for 5 h with the rotation speed of 13 rpm. The pre-mixed  $ Y_{2}O_{3}/TiAl $ powder particles are spherical in shape together with a few satellites (Fig. 2a). The powder surface is
Fig. 2. SEM micrographs of the pre-mixed Y₂O₃/TiAl powder: (a) powder morphology; (b) and (c) enlarged views of the powder; (d) to (i) SEM+EDS elemental mapping of Ti, Al, Cr, Nb, Y and O.

decorated with a network of grooves (Fig. 2b), signifying the dendritic structure caused by rapid cooling of the droplets during powder processing [32]. The spherical nanoparticles are mainly distributed at the grooves of dendrites (Fig. 2c), as confirmed by the elemental mapping (Fig. 2d–i), acquired using energy dispersive X-ray spectroscopy (EDS) in scanning electron microscope (SEM).

Two PBF-EB melt strategies are compared: hatch melt (used as the reference condition) vs. multi-spot (more exploratory). For the reference sample, three outlines with 0.5 mm offset (red lines in Fig. 3a) were produced during the contour melt whilst the electron beam meandered in a back-and-forth pattern during the hatch melt (black lines in Fig. 3a), with the 90^\circ scan rotation between layers. The pattern was formed by continuous movement of the electron beam (blue point in Fig. 3b). A layer thickness of 70 µm was used. More details about this conventional PBF-EB hatch melt can be found elsewhere [33].

By comparison, the multi-spot melt strategy created multiple closed loops along the perimeter of the sample on the x-y plane (black lines in Fig. 3c). The whole build area was subjected to a dummy scan upon the completion of each loop to ensure the same scanning time despite different loop perimeters. For this purpose, average beam current of I= 25 mA, scanning speed of v= 150000 mm/s and line offset of  $ L_{off}= 2 $ mm were chosen. The enlarged view of Fig. 3c presents a sketch with the numbers indicating the spot sequence. In this case, four concurrent beam spots were utilised. Fig. 3d shows the scanning pattern formed by the first spot of each short sections (blue) for the pre-defined loops.

Table 1 summarises the process parameters, and they were optimised to stabilise the building process. Especially, the process parameter set for the hatch melt scan strategy was proven as effective in producing the fully densified pure TiAl sample (without the addition of Y₂O₃), Fig. S1. All samples were processed at the build temperature of 1160 ^\circC and under a vacuum of 1 \times 10⁻² mbar which was controlled by using high purity helium as a regulating gas to prevent powder charging. For the multi-spot melt strategy, two PBF-EB sample batches were processed: one with the layer thickness of 90 \mum while the other with 70 \mum; hereafter these two sample conditions are abbreviated as L90 and L70, respectively.

## 2.2. Post-mortem characterisation

Densification of the as-built samples was evaluated based on the defect area fraction as determined by using Olympus LEXT OLS4000 3D laser confocal microscope. A Zeiss Gemini-300 SEM, equipped with detectors of secondary electron (SE2) and backscattered electron (BSE) imaging, energy dispersive X-ray spectroscopy (EDS) and HKI Nordlys Max3 electron backscatter diffraction (EBSD), was used for the

Table 1 Summary of the melt parameters. v: scanning speed, I: beam current,  $ L_{off} $: line offset, FO: focus offset,  $ E_{L} $: line energy, n: spot number, t: spot time, l: minimum distance per spot.  $ E_{L} $ is preferred here as the multi-spot melt does not involve the complex interaction between scan lines.

| Sample | $ \nu $ | I | $ L_{\text{off}} $ | FO | $ E_{\text{L}} $ | n | t | l |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ID | (mm/s) | (mA) | (mm) | (mA) | (J/mm) |  | (ms) | (mm) |
| Multi-spot | 600 | 25 | 0.5 | 0 | 2.5 | 50 | 0.8 | 4 |
| Hatch melt | 2400 | 8 | 0.1 | 0 | 0.2 |  | N/A |  |

(a)

microstructure characterisation. The number density per unit area, volume fraction and size of nanoparticles were measured based on at least ten SEM images via ImageJ. For the equiaxed microstructure and homogeneous distribution of nanoparticles, two-dimensional mean size as determined from the circular cross-sections represents the three-dimensional mean size [34]. For the EBSD data collection, step sizes of 0.1  $ \mu $m and 0.5  $ \mu $m were used. The HKL CHANNEL5 and OIM Analysis 7 were used to derive the orientation, phase constitution and geometrically necessary dislocations (GND). The Al concentration in the bulk sample was measured by means of titration.

Transmission electron microscopy (TEM, Tecnai G2 S-TWIN) operating at 300 kV was used to characterise the lamellar structure and nanoparticles, with the techniques including bright-field imaging, selected area diffraction pattern (SADP), high-resolution TEM (HRTEM) imaging, fast Fourier Transform (FFT), inverse FFT, high-angle annular dark field (HAADF) imaging, and EDS in scanning transmission electron microscopy (STEM) mode. TEM thin foils were prepared by first grinding down to thickness of  $ \sim $100  $ \mu $m and then was punched to a 3 mm disc. Finally, the disc was electropolished using a twin-jet electropolisher in a solution of 5 vol. % perchloric acid+ 30 vol. % butanol+ 65 vol. % methanol at 15 V and  $ -40 $ ^\circC.

Vickers microhardness measurements were performed on QATM Qness Q30 A+ utilising a 200 gf load with dwell time of 15 s. Ten indentations were made per condition to obtain the average value. Tensile tests were performed on an Instron 5582 universal testing machine at 800 ^\circC with a strain rate of  $ 2 \times 10^{-4} $ s $ ^{-1} $, according to ISO 783–1999. The tensile strain was measured by using the Epsilon high-temperature extensometer with a gauge length of 25 mm. The YS, UTS and tensile elongation (EL) were all determined from the engineering stress-strain curve. Fracture toughness ( $ K_{IC} $) was measured using single-edge notched bend (SENB) specimens with a clip-on gauge attached to UTM4204 universal testing machine to measure the force-displacement curve, according to ASTM E399. Specimen dimensions are shown in
Fig. 3. Schematics of (a) the snake-like melt and (c) the multi-spot melt strategies; the scanning pattern formed by the first beam spot under the hatch melt in (b) and multi-spot melt in (d).

Fig. S2. A minimum of three tests were performed to obtain the average data for mechanical testing.

## 3. Results

## 3.1. Comparison between the multi-spot and hatch melt strategy

The top surface is flat without swelling (Fig. 4a and c) for both the hatch melt and multi-spot samples, indicating a stable PBF-EB process under the selected parameters. Under high energy input, the steep temperature gradient developed between the centre and edge of the melt pool surface can generate a surface tension gradient and capillary forces, which is the cause of swelling [35,36]. Therefore, multi-spot melt strategy helps to reduce heat accumulation. Also, the independent melt pools can be seen clearly from the top surface of the multi-spot sample (Fig. 4c), suggesting that the spot was already solidified before the arrival of the next adjacent one. This is as expected due to the very short interaction time (0.8 ms) of the electron beam with powder bed [37]. By comparison, the melt pools of the hatch melt sample are connected to form a linear arrangement (Fig. 4a).

The cross section reveals the lack-of-fusion defect and a few pores in the hatch melt sample (Fig. 4b and S3a), with the defect area fraction measured as 1.6 %. By comparison, the multi-spot sample has a good densification with virtually no defect (Fig. 4d). The Al concentration was measured to be 46.3 at. % in the multi-spot sample ( $ E_{L}=2.5 $ J/mm), whilst 46.5 at. % in the hatch melt sample ( $ E_{L}=0.2 $ J/mm). The similar Al loss for two different  $ E_{L} $ values is unexpected as previous work showed that the higher Al loss was correlated with the higher energy input [38]. This is probably due to the more energy loss and fast cooling rate despite a higher energy input for the multi-spot melt.

The multi-spot sample has a phase constitution of 49.7 %  $ \alpha_{2} $-phase, 40.2 %  $ \gamma $-phase and 10.1 % B_{2}-phase, as illustrated by the EBSD phase map in Fig. 5a. The matrix exhibits a duplex microstructure consisting of  $ \alpha_{2}/\gamma $ lamellar colonies, equiaxed  $ \gamma $ and B_{2} grains, as shown by the BSE-SEM image in Fig. 5b. The inset in Fig. 5b shows the uniform distribution of nanoparticles without agglomeration and slagging. The size, number density and volume fraction of nanoparticles were determined as  $ 90 \pm 38 $ nm,  $ 0.28 \pm 0.14 $  $ \mu $m $ ^{-2} $ and  $ 0.8 \pm 0.2 $ %, respectively, based on SEM micrographs. The  $ \alpha_{2}/\gamma $ lamellar interface is straight and the lamellar spacing was measured to be  $ 208 \pm 72 $ nm (TEM image in Fig. 5c). Many twin intersections and dislocations (red arrows in Fig. 5e) can be seen in the equiaxed  $ \gamma $ grains, suggesting that the internal stress generated during the PBF-EB process is likely to be accommodated by deformation of  $ \gamma $ grains (TEM images in Figs. 5d and 5e). Fig. 5f is an HRTEM image taken from the twin intersections as identified from Fig. 5e. The stacking faults can be observed at the twin interface, suggesting that the twin formation involves the dislocation slip on the consecutive  $ \{111\}\gamma $ plane [39]. Also, twins develop along different directions, as delineated by the red, blue and green lines for the planes of  $ \gamma $-matrix (Fig. 5f). Secondary twinning (blue lines in Fig. 5f) is observed at the intersection of  $ \gamma_{T1} $ and  $ \gamma_{T2} $, and both twin bands are deflected. Fig. 5g to 5i show that the twins develop both along the interface and within the  $ \gamma $ lamellae. The twin lamellae within  $ \gamma $ lamellae can propagate across the twin interface but terminate at the  $ \gamma/\alpha_{2} $ interface.

The  $ \gamma $-phase fraction for the hatch melt sample is much higher than that of the multi-spot sample, comparing Fig. 6a with Fig. 5a. The EBSD determined phase constitution in the hatch melt sample is 14.3 %  $ \alpha_{2} $, 70.4 %  $ \gamma $ and 15.3 % B_{2}. The nanoparticles have a mean size of 218 \pm 113 nm and some particles are arranged in a chain-like pattern (Fig. 6b). Compared to the multi-spot sample (Fig. 5b), the nanoparticle size in the hatch melt sample is larger and its distribution is less uniform, which is corresponding to the lower nanoparticle number density of 0.09 \pm 0.03  $ \mu $m $ ^{-2} $ and similar volume fraction of 0.9 \pm 0.4 %. The lamellar interface is straight and the lamellar spacing was measured to be 959 \pm 155 nm (Fig. 6c). Dislocations and twins can be found in both the equiaxed  $ \gamma $ grains and  $ \gamma $ lamellae (Fig. 6d to f), but no evidence suggesting their presence in  $ \alpha_{2} $ and B_{2} grains. Dislocations are blocked by twins and grain boundaries (red arrows, Fig. 6d). Some dislocations are arranged in a parallel pattern (Fig. 6e), suggesting the twin formation mechanism via the dislocation pile-up at boundaries [39]. Fig. 6d and HAADF images (Fig. S4g) show the merging of twins proceeded by movement of small steps along the twin interface; this suggests the ‘terrace-ledge-kink’ mechanism [40]. In addition, the presence of dislocation sub-grain boundary within  $ \gamma $ lamellae (Fig. 6f) indicates that the internal stress during the PBF-EB process is high enough to trigger the recovery and recrystallisation of  $ \gamma $-TiAl [41].
Fig. 4. Top view of the as-built samples by comparing the hatch melt in (a) with the multi-spot melt in (c). Representative SEM micrographs taken by the SE2 mode, showing the defects in the hatch melt sample in (b) but virtually no defect in the multi-spot sample in (d). The relative density is measured by image method. More details of the defects in the hatch melt sample can be found in Fig. S3b to S3f.
Fig. 5. Representative microstructures of the multi-spot sample (L70): (a) EBSD map of phase constitution; (b) BSE-SEM micrograph and the figure inset showing the overall microstructure; (c) and (d) TEM bright-field images showing the nanoscale lamellar microstructure and the substructure in equiaxed  $ \gamma $ grains; (e) high-magnification TEM image as indicated in (d) showing the twin intersections and dislocations; (f) HRTEM image of the selected region in (e); (g) TEM bright-field image showing parallel twins associated with the  $ \gamma $ lamellae; (h) SADP for (g); (i) HRTEM image marked in (g). Note that the TEM SADPs for  $ \gamma $ and B_{2} phased in (d) are shown in Fig. S4a and S4b. The twin interfaces were determined by FFT performed on the selected areas in (f), referring to Fig. S4c to S4f.

Fig. 7 shows the tensile properties at 800 ^\circC of the multi-spot (lower row) and hatch melt samples (upper row). The hatch melt sample fractured either out of gauge length (Fig. 7a) or from the lack-of-fusion defects (Fig. 7b) in an intergranular manner (Fig. 7c). The engineering stress-strain curve shows a pure elastic characteristic, and thus the data is not included for brevity. Given the low densification of hatch melt sample, the tensile property and fracture behaviour of the multi-spot sample is explained in detail below. The stress-strain curve of the multi-spot sample shows a typical feature of ductile material (Fig. 7d). The YS, UTS and EL was measured as  $ 404 \pm 5 $ MPa,  $ 556 \pm 11 $ MPa and  $ 17.0 \pm 3.1 $ %, respectively. SEM fractography reveals both the transgranular fracture and ductile dimples (Fig. 7e). The cross-sectional view in Fig. 7f shows the deformed lamellae close to the fracture surface, most likely due to activation of multiple slip systems in  $ \alpha_{2} $ and  $ \gamma $ at high temperature [42]. The micro-voids are mainly observed at equiaxed  $ \gamma $ and B_{2} grain boundaries and their linkage forms the crack, implying the preferred inter-granular fracture at 800 ^\circC for the  $ \gamma $-TiAl alloy.

## 3.2. Microstructure homogeneity and nanoparticles of multi-spot sample

Given the good tensile property for the multi-spot sample, quantitative microscopy was performed on the x-y plane at three locations of A to C (Fig. 8a). Duplex microstructure with the lamellar colony fraction of  $ 54 \pm 5\% $,  $ 58 \pm 6\% $ and  $ 61 \pm 3\% $, and the colony size of  $ 42 \pm 10 \mu m $,  $ 34 \pm 11 \mu m $ and  $ 33 \pm 9 \mu m $, was found for the regions A, B and C, respectively, indicating a uniform microstructure. Since regions A to C represent different loop perimeters, this observation proves that the dummy scan applied at the finish of printing each loop has been successful in maintaining the uniform heat history on the powder bed. In
Fig. 6. Representative microstructure of hatch melt sample: (a) EBSD map of phase constitution; (b) BSE-SEM micrograph of the overall microstructure; (c) to (f) TEM bright-field images showing the lamellar microstructure, twin and dislocation substructure. Note that the  $ \gamma $-phase was confirmed via the EDS for (d) and SADPs for (e) and (f), as shown in Fig. S4h and S4i.
Fig. 7. Comparison of the tensile properties at 800 ^\circC: (a) and (b) photograph of tensile specimens after fracture and SEM fractography of the hatch melt sample; (c) enlarged view of the marked region in (b); (d) engineering stress-strain curves of the multi-spot sample (L70); (e) SEM fractography and (f) SEM cross-sectional view of the fractured surface.

addition, the Y₂O₃ nanoparticles are distributed homogenously within TiAl matrix irrespective of the location (insets of Fig. 8b–d).

TEM was used to further characterise the nanoparticles in the multi-spot sample. Nanoparticles have two distinct shapes: rod-like (Fig. 9b) and spherical (Fig. 9e); and both are randomly distributed in the TiAl matrix, as shown by the HAADF image of the low-magnification view (Fig. 9a). The STEM+EDS line scan shows that the nanoparticles are rich in Y and O elements while depletion in Ti and Al elements (Fig. 9c and f). The rod-like particle is monoclinic (Fig. 9d), while the spherical Y₂O₃ particle belongs to the cubic crystal system (Fig. 9g). Both are the Y₂O₃ type particles, according to their compositions (STEM+EDS results in Fig. 9c and f) and lattice parameters (SADP and FFT results in Fig. 9d and g).

Given the added  $ Y_{2}O_{3} $ nanoparticles in pre-mixed  $ Y_{2}O_{3}/TiAl $ powders have a spherical shape, it is likely that the spherical nanoparticles as observed in the as-built sample are inherited from the original  $ Y_{2}O_{3} $
Fig. 8. BSE-SEM micrographs along the diagonal direction at z = 22.5 mm in the multi-spot sample: (a) Schematic of the extraction position on the x-y plane; (b) to (d) microstructure of points A to C marked in (a). Insets in (b) to (d) illustrates the nanoparticle distribution.
Fig. 9. TEM examination of nanoparticles in the multi-spot sample: (a) HAADF image showing nanoparticles with two different shapes; (b) and (e) TEM bright-field image of rod-like and spherical nanoparticles; (c) and (f) STEM+EDS line scans across the nanoparticles along the arrow marked in (b) and (e); (d) SADP and (g) FFT diffractograms collected from the nanoparticle region in (b) and (e).

particles but get coarsened. For the rod-like nanoparticles, it is considered that the added  $ Y_{2}O_{3} $ nanoparticles are melted, followed by precipitating as the monoclinic structure with Nb element dissolved. The interface between the nanoparticle and TiAl matrix is clean, well defined and free of interfacial reactions (Fig. 9b and e); all these features indicating the strong interfacial bonding.

3.3. Comparison between the 90  $ \mu $m and 70  $ \mu $m layer thickness of multi-spot sample

Tensile properties at 800 ^\circC of the multi-spot sample L70 (YS: 404 \pm 5 MPa, UTS: 556 \pm 11 MPa, EL: 17.0 \pm 3.1 %, Fig. 7d to f) are generally better than the L90 counterpart (YS: 394 \pm 15 MPa, UTS: 456 \pm 4 MPa, EL: 18.4 \pm 4.6 %, derived from the stress-strain curves as shown in Fig. S5). L70 has the microhardness value of 383 \pm 25 HV₀.₂, which is also higher than 349 \pm 16 HV₀.₂ for L90. The most striking result is the room-temperature fracture roughness: L70 with  $ K_{IC} = 16.5 \pm 0.3 $ MPa\sqrtm as opposed to L90 with  $ K_{IC} = 11.7 \pm 1.0 $ MPa\sqrtm, and indeed both values exceeding the published  $ K_{IC} $ value for PBF-EB \gamma-TiAl [14].

SEM fractography reveals the pattern of steps (red circle) and lamellar delamination facets (blue circle), Fig. 10a and b for L90 and L70 samples respectively; both features suggesting the role of lamellar microstructure. Quantitative measurements confirm that the step width of L90 (~710 nm) (Fig. S6a) is larger than L70 (~160 nm) (Fig. S6b), indicating that finer lamellae caused by smaller layer thickness in L70 helps to enhance the material toughness.

SEM examination of the region close to the fracture surface corroborates our hypothesis. Trans-lamellar and inter-lamellar cracking characteristics are observed in L70 (Fig. 10c and d). The trans-lamellar
Fig. 10. SEM fractography of (a) L90 and (b) L70 observed after the SENB specimen was tested to fracture. SEM cross-sectional view of the near fracture surface: (c) trans-lamellar and (d) inter-lamellar cracking in L70.

fracture characterised by tortuous crack path is a result of the hindering effect of lamellae, increasing the fracture energy. The inter-lamellar fracture characterised by many parallel micro-cracks across the lamellae, contributes to local plasticity near the crack tip [43]. It can be concluded that the finer lamellar microstructure in L70 contributes to the material toughening. The slightly less tensile ductility of L70 (17.0 \pm 3.1 %) compared to L90 (18.4 \pm 4.6 %) at 800 ^\circC might be attributed to the lower content of \gamma-phase (40 % for L70 vs. 75 % for L90) since SEM fractography examination reveals little difference between the two (Fig. S6c and S6d). The face-centred cubic \gamma-phase in TiAl alloy tends to provide more plasticity compared to the hexagonal close-packed \alpha₂-phase [44], as observed in our TEM examination revealing the predominant twin and dislocation activities in the \gamma-phase (Fig. 5).

Representative SEM micrographs taken from the top layer of the L90 and L70 samples are shown in Fig. 11a and c, while those from the bulk samples are shown in Fig. 11b and d for comparison purposes. A fully lamellar microstructure consisting of the  $ \alpha_{2}/\gamma $ lamellar colonies is seen in the top layer (Fig. 11a for L90 and Fig. 11c for L70). By comparison, the bulk microstructure exhibits a duplex type (Fig. 11b for L90 and Fig. 11d for L70). The transition from the fully lamellar to duplex microstructure is attributed to the microstructure degradation caused by thermal cycling and exposure at high temperature during the PBF-EB
Fig. 11. Representative BSE-SEM micrographs taken from the top layer and bulk regions: top layers (a) L90 and (c) L70; which are compared with the bulk region (b) L90 and (d) L70. Blue and red rectangles highlight two lamellar degradation mechanisms. Green highlights a typical lamellar colony.

process. In detail, red rectangles in Fig. 11b and d suggest a degradation mechanism involving the decomposition of  $ \alpha_{2} $ lamellae accompanied by  $ \gamma $ merging via  $ \alpha_{2} \rightarrow \gamma $, while the blue rectangles indicate the  $ \gamma $ and/or B_{2} grains formation at lamellar colony boundaries [45]. The role of in-situ heat treatment is judged as limited considering the very short time in  $ (\alpha + \gamma) $ two phase field. Conventional heat treatment would require 2 h to obtain the duplex microstructure [46].

In terms of the colony boundary degradation,  $ \gamma $ grains are near-equiaxed in L90 (Fig. 11b), whereas the irregular shaped  $ \gamma $ grains with some of them extending into adjacent  $ \gamma $ lamellae are frequently observed in L70 (Fig. 11d). This indicates that the layer thickness plays a certain role in degradation mechanism at colony boundary during PBF-EB. The mechanism involving the colony boundary spheroidisation often leads to the equiaxed grain shape [45,47], as observed in L90 (Fig. 11b), while that of lamellar termination migration [45,48] ends up with the irregular shaped grains [6], as observed in L70 (Fig. 11d). Moreover, the top-layer microstructure of L70 exhibits a much higher aspect ratio (length-to-thickness of  $ \gamma $ lamellae) of  $ 114 \pm 38 $ (Fig. 11c) than that of  $ 31 \pm 13 $ (Fig. 11a) in the L90. According to [49], the larger the aspect ratio is, the higher likelihood the lamellar termination migration mechanism occurs. The reason for the higher aspect ratio in L70 is probably owing to the higher cooling rate under the condition of a smaller layer thickness [30].

The lamellar colony fraction along z direction of L70 and L90 samples are compared in Fig. 12a. The fraction reduces sharply from 100 % (i.e. fully lamellar microstructure as observed in the top layer) to 59 \pm 11 % and 78 \pm 2 % for L90 and L70, respectively, in the upper region (z \geq 58 mm, highlighted by yellow). This is followed by a moderate reduction between the z height of 58 mm and 47.5 mm, and then it shows little change when z \leq 47.5 mm, as highlighted by white in Fig. 12a. Overall, the severe reduction in lamellar colony fraction near the top-layer region indicates that the thermal cycling of the next adjacent layers plays a predominant role on the microstructure degradation. The lack of degradation gradient below the region of z = 47.5 mm indicates that the PBF-EB Y₂O₃/TiAl nanocomposite has a good resistance to microstructure degradation induced by high build temperature.

Despite a similar colony fraction between the bulk region of the L90 and L70, the  $ \alpha_{2} $-phase fraction of L70 was measured to be 50 %, which is considerably higher than the L90 (12 %). Fig. 12b shows a representative SEM micrograph of L70, revealing a region containing a few lamellar colonies which does not show  $ \alpha_{2} $ lamellae decomposition, as highlighted by red with the inset indicating well-defined  $ \alpha_{2}/\gamma $ lamellae. By comparison, such a feature cannot be seen in the L90. Thus, a smaller layer thickness in PBF-EB process helps to reduce the microstructure degradation.

The L90 sample was examined further by TEM, and the results are shown in Fig. 13, which can be compared with the TEM observation as shown in Fig. 5 for L70. It can be clearly seen that the coarsening of  $ \gamma $ lamellae and dissolution of  $ \alpha_{2} $ proceeds by movement of small steps along  $ \alpha_{2}/\gamma $ interface (Fig. 13a), indicating the diffusion-controlled step mechanism [50]. The dislocation slip in  $ \gamma $-phase seems to induce the formation of twins (Fig. 13b) or blocked at boundaries (Fig. 13c). Some  $ \gamma $ sub-grains are seen at lamellar interfaces and across the  $ \alpha_{2} $ and  $ \gamma $ lamellae (Fig. 13c, red line), implying the recrystallisation drives the lamellar degradation.

## 4. Discussion

## 4.1. Twins and nanoparticle/matrix interface in PBF-EB Y₂O₃/TiAl nanocomposite

Mechanical twin is formed via dislocations slip along multiple 1/6 < 11 $ \overline{2} $[111] of  $ \gamma $ under stress and it has a nanometre thickness [51]. The parallel twins and twin intersections with a thickness less than 10 nm within  $ \gamma $ lamellae and equiaxed  $ \gamma $ grains, as shown in Fig. 5 g and e, are mechanical twins. The nanotwins contrast as observed in the BSE-SEM image (Fig. S_{7}) indicates that these twins are not caused by the TEM sample preparation.

The stacking fault formed via Shockley partial dislocation slip in the direction of  $ \mathbf{b}=1/6<11\overline{2} $ on the  $ \{111\}\gamma $ plane is the precursor of twin nucleation [44]. Therefore, formation of twins depends on the stacking fault energy. Wen et al. evaluated the generalised planar fault energy of TiAl alloys with different Al concentrations by first-principles calculations with continuous density function theory, and the critical twinning stress of Ti-48Al alloy was calculated as 126 MPa [52]. Experimentally, by fitting the tensile yield stress and grain size, Monchoux et al. [39] and Kim et al. [53] speculated that the minimum stress necessary to propagate twins in Ti-47Al-2Cr-2 Nb at room temperature and Ti-48Al at 877 ^\circC was 24 MPa and 50 MPa, respectively. For Inconel 718 fabricated by PBF-EB, the maximum residual stress was measured to be up to 60 MPa by neutron diffraction [54]. The residual stress magnitude in the TiAl should be comparable with the Inconel 718 because of the similar thermal expansion coefficient, thermal conductivity and build temperature [55,56]. Therefore, the presence of mechanical twins can be justified.

There is no contrast change to suggest the twins or dislocations around the rod-like and near spherical nanoparticles (Fig. 9b and e) in the as-built sample. But such a misfit strain induced contrast was frequently observed in TiAl-based nanocomposites fabricated by conventional means (casting and powder metallurgy) [57]. As shown in the SEM fractography of the tensile specimen (Fig. 7e), added nanoparticles
Fig. 12. (a) Quantitative measurements of lamellar colony fraction along z direction in L90 and L70; (b) BSE-SEM micrographs of the bulk L70 showing a lamellar colony which has no degradation. Inset in upper right highlights the fine lamellae.
Fig. 13. TEM bright-field images of L90: (a) lamellar microstructure, (b) twins and dislocations and (c) sub-grains.

induce no crack. Therefore, a strong interfacial bonding exists between the nanoparticles and TiAl matrix in the PBF-EB Y₂O₃/TiAl nanocomposite.

Orientation relationship and coherency between Y₂O₃ and TiAl matrix can be worked out by the lattice images taken from the HRTEM and IFFT (Fig. 14). The rod-like Y₂O₃ with monoclinic crystal system consists of curved interface of (311)Y₂O₃||(110)\gamma (Fig. 14a and d) and straight interface of (001)Y₂O₃/(111)\gamma with a 17.4^\circ misorientation (Fig. 14b and e). The spherical Y₂O₃ with cubic crystal structure is formed by short steps composed of small facets along (110)\gamma||(013)Y₂O₃ planes and (240)Y₂O₃/(002)\gamma planes with a 14.9^\circ misorientation (Fig. 14c and f).

The level of misfit  $ \delta $ around the interface between  $ Y_{2}O_{3} $ particle and TiAl matrix can be calculated according to [58]:

 $$ \delta{=}2(a\mathrm{Y}_{2}\mathrm{O}_{3}{-}a\gamma)/(a\mathrm{Y}_{2}\mathrm{O}_{3}{+}a\gamma)\times100~\% $$ 

where  $ aY_{2}O_{3} $ and  $ \alpha\gamma $ are the periodic lengths of  $ Y_{2}O_{3} $ and  $ \gamma $ lattice along the interface, respectively. The calculation results are summarised

Lattice parameters and calculated misfits between Y₂O₃ and \gamma-phase.

| Lattice planes | aY_{2}O_{3} (nm) | a\gamma (nm) | Misfit, \delta (%) | Interface type |
| --- | --- | --- | --- | --- |
| ( $ \overline{3} $11)Y_{2}O_{3}||(1 $ \overline{1} $0) $ \gamma $ | 0.2939 | 0.2420 | 19.4 | Semi-coherent |
| (001)Y_{2}O_{3}/(111) $ \gamma $ | 0.2853 | 0.2810 | 1.5 | coherent |
| (0 $ \overline{1} $3)Y_{2}O_{3}||(110) $ \gamma $ | 0.2227 | 0.2017 | 9.9 | Semi-coherent |
| ( $ \overline{2} $40)Y_{2}O_{3}/(002) $ \gamma $ | 0.3258 | 0.3090 | 5.3 | Semi-coherent |
Fig. 14. HRTEM images from the Y₂O₃/TiAl interface of rod-like nanoparticles with (a) curve and (b) straight interface and (c) spherical nanoparticles. White dashed line delineates the interface. (d) to (f) IFFT for the rectangle-marked region in (a) to (c).

in Table 2. The misfit  $ \delta $ of interface ( $ \overline{311} $)Y $ _{2} $O $ _{3} $||(1 $ \overline{1} $0) $ \gamma $ in rod-like particles is 19.4 %, indicating a semi-coherent curved interface which is accommodated by some misfit dislocations (Fig. 14d). The 1.5 % misfit of the (001)Y $ _{2} $O $ _{3} $/(111) $ \gamma $ interface indicates a coherent relationship for the straight interface of the rod-like particles. Lattice distortion and steps as observed near the interface help to accommodate its misorientation (Fig. 14e). More dislocations at the curved semi-coherent interface could promote the interface diffusion and migration, leading to the fast growth along the straight edge. Compared to the semi-coherent interface, the straight and coherent interface is more stable due to the lower interface energy, resulting in a slow growth along its normal direction by step mechanism. Thus, the particles exhibit a rod-like shape. In terms of spherical particles (Fig. 14c and f), the misfit of (110) $ \gamma $||(0 $ \overline{1} $3)Y $ _{2} $O $ _{3} $ and ( $ \overline{2} $40)Y $ _{2} $O $ _{3} $/(002) $ \gamma $ interface was calculated as 9.9 % and 5.3 %, respectively, indicating a semi-coherent type. Therefore, the same growth condition contributes to the isotropic spherical shape. The rod shape is more effective in toughening by bridging whilst the spherical shape contributes to the strengthening by hindering dislocation motion.

## 4.2. Mechanical property comparison between the PBF-EB and conventional means

Fig. 15 compares the tensile properties (800 ^\circC) of the present PBF-EB Y₂O₃/TiAl nanocomposite with pure TiAl alloy and TiAl-based composites prepared by conventional methods (casting, powder metallurgy and hot working). Limited improvement of strength was found in the present PBF-EB Y₂O₃/TiAl nanocomposite when compared to the TiAl-based composites prepared by conventional methods. This might be caused by the higher fraction of brittle B_{2}-phase and equiaxed grains of \gamma and B_{2} whose boundaries are prone to cracking (Fig. 7f). However, it is worth noting that the strength and elongation of PBF-EB Y₂O₃/TiAl nanocomposite are much higher than those of the pure TiAl. This indicates that utilising multi-spot melt strategy has a potential in improving the mechanical property of PBF-EB TiAl alloys, especially after parameter optimisation to minimise B_{2}-phase.

The improved mechanical property for nanocomposite is generally attributed to the grain refinement, increased GND for accommodating mismatch of thermal expansion coefficients and elastic moduli between the matrix and nanoparticle, Orowan strengthening, and load bearing effect of nanoparticles. Experimentally, the YS was increased by 134 MPa in the present PBF-EB Y₂O₃/TiAl nanocomposite, in comparison with the data as reported in [59] for Ti-48Al-2Cr-2 Nb alloys fabricated by casting. According to the strengthening model utilised in [60,61], the increment in yield strength can be coupled together and expressed as follows:
Fig. 15. Tensile property comparison of the present PBF-EB Y₂O₃/TiAl nanocomposite with Ti_{4822} (Ti-48Al-2Cr-2 Nb) alloys, Ti_{4822}-based composites, other types of TiAl alloys and TiAl-based composites fabricated by conventional means (the tensile data used here are summarised in Table S_{1}).

 $$ \Delta\sigma=\sqrt{\Delta\sigma_{H a l l-P e t c h}^{2}+\Delta\sigma_{O r o w a n}^{2}+\Delta\sigma_{C E T}^{2}+\Delta\sigma_{E M}^{2}+\Delta\sigma_{l o a d}^{2}} $$ 

The microstructure of PBF-EB sample is significantly refined when compared to that processed by conventional means. According to the Hall-Petch relationship, the contribution by the grain boundary strengthening mechanism ( $ \Delta\sigma_{Hall-Petch} $) can be calculated as below:

 $$ \Delta\sigma_{H a l l-P e t c h}=k\bigg(\lambda_{P B F-E B}^{1/2}-\lambda_{c o n v e n t i o n a l}^{1/2}\bigg) $$ 

where k is a constant and  $ \lambda $ is the lamellar colony size.

The nanoparticles in PBF-EB TiAl-based composite have uniform distribution, acting as strong obstacles to the dislocation motion under high temperature deformation via Orowan strengthening. Therefore, the contribution by the Orowan strengthening mechanism induced by nanoparticles of  $ Y_{2}O_{3} $ ( $ \Delta\sigma_{Orowan} $) can be estimated by the following equation [62]:

 $$ \Delta\sigma_{Orowan}=\frac{0.13G_{m}b}{d}\ln\frac{D}{2b} $$ 

where  $ G_{m} $ is shear modulus of the matrix, D is the particle diameter, b is Burgers vector of the  $ \gamma $-phase and d is the interparticle spacing. Note that for simplification the above calculation does not take into account the shape and orientation of precipitates.

TiAl matrix and  $ Y_{2}O_{3} $ particles have different coefficients of thermal expansion. Therefore, the dislocation density will be generated during solidification and cooling owing to the thermal mismatch between the TiAl and  $ Y_{2}O_{3} $ particles. Thus,  $ \Delta\sigma_{CET} $ can be estimated as:

 $$ \Delta\sigma_{C E T}=\eta G_{m}b\sqrt{\frac{12\Delta\alpha\Delta T V_{p}}{b D(1-V_{p})}} $$ 

where  $ \eta $ is a given strengthening coefficient close to 1.25.  $ \Delta\alpha $ is the difference between TiAl alloy matrix and  $ Y_{2}O_{3} $ particles.  $ \Delta T $ is the difference between process temperature ( $ \sim $1160 ^\circC/1433 K) and test temperature (800 ^\circC/1073 K).  $ V_{p} $ is the volume fraction of nanoparticles.

The elastic modulus mismatch between the matrix and nanoparticles can also lead to increased GND during deformation. Such a strength increase ( $ \Delta\sigma_{EM} $) can be assessed by:

 $$ \Delta\sigma_{E M}=\gamma G_{m}b\sqrt{\frac{18V_{p}\varepsilon}{b D}} $$ 

where  $ \gamma $ is a constant in the order of 0.5.  $ \varepsilon $ is the uniform deformation which can be obtained from stress-strain curve.

The good combination of nanoparticles and matrix interface can provide a certain load bearing effect. This is caused by the shear transfer of load from the matrix to the particles during tensile and is represented by:

 $$ \Delta\sigma_{l o a d}=0.5V_{p}\sigma_{y} $$ 

where  $ V_{p} $ is the volume fraction of nanoparticles and  $ \sigma_{y} $ is the YS of the matrix.

The contributions of different strengthening mechanisms to the YS of PBF-EB Y₂O₃/TiAl nanocomposite were calculated based on the data given in Table S_{2}, using Eqs. (3) to (7), to be 25 MPa, 13 MPa, 55 MPa, 130 MPa and 1 MPa, respectively. The total contribution of 144 MPa is comparable with our experimental observation of \Delta\sigma = 134 MPa and the slight discrepancy can be accepted according to [60]. Therefore, the particle strengthening attributed to the mismatch of EM plays a major role in the enhancement of high temperature strength for the PBF-EB Y₂O₃/TiAl nanocomposite.

In addition, the much delayed drop in work-hardening rate during the tensile test at 800 ^\circC (Fig. S8) indicates the combined effect of dislocations and twins in PBF-EB Y₂O₃/TiAl nanocomposite. Deformation

by dislocations mechanism often leads to the noticeable work hardening drop, which seems to be offset by the twin mechanism [44,63]. It has been demonstrated that the twin interfaces contribute to toughening by reducing the number of slip systems needed for the deformation [64].

## 4.3. Multi-spot melt strategy and layer thickness

The hatch melt sample with addition of Y₂O₃ nanoparticles exhibits many lack-of-fusion defects (Fig. 4b), while the pure TiAl sample printed using the same parameters shows the full densification (Fig. S1). This indicates that the Y₂O₃ addition impacts the melting and solidification behaviour of the TiAl powders. The defects as observed in the hatch melt sample were carefully examined (Fig. S3). The presence of un-melted powders (Fig. S3b and S3c) implies that local heat was not sufficient to melt the powder. This might be attributed to the isolation of heat by surface adhered Y₂O₃ nanoparticles [65]. Defects are mainly located at the melt pool bottom, as revealed by the dark contrast under BSE imaging mode owing to the Al evaporation from the melt pool top and its propagation along the powder layer (Fig. S3d and S3e). It implies that the melt could not spread on the powder bed before solidification. Many Y₂O₃ nanoparticles found in such interlayer defects (Fig. S3f) indicate that the defect formation was due to the increased viscosity of the melt related to the Y₂O₃ nanoparticle addition [5]. Also, more frequent ‘smoke’ phenomena during the PBF-EB build process suggests the worse conductivity of pre-mixed powders, resulting in the lower density [66]. By comparison, ‘smoke’ was rarely observed for the multi-spot melt strategy, which is probably due to the short interaction time of electron beam with powder bed. Moreover, higher energy input (Eₐ=2.5 J/mm) helps to increase the melt fluidity to fully spread on the powder bed.

The duplex microstructure was found in both the multi-spot and hatch melt samples due to the similar Al concentration, suggesting the same transformation sequence. The fully lamellar microstructure formed after solidification of each layer via  $ \gamma $ lamellae precipitated from  $ \alpha $ grains, which was followed by the formation of equiaxed  $ \gamma $ grains via  $ \alpha \rightarrow \gamma $ transition due to the exposure at  $ \alpha + \gamma $ phase field (i.e. build temperature of 1160 ^\circC, Fig. S_{9}). In terms of the nanoparticles, they were subjected to melting, precipitation and coarsening. However, the multi-spot sample has a finer lamellar spacing, more  $ \alpha_{2} $-phase and smaller nanoparticle than the hatch melt sample.

The final microstructure difference between the two melt strategies is attributed to their thermal histories (refer to Table 1 for the process parameters). Faster scanning speed of the hatch melt sample (1800 mm/s) than the multi-spot melt sample (600 mm/s) would result in a short return time and more interactions between scan lines. This likely causes more heat accumulation in the hatch melt sample as well as the larger heat affected zone. Moreover, the smaller line offset of the hatch melt sample (0.1 vs. 0.5 mm) makes it suffer from more thermal cycles. Therefore, there is a larger diffusion driving force of atoms in the hatch melt sample, which promotes the phase transition and nanoparticle coarsening. In addition, a higher cooling rate for the multi-spot sample suggests a higher nucleation driving force of  $ \gamma $ lamellae.

The nanoparticles in the multi-spot sample showed a homogenous distribution (Fig. 5b), while some chain-like patterns were found in the hatch melt sample (Fig. 6b). The difference is likely attributed to the stirring of fluid flow within the melt pool. The nanoparticles at the top layer of the hatch melt sample were found to be arranged as a chain along the x/y direction (Fig. S10). Their location was measured as  $ \sim $50  $ \mu $m away from the top surface, which corresponds to the layer thickness (70  $ \mu $m) given the powder collapse after melting. Thus, the chain-like nanoparticle is considered as the consequence of the added Y $ _{2} $O $ _{3} $ which was segregated at the grooves of dendrites on the TiAl powder surface (Fig. 2c). This means that they were not stirred uniformly within the melt pool.

The stirring of the fluid flow during the PBF-type AM process is provided by Marangoni shear stress and recoil pressure, which leads to a vortical turbulence with different directions in melt pool [67,68]. Due to the instantaneous interaction between electron beam and powders during multi-spot scanning, the cold rear of the melt pool is shorter than that in hatch scanning. It results in the shorter flow distance and faster change of flow direction for the multi-spot scan strategy. This contributes to a higher stirring effect and is thus beneficial to the nanoparticle dispersion.

A few lamellar colonies without the  $ \alpha_{2} $ lamellae decomposition were found in the multi-spot sample L70 (Fig. 12b). The absence of such phenomenon in L90 indicates that a smaller layer thickness in PBF-EB process helps to reduce the  $ \alpha_{2} $ decomposition within lamellar colonies. The substructures occurred in as-built samples implies that the internal stress would affect the microstructural degradation. Therefore, EBSD was used to obtain the phase constitution and GND map to elaborate the different behaviour between L70 and L90 in terms of the  $ \alpha_{2} $ decomposition, as shown in Fig. 16. The internal stress of  $ \gamma $-phase seems to be less than that of  $ \alpha_{2} $ and B_{2}, which is the result of degradation dominated by  $ \gamma $ formation to release the internal stress. This is more obvious in L90, corresponding to the more serious degradation. By comparing Fig. 16b with 16d, the interfacial stress and GND gradient at  $ \alpha_{2}/\gamma $ lamellae interface in L70 are lower than that in L90; this seems to explain satisfactorily the SEM observation in Fig. 12b.

Firstly, during PBF-EB process, the temperature of previous thermal cycles is significantly higher than that of the subsequent thermal cycles which is close to build temperature [69]. Thus, the L70 with the small layer thickness would be subjected to more thermal cycles at lower temperatures than the L90, which helped to reduce the interfacial stress. The higher interfacial stress in L90 would raise the interfacial energy by destroying the coherent relationship of  $ \alpha_{2} $ and  $ \gamma $ [49], providing a higher driving force for the  $ \alpha_{2} $ lamellae decomposition. Secondly,  $ \alpha_{2} $ lamellae decomposition is a displacive-diffusive transformation by diffusion controlled ledge migration along the  $ \alpha_{2}/\gamma $ interface [70,71]. Larger GND gradient (i.e. stress gradient) in L90 would induce larger chemical potential gradient [72], which promotes the interaction of dislocations to form sub-grains (Fig. 13c) contributing to the  $ \gamma $ lamellae nucleation and drives the diffusion of atoms relatively fast to accelerate transition of  $ \alpha_{2}\rightarrow\gamma $ lamellae via ledge migration. In addition, the solidified layer of L70 is closer to the heat source of thermal cycles, raising the re-heat temperature to the level of over  $ T_{\alpha} $ of  $ \gamma $-TiAl alloy (Fig. S_{9}) [73]. Thermodynamically, this helps to preserve the  $ \alpha_{2} $ lamellae.

## 5. Conclusions

The multi-spot melt strategy coupled with the smaller layer thickness was used to additively manufacture  $ Y_{2}O_{3}/TiAl $ nanocomposite via the electron beam powder bed fusion (PBF-EB). From the detailed microstructure and property characterisations, the following conclusions can be drawn:

(1) Both the hatch melt and multi-spot samples exhibit a duplex microstructure. By contrast, multi-spot melt strategy helps to achieve a finer lamellar spacing as well as lower fraction of  $ \gamma $ and B_{2} phase for  $ Y_{2}O_{3} $ reinforced TiAl nanocomposite with smaller and more dispersed nanoparticles.

(2) A good balance of high-temperature strength of  $ 556 \pm 11 $ MPa and room-temperature fracture toughness of  $ 16.5 \pm 0.3 $ MPa\sqrtm in PBF-EB Y₂O₃/TiAl nanocomposite can be obtained in the multi-spot melt sample.

(3) Thermal cycling induced by the next adjacent layers, is the root cause for the lamellar colony degradation. Using small layer thickness contributes to the internal stress reduction due to the prolonged thermal cycles at low temperature, which also helps to reduce the  $ \alpha_{2} $ degradation within the colony.

(4) Two types of rod-like  $ Y_{2}O_{3} $ with monoclinic and spherical  $ Y_{2}O_{3} $ with cubic crystal system are identified, exhibiting either a semi-coherent or coherent type interface. The clean  $ Y_{2}O_{3}/TiAl $ interface with no twins or dislocations creates a strong interfacial
Fig. 16. EBSD phase distribution maps of (a) L90 and (c) L70; corresponding GND maps of (b) L90 and (d) L70; inserts in (b) and (d) showing the GND density profile across  $ \alpha_{2} $ lamellae from points A to A' and points B to B'. GND was calculated by OIM software and the considered slip systems for TiAl [64] are listed in Table S_{3}.

bonding. Dislocation tangles were formed only in the  $ \gamma $ lamellae and grains of hatch melt sample.

## CRediT Authorship

B. Gao: Investigation, Formal analysis, Writing - original draft, Visualization. H. Peng: Conceptualization, Supervision, Funding acquisition. H. Yue: Conceptualization, Supervision, Funding acquisition. H. Guo: Supervision, Resources. C. Wang: Conceptualization. B. Chen: Conceptualization, Supervision, Writing - original draft, Writing - review & editing, Funding acquisition.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data Availability

Data will be made available on request.

## Acknowledgements

This work was supported by the National Science and Technology Major Project (J2019-VII-0016–0157); the National Natural Science Foundation of China (Grant No. 51831001 and 52001143); the National Key Research and Development Program of China (2021YFB3700501); the UK's Engineering and Physical Sciences Research Council, EPSRC First Grant Scheme EP/P025978/1 and Early Career Fellowship Scheme EP/R043973/1. A special thank you is given to Prof. Sheng-kai Gong (BUAA) and Prof. Jun-pin Lin (SKLAMM, USTB) who provide continuous resources to foster the research collaboration.

## Associated content

The Supporting Information is available at the Supplementary Material File.

Representative SEM micrographs of Ti-48Al-2Cr-2 Nb and Ti-46Al-4 Nb-0.5Mo-0.2Si-0.05B alloy (Fig. S_{1}). Tensile and fracture toughness specimen dimensions (Fig. S_{2}); Lack-of-fusion defect as observed in the hatch melt sample (Fig. S_{3}); Additional TEM and HRTEM results for phase and twin identifications (Fig. S_{4}); Engineering stress-strain curves of the multi-spot sample L90 (Fig. S_{5}); SEM fractography of L70 and L90 specimens (Fig. S_{6}); Mechanical twins as observed by BSE-SEM in L70 sample (Fig. S_{7}); Work hardening rate of the multi-spot sample (Fig. S_{8}); Phase diagram of Ti-4822 (Fig. S_{9}); Chain-like pattern observed at the top layer in the hatch melt sample (Fig. S_{10}); Tabular data for plotting the tensile properties in Fig. 15 (Table S_{1}); Materials constants and parameters (Table S_{2}); Slip systems used to calculate the GND density (Table S_{3}).

## Appendix A. Supporting information

## Supplementary Material

## References

[1] M. Shahedi Asl, B. Nayebi, M. Farvizi, R. Alaghmandfard, M. Shokouhimehr, G. D. Janaki Ram, M. Mohammadi, Formation of Al–Al₂O₃ core–shell nanosphere chains during electron beam melting of \gamma-TiAl, Intermetallics 136 (2021)

[2] R. Gao, H. Peng, H. Guo, B. Chen, An innovative way to fabricate  $ \gamma $-TiAl blades and their failure mechanisms under thermal shock, Scr. Mater. 203 (2021), 114092.

[3] B. Stegman, B. Yang, Z. Shang, J. Ding, T. Sun, J. Lopez, W. Jarosinski, H. Wang, X. Zhang, Reactive introduction of oxide nanoparticles in additively manufactured 718 Ni alloys with improved high temperature performance, J. Alloy. Compd. 920 (2022), 165846.

[4] C. Guo, Z. Yu, X. Hu, G. Li, F. Zhou, Z. Xu, S. Han, Y. Zhou, R.M. Ward, Q. Zhu, Y_{2}O_{3} nanoparticles decorated IN738LC superalloy manufactured by laser powder bed fusion: cracking inhibition, microstructures and mechanical properties, Compos. Part B Eng. 230 (2022), 109555.

[5] M. Ghayoor, K. Lee, Y. He, C. hung Chang, B.K. Paul, S. Pasebani, Selective laser melting of austenitic oxide dispersion strengthened steel: processing, microstructural evolution and strengthening mechanisms, Mater. Sci. Eng. A 788 (2020), 139532.

[6] X. Wang, L.J. Zhang, J. Ning, S. Li, L.L. Zhang, J. Long, Hierarchical grain refinement during the laser additive manufacturing of Ti-6Al-4V alloys by the addition of micron-sized refractory particles, Addit. Manuf. 45 (2021), 102045

[7] J.A. Glerum, A. De Luca, M.L. Schuster, C. Kenel, C. Leinenbach, D.C. Dunand, Effect of oxide dispersoids on precipitation-strengthened Al-1.7Zr (wt%) alloys produced by laser powder-bed fusion, Addit. Manuf. 56 (2022), 102933.

[8] M. Shokouhimehr, S.A. Delbari, A.S. Namini, E. Taghizadeh, S. Jung, J.H. Cho, Q. Van, Le, J.H. Cha, S.Y. Kim, H.W. Jang, Nanostructure and nanoindentation study of pulse electric-current sintered TiB2–SiC–Cf composite, Sci. Rep. 13 (2023) 1–13.

[9] T.P. Nguyen, Z. Hamidzadeh Mahaseni, M. Dashti Germi, S.A. Delbari, Q. Van Le, Z. Ahmadi, M. Shokouhimehr, M. Shahedi Asl, A. Sabahi Namini, Densification behavior and microstructure development in  $ TiB_{2} $ ceramics doped with h-BN, Ceram. Int. 46 (2020) 18970–18975.

[10] S. Xiao, Y. Guo, Z. Liang, X. Wang, J. Yang, X. Wang, L. Xu, J. Tian, Y. Chen, The effect of nano-Y_{2}O_{3} addition on tensile properties and creep behavior of as-cast TiAl alloy, J. Alloy. Compd. 825 (2020), 153852.

[11] Y. Wu, S.K. Hwang, Microstructural refinement and improvement of mechanical properties and oxidation resistance in EPM TiAl-based intermetallics with yttrium addition, Acta Mater. 50 (2002) 1479–1493.

[12] A. Kostov, B. Friedrich, Predicting thermodynamic stability of crucible oxides in molten titanium and titanium alloys, Comput. Mater. Sci. 38 (2006) 374–385.

[14] B. Gao, H. Peng, Y. Liang, J. Lin, B. Chen, Electron beam melted TiC/high Nb-TiAl nanocomposite: microstructure and mechanical property, Mater. Sci. Eng. A. 811 (2021), 141059.

[13] C. Kenel, A. De Luca, S.S. Joglekar, C. Leinenbach, D.C. Dunand, Evolution of Y_{2}O_{3} dispersoids during laser powder bed fusion of oxide dispersion strengthened Ni-Cr-Al-Ti \gamma/\gamma′ superalloy, Addit. Manuf. 47 (2021), 102224.

[15] H. Yue, H. Peng, G. Fan, J. Yang, H. Chen, X. Fang, Microstructure and mechanical properties of Y_{2}O_{3}-bearing Ti–48Al–2Cr–2Nb alloy prepared by selective electron beam melting, Mater. Sci. Eng. A. 840 (2022), 142960.

[16] Y.W. Kim, Gammalloy materials—processes—application technology, Jom 69 (2017) 2563–2564.

[17] Y.K. Kim, J.K. Hong, K.A. Lee, Enhancing the creep resistance of electron beam melted gamma Ti–48Al–2Cr–2Nb alloy by using two-step heat treatment, Intermetallics 121 (2020), 106771.

[18] W. Kan, B. Chen, C. Jin, H. Peng, J. Lin, Microstructure and mechanical properties of a high Nb-TiAl alloy fabricated by electron beam melting, Mater. Des. 160 (2018) 611–623.

[19] A.R. Balachandramurthi, J. Olsson, J. Ålgårdh, A. Snis, J. Moverare, R. Pederson, Microstructure tailoring in electron beam powder bed fusion additive manufacturing and its potential consequences, Results Mater 1 (2019), 100017.

[20] M. Galati, S. Defanti, A. Saboori, G. Rizza, E. Tognoli, N. Vincenzi, A. Gatto, L. Iuliano, An investigation on the processing conditions of Ti-6Al-2Sn-4Zr-2Mo by electron beam powder bed fusion: Microstructure, defect distribution, mechanical properties and dimensional accuracy, Addit. Manuf. 50 (2022).

[21] X. Zhao, A. Rashid, A. Strondl, C. Hulme-Smith, N. Stenberg, S. Dadbakhsh, Role of superficial defects and machining depth in tensile properties of electron beam melting (EBM) made inconel, 718, J. Mater. Eng. Perform. 30 (2021) 2091–2101.

[22] N. Raghavan, R. Dehoff, S. Pannala, S. Simunovic, M. Kirka, J. Turner, N. Carlson, S.S. Babu, Numerical modeling of heat-transfer and the influence of process parameters on tailoring the grain morphology of IN718 in electron beam additive manufacturing, Acta Mater. 112 (2016) 303–314.

[23] M.M. Kirka, Y. Lee, D.A. Greeley, A. Okello, M.J. Goin, M.T. Pearce, R.R. Dehoff, Strategy for texture management in metals additive manufacturing, Jom 69 (2017) 523–531.

[24] A.R. Balachandramurthi, J. Moverare, N. Dixit, D. Deng, R. Pederson, Microstructural influence on fatigue crack propagation during high cycle fatigue testing of additively manufactured Alloy 718, Mater. Charact. 149 (2019) 82–94.

[25] X. Zhao, S. Dadbakhsh, A. Rashid, Contouring strategies to improve the tensile properties and quality of EBM printed Inconel 625 parts, J. Manuf. Process. 62 (2021) 418–429.

[26] S. Goel, H. Mehtani, S.W. Yao, I. Samajdar, U. Klement, S. Joshi, As-built and post-treated microstructures of an electron beam melting (EBM) produced nickel-based superalloy, Metall. Mater. Trans. A Phys. Metall. Mater. Sci. 51 (2020) 6546–6559.

[27] A. Simchi, Direct laser sintering of metal powders: mechanism, kinetics and microstructural features, Mater. Sci. Eng. A 428 (2006) 148–158.

[28] H. Bikas, A.K. Lianos, P. Stavropoulos, A design framework for additive manufacturing, Int. J. Adv. Manuf. Technol. 103 (2019) 3769–3783.

[29] J. Karlsson, A. Snis, H. Engqvist, J. Lausmaa, Characterization and comparison of materials produced by Electron Beam Melting (EBM) of two different Ti-6Al-4V powder fractions, J. Mater. Process. Technol. 213 (2013) 2109–2118.

[30] J. Li, X. Cheng, Z. Li, X. Zong, X.H. Chen, S.Q. Zhang, H.M. Wang, Microstructures and mechanical properties of laser additive manufactured Al-5Si-1Cu-Mg alloy with different layer thicknesses, J. Alloy. Compd. 789 (2019) 15–24.

[31] S. Dadbakhsh, L. Hao, Effect of layer thickness in selective laser melting on microstructure of Al/5 wt% Fe_{2}O_{3} powder consolidated parts, Sci. World J. 2014 (2014).

[32] S.K. Vajpai, K. Ameyama, A novel powder metallurgy processing approach to prepare fine-grained Ti-rich TiAl-based alloys from pre-alloyed powders, Intermetallics 42 (2013) 146–155.

[33] Y. Yao, C. Xing, H. Peng, H. Guo, B. Chen, Solidification microstructure and tensile deformation mechanisms of selective electron beam melted Ni3Al-based alloy at room and elevated temperatures, Mater. Sci. Eng. A. 802 (2021), 140629.

[34] S. Karagöz, I. Liem, E. Bischoff, H.F. Fischmeister, Determination of carbide and matrix compositions in high-speed steels by analytical electron microscopy, Metall. Trans. A 20 (1989) 2695–2701.

[35] W.J. Sames, F.A. List, S. Pannala, R.R. Dehoff, S.S. Babu, The metallurgy and processing science of metal additive manufacturing, Int. Mater. Rev. 61 (2016) 315–360.

[36] D. Gu, H. Wang, D. Dai, P. Yuan, W. Meiners, R. Poprawe, Rapid fabrication of Al-based bulk-form nanocomposites with novel reinforcement and enhanced performance by selective laser melting, Scr. Mater. 96 (2015) 25–28.

[37] A. Plotkowski, M.M. Kirka, S.S. Babu, Verification and validation of a rapid heat transfer calculation methodology for transient melt pool solidification conditions in powder bed metal additive manufacturing, Addit. Manuf. 18 (2017) 256–268.

[38] C. Kenel, G. Dasargyri, T. Bauer, A. Colella, A.B. Spierings, C. Leinenbach, K. Wegener, Selective laser melting of an oxide dispersion strengthened (ODS)  $ \gamma $-TiAl alloy towards production of complex structures, Mater. Des. 134 (2017) 81–90.

[39] J.P. Monchoux, J. Luo, T. Voisin, A. Couret, Deformation modes and size effect in near- $ \gamma $ TiAl alloys, Mater. Sci. Eng. A. 679 (2017) 123–132.

[40] A. Denquin, S. Naka, Phase transformation mechanisms involved in two-phase TiAl-based alloys - I. Lamellar structure formation, Acta Mater. 44 (1996) 343–352.

[41] F. Wagner, N. Bozzolo, O. Van Landuyt, T. Grosdidier, Evolution of recrystallisation texture and microstructure in low alloyed titanium sheets, Acta Mater. 50 (2002) 1245–1259.

[42] T. Kawabata, Y. Takezono, T. Kanai, O. Izumi, Bend tests and fracture mechanism of TiAl single crystals at 293–1073 K, Acta Met. 36 (1988) 963–975.

[43] K.S. Chan, Y.W. Kim, Effects of lamellae spacing and colony size on the fracture resistance of a fully-lamellar TiAl alloy, Acta Metall. Mater. 43 (1995) 439–451.

[44] G. Chen, Y. Peng, G. Zheng, Z. Qi, M. Wang, H. Yu, C. Dong, C.T. Liu, Polysynthetic twinned TiAl single crystals for higher-ture applications, Nat. Mater. 15 (2016) 876–881.

[45] H. Zhu, D.Y. Seo, K. Maruyama, P. Au, Microstructural stability of fine-grained fully lamellar XD TiAl alloys by step aging, Metall. Mater. Trans. A 36A (2005) 1339–1351.

[46] K.T. Venkateswara Rao, Y.W. Kim, C.L. Muhlstein, R.O. Ritchie, Fatigue-crack growth and fracture resistance of a two-phase ( $ \gamma + \alpha 2 $) TiAl alloy in duplex and lamellar microstructures, Mater. Sci. Eng. A. 192–193 (1995) 474–482.

[47] H. Zhu, D.Y. Seo, K. Maruyama, P. Au, Effect of Initial microstructure on microstructural instability and creep resistance of XD TiAl alloys, Metall. Mater. Trans. A 37A (2006) 3149–3159.

[48] T.T. Cheng, M.H. Loretto, The decomposition of the beta phase in Ti-44Al-8Nb and Ti-44Al-4Nb-4Zr-0.2Si alloys, Acta Mater. 46 (1998) 4801–4819.

[49] G. Sharma, R.V. Ramanujan, G.P. Tiwari, Instability mechanisms in lamellar microstructures, Acta Mater. 48 (2000) 875–889.

[50] G.H. Cao, A.M. Russell, C.G. Oertel, W. Skrotzki, Microstructural evolution of TiAl-based alloys deformed by high-pressure torsion, Acta Mater. 98 (2015) 103–112.

[51] H. GLEITERT, The formation of annealing twins, Acta Met. (1969) 1421–1428.

[52] Y.F. Wen, J. Sun, Generalized planar fault energies and mechanical twinning in gamma TiAl alloys, Scr. Mater. 68 (2013) 759–762.

[53] H.Y. Kim, K. Maruyama, Parallel twinning during creep deformation in soft orientation PST crystal of TiAl alloy, Acta Mater. 49 (2001) 2635–2643.

[54] S. Goel, M. Neikter, J. Capek, E. Polatidis, M.H. Colliander, S. Joshi, R. Pederson, Residual stress determination by neutron diffraction in powder bed fusion-built Alloy 718: Influence of process parameters and post-treatment, Mater. Des. 195 (2020), 109045.

[55] W.J. Zhang, B.V. Reddy, S.C. Deevi, Physical properties of TiAl-base alloys, Scr. Mater. 45 (2001) 645–651.

[56] L. Settineri, P.C. Priarone, M. Arft, D. Lung, T. Stoyanov, An evaluative approach to correlate machinability, microstructures, and material properties of gamma titanium aluminides, CIRP Ann. - Manuf. Technol. 63 (2014) 57–60.

[57] J. Lapin, T. Pelachová, O. Bajana, High temperature deformation behaviour and microstructure of cast in-situ TiAl matrix composite reinforced with carbide particles, J. Alloy. Compd. 797 (2019) 754–765.

[58] A. Chauniyal, R. Janisch, Influence of lattice misfit on the deformation behaviour of  $ \alpha2/\gamma $ lamellae in TiAl alloys, Mater. Sci. Eng. A 796 (2020).

[59] Z. Gao, J. Yang, Y. Wu, R. Hu, S.L. Kim, Y.W. Kim, A. Newly, Generated nearly lamellar microstructure in cast Ti-48Al-2Nb-2Cr alloy for high-temperature strengthening, Metall. Mater. Trans. A Phys. Metall. Mater. Sci. 50 (2019) 5839–5852.

[60] A. Sanaty-Zadeh, Comparison between current models for the strength of particulate-reinforced metal matrix nanocomposites with emphasis on consideration of Hall-Petch effect, Mater. Sci. Eng. A. 531 (2012) 112–118

[61] C.S. Goh, J. Wei, L.C. Lee, M. Gupta, Properties and deformation behaviour of Mg-Y_{2}O_{3} nanocomposites, Acta Mater. 55 (2007) 5115–5121.

[62] C. Hofmeister, M. Klimov, T. Deleghanty, K. Cho, Y. Sohn, Quantification of nitrogen impurity and estimated Orowan strengthening through secondary ion mass spectroscopy in aluminum cryomilled for extended durations, Mater. Sci. Eng. A 648 (2015) 412–417.

[63] G. Zheng, B. Tang, S. Zhao, W.Y. Wang, X. Chen, L. Zhu, J. Li, Evading the strength-ductility trade-off at room temperature and achieving ultrahigh plasticity at 800^\circC in a TiAl alloy, Acta Mater. 225 (2022), 117585.

[64] F. Appel, H. Clemens, F.D. Fischer, Modeling concepts for intermetallic titanium aluminides, Prog. Mater. Sci. 81 (2016) 55–124.

## B. Gao et al.

[65] C. Ma, L. Chen, C. Cao, X. Li, Nanoparticle-induced unusual melting and solidification behaviours of metals, Nat. Commun. 8 (2017) 1–7.

[66] C. Körner, Additive manufacturing of metallic components by selective electron beam melting - a review, Int. Mater. Rev. 61 (2016) 361–377.

[67] S.A. Khairallah, A.T. Anderson, A. Rubenchik, W.E. King, Laser powder-bed fusion additive manufacturing: physics of complex melt flow and formation mechanisms of pores, spatter, and denudation zones, Acta Mater. 108 (2016) 36–45.

[68] Y.S. Lee, W. Zhang, Modeling of heat transfer, fluid flow and solidification microstructure of nickel-base superalloy fabricated by laser powder bed fusion, Addit. Manuf. 12 (2016) 178–188.

[69] J. Romano, L. Ladani, J. Razmi, M. Sadowski, Temperature distribution and melt geometry in laser and electron-beam melting processes - a comparison among common materials, Addit. Manuf. 8 (2015) 1–11.

[70] F. Appel, J.D.H. Paul, M. Oehring, U. Fröbel, U. Lorenz, Creep behavior of TiAl alloys with enhanced high-temperature capability, Metall. Mater. Trans. A Phys. Metall. Mater. Sci. 34 A (2003) 2149–2164.

[71] T. Klein, L. Usategui, B. Rashkova, M.L. Nó, J. San Juan, H. Clemens, S. Mayer, Mechanical behavior and related microstructural aspects of a nano-lamellar TiAl alloy at elevated temperatures, Acta Mater. 128 (2017) 440–450.

[72] X. Wei, J.W. Kysar, Residual plastic strain recovery driven by grain boundary diffusion in nanocrystalline thin films, Acta Mater. 59 (2011) 3937–3945.

[73] E. Cakmak, P. Nandwana, D. Shin, Y. Yamamoto, M.N. Gussev, I. Sen, M.H. Seren, T.R. Watkins, J.A. Haynes, A comprehensive study on the fabrication and characterization of Ti–48Al–2Cr–2Nb preforms manufactured using electron beam melting, Materialia 6 (2019), 100284.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

Additive Manufacturing 72 (2023) 103650

Additive Manufacturing

Electron beam powder bed fusion of Y₂O₃/\gamma-TiAl nanocomposite with balanced strength and toughness

## Keywords
Gamma-TiAl
Additive manufacturing
Electron beam powder bed fusion
Microstructure
Mechanical properties
## ABSTRACT
## CRediT Authorship
## Supplementary Material

## ABSTRACT

https://doi.org/10.1016/j.addma.2023.103650 2214-8604/© 2023 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/). Mechanical twin is formed via dislocations slip along multiple 1/6 < 11 $ \overline{2} $[111] of  $ \gamma $ under stress and it has a nanometre thickness [51]. The parallel twins and twin intersections with a thickness less than 10 nm within  $ \gamma $ lamellae and equiaxed  $ \gamma $ grains, as shown in Fig. 5 g and e, are mechanical twins. The nanotwins contrast as observed in the BSE-SEM image (Fig. S_{7}) indicates that these twins are not caused by the TEM sample preparation. where  $ \eta $ is a given strengthening coefficient close to 1.25.  $ \Delta\alpha $ is the difference between TiAl alloy matrix and  $ Y_{2}O_{3} $ particles.  $ \Delta T $ is the difference between process temperature ( $ \sim $1160 ^\circC/1433 K) and test temperature (800 ^\circC/1073 K).  $ V_{p} $ is the volume fraction of nanoparticles. In addition, the much delayed drop in work-hardening rate during the tensile test at 800 ^\circC (Fig. S_{8}) indicates the combined effect of dislocations and twins in PBF-EB Y₂O₃/TiAl nanocomposite. Deformation (1) Both the hatch melt and multi-spot samples exhibit a duplex microstructure. By contrast, multi-spot melt strategy helps to achieve a finer lamellar spacing as well as lower fraction of  $ \gamma $ and B_{2} phase for  $ Y_{2}O_{3} $ reinforced TiAl nanocomposite with smaller and more dispersed nanoparticles. (2) A good balance of high-temperature strength of  $ 556 \pm 11 $ MPa and room-temperature fracture toughness of  $ 16.5 \pm 0.3 $ MPa\sqrtm in PBF-EB Y₂O₃/TiAl nanocomposite can be obtained in the multi-spot melt sample. [1] M. Shahedi Asl, B. Nayebi, M. Farvizi, R. Alaghmandfard, M. Shokouhimehr, G. D. Janaki Ram, M. Mohammadi, Formation of Al–Al₂O₃ core–shell nanosphere chains during electron beam melting of \gamma-TiAl, Intermetallics 136 (2021) [4] C. Guo, Z. Yu, X. Hu, G. Li, F. Zhou, Z. Xu, S. Han, Y. Zhou, R.M. Ward, Q. Zhu, Y_{2}O_{3} nanoparticles decorated IN738LC superalloy manufactured by laser powder bed fusion: cracking inhibition, microstructures and mechanical properties, Compos. Part B Eng. 230 (2022), 109555. [10] S. Xiao, Y. Guo, Z. Liang, X. Wang, J. Yang, X. Wang, L. Xu, J. Tian, Y. Chen, The effect of nano-Y_{2}O_{3} addition on tensile properties and creep behavior of as-cast TiAl alloy, J. Alloy. Compd. 825 (2020), 153852. [13] C. Kenel, A. De Luca, S.S. Joglekar, C. Leinenbach, D.C. Dunand, Evolution of Y_{2}O_{3} dispersoids during laser powder bed fusion of oxide dispersion strengthened Ni-Cr-Al-Ti \gamma/\gamma′ superalloy, Addit. Manuf. 47 (2021), 102224. [15] H. Yue, H. Peng, G. Fan, J. Yang, H. Chen, X. Fang, Microstructure and mechanical properties of Y_{2}O_{3}-bearing Ti–48Al–2Cr–2Nb alloy prepared by selective electron beam melting, Mater. Sci. Eng. A. 840 (2022), 142960. [31] S. Dadbakhsh, L. Hao, Effect of layer thickness in selective laser melting on microstructure of Al/5 wt% Fe_{2}O_{3} powder consolidated parts, Sci. World J. 2014 (2014). [61] C.S. Goh, J. Wei, L.C. Lee, M. Gupta, Properties and deformation behaviour of Mg-Y_{2}O_{3} nanocomposites, Acta Mater. 55 (2007) 5115–5121.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

ELSEVIER

Contents lists available at ScienceDirect

journal homepage: www.elsevier.com/locate/addma

Electron beam powder bed fusion of Y₂O₃/γ-TiAl nanocomposite with balanced strength and toughness

Keywords:
Gamma-TiAl
Additive manufacturing
Electron beam powder bed fusion
Microstructure
Mechanical properties

A B S T R A C T

* Corresponding authors.

E-mail addresses: penghui@buaa.edu.cn (H. Peng), bo.chen@leicester.ac.uk (B. Chen).

Received 23 February 2023; Received in revised form 28 May 2023; Accepted 7 June 2023

Available online 10 June 2023

Mechanical twin is formed via dislocations slip along multiple 1/6 < 11 $ \overline{2} $[111] of  $ \gamma $ under stress and it has a nanometre thickness [51]. The parallel twins and twin intersections with a thickness less than 10 nm within  $ \gamma $ lamellae and equiaxed  $ \gamma $ grains, as shown in Fig. 5 g and e, are mechanical twins. The nanotwins contrast as observed in the BSE-SEM image (Fig. S7) indicates that these twins are not caused by the TEM sample preparation.

where  $ \eta $ is a given strengthening coefficient close to 1.25.  $ \Delta\alpha $ is the difference between TiAl alloy matrix and  $ Y_{2}O_{3} $ particles.  $ \Delta T $ is the difference between process temperature ( $ \sim $1160 °C/1433 K) and test temperature (800 °C/1073 K).  $ V_{p} $ is the volume fraction of nanoparticles.

In addition, the much delayed drop in work-hardening rate during the tensile test at 800 °C (Fig. S8) indicates the combined effect of dislocations and twins in PBF-EB Y₂O₃/TiAl nanocomposite. Deformation

(1) Both the hatch melt and multi-spot samples exhibit a duplex microstructure. By contrast, multi-spot melt strategy helps to achieve a finer lamellar spacing as well as lower fraction of  $ \gamma $ and B2 phase for  $ Y_{2}O_{3} $ reinforced TiAl nanocomposite with smaller and more dispersed nanoparticles.

(2) A good balance of high-temperature strength of  $ 556 \pm 11 $ MPa and room-temperature fracture toughness of  $ 16.5 \pm 0.3 $ MPa√m in PBF-EB Y₂O₃/TiAl nanocomposite can be obtained in the multi-spot melt sample.

CRediT authorship contribution statement

Supplementary data associated with this article can be found in the online version at doi:10.1016/j.addma.2023.103650.

[1] M. Shahedi Asl, B. Nayebi, M. Farvizi, R. Alaghmandfard, M. Shokouhimehr, G. D. Janaki Ram, M. Mohammadi, Formation of Al–Al₂O₃ core–shell nanosphere chains during electron beam melting of γ-TiAl, Intermetallics 136 (2021)

[4] C. Guo, Z. Yu, X. Hu, G. Li, F. Zhou, Z. Xu, S. Han, Y. Zhou, R.M. Ward, Q. Zhu, Y2O3 nanoparticles decorated IN738LC superalloy manufactured by laser powder bed fusion: cracking inhibition, microstructures and mechanical properties, Compos. Part B Eng. 230 (2022), 109555.

[10] S. Xiao, Y. Guo, Z. Liang, X. Wang, J. Yang, X. Wang, L. Xu, J. Tian, Y. Chen, The effect of nano-Y2O3 addition on tensile properties and creep behavior of as-cast TiAl alloy, J. Alloy. Compd. 825 (2020), 153852.

[13] C. Kenel, A. De Luca, S.S. Joglekar, C. Leinenbach, D.C. Dunand, Evolution of Y2O3 dispersoids during laser powder bed fusion of oxide dispersion strengthened Ni-Cr-Al-Ti γ/γ′ superalloy, Addit. Manuf. 47 (2021), 102224.

[15] H. Yue, H. Peng, G. Fan, J. Yang, H. Chen, X. Fang, Microstructure and mechanical properties of Y2O3-bearing Ti–48Al–2Cr–2Nb alloy prepared by selective electron beam melting, Mater. Sci. Eng. A. 840 (2022), 142960.

[31] S. Dadbakhsh, L. Hao, Effect of layer thickness in selective laser melting on microstructure of Al/5 wt% Fe2O3 powder consolidated parts, Sci. World J. 2014 (2014).

[61] C.S. Goh, J. Wei, L.C. Lee, M. Gupta, Properties and deformation behaviour of Mg-Y2O3 nanocomposites, Acta Mater. 55 (2007) 5115–5121.

[63] G. Zheng, B. Tang, S. Zhao, W.Y. Wang, X. Chen, L. Zhu, J. Li, Evading the strength-ductility trade-off at room temperature and achieving ultrahigh plasticity at 800°C in a TiAl alloy, Acta Mater. 225 (2022), 117585.