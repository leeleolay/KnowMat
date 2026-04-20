DOI: 10.1016/j.ijplas.2024.104137

# Tailoring thickness debit for high-temperature fatigue resistance of Inconel 718 superalloy fabricated by laser powder bed fusion

Tao Ma $ ^{a} $, Bin Zhang $ ^{a,*} $, Li-Ming Lei $ ^{b,*} $, Yuan-Chen Wang $ ^{c} $, Zhu-Man Song $ ^{c} $, Guang-Ping Zhang $ ^{c,*} $

 $ ^{a} $ Key Laboratory for Anisotropy and Texture of Materials, Ministry of Education, School of Materials Science and Engineering, Northeastern University, 3-11 Wenhua Road, Shenyang 110819, PR China

 $ ^{b} $ TaiHang Laboratory, 619 Jicui Street, Tianfu New District, Chengdu 610213, PR China

 $ ^{c} $ Snenyang National Laboratory for Materials Science, Institute of Metal Research, Chinese Academy of Sciences, 72 Wenhua Road, Shenyang 110016, PR China

## ARTICLE INFO

## Keywords

Laser powder bed fusion

Inconel 718

High-temperature

Thickness debit

Fatigue

Heat treatment

## Abstract

The thickness debit often leads to uncertainty regarding the fatigue performance of laser powder bed fusion (LPBF)-fabricated Inconel 718 thin-walled components and restricts the structural design of these components. Aiming to address this issue, fatigue properties of LPBF-fabricated Inconel 718 homogenized at various temperatures were investigated at 650 ^\circC using specimens with different thicknesses. The results reveal a pronounced influence of both the thickness debit and the intricate interplay between the microstructural and geometrical scales of the thin-walled specimens on their fatigue life at 650 ^\circC. The fatigue life of the thin-walled specimens with the same microstructural scale reduces with decreasing the ratio (t/d) of the specimen thickness (t) to the grain length (d). The coupling effect is described by a mechanism model correlated with the geometrical and microstructural scales of the specimens, in which continuous damage mechanics (CDM) and calculation of the yield strength have been considered. Based on the model, a criterion of t/d > 6.2 for the LPBF-fabricated Inconel 718 specimens homogenized at 1100 ^\circC, and t/d > 8.8 for those homogenized at 1065 ^\circC are proven to be satisfied to ensure a longer and more stable fatigue life of the thin-walled specimens serving at 650 ^\circC. Elevating the homogenization temperature from 1065 ^\circC to 1100 ^\circC results in an extension of the fatigue life for specimens of the same thickness. This enhancement is attributed to the improved ability of grains to coordinate local deformation, as well as the reduced prevalence of elongated Laves and other phases, which typically serve as preferential sites for crack initiation and propagation. The finding suggests that the thickness debit in high-temperature fatigue resistance of LPBF-fabricated components can be minimized by tailoring the heat treatment strategy.

## 1. Introduction

Laser powder bed fusion (LPBF), an additive manufacturing (AM) technology, has gained wide attempts and applications in the industry due to its high fabrication precision and suitability for manufacturing complex-shaped components with small geometrical dimensions. These components include aero-engine turbine rotor blades with complex internal hollow thin-walled structures, as well

as oxygen-hydrogen micromixers with intricate channels. However, mechanical properties of different zones within a complex-shaped component, particularly those with thin-walled structures, can vary significantly, with a wall thickness ranging from 2 mm to several hundreds of micrometers. A decrease in thickness typically leads to a reduction in fatigue life or creep resistance, a phenomenon known as “thickness debit” (Cassenti and Staroselsky, 2009; Li et al., 2022c; Lv et al., 2022; Yu et al., 2020; Zhang et al., 2023). This is primarily influenced by the wall thickness and the microstructure of the component (Ahmad et al., 2022; Carpinteri, 1989; Dai et al., 2013b, 2011; Fang et al., 2014; Hanlon et al., 2003; Hatanaka et al., 1983; Järvenpää et al., 2014; Liu et al., 2017; Ma et al., 2018; Shukla et al., 2018; Sumigawa et al., 2018; Tomaszewski, 2020; Wan et al., 2021; Xu et al., 2014; Yan et al., 2020; Yang et al., 2022; Zheng et al., 2022).

Regarding the thickness debit in fatigue properties, it is always related to the so-called “size effect” on fatigue properties. It has been well-accepted that the smaller the geometrical size of a component (or specimen), the fewer defects would exist. As a result, this would decrease the probability of failure and increase fatigue limit/life, which has been proved by the investigation of homogeneous steel and faulty steel specimens with diameters ranging from 8 to 40 mm (Carpinteri, 1989; Carpinteri et al., 2002, 2009; Findley, 1972; Gaenser, 2008; Hatanaka et al., 1983; Kelly and Morrison, 1970; Phillips and Heywood, 2006; Tridello et al., 2021). However, for the AM processing, more defects, including surface and internal defects, are usually induced into the component, which would degrade fatigue strength and result in a large dispersion of fatigue life of AM-fabricated thin-walled structures (Razavi et al., 2020). To minimize such adverse effects, the surface defects and the rough surface can be minimized by post-processing, including machining, grinding, and polishing, and the internal defects are tried to be eliminated by the hot isostatic pressing (HIP) (Ahmad et al., 2022). Nevertheless, for the AM-fabricated thin-walled structures with a length scale ranging from 2 mm to several hundreds of micrometers, fatigue properties of the materials would be influenced by not only defects but also length scales (geometrical and microstructural scales).

For polycrystalline metal materials, the evaluation of the geometrical scale (specimen thickness/diameter, t) and microstructural scale (grain size/phase size, d) is done jointly using a scale ratio (t/d) (Keller and Hug, 2017; Lorenzino and Navarro, 2022; Zhang et al., 2022). This examination aims to assess the coupling effect of geometrical size and microstructure on fatigue properties, which is closely correlated with the number of grains in the cross-section of the specimen or component (Armstrong, 1961; Thompson, 1974). When t is close to d, the fatigue life of the specimens would be strongly dominated by t/d and the weakening effect of surface grains on fatigue properties gradually increases with decreasing t/d (Dai et al., 2013b, 2011; Yang et al., 2022). In addition, the crystal plasticity modeling on the notch fatigue behavior of Inconel 718 also proved that the crack initiation and propagation lives decreases with t/d decreasing under a given loading level (He et al., 2024a, 2024b).

Furthermore, the temperature gradient variation during the LPBF fabrication process can result in different microstructures in various thickness ranges of a component (Li et al., 2022e). As a result, significant attention has been given to the thickness debit in fatigue properties, with a focus on examining the coupling effect of geometrical and microstructural scales on the fatigue resistance of AM-fabricated alloys (Ahmad et al., 2022; Wan et al., 2020, 2021; Yu et al., 2021a). For electropolished LPBF-fabricated Inconel 718 specimens with identical microstructures but varying thicknesses ranging from 1.0 mm to 0.1 mm, Wan et al. found that fatigue life and fatigue limit decrease as the t/d ratio reduces under the same loading condition (Wan et al., 2021). Additionally, they determined a critical scale ratio of t/d = 4 based on the experimental data of fatigue strength measured using various materials at room temperature (RT), below which the fatigue strength would noticeably decrease. A similar trend was also observed when using specimens with thicknesses ranging from 2.5 mm to 0.5 mm (Ahmad et al., 2022), and positive effects were noted on the high-cycle fatigue life of thin-walled specimens subjected to HIP treatment and internal surface machining. In contrast, no significant difference in fatigue behavior or microstructure of the thin-walled specimens with thicknesses of 1~2 mm was reported when using polished LPBF-fabricated 316L specimens (Yu et al., 2021a). A recent study on the fatigue properties of LPBF-fabricated Inconel 718 thin-walled specimens at 650 ^\circC suggests that the fatigue life of the 1.3 mm-thick electropolished specimens was shorter than that of the 3.3 mm ones. This was attributed to the fact that the 1.3 mm-thick specimens had a stronger  $ \langle001\rangle $ texture and experienced larger accumulative cyclic plastic strain compared to the thicker ones (Wan et al., 2020). Nevertheless, the thickness debit in fatigue properties of AM-fabricated superalloys at elevated temperatures remains unclear due to the lack of systematic research in this area. Summarizing these findings, one may question how the thickness debit in 650 ^\circC-fatigue properties of the LPBF-fabricated Inconel 718 specimens varies. What is the critical scale value for such thickness debit in fatigue at elevated temperatures? Furthermore, is there any effective strategy to minimize the thickness debit in high-temperature fatigue properties of the LPBF-fabricated materials?

In this work, LPBF-fabricated Inconel 718 was selected. All the thin-walled specimens with different thicknesses ranging from 0.25 mm to 2.0 mm were taken from a bulk of LPBF-fabricated Inconel 718 alloy, and subjected to homogenization treatment at 1065 ^\circC and 1100 ^\circC. Then, fatigue tests were conducted at 650 ^\circC in air. The coupling effect of geometrical and microstructural scales on the fatigue life was examined. A model was proposed to describe the thickness debit in fatigue life of the LPBF-fabricated Inconel 718 at 650 ^\circC. The corresponding criterion determining the critical scale ratio t/d, and the feasible method to tailoring thickness debit for high fatigue resistance of LPBF-fabricated Inconel 718 components at 650 ^\circC were also suggested.

## 2. Materials and methods

## 2.1. Material and LPBF fabrication

Argon-atomized Inconel 718 powder with a median diameter of  $ D_{50} = 24.10 \, \mu m $ was used as raw material in the LPBF fabrication, whose chemical composition had been presented in our previous work (Ma et al., 2022). An LPBF machine (EOSINT M270D, EOS, Germany) equipped with a Yb fiber laser source was selected to fabricate an Inconel 718 block with dimensions of  $ 60 \, mm \times 45 \, mm \times $

45. mm. The processing parameters including the laser power, scanning speed, hatch spacing, layer thickness, and rotation angle between the successive layers were selected as 285 W, 960 mm/s, 0.100 mm, 0.040 mm, and 67^\circ, respectively, as schematically illustrated in Fig. 1(a). After the LPBF fabrication, the block was heated at 600 ^\circC for 2 h and then cooled in the furnace for stress relief.

## 2.2. Specimen preparation

To get rid of the potential difference in the influence of surface defects, all the thin-walled specimens were wire-electrical-discharge cut from the as-fabricated block at the same height and grouped according to the thickness, as illustrated schematically in Fig. 1(b). Dimensions of the specimens with different thicknesses for fatigue tests are shown in Fig. 1(b). A homogenization temperature of 1065 ^\circC in AMS5664 was selected as one temperature, and the onset temperature 1100 ^\circC of the recrystallization of the AM Inconel 718 alloy was selected as the other one to satisfy the requirement of tailoring grain and precipitate characteristics (Huang et al., 2019). Increasing the homogenization temperature is effective for improving the mechanical properties of Inconel 718, which have already been investigated (Liu et al., 2023; Ma et al., 2022; Taller and Austin, 2022; Zhao et al., 2021, 2020, 2023). Thus, two groups of specimens designated HA1065 and HA1100 were homogenized at 1065 ^\circC and 1100 ^\circC for 1 h, respectively, and then subjected to a two-step aging of 760 ^\circC - 10 h/furnace cooling to 650 ^\circC at 55 ^\circC/h + 650 ^\circC - 8 h/air cooling to RT. Fig. 1(c) shows a schematic illustration of the two heat treatments. After the heat treatment, the tensile specimens with gauge dimensions of 6 mm \times 1.5 mm \times 1.1 mm were ground and electropolished to the thickness of 0.75 mm, and each group of the fatigue specimens to the thicknesses of 0.25, 0.50, 0.75, 1.00, and 2.00 mm, respectively, with a tolerance of \pm 0.05 mm. It is necessary to emphasize that the front surface (X-Z plane) and the side surfaces (Y-Z plane) of each specimen were mechanically grounded and electropolished to minimize the effect of surface conditions. The roughness (S_a) of the electropolished surfaces was obtained using the confocal laser scanning microscope (CLSM, Zeiss LSM700) and the average value is 0.121 \pm 0.026 \mum.

## 2.3. Tensile and fatigue testing

The tensile tests were conducted on a self-developed testing machine at a strain rate of  $ 5 \times 10^{-3} \, s^{-1} $ and the loading direction along the BD at  $ 650 \, ^{\circ}C $. The strains were derived based on the digital image correlation technique (Li et al., 2022b; Yang et al., 2021). The axial force-controlled fatigue tests were performed along the BD on an Instron 8862 with a stress ratio of 0.1 and frequency of 1 Hz. The specimen clamped between the grips shown in the previous work (Wan et al., 2020) was heated to  $ 650 \, ^{\circ}C $ for 25 min and kept for 30 min to ensure a stable displacement. The fatigue tests for each thickness specimen were conducted three times, in accordance with the requirements of ASTM E739–23. As for the selection of the stress amplitude, two points were taken into account. In the evaluation of mechanical performance indicators, a component (or a specimen) should first be tested at the stress levels close to the yield stress and the service stress. It is known that once plastic deformation appears in the component, the damage will quickly accumulate. Thus, the testing at the stress levels close to the yield stress is more urgent. Here, the maximum stress was set below but close to the yield strength during the fatigue loading to minimize the initial plastic deformation. According to the load fluctuation range ( $ \pm 6.7 $ MPa) and the yield strength of the HA1065 and HA1100 specimens (1067.6 MPa and 1109.8 MPa shown in Section 3.4 respectively), the maximum stress was set as 900 MPa (the value is 85 % of the lower yield strength 1067.6 MPa) and the corresponding stress amplitude is 405 MPa. In addition, to minimize the influence of oxidation, fatigue testing time corresponding to the measured fatigue life of all the specimens needs to be relatively short. When the stress amplitude was set as 405 MPa, the fatigue life of the machined specimens treated by HA1065 was lower than  $ 10^{4} $ cycles (approximately 2.8 h) according to our previous report (Wan et al., 2020). For the smooth LPBF-fabricated Inconel 718 specimen with a grain size of  $ \sim 50 $  $ \mu $m, when the oxidation time in the air is shorter than 3 h, the specific mass gains are lower than  $ 0.007 \, mg \cdot cm^{-2} $ at  $ 600 \, ^{\circ}C $ and  $ 0.02 \, mg \cdot cm^{-2} $ at  $ 700 \, ^{\circ}C $, respectively (Juillet et al., 2018), which is too low for oxidation level to be a significant influence on the surface roughness. Thus, a stress amplitude of 405 MPa was selected in
Fig. 1. Schematic illustration of (a) laser scanning strategy, (b) building direction (BD), grouping, and dimensions of fatigue thin-walled specimens, and (c) heat treatment schedule.

this work. In this case, it should be pointed out that the experiments were within a high-cycle fatigue regime at high-stress level.

## 2.4. Characterization of microstructure

To fully detect defects in the as-fabricated block, five cylindrical specimens with a radius and height of 1.32 and 2.64 mm, respectively, were cut from the interior and four corners of the sampling region in the LPBF-fabricated Inconel 718 block. Sizes and distribution of defects in the as-cut cylindrical specimen were detected by a 3D X-ray tomography (3D-XRT, Versa XRM-500) system. With a voxel size of 3.02 \mum, 996 projected images were collected along the Z axis to be further reconstructed into 3D topography of defects by commercial software (Avizo fire version 7.1). Quantitative data, including the size, morphology, and coordinates of defects, were obtained. To ensure the validity of the data, here only defects with an equivalent diameter larger than 9.06 \mum (3 times the voxel size (Wu et al., 2021)) were used in the analysis. Besides, the grain morphology and orientation were characterized using an electron backscatter diffraction (EBSD, TSL-OIM) system mounted on a field-emission scanning electron microscope (FE-SEM, LEO Supra 35). The step size of the EBSD analysis was 2 \mum. Metallographic specimens were ground, mechanically polished, and etched in a solution of 80 ml HCl, 80 ml CH₃CH₂OH, and 6 g CuSO₄•5H₂O. The grain morphology and orientation of each specimen were obtained at least three times. The microstructure and fracture surface morphology were observed by using the FE-SEM.

## 3. Results

## 3.1. Examination of internal pores

A typical 3D-XRT image of the pores in the cylindrical specimen indicates that many spherical pores are uniformly distributed, as presented in Fig. 2(a). The equivalent diameter  $ \phi $ and the sphericity  $ \psi $ of the pores were calculated by

 $$ \phi=\sqrt[3]{6V/\pi} $$ 

 $$ \psi=\sqrt[3]{36\pi V^{2}}\Big/S $$ 

where V and S are the pore volume and surface area, respectively. The frequency distribution of the equivalent diameters and the corresponding sphericity are shown in Fig. 2(b). In general, the closer the sphericity is to 1, the more spherical the pore shape (Sanaei and Fatemi, 2020). Fig. 2(b) shows that all the pores have a sphericity greater than 0.8, indicating the pores in the XRT specimen are near-spherical gas pores. In addition, there are 95 % of the pores have an equivalent diameter of < 24 µm, which means that the size of most pores is small. Then, according to the volume of all the pores and the XRT specimen, the porosity is 0.01 % and the calculation density of the specimen is 99.99 %.

## 3.2. Grain characteristics

Typical morphology and grain orientation in the X-Y and Y-Z planes of the HA1065 and HA1100 specimens are shown in Fig. 3(a) and (c), respectively. The HA1065 specimen consists of epitaxial columnar and V-shaped grains, while the HA1100 one only has relatively equiaxed grains due to the recrystallization and grain growth. To display the grain orientation distribution of the HA1065 specimen, approximately 94 % of grains in Fig. 3(b) were divided into four types,  $ \langle001\rangle $,  $ \langle101\rangle $,  $ \langle111\rangle $ and  $ \langle112\rangle $, which were color-coded based on the misorientation between the BD and the grain orientation. A small number of columnar grains with  $ \langle001\rangle//BD $ and a large amount of V-shaped grains with  $ \langle101\rangle//BD $ are distributed alternately. There are lots of annealing twins in the HA1100 specimen, as highlighted by the red lines in Fig. 3(d).

In addition, to evaluate the grain size in the X-Y plane normal to the loading direction, the grain shape needs to be taken into
Fig. 2. (a) 3D-XRT image of internal pores in a specimen cut from the interior of Inconel 718 block, (b) frequency distribution of equivalent diameter and corresponding sphericity.
Fig. 3. Grain orientation maps in the X-Y and Y-Z plane of (a) HA1065 and (c) HA1000 specimens, (b) grain distribution with different orientations in HA1065 specimens, and (d) annealing twins in HA1100 specimens.

account. Here, it should be noted that the grain orientation maps in the Y-Z plane instead of the X-Y plane were used to quantify the equivalent diameter of each grain because the characterization in the X-Y plane of the HA1065 specimen cannot display the true shape of the grains and cannot be used for the effective grain size. In addition, considering the rotation angle of 67^\circ between the successive layers, the microstructure in any plane parallel to BD should be similar. There is no obvious difference in the grain morphology and orientation between the X-Z and Y-Z planes. What’s more, the Y-Z plane is parallel to the thickness direction of the specimen, which helps to understand the basic meaning of t/d — the number of grains along the thickness direction of the specimen. Thus, the grain orientation maps in the Y-Z plane were selected to obtain grain size. The area-weighted grain diameter of the HA1065 and HA1100 specimens was obtained using the same method as the previous work (Ma et al., 2022), which was described as  $ d = \sum_{i=1}^{n} d_i P_i $. With the grain shape taken into account, it is reasonable that the equivalent grain diameter  $ d_i $ was defined as an average value obtained by measuring the length at 2^\circ intervals while passing through the centroid of each grain in the Y-Z plane. The area percentage  $ P_i $ of each grain in the Y-Z plane was taken as the weight. The number n is the quantity of the grains (including twins) in the Y-Z plane of three statistical areas. To ensure the size validity, grains with an equivalent diameter of < 6 \mum (3 times the EBSD step size) were eliminated. Then, the area-weighted grain diameter was calculated as  $ d_{HA1065} = 58.5 $ \mum, and  $ d_{HA1100} = 54.1 $ \mum. In addition, abnormal grain growth was induced and resulted in large grains and twins. In general, when the homogenization temperature is higher than 1150 ^\circC, there will be many abnormally grown grains (Chen et al., 2022). Based on the EBSD characterization of different regions, only some normally grown grains exist in the HA1100 specimen. Thus, no special consideration is required for the effect of abnormal grain growth. In addition, to illustrate the difference in grain morphology between the HA1065 and HA1100 specimens, the grain shape aspect ratio (GSAR) was presented in Fig. S_{1} of Supplementary information (SI). Grains with high GSAR in the HA1065 are more than that in the HA1100 specimens.

## 3.3. Precipitate characteristics

Fig. 4(a) and (b) present SEM observations of precipitates in the HA1065 and HA1100 specimens, respectively. The precipitates distributed along the grain boundaries (GBs) in the HA1065 specimen are much more than those in the HA1100 one. As shown in Fig. 4(a), there exist many elongated Laves phases along the dendritic boundaries or irregular particle-like Laves phases at the GBs in the HA1065 specimens, as indicated by the yellow arrows, and many rod-like or needle-like  $ \delta $ phases distributed at the GBs, as indicated by

the red arrows. For the HA1100 specimen, many particle-like carbides pointed by the blue arrows were observed distributing at the GBs, as shown in Fig. 4(b). Notably, the size of many precipitates at GBs in the HA1065 specimen is larger than the spacing among them (see Fig. 4(a)). The statistical results (see Fig. S_{3}(a) and Table S_{1} in SI) show that the spacing between the adjacent precipitates at GBs in the HA1065 specimen is much smaller than that in the HA1100 specimen. The precipitates in the HA1065 specimens are longer but narrower than those in the HA1100 ones. Thus, the aspect ratio of the precipitates in the HA1065 specimens is larger than that in the HA1100 ones, as shown in Fig. S_{3}(b).

In addition, Fig. 5(a) and (b) present TEM bright field images of the HA1065 and HA1100 specimens, respectively. There are few spherical  $ \gamma' $ phases (black arrows) and lots of ellipsoidal  $ \gamma'' $ phases (white arrows). Besides, the  $ \gamma' $ phases often occur in a sandwiched configuration between two  $ \gamma'' $ phases or a side-by-side configuration with a single  $ \gamma'' $ phase, resulting in a difficult differentiation (Phillips et al., 2012; Tucho and Hansen, 2019). In general, for the  $ \gamma''/\gamma' $ phase, the ratio of the volume fraction is about 3~4 and the ratio of the anti-phase boundary energy is about 25 (Zhao et al., 2023). Thus, the weak strengthening effect of the  $ \gamma' $ phase compared with  $ \gamma'' $ is usually ignored and only the strengthening effect of  $ \gamma'' $ phases is taken into account. The statistical results (see Fig. S_{4} and Table S_{1} in SI) show that the average spacing of  $ \gamma'' $ phases in the HA1065 specimen is close to that in the HA1100 specimen, while the average length of  $ \gamma'' $ phases in the former is shorter than that in the latter. The width and volume fraction of  $ \gamma'' $ phases were also obtained based on the calculation method reported previously (Ma et al., 2022), and presented in Table S_{1}. The volume fraction of  $ \gamma'' $ phases in HA1100 specimens is higher than that in the HA1065 specimens.

3.4. Tensile and fatigue properties at  $ 650^{\circ}C $

The tensile engineering stress-strain curves of the HA1065 and HA1100 thin-walled specimens at 650 ^\circC are presented in Fig. 6(a). The average yield strength ( $ \sigma_y $), ultimate tensile strength ( $ \sigma_{uts} $) and fracture elongation ( $ \varepsilon_f $) were 1067.6 \pm 81.1 MPa, 1215.7 \pm 36.6 MPa and 9.1 \pm 1.1 % for the HA1065 specimen and 1109.8 \pm 40.6 MPa, 1222.3 \pm 40.6 MPa and 7.4 \pm 0.2 % for the HA1100 specimen, respectively. In addition, dynamic strain aging characterized by obvious serrations (Prasad et al., 2010) was not observed here. This is likely to be too low a sampling frequency (1 Hz) during tensile loading to capture the serrations. The comparison of the fatigue life ( $ N_f $) of the HA1065 and HA1100 specimens with different scale ratios (t/d) at the stress amplitude ( $ \sigma_a $) of 405 MPa is shown in Fig. 6(b).  $ N_f $ of the HA1100 specimen is longer than that of the HA1065 specimen for the specimens with the same thickness. Moreover, the HA1065 specimens exhibit a trend where  $ N_f $ decreases as the t/d value decreases from 34.5 to 4.5. Similarly, the HA1100 specimens show a decrease in  $ N_f $ as the t/d value decreases from 37.6 to 4.9. Especially, with increasing the homogenization temperature from 1065 ^\circC to 1100 ^\circC, the red dashed-line zone of the  $ N_f $-t/d diagram shifts toward the upper of the blue dashed-line zone, indicating there might be a potential opportunity to tune the sensitivity of the fatigue life to the t/d variation.

Fig. 7 presents a series of data on fatigue life and the scale ratio collected from the recent literature (Li et al., 2022a, 2022d; Liu et al., 2022; Muhammad et al., 2021; Wan et al., 2020, 2021, 2018; Witkin et al., 2020; Yu et al., 2021b; Zhao et al., 2023). The stress ratio of the fatigue test in the literature was converted to  $ R = 0.1 $ by the Goodman relationship. The data set shows a variation trend that  $ N_f $ decreases as the t/d value decreases at room temperature ( $ 25\,^{\circ}C $) and elevated temperature ( $ 650\,^{\circ}C $). There is a steeper descent of the fatigue life at  $ 650\,^{\circ}C $ than that at  $ 25\,^{\circ}C $ with the t/d value decreasing, which is caused by the more serious degradation of microstructure at elevated temperatures. Also, it should be pointed out the influence of the shape of the specimen cross section on the variation trend. Generally, at the same stress level, the fatigue life of the standard specimen with a circular cross-section is longer than that of the specimen with a rectangular cross-section, resulting from the greater possibility of the stress concentration at the edges. Regardless of the influence of the temperature and the specimen shape, based on the normalized stress level ( $ \sigma_a/\sigma_{uts} $), the variation trend is consistent.

## 3.5. Fractography

The fracture surface morphologies of the HA1065 and HA1100 specimens with  $ t = 0.25 \, mm $ and  $ 2.00 \, mm $ are presented in Fig. 8. Fatigue cracks of all the specimens mainly initiated from the surface, as indicated by the black arrows in Fig. 8(c), (f), (g) and (i). When
Fig. 4. SEM images of precipitates at GBs in (a) HA1065 and (b) HA1100 specimens.
Fig. 5. TEM bright field images of  $ \gamma'' $ phases in (a) HA1065 and (b) HA1100 specimens.
Fig. 6. (a) Tensile engineering stress-strain curves at 650 ^\circC, and (b) comparison of fatigue life at 650 ^\circC of the HA1065 and HA1100 specimens with different ratios of specimen thickness to grain length.

t = 0.25 mm, there is a typical feature of quasi-cleavage fracture in the HA1065 and HA1100 specimens, as shown in Fig. 8(c) and (f). The cracks are initiated from the microstructural defects near the surface with cleavage steps or river-like patterns. When t = 2.00 mm, the crack initiation zones in the HA1065 and HA1100 specimens are relatively flat and exhibit river-like patterns, as shown in Fig. 8(g) and (i). In addition, Fig. 8(b), (e), (h), and (j) show that the fatigue cracks propagated in an intergranular-transgranular mixed mode. In the propagation zones, fatigue striations were formed along the direction indicated by the blue arrows when cracks propagated through grains. It is worth noting that the intergranular fracture regions exhibit a rough surface of dendrite boundaries and precipitates for the HA1065 specimen (see the regions surrounded by red dashed lines in Fig. 8(b) and (h), and the closer observation and the corresponding EDS image in Figs. S_{5} of SI), while smooth surfaces of GBs for the HA1100 specimen (see the regions surrounded by yellow dashed lines in Figs. 8(e) and (j)).

## 4. Discussion

The aforementioned results highlight the thickness debit in the high-temperature fatigue life of the LPBF-fabricated Inconel 718 and the impact of heat treatment. In addition to such complicated coupling effects of geometrical and microstructural scales on the fatigue life of LPBF-fabricated Inconel 718 at 650 ^\circC, it seems that the thickness debit is likely to be tailored. Before addressing these questions, we will first examine the potential impact of oxidation and defects on the thickness debit in fatigue of the specimens.
Fig. 7. Comparison of the fatigue life vs. the scale ratio for the LPBF-fabricated Inconel 718 specimen with different heat treatments (Li et al., 2022a, 2022d; Liu et al., 2022; Muhammad et al., 2021; Wan et al., 2020, 2021, 2018; Witkin et al., 2020; Yu et al., 2021b; Zhao et al., 2023).

Subsequently, we will assess the basic mechanism of the thickness debit in high-temperature fatigue and explore potential strategies to reduce the susceptibility to the thickness debit in fatigue properties.

## 4.1. Effect of oxidation on thickness debit

Regarding the effect of the scale ratio t/d on fatigue life, one may argue that the oxidation during the fatigue test at 650 ^\circC may inevitably influence the fatigue properties of the thin-walled specimens. To minimize the influence of oxidation here, some points have already been taken into consideration, as stated in Section 2.3. It is believed that the existence of the oxide layer will result in the formation of surface microcracks under cyclic loading, which will decrease the resistance to fatigue crack initiation (Cruchley et al., 2015). When the fatigue experiments are conducted at higher temperatures than 650 ^\circC, the oxidation is likely to play a more important role in the oxidation-assisted crack initiation and propagation (Neu and Sehitoglu, 1989a, b). For the crack initiation, Neu et al. indicated that at high temperatures in an oxidation environment particularly at 950 ^\circC and above, the oxidation can reduce the toughness of single-crystal Ni-base superalloys on the surface and ahead of the crack tip, lowering the cracking threshold (Neu, 2019). For the crack propagation, they also proved that the oxidation-fatigue interaction is one of the reasons for Mode I opening crack propagation. The oxidation-fatigue interaction can lead to the \gamma′ degradation rate ahead of the crack tip faster than the fatigue crack propagation rate (Amaro et al., 2016; Kirka et al., 2015; Neu, 2019). After the same oxidation exposure time, the thinner the specimen, the higher the ratio of the oxide layer to the specimen volume, which also means that the thinner specimen has a lower load-bearing capacity and is easier to fracture. However, considering such thinner oxide layer thickness of the specimens with different thicknesses and different heat-treatment states mentioned in Section 4 of SI, it is clear that the oxidation might have no evident influence on the thickness debit in the fatigue life of specimens. A detailed discussion about the oxide layer thickness of the specimens after fatigue testing is given in Section 4 of SI.

## 4.2. Effect of LPBF-induced pores on thickness debit

Here, the 3D-XRT result in Section 3.1 has revealed that the main type of internal defect is the gas pore. Nevertheless, our SEM observations of all the broken specimens reveal that the crack did not initiate from the pores in the specimens, as shown in Fig. 8. According to the 3D-XRT results, the pores are spherical and uniformly distributed in the specimen. Considering that all specimens were taken from the same height and the inside of the Inconel 718 block, it is reasonable that the characteristics of the internal pores in all specimens are similar, including size, type, position and morphology. The heat treatment used in this work did not change the characteristics of the pores. However, the larger the volume, the higher the occurring probability of larger pores (Beretta, 2021; Beretta and Murakami, 1998). The specimen thickness in this work as a scale variable is related to the volume. Thus, it is necessary to determine the effect of pores in specimens with different thicknesses on fatigue properties. Based on the 3D-XRT data mentioned in Section 3.1 and the extreme value method (Beretta and Murakami, 1998), the relationship between the internal pore size and the specimen thickness is established. The calculation is presented in Section 5 of SI. It can be seen in Fig. 9 that there is a little difference in the predicted maximum pore size in the near-surface volume among the specimens with thickness ranging from 0.25 mm to 2.00 mm. Correspondingly, the predicted maximum pore size in the five kinds of specimens are 21.7  $ \mu $m, 22.0  $ \mu $m, 22.3  $ \mu $m, 22.6  $ \mu $m and 23.6  $ \mu $m, respectively. Generally, the smaller the maximum pore size in the specimen, the longer its fatigue life. Moreover, the thinner the specimen, the fewer pores there are, which also leads to a longer fatigue life. Thus, according to the predicted maximum pore size, the
Fig. 8. SEM images of fatigue fracture surfaces of (a)-(c), (g) and (h) HA1065 and (d)-(f), (i) and (j) HA1100 specimens with (a)-(f)  $ t = 0.25 \, mm $ and (g)-(j)  $ t = 2.00 \, mm $, respectively.
Fig. 9. Predicted maximum pore size in specimens with different thicknesses.

fatigue life of the specimens with  $ t = 0.25 \, mm $ should have been longer than that of the specimens with  $ t = 2.00 \, mm $. However, the result is the opposite, suggesting that for the thickness debit, the pore size is the secondary factor and there is a more important factor, the coupling effect of the geometrical and microstructural scales, which will be discussed in the subsequent sections.

It should be addressed that the LPBF-induced defects play a significant role in the degradation of mechanical properties, especially fatigue properties. If the fatigue specimens are directly fabricated by LPBF or cut from different locations of an LPBF-fabricated component, the competition of defects and microstructures will dominate the fatigue fracture. In this case, specimens with different thicknesses may have different sensitivities to the morphology, location, size and number of defects, and type of microstructure tailored by different heat treatments.

## 4.3. Effect of the specimen thickness on fatigue properties

Regarding the decrease in the fatigue life with decreasing specimen thickness (Fig. 6(b)), it is important to note that the fatigue crack initiation resistance should be consistent among specimens with the same microstructural scales, as the grains of specimens with different thicknesses share similar features. Therefore, it is crucial to examine the fatigue crack propagation resistance associated with dislocation-boundary interactions. For specimens subjected to the same heat treatment, the decrease in the specimen thickness means a decrease in the number of grains along the thickness direction, which is also a decrease in t/d. First, when t/d decreases to a critical value or is < 2 (single or oligo-crystal alloy specimen), the surface grains may be less constrained by the interior matrix grains (Ran et al., 2013) and the fatigue crack initiation is affected by strain localization (Wan et al., 2021). In particular, the deformation mechanism of single-crystal alloys is strongly dependent on the crystallographic orientation and the corresponding activated slip system, resulting in strain localization in specific directions (Yu et al., 2013). As the cyclic loading progresses, high plastic strains emerge at the surface grains of the oligo-crystal alloy specimen. Meanwhile, the interior grains, particularly the GBs, exhibit pronounced heterogeneity in slip due to constraints imposed by adjacent grains with varying orientations (Chen et al., 2017; Guan et al., 2017). Under the same test condition, the fewer the grains, the fewer the positions that facilitate the dislocation-boundary interactions, the easier it is for dislocations to escape from the surface due to the large volume fraction of the near-surface zone (Guo et al., 2019), and the more serious the strain localization and stress concentrating at the GB triple junctions near the free surface proved by the full-field crystal plasticity simulations of Zhang et al. (Zhang et al., 2018). Second, when t/d is high, especially higher than a critical value, the strain localization of the surface grains is no longer a main factor dominating fatigue life. There is a higher possibility of dislocations being pinned or immobilized by GBs in the large interior zone (Guo et al., 2019). In this case, once the cracks initiate, the crack propagation resistance is mainly affected by the GB at the crack tip. The GBs act not only the barriers to dislocation motion but also play a role in the deflection and branching of the crack. Under the same test condition, the fewer grains, the weaker the deflection and branching role by GBs in the thickness direction, and the weaker the crack propagation resistance. It has been also proved by the study on the fatigue crack propagation of cast Inconel 713C standard specimens with different grain sizes at 650 ^\circC (Liu et al., 2020). The crack propagation rate increases with decreasing t/d due to the frequent change in crack propagation directions rather than being dominated only by dislocation accumulation at the GBs.

## 4.4. Effects of microstructure on fatigue properties

For the specimens with the same thickness, one can find that the fatigue life of the HA1100 specimens is higher than that of the HA1065 ones, as shown in Fig. 6(b). This may be attributed to the difference in microstructures in the specimens due to different heat treatment conditions.

First, there is a difference in grain orientations. Based on the color-coded grains in Fig. 3(b), the microstructure in the HA1065 specimen mainly consists of a small number of columnar grains with  $ \langle001\rangle/ $BD and a large number of V-shaped grains with  $ \langle101\rangle/ $BD. The corresponding Schmid factors of the  $ \{111\}\langle101\rangle $ slip systems were 0.41~0.5 and 0.25~0.5, respectively (Ma et al., 2020). There is an incompatibility in deformation between the two types of grains, leading to poor deformability and intergranular fractures at dendrite boundaries or GBs (Fig. 8(b) and (h)). In the case of the HA1100 specimen, twin boundaries (TBs) play a dual role. The ability of dislocations to traverse TBs is influenced by the grain/twin interplanar angle, which is quantified by the Luster-Morris parameter (LMP). A detailed study on low cycle fatigue (LCF) crack propagation in Haynes 282 alloy (Barat et al., 2022) demonstrates that grain/twin pairs with a high LMP facilitate fatigue crack propagation, while those with a low LMP exhibit slip blocking, ultimately leading to crack arrest. On the one hand, crack initiation parallel to the TB is associated with high resolved shear stress on shared slip systems between twin and parent grains. Pollock et al. (Miao et al., 2009, 2012; Pinz et al., 2022; Stinville et al., 2016) reported that fatigue cracks have been observed initiating parallel to the TBs in René 88DT. On the other hand, cyclic strain localization and cracking at GBs can be effectively mitigated by these special boundaries, resulting in higher resistance to GB cracking and enhanced compatibility in deformation (Guan et al., 2022). In this study, the HA1100 specimen, compared to the HA1065 specimen, exhibits a statistically random orientation of grains, which does not show a specific tendency toward TB cracking. Therefore, it is essential to consider enhancing the capacity of TBs to accommodate local deformation. The weakened dislocation pile-up at TBs may effectively reduce the tendency of GB cracking (Guan et al., 2022; Lu et al., 2012). Besides, TBs interrupted the connectivity of the random GBs (Holland et al., 2018; Ma et al., 2022; Watanabe, 1994), which shortened the propagation paths of GB cracks. Therefore, these may contribute to the fatigue resistance of the HA1100 specimens being higher than that of the HA1065 ones.

Second, there are differences in the type, quantity, size and morphology of the precipitates between the HA1065 and HA1100 specimens. For the HA1065 specimen, there are not only lots of long-striped Laves and rod-like  $ \delta $ phases at GBs, but also many elongated Laves phases along the dendritic boundaries, as shown in Fig. 4(a). Based on the closer observation and the corresponding

EDS image (Fig. S_{5} of SI), there are many Laves and  $ \delta $ phases distributed on the dendrite boundaries and GBs. It is known that these brittle phases are preferential sites for crack nucleation (Cui et al., 2023; Mukherjee et al., 2019). After increasing the homogenization temperature to 1100 ^\circC, the large-sized Laves and  $ \delta $ phases dissolved into the matrix and more carbides became coarsened. The precipitates at the specimen surface are the stress concentration sites, then the cracks will initiate at the boundaries between the precipitate and the matrix because of the debonding. If the half-length of the cracks is considered as the length of the precipitates, the stress concentration factor  $ K_{t} $ can be calculated by

 $$ K_{t}=1+2\sqrt{h/\rho} $$ 

where h and  $ \rho $ are the depth and the half-width of the stress concentration site, respectively. For simplicity, the half of the aspect ratio  $ r_{p} $ shown in Table S_{1} can be used as  $ h/\rho $. Then, the frequency distribution of  $ r_{p} $ shown in Fig. S_{2}(b) is also the frequency distribution of  $ K_{t} $. It can be seen that the average  $ K_{t} $ of the HA1065 specimen is higher than that of the HA1100 specimen. Moreover, the former has more precipitates than the latter, thus the HA1065 specimens are more prone to initiate cracks and have a shorter fatigue life than the HA1100 specimens. This may be the second reason for the fatigue resistance of the HA110 specimens higher than that of the HA1065 ones.

## 4.5. Coupling effect of geometrical and microstructural scales on fatigue properties

To reveal the coupling effect of the geometrical and microstructural scales and the corresponding fatigue damage mechanism, the relationship between  $ N_{f} $ and the scale ratio (t/d) was established. In general, the fatigue damage of the superalloy at elevated temperatures is mainly attributed to some factors, such as the oxide layer cracking at the specimen surface (Hu et al., 2018; Li et al., 2022c; Srivastava and Needleman, 2013; Yu et al., 2020), the oxidation-induced near-surface precipitate-free zone (Hu et al., 2018; Li et al., 2022c; Srivastava and Needleman, 2013; Yu et al., 2020), the existence of the defects (Nadot, 2022; Sanaei and Fatemi, 2020), the coarsening of strengthening phases (Han et al., 1982; Murchú et al., 2017; Oruganti et al., 2011) and the creep damage (Mukherjee et al., 2022). These factors together would lead to a decrease in the fatigue resistance of the specimen. The fatigue accumulation damage is usually estimated based on the CDM (Chaboche, 1988; Zhang et al., 2023) by

 $$ d D=D^{-\alpha}\Big[\frac{\Delta\sigma}{M(\overline{\sigma})}\Big]^{\beta}d N $$ 

where $D$ is the fatigue damage, $\Delta\sigma$ is the stress amplitude. According to the different calculations of $\alpha$ (Chaboche and Lesne, 1988), the $\alpha$ value decreases with increasing the maximum stress and temperature. The function $M(\bar{\sigma})$ is described as a linear dependency on the mean stress and the fatigue limit (Chaboche and Lesne, 1988), and its value decreases with increasing the mean stress and the fatigue limit ($R = -1$). The exponent $\beta$ is the temperature-dependent material constant. Since the stress amplitude and temperature in this work are 405 MPa and 650 ^\circC, respectively, $\left[\frac{\Delta\sigma}{M(\bar{\sigma})}\right]^{\beta}$ can be regarded as a constant $k$. Thus, Eq. (4) becomes into:

 $$ d D=k D^{-\alpha}d N $$ 

The decrease in the yield stress results from the damage causes mentioned above, which acts as the damage parameter D and is defined as:

 $$ D=\frac{\sigma_{cy}-\sigma}{\sigma_{cy}}=1-\frac{\sigma}{\sigma_{cy}} $$ 

where  $ \sigma $ and  $ \sigma_{cy} $ are the transient and initial cyclic yield stresses, respectively. The damage parameter D represents the combined influence of oxidation, defects, size effects and other factors. Then, D = 0 at N = 0 (the beginning of the fatigue test) and  $ D = D_{cri} $ at N = N_f (the number of cycles to fatigue failure). Here, the critical value  $ D_{cri} $ is expressed as:

 $$ D_{cri}=1-\frac{\sigma_{max}}{\sigma_{cy}} $$ 

where  $ \sigma_{max} $ is the maximum stress at fatigue cyclic loading. When the transient cyclic yield stress is reduced to the maximum stress due to the continuous accumulation of damage, the local yield in the specimen will be transformed into the overall yield of the specimen, eventually leading to failure. Thus,  $ N_{f} $ can be obtained by integrating Eq. (5) as follows,

 $$ N_{f}=\frac{1}{k(1+\alpha)}\bigg(1-\frac{\sigma_{max}}{\sigma_{cy}}\bigg)^{1+\alpha} $$ 

Then, it is necessary to clarify the relationship between the initial cyclic yield stress  $ \sigma_{cy} $ and t/d. Here,  $ \sigma_{cy} $ is proportional to the monotonic yield strength  $ \sigma_{y} $, which depends on the stress ratio R. Due to R = 0.1,  $ \sigma_{cy} $ was approximately equal to  $ \sigma_{y} $. Then, according to the work of Dai et al. (Dai et al., 2013a), considering the weakening of surface grains,  $ \sigma_{y} $ can be estimated based on the rule of mixture:

 $$ \sigma_{y}=\left(1-\frac{2h}{t}\right)\sigma_{y,in}+\frac{2h}{t}\sigma_{y,sur} $$

where  $ \sigma_{y,in} $ and  $ \sigma_{y,sur} $ are the contributions of the interior grain and the surface grain to  $ \sigma_{y} $, respectively. Here, h represents the thickness of the surface grain layer and is proportional to the grain size (h = xd). To quantify the thickness of the surface grain layer h, the calculated value of the characteristic width of the GB-affected region ( $ l_{Gbar} $) was used to replace the value of h (Wang et al., 2023), which is estimated by:

 $$ l_{Gbar}\approx\frac{k_{HP}R^{3/2}}{\sqrt{2}M G b} $$ 

where  $ k_{HP} $ is the Hall-Petch coefficient, M is the Taylor factor (M = 3.06), R is the distance between the pinning points of the source (R  $ \approx $  $ 10^{3}b $), and b is the Burgers vector (b = 0.256 nm for nickel). Here, the Hall--Petch coefficient is controlled by the temperature dependence of the shear modulus (G) (Schneibel and Heilmaier, 2014) and is given by

 $$ k_{HP}(T)=\left[\frac{G(T)}{G(T_{0})}\right]^{1/2}k_{HP}(T_{0}) $$ 

where T is the transient temperature and in this work. The relationship between Young’s modulus E and the temperature T is given by (Rösler et al., 2007):

 $$ E(T)=E(T_{0})\left[1+\beta\frac{T}{T_{m}}\right] $$ 

where  $ T_m $ is the absolute melting point ( $ T_m = 1703 $ K for Inconel 718 (Sonar et al., 2021)),  $ \beta $ is the temperature coefficient of the Young’s modulus and  $ \beta = \frac{T_m}{E(T_0)} \frac{dE}{dT} $. The value of  $ G $ can be estimated by  $ E = 2G(1 + \nu) $. Then, with the help of Eq. (12), the Hall--Petch coefficient in Eq. (11) can be written as:

 $$ k_{HP}(T)=\left[1-\frac{T_{m}}{E(T_{0})}\frac{dE}{dT}\frac{T}{T_{m}}\right]^{1/2}k_{HP}(T_{0}) $$ 

where  $ \frac{dE}{dT} $ is regarded as a constant. According to the data in the work of Li et al. (Li et al., 2022d),  $ \frac{dE}{dT} = -0.0556 \text{ GPa} \cdot \text{K}^{-1} $, which was obtained by the linear fitting of Young's modulus at 298 K, 723 K and 923 K. Considering that  $ T_0 $ was set to 298 K in Eq. (13), the value of  $ E $ (298 K) and  $ k_{HP} $ (298 K) are 205.6 GPa (Li et al., 2022d) and 710 MPa  $ \cdot $  $ \mu $m $ ^{-1/2} $ (Sui et al., 2019) for Inconel 718, respectively. Thus,  $ G $ (923 K) = 65.7 GPa,  $ k_{HP} $ (923 K) = 615.0 MPa  $ \cdot $  $ \mu $m $ ^{-1/2} $ and we can obtain  $ l_{Gbar} $ (923 K) = 17.3  $ \mu $m.

Based on the area-weighted grain diameter presented in Section 3.2 and the relation  $ h = l_{Gbar} = xd $, the coefficient x for the HA1065 and HA1100 specimens are 0.30 and 0.32, respectively. Next, a common method to calculate the contribution of different strengthening mechanisms was used to obtain the value of  $ \sigma_{y,in} $ and  $ \sigma_{y,sur} $ in Eq. (9). The overall yield strength of the interior grains contributed by the intrinsic yield strength ( $ \sigma_{0} $) of the nickel-based superalloy, the GB strengthening ( $ \Delta\sigma_{HP} $), the strengthening of  $ \gamma'' $ phases ( $ \Delta\sigma_{\gamma''},or $,  $ \Delta\sigma_{\gamma''},co $,  $ \Delta\sigma_{\gamma''},cli $) and the precipitates at GBs ( $ \Delta\sigma_{p,cli} $) is given by

 $$ \sigma_{y,in}=\sigma_{0}+\left[\Delta\sigma_{HP}^{m}+\Delta\sigma_{\gamma^{\prime \prime},or}^{m}+\Delta\sigma_{\gamma^{\prime \prime},co}^{m}+\Delta\sigma_{\gamma^{\prime \prime},cli}^{m}+\Delta\sigma_{p,cli}^{m}\right]^{1/m} $$ 

For the surface grains, the GB effect ( $ \Delta\sigma_{HP}, \Delta\sigma_{p,cli} $) was removed and the overall yield strength is given by

 $$ \sigma_{y,s u r}=\sigma_{0}+\left[\Delta\sigma_{\gamma^{\prime \prime},o r}^{m}+\Delta\sigma_{\gamma^{\prime \prime},c o}^{m}+\Delta\sigma_{\gamma^{\prime \prime},c l i}^{m}\right]^{1/m} $$ 

Here, the value of the exponent m was selected as 1.17 (Sui et al., 2019). The calculation of each term is presented in Section 6 of SI and their values are listed in Table S2.

Finally, Eq. (13) can be written as:

 $$ \begin{aligned}&N_{f}=\frac{1}{k(1+\alpha)}\left[1-\frac{\sigma_{max}}{\left(1-\frac{2xd}{t}\right)\sigma_{y,in}+\frac{2xd}{t}\sigma_{y,sur}}\right]^{1+\alpha}\\ &\\&=\frac{1}{k(1+\alpha)}\left[1-\frac{\frac{t}{d}\sigma_{max}}{\left(\frac{t}{d}-2x\right)\sigma_{y,in}+2x\sigma_{y,sur}}\right]^{1+\alpha}\\ &\\&=A\left[1-\frac{\frac{t}{d}\sigma_{max}}{\left(\frac{t}{d}-2x\right)\sigma_{y,in}+2x\sigma_{y,sur}}\right]^{B}\\ \end{aligned} $$

where  $ A = \frac{1}{k(1+\alpha)} $ and  $ B = 1 + \alpha $. Now, Eq. (16) can be used to fit the data of the HA1065 and HA1100 specimens in Fig. 6(b), which was replotted in Fig. 10. When the average fatigue life of the specimens is fitted to the model, 67 % of the data points remain within the error band. The error bands for the HA1065 and HA1100 specimens overlap, but they do not coincide. Although the number of specimens is insufficient to establish a reliable fatigue life distribution, there is a noticeable difference in the fitting curves between the HA1065 and HA1100 specimens. Based on the fitting results, the value of  $ k $ and  $ \alpha $ can be obtained:  $ k = 6.25 \times 10^{-8} $ and  $ \alpha = 3.35 $ for the HA1065 specimen and  $ k = 1.84 \times 10^{-27} $ and  $ \alpha = 33.9 $ for the HA1100 specimen. According to Eqs. (4) and (5), the parameters  $ k $ and  $ \alpha $ are related to the experimental condition and the material microstructure. In this work, the experimental condition of all the specimens is the same. Thus, the differences in  $ k $ and  $ \alpha $ between the HA1065 and HA1100 specimens correspond to the difference in the microstructure between the two. Low  $ k $ and high  $ \alpha $ values will reduce the extent of the decrease in  $ N_f $ with decreasing  $ t/d $. Due to the linear dependency between  $ M(\bar{\sigma}) $ and the fatigue limit,  $ k $ can be related to the fatigue limit. The lower the  $ k $ value, the higher the fatigue limit of the specimen. Based on Eq. (4),  $ \alpha $ can be used to describe the damage accumulation rate. The lower the value of  $ \alpha $, the larger the fatigue damage in each cycle. Eq. (16) quantitatively describes the variation of the experimentally-obtained fatigue life with  $ t/d $ of the specimens as well. The physical reason why such a decrease in  $ N_f $ occurs with decreasing the  $ t/d $ value is that the volume fraction of the surface grains increases with decreasing the specimen thickness. During plastic deformation, the surface grains of the specimen lost part of the strengthening ability related to the GBs, mainly including the Hall-Petch strengthening and the Orowan precipitate strengthening.

## 4.6. Tailoring thickness debit for high fatigue resistance through heat treatment

The above analysis presents the variation of fatigue life  $ N_f $ with the scale ratio  $ t/d $ of the thin-walled specimens. Now, we will try to determine critical  $ t/d $ values so that we can find a way to tailor thickness debit for high fatigue resistance through heat treatment. Fig. 11 presents the variation of fatigue life  $ N_f $ with  $ t/d $ of the HA1065 and HA1100 specimens. The diagram can be divided into two regions, i.e. the scale-independent fatigue life region (SIR) where the fatigue life remains stable with decreasing scales, and the size-affected fatigue life region (SAR) where the fatigue life decreases with decreasing scales. The respective two lines are obtained by linear fitting based on the data in a certain range of the SIR and the SAR. Here, considering that the common grain size range of AM-fabricated Inconel 718 is 50~120  $ \mu $m (Hosseini and Popovich, 2019) and the range of the geometrical dimensions for the standard specimen is from 5.08 to 25.4 mm in ASTM E466–07. Thus, the range of the linear fitting for the SIR was selected as  $ t/d = 50 \sim 500 $. But for the linear fitting for the SAR, the range was selected as  $ N_f = 100 \sim 1000 $ cycles with a significant variation of  $ N_f $. Finally, a diagram of the transition between the SIR and the SAR was obtained, as presented in Fig. 11. The steps of determining the critical scale ratio is presented in Section 7 of SI. It is worth noting that the critical  $ t/d $ values for the HA1065 and HA1100 specimens are 8.8 and 6.2, respectively. This indicates that the homogenization temperature changing from 1065 ^\circC to 1100 ^\circC can decrease the critical  $ t/d $ value from 8.8 to 6.2, implying the thickness debit of the specimen can be reduced effectively.

When the geometrical dimension of the specimen or the component changes from standard dimension to miniature dimension, corresponding to the decrease in the t/d value, the fatigue life  $ N_{f} $ will inevitably experience the transition from the SIR and the SAR and then to the sudden drop region. Thus, the critical scale ratio t/d provides a limit for designing LPBF-fabricated thin-walled components, whose geometrical dimensions and grain sizes should be in line with the critical scale ratio. Second, the fact that the critical t/d = 6.2 of the HA1100 specimen at 650 ^\circC is lower than the critical t/d = 8.8 for the HA1065 specimen indicates that the thickness debit can be alleviated by the proper heat treatment. This means that in the case of almost the same grain size, the thickness for the occurrence of the significant thickness debit in the HA1100 specimen is thinner than that of the HA1065 specimen. It is worth noting that the reduction in the t/d ratio from 8.8 (for the HA1065) to 6.2 (for the HA1100) represents an approximate decrease of 30 %. Based on the grain sizes of the HA1065 and HA1100 specimens, their critical thicknesses are 0.515 mm and 0.335 mm, respectively. This reduction in critical thicknesses represents an approximate decrease of 35 %, which is considerable for thin-walled components. In other words, the HA1100 component can be permitted to be fabricated thinner than the HA1065 one without significant thickness debit and the reduction of the fatigue life. This is of great engineering significance that the thickness debit in fatigue resistance for the LPBF-fabricated Inconel 718 may be tailored toward the low critical t/d values, permitting the safety thickness of the AM-fabricated
Fig. 10. Fitting of variation of fatigue life  $ N_{f} $ with scale parameter t/d based on the mechanism-based model.
Fig. 11. Schematic diagram of transition between SIR and SAR.

components to be much thinner. Following such an idea, our heat treatment may provide a reasonable and easy-to-implement strategy to alleviate the thickness debit for the longer fatigue life of LPBF-fabricated Inconel 718. Such a strategy essentially eliminated the chain-like Laves phases and introduced twins and non-aging granular precipitates with a suitable fraction. This would lead to the critical t/d value moving toward the upper left corner of the  $ N_{f}-t/d $ diagram shown in Fig. 11.

Although only two homogenization temperatures were selected in this investigation, the results and discussion have proved the potential effectiveness in tailoring thickness debit and enhancing fatigue resistance. Here, the mechanism-based model was established to describe the coupling effect of geometrical and microstructural scales on fatigue properties of the LPBF-fabricated Inconel 718 at 650 ^\circC, and a feasible method for determining the critical scale ratio t/d was proposed. If more experimental data under different loading and testing conditions could be input to the model for determining the parameters k,  $ \alpha $ and t/d, the ultimate geometrical dimension of the components satisfying the service life would be determined according to the grain size and service condition. Further work will focus on finding out more effective heat treatment for higher fatigue resistance and making the critical scale ratio t/d further move to the upper left corner of the  $ N_f $-t/d diagram. The findings of this work may provide a new perspective for the exploration and establishment of qualification methods for LPBF-fabricated thin-walled components using miniature specimens. What's more, it also has an important reference value for the optimization of geometrical dimensions for LPBF-fabricated thin-walled metal components.

Additionally, we have incorporated the weakening of surface grains into the CDM model, based on the contributions of various microstructures to yield strength. This integration may have significant implications for the synergy and advancement of physics and CDM. The underlying mechanisms should be sound, encompassing the application of CDM, the contribution of each increment to yield strength, and the characteristic width of the GB-affected region. Consequently, we propose that the two parameters, k and  $ \alpha $, represent the effects of different microstructures on fatigue life. It is known that as the homogenization temperature increases from 1065 ^\circC to 1100 ^\circC, the changes in microstructure may include a reduction in harmful phases, a weakening of texture, alterations in grain size, and the introduction of annealing twins. Therefore, while the grain size serves as a variable, the other factors — phases, texture, and annealing twins—also contribute to the two parameters. It is important to emphasize that our model can be applied to materials with texture. We specifically designed both specimens with and without texture, i.e. the HA1065 and HA1100 specimens, respectively. Although texture was not considered during the establishment of the model, its effect on fatigue life is indeed incorporated into the two parameters of this model.

Considering that the experiments are within a high-cycle fatigue regime at high stress level, the  $ N_{f}-t/d $ diagram obtained here may not be applied to all the low and high-cycle fatigue regime. Thus, further works may focus on the  $ N_{f}-t/d $ diagram in the different strain/stress range of low/high-cycle fatigue regime. Furthermore, it is worth mentioning that the specimens utilized in this study were sourced from a Inconel 718 block fabricated via LPBF, polished, and homogenized. When designing the experiment, we minimized the influence of other factors including surface roughness, oxidation, defect features and residual stress. This preparation allows us to explicitly and effectively investigate the pure thickness debit in high-temperature fatigue. Thus, the model we proposed can only be applied under the above limitations at present. If thin-walled specimens of varying thicknesses are directly fabricated by LPBF, numerous uncertain factors may arise, including surface roughness, internal defects, grain size inhomogeneity, and residual stress. These factors, when present simultaneously, significantly complicate the task of elucidating the underlying mechanism. However, the findings of this study underscore the importance of further investigating the fatigue properties of LPBF-fabricated thin-walled components.

## 5. Conclusions

(1) For specimens with the same thickness, the fatigue life of LPBF-fabricated Inconel 718 specimens that underwent homogenization at 1100 ^\circC for 1 hour followed by aging is longer compared to specimens homogenized at 1065 ^\circC for 1 hour and aged. This extended fatigue life can be attributed to the enhanced coordination of local deformation among grains and the decreased occurrence of Laves and \delta phases with larger aspect ratios, which are recognized as initiators of fatigue cracks.

(2) For specimens with the same microstructure scale, the fatigue life decreases as the scale ratio of specimen thickness to grain size decreases. A mechanism-based model for fatigue life as a function of the scale ratio was developed, using CDM and scale-

dependent yield strength. This model effectively describes the coupling effect of geometrical and microstructural scales on the fatigue properties of LPBF-fabricated Inconel 718 at 650 ^\circC.

(3) The critical scale ratio of t/d was determined to illustrate the transition from the scale-independent fatigue life region to the size-affected fatigue life region on the  $ N_f $-t/d diagram. To ensure stable fatigue life at 650 ^\circC, it is recommended that the thin-walled components or specimens of LPBF-fabricated Inconel 718 meet the requirement of t/d > 8.8 for components or specimens homogenized at 1100 ^\circC for 1 hour and aged, and t/d > 6.2 for those homogenized at 1065 ^\circC for 1 hour and aged.

(4) The unavoidable thickness debit in fatigue of the LPBF-fabricated Inconel 718 at 650 ^\circC can be effectively mitigated by appropriately tailoring the heat treatment, such as through homogenization at 1100 ^\circC followed by aging, as demonstrated here.

## CRediT Authorship

Tao Ma: Writing – original draft, Investigation, Formal analysis. Bin Zhang: Writing – review & editing, Supervision, Methodology, Formal analysis, Conceptualization. Li-Ming Lei: Validation, Project administration, Methodology, Data curation. Yuan-Chen Wang: Validation, Investigation. Zhu-Man Song: Validation, Resources. Guang-Ping Zhang: Writing – review & editing, Supervision, Project administration, Funding acquisition, Formal analysis, Conceptualization.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data Availability

Data will be made available on request.

## Acknowledgments

This work was financially supported by the National Key Research and Development Program of China (grant no. 2022YFB4601000), the National Natural Science Foundation of China (NSFC, grant nos. 52171128 and 51971060), and the Postdoctoral Fellowship Program of China Postdoctoral Science Foundation (grant no. GZC20241763).

## Supplementary Materials

## Supplementary Material

## References

Ahmad, N., Shao, S., Seifi, M., Shamsaei, N., 2022. Additively manufactured IN718 in thin wall and narrow flow channel geometries: effects of post-processing and wall thickness on tensile and fatigue behaviors. Addit. Manufact. 60, 103264.

Amaro, R.L., Antolovich, S.D., Neu, R.W., Singh, P.M., 2016. High temperature oxidation and  $ \gamma' $ depletion in the single-crystal superalloy PWA 1484. Mater. High Temp. 33, 476–488.

Armstrong, R.W., 1961. On size effects in polycrystal plasticity. J. Mech. Phys. Solid. 9, 196–199.

Barat, K., Gnosn, A., Donarey, A., Mukherjee, S., Karmakar, A., 2022. Crystallographic evaluation of low cycle fatigue crack growth in a polycrystalline Ni based superalloy. Int. J. Plastic. 149, 103174.

Beretta, S., 2021. 25 years of extreme value statistics for defects: fundamentals, historical developments, recent applications. Int. J. Fatig. 151, 106407.

Beretta, S., Murakami, Y., 1998. Statistical analysis of defects for fatigue strength prediction and quality control of materials. Fatig. Fract. Eng. Mater. Struct. 21, 1049–1065.

Carpinteri, A., 1989. Decrease of apparent tensile and bending strength with specimen size: two different explanations based on fracture mechanics. Int. J. Solid. Struct. 25, 407–429.

Carpinteri, A., Spagnoli, A., Vantadori, S., 2002. An approach to size effect in fatigue of metals using fractal theories. Fatig. Fract. Engng. Mater. Struct. 25, 619–627.

Carpinteri, A., Spagnoli, A., Vantadori, S., 2009. Size effect in S–N curves: a fractal approach to finite-life fatigue strength. Int. J. Fatig. 31, 927–933.

Cassenti, B., Staroselsky, A., 2009. The effect of thickness on the creep response of thin-wall single crystal components. Mater. Sci. Eng.: A 508, 183–189.

Chaboche, J.L., 1988. Continuum damage mechanics: part II-damage growth, crack initiation, and crack growth. J. Appl. Mech. 55, 65–72.

Chaboche, J.L., Lesne, P.M., 1988. A non-linear continuous fatigue damage model. Fatig. Fract. Eng. Mater. Struct. 11, 1–17.

Chen, B., Jiang, J., Dunne, F.P.E., 2017. Microstructurally-sensitive fatigue crack nucleation in Ni-based single and oligo crystals. J. Mech. Phys. Solid. 106, 15–33.

Chen, K., Li, H., Lim, C.H., Jia, N., Yan, W., 2022. Fine grains within narrow temperature range by tuning strain-induced boundary migration dominated recrystallization for selective laser melted Inconel 718. Scr. Mater. 219, 114882.

Cruchley, S., Li, H.Y., Evans, H.E., Bowen, P., Child, D.J., Hardy, M.C., 2015. The role of oxidation damage in fatigue crack initiation of an advanced Ni-based superalloy. Int. J. Fatig. 81, 265–274.

Cui, L.Q., Deng, D.Y., Jiang, S., Peng, R.L., Xin, T.Z., Zhang, H.H., Hegedüs, Z., Liener, U., He, W.F., Moverare, J., 2023. New insights into the anisotropic ductility of additively manufactured Inconel 718. Int. J. Plastic. 169, 103738.

Dai, C.Y., Xu, J., Zhang, B., Zhang, G.P., 2013a. Understanding scale-dependent yield stress of metals at micrometre scales. Philos. Mag. Lett. 93, 531–540.

Dai, C.Y., Zhang, B., Xu, J., Zhang, G.P., 2013b. On size effects on fatigue properties of metal foils at micrometer scales. Mater. Sci. Eng.: A 575, 217–222.

Dai, C.Y., Zhang, G.P., Yan, C., 2011. Size effects on tensile and fatigue behaviour of polycrystalline metal foils at the micrometer scale. Philosoph. Magaz. 91, 932–945.

Fang, H., Shiohara, R., Sumigawa, T., Kitamura, T., 2014. Size dependence of fatigue damage in sub-micrometer single crystal gold. Mater. Sci. Eng.: A 618, Findlev. W.N.. 1972. Research note: an explanation of size effect in fatigue of metals. J. Mech. Eng. Sci. 14. 424–428.

nser, H.-P., 2008. Some notes on gradient, volumetric and weakest link concepts in fatigue. Comput. Mater. Sci. 44, 230–239.

Guan, X.J., Jia, Z.P., Liang, S.M., Shi, F., Li, X.W., 2022. A pathway to improve low-cycle fatigue life of face-centered cubic metals via grain boundary engineering. J. Mater. Sci. Technol. 113, 82–89.

Guan, Y., Chen, B., Zou, J., Britton, T.B., Jiang, J., Dunne, F.P.E., 2017. Crystal plasticity modelling and HR-DIC measurement of slip activation and strain localization in single and oligo-crystal Ni alloys under fatigue. Int. J. Plastic. 88, 70–88.

Guo, S., He, Y., Li, Z., Lei, J., Liu, D., 2019. Size and stress dependences in the tensile stress relaxation of thin copper wires at room temperature. Int. J. Plastic. 112, 278–296.

Han, Y.F., Deb, P., Chaturvedi, M.C., 1982. Coarsening behaviour of \gamma''- and \gamma'-particles in Inconel alloy 718. Metal Sci. 16, 555–562.

Hanlon, T., Kwon, Y.N., Suresh, S., 2003. Grain size effects on the fatigue response of nanocrystalline metals. Scr. Mater. 49, 675–680.

Hatanaka, K., Shimizu, S., Nagae, A., 1983. Size effect on rotating bending fatigue in steels. Bull. JSME 26, 1288–1295.

He, J.C., Zhu, S.P., Gao, J.W., Liu, R., Li, W., Liu, Q., He, Y., Wang, Q.Y., 2024a. Microstructural size effect on the notch fatigue behavior of a Ni-based superalloy using crystal plasticity modelling approach. Int. J. Plastic. 172, 103857.

He, J.C., Zhu, S.P., Luo, C.Q., Li, W., Liu, Q., He, Y., Wang, Q.Y., 2024b. Probabilistic notch fatigue assessment under size effect using micromechanics-based critical distance theory. Int. J. Fatig. 183, 108280.

Holland, S., Wang, X.Q., Fang, X.Y., Guo, Y.B., Yan, F., Li, L., 2018. Grain boundary network evolution in Inconel 718 from selective laser melting to heat treatment. Mater. Sci. Eng.: A 725, 406–418.

Hosseini, E., Popovich, V.A., 2019. A review of mechanical properties of additively manufactured Inconel 718. Addit. Manufact. 30, 100877.

Hu, Y.B., Zhang, L., Cheng, C.Q., Zhao, P.T., Cao, T.S., Guo, G.P., Zhao, J., 2018. Influence of specimen thickness on the creep behavior of a directional solidification nickel-based superalloy. Vacuum 150, 105–115.

Huang, W.P., Yang, J.J., Yang, H.H., Jing, G.Y., Wang, Z.M., Zeng, X.Y., 2019. Heat treatment of Inconel 718 produced by selective laser melting: microstructure and mechanical properties. Mater. Sci. Eng.: A 750, 98–107.

Järvenpää, A., Karjalainen, L.P., Jaskari, M., 2014. Effect of grain size on fatigue behavior of Type 301LN stainless steel. Int. J. Fatig. 65, 93–98.

Juillet, C., Oudriss, A., Balmain, J., Feaugas, X., Pedraza, F., 2018. Characterization and oxidation resistance of additive manufactured and forged IN718 Ni-based superalloys. Corros. Sci. 142, 266–276.

Keller, C., Hug, E., 2017. Kocks-Mecking analysis of the size effects on the mechanical behavior of nickel polycrystals. Int. J. Plastic. 98, 106–122.

Kelly, D.A., Morrison, J.L.M., 1970. Effect of Specimen Size and Preparation on the Fatigue Strength of a Plain Carbon Steel Tested in Rotating Bending and in Torsion. Proc. Instn. Mech. Engr.s. 185, 655–664.

Kirka, M.M., Brindley, K.A., Neu, R.W., Antolovich, S.D., Shinde, S.R., Gravett, P.W., 2015. Influence of coarsened and rafted microstructures on the thermomechanical fatigue of a Ni-base superalloy. Int. J. Fatig. 81, 191–201.

Li, L., Zhu, X., Tian, F., Chen, Y., Liu, Q., 2022a. Effect of annealing treatment on mechanical and fatigue properties of Inconel 718 alloy melted by selective laser melting. Matéria (Rio de Janeiro) 27.

Li, M.Y., Zhang, B., Song, Z.M., Luo, X.M., Zhang, G.P., 2022b. Detecting the deformation behavior of bimodal Ti-6Al-4V using a digital image correlation technique. Mater. (Basel) 15, 7504.

Li, Q., Xie, J., Yu, J.J., Shu, D.L., Hou, G.C., Sun, X.F., Zhou, Y.Z., 2022c. The thin-wall debit of a typical cast polycrystalline M951 alloy. Progr. Nat. Sci.: Mater. Int. 32, 104–113.

Li, W.B., Pang, J.C., Zhang, H., Li, S.X., Zhang, Z.F., 2022d. The high-cycle fatigue properties of selective laser melted Inconel 718 at room and elevated temperatures. Mater. Sci. Eng.: A 836, 142716.

Li, Y., Dlouhý, J., Koukolíková, M., Kirana, A., Vavřík, J., Džugan, J., 2022e. Effect of deposit thickness on microstructure and mechanical properties at ambient and elevated temperatures for Inconel 718 superalloy fabricated by directed energy deposition. J. Alloy. Compd. 908, 164723.

Liu, B., Ding, Y., Xu, J., Wang, X., Gao, Y., Hu, Y., Chen, D., 2023. Achievement of grain boundary engineering by transforming residual stress in selective laser-melted Inconel 718 superalloy. Mater. Sci. Eng.: A 866, 144683.

Liu, G., Winwood, S., Rhodes, K., Birosca, S., 2020. The effects of grain size, dendritic structure and crystallographic orientation on fatigue crack propagation in IN713C nickel-based superalloy. Int. J. Plastic. 125, 150–168.

Liu, M.Q., Liu, Y.L., Yan, Y., Han, D., Li, X.W., 2017. Thickness-dependent tensile and fatigue behavior of a single-slip-oriented Cu single crystal. Cryst. Res. Technol. 52, 1700178.

, Navarro, A., 2022. Influence of the ratio between specimen thickness and grain size on the fatigue and tensile properties of plain and notched m plate specimens. Int. J. Fatig. 164, 107149.

u, K., 2012. Work hardening of polycrystalline Cu with nanoscale twins. Scr. Mater. 66, 837–842.

Lv, J., Zhao, Y., Wang, S., Zhao, X., Zhao, J., Zheng, L., Guo, Y., Schmitz, G., Ge, B., 2022. Stress state mechanism of thickness debit effect in creep performances of a Ni-based single crystal superalloy. Int. J. Plastic. 159, 103470.

Ma, T., Zhang, B., Wang, L.Y., Song, Z.M., Luo, X.M., Liu, C.S., Zhang, G.P., 2020. Anisotropy of small punch creep performance of selective laser melted GH4169 650 ^\circC. Mater. Sci. Eng.: A 806, 140608.

Ma, T., Zhang, G.P., Tan, P., Zhang, B., 2022. Effects of homogenization temperature on creep performance of laser powder bed fusion-fabricated Inconel 718 at 650^\circC. Mater. Sci. Eng.: A 853, 143794.

Ma, Y.F., Song, Z.M., Zhang, S.Q., Chen, L.J., Zhang, G.P., 2018. Evaluation of fatigue properties of CA6NM martensite stainless steel using miniature specimens. Acta Metallurg. Sinica 54, 1359–1367.

Miao, J., Pollock, T.M., Wayne Jones, J., 2009. Crystallographic fatigue crack initiation in nickel-based superalloy René 88DT at elevated temperature. Acta Mater. 57, 5964–5974.

Miao, J., Pollock, T.M., Wayne Jones, J., 2012. Microstructural extremes and the transition from fatigue crack initiation to small crack growth in a polycrystalline nickel-base superalloy. Acta Mater. 60, 2840–2854.

Muhammad, M., Frye, P., Simsiriwong, J., Shao, S., Shamsaei, N., 2021. An investigation into the effects of cyclic strain rate on the high cycle and very high cycle fatigue behaviors of wrought and additively manufactured Inconel 718. Int. J. Fatig. 144, 106038.

Mukherjee, S., Barat, K., Sivaprasad, S., Tarafder, S., Kar, S.K., 2019. Elevated temperature low cycle fatigue behaviour of Haynes 282 and its correlation with microstructure – Effect of ageing conditions. Mater. Sci. Eng.: A 762, 138073.

Mukherjee, S., Kumar Kar, S., Sivaprasad, S., Tarafder, S., Viswanathan, G.B., Fraser, H.L., 2022. Creep-Fatigue Response, failure mode and deformation mechanism of HAYNES 282 Ni based superalloy: effect of dwell position and time. Int. J. Fatig. 159, 106820.

Murchú, C.Ó., Leen, S.B., O'Donoghue, P.E., Barrett, R.A., 2017. A physically-based creep damage model for effects of different precipitate types. Mater. Sci. Eng.: A 682, 714–722.

Nadot, Y., 2022. Fatigue from defect: influence of size, type, position, morphology and loading. Int. J. Fatig. 154, 106531

Neu, R.W., Sehitoglu, H., 1989a. Thermomechanical fatigue, oxidation, and creep: part I. Damage mechanisms. Metallurg. Transact. A 20, 1755–1767.

Neu, R.W., Sehitoglu, H., 1989b. Thermomechanical fatigue, oxidation, and Creep: part II. Life prediction. Metallurg. Transact. A 20, 1769–1783.

Oruganti, R., Karadge, M., Swaminathan, S., 2011. Damage mechanics-based creep model for 9-10%Cr ferritic steels. Acta Mater. 59, 2145–2155.

Phillips, C.E., Heywood, R.B., 2006. The size effect in fatigue of plain and notched steel specimens loaded under reversed direct stress. Proceed. Instit. Mech. Eng. 165, 113–124.

Phillips, P.J., McAllister, D., Gao, Y., Lv, D., Williams, R.E.A., Peterson, B., Wang, Y., Mills, M.J., 2012. Nano \gamma′/\gamma″ composite precipitates in Alloy 718. Appl. Phys. Lett. 100, 211913.

Pinz, M., Weber, G., Stinville, J.C., Pollock, T., Ghosh, S., 2022. Data-driven Bayesian model-based prediction of fatigue crack nucleation in Ni-based superalloys. npj Comput. Mater. 8, 39.

Prasad, K., Sarkar, R., Ghosal, P., Kumar, V., 2010. Tensile deformation behaviour of forged disc of IN 718 superalloy at 650 ^\circC. Mater. Des. 31, 4502–4507.

Ran, J.Q., Fu, M.W., Chan, W.L., 2013. The influence of size effect on the ductile fracture in micro-scaled plastic deformation. Int. J. Plastic. 41, 65–81.

Razavi, N., Van Hooreweder, B., Berto, F., 2020. Effect of build thickness and geometry on quasi-static and fatigue behavior of Ti-6Al-4V produced by Electron Beam Melting. Addit. Manufact. 36, 101426.

Rösler, J., Bäker, M., Harders, H., 2007. Elasticity. In: Rösler, J., Bäker, M., Harders, H. (Eds.), Mechanical Behaviour of Engineering Materials: Metals, Ceramics, Polymers, and Composites. Springer Berlin Heidelberg, Berlin, Heidelberg, pp. 31–62.

Sanaei, N., Fatemi, A., 2020. Defects in additive manufactured metals and their effect on fatigue performance: a state-of-the-art review. Prog. Mater. Sci., 100724 Schneibel, J.H., Heilmaier, M., 2014. Hall-Petch breakdown at elevated temperatures. Mater. Transact. 55, 44–51.

Shukla, S., Komarasamy, M., Mishra, R.S., 2018. Grain size dependence of fatigue properties of friction stir processed ultrafine-grained Al-5024 alloy. Int. J. Fatig. 109, 1–9.

Sonar, T., Balasubramanian, V., Malarvizhi, S., Venkateswaran, T., Sivakumar, D., 2021. An overview on welding of Inconel 718 alloy - effect of welding processes on microstructural evolution and mechanical properties of joints. Mater. Charact. 174, 110997.

Srivastava, A., Needleman, A., 2013. Phenomenological modeling of the effect of specimen thickness on the creep response of Ni-based superalloy single crystals. Acta Mater. 61, 6506–6516.

Stinville, J.C., Lenthe, W.C., Miao, J., Pollock, T.M., 2016. A combined grain scale elastic–plastic criterion for identification of fatigue crack initiation sites in a twin containing polycrystalline nickel-base superalloy. Acta Mater. 103, 461–473.

Sui, S., Tan, H., Chen, J., Zhong, C.L., Li, Z., Fan, W., Gasser, A., Huang, W.D., 2019. The influence of Laves phases on the room temperature tensile properties of Inconel 718 fabricated by powder feeding laser additive manufacturing. Acta Mater. 164, 413–427.

Sumigawa, T., Byungwoon, K., Mizuno, Y., Morimura, T., Kitamura, T., 2018. In situ observation on formation process of nanoscale cracking during tension-compression fatigue of single crystal copper micron-scale specimen. Acta Mater. 153, 270–278.

Taller, S., Austin, T., 2022. Using post-processing heat treatments to elucidate precipitate strengthening of additively manufactured superalloy 718. Addit. Manufact. 60, 103280.

Thompson, A.W., 1974. Use of non-polycrystal specimens in mechanical behavior tests. Scripta Metallurg. 8, 145–147.

Tomaszewski, T., 2020. Statistical size effect in fatigue properties for mini-specimens. Mater. (Basel) 13, 2384.

Tridello, A., Niutta, C.B., Berto, F., Paolino, D.S., 2021. Size-effect in very high cycle fatigue: a review. Int. J. Fatig. 153.

Tucho, W.M., Hansen, V., 2019. Characterization of SLM-fabricated Inconel 718 after solid solution and precipitation hardening heat treatments. J. Mater. Sci. 54, 823–839.

Wan, H.Y., Luo, Y.W., Zhang, B., Song, Z.M., Wang, L.Y., Zhou, Z.J., Li, C.P., Chen, G.F., Zhang, G.P., 2020. Effects of surface roughness and build thickness on fatigue properties of selective laser melted Inconel 718 at 650 ^\circC. Int. J. Fatig. 137, 105654.

Wan, H.Y., Yang, W.K., Wang, L.Y., Zhou, Z.J., Li, C.P., Chen, G.F., Lei, L.M., Zhang, G.P., 2021. Toward qualification of additively manufactured metal parts: tensile and fatigue properties of selective laser melted inconel 718 evaluated using miniature specimens. J. Mater. Sci. Technol. 97, 239–253.

Wan, H.Y., Zhou, Z.J., Li, C.P., Chen, G.F., Zhang, G.P., 2018. Enhancing fatigue strength of selective laser melting-fabricated Inconel 718 by tailoring heat treatment route. Adv. Eng. Mater. 20, 1800307.

Wang, Y.F., Huang, C.X., Ma, X.L., Zhao, J.F., Guo, F.J., Fang, X.T., Zhu, Y.T., Wei, Y.G., 2023. The optimum grain size for strength-ductility combination in metals. Int. J. Plastic. 164, 103574.

Watanabe, T., 1994. The impact of grain boundary character distribution on fracture in polycrystals. Mater. Sci. Eng.: A 176, 39–49.

Witkin, D.B., Patel, D., Albright, T.V., Bean, G.E., McLouth, T., 2020. Influence of surface conditions and specimen orientation on high cycle fatigue properties of Inconel 718 prepared by laser powder bed fusion. Int. J. Fatig. 132, 105392.

Wu, Z.K., Wu, S.C., Bao, J.G., Qian, W.J., Karabal, S., Sun, W., Withers, P.J., 2021. The effect of defect population on the anisotropic fatigue resistance of AlSi10Mg alloy fabricated by laser powder bed fusion. Int. J. Fatig. 151, 106317.

Xu, J., Dai, C.Y., Zhang, B., Zhang, G.P., 2014. Strain-gradient dependent fatigue behavior of micron-thick copper single crystal foils. Comput. Mater. Sci. 85, 223–229.

Yan, Y.B., Sumigawa, T., Wang, X.Y., Chen, W.F., Xuan, F.Z., Kitamura, T., 2020. Fatigue curve of microscale single-crystal copper: an in situ SEM tension-compression study. Int. J. Mech. Sci. 171, 105361.

Yang, W.K., Song, Z.M., Luo, X.M., Zhang, G.P., 2022. Evaluation of tensile and fatigue properties of metals using small specimens. Acta Metallurg. Sinica (Engl. Lett.) 36, 147–157.

Yang, W.K., Wang, L.Y., Song, Z.M., Luo, X.M., Zhang, G.P., 2021. Tensile plasticity of miniature specimens for a low alloy steel investigated by digital image correlation technique. Steel Res. Int. 92, 2000685.

Yu, C.H., Leicht, A., Peng, R.L., Moverare, J., 2021a. Low cycle fatigue of additively manufactured thin-walled stainless steel 316L. Mater. Sci. Eng.: A 821, 141598.

Yu, J., Li, J.R., Zhao, J.Q., Han, M., Shi, Z.X., Liu, S.Z., Yuan, H.L., 2013. Orientation dependence of creep properties and deformation mechanism in DD6 single crystal superalloy at 760 ^\circC and 785MPa. Mater. Sci. Eng.: A 560, 47–53.

Yu, X., Lin, X., Wang, Z., Zhang, S., Gao, X., Zhang, Y., Ren, Y., Huang, W., 2021b. Room and high temperature high-cycle fatigue properties of Inconel 718 superalloy prepared using laser directed energy deposition. Mater. Sci. Eng.: A 825, 141865.

Yu, Z.Y., Wang, X.M., Liang, H., Li, Z.X., Li, L., Yue, Z.F., 2020. Thickness debit effect in Ni-based single crystal superalloys at different stress levels. Int. J. Mech. Sci. 170, 105357.

Zhang, B., Wang, R.Q., Liu, H.Y., Hu, D.Y., Jiang, K.H., Jing, F.L., Mi, D., 2023. Low cycle fatigue lifetime and deformation behaviour prediction of nickel-based single crystal superalloy considering thickness debit effect. Eng. Fract. Mech. 281, 109076.

Zhang, D., Li, H., Guo, X., Yang, Y., Yang, X., Feng, Z., 2022. An insight into size effect on fracture behavior of Inconel 718 cross-scaled foils. Int. J. Plastic. 153, 103274.

Zhang, H., Liu, J., Sui, D., Cui, Z., Fu, M.W., 2018. Study of microstructural grain and geometric size effects on plastic heterogeneities at grain-level by using crystal plasticity modeling with high-fidelity representative microstructures. Int. J. Plastic. 100, 69–89.

Zhao, Y., Meng, F., Liu, C., Tan, S., Xiong, W., 2021. Impact of homogenization on microstructure-property relationships of Inconel 718 alloy prepared by laser powder bed fusion. Mater. Sci. Eng.: A 826, 141973.

Zhao, Y.N., Guan, K., Yang, Z.W., Hu, Z.P., Qian, Z., Wang, H., Ma, Z.Q., 2020. The effect of subsequent heat treatment on the evolution behavior of second phase particles and mechanical properties of the Inconel 718 superalloy manufactured by selective laser melting. Mater. Sci. Eng.: A 794, 139931.

Zhao, Z., Yang, W., Li, L., Sun, S., Zeng, Y., Yue, Z., 2023. Improved high-temperature fatigue performance of laser directed energy deposited Ni-based superalloy by regulating the heat treatment. Int. J. Fatig. 169, 107463.

Zheng, Z.B., Zhan, M., Fu, M.W., 2022. Microstructural and geometrical size effects on the fatigue of metallic materials. Int. J. Mech. Sci. 218, 107058.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

International Journal of Plasticity 182 (2024) 104137

International Journal of Plasticity

## Keywords

Laser powder bed fusion
Inconel 718
High-temperature
Thickness debit
Fatigue
Heat treatment

## ABSTRACT

https://doi.org/10.1016/j.ijplas.2024.104137

0749-6419/© 2024 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

## 45. mm. The processing parameters including the laser power, scanning speed, hatch spacing, layer thickness, and rotation angle between the successive layers were selected as 285 W, 960 mm/s, 0.100 mm, 0.040 mm, and 67^\circ, respectively, as schematically illustrated in Fig. 1(a). After the LPBF fabrication, the block was heated at 600 ^\circC for 2 h and then cooled in the furnace for stress relief.

(1) For specimens with the same thickness, the fatigue life of LPBF-fabricated Inconel 718 specimens that underwent homogenization at 1100 ^\circC for 1 hour followed by aging is longer compared to specimens homogenized at 1065 ^\circC for 1 hour and aged. This extended fatigue life can be attributed to the enhanced coordination of local deformation among grains and the decreased occurrence of Laves and \delta phases with larger aspect ratios, which are recognized as initiators of fatigue cracks.

dependent yield strength. This model effectively describes the coupling effect of geometrical and microstructural scales on the fatigue properties of LPBF-fabricated Inconel 718 at 650 ^\circC.

(4) The unavoidable thickness debit in fatigue of the LPBF-fabricated Inconel 718 at 650 ^\circC can be effectively mitigated by appropriately tailoring the heat treatment, such as through homogenization at 1100 ^\circC followed by aging, as demonstrated here.

## CRediT Authorship

## Declaration of Competing Interest

## Data Availability

## Supplementary Materials

## Supplementary Material

Han, Y.F., Deb, P., Chaturvedi, M.C., 1982. Coarsening behaviour of \gamma''- and \gamma'-particles in Inconel alloy 718. Metal Sci. 16, 555–562.

Ma, T., Zhang, B., Wang, L.Y., Song, Z.M., Luo, X.M., Liu, C.S., Zhang, G.P., 2020. Anisotropy of small punch creep performance of selective laser melted GH4169 650 ^\circC. Mater. Sci. Eng.: A 806, 140608.

Ma, T., Zhang, G.P., Tan, P., Zhang, B., 2022. Effects of homogenization temperature on creep performance of laser powder bed fusion-fabricated Inconel 718 at 650^\circC. Mater. Sci. Eng.: A 853, 143794.

Phillips, P.J., McAllister, D., Gao, Y., Lv, D., Williams, R.E.A., Peterson, B., Wang, Y., Mills, M.J., 2012. Nano \gamma′/\gamma″ composite precipitates in Alloy 718. Appl. Phys. Lett. 100, 211913.

Prasad, K., Sarkar, R., Ghosal, P., Kumar, V., 2010. Tensile deformation behaviour of forged disc of IN 718 superalloy at 650 ^\circC. Mater. Des. 31, 4502–4507.

Wan, H.Y., Luo, Y.W., Zhang, B., Song, Z.M., Wang, L.Y., Zhou, Z.J., Li, C.P., Chen, G.F., Zhang, G.P., 2020. Effects of surface roughness and build thickness on fatigue properties of selective laser melted Inconel 718 at 650 ^\circC. Int. J. Fatig. 137, 105654.

Yu, J., Li, J.R., Zhao, J.Q., Han, M., Shi, Z.X., Liu, S.Z., Yuan, H.L., 2013. Orientation dependence of creep properties and deformation mechanism in DD6 single crystal superalloy at 760 ^\circC and 785MPa. Mater. Sci. Eng.: A 560, 47–53.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

ELSEVIER

Contents lists available at ScienceDirect

journal homepage: www.elsevier.com/locate/ijplas

Keywords:
Laser powder bed fusion
Inconel 718
High-temperature
Thickness debit
Fatigue
Heat treatment

A B S T R A C T

E-mail addresses: zhangb@atm.neu.edu.cn (B. Zhang), bmhdx76@126.com (L.-M. Lei), gpzhang@imr.ac.cn (G.-P. Zhang).

https://doi.org/10.1016/j.ijplas.2024.104137

Received 21 July 2024; Received in revised form 13 September 2024;

Available online 23 September 2024

0749-6419/© 2024 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

T. Ma et al.

45 mm. The processing parameters including the laser power, scanning speed, hatch spacing, layer thickness, and rotation angle between the successive layers were selected as 285 W, 960 mm/s, 0.100 mm, 0.040 mm, and 67°, respectively, as schematically illustrated in Fig. 1(a). After the LPBF fabrication, the block was heated at 600 °C for 2 h and then cooled in the furnace for stress relief.

(1) For specimens with the same thickness, the fatigue life of LPBF-fabricated Inconel 718 specimens that underwent homogenization at 1100 °C for 1 hour followed by aging is longer compared to specimens homogenized at 1065 °C for 1 hour and aged. This extended fatigue life can be attributed to the enhanced coordination of local deformation among grains and the decreased occurrence of Laves and δ phases with larger aspect ratios, which are recognized as initiators of fatigue cracks.

dependent yield strength. This model effectively describes the coupling effect of geometrical and microstructural scales on the fatigue properties of LPBF-fabricated Inconel 718 at 650 °C.

(4) The unavoidable thickness debit in fatigue of the LPBF-fabricated Inconel 718 at 650 °C can be effectively mitigated by appropriately tailoring the heat treatment, such as through homogenization at 1100 °C followed by aging, as demonstrated here.

CRediT authorship contribution statement

Declaration of competing interest

Data availability

Supplementary materials

Supplementary material associated with this article can be found, in the online version, at doi:10.1016/j.ijplas.2024.104137.

Han, Y.F., Deb, P., Chaturvedi, M.C., 1982. Coarsening behaviour of γ''- and γ'-particles in Inconel alloy 718. Metal Sci. 16, 555–562.

Ma, T., Zhang, B., Wang, L.Y., Song, Z.M., Luo, X.M., Liu, C.S., Zhang, G.P., 2020. Anisotropy of small punch creep performance of selective laser melted GH4169 650 °C. Mater. Sci. Eng.: A 806, 140608.

Ma, T., Zhang, G.P., Tan, P., Zhang, B., 2022. Effects of homogenization temperature on creep performance of laser powder bed fusion-fabricated Inconel 718 at 650°C. Mater. Sci. Eng.: A 853, 143794.

Phillips, P.J., McAllister, D., Gao, Y., Lv, D., Williams, R.E.A., Peterson, B., Wang, Y., Mills, M.J., 2012. Nano γ′/γ″ composite precipitates in Alloy 718. Appl. Phys. Lett. 100, 211913.

Prasad, K., Sarkar, R., Ghosal, P., Kumar, V., 2010. Tensile deformation behaviour of forged disc of IN 718 superalloy at 650 °C. Mater. Des. 31, 4502–4507.

Wan, H.Y., Luo, Y.W., Zhang, B., Song, Z.M., Wang, L.Y., Zhou, Z.J., Li, C.P., Chen, G.F., Zhang, G.P., 2020. Effects of surface roughness and build thickness on fatigue properties of selective laser melted Inconel 718 at 650 °C. Int. J. Fatig. 137, 105654.

Yu, J., Li, J.R., Zhao, J.Q., Han, M., Shi, Z.X., Liu, S.Z., Yuan, H.L., 2013. Orientation dependence of creep properties and deformation mechanism in DD6 single crystal superalloy at 760 °C and 785MPa. Mater. Sci. Eng.: A 560, 47–53.