DOI: 10.1088/2631-7990/adbb95

PAPER • OPEN ACCESS

# Mechanical field assisted additive manufacturing of ultrahigh strength aluminum alloy

To cite this article: Wenjie Liu et al 2025 Int. J. Extrem. Manuf. 7 045008

View the  $ \underline{\text{article online}} $ for updates and enhancements.

## You may also like

- Performance-control-orientated hybrid metal additive manufacturing technologies: state of the art, challenges, and future trends

Jiming Lv, Yuchen Liang, Xiang Xu et al.

- Review on laser directed energy deposited aluminum alloys

Tian-Shu Liu, Peng Chen, Feng Qiu et al.

- Recent progress in bio-inspired macrostructure array materials with special wettability—from surface engineering to functional applications

Zhongxu Lian, Jianhui Zhou, Wanfei Ren et al.

Int. J. Extrem. Manuf. 7 (2025) 045008 (24pp)

# Mechanical field assisted additive manufacturing of ultrahigh strength aluminum alloy

Wenjie Liu $ ^{1,3,4} $, Shengnan Shen $ ^{1,5} $, Jinlong Meng $ ^{1} $, Jiafeng Xiao $ ^{1} $, Hui Li $ ^{1,5,**} $, Hejun Du $ ^{6} $, Qianxing Yin $ ^{1} $ and Chaolin Tan $ ^{2,3,*} $

 $ ^{1} $ School of Power and Mechanical Engineering, Wuhan University, Wuhan 430072, People’s Republic of China

 $ ^{2} $ Institute of Metallic Materials and Intelligent Manufacturing, Soochow University, Suzhou 215137, People’s Republic of China

 $ ^{3} $ Singapore Institute of Manufacturing Technology (SIMTech), Agency for Science, Technology and Research (A*STAR), 5 Cleantech Loop, Singapore 636732, Singapore

 $ ^{4} $ Henan Polytechnic University, Jiaozuo 454003, People’s Republic of China

 $ ^{5} $ The Institute of Technological Sciences, Wuhan University, Wuhan 430072, People’s Republic of China  

 $ ^{6} $ Nanyang Technological University, 50 Nanyang Avenue, Singapore 639798, Singapore

E-mail: cltan@suda.edu.cn, li_hui@whu.edu.cn and TCLSUCT@163.com

Accepted for publication 27 February 2025  

Published 3 April 2025

## Abstract

Additive manufacturing of aluminum (Al) alloys has attracted significant attention in the aerospace industry. However, achieving ultrahigh-strength (>500 MPa) Al alloys remains challenging due to their intrinsic poor printability. Here, we report a novel hybrid additive manufacturing (HAM) approach to process ultrahigh-strength AlMgSc alloy, which combines laser powder bed fusion (LPBF) with interlayer ultrasonic shot peening (USP). The results show that the interlayer ultrasonic shot peening depth reached ~700 \mum, leading to almost full density and residual stress convection from tension to compression. The HAM method promotes equiaxed grain formation and refines grain due to grain recrystallizations. Interestingly, the HAM followed by aging treatment tailors the hierarchically multi-gradient structures, inhibits Mg element intragranular segregation, and promotes the multi-nanoprecipitates (e.g. Al₃(Sc, Zr) and Al₆Mn) precipitation. Remarkably, the HAM followed by aging treatment achieves yield strength of 609 MPa and breaks elongation of 7.5%, demonstrating ultrahigh strength and good ductility compared with other Al alloys manufactured by AM and forging as reported in the literature. The strength enhancement mechanisms in this AlMgSc alloy are discussed. The high-density Al₃(Sc, Zr) precipitates are

the main strengthening contributor, and unique hetero-deformation induced (HDI) strengthening (originates from the heterogeneous microstructures) further enhances the strength of the material. This work highlights a novel approach for processing complex-structured ultrahigh strength Al alloy components by hybrid additive manufacturing.

## Supplementary Material

Keywords: additive manufacturing, AlMgSc alloy, hybrid additive manufacturing, gradient structures, dislocation evolution, mechanical properties

## 1. Introduction

Lightweight aluminum (Al) alloys are essential structural materials in the aerospace and transportation industries due to their low density and high strength, which enables products with lower fuel consumption and excellent performance $ ^{[1,2]} $. In particular, the development of ultrahigh-strength Al (UHSA) alloys (yield strength  $ \geq $500 MPa) is of significant interest for the aerospace application of load-bearing components, which is also a perpetual research hotspot $ ^{[3]} $. In addition, UHSA alloys have significant advantages and broad applications in advancing net-zero and sustainable ecosystems by reducing energy construction and waste emissions $ ^{[4,5]} $.

The traditional manufacturing methods for UHSA alloy components, such as cast, forging, extrusion, etc $ ^{[6,7]} $, failed to integrate intricate geometric structures with good strength-plasticity synergy. Fortunately, additive manufacturing (AM) enables the manufacture of extremely complex parts with tunable microstructures and properties on demand $ ^{[8,9]} $. Laser powder bed fusion (LPBF) is a widely used metal AM technique that enables the production of engineering components with intricate geometries and integrated functionalities, offering flexibility in design and cost efficiency $ ^{[10]} $. LPBF technology also has high potential in manufacturing Al alloy components with complex geometric structures, high strength, and good ductility. For instance, Li et al. $ ^{[10]} $ developed a high-strength AlMgSiScZr alloy by adjusting Mg content, and the heat-treated sample exhibited an ultimate tensile strength (UTS) of 550 MPa and an elongation ( $ \varepsilon $) of 8%. Current LPBF-manufactured high-strength Al alloys include Al-Mg $ ^{[10]} $, Al-Cu $ ^{[11]} $, and Al-Zn-Mg-Cu alloy $ ^{[12]} $. Among them, the LPBF-manufactured Al-Mg alloys exhibit good weldability, high strength, and excellent corrosion resistance $ ^{[13,14]} $. However, the LPBF-manufactured Al-Mg alloy is susceptible to various defects, including keyholes and element loss $ ^{[15,16]} $. Specifically, the low boiling point Mg element evaporates during high-energy laser processing, leading to severe porosity and element loss, which subsequently reduces the material mechanical properties $ ^{[17,18]} $. To solve the problem of solidification racking and insufficient mechanical properties, Sc and Zr elements are often added to Al-Mg alloys for inoculation treatments $ ^{[16]} $. Li et al. $ ^{[19]} $ fabricated a novel AlMgScZr alloy by LPBF and achieved a yield strength of 451 MPa along with a good  $ \varepsilon $ of 15.1%. However, it failed to achieve effective precipitation of Al $ _{3} $(Sc, Zr), particularly secondary Al $ _{3} $(Sc, Zr) nanoparticles in this AlMgScZr alloy due to the hindered nanoparticles nucleation by the intrinsic rapid cooling rate of LPBF process $ ^{[20,21]} $. Heat treatment (HT) is an effective method for enhancing the mechanical properties of the LPBF-manufactured AlMgSc alloy, which precipitates Al $ _{3} $(Sc, Zr) nanoparticles (L $ _{1} $2 structure) and inhibits grain boundary segregation. The mechanical properties of Scalmalloy $ ^{\circledR} $ alloy can be improved by aging treatment to attain yield strength above 450 MPa and UTS over 515 MPa, together with an  $ \varepsilon $ above 8% $ ^{[13]} $. Similar research was reported by Jia et al. $ ^{[22]} $.

However, heat treatments could induce grain growth and fail to eliminate internal keyholes, which limits the improvement in strength. Surface nanocrystalline modification techniques, such as ultrasonic shot peening (USP), laser shock peening (LSP), and mechanical rolling, have been deployed to generate gradient nanostructured (GNS) materials with exceptional mechanical properties $ ^{[23]} $. GNS materials have been predominantly deployed to metals to enhance the strength-ductility synergy, which offers guidance for enhancing the performance of AM-processed Al alloys. Chen et al. $ ^{[24]} $ developed an effective ultrasonic surface rolling process technology to improve the fatigue life of AM-processed CoCrNi alloy. Interestingly, Zhou et al. $ ^{[25]} $ proposed an LSP-assisted AM process to fabricate a highly dense AlSi10Mg alloy with excellent strength and plasticity. Besides, severe plastic deformation could also facilitate the closure of pores in material $ ^{[26,27]} $. For example, USP treatment featured with a profoundly affected area is an effective method to achieve pore closure, gradient microstructure, and strength-ductility synergy $ ^{[28]} $.

In this paper, we propose a USP-assisted LPBF manufacturing method for developing ultrahigh strength AlMgSc alloy with hierarchically gradient microstructures. Subsequent aging treatment is applied to facilitate the formation of multinanoprecipitates. The effect of LPBF parameters on densification behaviour is investigated, followed by studies on the effect of ultrasonic impact energy on microstructures. Besides, the residual stress and dislocation evolution, microstructure evolution, and strengthening mechanisms are discussed in detail.
Figure 1. Powder characteristics, hybrid additive manufacturing process, and characterization of AlMgSc alloy: (a) AlMgSc powder morphology, (b) EDS mapping analysis of powder, (c) schematic diagram of USP-assisted LPBF hybrid additive manufacturing processes followed by subsequent aging treatment (HAM-HT), (d) gradient microstructures, (e) schematic diagram of microstructure and residual stress characterization, and (f) tensile specimen dimensions (2 mm thick).

## 2. Method and materials

## 2.1. Materials and sample preparation

The gas-atomized spherical AlMgSc powder (Al-4.7 Mg-1.3Sc-0.6Zr-0.8Mn-0.01Si, wt%) was used as feedstock. The AlMgSc powder exhibits high sphericity with a particle size of 21.8–61.9  $ \mu $m (37  $ \mu $m on average), as shown in Figures 1(a) and (b). The detailed HAM method is shown in Figure 1(c), which aims to achieve a multilayer gradient structure, as illustrated in Figure 1(d). The LPBF process was performed using an SLM $ ^{\textregistered} $125 system, with the substrate preheated to 100 ^\circC. The oxygen level in the chamber during the LPBF process was kept below 0.1 vol% via argon gas flow. The process parameters were optimized to obtain high-density process parameters, which were elucidated in Supplementary Table S_{1}.

The USP process was performed using a UPM-3 000 equipment with 2.0 mm diameter bearing steel shots under an ultrasonic frequency of 20 kHz. As the effect of compressive residual stress (CRS) depth of USP was critical for pore closure and mechanical properties $ ^{[28]} $, different amplitudes of vibrating head, i.e. 30  $ \mu $m, 35  $ \mu $m, and 40  $ \mu $m, were set to optimise the CRS. The USP treatment was conducted at a distance of 16 mm. The USP process was ex-situ applied to the LPBF process every 33 layers (i.e. height of approximately  $ \sim $1.0 mm), with each USP treatment lasting 8 min. The USP effect area was a 30 mm diameter circular region, as shown in Figure 1(f). After sample fabrication, samples were aging treated in a TL1200 tube furnace protected by high-purity argon gas. A lower temperature aging (i.e. 300 ^\circC for 4 h, furnace cooling) was chosen in this work, given that the Al $ _{3} $(Sc,

Zr) nanoprecipitates were precipitated at a temperature range of 300 ^\circC–350 ^\circC $ ^{[16]} $, and a high HT temperature will coarsen the precipitates $ ^{[29,30]} $. Four types of samples were processed in this work for comparison: (i) the LPBF as-built sample (termed as LPBF), (ii) LPBF followed by aging treatment (termed as LPBF-HT), (iii) USP-assisted LPBF hybrid additive manufactured sample (termed as HAM), and (iv) HAM processed sample followed by subsequent aging treatment (termed as HAM-HT).

## 2.2. Microstructure characterization

The surface roughness of the AlMgSc samples was evaluated using the NewView 9000 3D optical profiler. The surface roughness measurement region was about 1.75 mm \times 1.75 mm, with repeated measurements on 3 randomly selected regions to calculate the average value. Microstructure analysis was performed on the longitudinal section of the AlMgSc samples, as shown in Figures 1(e) and (f). The relative density and porosity were detected by Archimedes' principle and micro-computed tomography (micro-CT) technology using a printed block with a size of 6 mm \times 6 mm \times 6 mm. The relative density of the LPBF sample was determined using Archimedes' principle to identify the optimal LPBF parameters. The theoretical density of AlMgSc calculated by JMatPro software is 2.72 g·cm⁻¹, and each block measurement was repeated 3 times. The LPBF, HAM, and HAM-HT samples were scanned using a nanoVoxel-4000 Micro-CT system at 200 kV voltage with a 3.9 \mum resolution to evaluate the porosity and verify the accuracy of the Archimedes test. Internal defect analysis was conducted using the Avizo software. An M230-3M180 optical microscope (OM) was used to observe the internal pores of the AlMgSc samples. Phase constitutions were identified by x-ray diffraction (XRD, D8 FOCUS) using Cu K\alpha radiation. The grain size, geometrically necessary dislocations, and textures were characterized by electron backscatter diffraction (EBSD), with the step sizes for the entire and ultra-fine grain regions of 0.3 \mum and 0.06 \mum, respectively. The EBSD data were analyzed by the AZtecCrystal software. The dislocation, precipitates, and element content were analyzed by Transmission electron microscopy (TEM, Thermofisher Talos F200X) and energy dispersive spectroscopy (EDS) operated at 200 kV. The detailed test sampling location of the microstructure is shown in Figure 1(e).

## 2.3. Residual stress and mechanical testing

According to GB/T 7704-2017 standard, an x-ray residual stress analyzer (X-350 A) with 20 kV and 5.0 mA was used to measure the residual stress in the sample along the depth. The Sid-inclination method was used to calculate the residual stress of AlMgSc alloy. Before residual stress measurements, the surfaces were manually ground using SiC sandpaper and polished using aqueous diamond suspension. The surface residual stress at depths of 0 \mum, 200 \mum, 400 \mum, 600 \mum, and 800 \mum was tested by removing the material by electrolytic polishing. Three points were measured at each depth to calculate the average value. The detailed detection position of surface residual stress is shown in Figure 1(e). Uniaxial tensile tests were performed on an INSTRON 68MT-50 universal material testing machine using a loading speed of 1 mm·min⁻¹. The loading-unloading-reloading process was carried out on the INSTRON 5982 universal material testing machine at a loading speed of 1 mm·min⁻¹. The unloading started at the strain of 2%, 4%, and 6%, respectively, until 50 MPa, and then reverting to loading automatically. A non-contact advanced video extensometer (AVE) was applied to measure the strain with a gauge length of 6 mm. The tensile sample dimension is shown in Figure 1(f). Tensile properties were assessed through 3–4 repeated tests and tensile fracture morphology was observed using SEM.

## 3. Results

## 3.1. Printing quality and defect regulation

Porosity is the key factor in evaluating the LPBF printing quality. Figure 2 shows the defect morphology, porosity, and relative density of LPBF samples. Figure 2(a) illustrates the defect types in the laser energy density ( $ E_{\nu}/(\text{J}\cdot\text{mm}^{-3}) $) range from 55.6 to 648.2 J·mm $ ^{-3} $, including lack of fusion, gas pore, and keyhole, while without discernible cracks. Numerous keyholes mainly concentrate in the range with high laser power (P) and low scanning speed ( $ \nu $), while plentiful lack of fusions concentrate in the range of low laser power and high scanning speed. The formation of keyholes is not only caused by excessive laser energy input but also attributed to Mg element loss $ ^{[31]} $. In contrast, lack of fusion is caused by insufficient  $ E_{\nu} $, which leads to incomplete melting of powder. Besides, small gas pores are randomly distributed in all samples with limited numbers. These gas pores are from the entrapment of protective gas in solidification and are inherited from the powder $ ^{[32]} $. Interestingly, porosity varies significantly for diverse combinations of P and  $ \nu $ even under the same  $ E_{\nu} $. The red border area in Figure 2(a) represents suitable printing parameters. Figure 2(b) shows the relative density demonstrates notable improvement within the  $ E_{\nu} $ range of 100 –200 J·mm $ ^{-3} $, the relative density can reach up to 99.69% at an  $ E_{\nu} $ of 185.2 J·mm $ ^{-3} $, and porosity analysis by Micro-CT was conducted on this sample. The porosity measured through Micro-CT is about 0.309%, whereas the porosity determined by Archimedes testing is 0.310% (Figure 3(a)), showing good consistency. The effect of USP assistance during LPBF on the densification behavior was studied by Micro-CT analysis, as shown in Figure 3.

Figure 3(a) shows the porosity of the LPBF sample is 0.309%, together with an abundant lack of fusions and keyholes. Note that the lack of fusion and keyhole pores have a significant impact on materials performance than gas pores $ ^{[33]} $. Representative lack of fusions and keyholes are shown in Figure 3(a) (marked as #2 and #3), with the maximum equivalent diameter of lack of fusion exceeding 400  $ \mu $m, which suggests it is necessary to improve the densification of LPBF manufactured AlMgSc alloy. After USP treatment, there is
Figure 2. Defects and densification of LPBF manufactured AlMgSc alloy: (a) OM microstructure, and (b) relative density and porosity versus laser energy densities. (The red border area represents suitable printing parameters.).

a substantial decrease in porosities, from 0.309% in the as-LPBFed sample to 0.049% and 0.018% in the HAM and HAM-HT samples, respectively, as shown in Figures 3(b) and (c). Besides, Figure 3(c) shows the keyhole and lack of fusion in the HAM-HT sample are almost eliminated with small gas pores. Notably, the HAM-HT method yields the most favorable results, achieving almost fully dense AlMgSc alloy. The internal porosity of the HAM-HT sample is further reduced compared with that of the HAM sample, which indicates that aging treatment will not open the USP-collapsed pores.

## 3.2. Residual stress distribution

Figure 4 shows the distribution of residual stress along the depth direction of the LPBF, LPBF-HT, HAM, and HAM-HT samples. The positive residual stress indicates tensile residual
Figure 3. Micro-CT tomographs showing 3D distributions of defect and porosity in (a) LPBF, (b) HAM, and (c) HAM-HT samples.
Figure 4. Residual stress distributions of the LPBF, LPBF-HT, HAM, and HAM-HT samples.

stress (TRS), while negative residual stress represents CRS. The uneven temperature field generated by heat input in the LPBF process leads to TRS in the material, which has a significant impact on material strength $ ^{[22]} $. In contrast, the CRS can close pores and prevent crack propagation, improving material densification $ ^{[34]} $. In Figure 4, the LPBF sample exhibits significant TRS up to 167 MPa on the surface and gradually decreases with increasing depth. However, aging treatment can diminish TRS to some extent (i.e. in the LPBF-HT sample). Interestingly, the TRS is transferred into CRS after USP treatments (i.e. in HAM and HAM-HT samples), and the CRS increases gradually with increasing depth from the surface until reaching the peak CRS value ( $ \sim $250 MPa) at a depth of 400 –600  $ \mu $m. and then gradually decreased until it is converted to TRS. The CRS on the surface of the HAM-HT sample is lower than that at a depth of 400  $ \mu $m, which is closely related to the TRS generated inside the LPBF during rapid solidification. The TRS of the LPBF sample is the largest (167 MPa) at the surface but is almost 0 MPa at a depth of 400  $ \mu $m. The CRS and TRS of the HAM-HT sample after impact treatment offset each other, so the CRS does not show the gradient distribution. Similar results were also reported in $ ^{[35]} $. Meanwhile, the effective depth of the HAM and HAM-HT samples exceeds 600  $ \mu $m, which is comparable to LSP treatment $ ^{[25,34]} $.

Severe TRS in the LPBF process may cause cracking in the material, limiting the applicability of the components $ ^{[22,36]} $. The interlayer USP demonstrated the capability to control residual stress in LPBF-manufactured parts. The multi-scale stress analysis of the HAM-HT manufactured AlMgSc alloy is shown in Figure 5. Figure 5(a) shows macroscopic residual stress evolution with ultrasonic energies. The CRS effect is obvious as ultrasonic energy increases from 30  $ \mu $m to 40  $ \mu $m. The maximum velocity of ultrasonic shot peening particles can be expressed as $ ^{[37]} $:

 $$ \nu_{max}=\left(\frac{\partial x\left(t\right)}{\partial t}\right)_{max}=2\pi A f $$ 

where A is the amplitude, and f is the frequency. The shot speed of the ultrasonic generator is proportional to its amplitude. A larger amplitude allows the pellets to achieve a higher
Figure 5. Residual stress evolution analysis: (a) residual stress evolution with ultrasonic energies, (b) strain-contouring distribution maps by EBSD, (c) interfacial lattice stress of primary  $ \mathrm{Al}_{3}(\mathrm{Sc}, \mathrm{Zr}) $ nanoprecipitate and matrix by Strain++ software.

initial velocity, resulting in greater impact velocity and kinetic energy. This higher kinetic energy produces greater plastic deformation in the material.

The relationship between the residual stress and plastic deformation in the ultrasonic impact strengthening specimen can be expressed as $ ^{[38]} $:

 $$ \sigma_{\mathrm{r e s}}=\sigma_{0}+\mu\varepsilon_{\mathrm{p}}\left(\frac{1+\upsilon}{1-\upsilon}\right)\left[1-\frac{4\sqrt{2}}{\pi}\left(1+\upsilon\right)\frac{L}{a}\right] $$ 

where  $ \sigma_{res} $ is the residual stress,  $ \varepsilon_{p} $ is the plastic strain induced by shot peening,  $ \sigma_{0} $ is the friction stress,  $ \mu $ is the Lame constant,  $ \upsilon $ is the Poisson’s ratio, a is the orientation factor, L is the effective depth. Based on equation (2), the residual stress in the specimen is proportional to the plastic deformation. Therefore, the CRS in the HAM-HT part is maximized at an amplitude of 35–40  $ \mu $m with an effective depth exceeding  $ \sim $700  $ \mu $m. The interlayer impact-induced CRS layer effectively inhibits crack propagation and ensures good plasticity $ ^{[39]} $. Besides, residual stress is closely related to microstrain and interfacial lattice stress between precipitate and matrix $ ^{[40]} $. Figure 5(b) shows the LPBF-HT sample exhibits massive grain action strain compared with LPBF. The high-density strain distribution of the HAM-HT sample mainly comes from the highly deformed grains induced by CRS. Figure 5(c) shows the Al $ _{3} $(Sc, Zr) presents both positive and negative lattice strains along  $ \sigma_{xx} $ and  $ \sigma_{yy} $ in the Al matrix with a value of up to 20%, suggesting a large amount of lattice distortion inside the matrix, which promotes strain accumulation and helps to strengthen Al matrix $ ^{[41]} $.

## 3.3. Microstructure analysis

3.3.1. Grain characteristics analysis. The microstructure of LPBF-manufactured AlMgSc alloy is shown in Figure 6(a), which exhibits multimodal grains with coarse columnar grains (CCGs), coarse equiaxed grains (CEGs), and fine equiaxed grains (FEGs). The FEGs exhibit an average diameter of  $ (1.25 \pm 0.13) $  $ \mu $m, which mainly fills the melt pool boundaries, occupying over 65% of the entire scan area, as shown in Figure 6(a). CCGs and CEGs of the LPBF sample are represented by coarse grains (CGs) with sizes between 1.5  $ \mu $m and 7.8  $ \mu $m (average  $ (1.86 \pm 0.48) $  $ \mu $m), which are mainly in the center of the melt pool (Figures 6(a) and (e)). After heat treatment, the number of coarse grains in the LPBF-HT sample is increased (Figures 6(b) and (g)). This is because
Figure 6. EBSD analysis of AlMgSc alloy produced by different processes: (a) LPBF, (b) LPBF-HT, (c) HAM and (d) HAM-HT samples’ grain morphology; (e) grain size distribution; (f) and (g) average grain size and proportion of the fine grain and coarse grain, respectively; (h) LPBF, (i) LPBF-HT, (j) HAM and (k) HAM-HT samples’ grain boundary maps; and (l) LPBF, (m) LPBF-HT, (n) HAM and (o) HAM-HT samples grain boundary distribution (black line represents high angle grain boundaries (HAGBs,  $ \theta > 15^{\circ} $) and green line represents low angle grain boundaries (LAGBs,  $ 2^{\circ}-15^{\circ} $) $ ^{[44]} $).

the aging treatment accelerates grain boundary migration, and promotes the growth of original fine grains in AlMgScZr alloy $ ^{[42]} $. Interestingly, USP is beneficial to promote the grain homogenization of AlMgSc samples. The grain morphology changed obviously in HAM and HAM-HT samples, especially in the HAM-HT sample, almost without CCGs, as shown in Figures 6(c) and (d). The original coarse columnar grains in the LPBF and LPBF-HT samples were transformed into homogeneous equiaxed grains in the HAM and HAM-HT samples. Figure 6(f) shows the average grain sizes of FEGs in LPBF, LPBF-HT, HAM, and HAM-HT samples, which were  $ (1.249 \pm 0.129) $  $ \mu $m,  $ (1.254 \pm 0.130) $  $ \mu $m,  $ (1.235 \pm 0.128) $  $ \mu $m, and  $ (1.241 \pm 0.128) $  $ \mu $m, respectively, with corresponding portion of 65.83%, 56.78%, 66.52% and 61.05%. After USP treatment, the grain size and number of HAM and HAM-HT samples were improved. Figure 6(g) shows that USP and HT treatments have no evident impact on the coarse grain size, but facilitated the formation of equiaxed grains. Thus, the HAM proves to be an efficient method for grain homogenization and columnar to equiaxed transition of AlMgSc samples. Figures 6(h)–(k) show interlayer USP promotes the formation of low-angle grain boundaries (LAGBs), and the LAGBs content reached the highest in the HAM-HT sample. Detailed grain misorientation angle distributions are plotted in Figures 6(l)–(o), in which the LAGBs contents in LPBF, LPBF-HT, HAM, and HAM-HT samples are 3.5%, 6.8%, 10.6%, and 15.4%, respectively. The augmented LAGBs of the HAM-HT sample can be attributed to the dislocation pile-up resulting from severe deformation $ ^{[43]} $.

The ultra-fine grains of LPBF-manufactured Al-Mg alloy contribute more to strength than CGs $ ^{[45]} $. Hence, the FEGs zone was further studied by EBSD in Figure 7 at a higher magnification. Figure 7(a) shows many ultra-fine equiaxed grains (UFEGs) with grain diameter of  $ <1 \mu m $ in the HAM-HT sample taken from the FEGs region. The average diameter of UFEGs is about  $ (0.60 \pm 0.21) \mu m $ with the smallest one down to  $ \sim 200 nm $ (Supplementary Figure S_{1}). This indicates that HAM-HT promotes the UFEGs nucleation.
Figure 7. Microstructure characteristics of UFEGs: (a) and (b) EBSD analysis of the UFEGs morphologies and recrystallization statistics of the HAM-HT sample, and (c)–(e) TEM show UFEGs morphologies of the LPBF, LPBF-HT, and HAM-HT samples.

Figure 7(b) shows the internal average misorientation angle (IAMA) map, which quantitatively reflects the recrystallization of the HAM-HT sample. The IAMA greater than 1^\circ is classified as deformed region. Grains composed of sub-grains with an IAMA less than 1^\circ but with orientation differences between subgrains exceeding 1^\circ are categorized as substructured regions. The remaining grains are classified as recrystallized regions $ ^{[46]} $. Figure 7(b) illustrates the recrystallized, substructured, and deformed grains, accounting for 97.1%, 2.4%, and 0.5% volume fractions, respectively. Notably, a substantial proportion of UFEGs is recrystallized grains, indicating that recrystallization is the main mechanism for UFEGs formation. More intriguingly, the smallest UFEGs of the HAM-HT samples are deformed grains. This is because the hard UFEGs inside are fractured by ultrasonic shock waves, resulting in grains at the nanometer level. A similar finding was reported in ultrasonic-assisted additive manufacturing of the 15-5PH stainless steel $ ^{[47]} $. Figure 7(c) reveals that the UFEGs size of the LPBF sample is as large as  $ \sim $700 nm. Moreover, substantial precipitation and agglomeration occur at grain boundaries and are accompanied by a few dislocations within the grain. In contrast, in the LPBF-HT and HAM-HT samples, there are formed high-density precipitates, mostly at grain boundaries (Figures 7(d) and (e)).

Solution strengthening is one of the main hardening mechanisms in Al-Mg alloys; hence, the main solid-soluble elements (i.e. Mg, Sc, and Mn) in FEGs (Supplementary Figures S_{2}(a)–(c)) and CGs regions (Supplementary Figures S_{2}(d)–(f)) of LPBF, LPBF-HT, and HAM-HT samples were analyzed and shown in Figures 8(a)–(c). Mg element, as the main solid solution element in Al-Mg alloy, mainly plays a role in refining grain and improving alloy strength $ ^{[48]} $. The Mg content in FEGs in the LPBF sample is lower compared with metal powder (Figure 8(a)). Interestingly, the content of the Mg element in CGs exceeds that in FEGs, which indicates that the solid solubility of Mg in CGs was higher than that in FEGs. The low content of Mg dissolved in the Al matrix of the LPBF sample reduced solid solution strengthening capability. In addition, there is a significant increase in the Mg element content in the FEG regions of the LPBF-HT and HAM-HT samples, i.e.  $ (4.4 \pm 0.8) $ at.\% and  $ (4.5 \pm 0.6) $ at.\%, respectively, as shown in Figures 8(b) and (c). This indicates that the LPBF-HT and HAM-HT process can effectively inhibit the Mg segregation and enhance the material's solid solution strengthening. Figures 8(b) and (c) show the Sc and Mn elemental contents with evident variations in different samples, which is closely related to the precipitation of  $ Al_{6}Mn $ and  $ Al_{3}Sc $ in response to the diffusion of Sc and Mn elements $ ^{[22,49]} $.

## 3.3.2. Phase and nanoprecipitate characteristics analyses.

Nanoprecipitation plays a crucial role in strengthening Al-Mg alloy by hindering dislocation movement. The main precipitates in this alloy were identified as  $ Al_{3}Sc $ and  $ Al_{3}Zr $ by XRD scan (Figure 9) together with phase diagram calculation in Supplementary Figure S_{3}. In addition, a small amount of  $ Mg_{2}Si $ and  $ Al_{6}Mn $ was identified in the phase calculations, however, no distinct peaks were observed in the XRD results, likely due to the limited content and small size. Relevant
Figure 8. Element content statistics of main solid solution elements: (a) Mg, (b) Sc, and (c) Mn. The locations of measurements are shown in Supplementary Figure S_{2}.
Figure 9. Phase composition of AlMgSc alloy in different conditions: (a) XRD diffractograms of the LPBF, LPBF-HT, HAM, and HAM-HT samples, and the zoom-in image of the selected (b) (111) and (c) (220) peaks.

literature $ ^{[32,50]} $ has reported the precipitation of  $ Al_{3}Sc $, and  $ Al_{3}Zr $ in LPBF-manufactured AlMgSc alloy. The primary diffraction peak observed in all samples is  $ \alpha $-Al. Nevertheless, the peaks corresponding to  $ Al_{3}(Sc, Zr) $ were exclusively detected in the LPBF-HT and HAM-HT samples in Figures 9(a) and (c). No evident  $ Al_{3}(Sc, Zr) $ peaks were observed in LPBF and HAM samples (without HT) due to the sluggish diffusion of Sc and Zr elements.

TEM analysis was conducted to further investigate the nanoprecipitates. Figure 10(a) shows the Mg enrichment network at the grain boundary of CGs in the LPBF sample, while white round particles enriched with Mg elements are randomly dispersed in the grains. Figure 10(b) shows the more significant enrichment of Mg-enrichment networks along the grain boundary of FEGs, suggesting Mg is more keen to segregate at the FEGs than in CGs. Besides, Figure 10(c) shows the network dislocation structures with embedded Mg-enriched particles. The white round particles enriched in Mg and O elements are identified as MgO nanoprecipitates by EDS analysis in Figures 10(d) and (e), which are formed due to the reaction between residual oxygen (in the powder or the processing chamber) with active Mg. A similar finding was also observed in LPBF-manufactured AlMnMg alloy by Bayoumy et al. $ ^{[51]} $. Figures 10(d) and (e) also show the Sc and Zr-enriched nanoparticles persist at CGs. Furthermore, the diameter of MgO nanoparticles is 20–50 nm, and a small amount of black Sc and Zr-enriched nanoparticles are in polygons with a length of  $ \sim $50 nm. The lattice structures of the Sc- and Zr-enriched nanoparticles are determined by selected area electronic diffraction (SAED) analysis (Figure 10(f)). Sc and Zr enriched nanoparticles are the Al $ _{3} $(Sc, Zr) with L1 $ _{2} $ structure. It is observed that Al $ _{3} $(Sc, Zr) particles are predominantly square-shaped and concentrated mainly at grain boundaries (Figure 10(g)). In addition, there are many Al $ _{3} $(Sc, Zr) nanoparticles agglomerates at the grain boundaries of the FEGs.

Figure 11 shows the nanoprecipitates in the LPBF-HT sample. Figure 11(a) shows the CGs and FEGs regions, with zoom-in images displayed in Figures 11(b) and (c), respectively, showing that the nanoprecipitate contents in CGs are lower than that in FEGs. There are evident dislocations networks in the CGs region (Figure 11(b)) and nanoprecipitates mainly along grain boundaries in FEGs (Figure 11(c)).
Figure 10. TEM morphologies and EDS mapping analysis of nanoprecipitates in the LPBF sample: (a) and (b) CGs and FEGs morphologies along with Mg element mapping, (c) bright field (BF) image shows rich-Mg nanoparticles distribution, (c) FEGs morphology and Al, Mg elements mapping, (d) and (e) nanoprecipitates in CGs and FEGs, (f) high-angle annular dark field (HAADF) image taken in CGs and SAED pattern from the yellow block, and (g) BF image taken in FEGs, interface of nanoprecipitate and matrix, and SAED pattern from the red block.

Compared with the LPBF sample (Figures 10(a) and (b)), the Mg-rich network disappeared in the LPBF-HT sample as revealed by Figures 11(d) and (e), suggesting a homogeneity distribution of Mg element, and subsequently better solid solution strengthening from Mg. Besides, Figure 11(d) shows the presence of massive Mn-enriched nanoparticles with a length of  $ \sim $20 nm, and also a small amount of Al $ _{3} $(Sc, Zr) nanoparticles. The enriched Mn nanoparticles could be Al $ _{6} $Mn, which is a typical precipitate in LPBF-manufactured AlMgSc alloy $ ^{[52,53]} $. Figure 11(e) shows there are only Al $ _{3} $(Sc, Zr) and Al $ _{6} $Mn nanoparticles in the matrix, but also Si-riched nanoparticles in the FEGs region. Notably, the co-existing of Si and Mg enrichments at the same positions suggests the formation of Mg $ _{2} $Si. Overall, the precipitate density in the FEGs region of the LPBF-HT samples (Figure 11(e)) is significantly higher than that in the LPBF sample (Figure 10(e)).

Further TEM analysis on the HAM-HT sample is shown in Figure 12. Figures 12(a) and (b) show ultra-fine columnar grains with a width of  $ \sim $300 nm and dense dislocations in the HAM-HT sample, which are caused by severe plastic deformation after interlayer USP impact. Besides, Mg network structures in both CGs and FEGs regions are eliminated, concomitant with the formation of uniformly distributed Mg $ _{2} $Si nanoprecipitates (Figures 12(c), (e), and (f)). Figures 12(b) and (d) reveal the presence of numerous dislocation cells in both CGs and FEGs regions, with dislocations entangled around the precipitates. Figures 12(e) and (f) illustrate the multi-precipitates in both CGs and FEG regions, which are Al $ _{3} $(Sc, Zr) and Al $ _{6} $Mn precipitates. Figure 12(g) shows primary Al $ _{3} $(Sc, Zr) alongside the SAED pattern taken from the [001] zone axis. The coherent interface between Al $ _{3} $(Sc, Zr) and Al matrix can effectively transfer load, induce crack deflection, and hinder dislocation movement. The secondary Al $ _{3} $(Sc, Zr) precipitates are generally formed during the HT process. Aging treatment facilitates the precipitation of a substantial amount of secondary Al $ _{3} $(Sc, Zr) within the matrix. Figure 12(h) shows high-density secondary Al $ _{3} $(Sc,
Figure 11. TEM and EDS images show the nanoprecipitates of the LPBF-HT sample: (a) coarse-fine grain transition region, (b) grain morphologies and dislocation distribution of CGs, (c) grain morphologies of FEGs, (d) nanoprecipitates structures in CGs, and (e) nanoprecipitates structures in FEGs.

Zr) precipitates with a width of  $ \sim $5 nm in the zoom-in image, which is uniformly distributed throughout the matrix. Fast Fourier Transform (FFT) analysis reveals that the secondary  $ Al_{3}(Sc, Zr) $ has an  $ L1_{2} $ structure. Hence, the HAM followed by HT achieves the coexistence of high dislocation density and high-volume fraction of multi-precipitates in the AlMgSc alloy.

## 3.4. Mechanical properties

Figure 13(a) shows the engineering tensile stress-strain curve of the LPBF, LPBF-HT, HAM, and HAM-HT samples (repeated engineering tensile stress-strain curves are shown in Supplementary Figure S_{6}). The stress-strain curve indicates that the alloy undergoes discontinuous yielding under tensile deformation with the transition from higher yield strength ( $ \sigma_{u}y $) to lower yield strength ( $ \sigma_{ly}y $). However, the LPBF and HAM samples have an obvious Portevin-Le Chatelier (PLC) effect, as shown in Figure 13(a). The PLC effect typically manifests as local instability in materials under continuous stress, resulting in noticeable discontinuities in the stress-strain curve. This phenomenon may lead to early failure or a decrease in material durability $ ^{[54]} $. Fortunately, there is no PLC effect in LPBF-HT and HAM-HT samples. Figure 13(b) and Table 1 summarise the tensile results of different samples. The average yield strength (YS), ultimate tensile strength (UTS), and break elongation ( $ \varepsilon $) of the LPBF sample are  $ (429 \pm 20) $ MPa,  $ (447 \pm 19) $ MPa, and  $ (8.9 \pm 1.5)\% $, respectively. After LPBF-HT, HAM, and HAM-HT, the material’s strength significantly increases with a minor loss in  $ \varepsilon $. The yield strength of the LPBF-HT sample is  $ (539 \pm 6) $ MPa, suggesting an increase of  $ \sim 100 $ MPa in yield strength by aging treatment at  $ 300\ ^{\circ}C $ for 4 h due to the precipitation of the high-density  $ Al_{3}(Sc, Zr) $ nanoprecipitates.

In addition, the YS and UTS of the HAM-HT sample both exceed 600 MPa while maintaining good plasticity. Compared with the LPBF sample, the YS, and UTS of the HAM-HT sample increased by 41.7% and 38.8% respectively. Moreover, the YS and UTS of the HAM-HT sample increased by 70 and 60 MPa compared with the LPBF-HT sample, respectively, while maintaining similar elongation. Figures 13(c) and (d) along with Supplementary Table S_{3} show the mechanical properties of Al alloys processed by LPBF, casting, and wrought methods reported in existing literature. The HAM-HT sample with YS of  $ (609 \pm 10) $ MPa, UTS of  $ (626 \pm 19) $ MPa, and  $ \varepsilon $ of  $ (7.5 \pm 2.4)\% $ demonstrated one of the best strength-ductility synergies among many LPBF-processed AlMgSc alloys $ ^{[7,55]} $. The HAM-HT AlMgSc alloy demonstrates an exceptional balance between strength and plasticity compared to AlMgSc alloy produced by other methods (wrought, cast, and laser directed energy deposition (LDED)) $ ^{[55-57]} $. Furthermore, the strength of the HAM-HT sample stands out among other series of Al alloys, including Al-Zn-Mg $ ^{[12]} $, Al-Cu $ ^{[58]} $, etc. Therefore, the HAM-HT AlMgSc alloy in this work substantiates the high strength together with good ductility. The strength improvement will be elaborated on in Section 4.3. The good plasticity of the HAM-HT sample comes from pore closure and grain recrystallization. (i) Pore closure. During the LPBF process, the temperature gradient within the melt pool induces stress concentration around the pore, promoting crack initiation and propagation under applied stress $ ^{[59]} $. After USP treatment, the internal porosities of the HAM and HAM-HT samples were reduced to below 0.05% with the lack of fusion and pore
Figure 12. TEM analysis of the nanoprecipitates in the HAM-HT sample: (a) and (b) columnar grains and dislocations in CGs zone, (c) and (d) FEGs morphology, Mg element distribution and dislocation in FEGs zone, (e) nanoprecipitates in CGs, (f) nanoprecipitates in FEGs, (g)  $ Al_{3}(Sc, Zr) $ nanoprecipitate in CGs (SAED pattern taken from yellow box), and (h) secondary  $ Al_{3}(Sc, Zr) $ nanoprecipitate in FEGs (FFT pattern from blue box).

defects being effectively suppressed (Figures 3(b) and (c)). (ii) Grain recrystallization. Recrystallization reduces the internal stress of the material and improves the elongation by eliminating the dislocations introduced by plastic deformation $ ^{[60]} $. The high dislocation density AlMgSc alloy was formed in USP-assisted LPBF (Figure 12(b)). Subsequent aging treatment induced recrystallization in the HAM-HT sample and led to good plasticity.

## 4. Discussion

## 4.1. Dislocation evolution

The dislocation evolution is the essence of metal plastic deformation, which plays a decisive role in the material’s deformation behaviour and strengthening mechanism $ ^{[34]} $. The geometrically necessary dislocations (GNDs) refer to dislocations that are generated due to the geometrical necessity of accommodating strain gradients in the material. These dislocations are closely linked to the material’s deformation behavior $ ^{[61]} $. The GNDs density of LPBF, LPBF-HT, and HAM-HT samples as  $ 3.14 \times 10^{14} $ m $ ^{-2} $,  $ 2.79 \times 10^{14} $ m $ ^{-2} $, and  $ 3.61 \times 10^{14} $ m $ ^{-2} $, respectively, as calculated from EBSD in Figure 14(a). The high dislocation density in the HAM-HT sample is attributed to the several strains resulting from interlayer USP. Figures 14(b) and (c) show the existence of a limited number of dislocation tangles and lines in LPBF and LPBF-HT samples. In contrast, the HAM-HT exhibits a higher dislocation density than the LPBF and LPBF-HT samples due to the USP induced severe plastic deformation $ ^{[62]} $.

To clarify the spatial distribution of dislocations in the HAM-HT sample, EBSD and TEM were used to characterize the dislocation density and structure along shock depths, as shown in Figure 15. Figure 15(a) shows the dislocation density from the surface USP layer to interior regions. The dislocation density in the surface region is higher than that in
Figure 13. Tensile properties of the LPBF, LPBF-HT, HAM, and HAM-HT AlMgSc alloy samples in this work and their comparisons with literature: (a) representative tensile stress-strain curves, (b) a summary of tensile properties, (c) yield strength or (d) ultimate tensile strength versus elongation compared with literature. All the data is summarized in Supplementary Table S_{3} with references.

Table 1. Tensile properties of the AlMgSc samples under LPBF, LPBF-HT, HAM, and HAM-HT conditions.

| Samples | YS/MPa | UTS/MPa | $ \varepsilon/\% $ |
| --- | --- | --- | --- |
| LPBF | 429  $ \pm $ 20 | 447  $ \pm $ 19 | 8.9  $ \pm $ 1.5 |
| LPBF-HT | 539  $ \pm $ 6 | 566  $ \pm $ 6 | 8.3  $ \pm $ 0.2 |
| HAM | 451  $ \pm $ 4 | 461  $ \pm $ 8 | 6.7  $ \pm $ 0.4 |
| HAM-HT | 609  $ \pm $ 10 | 626  $ \pm $ 19 | 7.5  $ \pm $ 2.4 |

the interior regions, forming hard and soft regions. To further determine the dislocation types and distribution evolution with shock depth, the dislocation at depths of 10  $ \mu $m, 100  $ \mu $m, 200  $ \mu $m, and 300  $ \mu $m are characterized by TEM (Figures 15(b)–(e)). Figure 15(b) shows that there is a substantial quantity of nanograin, dislocation cells in the near-surface region. At the depth of 100  $ \mu $m, the grain diameter is notably fine, accompanied by the formation of many dislocation entanglements and walls (Figure 15(c)). As the plastic deformation decreases, there is a noticeable reduction in dislocations, as shown in Figures 15(d) and (e). This indicates that the dislocation type changes accordingly as the impact depth increases, and the density of dislocation per unit area decreases. Plastic deformation in metal materials primarily manifests as dislocation movement within the grains under external load, the relationship between dislocation density and strain rate is as follows $ ^{[63]} $:

 $$ \rho_{m}=\frac{\dot{\varepsilon}}{\omega b\nu} $$
Figure 14. Dislocation evolution of LPBF, LPBF-HT, and HAM-HT samples: (a) dislocation density map of the LPBF, LPBF-HT, and HAM-HT samples by EBSD, (b) and (c) TEM images show dislocation distribution in CG and FEGs region with various manufacturing conditions.

where  $ \rho_{m} $ is the density of mobile dislocation,  $ \dot{\varepsilon} $ is the strain rate,  $ \omega $ is the proportional constant, b is the Burgers vector, and  $ \nu $ is the dislocation movement rate. The internal strain rate ( $ \dot{\varepsilon} $) of the part gradually decreases with the increase of shock depth, and dislocation density in the material gradually decreases, resulting in the gradient dislocation structure.

## 4.2. Microstructure evolution

## 4.2.1. Grain refinement mechanism analysis. The LPBF-manufactured AlMgSc alloy exhibits multimodal grains, with FEGs filling the boundaries of the melt pool and CGs mainly located in the center of the melt pool, as shown in Figure 6(a). The grain morphology and size are related to the nucleation and growth processes, which are governed by the temperature gradient (G) and solidification rate (R) $ ^{[64]} $. During the rapid solidification of the AlMgSc alloy, primary Al $ _{3} $Sc precipitates form before the Al phase, serving as effective nucleation sites for Al grains, which is the primary mechanism for forming equiaxed grain regions $ ^{[65]} $. Meanwhile, the R at the edge of the melt pool is low in the early stage of solidification $ ^{[20]} $, which provides sufficient time for Sc diffusion and agglomeration to form the primary Al $ _{3} $Sc precipitation (Figure 10(g)). As solidification proceeds, R increases rapidly and reaches a maximum value at the top of the melt pool $ ^{[20]} $, which restricts the agglomeration of Sc solute atoms and subsequent formation of the primary Al $ _{3} $(Sc, Zr) $ ^{[66,67]} $, resulting in the formation of the CGs at the central melt pool (Figure 6(a)). Therefore, the LPBF-manufactured AlMgSc samples exhibited an inhomogeneous grain structure.

USP treatment helps to homogenize the grain due to the flattening effect and dynamic recrystallization induced by high-frequency plastic deformation $ ^{[68,69]} $. (i) Flattening effect. The transient stress generated by the USP high-frequency impact exceeds the material’s yield strength, resulting in a strong plastic flow of the grains near the surface (Supplementary
Figure 15. Dislocation density evolution with shock depth: (a) dislocation density maps at the surface USP layer, center, bottom, and interlayer USP regions by EBSD analysis, (b)–(e) TEM analysis of dislocation distribution at varying depths: (b) 10  $ \mu $m, (c) 100  $ \mu $m, (d) 200  $ \mu $m, and (e) 300  $ \mu $m, respectively.

Figure S_{10}). The original coarse columnar grains were compressed in the stress direction, and gradually transformed into equiaxed grains (Figures 6(c) and (d)). (ii) Dynamic recrystallization. Under the high energy input provided by ultrasonic shock, dynamic recrystallization was induced inside the material to generate new fine equiaxed grains (Figure 7(b)). Dynamic recrystallization can occur through grain fragmentation and new grain formation $ ^{[69,70]} $. Hence, the CGs in the USP-treated sample are refined to achieve homogenous grain size. Besides, Figure 16 shows many nanograins in the impact layer of the HAM-HT sample.

The grain refinement mechanism induced by HAM-HT is shown in Figure 16(c). Stage I: the ultrasonic shock waves impact the material by generating numerous compressive stresses in the matrix (Figures 4 and 5(a)). This compression causes atoms to exert pressure on each other, resulting in the generation of numerous dislocation lines moving within the grain and forming dislocation tangles $ ^{[28]} $. Stage II: the dislocation movement is impeded by grain boundaries, and multi-nanoprecipitates (e.g. Al $ _{3} $(Sc, Zr) and Al $ _{6} $Mn), leading to the dislocation accumulation and entanglement (Figure 12(b)). With the mutual accumulation of ultrasonic impact strains, numerous movements of dislocation tangles interact with dislocation walls, forming dislocation cells (Figure 14(c)). Stage III: the dislocation density increases as a result of repeated interlayer USP. Dislocations surrounding the dislocation wall and cell in grain undergo annihilation and rearrangement, leading to the formation of LAGBs (Figure 14(b)) and changes from LAGBs to HAGBs, forming massive nanograins (Figure 16(b)). Thus, the HAM-HT method effectively homogenizes grains and refines the grain size near the USP layer.

## 4.2.2. Nanoprecipitates evolution analysis. Nanoprecipitates play an important role in performance improvement in AlMgSc alloy by pinning dislocation $ ^{[20,71]} $. Given that the Mn- and Mg-enriched nano-precipitates (Figures 12(e) and (f)) are quite limited in numbers, here only focus on the precipitation behaviour of the Al $ _{3} $(Sc, Zr). Figure 17 summarises the precipitation evolution of the LPBF, LPBF-HT, and HAM-HT samples. The LPBF sample is primarily composed of infrequent Al $ _{3} $(Sc, Zr) precipitates (Figure 17(a)). This is due to the repeated thermal history during the LPBF process that promotes the precipitation of a small amount of primary Al $ _{3} $(Sc, Zr) $ ^{[52]} $. Heat treatment increased the density and size of Al $ _{3} $(Sc, Zr) (Figures 11(f) and 17(b)) with a diameter reaching about 80 nm. The nucleation and coarsening of Al $ _{3} $(Sc, Zr) is associated with the diffusion of Sc and Zr elements during aging treatment $ ^{[72]} $.
Figure 16. Grain refinement mechanism analysis: (a) and (b) TEM images show grain morphology by LPBF and HAM-HT, and (c) schematic diagram of grain refinement mechanism in the HAM-HT sample.

Figure 17(c) shows the numerous  $ Al_{3}(Sc, Zr) $ nanoprecipitates that are evenly distributed in the HAM-HT sample, with density significantly higher than that in the LPBF and LPBF-HT samples. From LPBF to HAM-HT samples, the average diameter of secondary  $ Al_{3}(Sc, Zr) $ nanoparticles decreases, while the number of nanoparticles increases (Figures 17(d)–(f)).

The formation of ultrafine and high-density  $ Al_{3}(Sc, Zr) $ nanoprecipitations in HAM-HT sample after heat treatment could be explained as follows: the high cooling rate of LPBF together with subsequent USP treatment induced abundant dislocation entanglements and walls in material $ ^{[73]} $. The interlayer USP-induced strain reached the strength level of the  $ Al_{3}(Sc, Zr) $ precipitates, and dislocations could traverse through and break the precipitates to form numerous fine precipitates $ ^{[74]} $. Moreover, the high-density dislocation provides more nucleation sites for  $ Al_{3}(Sc, Zr) $ nucleation $ ^{[39]} $. The nucleation theory of the precipitate during aging can be expressed as $ ^{[72]} $:

 $$ \left.\frac{dN}{dt}\right|_{nucleation}=N_{0}Z^{\prime}\beta^{\prime}\exp\left(-\frac{\Delta G}{kT}\right)\exp\left(-\frac{\tau}{t}\right) $$ 

where  $ N_{0} $ is the number of potential nucleation sites proportional to dislocation density,  $ Z' $ is the Zeldovich factor,  $ \beta' $ is the atomic impingement rate,  $ \Delta G $ is the chemical driving force dependent on temperature, k is the Boltzmann constant, T is the temperature,  $ \tau $ is the incubation period, and t is the time. Thus, more nucleation sites provided by dense dislocations could increase  $ N_{0} $ and subsequently attain a higher precipitation density of  $ Al_{3}(Sc, Zr) $ particles during aging treatment at 300 ^\circC for 4 h. Hence, the HAM-HT sample exhibits a high-volume fraction of secondary  $ Al_{3}(Sc, Zr) $ nanoparticles (Figure 17(f)).
Figure 17. Nanoprecipitates evolution in AlMgSc alloy by LPBF, LPBF-HT, and HAM-HT: (a)–(c) multi-nanoprecipitate morphologies, (d)–(f) morphology of secondary Al₃(Sc, Zr). ((a) and (d) LPBF, (b) and (e) HT, and (c) and (f) HAM-HT samples.

## 4.2.3. Hierarchically multi-gradient structures analysis.

USP has been utilized to generate GNS materials with exceptional mechanical properties $ ^{[23]} $. The underlying gradient microstructures evolution mechanism of AlMgSc alloy after USP treatment remains largely unknown. Up to now, no systematic investigation has been conducted on the feasibility of the LPBF interlayer USP subsequent HT for tailoring hierarchical gradient microstructures of AlMgSc alloy. In this paper, owing to the restricted impact depth of USP, achieving the elimination of internal defects in AlMgSc components is challenging with a single gradient structure (only surface impact). Moreover, the mechanical properties enhancement of a single gradient structure is inferior to those of a multi-gradient structure achieved through dislocation, grain, and HDI strengthening $ ^{[75]} $. A multi-gradient microstructures preparation method for HAM-HT is proposed, which can achieve high density and address the trade-off between strength and ductility by tailoring hierarchical gradient microstructures, and the detailed microstructure is shown in Figure 18. Figure 18(a) shows grain morphologies of two-layer impact. It is obvious that the grain presents a multi-gradient structure, and grain distribution is a combination of nano/fine grains fine/coarse grains, and a single gradient is superimposed on each other to form multi-gradient structures. More interestingly, many CCGs in the center of the melt pool are mostly eliminated by repeated interlayer USP, and the grains are equiaxed. The columnar to equiaxed transition is caused by dislocation movement and grain refinement $ ^{[28]} $. Figure 18(b) shows the hierarchical multi-gradient microstructure of grains, dislocations, and precipitates. In each cycle, there are three different regions (i.e. regions I to III), which are characterized by different features of grain size, dislocation density, and nanoprecipitate distributions. Overall, multi-gradient structure features are crossing these three regions. The grain size increased progressively while the dislocation density reduced evidently from region I to region III. Meanwhile, the multiprecipitates (i.e. Al $ _{3} $(Sc, Zr), Mg $ _{2} $Si, etc) were uniformly distributed throughout the Al matrix. Therefore, the hierarchical multi-gradient structures customized by HAM-HT have both grain and dislocation multi-gradient structures.

## 4.3. Estimation of multi-strengthening mechanisms

As depicted in Figures 6, 8, 11, 17, and 18, the HAM-HT sample presents multi-modal grains, homogenous Mg distribution, high-density dislocation, multi-precipitate, and hierarchical multi-gradient structure. The main strengthening mechanisms of HAM-HT are grain boundary, solid-solution, dislocation, precipitation, and HDI strengthening. Relevant parameters for strength calculation are summarized in Table 2.

(i) Grain boundary strengthening ( $ \sigma_{GB} $). The grain refinement in the HAM-HT sample, particularly the ultrafine/nano grains in the interlayer USP impact layers (see Figure 18(a)), led to the grain boundary strengthening
Figure 18. The hierarchical gradient structure of the HAM-HT manufactured AlMgSc alloy: (a) grain morphologies maps at the top, center, and bottom regions, and (b) schematic illustration of the HAM-HT induced hierarchically gradient nanostructures.

 $ \sigma_{GB} $ as following $ ^{[12]} $:

 $$ \sigma_{GB}=k_{\gamma}\left(V_{f}d_{f}^{-\frac{1}{2}}+V_{c}d_{c}^{-\frac{1}{2}}\right) $$ 

Based on the relevant parameters in Table 2, the estimated contribution from  $ \sigma_{GB} $ of the HAM-HT sample is  $ \sim $116 MPa.

(ii) Solid-solution strengthening ( $ \sigma_{ss} $). Considering the minor content of Sc, Mn, and Zr in this alloy, the main solid solution strengthening in the HAM-HT sample could originate from Mg due to its uniform distribution without evident segregation in the material (Figure 8). The solution of Mg in AlMgSc alloys could enlarge the Al matrix lattice parameter and increase the coherency between the Al matrix with the precipitates $ ^{[48]} $. The  $ \sigma_{ss} $ contribution can be estimated $ ^{[71]} $:

 $$ \sigma_{ss}=\frac{3.1\varepsilon G\left(V_{f}c_{f}^{1/2}+V_{c}c_{c}^{1/2}\right)}{700} $$ 

where  $ c_{f} $ and  $ c_{c} $ are the concentration of the solute element in FG and CG. Detailed Mg element contents in FEGs and CGs are shown in Supplementary Table S_{2}. The calculated strength by  $ \sigma_{ss} $ of the HAM-HT sample is  $ \sim 95 $ MPa.

) Dislocation strengthening ( $ \sigma_{dis} $). Severe plastic deformation can increase tensile strength owing to high-density dislocations $ ^{[34]} $. In this study, the high-density dislocations induced dislocation strengthening ( $ \sigma_{dis} $) to material can be calculated as $ ^{[25]} $:

 $$ \sigma_{dis}=M\alpha Gb\sqrt{\rho} $$ 

where  $ \rho $ is the dislocation density, and  $ \rho = 3.61 \times 10^{14} $ m $ ^{-2} $ in the HAM-HT sample as calculated in Figure 14(a). Therefore, the calculated  $ \sigma_{dis} $ value is  $ \sim 73 $ MPa.

(iv) Precipitate strengthening ( $ \sigma_{p} $). The HAM-HT manufactured AlMgSc alloy exhibits multi-type precipitates. However, considering that the Al $ _{6} $Mn and Mg $ _{2} $Si particles are large and in low fractions, their strengthening effect on the material could be neglected. Hence, the statistical calculation is mainly performed on both primary and secondary Al $ _{3} $(Sc, Zr) particles. Both the primary and secondary Al $ _{3} $(Sc, Zr) particles with sizes exceeding 6 nm can endure the dislocation cutting. In this case, the contribution of the precipitates to the yield strength follows
Figure 19. HDI effect comparison between LPBF-HT and HAM-HT samples: (a) cyclic loading-unloading-reloading curves of the LPBF-HT and HAM-HT samples, (b) the enlarged view of typical hysteresis loops in the shadow area in (a) used to calculate the HDI strengthening.

Table 2. A summary of physical parameters and their values used for strengthening mechanism calculations.

| Symbol | Meaning | Value | Units | Ref. |
| --- | --- | --- | --- | --- |
| m | Constant | 0.85 |  | [52] |
| G | Shear modulus of Al | 25.4 | GPa | [20] |
| b | Burger’s vector | 0.248 | nm | [53] |
| $ \varepsilon $ | Experimental constant | 0.38 |  | [76] |
| $ k_{r} $ | Hall-Petch coefficient | 0.14 | MPa·m $ ^{-1/2} $ | [77] |
| M | Taylor factor | 3.06 |  | [77] |
| $ \alpha $ | Materials constant | 0.20 |  | [78] |
| $ \nu $ | Poisson’s ratio | 0.27 |  | [79] |
| $ V_{f} $ | Volume fraction of FEGs | 61.05 | % | This work |
| $ V_{c} $ | Volume fraction of CGs | 38.95 | % | This work |
| $ d_{f} $ | Average grain diameter of FEGs | 1.241 | $ \mu $m | This work |
| $ d_{c} $ | Average grain diameter of CGs | 1.956 | $ \mu $m | This work |

the Orowan mechanism $ ^{[45]} $:

 $$ \sigma_{p}=\frac{0.4MGb}{\pi L}\frac{\ln\frac{r\pi}{2b}}{\sqrt{1-\nu}} $$ 

where  $ L = r \sqrt{\left(\frac{2\pi}{3f} - \frac{\pi}{2}\right)} $, r is the average particle radius, and f is the volume fraction of nanoparticles. Here, the  $ f_m $ of the primary  $ Al_3(Sc, Zr) $ is estimated as  $ \sim 2.84\% $ with a mean radius  $ r_m $ of  $ \sim 43.8 $ nm, and the  $ f_s $ of the secondary  $ Al_3(Sc, Zr) $ is estimated as  $ \sim 1.02\% $ with a mean radius  $ r_s $ of  $ \sim 3.2 $ nm. Therefore, the strengthening from the primary and secondary  $ Al_3(Sc, Zr) $ particles is about 24 and 217 MPa, respectively. Hence, the total strength increment by  $ \sigma_{Oro} $ in the HAM-HT sample is  $ \sim 241 $ MPa.

(v) HDI strengthening ( $ \sigma_{HDI} $). Hierarchically gradient structure in the material can enhance mechanical properties due to the hetero-deformation induced (HDI) strengthening effect caused by the interaction of back stress in soft regions (e.g. CGs region) and forward stress in the hard zones (e.g. UFEGs region) during deformation $ ^{[80]} $. Back stress is generated in soft domains to counteract the applied stress, making these domains appear stronger. To quantify the HDI strengthening ( $ \sigma_{HDI} $), cyclic loading-unloading tensile tests are performed, and the obtained typical true stress-strain curves of LPBF-HT and HAM-HT samples are shown in Figure 19(a), and the  $ \sigma_{HDI} $ is calculated according to the equation (9) $ ^{[81]} $:

 $$ \sigma_{HDI}=\frac{\sigma_{r}+\sigma_{u}}{2} $$ 

where  $ \sigma_{u} $ is the unloading stress,  $ \sigma_{r} $ is the reloading stress. The LPBF-HT sample exhibits smaller hysteresis loops compared with the HAM-HT sample overall (Figure 19(b)), indicating a limited Bauschinger effect and HDI strengthening effect $ ^{[81]} $. Considering that there are no gradient structures in the LPBF-HT sample, the difference of  $ \sigma_{HDI} $ value calculated in HAM-HT and LPBF-HT samples could be originated from the gradient microstructures. Thus, the additional strengthening effect from USP-induced heterogeneous microstructures is calculated as  $ \sim99 $ MPa.

Consequently, the theoretical yield strength of the HAM-HT sample is calculated as 624 MPa, which is highly
Figure 20. Comparison of the calculated yield stress with experimentally obtained yield stress.

consistent with the experimental results (609 MPa). The precipitation strengthening from  $ \mathrm{Al}_{3}(\mathrm{Sc}, \mathrm{Zr}) $ particles is the main strengthening segment in the HAM-HT sample (Figure 20). Besides, the HDI strengthening induced by hierarchical multi-gradient structures contributed to achieving a yield strength of over 600 MPa.

## 5. Conclusion

Our research proposed a novel hybrid additive manufacturing method by combining LPBF with interlayer ultrasonic shot peening to achieve a hierarchical gradient structure with multi-nanoprecipitates in AlMgSc alloy for superior strength. The main conclusions are:

(1) The HAM method can improve density, eliminate residual tensile stress, and refine grains. The effective depth of CRS reached  $ \sim $700  $ \mu $m by USP, and the material’s porosity decreased to 0.049% after HAM treatment. Additionally, the HAM method attained refined grain in the FEGs region and formed completely equiaxed grains. Besides, many nanograins and FEGs formed in the USP layer, which is caused by dense dislocation cells and walls induced recrystallization due to dislocation movements.

(2) The HAM followed by HT tailored the hierarchically multi-gradient structures, inhibited Mg element intragranular segregation, and promoted the multi-nanoprecipitates precipitation. The grain and dislocation present a multi-gradient structure. The LPBF-manufactured AlMgSc alloy exhibits an Mg network structure and obvious Mg element intragranular segregation. The HAM-HT significantly eliminates the Mg network structure and improves the Mg solution in the matrix, promoting the subsequent precipitation of multi-nanoprecipitates (e.g. Al₃(Sc, Zr) and Al₆Mn) during aging treatment.

(3) The HAM-HT AlMgSc alloy demonstrated ultrahigh strength and good ductility. The HAM-HT achieved YS of 609 MPa together with an elongation of 7.5%, which demonstrated that HAM can improve the strength significantly without evident loss of ductility. The achieved mechanical properties of HAM-processed AlMgSc alloy are one of the highest strength-ductility synergy compared with many AlMgSc alloys and other series of Al alloys produced by LPBF and wrought. The strength enhancement comes from the synergy of multi-strengthening mechanisms, in which precipitation is one of the main strengthening mechanisms and HDI strengthening is a unique strengthening mechanism originating from the heterogeneous microstructures.

## Acknowledgments

This work was supported by the National Natural Science Foundation of China (Grant No: 52475484), National Key R&D Program of China (Grant No: 2022YFB4600800), and the 2022 MTC Young Individual Research Grants (Grant No: M22K3c0097) under the Singapore RIE 2025 Plan.

## Conflict of interest

The authors declare that they have no known competing interests.

## ORCID iDs

Wenjie Liu  $ \textcircled{iD} $ https://orcid.org/0009-0007-2078-9263

Shengnan Shen  $ \textcircled{iD} $ https://orcid.org/0000-0002-3964-8475

Hui Li  $ \textcircled{iD} $ https://orcid.org/0000-0002-4404-8845

Chaolin Tan  $ \textcircled{iD} $ https://orcid.org/0000-0003-2029-4600

## References

[1] Aboulkhair N T, Simonelli M, Parry L, Ashcroft I, Tuck C and Hague R. 2019. 3D printing of aluminium alloys: additive manufacturing of aluminium alloys using selective laser melting. Prog. Mater. Sci. 106, 100578.

[2] Zhao H, Chakraborty P, Ponge D, Hickel T, Sun B H, Wu C H, Gault B and Raabe D. 2022. Hydrogen trapping and embrittlement in high-strength al alloys. Nature 602, 437–441.

[3] Liu T S, Chen P, Qiu F, Yang H Y, Jin N T Y, Chew Y, Wang D, Li R D, Jiang Q C and Tan C L. 2024. Review on laser directed energy deposited aluminum alloys. Int. J. Extrem. Manuf. 6, 022004.

[4] Zhang W and Xu J. 2022. Advanced lightweight materials for automobiles: a review. Mater. Des. 221, 110994.

[5] Raabe D et al. 2022. Making sustainable aluminum by recycling scrap: the science of “dirty” alloys. Prog. Mater. Sci. 128, 100947.

[6] Liu Z B, Sun J N, Yan Z G, Lin Y J, Liu M P, Roven H J and Dahle A K. 2021. Enhanced ductility and strength in a cast Al-Mg alloy with high Mg content. Mater. Sci. Eng. A 806, 140806.

[7] Wang M B, Li R D, Yuan T C, Chen C, Zhou L B, Chen H, Zhang M and Xie S Y. 2019. Microstructures and mechanical property of AlMgScZrMn—a comparison between selective laser melting, spark plasma sintering and cast. Mater. Sci. Eng. A 756, 354–364.

[8] Gao S B et al. 2023. Additive manufacturing of alloys with programmable microstructure and properties. Nat. Commun. 14, 6752.

[9] Tan C L, Liu Y C, Weng F, Ng F L, Su J L, Xu Z K, Ngai X D and Chew Y. 2022. Additive manufacturing of voxelized heterostructured materials with hierarchical phases. Addit. Manuf. 54, 102775.

[10] Li R D, Wang M B, Li Z M, Cao P, Yuan T C and Zhu H B. 2020. Developing a high-strength Al-Mg-Si-Sc-Zr alloy for selective laser melting: crack-inhibiting and multiple strengthening mechanisms. Acta Mater. 193, 83–98.

[11] Zhang H, Zhu H H, Qi T, Hu Z H and Zeng X Y. 2016. Selective laser melting of high strength Al-Cu-Mg alloys: processing, microstructure and mechanical properties. Mater. Sci. Eng. A 656, 47–54.

[12] Zhu Z G, Ng F L, Seet H L, Lu W J, Liebscher C H, Rao Z Y, Raabe D and Mui Ling Nai S. 2022. Superior mechanical properties of a selective-laser-melted AlZnMgCuScZr alloy enabled by a tunable hierarchical microstructure and dual-nanoprecipitation. Mater. Today 52, 90–101.

[13] Spierings A B, Dawson K, Kern K, Palm F and Wegener K. 2017. SLM-processed Sc- and Zr- modified Al-Mg alloy: mechanical properties and microstructural effects of heat treatment. Mater. Sci. Eng. A 701, 264–273.

[14] Cabrera Correa L, González Rovira L, Ojeda López A, de Dios López Castro J and Botana F J. 2023. Localized and stress corrosion cracking of sensitized Al-Mg-Sc-Zr alloy manufactured by laser powder bed fusion. Corros. Sci. 218, 111166.

[15] Zhu Z G, Hu Z H, Seet H L, Liu T T, Liao W H, Ramamurty U and Ling Nai S M. 2023. Recent progress on the additive manufacturing of aluminum alloys and aluminum matrix composites: microstructure, properties, and applications. Int. J. Mach. Tools Manuf. 190, 104047.

[16] Bayoumy D, Kan W H, Wu X H, Zhu Y M and Huang A J. 2023. The latest development of Sc-strengthened aluminum alloys by laser powder bed fusion. J. Mater. Sci. Technol. 149, 1–17.

[17] Yuan T, Yu Z L, Chen S J, Xu M and Jiang X Q. 2020. Loss of elemental Mg during wire+arc additive manufacturing of Al-Mg alloy and its effect on mechanical properties. J. Manuf. Process. 49, 456–462.

[18] Huang Y, Hua X M, Shen C, Li F, Ding Y H and Mou G. 2021. Metal evaporation flux across knudsen layer in laser keyhole welding of Al-Mg alloys with pressure balance condition method. Appl. Surf. Sci. 536, 147838.

[19] Li X, Liu Y Z, Tan C L and Zou Y M. 2023. Laser powder bed fusion of a novel crack-free Al-Mg-Sc-Zr alloy: printability, microstructure characterization and mechanical performance. Opt. Laser Technol. 162, 109281.

[20] Zhang H, Dai D H, Yuan L H, Liu H and Gu D D. 2023. Temperature gradient induced tough-brittle transition behavior of a high-strength Al-4.2Mg-0.4Sc-0.2Zr alloy fabricated by laser powder bed fusion additive manufacturing. Addit. Manuf. 73, 103655.

[21] Kuo C N and Peng P C. 2023. The strengthening mechanism synergy of heat-treated 3D printed Al-Sc alloy. Virtual Phys. Prototyp. 18, e2166539.

[22] Jia Q B, Rometsch P, Kürnsteiner P, Chao Q, Huang A J, Weyland M, Bourgeois L and Wu X H. 2019. Selective laser melting of a high strength Al-Mn-Sc alloy: alloy design and strengthening mechanisms. Acta Mater. 171, 108–118.

[23] Ji W M, Zhou R H, Vivegananthan P, See Wu M, Gao H J and Zhou K. 2023. Recent progress in gradient-structured metals and alloys. Prog. Mater. Sci. 140, 101194.

[24] Chen X Y, Lu T W, Yao N, Chen H Y, Sun B H, Xie Y, Chen Y F, Wan B B, Zhang X C and Tu S T. 2023. Enhanced fatigue resistance and fatigue-induced substructures in an additively manufactured CoCrNi medium-entropy alloy treated by ultrasonic surface rolling process. Int. J. Plast. 169, 103721.

[25] Zhou J T, Zhou X, Li H, Hu J W, Han X and Liu S. 2022. In-situ laser shock peening for improved surface quality and mechanical properties of laser-directed energy-deposited AlSi10Mg alloy. Addit. Manuf. 60, 103177.

[26] Tan C L et al. 2023. Review on field assisted metal additive manufacturing. Int. J. Mach. Tools Manuf. 189, 104032.

[27] Liu W J, Li H, Yin Q X and Zhou X. 2025. Promoting densification and strengthening effect of ultrasonic impact treatment on haynes 230 alloy manufactured by laser powder bed fusion. J. Mater. Sci. Technol. 216, 226–240.

[28] Deng W W, Wang C Y, Lu H F, Meng X K, Wang Z, Lv J M, Luo K Y and Lu J Z. 2023. Progressive developments, challenges and future trends in laser shock peening of metallic materials and alloys: a comprehensive review. Int. J. Mach. Tools Manuf. 191, 104061.

[29] Li X and Liu Y Z. 2023. Microstructure characterization and mechanical performance of laser powder bed fusion processed AlMgScZr alloy: effect of heat treatment. Mater. Sci. Eng. A 862, 144501.

[30] Deillon L, Jensch F, Palm F and Bambach M. 2022. A new high strength Al-Mg-Sc alloy for laser powder bed fusion with calcium addition to effectively prevent magnesium evaporation. J. Mater. Process. Technol. 300, 117416.

[31] Zhao D S, Long D F, Niu T R, Zhang T F, Hu X and Liu Y J. 2022. Effect of Mg loss and microstructure on anisotropy of 5356 wire arc additive manufacturing. J. Mater. Eng. Perform. 31, 8473–8482.

[32] Zhao J H, Luo L S, Zheng X N, Zhang T, Luo H, Li Z, Liu T, Wang L and Su Y Q. 2024. The effect of Mn content on a novel Al-Mg-Si-Sc-Zr alloy produced by laser powder bed fusion: the microstructure and mechanical behavior. J. Mater. Res. Technol. 28, 989–1001.

[33] Ponnusamy P, Rahman Rashid R A, Masood S H, Ruan D and Palanisamy S. 2020. Mechanical properties of SLM-printed aluminium alloys: a review. Materials 13, 4301.

[34] Li X Z, Fang X W, Zhang M G, Zhang H K, Duan Y S and Huang K. 2023. Gradient microstructure and prominent performance of wire-arc directed energy deposited magnesium alloy via laser shock peening. Int. J. Mach. Tools Manuf. 188, 104029.

[35] Kalentics N, Boillat E, Peyre P, Gorny C, Kenel C, Leinenbach C, Jhabvala J and Logé R E. 2017. 3D laser shock peening—a new method for the 3D control of residual stresses in selective laser melting. Mater. Des. 130, 350–356.

[36] Lim C H, Li H, Krishnan M, Chen K W and Li J R. 2023. Novel method of residual stress reduction for AlSi10Mg manufactured using selective laser melting without compromise of mechanical strength. Virtual Phys. Prototyp. 18, e2131583.

[37] Zhu L H, Guan Y J, Wang Y J, Xie Z D, Lin J and Zhai J Q. 2017. Influence of process parameters of ultrasonic shot peening on surface roughness and hydrophilicity of pure titanium. Surf. Coat. Technol. 317, 38–53.

[38] Meng X K, Zhao Y M, Zhou J Z, Huang S, Leng X M and Li L. 2022. Surface properties of 2024 aluminum alloy strengthened by laser ultrasonic composite shock peening. Chin. J. Lasers 49, 1602003.

[39] Pan X L, Zhou L C, Wang C X, Yu K, Zhu Y Q, Yi M, Wang L F, Wen S F, He W F and Liang X Q. 2023. Microstructure and residual stress modulation of 7075 aluminum alloy for improving fatigue performance by laser shock peening. Int. J. Mach. Tools Manuf. 184, 103979.

[40] Tekumalla S, Seita M and Zaefferer S. 2024. Delineating dislocation structures and residual stresses in additively manufactured alloys. Acta Mater. 262, 119413.

[41] Xiao Y M, Yang Y Q, Wang D, Liu L Q, Liu Z B, Wu S B, Zhou H X, Liu Z X and Song C H. 2023. In-situ synthesis of high strength and toughness TiN/Ti6Al4V sandwich

composites by laser powder bed fusion under a nitrogen-containing atmosphere. Composites B 253, 110534.

[42] Bi J et al. 2022. Microstructure, tensile properties and heat-resistant properties of selective laser melted AlMgScZr alloy under long-term aging treatment. Mater. Sci. Eng. A 833, 142527.

[43] Chen X J, Xie X C, Zhang Y P, Wang H Y and Liang Z W. 2023. Tungsten carbide coating prepared by ultrasonic shot peening to improve the wear properties of magnesium alloys. J. Mater. Res. Technol. 26, 2451–2464.

[44] Liu H, Gu D D, Shi K Y, Zhang H, Li L X, Zhang Y J, Li J Y and Qi J F. 2024. High-strength aluminum alloy processed by micro laser powder bed fusion ( $ \mu $-LPBF): coordination of laser formability, microstructure evolution, and mechanical properties. J. Mater. Process. Technol. 332, 118580.

[45] Bayoumy D et al. 2022. Origin of non-uniform plasticity in a high-strength Al-Mn-Sc based alloy produced by laser powder bed fusion. J. Mater. Sci. Technol. 103, 121–133.

[46] Chen Y T, Wang K and Ren Z. 2024. Interaction between phase transformation and static recrystallization during annealing of rolled TC18 titanium alloy. J. Mater. Sci. Technol. 202, 1–15.

[47] Chen W, Xu L Y, Zhao L, Han Y D, Wang X, Hu C C and Jing H Y. 2022. Application of hybrid additive manufacturing technology for performance improvement of martensitic stainless steel. Addit. Manuf. 51, 102648.

[48] Liu Z Z, Zhou Q H, Liang X K, Wang X B, Li G C, Vanmeensel K and Xie J X. 2024. Alloy design for laser powder bed fusion additive manufacturing: a critical review. Int. J. Extrem. Manuf. 6, 022002.

[49] Bi J, Lei Z L, Chen Y B, Chen X, Tian Z, Lu N N, Qin X K and Liang J W. 2021. Microstructure, tensile properties and thermal stability of AlMgSiScZr alloy printed by laser powder bed fusion. J. Mater. Sci. Technol. 69, 200–211.

[50] Li Q G, Li G C, Lin X, Zhu D M, Jiang J H, Shi S Q, Liu F G, Huang W D and Vanmeensel K. 2022. Development of a high strength Zr/Sc/Hf-modified Al-Mn-Mg alloy using laser powder bed fusion: design of a heterogeneous microstructure incorporating synergistic multiple strengthening mechanisms. Addit. Manuf. 57, 102967.

[51] Bayoumy D, Boll T, Schliephake D, Wu X H, Zhu Y M and Huang A J. 2022. On the complex intermetallics in an Al-Mn-Sc based alloy produced by laser powder bed fusion. J. Alloys Compd. 901, 163571.

[52] Zhang H, Zhang L C, Liu H Y, Niu X D, Lam M C, Zhang W Z, Jin X J, Chu F Z, Wu X H and Cao S. 2023. Strong and ductile Al-Mn-Mg-Sc-Zr alloy achieved in fabrication-rate enhanced laser powder bed fusion. Virtual Phys. Prototyp. 18, e2250769.

[53] Sun J, Gao L, Liu Q, Wang P, Qu X H and Zhang B C. 2023. Novel isotropic mechanical properties of laser powder-bed fusion Sc/Zr modified alloy. Mater. Sci. Eng. A 872, 145003.

[54] He P D, Webster R F, Yakubov V, Kong H, Yang Q, Huang S K, Ferry M, Kruzic J J and Li X P. 2021. Fatigue and dynamic aging behavior of a high strength Al-5024 alloy fabricated by laser powder bed fusion additive manufacturing. Acta Mater. 220, 117312.

[55] Hua Q, Wang W J, Li R D, Zhu H B, Lin Z H, Xu R, Yuan T C and Liu K. 2022. Microstructures and mechanical properties of Al-Mg-Sc-Zr alloy additively manufactured by laser direct energy deposition. Chin. J. Mech. Eng.: Addit. Manuf. Front. 1, 100057.

[56] Baek M S, Shah A W, Kim Y K, Kim S K, Kim B H and Lee K A. 2023. Microstructures, tensile properties, and strengthening mechanisms of novel Al-Mg alloys with high Mg content. J. Alloys Compd. 950, 169866.

[57] Li G et al. 2024. Additively manufactured fine-grained ultrahigh-strength bulk aluminum alloys with nanostructured strengthening defects. Mater. Today 76, 40–51.

[58] Chen Y, Xiao C W, Zhu S, Li Z W, Yang W X, Zhao F, Yu S F and Shi Y S. 2022. Microstructure characterization and mechanical properties of crack-free Al-Cu-Mg-Y alloy fabricated by laser powder bed fusion. Addit. Manuf. 58, 103006.

[59] Lu J W, Zheng H, Ji X C, Guan Y, Wang Z L, Cheng J and Zhang W. 2024. Crack characteristics analysis and mechanisms in GH3536 alloy manufactured by laser powder bed fusion. Eng. Fail. Anal. 162, 108382.

[60] Song Y L, Wu Y H, Lu J, Mei M L, Xie L C and Hao C C. 2023. Promoting dynamic recrystallization of Al-Zn-Mg-Cu alloy via electroshock treatment. Metals 13, 944.

[61] Cui L Q, Yu C H, Jiang S, Sun X Y, Peng R L, Lundgren J E and Moverare J. 2022. A new approach for determining GND and SSD densities based on indentation size effect: an application to additive-manufactured Hastelloy X. J. Mater. Sci. Technol. 96, 295–307.

[62] Li Y J, Liu X T, Wang F, Zhou W F and Ren X D. 2024. Influence of ultrasonic shot peening on the surface acid etching behavior of pure titanium. Mater. Chem. Phys. 313, 128720.

[63] Kun Q, Yang L M and Hu S S. 2009. Mechanism of strain rate effect based on dislocation theory. Chin. Phys. Lett. 26, 036103.

[64] Bermingham M J, StJohn D H, Krynen J, Tedman Jones S and Dargusch M S. 2019. Promoting the columnar to equiaxed transition and grain refinement of titanium alloys during additive manufacturing. Acta Mater. 168, 261–274.

[65] Martin J H et al. 2020. Grain refinement mechanisms in additively manufactured nano-functionalized aluminum. Acta Mater. 200, 1022–1037.

[66] Rometsch P A, Zhu Y M, Wu X H and Huang A J. 2022. Review of high-strength aluminium alloys for additive manufacturing by laser powder bed fusion. Mater. Des. 219, 110779.

[67] Tan Q Y and Zhang M X. 2024. Recent advances in inoculation treatment for powder-based additive manufacturing of aluminium alloys. Mater. Sci. Eng. R 158, 100773.

[68] Xie X C, Ye Y, Zou Z X, Mo Y D, Liang Z W and Tang G B. 2024. Improving the corrosion resistance of aluminum alloy welds through powder-ball combined ultrasonic shot peening. J. Mater. Process. Technol. 332, 118557.

[69] Wang Y C and Shi J. 2020. Recrystallization behavior and tensile properties of laser metal deposited Inconel 718 upon in-situ ultrasonic impact peening and heat treatment. Mater. Sci. Eng. A 786, 139434.

[70] Yin F, Zhang X D, Chen F, Hu S, Ming K S, Zhao J H, Xie L C, Liu Y X, Hua L and Wang J. 2023. Understanding the microstructure refinement and mechanical strengthening of dual-phase high entropy alloy during ultrasonic shot peening. Mater. Des. 227, 111771.

[71] Ekubaru Y, Gokcekaya O, Ishimoto T, Sato K, Manabe K, Wang P and Nakano T. 2022. Excellent strength-ductility balance of Sc-Zr-modified Al-Mg alloy by tuning bimodal microstructure via hatch spacing in laser powder bed fusion. Mater. Des. 221, 110976.

[72] Russell K C. 1980. Nucleation in solids: the induction and steady state effects. Adv. Colloid Interface Sci. 13, 205–318.

[73] Kim R E, Karthik G M, Amanov A, Heo Y U, Jeong S G, Gu G H, Park H, Kim E S, Lee D W and Kim H S. 2023. Superior gradient heterostructured alloys fabricated by laser powder bed fusion via annealing and ultrasonic nanocrystal surface modification. Scr. Mater. 230, 115422.

[74] Wang C Y, Luo K Y, Wang J and Lu J Z. 2022. Carbide-facilitated nanocrystallization of martensitic laths and

carbide deformation in AISI 420 stainless steel during laser shock peening. Int. J. Plast. 150, 103191.

[75] Qin S, Yang M X, Jiang P, Wang J, Wu X L, Zhou H and Yuan F P. 2022. Designing structures with combined gradients of grain size and precipitation in high entropy alloys for simultaneous improvement of strength and ductility. Acta Mater. 230, 117847.

[76] Krug M E, Mao Z G, Seidman D N and Dunand D C. 2014. Comparison between dislocation dynamics model predictions and experiments in precipitation-strengthened Al–Li–Sc alloys. Acta Mater. 79, 382–395.

[77] Liu D H et al. 2023. Superior strength of laser-arc hybrid additive manufactured Al-Zn-Mg-Cu alloy enabled by a tunable microstructure. Addit. Manuf. 68, 103526.

[78] Xu H, Ren W J, Ma C Y, Xu L Y, Han Y D, Zhao L and Hao K D. 2023. Laser-directed energy deposition of  $ ZrH_{2} $ particles reinforced Al_{7075} alloy: cracks elimination and strength enhancement. Addit. Manuf. 78, 103877.

[79] Wang G D, Zhou Y R, Cao J Y and Tian Y. 2024. Tensile properties and fracture behavior of Al-8Si alloy sheets with different Mg under natural aging. J. Mater. Sci. 59, 7368–7386.

[80] Wu D et al. 2023. Heterostructures enhance simultaneously strength and ductility of a commercial titanium alloy. Acta Mater. 257, 119182.

[81] Guo S K, Ma Z L, Xia G H, Li X Y, Xu Z Q, Li W Z, Jin X Y and Cheng X W. 2024. Pursuing ultrastrong and ductile medium entropy alloys via architecting nanoprecipitates-enhanced hierarchical heterostructure. Acta Mater. 263, 119492.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

International Journal of Extreme Manufacturing

- Performance-control-orientated hybrid metal additive manufacturing technologies: state of the art, challenges, and future trends
Jiming Lv, Yuchen Liang, Xiang Xu et al.

- Review on laser directed energy deposited aluminum alloys
Tian-Shu Liu, Peng Chen, Feng Qiu et al.

- Recent progress in bio-inspired macrostructure array materials with special wettability—from surface engineering to functional applications
Zhongxu Lian, Jianhui Zhou, Wanfei Ren et al.

This content was downloaded from IP address 128.199.174.229 on 18/08/2025 at 04:17

OPEN ACCESS
IMMT | IOP Publishing

https://doi.org/10.1088/2631-7990/adbb95

$ ^{5} $ The Institute of Technological Sciences, Wuhan University, Wuhan 430072, People’s Republic of China  
 $ ^{6} $ Nanyang Technological University, 50 Nanyang Avenue, Singapore 639798, Singapore

Accepted for publication 27 February 2025  
Published 3 April 2025

$ ^{*} $ Author to whom any correspondence should be addressed.
 $ ^{**} $ Author to whom any correspondence should be addressed secondly.

Original content from this work may be used under the terms of the Creative Commons Attribution 4.0 licence. Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.

© 2025 The Author(s). Published by IOP Publishing Ltd on behalf of the IMMT

Mechanical field assisted additive manufacturing...
Liu W et al.

## Supplementary Material

Mechanical field assisted additive manufacturing...

Liu W et al.

where  $ c_{f} $ and  $ c_{c} $ are the concentration of the solute element in FG and CG. Detailed Mg element contents in FEGs and CGs are shown in Supplementary Table S_{2}. The calculated strength by  $ \sigma_{ss} $ of the HAM-HT sample is  $ \sim 95 $ MPa.

Wenjie Liu  $ \textcircled{iD} $ https://orcid.org/0009-0007-2078-9263
Shengnan Shen  $ \textcircled{iD} $ https://orcid.org/0000-0002-3964-8475
Hui Li  $ \textcircled{iD} $ https://orcid.org/0000-0002-4404-8845
Chaolin Tan  $ \textcircled{iD} $ https://orcid.org/0000-0003-2029-4600

[78] Xu H, Ren W J, Ma C Y, Xu L Y, Han Y D, Zhao L and Hao K D. 2023. Laser-directed energy deposition of  $ ZrH_{2} $ particles reinforced Al_{7075} alloy: cracks elimination and strength enhancement. Addit. Manuf. 78, 103877.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

Received 8 October 2024, revised 29 December 2024  
Accepted for publication 27 February 2025  
Published 3 April 2025

Supplementary material for this article is available online

where  $ c_{f} $ and  $ c_{c} $ are the concentration of the solute element in FG and CG. Detailed Mg element contents in FEGs and CGs are shown in Supplementary Table S2. The calculated strength by  $ \sigma_{ss} $ of the HAM-HT sample is  $ \sim 95 $ MPa.

[78] Xu H, Ren W J, Ma C Y, Xu L Y, Han Y D, Zhao L and Hao K D. 2023. Laser-directed energy deposition of  $ ZrH_{2} $ particles reinforced Al7075 alloy: cracks elimination and strength enhancement. Addit. Manuf. 78, 103877.