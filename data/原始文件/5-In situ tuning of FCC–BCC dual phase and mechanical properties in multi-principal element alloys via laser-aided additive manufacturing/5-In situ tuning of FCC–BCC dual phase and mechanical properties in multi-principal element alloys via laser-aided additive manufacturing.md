DOI: 10.1007/s12598-025-03420-w

ORIGINAL ARTICLE

# In situ tuning of FCC–BCC dual phase and mechanical properties in multi-principal element alloys via laser-aided additive manufacturing

Lijia Chen, Sihao Zou, Shang Sui, Fei Weng, Shangxiong Huangfu, Lichao Cao, Hao Zhang, Sergey-Vasilievich Gaponenko, Tao Yang, Jiang Ju, Lidong Zhao, Wenjun Lu*, Guijun Bi*

Received: 3 March 2025 / Revised: 25 April 2025 / Accepted: 27 April 2025

© Youke Publishing Co., Ltd. 2025

## Abstract

 A novel approach for fabricating multi-principal element alloys with adjustable phase configurations and mechanical properties was developed using laser-aided additive manufacturing (LAAM), combining FCC-structured (face-centered cubic) CoCrNi and BCC-structured (body-centered cubic) CoCrNiAl0.6TiFe feedstocks. During fabrication, CoCrNi powders and CoCrNiAl0.6TiFe powders were simultaneously fed into the melt pool at individually adjustable rates, allowing for controlled phase transitions. The resulting phase evolution demonstrated a gradual transition from a single FCC structure CoCrNi(Al_{0}.6TiFe)x (x = 0, 0.1, 0.2, 0.3) to a dual FCC-

B_{2} structure CoCrNi(Al_{0}.6TiFe)x (x = 0.4, 0.5) as the proportion of BCC-structured powders increased. The B_{2} phase, enriched in Ti and Al due to their larger atomic radii and negative segregation enthalpy, precipitated around the FCC matrix, with volume fractions of 0.5% and 5.7% for CoCrNi(Al_{0}.6TiFe)0.4 and CoCrNi(Al_{0}.6TiFe)0.5, respectively. This phase transition resulted in significant mechanical enhancements. Yield and ultimate tensile strengths increased from 486.0 and 781.2 MPa (CoCrNi) to 887.2 and 1165.2 MPa (CoCrNi(Al_{0}.6TiFe)0.5). Dislocation-mediated hardening prevailed in single-phase FCC alloys, exhibiting a characteristic dislocation density of  $ 2.5 \times 10^{15} $ m $ ^{-2} $ for CoCrNi(Al_{0}.6TiFe)0.3 alloy. Once the B_{2} phase precipitated, precipitation strengthening became dominant, as observed in transmission electron microscopy (TEM), where dislocations accumulated around B_{2} precipitates. This study presents an innovative alloy fabrication strategy that enables precise tuning of FCC–BCC dual-phase structures, facilitating the direct fabrication of

## F. Weng

School of Materials Science and Engineering, Shandong University, Jinan 250061, China

## S. Huangfu

Laboratory for High Performance Ceramics, Empa. Swiss Federal Laboratories for Materials Science and Technology, Überlandstrasse 129, Dübendorf CH - 8600, Switzerland

## S.-V. Gaponenko

State Scientific Institution, B.I.Stepanov Institute of Physics of the National Academy of Sciences of Belarus, Minsk 220072, Belarus

## T. Yang, J. Ju

Department of Materials Science and Engineering, City University of Hong Kong, Hong Kong 999077, China

components with spatially customized properties. These findings provide valuable insights for developing multi-principal element alloys with heterogeneous microstructures for advanced engineering applications.

Keywords Laser-aided additive manufacturing; Tunable phases; Phase formation; Strengthening mechanisms; Multi-principal element alloys

## 1. Introduction

Traditional structural materials, often composed of a single phase, frequently struggle to meet the evolving demands of high-performance and lightweight applications in industries such as aerospace [1, 2], bioengineering [3, 4], automotive [5], and other fields [6, 7]. As a result, the integration of compositional and functional gradation in materials has become a key focus in modern manufacturing [8, 9]. To address these challenges, dual-phase materials have been extensively investigated. For example, FCC/BCC CoNiFeAlxCu1−x multilayers have demonstrated superior Young’s modulus compared to their single-phase counterparts. In particular, when the layer is 2 nm thickness, the high-density FCC/BCC interfaces interact with stacking faults, driving crystallographic reconfiguration from BCC to FCC. This transformation facilitates deformation twins formation, ultimately leading to the phase interface converting into a perfect twin boundary, enhancing mechanical performance [10]. However, due to limited fabricating control over composition and spatial structure, conventional fabrication techniques such as casting or forging struggle to produce phase-tunable materials with tailored microstructures.

Additive manufacturing (AM) has become a transformative method for developing high-performance alloys, including magnesium alloys [11], NiTi shape memory alloy [12–16], copper matrix composites [17], aluminum matrix composites [18], and titanium alloys [19–21]. AM’s design flexibility and ability to fabricate complex structures in a single process have significantly enhanced the feasibility of producing phase-tunable materials compared to traditional methods [22]. Among AM techniques, laser powder bed fusion (LPBF), a primary technology in AM has been widely adopted; however, its ability to dynamically regulate composition in real-time is constrained by the difficulty of altering powder feedstocks [23]. While various powder-spreading systems have been developed, their high costs and low efficiency in fabricating tailored chemical powders remain significant challenges [24–26]. In contrast, laser-aided additive manufacturing (LAAM), which employs a multiple powder feeding system, offers distinct advantages in precisely controlling microstructural evolution. For instance, a CrMnFeCoNi/AlCoCrFeNiTi0.5 laminated multi-principal element alloy fabricated using LAAM exhibited an enhanced strength-plasticity synergy due to its unique heterogeneous microstructure—soft FCC columnar grains and ultra-hard BCC equiaxed grains alternating within the alloy [27]. Similarly, spatially heterostructured C_{300} maraging steel and 420 stainless steel have demonstrated superior strength-ductility combination. This is attributed to the effect of rule-of-mixture and hetero-deformation strengthening, which redistribute stress away from the soft to hard regions, ultimately improving global yield strength [28]. The (CoCrNi)87Al13 alloy prepared via multiple powder feeding system—employing CoCrNi powder combined with pure aluminum powder—exhibited a heterogeneous microstructure characterized by ordered/disordered BCC phases and the yield strength achieved 578 MPa [29]. These investigations demonstrated the immense potential of AM in fabricating phase-tunable materials. However, prior studies have primarily achieved phase tunability by modulating the existing FCC or/and BCC phases within lamellae or spatial structures, lacking real-time control over constituent materials during fabrication. This limitation restricts both design flexibility and mechanical property optimization.

Multi-principal-element alloys have attracted great attention due to their simple phase composition and performance [30–33]. Among these alloys, the FCC-structured CoCrNi alloy demonstrates exceptional strength-ductility synergy [34], while BCC-structured CoCrNiAl0.6TiFe exhibits outstanding hardness and strength [35]. These two alloys exhibit complementary phase architectures and mechanical properties, enabling their synergistic utilization in phase-tunable alloy design through strategic composition modulation. Therefore, this study proposes a strategy using dual-powder feeding that combines FCC-structured and BCC-structured multi-principal element alloy powders, enabling the fabrication of a series of materials with tunable FCC–BCC dual-phase structures and tailored mechanical properties. The research systematically investigates the microstructural evolution, underlying strengthening mechanisms, and the in situ deformation behavior of these alloys. By leveraging AM’s advanced capabilities, this study provides a foundational framework for exploring the relationship between additive manufacturing processes, phase tuning, and mechanical performance, paving the way for the development of next-generation high-performance, phase-engineered materials.

## 2. Experimental

## 2.1. Materials, fabrication and mechanical testing

Multi-principal element alloys were fabricated using LAAM, integrating a Kuka robotic system, Precitec laser

head, Sulzer metco twin powder feeder, and an IPG ytterbium fiber laser system (Fig. S_{1}). Pre-alloyed CoCrNi and CoCrNiAl0.6TiFe powders were prepared via gas atomization to ensure high sphericity and uniform size distribution and the particle sizes of the powders ranging from 15 to 45  $ \mu $m were confirmed using a laser particle size analyzer. The powders were then separately loaded into hoppers, blended, and fed into the powder nozzle. X-ray diffraction (XRD) patterns and scanning electron microscope (SEM) images confirmed the spherical morphology of both powders, with FCC and BCC phases in CoCrNi and CoCrNiAl0.6TiFe, respectively. By adjusting the feed rate ratios, six alloy compositions were produced as 50 mm \times 20 mm \times 6 mm blocks on 304 stainless steel substrates. Process optimization yielded the following parameters: 1.3 mm beam diameter, 570 W laser power, 5.4 g min $ ^{-1} $ total powder feed rate, and 1200 mm min $ ^{-1} $ scan velocity. The deposit layer was around 0.5 mm thickness, with a 90^\circ rotation between adjacent layers. The overlap rate was 50%, and argon gas (purity \geq 99.999%) was used for shielding and powder transport. The chemical compositions of the raw powders and fabricated blocks are detailed in Tables 1 and 2.

A uniaxial tensile loading experiment was executed utilizing a MTS E45 servo-hydraulic testing system integrated with a Correlated solutions’ optical strain measurement system featuring non-contact digital image correlation (DIC) technology. A 12MP camera (3000 \times 4000 pixels) captured strain images at 2 Hz. Testing coupons (25 mm \times 6 mm \times 4 mm) were extracted via wire cut electrical discharge machining, with tests conducted at a nominal strain rate of 0.6 mm min $ ^{-1} $.

## 2.2. Microstructural characterization

Phase identification was conducted using XRD (Rigaku Smartlab) with a Cu K\alpha radiation source at 150 mA and 40 kV. The scanning parameters included a 0.01^\circ step size and a 6^\circ min $ ^{-1} $ scanning speed. For microstructural analysis, a scanning electron microscope (SEM, FEI Apreo2S Lovac) was employed alongside electron backscattered diffraction (EBSD) and energy dispersive X-ray spectroscopy (EDS). Acceleration voltages were set at 10 kV for SEM and 20 kV for EBSD. A twin-jet electrochemical polishing procedure was used to prepare specimens for transmission electron microscopy (TEM) analysis with a 95

Table 1 Elemental compositions of feedstock powders (wt%)

| Powders | Co | Cr | Ni | Al | Ti | Fe |
| --- | --- | --- | --- | --- | --- | --- |
| CoCrNi | 34.14 | 30.14 | 35.72 |  |  |  |
| CoCrNiAl0.6TiFe | 20.09 | 17.12 | 21.37 | 6.12 | 15.69 | 19.61 |

Table 2 Weight percentage (wt%) of the CoCrNi and CoCr-NiAlO.6TiFe for fabrication of CoCrNi(AlO.6TiFe)x blocks

| No. | CoCrNi | CoCrNiAl0.6TiFe | Alloy code |
| --- | --- | --- | --- |
| 1 | 100 | 0 | CoCrNi |
| 2 | 90 | 10 | CoCrNi(Al0.6TiFe)0.1 |
| 3 | 80 | 20 | CoCrNi(Al0.6TiFe)0.2 |
| 4 | 70 | 30 | CoCrNi(Al0.6TiFe)0.3 |
| 5 | 60 | 40 | CoCrNi(Al0.6TiFe)0.4 |
| 6 | 50 | 50 | CoCrNi(Al0.6TiFe)0.5 |

vol% ethanol and 5 vol% perchloric acid electrolyte solution. Comprehensive microstructural characterization was conducted by use of a FEI Talos F200X G2 device at 200 kV. This system was configured for multiple advanced imaging modalities, including annular bright field (ABF)-STEM, annular dark field (ADF)-STEM, high-angle annular dark field (HAADF)-scanning TEM (STEM), and EDS. Instrument-specific parameters are as follows. HAADF-STEM: inner/outer semi-collection angles = 73–200 mrad; probe semi-convergence angle = 17 mrad. ADF-STEM: inner/outer collection angles = 14–63 mrad; probe semi-convergence angle = 17 mrad. ABF-STEM: inner/outer collection angles = 13–21 mrad; probe semi-convergence angle = 17 mrad. Fast Fourier transform (FFT) analysis was used for crystallographic examination of specific regions in HRTEM images.

Equilibrium phase diagrams of the LAAMed alloys were calculated using the Thermo-Calc software, specifically employing the Thermo-Calc high-entropy alloy version 6 (TCHEA6) database for phase diagram modeling and prediction.

## 3. Results

## 3.1. Microstructures

As evidenced by XRD analysis (Fig. 1A), FCC phase dominance persisted throughout all alloy variants, with lattice parameter expansion correlating to increased BCC-structured powder content. A progressive increase in lattice parameters is observed, ranging from CoCrNi to CoCr-Ni(Al_{0}.6TiFe)0.5 alloys. Based on calculations using Bragg’s law, the lattice parameters are determined to be 0.3282, 0.3291, 0.3297, 0.3303, 0.3306, and 0.3312 nm for CoCrNi, CoCrNi(Al_{0}.6TiFe)0.1, CoCrNi(Al_{0}.6TiFe)0.2, CoCrNi(Al_{0}.6TiFe)0.3, CoCrNi(Al_{0}.6TiFe)0.4, and CoCrNi(Al_{0}.6TiFe)0.5 alloys, respectively. This is primarily due to the solid solution effect of elements with larger atomic radii, such as Al and Ti. The CoCrNi alloy

Fig. 1 A XRD patterns and EBSD phase images of the LAAMed alloys: B CoCrNi; C CoCrNi(Al_{0}.6TiFe)0.1; D CoCrNi(Al_{0}.6TiFe)0.2; E CoCrNi(Al_{0}.6TiFe)0.3; F CoCrNi(Al_{0}.6TiFe)0.4; G CoCrNi(Al_{0}.6TiFe)0.5

consists predominantly of smaller atoms like Co (0.125 nm), Cr (0.127 nm), and Ni (0.124 nm), while the addition of Al (0.143 nm) and Ti (0.147 nm) significantly increases the average atomic size within the FCC phase, leading to lattice expansion [36]. Furthermore, the incorporation of Al and Ti may induce local lattice strain, further contributing to the observed lattice parameter changes. Further insights are provided by the EBSD phase maps shown in Fig. 1B–G. All of the investigated alloys predominantly exhibit an FCC phase structure, as corroborated

by XRD analysis. Notably, distinct microstructural variations are evident in CoCrNi(Al_{0}.6TiFe)0.4 and CoCrNi(Al_{0}.6TiFe)0.5 alloys, where micrometer-sized BCC precipitates are observed within the primary dendritic network. These precipitation features are distinctly visualized in the magnified regions shown in Fig. 1F, G. In the CoCrNi(Al_{0}.6TiFe)0.4 alloy, the BCC phase appears as small, irregular precipitates ( $ \sim $ 0.42  $ \mu $m) with a volume fraction of 0.5%, randomly dispersed within the FCC matrix. While in the CoCrNi(Al_{0}.6TiFe)0.5 alloy, the BCC phase grows to  $ \sim $ 2  $ \mu $m in size and surrounds the FCC matrix, with a volume fraction of 5.7%. This demonstrates enhanced segregation of Ti and Al at dislocation cell boundaries.

Figure 2A presents the ABF image of the CoCrNi alloy, where round-shaped nanoparticles are found distributed sporadically in the alloys. As shown in Fig. 2B, SAED analysis was conducted within a nanoparticle-free region, implying FCC phase of the CoCrNi alloys. Furthermore, EDS mapping results in Fig. 2C show that elemental segregations are absent in the alloys and the nanoparticles are depleted in Co and Ni, rich in O and Cr. This indicates that the nanoparticles are chromium oxide. The experimental data obtained in this study were corroborated by Weng et al. [37].

The TEM graphs, corresponding EDS mapping results, and SAED pattern of the CoCrNi(Al_{0}.6TiFe)0.2 alloys are depicted in Fig. 3. ABF and ADF images in Fig. 3A, B present numerous nanoparticle clusters. The phase identification was conducted, and the SAED pattern shown in Fig. 3C confirms that the alloy primarily exhibits FCC

Fig. 2 TEM/STEM results of LAAMed CoCrNi alloy. A An ABF-STEM image of the matrix; B a SAED pattern of the matrix; C the corresponding STEM-EDS maps

Fig. 3 TEM/STEM results of LAAMed CoCrNi(Al_{0}.6TiFe)0.2 alloy. A an ABF-STEM image, B an ADF-STEM image, C a SAED pattern of the matrix, D the corresponding STEM-EDS maps

phase. EDS analysis results, illustrated in Fig. 3D, indicate that these nanoparticles are rich in Al and O, suggesting that the addition of CoCrNiAl0.6TiFe powders has altered the preferential order of chemical reactions. It is worth noting that all alloys in this study were manufactured under local inert gas shielding conditions, hence, complete prevention of oxidation reactions was unattainable. Following the activity series of metals, the elements of the powders used in this study react with oxygen in the sequence of Al, Ti, Cr, Fe, Co and Ni. In the CoCrNi alloy, Cr is the most susceptible element to oxidation, primarily forming Cr oxides. However, with the addition of CoCrNiAl0.6TiFe, Al became the element most prone to oxidation, resulting in the formation of Al oxide nanoparticles in the CoCr-Ni(Al_{0}.6TiFe)0.2 alloy.

For CoCrNi(Al_{0}.6TiFe)0.3 alloy, the presence of nanoparticle clusters dispersed within the matrix has been detected, as illustrated in Fig. S_{2}. The morphologies are similar to that in CoCrNi(Al_{0}.6TiFe)0.2 alloy. The SAED graph confirms the dominance of FCC phase. The EDS mapping results show that some aluminum oxides exist in the alloy. Besides, elemental segregations are not observed in both CoCrNi(Al_{0}.6TiFe)0.2 and CoCrNi(Al_{0}.6TiFe)0.3 alloys. This indicates that during the LAAM process, FCC-structured and BCC-structured powders are fully mixed and melted, elemental diffusion in liquid alloys is sufficient. These findings are well agreed with XRD and EBSD analysis results. For alloys with addition of BCC-structured CoCrNiAl0.6TiFe powders less than 30 wt%, FCC phase is the primary phase.

Figure 4 illustrates the TEM/STEM results of the CoCrNi(Al_{0}.6TiFe)0.4 alloy. In Fig. 4A, irregularly shaped precipitates and nanoparticles are observed. The EDS results in Fig. 4B demonstrate that the precipitates exhibit richness in Al, Ti, and trace amounts of Ni. Meanwhile, the nanoparticles are rich in Al and O, indicating the formation of aluminum oxide during alloy fabrication. Figure 4C, D shows the SAED patterns of the

Fig. 4 TEM/STEM results of LAAMed CoCrNi(Al_{0}.6TiFe)0.4 alloy. A an ADF-STEM image, B STEM-EDS mapping results, C a SAED pattern of the matrix, D a SAED pattern of the precipitate

matrix and the precipitates, revealing that the CoCr-Ni(Al_{0}.6TiFe)0.4 alloys are composed of B_{2} phase and FCC phase. The finding of phase composition is consistent with EBSD phase analysis (Fig. 1). It can be deduced that B_{2} phase precipitated from the LAAMed alloys when the content of BCC-structured powders in raw powders is more than 40 wt%.

The morphology and EDS mapping results of CoCr-Ni(Al_{0}.6TiFe)0.5 in Fig. S_{3} further prove the formation mechanism of B_{2} phase. More obvious cellular structures were observed when compared to CoCrNi(Al_{0}.6TiFe)0.4 alloy, in which the FCC phase is encircled by bright precipitates. This indicates that as the portion of BCC-structured powders increases in the raw powders, more B_{2} phase precipitates in the LAAMed alloys. The elemental distribution of CoCrNi(Al_{0}.6TiFe)0.5 alloy reveals that the precipitates are depleted in Co, Cr, Fe, displaying similar characteristics to those observed in CoCrNi(Al_{0}.6TiFe)0.4 alloy. Additionally, some aluminum oxides are detected, which mainly distribute inner the cellular structure. It is noteworthy that Fe is depleted in B_{2} phase. In the raw powders, Fe exists in the BCC-structured powders. However, after LAAM, Fe tends to gather in FCC phase. This means that B_{2} phase precipitated from the mixed liquid alloy rather than remnant of BCC-structured powder. Through detailed analysis for the LAAMed alloys, it demonstrates that LAAM could tune the phase composition by changing the delivering ratio of FCC and BCC powders. This simple and convenient method provides huge potential in fabricating tunable microstructures of materials and then customizing the mechanical properties.

## 3.2. Mechanical properties

Figure 5 shows the DIC images during tensile test, engineering stress–strain curves, true stress–strain curves and work-hardening rate curves of the LAAMed alloys. Figure 5A presents the final macro-DIC image of the tensile

Fig. 5 Mechanical properties of the LAAMed alloys. A DIC images; B engineering strain–stress curves; C true strain–stress curves and D work-hardening rate curves

samples before fracture. It can be observed that with the addition of BCC-structured powders, the maximum local strain of the alloy decreases from 79% to 5%, while the deformation in the gauge section of the alloy is significantly reduced, indicating a substantial decrease in the alloy’s plasticity. The engineering stress–strain curves depicted in Fig. 5B reveal a pronounced strengthening effect with increasing proportion of BCC-structured powders in the feedstock mixture (quantitative data are provided in Table S_{1}). The CoCrNi alloy demonstrates a yield strength of 486 MPa, an ultimate tensile strength of 781 MPa, and an elongation at failure of 42.2%, while the CoCrNi(Al_{0}.6TiFe)0.5 alloy demonstrates a yield strength and ultimate tensile strength of 887.2 and 1165.2 MPa accompanied by a reduced ductility of 4.0%. This enhanced strength can be attributed to the precipitation of B_{2} phase, which are inherently prone to interact with dislocations and impede the motion of dislocations. Furthermore, similar trend of mechanical properties is also observed in the true stress–strain curves, as shown in Fig. 5C.

Figure 5D reveals the corresponding work-hardening rate curves with respect to the true strain in the LAAMed alloys before necking. Apparently, CoCrNi, CoCrNi(Al_{0}.6TiFe)0.1, CoCrNi(Al_{0}.6TiFe)0.2, and CoCrNi(Al_{0}.6TiFe)0.3 alloys exhibit a characteristic triphasic decline in strain-hardening rate with increasing plastic strain. Stage I (elastic–plastic transition): The initial precipitous drop in work-hardening rate is attributed to the dominance of elastic-to-plastic deformation accommodation, where dislocation nucleation and short-range glide prevail. Stage II (deformation mode coupling): A reduced work-hardening rate slope emerges as deformation mechanisms transition from dislocation slip dominance to a synergistic interplay of twinning, phase transformation, and localized shear banding. Stage III (damage accumulation): The work-hardening rate undergoes a steep decay prior to fracture, indicative of strain localization and microvoid coalescence exceeding the material’s capacity for defect storage. These features of work-hardening rate would postpone the initiation of necking, manifesting superior combination of tensile strength and uniform elongation [38, 39]. For CoCrNi(Al_{0}.6TiFe)0.4 alloy, only stage I and stage III appear in the work-hardening rate curves, revealing a dislocation-governed deformation mechanism. It is also observed that CoCrNi(Al_{0}.6TiFe)0.5 alloy just experienced stage I and then fractured due to lack of ductility. Besides, it is worth to note that in the initial stage, the values of work-hardening rate in CoCrNi(Al_{0}.6TiFe)0.4, and CoCrNi(Al_{0}.6TiFe)0.5 alloys are much larger than CoCrNi, CoCrNi(Al_{0}.6TiFe)0.1, CoCrNi(Al_{0}.6TiFe)0.2, and CoCrNi(Al_{0}.6TiFe)0.3 alloys. For example, at strain of 3.5%, the work-hardening rates for CoCrNi, CoCrNi(Al_{0}.6TiFe)0.1, CoCrNi(Al_{0}.6TiFe)0.2, CoCrNi(Al_{0}.6TiFe)0.3, CoCrNi(Al_{0}.6TiFe)0.4, and CoCrNi(Al_{0}.6TiFe)0.5 are 2206, 2535, 2637, 3035, 4404, and 6539 MPa, respectively. Such strong work-hardening capacity enables CoCrNi(Al_{0.6}-TiFe)0.4 and CoCrNi(Al_{0}.6TiFe)0.5 alloys the excellent strength. In CoCrNi(Al_{0}.6TiFe)0.4 and CoCrNi(Al_{0.6}-TiFe)0.5 alloys, B_{2} phase hindered the motion of dislocations, resulting their accumulation around the B_{2} phase and then causing greatly increased strength.

In order to further investigate the deformation behavior, microstructural characterization at sequential strain levels during DIC tests was undertaken. To avoid repeated description for similar structures, CoCrNi, CoCrNi(Al_{0}.6TiFe)0.2, and CoCrNi(Al_{0}.6TiFe)0.4 alloys are selected as representatives. Figure 6 systematically depicts the kernel average misorientation (KAM) diagrams, inverse pole figure (IPF) maps subjected to progressive deformation levels ( $ \varepsilon = 0\% $, 25%, 45%, and 74.5% at fracture) in the same testing sample, and TEM observations of the fracture surface for CoCrNi alloys. The IPF patterns (Fig. 6A, C, E, G) reveal pronounced grain elongation along the tensile loading direction. Analysis of the KAM maps (Fig. 6B, D, F, H) demonstrates stress concentration heterogeneity. In the undeformed region ( $ \varepsilon = 0\% $), residual stresses are localized at grain boundaries, whereas most grains exhibit low-stress regions (blue-dominated areas) indicating near-

Fig. 6 EBSD and TEM/STEM results of CoCrNi alloy. IPF and KAM diagrams for distinct deformation zones: A, B undeformed, C, D  $ \varepsilon = 25\% $, E, F  $ \varepsilon = 45\% $, G, H fracture region, and TEM results on fracture surface: I an ADF-STEM image of dislocations, J an ABF-STEM image of the twin and corresponding SAED pattern, K HRTEM image of the stacking faults, L FFT of the stacking faults

equilibrium stress states. As the deformation level increases, more yellow-colored stress concentration regions appeared within the grains, uniformly distributed along the slip direction. This indicates that the CoCrNi alloy underwent homogeneous deformation, with a large portion of the grains participating in plastic deformation, thereby exhibiting high plasticity. In addition, the insets of Fig. 6G, H show the morphology at high-magnification, numerous twins induced by deformation can be observed. This demonstrates the occurrence of the twinning-induced plasticity effect (TWIP), which contributed to the plasticity of the CoCrNi alloy, consistent with previous research findings by Gludovatz et al. [40]. Figure 6I–L illustrates the TEM findings of the CoCrNi alloy after deformation. In Fig. 6I, high density of dislocations can be observed, implying mediated plasticity by planar dislocation slip. On the other hand, due to the characteristics of non-uniform solidification and high cooling rates in the LAAM process, the resulting alloy grains are fine and the boundaries are effective obstacles to dislocation motion. This explains why the additively manufactured alloys often exhibit higher yield strength compared to conventionally cast alloys [41]. Figure 6J–L exhibits the morphology and SAED of deformation twin, high-resolution images of stacking faults and the corresponding fast Fourier transform. These indicate twinning and stacking faults participated in the deformation and well explained the smaller slope of work-hardening rate in the stage II (Fig. 5D).

Figure 7A–M shows the EBSD results of CoCr-Ni(Al_{0}.6TiFe)0.2 alloy during tensile test. Similar to the CoCrNi alloy, pronounced grain elongation along the tensile loading axis is evident in the deformed microstructure (Fig. 7A, C, E, G). Quantitative KAM analysis (Fig. 7B, D, F, H) demonstrates stress state heterogeneity. In the undeformed region, residual stresses are localized at grain boundaries, while low-stress domains (blue-dominated areas) dominate most grains. As deformation progresses, yellow regions indicative of elevated stress concentrations emerge within the grains, exhibiting analogous stress distribution patterns to those observed in the CoCrNi alloy (Fig. 6). The contrast with CoCrNi lies in the fact that, in CoCrNi(Al_{0}.6TiFe)0.2 alloy, with increased deformation, stress concentrates at grain boundaries, exhibiting a deep yellow hue. This concentration of stress at interfaces can lead to premature fracture without sufficient internal deformation, thereby limiting the alloy’s ability for uniform deformation and resulting in decreased plasticity. Additionally, the absence of deformation twins further diminishes the alloy’s plasticity. Figure 7I–K exhibits the TEM results after deformation. In the ABF-STEM image (Fig. 7I), amounts of dislocations are evident within the cellular structure, signifying an intense dislocation strengthening effect, resulting in its higher yield and ultimate strength. This high-density dislocation phenomenon has been previously documented in Mu et al.’s research [42]. Figure 7J, K reveals the presence of complex dislocation networks localized at the dendritic network boundaries, which function as critical strengthening elements through the restriction of dislocation slip mechanisms. These microstructural features contribute to significant strength enhancement by acting as barriers to dislocation propagation, thereby improving the alloy’s mechanical performance.

The EBSD results in different deformed regions and TEM results on fracture surface of the CoCrNi(Al_{0.6}-TiFe)0.4 alloy are shown in Fig. 8. Heavily deformed grains elongated along the tension axis can also be observed in the IPF graphs (Fig. 8A, C, E, G). Figure 8B reveals pronounced stress heterogeneity in the undeformed region, with notable stress localization at the boundaries of the cellular microstructures. High-magnification EBSD observations (inset) confirm the presence of B_{2}-type intermetallic precipitates at these stress-concentrated regions. During LAAM processing, the FCC phase exhibits selective nucleation and solidification behavior prior to B_{2} phase formation. This sequential phase evolution results in the embedding of B_{2} phase particles within the interphase regions of multiple FCC cellular networks. The elevated processing temperature combined with ultra-rapid cooling rates (approximate  $ 10^{6} $ ^\circC·s $ ^{-1} $) [43] leads insufficient release of thermal stress, ultimately concentrating stress within the B_{2} phase. With increasing deformation (Fig. 8D, F, H), the stress concentration phenomenon at the boundaries of the cellular structure becomes more pronounced, and these stressed areas progressively connecting. This is related to the increased strength and decreased ductility shown in Fig. 5B. Under external tensile force, dislocations move in the FCC phase before reaching the B_{2} phase, endowing the alloy ductility. Then, the dislocations accumulate at the boundaries due to the obstacle of B_{2} phase, resulting in higher strength to fracture. These results imply a dislocation-governed deformation for CoCrNi(Al_{0}.6TiFe)0.4 alloy, which can well explain the two-stage decrease feature of the strain-hardening rate (Fig. 5D). The TEM images on the fracture surface are depicted in Fig. 8I–K. It is obvious that dislocations are detected in both the matrix FCC phase (Fig. 8I) and B_{2} phase (Fig. 8J). In addition, high-density dislocations were observed at the boundaries between FCC and B_{2} phases.

TEM findings of the CoCrNi(Al_{0}.6TiFe)0.5 alloy after deformation are illustrated in Fig. S_{4}. Compared to CoCrNi(Al_{0}.6TiFe)0.4 alloy, bigger precipitated B_{2} phases around FCC matrix are observed, which are ascribed to the microstructure-tunable LAAM strategy. High-density dislocations are observed on the FCC matrix side, implying

Fig. 7 EBSD and STEM results of CoCrNi(Al_{0}.6TiFe)0.2 alloy. IPF and KAM diagrams for distinct deformation zones: A, B undeformed, C, D  $ \varepsilon = 25\% $, (E, F)  $ \varepsilon = 45\% $, G, H fracture region, and TEM observation on fracture surface: I an ABF-STEM image in low magnification J an ADF-STEM image in high magnification, K an ADF-STEM image of the cellular boundary

that the high strength of the CoCrNi(Al_{0}.6TiFe)0.5 alloy stems from the strengthening effect of dislocations and precipitates. The CoCrNi(Al_{0}.6TiFe)0.5 alloy has excellent strength, but fractures after stage I (Fig. 5D), which is related to the abundantly precipitated B_{2} phase. The B_{2} phase at the cellular structure boundaries can hinder the movement of dislocations, thereby increasing the strength but impeding the plastic deformation and prone to break. The cracks at the boundaries are the hard evidence for its brittle characteristic.

## 4. Discussion

## 4.1. Phase formation and microstructural evolution

In the above analyses, the phase composition of the alloys (Fig. 1) and different chemical composition of B_{2} phase (Fig. 4) with BCC-structured powder demonstrate that the raw powders are fully mixed and melted during the AM process. This demonstrated that B_{2} precipitates in CoCr-Ni(Al_{0}.6TiFe)0.4 and CoCrNi(Al_{0}.6TiFe)0.5 alloys

Fig. 8 EBSD and TEM/STEM results of CoCrNi(Al_{0}.6TiFe)0.4 alloy. IPF and KAM diagrams for distinct deformation zones: A, B undeformed, C, D  $ \varepsilon = 10\% $, E, F  $ \varepsilon = 15\% $, G, H fracture region, and TEM graphs on fracture surface: I an ADF-STEM image of FCC matrix and B_{2} precipitates, J a HRTEM image of the B_{2} phase, K an ABF-STEM image of the boundary

originated from in situ phase separation rather than residual unmelted BCC-structured particles, which means that the formation of the phase in these alloys obeys the formation rules of CoCrNi(Al_{0}.6TiFe)x. Figure S_{5} shows the calculated phase composition by CALPHAD method based on high-entropy alloy version 6 thermodynamic database. The results show that CoCrNi, CoCrNi(Al_{0}.6TiFe)0.1 and CoCrNi(Al_{0}.6TiFe)0.2 alloys have FCC and sigma ( $ \sigma $) phases, while CoCrNi(Al_{0}.6TiFe)0.3, CoCrNi(Al_{0.6}-TiFe)0.4 and CoCrNi(Al_{0}.6TiFe)0.5 have FCC,  $ \sigma $ and B_{2} phases. However, these theoretical results are inconsistent with experimental observation (Fig. 1). In experimental detection,  $ \sigma $ phase was not observed in all of the alloys, while B_{2} phase did not precipitate from CoCrNi(Al_{0.6}-TiFe)0.3 alloy. The discrepancy is believed to be associated with the AM process. In calculation, the predicted phase composition is in equilibrium state, but the AM process is a non-equilibrium state due to the intrinsic large thermal gradient and high cooling rate [44]. In the AM process, the powders were melted by laser and then solidified rapidly, inhibiting the  $ \sigma $ and B_{2} phases’ precipitation. The only stable phase that forms during cooling is

the FCC phase [45]. For CoCrNi(Al_{0}.6TiFe)0.4 and CoCrNi(Al_{0}.6TiFe)0.5 alloys, however, B_{2} phase increases to about 10% and 20% in thermal-calc diagram, the high solidification rate is not enough to inhibit their precipitation in fabrication process.

Microstructural evolution of the AMed alloys is associated with the chemical composition of CoCrNi(Al_{0}.6Ti-Fe)x alloys. In CoCrNi, CoCrNi(Al_{0}.6TiFe)0.1, CoCrNi(Al_{0}.6TiFe)0.2 and CoCrNi(Al_{0}.6TiFe)0.3 alloys, constituent elements are distributed uniformly, exhibiting FCC solid solution phase. Whereas, in CoCrNi(Al_{0.6}-TiFe)0.4 and CoCrNi(Al_{0}.6TiFe)0.5 alloys, B_{2} phase rich in Ti, Al precipitated around the FCC phase (Figs. 4, S_{4}). Elemental segregation at grain boundaries is fundamentally governed by the segregation enthalpy ( $ \Delta H_{i}^{seg} $), defined as the Gibbs free energy difference between solute atoms occupying the boundary site and intra-grain site,  $ \Delta H_{i}^{seg} \approx \Delta E_{i}^{seg} = \Delta E_{b,i}^{solute} - \Delta E_{g}^{solute} $. A negative  $ \Delta E_{i}^{seg} $ promotes segregation of the element. The  $ \Delta E_{i}^{seg} $ in a polycrystal will determine the extent of equilibrium boundary segregation in an alloy. According to the prediction [46], the segregation energies of Ti, Al and the main constituent elements in the present alloys Co, Ni are all negative. Therefore, Ti, Al elements are rich in the cellular boundaries. Atomic radii difference can also affect the elemental segregation. Since the atomic volumes of Ti, Al elements are larger than Co, Cr, Ni, and Fe [47], their segregation can lower the lattice distortion energy, increase the phase stability of the alloy.

## 4.2. Tuned mechanical properties via dual-phase microstructure

The mechanical properties are greatly depended on the phase composition and microstructures. In this investigation, CoCrNi(Al_{0}.6TiFe)x alloys with microstructurally diverse characteristics were successfully processed using a dual-powder feeding LAAM technique. In turn, the mechanical properties were tuned by the different phases and microstructures.

To establish quantitative structure–property relationships in the CoCrNi(Al_{0}.6TiFe)x system (x = 0–0.5), a multiscale strengthening model was implemented incorporating four dominant mechanisms: solid solution strengthening  $ \sigma_{Solution} $, grain-refinement strengthening  $ \sigma_{Grain} $, dislocation strengthening  $ \sigma_{Dislocation} $ and precipitation strengthening  $ \sigma_{Precipitation} $ [48], and the yield strength ( $ \sigma_{yield} $) of the alloys can be mathematically expressed as Eq. (1):

 $$ \sigma_{yield}=\sigma_{0}+\sigma_{Solution}+\sigma_{Grain}+\sigma_{Dislocation}+\sigma_{Precipitation} $$ 

where  $ \sigma_{0} = 218 $ MPa is the intrinsic strength of CoCrNi alloy [49]. On account of the absence of precipitation in CoCrNi alloy, the increase of yield strength of CoCrNi(Al_{0}.6TiFe)x alloys compared to CoCrNi alloys can be described in Eqs. (2–4):

 $$ \mathbf{\Delta}\sigma_{yield,i}=\sigma_{Solution,i}+\mathbf{\Delta}\sigma_{Grain,i}+\mathbf{\Delta}\sigma_{Disloaton,i}+\sigma_{Precipitation,i} $$ 

 $$ \Delta\sigma_{\mathrm{G r a i n},i}=\sigma_{\mathrm{G r a i n},i}-\sigma_{\mathrm{G r a i n,C o C r N i}} $$ 

 $$ \Delta\sigma_{\mathrm{Dislocation},i}=\sigma_{\mathrm{Dislocation},i}-\sigma_{\mathrm{Dislocation,CoCrNi}} $$ 

In CoCrNi(Al_{0}.6TiFe)x alloys, Al, Ti, Fe are considered as solid solution elements in CoCrNi alloy. The contribution of substitutional solid solution strengthening ( $ \sigma_{Solution} $) is calculated using the classical Taylor model [50], as shown in Eqs. (5–7).

 $$ \sigma_{Solution}=M\frac{G\cdot\varepsilon_{S}^{3/2}\cdot c^{1/2}}{700} $$ 

 $$ \varepsilon_{\mathrm{S}}=|3\varepsilon_{\mathrm{a}}| $$ 

 $$ \varepsilon_{\mathrm{a}}=\frac{1}{a}\frac{\partial a}{\partial c} $$ 

where Taylor factor $M = 3.06$, shear modulus $G = 90$ GPa is estimated, the lattice parameters $a$ were refined using Rietveld analysis of XRD patterns: $a_{\mathrm{CoCrNi}} = 0.3282$ nm, $a_{\mathrm{CoCrNi(Al0.6TiFe)0.1}} = 0.3291$ nm, $a_{\mathrm{CoCrNi(Al0.6TiFe)0.2}} = 0.3297$ nm, $a_{\mathrm{CoCrNi(Al0.6TiFe)0.3}} = 0.3303$ nm, $a_{\mathrm{CoCrNi(Al0.6TiFe)0.4}} = 0.3306$ nm and $a_{\mathrm{CoCrNi(Al0.6TiFe)0.5}} = 0.3312$ nm, molar ratio $c = x_{\mathrm{Al}} + x_{\mathrm{Ti}} + x_{\mathrm{Fe}}$.

The grain boundary strengthening contribution is quantified using the classical Hall–Petch relationship [51], as shown in Eq. (8):

 $$ \sigma_{Grain}=k_{y}\times\frac{1}{d^{1/2}} $$ 

where empirical strength coefficient  $ k_{y} = 568 $ MPa  $ \mu $m $ ^{1/2} $ is determined from nano-indentation tests on CoCrNi alloys [52], and the average grain size d is obtained via XRD line broadening analysis.

The dislocation hardening contribution is derived using the Taylor hardening law [53], as shown in Eq. (9):

 $$ \sigma_{\mathrm{D i s l o c a t i o n}}=M\alpha G b\sqrt{\rho} $$ 

where  $ \alpha = 0.2 $ is a constant for FCC metals,  $ b = a/\sqrt{2} $ is the burgers vector. And dislocation density  $ \rho $ is determined via modified Williamson–Hall method, as shown in Eq. (10):

 $$ \rho=\frac{2\sqrt{3}\varepsilon_{\mathrm{D}}}{db} $$ 

where  $ \varepsilon_{D} $ is the micro-strain caused by dislocations obtained from the refined XRD data.

Rare Met.

Table 3 Calculated yield strength increase compared to CoCrNi alloy

| Alloy code | Phase composition | $ \sigma_{S} $ (MPa) | $ \Delta\sigma_{G} $(MPa) | $ \Delta\sigma_{D} $ (MPa) | $ \sigma_{P} $ (MPa) | $ \rho $ (m $ ^{-2} $) |
| --- | --- | --- | --- | --- | --- | --- |
| CoCrNi(Al0.6TiFe)0.1 | FCC | 3.29 | - 7.82 | 76.29 | - | 5.6  $ \times $ 10 $ ^{14} $ |
| CoCrNi(Al0.6TiFe)0.2 | FCC | 4.62 | 14.31 | 94.29 | - | 1.7  $ \times $ 10 $ ^{15} $ |
| CoCrNi(Al0.6TiFe)0.3 | FCC | 5.62 | 14.92 | 210.00 | - | 2.5  $ \times $ 10 $ ^{15} $ |
| CoCrNi(Al0.6TiFe)0.4 | FCC + B2 | 6.45 | 15.06 | 90.55 | 302.57 | 1.6  $ \times $ 10 $ ^{15} $ |
| CoCrNi(Al0.6TiFe)0.5 | FCC + B2 | 7.16 | - 1.57 | 115.12 | 371.81 | 5.5  $ \times $ 10 $ ^{14} $ |

 $ \sigma_{\text{Precipitation}} $ is estimated by modified shear-lag model [53], which is expressed as Eqs. (11, 12):

 $$ \sigma_{Precipitation}=\sigma_{m}\left[\frac{V_{p}\left(S_{p}+2\right)}{2}+1-V_{p}\right] $$ 

 $$ \sigma_{\mathrm{m}}=\sigma_{0}+\sigma_{\mathrm{S o l u t i o n}}+\sigma_{\mathrm{G r a i n}} $$ 

where  $ \sigma_{m}=295.91 $ is the strength of FCC matrix, volume fraction ( $ V_{p} $) and average aspect ratio ( $ S_{p} $) of B_{2} precipitations are counted through EBSD images. The applied values of  $ V_{p} $ are 0.005 and 0.057 for CoCrNi(Al_{0}.6TiFe)0.4 and CoCrNi(Al_{0}.6TiFe)0.5 alloys, while  $ S_{p}=9 $ is adopted for both alloys.

The calculation results are shown in Table 3. In CoCr-Ni(Al_{0}.6TiFe)0.1, CoCrNi(Al_{0}.6TiFe)0.2 and CoCr-Ni(Al_{0}.6TiFe)0.3 alloys, the total strength increases compared to CoCrNi alloy are 71.76, 113.22 and 230.54 MPa, respectively. These calculated values are well agreed with the experimental testing results (69.1, 105 and 203.3 MPa, respectively). Meanwhile, the strength increase contributed by solutes and refined grain is just several and a dozen MPa, which is much fewer than dislocation strengthening. Especially for CoCrNi(Al_{0}.6TiFe)0.3 alloy, dislocation strengthening devotes 210 MPa (about 91%) to the total strength increase compared to CoCrNi alloy. It plays a dominant role in enhancing the mechanical properties. In CoCrNi(Al_{0}.6TiFe)0.4, CoCrNi(Al_{0}.6TiFe)0.5 alloys, dislocation strengthening still plays a role. The dislocation density resulted from non-uniform solidification and high cooling rates in the LAAM process reaches  $ 1.6 \times 10^{15} $ m $ ^{-2} $ and  $ 5.5 \times 10^{14} $ m $ ^{-2} $ respectively. However, due to the precipitation of B_{2} phase, the role of precipitation strengthening is increasing. As presented in Table 3, precipitation strengthening is triple as strong as dislocation strengthening, which is attributed to the increasing fraction of B_{2} phase. The strengthening mechanisms also caused the special work-hardening rate curves (Fig. 5D) of CoCrNi(Al_{0}.6TiFe)0.4 and CoCrNi(Al_{0.6}-TiFe)0.5 alloys. The precipitated B_{2} phase hindered the motion of dislocations, causing the high work-hardening rate in the initial stage. Meanwhile, the intrinsic undeformable nature of B_{2} phase resulted in the sharp drop of the rate as the strain increased.

## 5. Conclusion

This study demonstrates a novel strategy for designing high-performance multi-principal element alloys with tunable FCC–BCC phases and mechanical properties via laser-aided additive manufacturing using dual FCC/BCC powder feedstock.

The phase compositions are determined by the phase formation rules of CoCrNi(Al_{0}.6TiFe)x multi-principal element alloys in addition to the intrinsic high cooling rate and large thermal gradient of AM process. The elemental segregation of Al, Ti at cellular boundaries is associated with the larger atomic radii and negative segregation enthalpy with other main constituent elements.

The tensile yield strength and work-hardening rate increase dramatically with the content of BCC-structured CoCrNiAl0.6TiFe powders increases in the raw powders. Dislocation strengthening (76–210 MPa) is the major strengthening mechanism when the alloys exhibit a single FCC phase. Once the B_{2} phase precipitates, precipitation strengthening dominates the strength enhancement.

Laser-aided additive manufacturing is an effective method to obtain new alloys by adopting existing alloy powders instead of fabricating new alloy powders with different compositions. It can easily tune the alloy composition and phases by changing the delivery ratio of FCC and BCC powders, exhibiting a promising route to produce parts with diverse mechanical properties in different zones.

Acknowledgements This study was financially supported by the following sources: Guangdong Basic and Applied Basic Research Foundation (No. 2023B1515120045), Yangjiang City Key Industry Talent Revitalization Plan Project for Alloy Materials and Hardware Scissors (No. RCZX202302), GDAS' Project of Science and Technology Development (Nos. 2022GDASZH-2022010108, 2022GDASZH-2022010107 and 2024GDASZH-2024010102), GDAS' Young Talent Project (No. 2024GDASQNRC-0314), Guangzhou Basic and Applied Basic Research Foundation (No. 2023A04J1628), the National Key R&D Program of China (No. 2022YFB4600700), National Natural Science Foundation of China (No. 52371110), Guangdong Basic and Applied Basic Research Foundation (No. 2023A1515011510), Shenzhen Science and Technology Program (Nos. JCYJ20220530115011026 and JCYJ20230807093410021), and Shanxi Province Key R&D Project (No. 202302050201011).

Author contributions Lijia Chen was involved in conceptualization, methodology, validation, formal analysis, investigation, writing—original draft, and visualization; Sihao Zou was involved in validation, formal analysis, investigation, and visualization; Shang Sui was involved in visualization; Fei Weng was involved in writing—review and editing; Shangxiong Huangfu was involved in writing—review and editing; Lichao Cao was involved in writing—review and editing; Hao Zhang was involved in writing—review and editing; Sergey-Vasilievich Gaponenko was involved in writing—review and editing; Tao Yang was involved in writing—review and editing; Jiang Ju was involved in writing—review and editing; Lidong Zhao was involved in writing—review and editing; Wenjun Lu was involved in resources, data curation, writing—review and editing, supervision, and project administration; Guijun Bi was involved in conceptualization, resources, data curation, writing—review and editing, supervision, and project administration.

## Data Availability

## Declarations

Conflict of interests The authors declare that they have no conflict of interest.

## References

[1] Su JL, Jiang FL, Teng J, Chen LQ, Requena G, Yan M, Zhang LC, Wang Y, Okulov I, Zhu HM, Bo GW, Chew YX, Tan CL. Laser additive manufacturing of titanium alloys: process, materials and post-processing. Rare Met. 2024;43(12):6288–328. https://doi.org/10.1007/s12598-024-02685-x.

[2] Zhang WT, Wang XQ, Zhang FQ, Cui XY, Fan BB, Guo JM, Guo ZM, Huang R, Huang W, Li XB, Li MR, Ma Y, Shen ZH, Sun YG, Wang DZ, Wang FY, Wang LQ, Wang N, Wang TL, Wang W, Wang XY, Wang YH, Yu FJ, Yin YZ, Zhang LK, Zhang Y, Zhang JY, Zhao Q, Zhao YP, Zhu XD, Sohail Y, Chen YN, Feng T, Gao QL, He HY, Huang YJ, Jiao ZB, Ji H, Jiang Y, Li Q, Li XM, Liao WB, Lin HJ, Liu H, Liu Q, Liu QF, Liu WD, Liu XJ, Lu Y, Lu YP, Ma W, Miao XF, Pan J, Wang Q, Wu HH, Wu Y, Yang T, Yang WM, Yu Q, Zhang JY, Chen ZG, Mao L, Ren Y, Shen BL, Wang XL, Jia Z, Zhu H, Wu ZD, Lan S. Frontiers in high entropy alloys and high entropy functional materials. Rare Met. 2024;43(10):4639–776. https://doi.org/10.1007/s12598-024-02852-0.

[3] Tu HL, Zhao HB, Fan YY, Zhang QZ. Recent developments in nonferrous metals and related materials for biomedical applications in China: a review. Rare Met. 2022;41(5):1410–33. https://doi.org/10.1007/s12598-021-01905-y.

[4] Garcia-Gonzalez D, Ter-Yesayants T, Moreno-Mateos MA, Lopez-Donaire ML. Hard-magnetic phenomena enable autonomous self-healing elastomers. Compos B Eng. 2023;248:110357. https://doi.org/10.1016/j.compositesb.2022.110357.

[5] Temesi T, Czigany T. Integrated structures from dissimilar materials: the future belongs to aluminum–polymer joints. Adv Eng Mater. 2020. https://doi.org/10.1002/adem.20200007.

[6] Wu MW, Hu ZF, Yang BB, Tao Y, Liu RP, Ma CM, Zhang L. Additive manufacturing of Cu-Al-Mn shape memory alloy with enhanced superelasticity. Rare Met. 2023;42(12):4234–45. https://doi.org/10.1007/s12598-023-02353-6.

[7] Wang D, Liu LQ, Deng GW, Deng C, Bai YC, Yang YQ, Wu WH, Chen J, Liu Y, Wang YG, Lin X, Han CJ. Recent progress on additive manufacturing of multi-material structures with laser powder bed fusion. Virtual Phys Prototyping. 2022;17(2):329–65. https://doi.org/10.1080/17452759.2022.2028343.

[8] Nazir A, Gokcekaya O, Md Masum Billah K, Ertugrul O, Jiang J, Sun J, Hussain S. Multi-material additive manufacturing: a systematic review of design, properties, applications, challenges, and 3D printing of materials and cellular metamaterials. Mater Des. 2023;226:111661. https://doi.org/10.1016/j.matdes.2023.111661.

[9] Li Y, Feng Z, Hao L, Huang L, Xin C, Wang Y, Billotti E, Essa K, Zhang H, Yan FF, Peijs T. A review on functionally graded materials and structures via additive manufacturing: from multi-scale design to versatile functional properties. Adv Mater Technol. 2020. https://doi.org/10.1002/admt.201900981.

[10] Ding B, Song HY, An MR, Xiao MX, Li YL. Atomistic simulations of deformation mechanism of fcc/bcc dual-phase high-entropy alloy multilayers. J Appl Phys. 2021. https://doi.org/10.1063/5.0070470.

[11] Chang C, Liao H, Yi L, Dai Y, Cox SC, Yan M, Liu M, Yan XC. Achieving ultra-high strength and ductility in Mg–9Al–1Zn–0.5 Mn alloy via selective laser melting. Adv Powder Mater. 2023;2(2):100097. https://doi.org/10.1016/j.apmate.2022.100097.

[12] Yuan B, Ge JG, Zhang L, Chen HJ, Wei LS, Zhou YD, Song RH. Laser powder bed fusion of NiTiFe shape memory alloy via pre-mixed powder: microstructural evolution, mechanical and functional properties. Rare Met. 2024;43(5):2300–16. https://doi.org/10.1007/s12598-023-02604-6.

[13] Ma C, Ge Q, Yuan L, Gu D, Dai D, Setchi R, Wu MP, Liu Y, Li DY, Ma S, Peng X, Fang ZY. The development of laser powder bed fused nano-TiC/NiTi superelastic composites with hierarchically heterogeneous microstructure and considerable tensile recoverable strain. Compos B Eng. 2023;250:110457. https://doi.org/10.1016/j.compositesb.2022.110457.

[14] Hehr A, Dapino MJ. Interfacial shear strength estimates of NiTi–Al matrix composites fabricated via ultrasonic additive manufacturing. Compos B Eng. 2015;77:199–208. https://doi.org/10.1016/j.compositesb.2015.03.005.

[15] Li K, Ma R, Zhan J, Wu J, Fang J, Wang S, Yang QJ, Gong N, Murr L, Cao HJ. Insight into the cracking mechanism of super-elastic NiTi alloy fabricated by laser powder bed fusion. Virtual Phys Prototyping. 2024. https://doi.org/10.1080/17452759.2024.2368654.

[16] Li K, Fang J, Zhan J, Ma R, Wang S, Yang X, Zhang DZ, Murr L, Cao HJ. Elastocaloric effect of laser powder bed fused NiTi alloy with customizable hierarchical heterogeneous microstructure. Addit Manuf. 2025;97:104619. https://doi.org/10.1016/j.addma.2024.104619.

[17] Mousapour M, Kumar SS, Partanen J, Salmi M. 3d printing of a continuous carbon fiber reinforced bronze-matrix composite using material extrusion. Compos B Eng. 2025;289:111961. https://doi.org/10.1016/j.compositesb.2024.111961.

[18] Zhang J, Yuan W, Song B, Yin S, Wang X, Wei Q, Shi YS. Towards understanding metallurgical defect formation of selective laser melted wrought aluminum alloys. Adv Powder Mater. 2022;1(4):100035. https://doi.org/10.1016/j.apmate.2022.100035.

[19] Sui S, Chew Y, Hao Z, Weng F, Tan C, Du Z, Bi GJ. Effect of cyclic heat treatment on microstructure and mechanical properties of laser aided additive manufacturing Ti–6Al–2Sn–4Zr–2Mo alloy. Adv Powder Mater. 2022;1(1):100002. https://doi.org/10.1016/j.apmate.2021.09.002.

[20] Li GC, Cheng X, Wang HM. Microstructure and property of laser additive manufactured alloy Ti–6Al–2V–1.5Mo–0.5Zr–0.3Si after aged at different temperatures. Rare Met. 2024;43(5):2275–81. https://doi.org/10.1007/s12598-018-1188-6.

[21] Wang JC, Liu YJ, Liang SX, Zhang YS, Wang LQ, Sercombe TB, Zhang LC. Comparison of microstructure and mechanical behavior of Ti-35Nb manufactured by laser powder bed fusion from elemental powder mixture and prealloyed powder. J Mater Sci Technol. 2022;105:1–16. https://doi.org/10.1016/j.jmst.2021.07.021.

[22] Wei C, Gu H, Gu Y, Liu L, Huang Y, Cheng D, Li ZQ, Li L. Abnormal interfacial bonding mechanisms of multi-material additive-manufactured tungsten–stainless steel sandwich structure. Int J Extrem Manuf. 2022;4(2):25002. https://doi.org/10.1088/2631-7990/ac5f10.

[23] Saleh B, Jiang J, Fathi R, Al-hababi T, Xu Q, Wang L, Song D, Ma AB. 30 Years of functionally graded materials: an overview of manufacturing methods, applications and future challenges. Compos B Eng. 2020;201:108376. https://doi.org/10.1016/j.compositesb.2020.108376.

[24] Guo H, Liu D, Xu M, Dong Z, Zhang L. Preparation, characterization and composition optimization design of laser powder bed fusion continuously graded Invar36/316L stainless steel alloys. Mater Charact. 2024;209:113709. https://doi.org/10.1016/j.matchar.2024.113709.

[25] Sun Z, Tang C, Soh V, Lee C, Wu X, Sing SL, Liu AZ, Wei SY, Zhou K, Tan CC, Wang P, Chua CK. Laser powder bed fusion of 316L stainless steel and K220 copper multi-material. Virtual Phys Prototyping. 2024. https://doi.org/10.1080/17452759.2024.2356078.

[26] Wei C, Li L, Zhang X, Chueh YH. 3D printing of multiple metallic materials via modified selective laser melting. CIRP Ann. 2018;67(1):245–8. https://doi.org/10.1016/j.cirp.2018.04.096.

[27] Guan S, Wan D, Solberg K, Berto F, Welo T, Yue TM, Chan KC. Additively manufactured CrMnFeCoNi/AlCoCrFeNiTi0.5 laminated high-entropy alloy with enhanced strength-plasticity synergy. Scripta Mater. 2020;183:133–8. https://doi.org/10.1016/j.scriptamat.2020.03.032.

[28] Tan C, Chew Y, Weng F, Sui S, Ng FL, Liu T, Bi GJ. Laser aided additive manufacturing of spatially heterostructured steels. Int J Mach Tools Manuf. 2022;172:103817. https://doi.org/10.1016/j.ijmachtools.2021.103817.

[29] Zheng M, Li C, Ye Z, Zhang X, Yang X, Wang Q, Gu JF. Strength-ductility synergy of additively manufactured (CoCr-Ni)87Al13 medium entropy alloy with heterogeneous multiphase microstructure. Scripta Mater. 2023;222:115016. https://doi.org/10.1016/j.scriptamat.2022.115016.

[30] Yan YG, Lu D, Wang K. Overview: recent studies of machine learning in phase prediction of high entropy alloys. Tungsten. 2023;5(1):32–49. https://doi.org/10.1007/s42864-022-00175-0.

[31] Zhang HT, Wang CL, Miao JW, Shi SY, Li TJ, Yan HW, Zhang YA, Lu YP. Effect of microstructure evolution on wear resistance of equal molar CoCrFeNi high-entropy alloy. Rare Met. 2023;42(11):3797–805. https://doi.org/10.1007/s12598-023-02384-z.

[32] Tan Z, Jiang X, Xi Z, Zhou Z, Wang B, Li G, He DY. Fabrication of Zr-based bulk metallic glass lattice structure with high specific strength by laser powder bed fusion. Addit Manuf. 2024;95:104556. https://doi.org/10.1016/j.addma.2024.104556.

[33] Zhang R, Yao H, Lin X, Gao J, Guo Z, Gong J, Zhao Y, Tan Z, He DY, Zhou Z. Regulating mechanical properties of laser powder bed fusion manufactured CoCrFeMnNi high-entropy alloy using oversaturated boron doping. Virtual Phys Prototyping. 2025. https://doi.org/10.1080/17452759.2025.2470923.

[34] Bi X, Li R, Liu B, Cheng J, Guan D. A comparative study on anisotropy of additively manufactured CoCrNi medium-entropy alloys by hot isostatic pressing and ultrasonic impact treatment. Mater Des. 2024;240:112871. https://doi.org/10.1016/j.matdes.2024.112871.

[35] Chen L, Bobzin K, Zhou Z, Zhao L, Öte M, Königstein T, Tan Z, He DY. Wear behavior of HVOF-sprayed Al_{0}.6TiCrFeCoNi high entropy alloy coatings at different temperatures. Surface Coat Technol. 2019;358:215–22. https://doi.org/10.1016/j.surfcoat.2018.11.052.

[36] Chen L, Zou S, Zhang H, Sui S, Cao L, Huangfu S, Zhao DK, Chen J, Lu WJ, Bi GJ. Microstructure and fracture behavior of multi-elements strengthened CoCrNi alloy produced by

laser-directed energy deposition. J Alloy Compd. 2025;1011:178461. https://doi.org/10.1016/j.jallcom.2025.178461.

[37] Weng F, Chew Y, Zhu Z, Sui S, Tan C, Yao X, Ng FL, Ong WK, Bi GJ. Influence of oxides on the cryogenic tensile properties of the laser aided additive manufactured CoCrNi medium entropy alloy. Compos B Eng. 2021;216:108837. https://doi.org/10.1016/j.compositesb.2021.108837.

[38] Tong Y, Chen D, Han B, Wang J, Feng R, Yang T, Zhao C, Zhao YL, Guo W, Shimizu Y, Liu CT, Liaw PK, Inoue K, Nagai Y, Hu A, Kai JJ. Outstanding tensile properties of a precipitation-strengthened FeCoNiCrTi0.2 high-entropy alloy at room and cryogenic temperatures. Acta Mater. 2019;165:228–40. https://doi.org/10.1016/j.actamat.2018.11.049.

[39] Zhang DD, Zhang JY, Kuang J, Liu G, Sun J. Superior strength-ductility synergy and strain hardenability of Al/Ta co-doped NiCoCr twinned medium entropy alloy for cryogenic applications. Acta Mater. 2021;220:117288. https://doi.org/10.1016/j.actamat.2021.117288.

[40] Gludovatz B, Hohenwarter A, Thurston KVS, Bei H, Wu Z, George EP, Ritchie RO. Exceptional damage-tolerance of a medium-entropy alloy CrCoNi at cryogenic temperatures. Nat Commun. 2016;7:10602. https://doi.org/10.1038/ncomms10602.

[41] Li K, Yang T, Gong N, Wu J, Wu X, Zhang DZ, Murr L. Additive manufacturing of ultra-high strength steels: a review. J Alloy Compd. 2023;965:171390. https://doi.org/10.1016/j.jallcom.2023.171390.

[42] Mu Y, He L, Deng S, Jia Y, Jia Y, Wang G, Zhai QJ, Liaw PK, Liu CT. A high-entropy alloy with dislocation-precipitate skeleton for ultrastrength and ductility. Acta Mater. 2022;232:117975. https://doi.org/10.1016/j.actamat.2022.117975.

[43] Kumar P, Michalek M, Cook DH, Sheng H, Lau KB, Wang P, Zhang MW, Minor A, Ramamurty U, Ritchie RO. On the strength and fracture toughness of an additive manufactured CrCoNi medium-entropy alloy. Acta Mater. 2023;258:119249. https://doi.org/10.1016/j.actamat.2023.119249.

[44] Zhu Y, Zhang K, Meng Z, Zhang K, Hodgson P, Birbilis N, Weyland M, Fraser HL, Lim S, Peng HZ, Yang R, Wang H, Huang AJ. Ultrastrong nanotwinned titanium alloys through additive manufacturing. Nat Mater. 2022;21(11):1258–62. https://doi.org/10.1038/s41563-022-01359-2.

[45] Manzoni A, Daoud H, Mondal S, van Smaalen S, Völkl R, Glatzel U, Wanderka N. Investigation of phases in Al_{23}Co_{15}Cr_{23}Cu_{8}Fe_{15}Ni_{16} and Al_{8}Co_{17}Cr_{17}Cu_{8}Fe_{17}Ni_{33} high entropy alloys and comparison with equilibrium phases predicted by Thermo-Calc. J Alloy Compd. 2013;552:430–6. https://doi.org/10.1016/j.jallcom.2012.11.074.

[46] Wagih M, Larsen PM, Schuh CA. Learning grain boundary segregation energy spectra in polycrystals. Nat Commun. 2020;11(1):6376. https://doi.org/10.1038/s41467-020-20083-6.

[47] Ito K, Sawada H. First-principles analysis of the grain boundary segregation of transition metal alloying elements in  $ \gamma $Fe. Comput Mater Sci. 2022;210:111050. https://doi.org/10.1016/j.commatsci.2021.111050.

[48] Kamikawa N, Sato K, Miyamoto G, Murayama M, Sekido N, Tsuzaki K, Furuhara T. Stress–strain behavior of ferrite and bainite with nano-precipitation in low carbon steels. Acta Mater. 2015;83:383–96. https://doi.org/10.1016/j.actamat.2014.10.010.

[49] Yoshida S, Bhattacharjee T, Bai Y, Tsuji N. Friction stress and Hall-Petch relationship in CoCrNi equi-atomic medium entropy alloy processed by severe plastic deformation and subsequent annealing. Scripta Mater. 2017;134:33–6. https://doi.org/10.1016/j.scriptamat.2017.02.042.

[50] He JY, Liu WH, Wang H, Wu Y, Liu XJ, Nieh TG, Lu ZP. Effects of Al addition on structural evolution and tensile properties of the FeCoNiCrMn high-entropy alloy system. Acta Mater. 2014;62:105–13. https://doi.org/10.1016/j.actamat.2013.09.037.

[51] Wu J, Guo Y, Wang F, Shang X, Zhang J, Liu Q. A D019 precipitate strengthened laser additively manufactured V and Nb bearing CoCrFeNi based high entropy alloys. Mater Des. 2023;235:112464. https://doi.org/10.1016/j.matdes.2023.112464.

[52] Zhi H, Ma S, Wang Z, Zhang T, Wang Q, Wang T, Wang ZH, Huang QX. Excellent mechanical properties and strengthening mechanisms in ultrathin foils of CoCrNi medium-entropy alloy via accumulative rolling. J Market Res. 2024;28:2326–37. https://doi.org/10.1016/j.jmrt.2023.12.101.

[53] He JY, Wang H, Huang HL, Xu XD, Chen MW, Wu Y, Liu XJ, Nieh TG, An K, Lu ZP. A precipitation-hardened high-entropy

alloy with outstanding tensile properties. Acta Mater. 2016;102:187–96. https://doi.org/10.1016/J.ACTAMAT.2015.08.076.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

Rare Met.
https://doi.org/10.1007/s12598-025-03420-w

RARE METALS

Li-jia Chen and Si-hao Zou have contributed equally to this work.

Supplementary Information The online version contains supplementary material available at https://doi.org/10.1007/s12598-025-03420-w.

L. Chen, L. Cao, H. Zhang, G. Bi*
Institute of Intelligent Manufacturing, Guangdong Academy of Sciences, Guangdong Key Laboratory of Modern Control Technology, Guangzhou 510070, China
e-mail: gj.bi@giim.ac.cn

L. Chen, G. Bi
Key Laboratory of Intelligent Laser Directed Energy Deposition
Additive Manufacturing Technology, China Machinery Industry
Federation, Guangzhou 510070, China

S. Zou, W. Lu*
Department of Mechanical and Energy Engineering, Southern University of Science and Technology, Shenzhen 518055, China
e-mail: luwj@sustech.edu.cn

S. Sui
School of Materials Science and Engineering, Xi'an University of Technology, Xi'an 710048, China

$  \frac{1}{2}  $

L. Chen et al.

1 Introduction

2 Experimental

2.1 Materials, fabrication and mechanical testing

A uniaxial tensile loading experiment was executed utilizing a MTS E45 servo-hydraulic testing system integrated with a Correlated solutions’ optical strain measurement system featuring non-contact digital image correlation (DIC) technology. A 12MP camera (3000 × 4000 pixels) captured strain images at 2 Hz. Testing coupons (25 mm × 6 mm × 4 mm) were extracted via wire cut electrical discharge machining, with tests conducted at a nominal strain rate of 0.6 mm min $ ^{-1} $.

2.2 Microstructural characterization

3 Results

3.1 Microstructures

The TEM graphs, corresponding EDS mapping results, and SAED pattern of the CoCrNi(Al0.6TiFe)0.2 alloys are depicted in Fig. 3. ABF and ADF images in Fig. 3A, B present numerous nanoparticle clusters. The phase identification was conducted, and the SAED pattern shown in Fig. 3C confirms that the alloy primarily exhibits FCC

Figure 4 illustrates the TEM/STEM results of the CoCrNi(Al0.6TiFe)0.4 alloy. In Fig. 4A, irregularly shaped precipitates and nanoparticles are observed. The EDS results in Fig. 4B demonstrate that the precipitates exhibit richness in Al, Ti, and trace amounts of Ni. Meanwhile, the nanoparticles are rich in Al and O, indicating the formation of aluminum oxide during alloy fabrication. Figure 4C, D shows the SAED patterns of the

matrix and the precipitates, revealing that the CoCr-Ni(Al0.6TiFe)0.4 alloys are composed of B2 phase and FCC phase. The finding of phase composition is consistent with EBSD phase analysis (Fig. 1). It can be deduced that B2 phase precipitated from the LAAMed alloys when the content of BCC-structured powders in raw powders is more than 40 wt%.

3.2 Mechanical properties

TEM findings of the CoCrNi(Al0.6TiFe)0.5 alloy after deformation are illustrated in Fig. S4. Compared to CoCrNi(Al0.6TiFe)0.4 alloy, bigger precipitated B2 phases around FCC matrix are observed, which are ascribed to the microstructure-tunable LAAM strategy. High-density dislocations are observed on the FCC matrix side, implying

4 Discussion

4.1 Phase formation and microstructural evolution

In the above analyses, the phase composition of the alloys (Fig. 1) and different chemical composition of B2 phase (Fig. 4) with BCC-structured powder demonstrate that the raw powders are fully mixed and melted during the AM process. This demonstrated that B2 precipitates in CoCr-Ni(Al0.6TiFe)0.4 and CoCrNi(Al0.6TiFe)0.5 alloys

the FCC phase [45]. For CoCrNi(Al0.6TiFe)0.4 and CoCrNi(Al0.6TiFe)0.5 alloys, however, B2 phase increases to about 10% and 20% in thermal-calc diagram, the high solidification rate is not enough to inhibit their precipitation in fabrication process.

4.2 Tuned mechanical properties via dual-phase microstructure

The mechanical properties are greatly depended on the phase composition and microstructures. In this investigation, CoCrNi(Al0.6TiFe)x alloys with microstructurally diverse characteristics were successfully processed using a dual-powder feeding LAAM technique. In turn, the mechanical properties were tuned by the different phases and microstructures.