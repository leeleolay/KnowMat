DOI: 10.1016/j.ijplas.2024.104142

# Multiscale plastic deformation in additively manufactured FeCoCrNiMo $ _{x} $ high-entropy alloys to achieve strength–ductility synergy at elevated temperatures

Danyang Lin $ ^{a} $, Jixu Hu $ ^{a} $, Renhao Wu $ ^{b,*} $, Yazhou Liu $ ^{a,d} $, Xiaoqing Li $ ^{c} $, Man Jae SaGong $ ^{b} $, Caiwang Tan $ ^{a} $, Xiaoguo Song $ ^{a,*} $, Hyoung Seop Kim $ ^{b,d,e,f,*} $

 $ ^{a} $ State Key Laboratory of Precision Welding & Joining of Materials and Structures, Harbin Institute of Technology, Harbin 150001, China

 $ ^{b} $ Graduate Institute of Ferrous & Eco Materials Technology, Pohang University of Science & Technology, Pohang 37673, Korea

 $ ^{c} $ Department of Materials Science and Engineering, Applied Materials Physics, KTH - Royal Institute of Technology, Stockholm SE-10044, Sweden

 $ ^{d} $ Department of Materials Science & Engineering, Pohang University of Science & Technology, Pohang 37673, Korea

 $ ^{e} $ Advanced Institute for Materials Research (WPI-AIMR), Tohoku University, Sendai 980-8577, Japan

 $ ^{f} $ Institute for Convergence Research and Education in Advanced Technology, Yonsei University, Seoul 03722, South Korea

## ARTICLE INFO

## Keywords

Additively manufactured FeCoCrNiMo $ _{x} $

Multiscale plastic deformation

Deformation twinning

Molecular dynamics simulation

Elevated temperature

## Abstract

The application of structural metals in extreme environments necessitates materials with superior mechanical properties. Mo-doped FeCoCrNi high-entropy alloys (HEAs) have emerged as potential candidates for use in such demanding environments. This study investigates the high-temperature performance of FeCoCrNiMo $ _{x} $ HEAs with varying Mo contents (x = 0, 0.1, 0.3, and 0.5) prepared by laser powder bed fusion additive manufacturing. The mechanical properties were evaluated at room and 600 ^\circC temperatures, and the microstructures were characterized using scanning electron microscopy, electron backscatter diffraction, energy dispersive X-ray spectroscopy, and transmission electron microscopy. The intrinsic dislocation cell patterning, solid-solution strengthening, nanoprecipitation, and twinning effects collectively modulated the plastic deformation behavior of the samples. The high-temperature mechanical performance was comprehensively analyzed in conjunction with ab initio calculations and molecular dynamics simulations to reveal the origin of the experimentally observed strength–ductility synergy of FeCoCrNiMo $ _{0.3} $. This study has significant implications for FeCoCrNiMo $ _{x} $ HEAs and extends our understanding of the structural origins of the exceptional mechanical properties of additively manufactured HEAs.

## 1. Introduction

The pursuit of advanced structural metals that perform reliably in high-temperature environments remains a challenge. High-

entropy alloys (HEAs) have significantly broadened the compositional space of metals owing to their unique physical, chemical, and mechanical properties. Face-centered cubic (FCC) FeCoCrNi-based HEAs exhibit excellent mechanical properties, including high strength, hardness, and wear resistance. (Beyr amali Kivy and Asle Zaeem, 2017; He et al., 2018). The most renowned variant, equiatomic FeCoCrNiMn (Shahmir et al., 2023), tends to form with a low stacking fault energy (SFE) of  $ \sim $20 mJ/m $ ^{2} $ (Huang et al., 2015). $ ^{1} $

However, despite the satisfactory mechanical properties of single-phase FeCoCrNi-based HEAs at room and low temperatures (Gludovatz et al., 2014; Kuzminova et al., 2021; Liu et al., 2017), the high-temperature mechanical performance requires further improvement. For instance, Liao et al. (2023) explored the compression behavior of equimolar FeCoCrNi HEAs, and noticed a softening effect at elevated temperatures owing to increased grain boundary migration and thermal activation of the matrix. This pronounced softening effect significantly reduces the strength and plasticity of FeCoCrNi-based HEAs at 600 ^\circC (Lin et al., 2022). During deformation, nanoclusters cause cracks to form at the grain boundaries, leading to a loss of ductility at high temperatures. Similarly, the high-temperature tensile properties of FeCoCrNiMn show evident softening at 600–700 ^\circC, resulting in poor performance at high temperatures (Jo et al., 2022; Sun et al., 2022).

To enhance the high-temperature mechanical properties of HEAs, significant progress has been made in controlling precipitation (Yang et al., 2020) and alloying-element segregation at grain boundaries (Hou et al., 2022). Gan et al. (2024) introduced D022 nanoparticles into an FCC HEA, which increased the dislocation storage capability and strain hardening, greatly improving the tensile properties in the 600–700 ^\circC range. Researchers have also achieved improvements in strength and plasticity at 750 ^\circC by doping the FCC matrix with elements such as Ti, Nb, Ta, Mo, and W to reduce the SFE and introduce nanoscale L12 precipitates, resulting in various work-hardening behaviors (Gao et al., 2024). Therefore, adding trace elements and introducing nanoscale precipitates into the FCC matrix is a promising strategy for improving the high-temperature performance.

The addition of medium-atomic-size Mo to the FeCoCrNi matrix can induce precipitation strengthening in the solid-solution FCC phase and even trigger a eutectic precipitation reaction (Guo et al., 2020). Consequently, Mo-doped FeCoCrNi HEAs exhibit enhanced mechanical properties, including good wear resistance (Fan et al., 2024), corrosion resistance (Dai et al., 2020; Yen et al., 2024), and biocompatibility (Hiyama et al., 2024). By controlling the Mo content, phase selection can be achieved to alter the structure and properties of the HEAs, which is crucial for regulating the performance.

Dai et al. (2021) reported the effect of grain size on the mechanical properties of FeCoCrNiMo₀.₁. The mechanical performance at −196.15 ^\circC was superior to that at 0 ^\circC because of twinning-induced plasticity. By comparison, FeCoCrNiMo₀.₂ has a higher activation energy, and the matrix and precipitate phases segregate during deformation at elevated temperatures (Wu et al., 2018). The enhanced slip reversibility is attributed to improved slip planarity owing to the addition of Mo, which results in a decreased SFE and increased lattice friction stress and shear modulus. Moreover, the stacking-fault-mediated deformation mechanism in FeCoCrNiMo₀.₂ helps to inhibit fatigue-induced plastic deformation (Li et al., 2019). Cai et al. (2017) discovered that Mo-rich intermetallic compounds precipitate in FeCoCrNiMo₀.₂₃ upon annealing. However, the bonding force between the intermetallic compounds and matrix is weak, and the probability of stacking faults is reduced, thus suppressing the formation of deformation twins and resulting in a tradeoff between strength and ductility. Liu et al. (2016) found that in FeCoCrNiMo₀.₃, the precipitation of hard \sigma and \mu phases greatly strengthens the material (tensile strength of up to 1.2 GPa) without causing severe embrittlement. Shun et al. (2012) reported that with an increase in the Mo content in cast FeCoCrNiMoₓ, the strength increases, whereas the plasticity decreases. Aged FeCoCrNiMo₀.₈₅ has a higher hardness than aged FeCoCrNiMo₀.₃ and FeCoCrNiMo₀.₅ owing to the precipitation of a larger volume fraction of hard needle-like \sigma phases in the FCC matrix. However, these studies mostly focused on the influence of Mo on the mechanical properties, without considering the effect of temperature in detail. In particular, few studies have evaluated the high-temperature mechanical properties and microstructural evolution of FeCoCrNiMoₓ HEAs (Li et al., 2022; Wang et al., 2017), and systematic and in-depth studies on the high-temperature mechanical properties and intrinsic deformation mechanisms of FeCoCrNiMoₓ HEAs are lacking.

Laser-based additive manufacturing (L-AM) is an advanced precision manufacturing technique that facilitates high-throughput fabrication and offers significant opportunities for in situ materials design with tailored microstructures (Li et al., 2022). An et al. (2023) revealed that L-AM-processed FCC metals have hierarchical microstructures that exhibit several plastic deformation mechanisms, thereby enhancing the mechanical performance compared with conventionally fabricated counterparts. Notably, the unique dislocation cell patterns, which are caused by residual stresses arising from the large temperature gradient and thermal cycling during L-AM, significantly contribute to the strength (He et al., 2022; Kwon et al., 2022). Sui et al. (2022) investigated L-AM-processed FeCoCrNiMo and reported that its hierarchical eutectic and irregular lamellar structures resulted in high hardness and wear resistance. Furthermore, in our previous work, we demonstrated the capability of L-AM for fabricating FeCoCrNiMo $ _{x} $ (x = 0.3 and 0.5) HEAs with good mechanical properties (Lin et al., 2024, 2023). Deformation twinning and micro/nanoprecipitates such as  $ \sigma $ phases were observed when the Mo fraction exceeded 0.3.

In this study, we utilized laser powder bed fusion (L-PBF) additive manufacturing to fabricate a series of defect-free FeCoCrNiMo $ _{x} $ HEAs with varying Mo contents (x = 0, 0.1, 0.3, and 0.5). The mechanical properties and microstructural evolution were systematically investigated at room and elevated temperatures. The thermal stability and uniaxial tensile deformation behavior were studied by electron backscatter diffraction (EBSD) and transmission electron microscopy (TEM). Additionally, ab initio calculations and molecular

dynamics (MD) simulation models were established to quantify changes in the microscale lattice strain and stacking fault probability associated with plastic deformation. This work provides a quantitative assessment of the effects of the hierarchical microstructure on the mechanical response of L-PBF-processed FeCoCrNiMo $ _{x} $ HEAs, which is beneficial for enhancing their high-temperature performance as structural materials.

## 2. Materials and methods

## 2.1. Powder preparation and L-PBF process

To fabricate the FeCoCrNiMo $ _{x} $ HEAs (x = 0, 0.1, 0.3, and 0.5; Mo content = 0, 2.44, 6.98, and 11.11 at%, respectively), denoted as Mo_{0}, Mo_{1}, Mo_{3}, and Mo_{5}, respectively, equiatomic FeCoCrNi and FeCoCrNiMo powders with spherical particles (diameter: 15–53  $ \mu $m) were produced by gas atomization. The powders were then mixed at different molar ratios in a three-dimensional mixer at 40 rpm for 5 h under a protective Ar atmosphere (Fig. 1a). Next, L-PBF was conducted using a RENISHAW AM-400 platform with a preheating temperature of 120 ^\circC. The processing parameters were as follows: bidirectional scanning speed, 750 mm/s; laser power, 200 W; hatch spacing, 80  $ \mu $m (Mo_{0}, Mo_{1}, and Mo_{3}) or 70  $ \mu $m (Mo_{5}); layer thickness, 40  $ \mu $m; and rotation between layers, 67^\circ. Blocks with
Fig. 1. L-PBF additive manufacturing procedures and prepared samples for tensile tests: (a) different Mo content ratios are achieved by adjusting the ratio of FeCoCrNi and FeCoCrNiMo powders, (b) Schematic diagram of L-PBF process, (c) Size of tensile specimen at room temperature (dogbone shape) and high temperature (600 ^\circC, round rod shape).

dimensions of  $ 80 \times 40 \times 20 $ mm were fabricated (Fig. 1b).

## 2.2. Mechanical testing

Mechanical testing was conducted using dog-bone samples (room-temperature tests) or rod-shaped samples (high-temperature tests) (Fig. 1c). The samples were extracted from the center of the L-PBF-processed blocks via electrical discharge machining. Tensile tests were performed until failure using a 3910-type microcomputer-controlled electronic universal testing machine at a crosshead speed of 0.5 mm/min (initial strain rate:  $ \sim 3 \times 10^{-4} \, s^{-1} $).

## 2.3. Microstructural characterization

The microstructural characteristics and fracture surfaces of the tensile samples were characterized using field-emission scanning electron microscopy (SEM; ZEISS-EVO 18) in backscattered electron mode and EBSD. Field-emission TEM (FEI-Tecnai G2 F_{30}) and energy-dispersive X-ray spectroscopy (EDS) were used to analyze the microstructures and chemical compositions of the samples. The crystal structure and dislocation morphology of the matrix and secondary phases were characterized by TEM. The microstructural evolution of Mo_{5} was characterized by SEM, EBSD, EDS, and TEM.

## 2.4. Ab initio calculations and molecular dynamics (MD) simulations

Ab initio calculations were conducted using density functional theory (DFT) (Hohenberg and Kohn, 1964), employing the exact muffin-tin orbitals method to solve the Kohn–Sham equations (Andersen et al., 1995; Vitos, 2001; Vitos et al., 2000). The Perdew–Burke–Ernzerhof exchange–correlation functional was used for self-consistent determination of the charge density and total energy (Perdew et al., 1996). Given that the magnetic ordering temperature of FeCoCrNi is well below room temperature, all spin-polarized DFT calculations were performed assuming a paramagnetic state (Gyorffy et al., 1985). The paramagnetic state was described using a disordered local moment approach. The coherent potential approximation was employed to model the chemical disorder (Gyorffy, 1972; Vitos et al., 2001).

For SFE calculations, we followed the methodology described by Schönecker et al. (Schönecker et al., 2021). The thermal lattice expansion and magnetic contributions were considered to account for the temperature dependence of the SFE. Specifically, we derived the lattice expansion of the FCC phase by minimizing the free energy  $ F(V, T) = E^{\mathrm{PM}}(V) - TS^{\mathrm{PM}}(V) + F^{\mathrm{vib}}(V, T) $ over the atomic volume V for a given temperature T, where  $ E^{\mathrm{PM}} $ and  $ S^{\mathrm{PM}} $ are the total energy and magnetic entropy of the paramagnetic state, respectively, and  $ F^{\mathrm{vib}} $ is the vibrational free energy. Next, the FCC lattice parameter corresponding to a certain T was employed to calculate the SFE,
Fig. 2. Tensile properties of the L-PBF additively manufactured FeCoCrNiMox (x = 0, 0.1, 0.3, and 0.5) HEAs: (a) 25 ^\circC, (b) 600 ^\circC. “\infty” denotes the UTS point of sample. (c) Evolution of the work hardening rate samples over the true strain at 600 ^\circC, (d) Comparison of the ultimate tensile strength (UTS) and uniform elongation (UFE) at elevated temperature (600 ^\circC) of the additively manufactured FeCoCrNiMox in this work and some reported alloys (References for these data are given in the Supplementary Materials).

considering the contributions from  $ E^{\mathrm{PM}} $ and  $ S^{\mathrm{PM}} $.  $ F^{\mathrm{vib}} $ of the FCC phase was calculated using the Debye–Grüneisen model (Moruzzi et al., 1988).  $ S^{\mathrm{PM}} $ was calculated with consideration to the transverse degrees of freedom using the mean-field expression for uncorrelated magnetic moments (Grimvall, 1975).

The open-source MD simulation software, LAMMPS, is employed for the uniaxial stretching simulation (Plimpton, 1995). The potential function used is the modified embedded atom method (MEAM) potential for six elements (Ni-Cr-Co-Mo-V-Al) developed by Wang et al. (2023), and it is incorporated into the HEA model’s machine learning through a neural network. Liu et al. (2024) and (Shi et al., 2024) respectively used this potential function to verify the deformation mechanisms of medium entropy alloy (MEA) and HEAs, achieving ideal results. The uniaxial tensile simulations of the single crystal nanowire are conducted at two temperatures: 25 ^\circC and 600 ^\circC. For visualization, the open-source software OVITO is used.

To obtain atomic models with random elements distribution, we first conducted energy minimization on the initial models, followed by relaxation for 20 ps at 25 ^\circC. Using a combination of MC atom swaps and MD hybrid method, we constructed atomic models for alloy containing CSRO based on the initial models. After MC simulation, we annealed the model from 1227 ^\circC to 25 ^\circC and 600 ^\circC at a 1 ^\circC/ps rate. For a second lattice relaxation under canonical ensemble (NVT), we switched the model to non-periodic boundary conditions on the x, y, and z axes. The y-direction deformation is performed at an engineering strain rate of  $ 2 \times 10^8 \, s^{-1} $. At the top and bottom regions of the simulation box, rigid blocks containing immobile atoms were positioned. A constant velocity was applied to these blocks in opposite directions to deform the model. Free boundary conditions were established on the planes parallel to the loading axis. During the tensile process, velocity rescaling was performed at every step. While this may influence the thermal conductivity analysis of HEAs, both the literature (Chen et al. 2021) and our research (Liu et al. 2024) indicate that this approach stabilizes the deformation temperature, with negligible impact on deformation twinning. We compared velocity rescaling every 1, 5, 10, and 100 steps, as well as a case with no rescaling. The lack of thermal energy in the system does not significantly affect the MD simulation results.

In the simulation process, the strain rate is actually  $ 10^{8}-10^{9}s^{-1} $. (Chen et al., 2021; Liu et al., 2024) This calculation speed is closer to the experimental results in macroscopic experiments, although there is a large gap between the calculation speed and the actual speed. However, due to the effects of size effects, etc., it is possible to qualitatively analyze the deformation mechanism.

## 3. Results and discussion

## 3.1. Mechanical properties

Figs. 2a and 2b show the uniaxial tensile stress–strain curves of the as-built L-PBF-processed samples with varying Mo contents (Mo_{0}, Mo_{1}, Mo_{3}, and Mo_{5}) at temperatures of 25 and 600 ^\circC. At room temperature, Mo enhances both the strength and ductility (Table 1). Compared with Mo_{0}, the yield strength (YS) of Mo_{1} increases from 566 to 609 MPa and the ductility increases from 19% to 27%. Mo_{3} and Mo_{5} exhibit even higher room-temperature mechanical properties.

The mechanical performance of all samples decreases significantly at elevated temperatures, with their YS and ultimate tensile strength (UTS) varying considerably. The ductility of MoO is less than 10%, indicating its unsuitability for high-temperature applications. Mo_{1} displays dynamic strain strengthening during high-temperature tensile loading; however, its ductility is still less than 10%. A notable disparity is observed in the high-temperature tensile performance of Mo_{3} and Mo_{5}. For Mo_{3}, the YS, UTS, and uniform elongation at 600 ^\circC are 20%, 57%, and 1513% higher, respectively, than those of MoO. The strain hardening of Mo_{3} is essentially the same as that at room temperature (Fig. 2c). Consequently, it demonstrates a successful balance between strength and ductility at high temperatures. Bv contrasts the ductility of Mo_{5} approaches the lower limit of the acceptable range (10%).

At 600 ^\circC, Mo_{1} exhibited significant serrated flow behavior, whereas Mo_{0}, Mo_{3}, and Mo_{5} did not show this phenomenon at this temperature. It can be seen that at the same temperature, serrated flow behavior is closely related to the Mo content. The essence of serrated flow is the pinning effect of solute atom clusters on dislocations, which increases the flow stress. When the flow stress increases to a certain value, the dislocations break through the solute clusters, causing a sudden drop in flow stress. These two actions alternate, forming the serrated flow behavior. In Mo_{0}, no Mo element was added, and the structure contains only Fe, Co, Cr, and Ni elements, with atomic radii of 124.1, 125.3, 124.9, and 124.6 Å, respectively. Since the atomic diameters are relatively close, the lattice distortion effect is not significant, and the pinning effect of solute atoms on dislocation motion is low. Thus, no serrated flow behavior occurs. In Mo_{1}, Mo atoms (with a diameter of 136.3 Å) aggregate into solute clusters near dislocations, significantly increasing the

Summary of mechanical properties of the L-PBF additively manufactured FeCoCrNiMox (x = 0, 0.1, 0.3, and 0.5) HEAs at different temperature conditions.

<table border="1" style="margin: auto; word-wrap: break-word;"><tr><td style="text-align: center; word-wrap: break-word;">Sample</td><td style="text-align: center; word-wrap: break-word;">Temperature, ^\circC</td><td style="text-align: center; word-wrap: break-word;">YS, MPa</td><td style="text-align: center; word-wrap: break-word;">UTS, MPa</td><td style="text-align: center; word-wrap: break-word;">UFE, %</td><td style="text-align: center; word-wrap: break-word;">TE, %</td></tr><tr><td rowspan="2">Mo0</td><td style="text-align: center; word-wrap: break-word;">25</td><td style="text-align: center; word-wrap: break-word;">566</td><td style="text-align: center; word-wrap: break-word;">719</td><td style="text-align: center; word-wrap: break-word;">18.15</td><td style="text-align: center; word-wrap: break-word;">19.82</td></tr><tr><td style="text-align: center; word-wrap: break-word;">600</td><td style="text-align: center; word-wrap: break-word;">398</td><td style="text-align: center; word-wrap: break-word;">420</td><td style="text-align: center; word-wrap: break-word;">1.20</td><td style="text-align: center; word-wrap: break-word;">1.25</td></tr><tr><td rowspan="2">Mo1</td><td style="text-align: center; word-wrap: break-word;">25</td><td style="text-align: center; word-wrap: break-word;">609</td><td style="text-align: center; word-wrap: break-word;">776</td><td style="text-align: center; word-wrap: break-word;">27.46</td><td style="text-align: center; word-wrap: break-word;">36.51</td></tr><tr><td style="text-align: center; word-wrap: break-word;">600</td><td style="text-align: center; word-wrap: break-word;">407</td><td style="text-align: center; word-wrap: break-word;">473</td><td style="text-align: center; word-wrap: break-word;">6.71</td><td style="text-align: center; word-wrap: break-word;">8.23</td></tr><tr><td rowspan="2">Mo3</td><td style="text-align: center; word-wrap: break-word;">25</td><td style="text-align: center; word-wrap: break-word;">698</td><td style="text-align: center; word-wrap: break-word;">953</td><td style="text-align: center; word-wrap: break-word;">25.02</td><td style="text-align: center; word-wrap: break-word;">27.78</td></tr><tr><td style="text-align: center; word-wrap: break-word;">600</td><td style="text-align: center; word-wrap: break-word;">477</td><td style="text-align: center; word-wrap: break-word;">661</td><td style="text-align: center; word-wrap: break-word;">19.35</td><td style="text-align: center; word-wrap: break-word;">22.98</td></tr><tr><td rowspan="2">Mo5</td><td style="text-align: center; word-wrap: break-word;">25</td><td style="text-align: center; word-wrap: break-word;">830</td><td style="text-align: center; word-wrap: break-word;">1091</td><td style="text-align: center; word-wrap: break-word;">19.38</td><td style="text-align: center; word-wrap: break-word;">19.93</td></tr><tr><td style="text-align: center; word-wrap: break-word;">600</td><td style="text-align: center; word-wrap: break-word;">578</td><td style="text-align: center; word-wrap: break-word;">799</td><td style="text-align: center; word-wrap: break-word;">11.16</td><td style="text-align: center; word-wrap: break-word;">11.33</td></tr></table>

resistance to dislocation motion, leading to the formation of serrated flow behavior. As the Mo content further increases, the sluggish diffusion effect of HEAs gradually suppresses the diffusion behavior of solute atoms, reducing the tendency to form solute atom clusters around dislocations, thereby eliminating serrated flow behavior.

From the perspective of material plasticity, the plasticity of Mo_{1} at 600 ^\circC is much higher than that of Mo_{0}. Our previous research (Lin et al., 2022) has revealed that the high-temperature brittleness of Mo_{0} is caused by the nanocluster formation of elements at the grain boundaries. Therefore, the addition of Mo in Mo_{1} and Mo_{3} improves the bonding strength at the grain boundaries, enhancing high-temperature plasticity. The slight decrease in plasticity of Mo_{5} compared to Mo_{3} is due to the embrittlement caused by the growth of the \sigma phase.

Fig. 2d compares the high-temperature ( $ >600\ ^{\circ}C $) mechanical properties of various FeCoCrNi-based HEAs, Ti-based alloys, and Ni-based superalloys. Mo_{3} and Mo_{5} exhibit comparatively remarkable mechanical performance, particularly regarding the strength–ductility trade-off. This advancement demonstrates the potential of these alloys for use in high-temperature environments.

## 3.2. Initial microstructures of L-PBF-processed FeCoCrNiMo $ _{x} $ HEAs

For a more comprehensive understanding of the reasons behind the changes in performance, we conducted a detailed microstructural analysis. Fig. 3 presents SEM images of the additively manufactured FeCoCrNiMo $ _{x} $ HEAs. The samples are nearly defect-free, although a few small round pores (<1  $ \mu $m) are visible near the fusion lines. Moreover, a distinct dendritic structure is concentrated at the overlaps of the melt pools, with clear dendrite and interdendrite regions (Figs. 3a, 3b, and 3c, insets). In comparison with MoO (Fig. 3a), the Mo-containing samples exhibit sharper dendrites (Figs. 3b and 3c). Because of the significant temperature gradient and thermal cycling during L-PBF, the initial solidification occurs faster at the top of the molten pool than at the bottom (Hu et al., 2022; Munusamy and Jerald, 2023; Wang et al., 2023b). This results in dendritic growth at the top of the pool, whereas the bottom maintains planar crystal growth. Small grains form in the intersecting areas of the melt pools (Fig. 3d, inset). Therefore, the additively manufactured FeCoCrNiMo $ _{x} $ HEAs exhibit microstructural heterogeneity, with a grain size distribution of a few microns to tens of microns.

Fig. 4 presents the EBSD results of the as-built FeCoCrNiMo $ _{x} $ HEAs. From the inverse pole figure maps, the MoO grains show a clear tendency to grow along the direction of construction (z direction). This is attributed to the thermal gradient and optimal solidification orientation (Körner et al., 2020). Thus, the grains have a unidirectional epitaxial columnar shape. In addition, the matrix exhibits a relatively obvious 100<111> texture, as illustrated in the pole figure in Fig. 4a3. However, the introduction of Mo induces notable changes (Figs. 4b1, 4c1, and 4d1), with a more random grain orientation. Furthermore, the average grain size increases from 35.1  $ \mu $m for MoO to 57.5  $ \mu $m for Mo_{3}. Given that Mo is a refractory element, a higher energy density is required for preparation. Therefore, the
Fig. 3. Typical microstructure of L-PBF additively manufactured FeCoCrNiMox samples: (a) Mo_{0}, (b) Mo_{1}, (c) Mo_{3}, and (d) Mo_{5}. Distinct dendritic structure is concentrated at the overlap of the molten pool. Small grains generate in the intersection area of the molten pool.
Fig. 4. Typical microstructure of L-PBFed samples: (a1-a3) Mo_{0}, (b1-b3) Mo_{1}, (c1-c3) Mo_{3}, and (d1-d3) Mo_{5}. (a1, b1, c1, d1) EBSD inverse pole figure (IPF) maps showing the grain size and morphology. (a2, b2, c2, d2) KAM images superimposed with high angle grain boundaries (HAGBs, black lines). (a3) Texture orientation of Mo showing 100<111>; (b3, c3) Statistics for the grain size; (d3) Distribution of grain state in recrystallized, substructured, and deformed.

Summary of microstructural characteristics of the as-built FeCoCrNiMox HEAs (x = 0, 0.1, 0.3, and 0.5).

| Sample | Mo at% | Avg. grain size,  $ \mu $m | GND density,  $ \times 10^{14} /m^{2} $ | Fraction of RX, % | Texture orientation |
| --- | --- | --- | --- | --- | --- |
| Mo0 | 0 | 35.1 | 8.45 | 2.9 | 100<111> |
| Mo1 | 2.44 | 47.4 | 9.84 | 13.3 | 100<111> |
| Mo3 | 6.98 | 57.5 | 8.25 | 10.7 | 100<111> |
| Mo5 | 11.11 | 51.9 | 8.99 | 6.4 | 100<111> |

average geometrically necessary dislocation density of Mo3, as calculated from the kernel average misorientation, is similar to that of Mo0. The microstructural characteristics are summarized in Table 2.

The variations in the grains (orientation, recrystallization, and size) of the FeCoCrNiMo $ _{x} $ HEAs highlight the complex interplay between the composition and processing parameters, resulting in differences in the mechanical properties. Overall, the multiscale heterogeneity is derived from microscale lattice defects (Zhang et al., 2018), requiring more geometrically necessary dislocations to achieve microstructural deformation during L-PBF. As shown in Fig. 4d3, Mo_{5} contains a few recrystallized grains, whereas most grains are substructured and deformed, indicating a high dislocation density. In addition to the high density of dislocation cells caused by thermal residual stress, slow elemental diffusion within HEAs is also considered to hinder recrystallization (Miracle and Senkov, 2017). The fraction of partially recrystallized grains is affected by the Mo concentration (Ming et al., 2019), as well as laser-induced structural deformation (Peng et al., 2024) and precipitation (He et al., 2021a). The recrystallized fraction of the FeCoCrNiMo $ _{x} $ samples varies from 2.9% to 13.3%, which will affect the dislocation hardening behavior during tensile deformation.

Fig. 5 shows the dislocation morphology and elemental segregation of the FeCoCrNiMo $ _{x} $ HEAs, as characterized by TEM and EDS. Laser-printed samples typically exhibit hexagonal dislocation cell patterns because of residual stresses during solidification (He et al., 2022). However, the dislocation cell patterns are not obvious in MoO. As the Mo content increases, the dislocation cell features become more obvious and the cell walls become sharper. The cell wall thickness decreases from approximately 200 nm for Mo_{1} to 50 nm for Mo_{5}, and the cell size increases slightly. Some stacking faults can also be observed in Mo_{5}.

Mo_{3} and Mo_{5} contain rod-shaped nanoscale  $ \sigma $-phase precipitates at the grain boundaries (Figs. 5c and 5d). This is because Mo, a refractory metal with a large atomic radius, is likely to be enriched at locations with large lattice distortions, such as grain boundaries,

L-PBF additive manufacturing as-built state
Fig. 5. TEM image reveals the microstructure of the dislocation networks of the as-built FeCoCrNiMox HEAs: (a) Mo_{0}, (b) Mo_{1}, (c) Mo_{3}, and (d) Mo_{5}; EDS mapping results of the Cr-rich nano precipitates in rod shape (\sigma phase) and blocky shape (\mu phase) in Mo_{3} and Mo_{5} samples. Nano-twins generate in Mo_{5} samples inside of the DCP. The white arrows highlight the emission of stacking faults (SFs) with the DCP.

which act as nucleation sites. Segregated Cr/Mo solutes can also redistribute or diffuse into mobile grain boundaries during matrix growth (He et al., 2021a), thereby promoting \sigma-phase nucleation along the grain boundaries. The diffusion rate of Mo is much slower than that of Cr. In addition, it is present in relatively lower concentrations than the other elements in the HEA. Therefore, it is primarily Cr (He et al., 2021a) that partitions into the \sigma phase. In addition to the nanoscale \sigma-phase precipitates, blocky \mu-phase precipitates can also be observed (Cr-rich Mo). The \mu-phase precipitates appear at the edges of the \sigma-phase precipitates, indicating that they may be generated by transformation of the \sigma phase during solidification. Sui et al. (Sui et al., 2022) credited \mu-phase formation to the lattice strain produced by excessive Mo, which makes the \sigma phase unable to maintain its tetragonal structure. The release of lattice strain

Post-necking state after tensile deformation @25^\circC
Fig. 6. Deformation microstructures evolution of L-PBFed FeCoCrNiMox sample at the post-necking deformation stage under tensile tests at room temperature is presented. Bright-field and dark-field TEM images reveal the different twinning effects of the FeCoCrNiMox HEAs: (a) Mo_{0}, (b) Mo_{1}, (c) Mo_{3}, and (d) Mo_{5}.

causes the  $ \sigma $ phase to transform into the rhombohedral  $ \mu $ phase. Furthermore, supersaturated Mo induces  $ \sigma $-phase formation along the grain boundaries, which effectively inhibits the formation of Mo-containing alloy through the pinning effect and can effectively delay recrystallization and grain growth (Linder et al., 2024; Miracle and Senkov, 2017).

3.3. Microstructural evolution of FeCoCrNiMo $ _{x} $ HEAs during deformation at 25 and 600 ^\circC

Fig. 6 shows TEM images of near-neck regions of the samples deformed at room temperature. These images demonstrate the distinctive role of twinning in the room-temperature plastic deformation of FeCoCrNiMo $ _{x} $ HEAs. However, there is a notable variation in the density and width of twins across different samples. Specifically, the presence of twins in the Mo_{0}, Mo_{1}, and Mo_{3} samples is more pronounced compared to the Mo_{5} sample, where the number is relatively small, as shown in Fig. 6d2. This suggests that the critical stress required for twin activation in the as-built Mo_{5} sample is significantly higher than the other samples, even though it exhibits greater strength and ductility than the Mo_{0} and Mo_{1} HEAs. This is primarily due to the presence of a significant amount of  $ \sigma $ precipitates (Fig. 5) in Mo_{5}. These precipitates can partially hinder the movement of dislocations, thereby preventing the formation of stacking faults in the matrix (Cai et al., 2017). Consequently, this reduces the likelihood of stacking faults, and further decreases the probability of twin formation. Additionally, the significant plastic deformation during the stretching process in Mo_{3}, combined with the lower quantity of  $ \sigma $ precipitates, leads to a much higher number of twins in Mo_{3} compared to Mo_{5}.

According to Table 1, the strength of Mo_{0} and Mo_{1} decreased by 40% at high temperatures, while the ductility of Mo_{3} and Mo_{5} only decreased by 30%. Moreover, Mo_{3} and Mo_{5} retained a higher percentage of elongation. To understand this difference, we conducted high-temperature fracture surface TEM analysis. Fig. 7 displays the TEM characterization results of the near-necking position of samples with different Mo contents after deformation at high temperatures. We observed that due to the lack of precipitates hindering their movement, the grains in the Mo_{0} and Mo_{1} samples were significantly elongated post-deformation. These lamellar grain boundaries act as strengthening barriers, accumulating intragranular dislocations and consequently reducing the ductility of the samples. In the Mo_{3} and Mo_{5} sample, some cellular dislocations remained visible, and short rod-shaped precipitates of the \sigma phase were located on the dislocation cell wall. These precipitates played a pinning role in the movement of the dislocation cell, contributing to its high-temperature stability. It is worth noting that in the Mo_{3} and Mo_{5} samples, the hindrance of dislocation motion by precipitates results in the accumulation of a large number of dislocations at grain boundaries. This leads to stress concentrations exceeding the critical twinning stress level, causing the formation of deformation twins. This indicates that in addition to the dislocation coordination deformation observed in Mo_{0} and Mo_{1}, twinning induced plasticity (TWIP) effects also came into play. Since the deformation temperature does not reach the secondary precipitation temperature of the \sigma phase, the ratio of precipitates will not increase further during the high-temperature deformation process (Elmer et al., 2007). High-density dislocations pile up along the hard \sigma-phase precipitates, hindering further dislocation slip. The excessive \sigma-phase cannot deform coherently with the matrix, leading to cracking under low plastic deformation conditions. As a result, stress concentration-induced cracking occurs earlier in Mo_{5} than in Mo_{3} sample during tensile deformation.

Post-necking state after tensile deformation @600^\circC
Fig. 7. Deformation microstructures evolution of L-PBFed FeCoCrNiMox sample at necking-fracture state after tensile deformed at 600 ^\circC: (a) Mo_{0}, (b) Mo_{1}, (c) Mo_{3}, and (d) Mo_{5}. GB: grain boundary.
Fig. 8. Necking-fracture morphology of (a) Mo3 and (b) Mo5 samples after tensile deformation at 25 ^\circC.

3.4. Fracture morphology of Mo3 and Mo5 at 25 and 600 ^\circC

To elucidate the fracture mechanisms of the Mo3 and Mo5 samples, we conducted an analysis of the fracture surfaces of the tensile specimens at 25 ^\circC and 600 ^\circC. Fig. 8 illustrates the room-temperature fracture morphologies of Mo3 and Mo5. The fracture surfaces are characteristic of FCC materials, with high densities of tears and dimples. Under uniaxial loading, the initial crack extends in the tensile direction, forming voids during the crack extension stage. The connections between these voids result in fractures. Some tongue-shaped pits or protrusions formed by extension of the cleavage cracks along the twin boundaries are visible (Fig. 8b2). This phenomenon is consistent with the findings of Sui et al. (Sui et al., 2022). Fig. 8a3 indicates that the molten pool boundary is susceptible to fracture.

Fig. 9 illustrates the high-temperature fracture morphologies of Mo_{3} and Mo_{5}. The fracture surface of Mo_{3} still exhibits ductile fracture characteristics, albeit with a diminished presence of dimples as compared to that at room temperature. The emergence of twins during the latter stages of deformation renders the fracture surface akin to the room-temperature fracture surface of Mo_{5}, with tongue-shaped cleavage crack patterns. By contrast, the high-temperature fracture surface of Mo_{5} exhibits quasi-cleavage traits. Cleavage steps are formed by fracture along the crystal planes at varying heights. The fracture surface of Mo_{5} (Fig. 9b2) is considerably flatter than that of Mo_{3} (Fig. 9a2), suggesting that the fracture strain was relatively constrained during the tensile process. This observation aligns with the high-temperature tensile stress–strain curves. The presence of \sigma-phase precipitates, which are hard and brittle intermetallic compounds, enhances the compressive strength but concurrently reduces the fracture strain.

a1
Fig. 9. Necking-fracture morphology of additively manufactured CoCrFeNiMox HEA samples after tensile deformation at 600 ^\circC: (a) Mo3 and (b) Mo5.

Comparing the room- and high-temperature tensile fracture morphologies of Mo_{3} and Mo_{5} reveals a trend of transition and transformation in the fracture characteristics, suggesting that the strength of additively manufactured FeCoCrNiMoₓ HEAs can be significantly enhanced by adding an appropriate amount of Mo. Moreover, it potentially reveals the Mo content window for tuning the mechanical properties of FeCoCrNiMoₓ HEAs.
Fig. 10. (a) The diagram of the nonequilibrium solidification thermodynamic process and phase evolution of Mo_{0}, Mo_{1}, Mo_{3} and Mo_{5} HEAs calculated using Thermo-calc software, specific elemental content in solid phase during solidification process of (b) Mo_{1} and (c) Mo_{5}, (d) Comparison of printed microstructure characteristics with varying Mo additions.

a Closed-packed planes

b Perfect stacking Intrinsic stacking fault
Fig. 11. (a) Schematics of close-packed planes in the FCC structure with three possible atomic positions A, B, or C, selected crystallographic directions, partial Burgers vectors. (b) Schematic view of fault-free FCC lattice and FCC lattice with intrinsic stacking fault. A, B, and C, and associated color-coded spheres indicate the stacking sequence of atoms and the thin lines describe the undistorted and tilted nine-layers unit cells used for calculating the  $ \gamma_{isf} $. (c) Ab initio calculation for  $ \gamma_{isf} $ of the FeCoCrNiMox HEAs as a function of the Mo content and temperature. The solid lines indicate the results from 200 K to 1000 K for 0 at%, 6 at%, and 11 at% Mo-doped into FeCoCrNi matrix, respectively.

## 3.5. Solidified phase equilibrium state of FeCoCrNiMo $ _{x} $ HEAs

The \sigma-phase is brittle, and therefore, its presence is generally detrimental for long-term applications. However, in this study, the addition of Mo promoted the precipitation of the \sigma-phase at grain boundaries, which further hindered cell deformation at high temperatures. Additionally, the pinning effect suppressed grain boundary migration, enhancing the high-temperature strength and plasticity of the HEA. Therefore, it is necessary to study the precipitation behavior of the \sigma-phase. Fig. 10 presents the change in the phase and element ratios during the solidification of the melt pools for different samples. The melting point ( $ T_{m} $) of the HEAs decreases from 1446 ^\circC for Mo_{0} to 1381 ^\circC for Mo_{5} (Fig. 10a). The FCC matrix forms from the liquid phase during solidification, accompanied by \sigma-phase precipitation for the Mo-doped HEAs. The onset of FCC solidification and \sigma-phase precipitation occur at different solid-phase molar fractions, although the step distance (molar amount) is much shorter for Mo_{3} than for Mo_{1} and Mo_{5}. In fact, \sigma-phase precipitation in Mo_{3} begins almost simultaneously with the solidification of the FCC matrix.

Mo_{1} and Mo_{5} exhibit a similar trend in terms of the solid-phase content (Figs. 10b and 10c), which is quite different from that of Mo_{3} (Lin et al., 2023). In Mo_{3}, the Mo-rich \sigma phase precipitates first, followed by simultaneous precipitation of the FCC and \sigma phases. By contrast, in Mo_{1} and Mo_{5}, the Mo-rich \sigma phase precipitates later in the solidification process. As summarized in Fig. 10d, nanosized \sigma and \mu phases precipitate in the subgrains and at the subgrain boundaries owing to the two-stage solidification (Lin et al., 2023). The differences in the fractions and distributions of precipitate phases caused by the different Mo contents and the coupling effect with dislocations lead to different degrees of sharpening of the dislocation cell walls (Fig. 5). It is worth noting that dynamic recrystallization may occur at the high-temperature tensile conditions of 600 ^\circC (>0.35T_m). However, the Mo-rich precipitates that form during L-PBF could suppress grain boundary migration via pinning, thereby increasing the size of the recrystallized grains (Wang et al., 2017).

## 3.6. Ab initio calculations and molecular dynamics (MD) simulations for revealing the effects of Mo content and temperature

According to Figs. 2, 6, and 7, there are significant differences in the plasticity of HEAs with varying Mo content. To thoroughly investigate the reasons behind these differences, we conducted ab initio calculations for auxiliary analysis. As an important strengthening and hardening mechanism, the morphology and distribution of the deformation twins are closely related to the Mo content and temperature, which directly affect the SFE (Chang et al., 2021; Wang et al., 2017). The intrinsic SFE  $ \gamma_{isf} $, representing the energy barrier of generating intrinsic SFs, determines twin formation. In FCC crystals, we consider the usual  $ a_{FCC}/2 $  $ [10\overline{1}](111)_{FCC} $ slip system where a perfect lattice dislocation can dissociate into two Shockley partials with Burgers vectors  $ b_{p1}^{FCC}=a_{FCC}/6[11\overline{2}]_{FCC} $ and  $ b_{p2}^{FCC}=a_{FCC}/6[21\overline{1}]_{FCC} $.  $ a_{FCC} $ is the FCC lattice parameter. The stacking sequence of  $ (111)_{FCC} $ close-packed planes is ABC|ABC| ABC..., where the labels A through C correspond to the three possible atomic positions in a  $ (111)_{FCC} $ plane. The schematic diagram is shown in Fig. 11a. Next, and intrinsic stacking fault, of energy  $ \gamma_{ISFE} $ was created by shifting the top ten layers along the  $ [1\ 1\ 2] $ direction by the Burgers vector of the Shockley partial  $ b_{p1}^{FCC} $, this resulted in a stacking sequence: ABC|BC|ABC, shown in Fig. 11b. Our ab initio calculation results, depicted in Fig. 11, reveal that  $ \gamma_{isf} $ is approximately -21, -33, and -48 mJ/m $ ^2 $ for HEAs with 0, 6, and 11 at% Mo, respectively, at room temperature. However, at 600 ^\circC,  $ \gamma_{isf} $ is estimated to be approximately -9, -15, and -26 mJ/m $ ^2 $, respectively. Thus, the addition of Mo reduces  $ \gamma_{isf} $ for the as-built FeCoCrNiMo $ _{x} $ HEAs, especially at elevated temperatures. As the SFE increases, the dynamic recovery becomes more active at high temperatures, facilitating dislocation movement such as cross-slip. However, dynamic recovery occurs earlier during deformation at 600 ^\circC than at 25 ^\circC, leading to a rapid decrease in the work-hardening rate at high strain stages. For Mo_{5} (11 at%), although it has a lower stacking fault energy, we did not observe a significant amount of twinning in the matrix. This is because dislocation slip and diffusion mechanisms are more active at high temperatures, which increases the activation stress for twinning deformation. Additionally, the presence of a large amount of  $ \sigma $-phase attached to the grain boundaries leads to fracture at lower strain values. This reduction in plastic deformation also decreases the occurrence of twinning to some extent. The dynamic Hall-Petch effect, induced by the twin boundary in Mo_{3}, introduces new interfaces and reduces the dislocation mean free path, providing further contribution. Consequently, the dislocation cell patterns of the FeCoCrNiMo $ _{x} $ HEAs are altered by the
Fig. 12. (a) Schematic illustration of the uniaxial tensile MD simulation conducted on a single crystal Mo3 nanowire. (b) Simulated stress-strain curves at 25 ^\circC and 600 ^\circC show difference in elastic modulus and stress softening due to elevated temperature.

temperature and Mo content, which is consistent with the experimental observations and TEM characterizations. Because the SFE evolution is critical for revealing the potential deformation mechanism in the activation of twinning, ab initio calculations provide valuable insight into the design of FeCoCrNiMo $ _{x} $ HEAs.

In order to further explore the plastic deformation essence of Mo_{3} alloy, we conducted molecular dynamics simulations. In the MD simulations, the Mo_{3} tensile specimen was simulated using a single-crystal nanowire, as displayed in Fig. 12a. The model had an FCC crystal structure with a lattice constant of 3.60 Å. The crystallographic directions along the x, y, and z axes were [001], [110], and [110], respectively. The nanowire comprised 100,000 atoms, including 23,254, 23,259, 23,255, 23,256, and 6976 Fe, Co, Cr, Ni, and Mo atoms, respectively, thereby satisfying the atomic ratio of FeCoCrNiMo0.3 (Mo_{3}). Periodic boundary conditions were applied in all three directions. The top and bottom layers, each measuring 27 Å along the y axis, were fixed. To simulate uniaxial tensile deformation, these fixed layers were extended in opposite directions along the y axis, with a stretching speed of 0.02 Å/ps. The deformation zone, subjected to stretching, measured 200 \times 72 \times 64 Å.

As illustrated in Fig. 12b, Mo3 shows significant stress softening at 600 ^\circC compared to that at 25 ^\circC. Moreover, the elastic modulus at 600 ^\circC is significantly lower than that at 25 ^\circC. As deformation proceeds, twinning occurs, which causes stress drops.

Figs. 13a and 13b illustrate the MD simulations of twin evolution in Mo3 during tensile deformation at room and high temperatures, respectively. The presence of Mo enhances the lattice distortion. During tensile deformation, stacking faults are generated. As the strain increases, these stacking faults accumulate, leading to the formation of micro twins (Tian et al., 2024). Despite the generation of micro twins at 25 ^\circC, the growth of these micro twins is suppressed as the strain continues to increase, because a significant number of stacking faults accumulate. This results in an alternating structure of micro twins and stacking faults, thereby enhancing the ductility (Guo et al., 2024; He et al., 2021b; Jo et al., 2014).

As the temperature rises to 600 ^\circC, the SFE gradually increases, as demonstrated by the ab initio calculation results in Fig. 11b. The local stress of twinning tends to increase with increasing temperature. Thus, the twin lamellae are larger than those at 25 ^\circC, as displayed in Fig. 13b. The stacking faults expand during tensile straining, thereby consuming the twins. Consequently, the strength is reduced owing to the interaction between stacking faults and twins. Owing to the mutual interaction between the twins and stacking faults during tensile deformation, Mo_{3} still has good ductility at 600 ^\circC.

Our calculations at the atomic scale indicate that when HEA yields, the ISF structure emerges within the crystal. Some researchers have characterized through TEM that stacking faults and slip are the initial structures observed during the yielding of FCC alloys. With increasing temperature,  $ \gamma_{isf} $ increases, but studies suggest that  $ \gamma_{ui} $ exhibits only slight variations. Temperature provides kinetic energy to atomic motion, leading to lower yield strength of materials at elevated temperatures. Tadmor and Bernstein introduced an alternative approach known as  $ \tau_{a} $ (Bernstein and Tadmor, 2004). The following expression can approximate this method (Wu et al., 2014).

 $$ \tau_{\mathrm{a}}=\left[1.136-0.151\frac{\gamma_{\mathrm{isf}}}{\gamma_{\mathrm{ui}}}\right]\sqrt{\frac{\gamma_{\mathrm{ui}}}{\gamma_{\mathrm{esf}}}} $$ 

Where the  $ \gamma_{ui} $ is the maximum value of intrinsic stacking faults, the  $ \gamma_{esf} $ is the minimum extrinsic stacking fault. The higher the value of  $ \tau_{a} $, the more likely it is to produce extrinsic stacking fault (ESF). As the temperature increases, the proportion of ISF transforming into ESF decreases gradually. ISF without transformation to ESF may generate two neighboring ISFs that can be understood as a twin (TW) structure. The transformation path of ISF into ESF and then into TW is the sole path of transformation for TW during the simulation. The transformation of ISF into TW requires a significant shear stress to take place, and the magnitude of the shear force,  $ \tau_{TW} $, can be determined using the following equation (Huang et al., 2006):

 $$ \tau_{\mathrm{T W}}=\frac{\gamma}{\mathbf{n b}_{1}}+\frac{\mathbf{G b}_{1}\sqrt{\rho}}{\mathbf{n}} $$ 

A stress concentration factor, represented by n, is required in the early stages of nucleation, typically ranging from 2 to 4. The parameter  $ \gamma $ denotes the surface energy of the meta material, whereas b1 refers to the modulus of the Burgers vector of the Shockley partial dislocation and G represents the shear modulus.

According to the Taylor dislocation hardening model, the local shear stress,  $ \tau_{TW} $, increases with an increase in dislocation density for FCC metals, which are known for their high-strain hardening ability(Huang et al., 2006).
Fig. 13. Uniaxial tensile MD simulation results of Mo_{3} HEA. (a) A large number of stacking faults accumulate to form an alternating structure of micro twins and stacking faults at 25 ^\circC. (b) The reduced stacking faults play interaction with micro twins, resulting in a decrease in strength at 600 ^\circC.

$$ \tau_{\mathrm{T W}}=\alpha_{1}\mathbf{G}\mathbf{b}\sqrt{\rho}=\frac{\Delta\sigma}{\mathbf{M}} $$ 

\Delta\sigma represents the increase in tensile stress, the Taylor factor is denoted as M, \alpha is a constant value, b represents the magnitude of the Burgers vector, and \rho is the dislocation density. The true tensile stress and resolved shear stress (Laplanche et al., 2016) at which twinning occurs are 550–600 MPa and 230–245 MPa, respectively. We illustrate the process of twin formation and the necessary range of true stress to induce twinning. At room temperature, all alloys exhibit high levels of yield stress, leading to twinning in each case. However, at 600 ^\circC, MoO and Mo_{1} alloys display lower yield stress levels, while Mo_{3} and Mo_{5} exhibit higher levels, consequently resulting in twinning in the Mo_{3} and Mo_{5} alloys.

## 3.7. Effect of hierarchical microstructure on mechanical properties

The multiscale strengthening mechanisms of the as-built FeCoCrNiMo $ _{x} $ HEAs are important for clarifying the deformation mechanism, particularly the complex mechanical response of the hierarchical microstructure. For metals, the flow stress ( $ \sigma_{flow} $) can be expressed as

 $$ \sigma_{flow}=\frac{\sigma_{0}+\sigma_{\rho}+\sigma_{TW}+\sigma_{Intra}}{\sigma_{th}}+\frac{\sigma_{ss}+\sigma_{GB}+\sigma_{ppt}}{\sigma_{ath}} $$ 

where  $ \sigma_{ath} $ and  $ \sigma_{th} $ are thermally independent and dependent stress items, respectively, and  $ \sigma_{0} $ is the friction stress from lattice resistance (i.e., the Peierls–Nabarro stress), which is 125 MPa for Mo0 (Otto et al., 2013) and 237.19 MPa for Mo1 (Dai et al., 2021) at 25 ^\circC.  $ \sigma_{0} $ can be calculated using the following formula (Ramakrishnan, 1996):

 $$ \sigma_{0}=\frac{2MG}{1-\nu}\exp\left(-\frac{2\pi c}{b(1-\nu)}\right) $$ 

where c is the distance between adjacent slip surfaces (0.206 nm;  $ a/\sqrt{3} $), M is the Taylor factor ( $ \sim $3.06 for the FCC matrix),  $ \alpha $ is a geometric factor (0.2 for FCC materials), b is the Burgers vector (0.146 nm for Shockley partial dislocations) (Dai et al., 2021),  $ \nu $ is Poisson’s ratio, and G is the shear modulus, which is affected by the Mo content (Liu et al., 2020) and temperature (Huang et al., 2015). Here, G was calculated and measured experimentally using Young’s modulus. Note that  $ \sigma_{0} $ is temperature-sensitive because it depends largely on the short-range atomic order and strength of the atomic bonds. As the temperature increases, the atomic vibrations increase, and the atomic bond strength decreases; therefore,  $ \sigma_{0} $ decreases (Wang et al., 2017).

From the ab initio calculations, the SFE of FeCoCrNiMo $ _{x} $ HEAs decreases with increasing Mo content. Moreover, the stress is below the twinning threshold at the initial stage of yielding. Therefore,  $ \sigma_{TW} $ can be temporarily ignored at the yield deformation stage.

The coarse- and fine-grained regions and dislocation cell patterns inside the L-PBF-processed grains regulate dislocation slip during deformation (Liu et al., 2024). Thus, dislocation strengthening and back-stress strengthening in the initial deformation stage are very important and collectively increase the hetero-deformation-induced strengthening effect (Chu et al., 2024; Gao et al., 2023; Karthik and Kim, 2021). For the back stress, which comprises inter- and intragranular stresses, the intergranular stress is nearly zero at the initial stage of deformation (An et al., 2023), whereas the intragranular stress, caused by the heterogeneously distributed dislocations piling up at the interface (Gao et al., 2022) (i.e., high-density dislocation walls within the cellular structure in MoO), can be roughly estimated by the dislocation hardening model. For Mo_{1}, Mo_{3}, and Mo_{5}, precipitation and solid-solution strengthening suppress intragranular stress generation. The empirical relationship for the dislocation hardening stress ( $ \sigma_{\rho} $) can be expressed as

 $$ \sigma_{\rho}=M\alpha Gb\sqrt{\rho_{GND}} $$ 

The geometrical factor  $ \alpha $ is also taken as a constant for FCC martial as 0.2 (Yim et al., 2019). The  $ \rho_{GND} $ can be obtained according to Table 2. Because dislocation and precipitation strengthening are both related to the cellular structure, the root mean square of the two effects, i.e.,  $ \sigma_{cc} = \sqrt{\sigma_{\rho}^{2} + \sigma_{ppt}^{2}} $, can be used to evaluate dislocation-cell strengthening in Mo-containing samples (Liu et al., 2023).

For the samples with Mo, the precipitation strengthening stress ( $ \sigma_{npt} $) is expressed as

For the samples with Mo, the precipitation strengthening stress ( $ \sigma_{ppt} $) is expressed as

 $$ \sigma_{p p t}=\frac{G b}{2\pi}\frac{1}{D_{e}^{p p t}}\mathrm{I n}\left(\frac{D_{e}^{p p t}}{b}\right) $$ 

where $D_e^{ppt}$ denotes the average particle spacing, calculated using $d_p\left(\sqrt{\frac{\pi}{6f}} - \sqrt{\frac{2}{3}}\right)$. Here, $d_p$ $d_p$ is the average radius of the precipitated particles and $f$ is the fraction of particles. The characteristics of the precipitates in Mo_{1}, Mo_{3}, and Mo_{5} were obtained by TEM and in our previous work (Lin et al., 2024, 2023). Note that $\sigma_{ppt}\sigma_{ppt}$ is also affected by temperature, similarly to the variation in shear modulus $G$.

The atomic numbers of Co, Cr, Fe, and Ni are sequentially adjacent; therefore, there is little difference in their atomic radii. Consequently, the atomic size mismatch within FCC FeCoCrNi HEAs is negligible. Hence, only Mo is recognized as a strengthening element. The solid-solution strengthening stress ( $ \sigma_{ss} $) caused by Mo is expressed as

 $$ \sigma_{\mathrm{s s}}=k_{\mathrm{M o}}c_{\mathrm{M o}}\sigma_{\mathrm{s s}}=k_{\mathrm{M o}}c_{\mathrm{M o}} $$

where  $ c_{Mo} $ is the concentration of solute Mo atoms and  $ k_{Mo} $ is the strengthening coefficient of the matrix (19.4 MPa/at%) (Kenji et al., 2002).

From the Hall–Petch relation, the grain boundary strengthening stress ( $ \sigma_{GB} $) is given as

 $$ \sigma_{GB}=\frac{k_{HP}}{\sqrt{d}\sigma_{GB}}=\frac{k_{HP}}{\sqrt{d}} $$ 

where  $ k_{HP} $ is the Hall–Petch coefficient (taken as 226 MPa/ $ \mu $m $ ^{1/2} $ from the FeCoCrNiMn system) (Peng et al., 2022). Although there is no obvious difference in grain size between the samples with different Mo contents,  $ k_{HP} $ is influenced by both interstitial and substitutional elements. This leads to a correction term of 48[Mo] (where [Mo] is the Mo concentration in at%) (Kenji et al., 2002) for  $ k_{HP} $ in the Fe–Cr–Ni system, which is quite near the measured  $ k_{HP} $ value of 297 MPa/ $ \mu $m $ ^{1/2} $ for Mo_{1} (Dai et al., 2021). Therefore,  $ \sigma_{GB} $ is modified as follows:

 $$ \sigma_{GB}=\frac{(k_{HP}+48Mo)}{\sqrt{d}\sigma_{GB}}=\frac{(k_{HP}+48Mo)}{\sqrt{d}} $$ 

Figs. 14a and 14b compare the sum and contribution of each stress strengthening term to the yield strength during tensile deformation at room and high temperatures, respectively, which show good agreement with the experimental results. The most significant contribution is dislocation cell-coupled strengthening, which is characteristic of L-PBF-processed metals. Compared with MoO, an appropriate Mo addition ( $ \geq $7 at%) can markedly enhance the yield strength of FeCoCrNi-based HEAs, especially at high temperatures. This is because, although high temperatures can induce grain recovery, the solid-solution and precipitation strengthening induced by Mo can impede dislocation slip and exert a grain-boundary pinning effect.

However, the TEM characterization, ab initio calculations, and MD simulations reveal that excess Mo (e.g., 11.11 at%, Mo_{5}) leads to excessive precipitation at grain boundaries. This significantly increases the SFE at high temperatures and hinders continuous dislocation slip after the initiation of yielding, culminating in a substantial decrease in the uniform elongation of samples with high Mo contents. Although the SFE of samples with low or no Mo (~2.4 at%, Mo_{1}; 0 at%, Mo_{0}) increases less than that of Mo_{5} at high temperatures, the fracture of these samples occurs before the tensile stress reaches the critical value for twinning, resulting in a significant loss of strength and toughness and compromising their high-temperature performance. Moreover, the critical twinning stress decreases within coarse grains (Cai et al., 2017; Wagner and Laplanche, 2023); therefore, the larger grain size of Mo_{3} is conducive to twinning. The dynamic Hall–Petch effect further enhances the strain-hardening ability (Liu et al., 2022). Consequently, an optimal Mo content (~7 at%, Mo_{3}) can maintain the effects of solid-solution and precipitation strengthening while also inducing twinning in the later stages of deformation, which further enhances the dislocation hardening ability.

Fig. 14c depicts the distinctive mechanical performance of the L-PBF-processed FeCoCrNiMo $ _{x} $ HEAs versus other alloys at 600 ^\circC (see Fig. 2d and the Supplementary Material for further detail). By incorporating an optimal amount of Mo (7–11 at%), it is possible to regulate multiple strengthening and hardening mechanisms. These mechanisms include solid-solution strengthening, grain-boundary strengthening, precipitation strengthening, and twinning. This regulation facilitates enhanced strength–ductility synergy in Mo_{3} at elevated temperatures.

## 4. Conclusions

In this study, we systematically studied the mechanical properties of L-PBF additively manufactured FeCoCrNiMo $ _{x} $ HEAs with varying Mo contents at both room and elevated temperatures (25 and 600 ^\circC, respectively). A multiscale analysis, incorporating SEM, EBSD, TEM, and quantitative simulations, was conducted to assess the microstructural evolution and tensile deformation and elucidate the underlying mechanisms. The conclusions drawn from this study are as follows:

 $$ \mathrm{FeCoCrNiMo_{x}} $$ 

2. In conjunction with ab initio calculations, MD simulations, and TEM observations, the SFE of the FeCoCrNiMo $ _{x} $ HEAs decreases with increasing Mo content and increases at elevated temperatures. As a result, twinning is more likely to occur at room temperature for all samples. However, at 600 ^\circC, twinning is only observed for Mo3 owing to the increased SFE.

## 3. The addition of Mo to the FeCoCrNi matrix promotes both solid-solution and precipitation strengthening. By leveraging the versatility and rapid cooling of L-PBF, the introduction of an appropriate amount of Mo (7–11 at%) allows for precise microstructural control. This results in the simultaneous or sequential regulation of multiple strengthening mechanisms, including dislocation hardening, solid-solution strengthening, precipitation strengthening, hetero-deformation-induced strengthening, and twinning. Consequently, FeCoCrNiMo $ _{x} $ HEAs (x = 0.3–0.5) exhibit improved formability at room temperature and enhanced strength–ductility synergy at high temperatures. Specifically, the YS, UTS, and uniform elongation reach 580 MPa, 800 MPa, and 20%, respectively.

This study successfully demonstrates the relationship between the processing, microstructure, and mechanical properties of FCC FeCoCrNiMo $ _{x} $ HEAs at both room and elevated temperatures. Multiscale investigations, encompassing both experimental observations and modeling simulations, promote the understanding of the deformation mechanisms in Mo-doped HEAs. This understanding is based
Fig. 14. Comparison of yield strength as a cumulative structural calculation of various stress hardening terms with experimental results: (a) 25 ^\circC, (b) 600 ^\circC. (c) Schematic of the deformation mechanisms of L-PBFed Mo_{3} HEAs achieving enhanced strength-ductility synergy at elevated temperature.

on key microstructural characteristics such as stacking faults, twins, precipitates, and dislocation cell patterns, verifying the feasibility of using L-PBF to regulate the sequential activation of different strengthening mechanisms. Conventional methods such as SEM, TEM, and EBSD cannot capture the microstructure and twinning process at high temperatures. However, we have revealed this process through first-principles calculations and molecular dynamics simulations. By combining experimental observations with simulations, we have thoroughly analyzed the plastic deformation mechanisms of HEA alloys. This approach provides valuable insights for the development of new materials. This study provides valuable insights for structural HEAs to achieve synergistic high-temperature mechanical properties, thereby proving their significance and practicality in both scientific and engineering contexts.

## CRediT Authorship

Danyang Lin: Writing – original draft, Investigation, Funding acquisition, Conceptualization. Jixu Hu: Project administration, Methodology, Investigation, Conceptualization. Renhao Wu: Writing – review & editing, Visualization, Investigation, Funding acquisition. Yazhou Liu: Visualization, Investigation. Xiaoqing Li: Visualization, Investigation. Man Jae SaGong: Validation, Methodology, Investigation. Caiwang Tan: Project administration, Investigation. Xiaoguo Song: Supervision, Investigation, Funding acquisition. Hyoung Seop Kim: Writing – review & editing, Supervision, Methodology, Investigation, Funding acquisition.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data Availability

Data will be made available on request.

## Acknowledgments

The authors are greatly appreciated for the financial support by the National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIP) (Nos. NRF-2021R1A2C3006662 and NRF-2022R1A5A1030054). Dr. Renhao Wu is supported by Brain Pool Program through the NRF of Korea, funded by the Ministry of Science and ICT (NRF-RS202300263999). Dr. X. Li gratefully acknowledges financial support from the Swedish Research Council, the Göran Gustafsson Foundation, and the Carl Tryggers Foundation. The computations were enabled by resources provided by the National Academic Infrastructure for Supercomputing in Sweden (NAISS) at Linköping partially funded by the Swedish Research Council through grant agreement no.2022-06725. This work is also supported by the National Natural Science Foundation of China (Grant No. 52175307 by Dr. Song, and No. 52205348 by Dr. Lin), and the Natural Science Foundation of Shandong Province (Grant: ZR2023JQ021 by Dr. Song and ZR2022QE087 by Dr. Lin).

## Supplementary Materials

## Supplementary Material

## References

An, D., Zhou, Y., Liu, X., Wang, H., Li, S., Xiao, Y., Li, R., Li, X., Han, X., Chen, J., 2023. Exploring structural origins responsible for the exceptional mechanical property of additively manufactured 316L stainless steel via in-situ and comparative investigations. Int. J. Plast. 170, 103769.

Andersen, O.K., Kumar, V., Mookerjee, A., 1995. In: Lectures On Methods Of Electronic Structure Calculations-Proceedings Of The Miniworkshop On" Methods Of Electronic Structure Calculations" And Working Group On" Disordered Alloys. World Scientific.

Bernstein, N., Tadmor, E., 2004. Tight-binding calculations of stacking energies and twinnability in fcc metals. Physical review. B, Condensed matter and materials physics 69.

Beyramali Kivy, M., Asle Zaeem, M., 2017. Generalized stacking fault energies, ductilities, and twinnabilities of CoCrFeNi-based face-centered cubic high entropy alloys. Scr. Mater. 139, 83–86.

Cai, B., Liu, B., Kabra, S., Wang, Y., Yan, K., Lee, P.D., Liu, Y., 2017. Deformation mechanisms of Mo alloyed FeCoCrNi high entropy alloy: in situ neutron diffraction. Acta Mater. 127, 471–480.

ang, W., Yan, J., Yu, H., Bai, X., Li, J., Wang, S., Zheng, S., Yin, F., 2021. Microstructure and mechanical properties of CoCrNi-Mo medium entropy alloys:

ents and first-principle calculations. J. Mater. Sci. Technol. 62, 25–33.

:n, K., Wei, T., Li, G., Chen, M., Chen, Y., Chang, S., Yen, H., Chen, C., 2021. Mechanical properties and deformation mecanisms in cocremnni nigu europy auoys. a molecular dynamics study. Mater. Chem. Phys. 271, 124912.

Dai, C., Fu, Y., Pan, Y., Yin, Y., Du, C., Liu, Z., 2021. Microstructure and mechanical properties of FeCoCrNiMo0.1 high-entropy alloy with various annealing treatments. Mater. Charact. 179, 111313.

Dai, C., Zhao, T., Du, C., Liu, Z., Zhang, D., 2020. Effect of molybdenum content on the microstructure and corrosion behavior of FeCoCrNiMox high-entropy alloys. J. Mater. Sci. Technol. 46, 64–73.

Elmer, J.W., Palmer, T.A., Specht, E.D., 2007. In situ observations of sigma phase dissolution in 2205 duplex stainless steel using synchrotron X-ray diffraction. Mater. Sci. Eng.: A 459, 151–155.

Fan, N., Chen, T., Ju, J., Rafferty, A., Lupoi, R., Kong, N., Xie, Y., Yin, S., 2024. Solid-state deposition of Mo-doped CoCrFeNi high-entropy alloy with excellent wear resistance via cold spray. J. Mater. Res. Technol.

Gao, S., Li, Z., Van Petegem, S., Ge, J., Goel, S., Vas, J.V., Luzin, V., Hu, Z., Seet, H.L., Sanchez, D.F., Van Swygenhoven, H., Gao, H., Seita, M., 2023. Additive manufacturing of alloys with programmable microstructure and properties. Nat. Commun. 14, 6752.

Gao, S., Yoshino, K., Terada, D., Kaneko, Y., Tsuji, N., 2022. Significant Bauschinger effect and back stress strengthening in an ultrafine grained pure aluminum fabricated by severe plastic deformation process. Scr. Mater. 211, 114503.

Gan, J., Hou, J., Chou, T., Luo, X., Ju, J., Luan, J., Huang, G., Xiao, B., Zhang, J., Zhang, J., Tao, Y., Gao, J., Yang, T., 2024. A novel D022-strengthened medium entropy alloy with outstanding strength-ductility synergies over ambient and intermediate temperatures. J. Mater. Sci. Technol. 202, 152–164.

Gao, L., Wu, Y., An, N., Chen, J., Liu, X., Bai, R., Hui, X., 2024. Nanoscale l12 phase precipitation induced superb ambient and high temperature mechanical properties in ni-co-cr-al system high-entropy superalloys. Mater. Sci. Eng.: A 898, 145995.

Gludovatz, B., Hohenwarter, A., Catoor, D., Chang, E.H., George, E.P., Ritchie, R.O., 2014. A fracture-resistant high-entropy alloy for cryogenic applications. Science (1979).

Grimvall, 1975. Polymorphism in metals II. electronic and magnetic free energy. Phys. Scr. 12, 173.

Guo, B., Yang, Z., Wu, Q., Xu, C., Cui, D., Jia, Y., Wang, L., Li, J., Wang, Z., Lin, X., Wang, J., He, F., 2024. Multi-scale annealing twins generate superior ductility in an additively manufactured high-strength medium entropy alloy. Int. J. Plast., 104045

Guo, L., Wu, W., Ni, S., Yuan, Z., Cao, Y., Wang, Z., Song, M., 2020. Strengthening the FeCoCrNiMo0.15 high entropy alloy by a gradient structure. J. Alloys. Compd. 841, 155688.

Gyorffy, B., 1972. Coherent-potential approximation for a nonoverlapping-muffin-tin-potential model of random substitutional alloys. Physical Review B 5, 2382.

Gyorffy, B., Pindor, A., Staunton, J., Stocks, G., Winter, H., 1985. A first-principles theory of ferromagnetic phase transitions in metals. Journal of Physics F: Metal Physics 15, 1337.

He, F., Wang, Z., Han, B., Wu, Q., Chen, D., Li, J., Wang, J., Liu, C.T., Kai, J.J., 2018. Solid solubility, precipitates, and stacking fault energy of micro-alloyed CoCrFeNi high entropy alloys. J. Alloys. Compd. 769, 490–502.

He, J., Wu, X., Guo, Y., Makineni, S.K., 2021a. On the compositional and structural redistribution during partial recrystallisation: a case of  $ \sigma $-phase precipitation in a Mo-doped NiCoCr medium-entropy alloy. Scr. Mater. 194, 113662.

He, M., Cao, H., Liu, Q., Yi, J., Ni, Y., Wang, S., 2022. Evolution of dislocation cellular pattern in Inconel 718 alloy fabricated by laser powder-bed fusion. Addit. Manuf. 55, 102839.

He, Z., Jia, N., Yan, H., Shen, Y., Zhu, M., Guan, X., Zhao, X., Jin, S., Sha, G., Zhu, Y., Liu, C.T., 2021b. Multi-heterostructure and mechanical properties of N-doped FeMnCoCr high entropy alloy. Int. J. Plast. 139, 102965.

Hiyama, K., Ueki, K., Ueda, K., Narushima, T., 2024. Probing plastic deformation-related properties in static recrystallized Co–Cr–Fe–Ni–Mo alloy for biomedical applications. Mater. Sci. Eng.: A 899, 146458.

Hohenberg, P., Kohn, W., 1964. Inhomogeneous electron gas. Physical review 136, B864.

Hu, D., Grilli, N., Wang, L., Yang, M., Yan, W., 2022. Microscale residual stresses in additively manufactured stainless steel: computational simulation. J. Mech. Phys. Solids. 161, 104822.

Huang, S., Li, W., Lu, S., Tian, F., Shen, J., Holmström, E., Vitos, L., 2015. Temperature dependent stacking fault energy of FeCrCoNiMn high entropy alloy. Scr. Mater. 108, 44–47.

Huang, C.X., Wang, K., Wu, S.D., Zhang, Z.F., Li, G.Y., Li, S.X., 2006. Deformation twinning in polycrystalline copper at room temperature and low strain rate. Acta Mater. 54, 655–665.

Hou, J.X., Liu, S.F., Cao, B.X., Luan, J.H., Zhao, Y.L., Chen, Z., Zhang, Q., Liu, X.J., Liu, C.T., Kai, J.J., Yang, T., 2022. Designing nanoparticles-strengthened high-entropy alloys with simultaneously enhanced strength-ductility synergy at both room and elevated temperatures. Acta Mater. 238, 118216.

Yang, T., Zhao, Y.L., Fan, L., Wei, J., Luan, J.H., Liu, W.H., Wang, C., Jiao, Z.B., Kai, J.J., Liu, C.T., 2020. Control of nanoscale precipitation and elimination of intermediate-temperature embrittlement in multicomponent high-entropy alloys. Acta Mater. 189, 47–59.

Jo, M., Suh, J., Kim, M., Kim, H., Jung, W., Kim, D., Han, H.N., 2022. High temperature tensile and creep properties of crmnfeconi and CrFeCoNi high-entropy alloys. Mater. Sci. Eng.: A 838, 142748.

Jo, M., Koo, Y.M., Lee, B.J., Johansson, B., Vitos, L., Kwon, S.K., 2014. Theory for plasticity of face-centered cubic metals. Proc. Natl. Acad. Sci. u S. a 111, 6560–6565.

Karthik, G.M., Kim, H.S., 2021. Heterogeneous Aspects of Additive Manufactured Metallic Parts: a Review. Met. Mater. Int. 27, 1–39.

Kenji, K., Eishi, K., Joji, O., Masami, M., 2002. Effects of various alloying elements on tensile properties of high-purity Fe–18Cr–(14–16)Ni alloys at room temperature. Mater. Trans. 42, 155–162.

Körner, C., Markl, M., Koepf, J.A., 2020. Modeling and simulation of microstructure evolution for additive manufacturing of metals: a critical review. Metallur. Mater. Trans. A 51, 4970–4983.

Kuzminova, Y., Shibalova, A., Evlashin, S., Shishkovsky, I., Krakhmalev, P., 2021. Structural effect of low Al content in the in-situ additive manufactured CrFeCoNiAlx high-entropy alloy. Mater. Lett. 303, 130487.

Kwon, J., Karthik, G.M., Estrin, Y., Kim, H.S., 2022. Constitutive modeling of cellular-structured metals produced by additive manufacturing. Acta Mater. 241, 118421.

Laplanche, G., Kostka, A., Horst, O.M., Eggeler, G., George, E.P., 2016. Microstructure evolution and critical stress for twinning in the crmnfeconi high-entropy alloy. Acta Mater. 118, 152–163.

Li, R., One, P., Yang, X., Huang, Y., Ning, Z., Sun, J., Fan, H., 2022. Enhanced tensile properties and wear resistance of additively manufactured cocrfemnni high-entropy alloy at cryogenic temperature. Rare Metals. 41, 1210–1216.

Li, W., Long, X., Huang, S., Fang, Q., Jiang, C., 2019. Elevated fatigue crack growth resistance of Mo alloyed CoCrFeNi high entropy alloys. Eng. Fract. Mech. 218, 106579.

Lin, D., Xi, X., Li, X., Hu, J., Xu, L., Han, Y., Zhang, Y., Zhao, L., 2022. High-temperature mechanical properties of FeCoCrNi high-entropy alloys fabricated via selective laser melting. Mater. Sci. Eng.: A 832, 142354.

Lin, D., Chen, Q., Xi, X., Ma, R., Shi, Z., Song, X., Xia, H., Bian, H., Tan, C., Lu, Y., Li, R., 2024. Laser powder bed fusion to fabricate high-entropy alloy FeCoCrNiMo0.5 with excellent high-temperature strength and ductility. Mater. Sci. Eng.: A 900, 146413.

Lin, D., Xi, X., Ma, R., Shi, Z., Wei, H., Song, X., Hu, S., Tan, C., 2023. Fabrication of a strong and ductile FeCoCrNiMo0.3 high-entropy alloy with a micro-nano precipitate framework via laser powder bed fusion. Composites Part B: Engineering 266, 111006.

Linder, C., G. Rao, S., Boyd, R., Greczynski, G., Eklund, P., Munktell, S., le Febvrier, A., Björk, E.M., 2024. Effect of Mo content on the corrosion resistance of (CoCrFeNi)1-xMox thin films in sulfuric acid. Thin. Solid. Films. 790. 140220.

Liu, Y.Z., Shi, Z.L., Zhang, Y.B., Qin, M., Hu, S.P., Song, X.G., Fu, W., Lee, B.J., 2024. Effect of temperature on the mechanical properties of Ni-based superalloys via molecular dynamics and crystal plasticity. J. Mater. Sci. Technol. 203, 126–142.

Liu, S.Y., Wang, H., Zhang, J.Y., Zhang, H., Xue, H., Liu, G., Sun, J., 2022. Trifunctional Laves precipitates enabling dual-hierarchical FeCrAl alloys ultra-strong and ductile. Int. J. Plast. 159, 103438.

Liu, T.K., Wu, Z., Stoica, A.D., Xie, Q., Wu, W., Gao, Y.F., Bei, H., An, K., 2017. Twinning-mediated work hardening and texture evolution in CrCoFeMnNi high entropy alloys at cryogenic temperature. Mater. Des. 131, 419–427.

Liu, W.H., Lu, Z.P., He, J.Y., Luan, J.H., Wang, Z.J., Liu, B., Liu, Y., Chen, M.W., Liu, C.T., 2016. Ductile CoCrFeNiMox high entropy alloys strengthened by hard intermetallic phases. Acta Mater. 116, 332–342.

Liu, X., Hu, R., Yang, C., luo, X., Hou, Y., Bai, J., Ma, R., 2023. Strengthening mechanism of a Ni-based superalloy prepared by laser powder bed fusion: the role of cellular structure. Mater. Des. 235, 112396.

Liu, Y., Wang, K., Xiao, H., Chen, G., Wang, Z., Hu, T., Fan, T., Ma, L., 2020. Theoretical study of the mechanical properties of CrFeCoNiMo (x) (0.1 <= x <= 0.3) alloys. RSC. Adv. 10, 14080–14088.

Ming, K., Bi, X., Wang, J., 2019. Strength and ductility of CrFeCoNiMo alloy with hierarchical microstructures. Int. J. Plast. 113, 255–268.

Miracle, D.B., Senkov, O.N., 2017. A critical review of high entropy alloys and related concepts. Acta Mater. 122, 448–511.

Moruzzi, V., Janak, J., Schwarz, K., 1988. Calculated thermal properties of metals. Physical Review B 37, 790.

Munusamy, S., Jerald, J., 2023. Effect of in-Situ Intrinsic Heat Treatment in Metal Additive Manufacturing: a Comprehensive Review. Met. Mater. Int. 29, 3423–3441.

Otto, F., Dlouhý, A., Somsen, C., Bei, H., Eggeler, G., George, E.P., 2013. The influences of temperature and microstructure on the tensile properties of a CoCrFeMnNi high-entropy alloy. Acta Mater. 61, 5743–5755.

Peng, J., Li, J., Liu, B., Fang, Q., Liaw, P.K., 2024. Origin of thermal deformation induced crystallization and microstructure formation in additive manufactured FCC, BCC, HCP metals and its alloys. Int. J. Plast. 172, 103831.

Peng, Y., Jia, C., Song, L., Bian, Y., Tang, H., Cai, G., Zhong, G., 2022. The manufacturing process optimization and the mechanical properties of FeCoCrNi high entropy alloys fabricated by selective laser melting. Intermetallics. (Barking) 145, 107557.

Perdew, J.P., Burke, K., Ernzerhof, M., 1996. Generalized gradient approximation made simple. Phys. Rev. Lett. 77, 3865.

Ramakrishnan, N., 1996. An analytical study on strengthening of particulate reinforced metal matrix composites. Acta Mater. 44, 69–77.

Schönecker, S., Li, W., Vitos, L., Li, X., 2021. Effect of strain on generalized stacking fault energies and plastic deformation modes in fcc-hcp polymorphic high-entropy alloys: a first-principles investigation. Phys. Rev. Mater. 5, 075004.

Shi, Z., Liu, Y., Zhang, H., Li, C., Chen, S., Yang, Y., Liang, S., Ma, M., 2024. Synergistic strength-ductility enhancement of CoCrFeNi high-entropy alloys with regulated Co/Cr atomic ratios. Mater. Sci. Eng.: A 912, 146995.

Shahmir, H., Mehranpour, M.S., Arsalan Shams, S.A., Langdon, T.G., 2023. Twenty years of the CoCrFeNiMn high-entropy alloy: achieving exceptional mechanical properties through microstructure engineering. J. Mater. Res. Technol. 23, 3362–3423.

Shun, T.-T., Chang, L.-Y., Shiu, M.-H., 2012. Microstructure and mechanical properties of multiprincipal component CoCrFeNiMox alloys. Mater. Charact. 70, 63–67.

Sui, Q., Wang, Z., Wang, J., Xu, S., Liu, B., Yuan, Q., Zhao, F., Gong, L., Liu, J., 2022. Additive manufacturing of CoCrFeNiMo eutectic high entropy alloy: microstructure and mechanical properties. J. Alloys. Compd. 913, 165239.

Sun, J., Zhao, W., Yan, P., Li, S., Dai, Z., Jiao, L., Qiu, T., Wang, X., 2022. High temperature tensile properties of as-cast and forged CrMnFeCoNi high entropy alloy. Mater. Sci. Eng.: A 850, 143570.

Tian, C., Ouyang, D., Wang, P., Zhang, L., Cai, C., Zhou, K., Shi, Y., 2024. Strength-ductility synergy of an additively manufactured metastable high-entropy alloy achieved by transformation-induced plasticity strengthening. Int. J. Plast. 172, 103823.

Vitos, L., 2001. Total-energy method based on the exact muffin-tin orbitals theory. Physical Review B 64, 014107.

Vitos, L., Abrikosov, I., Johansson, B., 2001. Anisotropic lattice distortions in random alloys from first-principles theory. Phys. Rev. Lett. 87, 156401.

Vitos, L., Skriver, H.L., Johansson, B., Kollár, J., 2000. Application of the exact muffin-tin orbitals theory: the spherical cell approximation. Comput. Mater. Sci. 18, 24–38.

Wagner, C., Laplanche, G., 2023. Effect of grain size on critical twinning stress and work hardening behavior in the equiatomic CrMnFeCoNi high-entropy alloy. Int. J. Plast. 166, 103651.

Wang, J., Kwon, H., Kim, H.S., Lee, B.-J., 2023a. A neural network model for high entropy alloy design. NPJ. Comput. Mater. 9.

Wang, J., Liu, Y., Liu, B., Wang, Y., Cao, Y., Li, T., Zhou, R., 2017. Flow behavior and microstructures of powder metallurgical CrFeCoNiMo0.2 high entropy alloy during high temperature deformation. Mater. Sci. Eng.: A 689, 233–242.

Wang, L., Guo, Q., Chen, L., Yan, W., 2023b. In-situ experimental and high-fidelity modeling tools to advance understanding of metal additive manufacturing. International Journal of Machine Tools and Manufacture 193, 104077.

Wu, Q., Wang, Z., He, F., Li, J., Wang, J., 2018. Revealing the Selection of \sigma and \mu Phases in CoCrFeNiMox High Entropy Alloys by CALPHAD. J. Phase Equilibria Diffus. 39, 446–453.

Wu, X., Liu, L., Wang, R., Liu, Q., 2014. The generalized planar fault energy, ductility, and twinnability of al and Al—Re (Re = Sc, Y, Dy, Tb, Nd) at different temperatures: a first-principles study. CHINESE PHYS B 23, 66101–66104.

Yen, C.-C., Lin, S.-Y., Ting, C.-L., Tsai, T.-L., Chen, Y.-T., Yen, S.-K., 2024. Passivation mechanisms of CoCrFeNiMox (x = 0, 0.1, 0.2, 0.3) high entropy alloys and MP35N in 3.5 wt% NaCl aerated aqueous solutions. Corros. Sci. 228, 111812.

Yim, D., Sathiyamoorthi, P., Hong, S.-J., Kim, H.S., 2019. Fabrication and mechanical properties of TiC reinforced CoCrFeMnNi high-entropy alloy composite by water atomization and spark plasma sintering. J. Alloys. Compd. 781, 389–396.

Zhang, H., Liu, J., Sui, D., Cui, Z., Fu, M.W., 2018. Study of microstructural grain and geometric size effects on plastic heterogeneities at grain-level by using crystal plasticity modeling with high-fidelity representative microstructures. Int. J. Plast. 100, 69–89.