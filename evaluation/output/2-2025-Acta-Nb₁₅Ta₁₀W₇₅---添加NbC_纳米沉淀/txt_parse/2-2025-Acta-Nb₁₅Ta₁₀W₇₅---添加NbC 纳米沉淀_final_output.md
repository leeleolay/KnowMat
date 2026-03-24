DOI: 10.1016/j.actamat.2025.121325

# Simultaneous improvement of printability, mechanical isotropy, and high temperature strength in additively manufactured refractory multi-principal element alloy via ceramic powder additions and in-situ NbC nano-precipitation

Ran Duan $ ^{a} $, Yakai Zhao $ ^{b,c} $ $ ^{iD} $, Xiaodan Li $ ^{e} $, Jintao Xu $ ^{a} $, Meng Qin $ ^{a} $, Kai Feng $ ^{a,d,*} $ $ ^{iD} $, Zhuguo Li $ ^{a,*} $, Beibei Xu $ ^{f,*} $, Upadrasta Ramamurty $ ^{g} $

 $ ^{a} $ Shanghai Key Laboratory of Materials Laser Processing and Modification, School of Materials Science and Engineering, Shanghai Jiao Tong University, Shanghai, 200240, PR China

Future Energy Acceleration & Translation (FEAT), Agency for Science, Technology and Research (A*STAR), Singapore, 138634, Singapore

 $ ^{c} $ Institute of Materials Research and Engineering (IMRE), Agency for Science, Technology and Research (A*STAR), Singapore, 138634, Singapore

 $ ^{d} $ School of Materials and Energy Engineering, Guizhou Institute of Technology, Guiyang, Guizhou, 550002, PR China

 $ ^{e} $ Shenvang Aircraft Corporation, Shenvang 110000, PR China

 $ ^{f} $ State Key Laboratory of Materials for Integrated Circuits, Shanghai Institute of Microsystem and Information Technology, Shanghai, 200050, PR China

 $ ^{8} $ School of Mechanical and Aerospace Engineering, Nanyang Technological University, Singapore, 639798, Singapore

## ARTICLE INFO

## Keywords

Refractory multi principal element alloys

Laser powder bed fusion

In-situ nano-precipitates

Printability

High-temperature strength

## Abstract

The inherent brittleness of the refractory multi-principal element alloys (RMPEAs) renders manufacturing of structural components with complex geometries using conventional means difficult. The additive manufacturing technique of laser powder bed fusion (LPBF) can potentially circumvent this problem. However, eliminating cracks, minimizing porosity, reducing the microstructural and (consequent) mechanical anisotropy, and retaining high-temperature (HT) strength—all simultaneously—remain the key challenges. Adding ceramic particles to the alloy can improve the printability and HT strength. However, the extreme melting points of RMPEAs can lead to their dissolution. Keeping this in view, 1.5 at. % WC powder—determined theoretically to be the optimum—was added to the  $ Nb_{15}Ta_{10}W_{75} $ powders prior to LPBF. Results show an expanded process window and improved printability, attributed to the enhanced laser absorptivity, without compromising powder flowability. Carbon released through the dissolution of WC combines with Nb to form NbC in-situ, which promotes in the columnar-to-equiaxed microstructural transition and hence reduced mechanical anisotropy. The NbC nanoprecipitates also enhance the high temperature strength (up to 1600 ^\circC) by hindering the mobility of both screw and edge dislocations.

## 1. Introduction

The advent of multi-principal element alloys (MPEAs) has opened the arena of alloy design to a vast multicomponent space and enabled the identification of alloys with prominent properties for various applications[1–4]. Specifically, the refractory multi-principal element alloys (RMPEAs) exhibit excellent high-temperature (HT) strength and resistance to HT softening, making them potential candidates in a wide variety of high temperature applications [5–8]. Among RMPEAs reported thus far, NbMoTaW exhibits promising phase stability, resistance to softening at HT, and HT strength ( $ \sim $400 MPa at 1600 ^\circC), far exceeding the service temperature of Ni-based superalloys [9]. While it is particularly suitable for HT pressure-bearing components, its intrinsic brittleness severely limits the application potential as producing components with complex shapes is difficult [10]. The additive manufacturing technique of laser powder bed fusion (LPBF) enables the direct fabrication of such components, overcoming the limitations (such as restricted mold shapes and poor processability) of arc melting [11–13]. However, two critical challenges remain for LPBF of NbMoTaW. First, the inherent brittleness of NbMoTaW could induce cracking

under the high thermal gradients intrinsic to LPBF, making defect elimination particularly challenging [14]. Second, columnar grains preferentially form along the [001] or [101] crystallographic directions during LPBF, resulting in anisotropy that could adversely affect practical applications [15,16]. These challenges are addressed—primarily—by adding low-melting-point elements or ceramic particles to RMPEAs.

Incorporating low melting point (MP) elements (e.g., Ti, Zr, or Hf with the melting points of 1670, 1852, and 2227 ^\circC, respectively) significantly enhances the constitutional undercooling ( $ \Delta T_{CS} $). It, in turn, provides the driving force for heterogeneous nucleation and thus suppresses the columnar grain growth during LPBF [17,18]. However, alloying with elements with lower MP reduces the plastic flow softening temperature and promotes the transition of dislocation-mediated plastic deformation from that governed by cross-kinking to that of diffusion, thereby adversely affecting the HT strength [19–21]. It also could adversely affect the printability during LPBF. The significant thermodynamic differences (e.g., melting point, viscosity, and thermal expansion coefficient) between the high and low MP elements narrow the processing window and increase the risk of segregation-induced cracking owing to the increased volatility of low MP elements [21–23].

The addition of ceramic particles to alloys during LPBF can enhance heterogeneous nucleation, suppress columnar grains, and hinder dislocation mobility during HT deformation of the alloy [24]. The ceramic particles can also improve printability through the following possible mechanisms. They could (i) refine grains, which could help resist crack formation [25], (ii) lower the melt viscosity, which would promote the molten metal flow in filling the pores [26], (iii) enhance wettability that would facilitate stronger interlayer bonding [27], and (iv) alleviate the tensile stresses generated during solidification by ceramic-induced compressive stress to suppress cracking [28]. The effectiveness of these mechanisms depends critically on the survival of ceramic particles within the melt pools of LPBF, as the high MP of RMPEA poses the risk of ceramic particle dissolution.

Keeping the above in mind, this work selectively incorporates nano-sized carbide particles into  $ Nb_{15}Ta_{10}W_{75} $ powders to improve printability by enhancing laser absorptivity. It also utilizes in-situ precipitation during LPBF to reduce the anisotropy and improve the room temperature (RT)/HT strengths. The roles of carbide particles and in-situ precipitates are further summarized in Supplementary-Note 1. This strategy effectively addresses the thermal stability limitations of ceramic particles in improving printability and HT strength in RMPEAs.  $ Nb_{15}Ta_{10}W_{75} $ alloy was chosen as the matrix, as it was optimized from the Nb-Mo-Ta-W alloy systems using the Toda-Caraballo model and demonstrated to exhibit an excellent HT strength of 640 MPa at 1600 ^\circC [29]. The selection of ceramic particles involved the following three steps. (i) The type of non-metallic element within ceramic particles was determined by evaluating the solid solubility and melting point (obtained from the equilibrium phase diagram) of its in-situ formed compounds. (ii) The optimum ceramic content to be added was determined based on the critical re-precipitation amount (obtained from the non-equilibrium solidification path calculations) to ensure in-situ nano-precipitate formation during LPBF. (iii) The ceramic type was selected by evaluating mixed powder characteristics (including laser absorptivity and flowability), which can minimize the impact of the ceramic addition on the powder spreading characteristics and improve printing quality. The formation mechanisms of the NbC nano-precipitates, as well as their effects on microstructural evolution and RT/HT mechanical properties, were investigated in detail. Notably, the impact of NbC nano-precipitates on the screw/edge dislocation mobility at high temperatures is evaluated.

## 2. Materials and methodologies

## 2.1. Material design and powder mixing

Since MPs of all the elements in the  $ Nb_{15}Ta_{10}W_{75} $ alloy are high, it is difficult to achieve a large degree of  $ \Delta T_{CS} $. Adding suitable ceramic particles, which would act as the heterogeneous nucleation cites, is essential for achieving the columnar to equiaxed transition (CET) in it [13]. Since the high MP of  $ Nb_{15}Ta_{10}W_{75} $ can result in the dissolution of the added particles, the key strategy employed here is to add ceramic powders that can dissolve in the melt pools and, in the process, introduce a non-metallic element to the melt, which subsequently re-precipitate in-situ and regulates the grain morphology. The phase stability of the in-situ formed precipitates is an additional consideration that is crucial for maintaining grain morphology and strength of the alloy at HT. To this end, the solid solubility and melting points of various in-situ precipitations were assessed using an equilibrium phase diagram obtained from the Thermo-Calc software. An example of it is displayed in Fig. 1(a). It shows that with the incorporation of 0.25 at. % C into  $ Nb_{15}Ta_{10}W_{75} $, the matrix phase with the body centered cubic (BCC) crystal structure first solidifies, followed by the metal carbide (MC) phase at 2613 ^\circC, with a maximum molar fraction of 1.1 %. Similar equilibrium phase diagrams were obtained when C, N, B, or O in different proportions were introduced into  $ Nb_{15}Ta_{10}W_{75} $, which all consist of BCC phase and in-situ precipitates (MC, MN, MB, or MO, respectively). The precipitation temperatures of MC, MN, MB, and MO are displayed in Fig. 1(b), and the maximum re-precipitation contents after adding different contents of C, N, B, or O into  $ Nb_{15}Ta_{10}W_{75} $ matrix are shown in Fig. 1(c). The MC phase has the highest precipitation temperature (the best phase stability) and re-precipitation content (the lowest solid solubility) compared to the MN, MB, and MO type precipitates. Therefore, it is inferred that adding C to  $ Nb_{15}Ta_{10}W_{75} $ aids in the in-situ formation precipitates and contributes to the phase stability.

To ensure the in-situ MC precipitation during LPBF, the non-equilibrium solidification paths of  $ (Nb_{15}Ta_{10}W_{75})_{100-x}C_x $ ( $ x = 0, 1.0, 1.5 $ at. %) at a cooling rate of  $ 10^7 $ K/s were estimated using the Gulliver-Scheil model module (available in the Thermo-calc software) to determine the amount of C that needs to be added. Results are displayed in Figs.1 ( $ d_1 $- $ d_2 $). The Gulliver-Scheil model is suitable for simulating the non-equilibrium solidification process that occurs under the rapid solidification conditions which prevail during the LPBF process [30]. This model assumes that complete diffusion occurs within the liquid phase, while no diffusion occurs in the solid phase [30]. Figures.1 ( $ d_1 $- $ d_2 $) show that the solidification sequence remains liquid (L)\rightarrow BCC phase as long as the added C content is below 1.5 at. %. It changes to L\rightarrow BCC\rightarrow BCC+MC when more than 1.5 at. % C. Therefore, incorporating more than 1.5 at. % C to  $ Nb_{15}Ta_{10}W_{75} $ is deemed beneficial for in-situ MC precipitation during LPBF.

While increasing the C content beyond 1.5 at. % can contribute positively to the precipitate formation during LPBF, it also could adversely affect the powder flowability, as it reduces the smoothness of the powder surfaces and thus enhances the rolling friction between the powder particles [31]. For determining the optimal type of carbide ceramic additions, the flowability and laser absorptivity of  $ Nb_{15}Ta_{10}W_{75} $ powders mixed with different ceramic powder contents were assessed. The detailed selection process is shown in Supplementary-Note 2, and only the best results are presented below.

The required quantities of elemental powders (Nb, Ta, W, > 99.9 % purity, Xiamen Tungsten Co.,Ltd., China) for forming  $ Nb_{15}Ta_{10}W_{75} $ were accurately weighed using an electronic analytical balance. The pre-mixed powders were put into a mixing tank and evacuated to a vacuum of  $ 10^{-1} $ Pa before filling it with the argon gas. The pre-mixed powder was then mixed at 120 r/min for 6 h in a three-dimensional (3D) planetary mill. A laser diffraction analyzer (DC24000 UHR, CPS, Inc.) was used to measure the equivalent diameter of the powders. The  $ D_{10} $,  $ D_{50} $, and  $ D_{90} $ of the  $ Nb_{15}Ta_{10}W_{75} $ powders were 20, 37, and 57  $ \mu $m, respectively. The powders display a spherical morphology, as shown in Figs.2 ( $ a_{1} $) and ( $ b_{1} $). Then, WC powder was added to the  $ Nb_{15}Ta_{10}W_{75} $ powder such that the C content in the combined alloy corresponds to 1.5 % of the total at %; this alloy is referred to as ( $ Nb_{15}Ta_{10}W_{75} $) $ _{98.5} $C $ _{1.5} $ hereafter. The WC powder size follows the Gaussian distribution and
Fig. 1. (a) Equilibrium phase diagram and element compositions of  $ Nb_{15}Ta_{10}W_{75} $ doped with non-metallic elements. (b) Precipitation temperatures of MC, MN, MB, MO. (c) Comparison of the molar fractions of different in-situ precipitated phases for different non-metallic element additions. Selection of non-metallic element content based on the solidification path for  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{100-\mathrm{x}}\mathrm{C}_{\mathrm{x}} $:  $ (\mathrm{d}_{1}) $ x = 0 at. %;  $ (\mathrm{d}_{2}) $; x = 1.5 at. %.

was found to be uniformly distributed on the surfaces of the  $ Nb_{15}Ta_{10}W_{75} $ powders after being mixed in a planetary mill for 5 h, as shown in Figs. 2(a2) and (b2). The flowability of powders, which is crucial for printing quality, was evaluated by using the Hall flowmeter [32]. Both the Hall flow rate (HRF) and the angle of repose (AOR) did not show significant changes after the incorporation of WC powders, as shown in Figs.2 ( $ c_{1}-c_{2} $), indicating that it will not affect the powder flow and spread

Apart from powder flowability, laser absorptivity also significantly influences print quality. The addition of smaller WC particles to the  $ Nb_{15}Ta_{10}W_{75} $ powder increases its convex and specific surface areas and thus could enhance its laser absorptivity and reduce the energy required for melting powders [32]. To ascertain this, the laser absorptivity was measured using the diffuse reflectance spectroscopy (DRS, UV–vis-NIR Lambda 950 Spectrophotometer, PerkinElmer, Inc.). The laser absorptivity of the  $ Nb_{15}Ta_{10}W_{75} $_{98.5}C_{1.5} powders is 88 % higher (at a wavelength of 1070 nm used for the LPBF process) than that of the  $ Nb_{15}Ta_{10}W_{75} $ powders, as shown in Figs.2 ( $ d_{1} $- $ d_{2} $). Thus, incorporation of 1.5 at. % WC powders into  $ Nb_{15}Ta_{10}W_{75} $ aids in the in-situ precipitation as well as fabrication using LPBF.

## 2.2. Material preparation

The LPBF processes were carried in an SLM 280 metal printer (Zhong Rui Technique, China), which was equipped with a maximum laser power of 500 W (YAG fiber laser; beam spot diameter 90  $ \mu $m; wavelength 1070 nm). The process chamber was filled with high-purity argon (99.999 vol %; oxygen content below 100 ppm) and shielded the sam-
Fig. 2. Surface morphology of  $ (a_{1}) $ Matrix powders and  $ (a_{2}) $ Mixed powders; Particle size distribution of  $ (b_{1}) $ Matrix powders and  $ (b_{2}) $ WC powder additions; HRF and AOE of  $ (c_{1}) $ Matrix powders and  $ (c_{2}) $ Mixed powders; Laser absorptivity of  $ (d_{1}) $ Matrix powders and  $ (d_{2}) $ Mixed powders.

ples from oxidation. A rotation angle of  $ 67^{\circ} $ between successive layers was applied to reduce stress and anisotropy. A polished pure tungsten plate was used as the substrate to improve the bonding with the material. The melting points of Nb, Mo, Ta, and W all exceeded  $ 2400^{\circ} $C [8], requiring high energy input to melt the powders during LPBF completely. To analyze the influence of WC powder addition on the optimum printing process parameter window of  $ Nb_{15}Ta_{10}W_{75} $, a series of samples were printed using different volumetric energy densities (VED) [33]:

 $$ VED=\frac{P}{\nu h t}. $$ 

In Eq. (1), P is laser power,  $ \nu $ is the scanning speed, h is the hatch spacing, and t is the layer thickness. A total of 480 process parameter combinations, with the VED and P ranges of 50 to 850 J/mm $ ^{3} $ and 150 to 400 W, respectively, for each composition were explored. In all cases, t was fixed at 40  $ \mu $m, while h was either 30 or 40  $ \mu $m,  $ \nu $ was adjusted accordingly based on the above parameters. Based on these trails, the following optimum process parameter combination for Nb $ _{15} $Ta $ _{10} $W $ _{75} $ was identified: P = 300 W,  $ \nu $ = 400 mm/s, t = 40  $ \mu $m, and h = 30  $ \mu $m. With the addition of 1.5 at. % WC powder, a  $ \nu $ of 690 mm/s (while the other three process parameters remained the same) gave the best results.

A gas expansion density tester (HX-TD, Hiseel, China) was used to measure the relative density of the printed samples. This device measured the variation in helium gas volume within the test chamber before and after placing the sample, providing an efficient, accurate, and non-destructive method to measure the true volume and density of the printed samples. To ensure measurement accuracy, the printed samples were successively polished using the 500 #, 1000 #, 1500 #, 2000 # and 3000 # grit sandpapers to minimize the influence of irregular surface contours. For each printing parameter combination, nine samples were printed, and their density was measured, with each sample tested 3 times to ensure the reliability of the results. Cubic samples of  $ 8 \times 8 \times 10 $ mm $ ^{3} $ were printed and used for density measurement, microstructural characterization, and compression experiments.

## 2.3. Microstructural and mechanical characterization

The crystal structure of the phase(s) in the microstructure was analyzed by using the X-ray diffraction (XRD; D8 Advance Da Vinci, Bruker Corp., USA) equipped with Cu-K\alpha radiation ( $ \lambda = 1.5418 $ Å) operating at 40 kV, 40 mA, and performed over a scan range of 20 ^\circ and 100 ^\circ with a scan rate of 1.5 ^\circ/min. The defect characteristics of the printed samples were characterized using an optical microscope (OM; Axio Imager A2m, Zeiss, Germany). Microstructural characteristics and powder morphology were observed with the aid of a scanning electron microscope (SEM; FEI Co., Hillsboro, OR, USA). It was equipped with the energy dispersive spectroscopy (EDS) and electron backscatter diffraction (EBSD) detectors, which were used to analyze the microscopic segregation and the grain orientation, respectively. The EBSD experiments were performed at an accelerating voltage of 20 kV with a scan step size of 0.1 \mum. The finer microstructures and precipitates were observed by using transmission electron microscopy (TEM; JEM-F200X, JEOL Ltd., Tokyo, Japan) working at a voltage of 200 kV. For TEM, foils were prepared by a focused ion beam (FIB; Carl Zeiss AG) equipped with an electron beam at 100 kV. The elemental distribution within the precipitates was characterized using the 3D-atom probe tomography (3D-APT; LEAP 5000X), operating at a pulse repetition rate of 200 kHz and a UV laser energy of 60 pJ. The sharp tipped samples for 3D-APT were fabricated by annular milling within the grains using FIB.

Uniaxial compression experiments were performed in a universal testing machine (Sans Testing Machine Co., Ltd., Shenzhen, China) equipped with a video extensometer (LVE-MICRO30) at a nominal constant loading rate of 0.008 mm/s. The size of compression specimens was  $ \Phi 2 $ mm  $ \times $ 4 mm. At least three samples were tested for each case. The HT compression properties were measured by using a Gleeble-3500 testing machine, with a heating rate of 10  $ ^{\circ} $C/min and a constant displacement rate ( $ \varepsilon_{L} $) of 0.0025 mm/s. The size of HT compression specimens was  $ \Phi 4 $ mm  $ \times $ 8 mm.

## 3. Results

## 3.1. Sample preparation

Results of the defect morphologies of the printed samples, characterized using OM, and their relative densities, measured using a gas expansion density tester, are shown in Fig. 3(a). For VED below 310 J•mm⁻³, lack of fusion (LOF) pores were observed in both Nb₁₅Ta₁₀W₇₅ and (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅. They are likely due to inadequate heat input for fully melting refractory metal powders [34,35]. When VED exceeded 620 J•mm⁻³, cracks were observed in both RMPEAs. Cracking is thought to be driven by the accumulation of thermal stresses, caused by the excessive energy input [23]. The optimal VED ranges for Nb₁₅Ta₁₀W₇₅ and (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅ were found to be 520–620 J•mm⁻³ and 360–520 J•mm⁻³, which resulted in the densities of 99.2 \pm 0.15 % and 99.5 \pm 0.1 %, respectively, with pores being the only type of defects present in the blocks fabricated using these parameters. The incorporation of WC powders not only led to a higher density—that too at a lower VED, but also a wider process window (extended by 50 J•mm⁻³), compared to Nb₁₅Ta₁₀W₇₅, possibly due to the enhanced laser absorptivity (Fig. 2(d₂)). Cuboidal samples (8 \times 8 \times 10 mm³) of both the alloys were manufactured with the optimal process (mentioned in Section 2.2) and are used for microstructure characterization and compression experiments, as shown in Fig. 3(b).

## 3.2. Microstructural characterization

The XRD patterns obtained on  $ Nb_{15}Ta_{10}W_{75} $ and  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ are shown in Fig. 4. The pattern obtained on  $ Nb_{15}Ta_{10}W_{75} $ shows a single phase with the BCC crystal structure. With the incorporation of WC powder, additional peaks corresponding to the NbC precipitates with  $ B_{2} $ crystal structure are observed. The dislocation density ( $ \rho $) within the built samples was estimated using the XRD data and the following equations [36,37]:

 $$ \rho=\frac{2\sqrt{3}\vartheta}{\psi b} $$ 

 $$ \vartheta=\frac{\beta}{4tan\theta} $$ 

 $$ \psi=\frac{K\lambda}{\beta cos\theta} $$ 

where  $ \vartheta $ is the micro-strain (which is related to the full width at half maximum (FWHM) of the XRD peak,  $ \beta $ [38]),  $ \psi $ is the coherent domain size (that depends on the X-ray wavelength,  $ \lambda = 0.15405 $ nm [38,39]), b is the Burgers vector,  $ \theta $ is the Bragg angle, and K is a dimensionless factor (= 0.89 [39]). Details of the calculations used for estimating  $ \rho $ based on the XRD data are provided in Supplementary-Note 3. The estimated  $ \rho $ values in  $ Nb_{15}Ta_{10}W_{75} $ and  $ Nb_{15}Ta_{10}W_{75} $ $ _{98.5}C_{1.5} $ are about  $ 3.36 \pm 0.2 \times 10^{14} $ and  $ 3.96 \pm 0.3 \times 10^{14} m^{-2} $, respectively.

Figs. 5 ( $ a_{1}-a_{4} $) display the SEM images of the X-Y and X-Z planes of  $ Nb_{15}Ta_{10}W_{75} $ and  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $. They show few pores and no cracks, confirming the high relative densities and good quality prints. The inverse pole figure (IPF) maps (overlapped with the high-angle grain boundaries (HAGBs) for showing grain morphologies) are displayed in Figs. 5 ( $ b_{1}-b_{4} $). Generally, the misorientation angles between neighboring grains exceed  $ 15^{\circ} $ for HAGBs, while the low-angle grain boundaries (LAGBs) are those grain boundaries (GBs) with misorientation angles between  $ 2^{\circ} $ and  $ 15^{\circ} $ [40]. In the X-Y plane, both the alloys do not exhibit significant columnar grain morphology. In the X-Z plane,  $ Nb_{15}Ta_{10}W_{75} $ exhibits a columnar grain morphology, with the long axis
Fig. 3. (a) OM images combined with gas expansion densities at different VEDs illustrate the variations in the defect characteristics, relative density, and process window after the WC powder addition; (b) Display of  $ Nb_{15}Ta_{10}W_{75} $ and  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ samples used for microstructure characterization and compression experiments.
Fig. 4. X-ray diffraction patterns obtained on the  $ Nb_{15}Ta_{10}W_{75} $ and  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $.

of the grains oriented along the Z-axis direction. This is due to the significant temperature gradient along the Z-axis, which leads to the formation of columnar grains aligned with it [39].

To further identify the grain morphology, the grain shape aspect ratio (GSAR) is analyzed, as shown in Figs.5 ( $ c_{1} $- $ c_{4} $). The GSAR is defined as the ratio of the short to long axis of the grains, with distinct colors used to differentiate grain morphologies. Both  $ Nb_{15}Ta_{10}W_{75} $ and  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ exhibit cellular grain morphology on the X-Y plane. The GSAR values are closely concentrated in the range of 0.3–0.6, comprising 66.3 % for  $ Nb_{15}Ta_{10}W_{75} $ and 63.5 % for  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $, as shown in Figs.5 ( $ c_{1} $) and ( $ c_{3} $). The GSAR of  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ on the X-Z plane increases significantly compared to that of  $ Nb_{15}Ta_{10}W_{75} $, particularly in the range of 0.3–0.6, rising from 35.5 % to 71.0 %, as shown in Figs.5 ( $ c_{2} $) and ( $ c_{4} $). This indicates a significant increase in short axis grains, and the addition of WC powders effectively inhibits the growth of columnar grains. Besides, GSAR maps over a larger area (500  $ \mu $m \times 600  $ \mu $m) on the X-Z plane were obtained to further distinguish grain morphology (Figs.5 ( $ d_{1} $- $ d_{2} $)). The results indicate that  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ has a higher GSAR value, with a high proportion of 69.9 % at 0.3–0.6 and 8.7 % at 0.6–1.0, indicating the WC powder addition suppresses the columnar grain growth and results in an equiaxed microstructure.

Except for grain morphology, the pole figures (PFs) also confirm that the addition of WC powders suppresses the columnar grain growth, as shown in Figs.5 (e₁-e₄). In the X-Y plane, random texture is noted for both the alloys (Fig. 5(e₁) and (e₃)). The maximum uniform distribution (MUD) values are 2.93 and 2.83 for Nb₁₅Ta₁₀W₇₅ and (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅, respectively. In the X-Z plane of Nb₁₅Ta₁₀W₇₅, strong {100} texture can be observed (Fig. 5(e₂)), which is the preferred grain growth direction during LPBF [10,11]. The corresponding MUD value is 3.29. With the WC powder addition, significant reduction in the intensity of {100} texture is noted, making the texture random (Fig. 5(e₄)). Correspondingly, the MUD value decreased to 3.02.

Bright-field (BF) TEM images obtained from the  $ Nb_{15}Ta_{10}W_{75} $ and  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ samples are shown in Figs.6 ( $ a_{1} $) and ( $ a_{2} $), respectively.  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ contains a large number of dispersed precipitates, which were uniformly distributed both within the grains and at the GBs. Selected area electron diffraction (SAED) patterns of  $ Nb_{15}Ta_{10}W_{75} $, obtained using the  $ [01-1]_{BCC} $ zone axis, and  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ along the  $ [1-31]_{BCC} $ zone axis, are shown in Figs.6 ( $ b_{1} $) and ( $ b_{2} $), respectively.  $ Nb_{15}Ta_{10}W_{75} $ exhibits only a BCC structure without any second phase. In contrast,  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ displays an additional set of diffraction spots, which correspond to the  $ B_{2} $ crystal structure, indicating the in-situ formation of MC precipitates. The phase structures observed from the SAED patterns are consistent with the XRD results shown in Fig. 4. An EDS line scan, performed on the nano-precipitates inside the grains (red dashed box), is shown in Fig. 6(c). The C and Nb contents are the highest in the center of the nano-scale precipitate, while other elements are significantly lower. Especially, the W content is significantly lower in the precipitate than in the matrix, whereas Ta content is nearly constant. The elemental distribution confirms that the observed particles are indeed NbC nano-precipitates, with the length and width of about  $ 67 \pm 5 $ and  $ 45 \pm 4 $ nm. respectively.

Fig.6(d) displays the TEM dark-field (DF) micrographs of the NbC precipitates within  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $, which is obtained along the  $ [222]_{NbC} $ zone axis (Fig. 6(e)). The results show that a considerable number of precipitates are uniformly distributed in the alloy. Based on the DF-TEM images, the average diameter (r) of these precipitates (measured using the Image-Pro-Plus software) is determined to be 37.2

 $ \pm 4.3 \, nm $ (Fig. 6(f)). Their number density (N) was estimated by using the following equations [40]:

 $$ N=\frac{f}{4/3\pi r^{3}} $$ 

 $$ f=\frac{\sum_{i}\pi r_{i}^{2}T_{avg}}{2x_{p}y_{p}t_{d}} $$ 

 $$ T_{avg}=1.15R(1)+2.07R(2)+2.99R(3)+3.91R(4) $$ 

where $f$ is the volume fraction. $T_{avg}$ is the average thickness of NbC, taken across four different locations $(R(i))$ of the TEM sample [40], $x_{p}$ and $y_{p}$ are the dimensions of the TEM image, and $t_{d}$ is the thickness of the TEM sample. The obtained $N$ value of the NbC precipitate, $9.7 \pm 3.8 \times 10^{22} \, m^{-3}$, suggests that a large amount of NbC precipitates were uniformly dispersed in $(Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5}$ RMPEAs.

For  $ Nb_{15}Ta_{10}W_{75} $, the typical atomic structure of the matrix is observed from the intragranular region using HRTEM (Fig. 7(a)). The HRTEM image of this region is enlarged, and the corresponding Fast Fourier transform (FFT) images are shown in Figs.7 ( $ b_{1} $) and ( $ b_{2} $),
Fig. 5. Effect of adding WC powders on defects and grain morphologies. (a₁-a₄) SEM images showing high density with fewer defects. (b₁-b₄) IPF maps overlapping with HAGBs showing the grain morphology. (c₁-c₄) GSAR maps and (d₁-d₂) Extended-range measurement GSAR maps used to distinguish grain morphology. (e₁-e₄) Pole figures showing the variations in the texture.

respectively. The selected area exhibits a BCC structure without additional diffraction spots, consistent with the results of SAED (Fig. 6(b1)). The interplanar spacing along [011]BCC was measured as 0.22 nm, which corresponds to a lattice parameter of 3.22 Å. Fig. 7(c) shows the crystal structures of the matrix, NbC/matrix interface, and NbC in (Nb $ _{15} $Ta $ _{10} $W $ _{75} $) $ _{98.5} $C $ _{1.5} $. High-magnification HRTEM images and FFT patterns of the nano-precipitates are shown in Figs.7 (d $ _{1} $-d $ _{2} $), (e $ _{1} $-e $ _{2} $), and (f $ _{1} $-f $ _{2} $), respectively. Only one set of diffraction spots is present in the matrix (Fig. 7(d $ _{2} $)) and NbC (Fig. 7(f $ _{2} $)). In contrast, two sets of diffraction spots are observed at the NbC/matrix interface (Fig. 7(e $ _{2} $)), confirming the phase relationship of [011]BCC//[0-1-1]NbC. The measured interplanar spacings of [011]BCC and [011]NbC are 0.224 nm (Fig. 7(d $ _{1} $)) and 0.231 nm (Fig. 7(f $ _{1} $)), respectively, with corresponding lattice parameters of 3.26 and 3.36 Å. The lattice mismatch ( $ \delta $) between the BCC matrix and NbC nano-precipitates was estimated using the following equation [42]:

 $$ \delta=\frac{\alpha_{NbC}-\alpha_{BCC}}{\alpha_{NbC}} $$ 

where  $ \alpha_{NbC} $ and  $ \alpha_{BCC} $ are the lattice parameters of the carbide and BCC
Fig. 6. (a₁–a₂) Representative TEM bright-field images obtained from the Nb₁₅Ta₁₀W₇₅ and (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅ samples. Insets (b₁–b₂) show the corresponding SAED patterns. (c) EDS line scans showing the compositional distribution inside the nano-precipitates. (d) A TEM dark-field image of (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅ containing NbC precipitates and (e) the corresponding SAED pattern. (f) Normal distribution pattern of NbC precipitates.

phases. The lattice mismatch between the BCC matrix and NbC is estimated to be 2.9 % (<5 % [28,41,42]), indicating that the interface between NbC and the matrix is coherent (Fig. 7(e1)).

## 3.3. Mechanical properties

Representative compressive engineering stress–strain responses and fracture morphologies are shown in Fig. 8. The mechanical properties at different temperatures are listed in Table 1.  $ Nb_{15}Ta_{10}W_{75} $ displays significant mechanical anisotropy, as seen from Figs. 8( $ a_{1} $) and ( $ a_{2} $). The compressive yield strength ( $ \sigma_{0.2} $), ultimate compressive strength ( $ \sigma_{m} $), and fracture strain ( $ \varepsilon $) at RT and parallel to BD are  $ 759 \pm 17 $ MPa,  $ 939 \pm 16 $ MPa, and  $ 2.6 \pm 0.2\% $, respectively. Perpendicular to BD, they are  $ 1409 \pm 22 $ MPa,  $ 1520 \pm 13 $ MPa, and  $ 5.3 \pm 0.3\% $, respectively. The  $ \sigma_{0.2} $ and  $ \varepsilon $ values in the direction perpendicular to BD are nearly-double of those along BD, illustrating significant anisotropy. In contrast, incorporating WC powder into  $ Nb_{15}Ta_{10}W_{75} $ effectively eliminates the mechanical anisotropy due to CET (Fig. 5). In addition,  $ \sigma_{0.2} $,  $ \sigma_{m} $, and  $ \varepsilon $ along BD increased significantly to  $ 1591 \pm 25 $ MPa,  $ 1667 \pm 13 $ MPa, and  $ 7.4 \pm 0.1\% $, respectively. Perpendicular to BD, they increased to  $ 1615 \pm 28 $ MPa,  $ 1692 \pm 21 $ MPa, and  $ 8.3 \pm 0.4\% $, respectively. Note that  $ \sigma_{0.2} $ and  $ \varepsilon $ of ( $ Nb_{15}Ta_{10}W_{75} $) $ _{98.5}C_{1.5} $ in the two orientations are nearly the same.

The fractographs obtained from the specimens tested in different orientations are shown in Figs.8 (b₁-b₄). For Nb₁₅Ta₁₀W₇₅, fractographs of specimens tested along BD show cleavage fracture characteristics, with relatively smooth surfaces and river patterns (Fig. 8(b₁)). When compressed in the direction perpendicular to BD, the fractured surface exhibits a mixture of cleavage and quasi-cleavage fracture characteristics (Fig. 8(b₃)). After adding WC powder, the fracture mechanism across both compression directions transitions to quasi-cleavage fracture, exhibiting a greater number of torn edges (Figs.8 (b₂) and (b₄)).

The stress–strain responses of  $ Nb_{15}Ta_{10}W_{75} $ and  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $, with the compression direction perpendicular to BD, at HT are shown in Figs.8 ( $ c_{1}-c_{4} $). At 1000, 1200, and 1400 ^\circC, the stress-strain curves for  $ Nb_{15}Ta_{10}W_{75} $ and  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ exhibit elastic deformation before fracture, with some limited plasticity only observed at 1600 ^\circC. This is probably due to the transition from cross-kinking to a diffusion-controlled dislocation slip mechanism at higher temperatures, facilitating dislocation slip and hence plastic deformation [43]. More importantly,  $ \sigma_{0.2} $ of  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ over the temperature range of 1000 and 1600 ^\circC exceed those of  $ Nb_{15}Ta_{10}W_{75} $ by about 100 MPa. The mechanical test results indicate that the incorporation of WC powder into  $ Nb_{15}Ta_{10}W_{75} $ can eliminate anisotropy, improve RT plasticity, and enhance strength at both RT and HT.

## 4. Discussion

## 4.1. Formation mechanisms of the NbC precipitates

From Fig. 6, it is obvious that the WC particles added to the RMPEA powder completely dissolves during the LPBF process, and then lead to the formation of the NbC nano-precipitates within the matrix. These precipitates suppress the columnar grain growth, and, in turn, reduce the mechanical anisotropy (Figs. 5 and 8). It is well known that in-situ
Fig. 7. (a) HRTEM image, (b₁) an enlarged HRTEM image, and (b₂) the corresponding FFT pattern obtained on Nb₁₅Ta₁₀W₇₅. (c) HRTEM image of the interface between BCC matrix and NbC precipitate in (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅. Magnified HRTEM images and corresponding FFT patterns used to analyze the crystal structure at different locations of (d₁-d₂) the BCC matrix, (e₁-e₂) the NbC/matrix interface, and (f₁-f₂) the NbC precipitates.

precipitation during LPBF facilitates CET [44]. Therefore, the mechanisms responsible for the NbC formation in  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ need elucidation, which is attempted in the following through a comparative analysis of the physical characteristics and precipitation kinetics.

Generally, a lower mixing enthalpy ( $ \Delta H_{mix} $) indicates a stronger affinity between the elements, which favors the formation of stable compounds during LPBF [45]. The values of  $ \Delta H_{mix} $ of Nb, Ta, and W with C are shown in Fig. 9(a). Amongst them, Nb-C exhibits the lowest  $ \Delta H_{mix} $, compared to Ta-C and W-C, suggesting a strong preference for forming NbC. This observation rationalizes their in-situ formation during LPBF of ( $ Nb_{15}Ta_{10}W_{75} $) $ _{98.5}C_{1.5} $. Notably, the comparison of  $ \Delta H_{mix} $ values among metallic compounds provides a meaningful starting point for the kinetic calculations (including precipitate nucleation and growth), ensuring that the predicted phase was the most thermodynamically favorable one, while ruling out metastable phases (for example,  $ \Delta H_{mix} $ for W-C is -60 kJ/mol). The nucleation of precipitates is predominantly influenced by the thermodynamic driving force ( $ \Delta G^{*} $), which influences the nucleation rate ( $ N_{\nu} $) [46,47]. Using the Thermo-Calc software, values for  $ \Delta G^{*} $ and  $ N_{\nu} $ of the BCC and NbC phases that are included in the non-equilibrium solidification curve 2 of Fig. 1(d2) are obtained. Results are shown in Figs.9 (b-c). The maximum  $ \Delta G^{*} $ value of NbC (6177 J) is nearly-seven times that of the BCC phase (851 J), resulting in  $ N_{\nu} $ for NbC being about  $ 10^{7} $ times higher than that for BCC phase. On this basis, it is reasonable to assume that NbC nucleates rapidly (even at high cooling rates ( $ 10^{7} $ K/s) that prevail during LPBF).

The diffusion coefficient ( $ \zeta $) also plays a critical role in the nucleation and growth of NbC [48]. The  $ \zeta $ values of Nb, Ta, W, and C are estimated using the following equation [49]:

 $$ \varsigma=\varsigma_{0}exp\left(\frac{-Q_{D}}{RT}\right) $$ 

where  $ \varsigma_{0} $ is the intrinsic diffusion coefficient ( $ m^{2}/s $) and  $ Q_{D} $ is the activation energy for diffusion (kJ/mol). These parameters are obtained from literature through experiments or simulations of refractory metals composed of Nb, Ta, and W [49], and listed in Table 2. The temperature-dependence of  $ \varsigma $ for Nb, Ta, W, and C is shown in Fig. 9(d). The results indicate that C has significantly higher  $ \varsigma $ than the metallic elements across different temperatures, which would also facilitate the in-situ formation of carbides including NbC. Overall, the small  $ \Delta H_{mix} $ as well as large  $ \Delta G^{*} $,  $ N_{v} $,  $ \varsigma $ of NbC, are possibly the reasons that ensure the nucleation and growth of NbC during LPBF.

Variations in the phase volume fractions and element contents under the conditions of non-equilibrium solidification ( $ 10^{7} $ K/s) are analyzed to further explore the origin of in-situ formed NbC. The non-equilibrium cooling path containing NbC is shown in Fig. 10(a), which is derived from stage 2 of the non-equilibrium cooling curve depicted in Fig. 1(d2). The variations in the volume fractions of the liquid, BCC and NbC phases with the temperature are shown in Fig. 10(b). As the temperature decreases from 2755 to 2680 ^\circC at a cooling rate of  $ 10^{7} $ K/s, the liquid phase simultaneously transforms into BCC and NbC phases. Within this temperature range, the formation temperature of NbC (2740 ^\circC) slightly lags behind that of the BCC phase (2753 ^\circC), with higher  $ \Delta G^{*} $,  $ N_{\nu} $, and  $ \zeta $ values promoting the transformation. The phase transformation pathways are governed by elemental redistribution. Therefore, the ThermoCalc software was employed to calculate the compositional variations under non-equilibrium cooling conditions ( $ 10^{7} $ K/s). Results, shown in Figs.10 ( $ c_{1} $- $ c_{4} $), indicate that, during the formation of NbC, C
Fig. 8. Compression engineering stress-strain curves at RT of the (a₁) vertical sample and (a₂) horizontal sample; RT compression fracture morphology of the (b₁-b₂) vertical samples and (b₃-b₄) horizontal samples; HT stress-strain curves at (c₁) 1000, (c₂) 1200, (c₃) 1400, and (c₄) 1600 ^\circC.

Table 1 Mechanical properties of Nb $ _{15} $Ta $ _{10} $W $ _{75} $ and (Nb $ _{15} $Ta $ _{10} $W $ _{75} $) $ _{98.5} $C $ _{1.5} $ along different compression directions.

<table border="1" style="margin: auto; word-wrap: break-word;"><tr><td colspan="2" rowspan="2"></td><td colspan="3">Nb_{15}Ta_{10}W_{75}</td><td colspan="3">(Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5}</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \sigma_{0.2} $ (MPa)</td><td style="text-align: center; word-wrap: break-word;">$ \sigma_{m} $ (MPa)</td><td style="text-align: center; word-wrap: break-word;">$ \varepsilon $ (%)</td><td style="text-align: center; word-wrap: break-word;">$ \sigma_{0.2} $ (MPa)</td><td style="text-align: center; word-wrap: break-word;">$ \sigma_{m} $ (MPa)</td><td style="text-align: center; word-wrap: break-word;">$ \varepsilon $ (%)</td></tr><tr><td style="text-align: center; word-wrap: break-word;">Parallel-BD</td><td style="text-align: center; word-wrap: break-word;">25 ^\circC</td><td style="text-align: center; word-wrap: break-word;">759 \pm 17</td><td style="text-align: center; word-wrap: break-word;">939 \pm 16</td><td style="text-align: center; word-wrap: break-word;">2.6 \pm 0.2</td><td style="text-align: center; word-wrap: break-word;">1591 \pm 25</td><td style="text-align: center; word-wrap: break-word;">1667 \pm 13</td><td style="text-align: center; word-wrap: break-word;">7.4 \pm 0.1</td></tr><tr><td rowspan="5">Perpendicular-BD</td><td style="text-align: center; word-wrap: break-word;">25 ^\circC</td><td style="text-align: center; word-wrap: break-word;">1409 \pm 22</td><td style="text-align: center; word-wrap: break-word;">1520 \pm 13</td><td style="text-align: center; word-wrap: break-word;">5.3 \pm 0.3</td><td style="text-align: center; word-wrap: break-word;">1615 \pm 28</td><td style="text-align: center; word-wrap: break-word;">1692 \pm 21</td><td style="text-align: center; word-wrap: break-word;">8.3 \pm 0.4</td></tr><tr><td style="text-align: center; word-wrap: break-word;">1000 ^\circC</td><td style="text-align: center; word-wrap: break-word;">1009 \pm 10</td><td style="text-align: center; word-wrap: break-word;">1451 \pm 13</td><td style="text-align: center; word-wrap: break-word;">15.9 \pm 0.5</td><td style="text-align: center; word-wrap: break-word;">1105 \pm 31</td><td style="text-align: center; word-wrap: break-word;">1602 \pm 15</td><td style="text-align: center; word-wrap: break-word;">16.4 \pm 0.1</td></tr><tr><td style="text-align: center; word-wrap: break-word;">1200 ^\circC</td><td style="text-align: center; word-wrap: break-word;">942 \pm 27</td><td style="text-align: center; word-wrap: break-word;">1372 \pm 21</td><td style="text-align: center; word-wrap: break-word;">17.2 \pm 0.4</td><td style="text-align: center; word-wrap: break-word;">1042 \pm 29</td><td style="text-align: center; word-wrap: break-word;">1513 \pm 22</td><td style="text-align: center; word-wrap: break-word;">15.0 \pm 0.2</td></tr><tr><td style="text-align: center; word-wrap: break-word;">1400 ^\circC</td><td style="text-align: center; word-wrap: break-word;">841 \pm 25</td><td style="text-align: center; word-wrap: break-word;">1242 \pm 24</td><td style="text-align: center; word-wrap: break-word;">14.4 \pm 0.1</td><td style="text-align: center; word-wrap: break-word;">952 \pm 20</td><td style="text-align: center; word-wrap: break-word;">1397 \pm 24</td><td style="text-align: center; word-wrap: break-word;">14.8 \pm 0.8</td></tr><tr><td style="text-align: center; word-wrap: break-word;">1600 ^\circC</td><td style="text-align: center; word-wrap: break-word;">640 \pm 18</td><td style="text-align: center; word-wrap: break-word;">744 \pm 9</td><td style="text-align: center; word-wrap: break-word;">14.6 \pm 0.5</td><td style="text-align: center; word-wrap: break-word;">750 \pm 16</td><td style="text-align: center; word-wrap: break-word;">957 \pm 12</td><td style="text-align: center; word-wrap: break-word;">15.3 \pm 0.7</td></tr></table>

and Nb rapidly diffuse to it in the liquid phase, reaching 18.5 and 68.5 at. %, respectively. On the other hand, W segregates to the BCC phase, reaching 78.4 %. Ta is relatively uniformly distributed in both the phases, with concentrations of 15.9 and 8.5 at. %, respectively. The combination of (i) rapid cooling process of LPBF [13], (ii) the low diffusion rate of refractory metals (Fig. 9(d)), and (iii) the minimal variation in elemental composition during non-equilibrium solidification (Fig. 10 (c₁-c₄)), result in the preservation of precipitate compositions that essentially mirrors the initial solidification composition of liquid pools. Therefore, measurement of the composition of NbC precipitate and comparing it with the composition calculated by Thermo-Calc can effectively confirm the source of the precipitate.

For verifying the Thermo-Calc results experimentally, APT experiments were performed to determine the composition of the NbC nano-precipitates, after preparing the samples by FIB and identifying the precipitate locations using TEM (Fig. 10(d)). Results indicate significant aggregation of C and Nb in NbC, while W is absent (Figs.10 (e1-e4)). To identify NbC and quantify the elemental distributions, a surface with a C concentration of 0.15 at. % is constructed (Fig. 10(f)), and a one-dimensional (1D) composition map perpendicular to this surface is created (Fig. 10(g)). The elemental content in NbC obtained from APT is consistent with the Thermo-Calc predictions (Fig. 10(h)), which confirms the accuracy of non-equilibrium solidification calculations, indicating that NbC originates from the liquid phase. As the temperature reaches the precipitation range for NbC (2680 to 2755 ^\circC), the combination of low  $ \Delta H_{mix} $ and high  $ \Delta G^{*} $,  $ N_{v} $,  $ \zeta $ values promotes Nb and C atoms.

(a) Formation enthalpies

(d) Diffusion coefficients 3000 2400 1800 1200 600 (K)
Fig. 9. Evaluation of the precipitate stability contained in  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ RMPEA by comparing (a) mixing enthalpy; Comparative analysis of nucleation and growth ability in BCC phase and NbC based on (b) the driving force for nucleation, (c) the rate of nucleation, and (d) the diffusion coefficient.

Table 2 Intrinsic diffusion coefficients and activation energies for diffusion.

|  | Nb | Ta | W | C | Ref. |
| --- | --- | --- | --- | --- | --- |
| $ \varsigma_{0} $ ( $ 10^{-4} $ m $ ^{2} $/s) | 4.5 | 6.2 | 46 | 2.58 | [49] |
| $ Q_{D} $ (KJ/mol) | 480.2 | 601.7 | 666.2 | 140.6 | [49] |

to rapidly aggregate resulting in the nucleation of NbC from the liquid phase. During LPBF, the added WC particles dissolve into the molten pool first, followed by the distribution of C throughout the liquid alloy, and subsequent precipitation of NbC from the liquid phase upon solidification. This process circumvents the uneven distribution and agglomeration of secondary particles, which is a common phenomenon otherwise [50].

## 4.2. Effect of the NbC precipitates on the grain structure

To analyze the effects of the in-situ formed NbC on the grain shape, especially on the planes along BD (X-Z and Y-Z), the grain boundary distributions are obtained and plotted in Figs.11 ( $ a_{1} $- $ a_{4} $). Based on these images, the size of the irregular grains is measured using two different (line intercept and area measurement) methods. The line intercept method measures the average size of grains intersected by a line, while the area measurement method estimates the average grain size based on the grain’s area. The equations for these methods are the following [51]:

 $$ \mathbf{d}_{Line}=\frac{1}{N_{g}}\sum_{i=1}^{N_{g}}di $$ 

 $$ \mathrm{d}_{Area}=\frac{2\sum_{\mathrm{i}=1}^{Ng}A\mathrm{i}\bullet\left(A\mathrm{i}/\pi\right)^{1/2}}{\sum_{\mathrm{i}=1}^{Ng}A\mathrm{i}} $$ 

where  $ d_{Line} $ is the average grain size obtained by the line intercept method,  $ N_{g} $ is the total number of grains,  $ d_{i} $ is the length for grain i,  $ d_{Area} $ is the average grain size obtained by the area method,  $ A_{i} $ is the area of grain i, and  $ 2(A_{i}/\pi)^{1/2} $ is the equivalent diameter based on the area of grain i. By comparing grain size values obtained by the line intercept method along the X direction (for the width of columnar grains), along the Z direction (for the length of columnar grains), and by the area method (for the averaged size of columnar grains), the impact of WC particles on the size of the columnar grains could be revealed. The grain size on X-Z plane decrease from  $ 7.34 \pm 1.3 $  $ \mu $m in  $ Nb_{15}Ta_{10}W_{75} $ to  $ 6.10 \pm 0.9 $  $ \mu $m in  $ Nb_{15}Ta_{10}W_{75} $ $ _{98.5}C_{1.5} $, as shown in Fig. 11(b) (similar trend can be seen for the X-Y plane as well, as shown in Supplementary-Note 4). Figs.11(c) and (d) show the grain size distributions with the measurement line directions oriented perpendicular or parallel to the Z-axis, respectively. The vertical grain size (10.4  $ \mu $m) in  $ Nb_{15}Ta_{10}W_{75} $ exceeds the horizontal one (6.72  $ \mu $m), typical of columnar grain morphology. The grain size in  $ Nb_{15}Ta_{10}W_{75} $ $ _{98.5}C_{1.5} $ decreases to 6.46  $ \mu $m in the horizontal direction and 5.98  $ \mu $m in the vertical direction, displaying a much more equiaxed morphology than in  $ Nb_{15}Ta_{10}W_{75} $. These results further confirm that the NbC precipitates not only inhibit the columnar grain growth during LPBF, but also lead to the refinement of the grains.

The influence of NbC and corresponding process parameters on the suppression of columnar grains is analyzed using the inter-dependence model, which effectively evaluates the synergetic effect of alloy composition, nucleation efficiency, and interparticle distance on grain refinement [52,53]. This model has been widely used to evaluate grain size in alloys produced using casting [54], welding [55], and additive manufacturing [56]. The interdependence model and the key control parameters of grain size can be expressed as following [57]:

 $$ d_{gs}=X_{cs}+X_{dl}+X_{sd} $$ 

 $$ X_{cs}=\frac{D\cdot z\Delta T_{n}}{\nu Q} $$ 

 $$ \Delta T_{n}=\frac{C_{E}}{\Delta S_{\nu}}\delta^{2} $$ 

 $$ Q=\sum_{i=1}^{\mathrm{n}}m_{i}\cdot(k_{i}-1)\cdot C_{0,i} $$ 

 $$ X_{dl}\propto Q $$ 

 $$ X_{\mathrm{sd}}\propto\frac{\Delta T}{\Delta T_{\mathrm{n}}} $$ 

 $$ \Delta T=\Delta T_{cs}+\Delta T_{t} $$
Fig. 10. (a to c) Predictions and (d to f) experimental verification. (a) Non-equilibrium cooling path containing NbC nano-precipitates. (b) Variations of the volume fractions of different phases with temperature. (c₁-c₄) Element distribution in different phases. (d) An image of the APT samples containing a NbC precipitate. (e₁-e₄) Distribution maps of Nb, Ta, W, and C near and inside NbC. (f) Equal concentration C surface of 0.15 at. % distinguishing the NbC precipitate. (g) 1D concentration map reflecting the element distributions in NbC. (h) Comparison of elemental distributions obtained using experimentally with APT and with the Thermo-Calc based calculations.

 $$ \Delta T_{c s}\propto Q $$ 

 $$ \Delta T_{t}\propto V_{\mathrm{a}} $$ 

 $$ V_{a}=v c o s\phi $$ 

where  $ d_{gs} $ is the grain size predicted using the interdependence model,  $ X_{cs} $ is the critical distance that grains must grow before producing adequate  $ \Delta T_{Cs} $ to initiate subsequent nuclei, D is the diffusion coefficient of the solute in the liquid, z is the fraction of  $ \Delta T_{cs} $ required for heterogeneous nucleation,  $ \nu $ is the laser scanning speed,  $ \Delta T_{cs} $ is the undercooling of critical nucleation,  $ C_{E} $ is the elasticity coefficient,  $ \Delta S\nu $ is the entropy of fusion per unit volume, and  $ \delta $ is the degree of interfacial lattice parameter match between the nucleating particles and the matrix.  $ \Delta T_{n} $ is closely related to  $ \delta $ between nucleating particles and matrix. A smaller  $ \delta $ lowers  $ \Delta T_{n} $ is required for the activation of heterogeneous nucleation processes, i.e.,  $ \Delta T_{n} \propto \delta $ [52]. Q is a growth restriction factor;  $ m_{i} $ is the slope of the liquidus line for the  $ i^{th} $ solute in the alloy;  $ k_{i} $ and  $ C_{O,i} $ are the partition coefficient and solute concentration, respectively.  $ X_{dl} $ is the diffusion field distance of accumulated solutes that can compensate for insufficient  $ \Delta T_{cs} $ due to solute diffusion at the S/L interface and is directly related to Q values.  $ X_{sd} $ is the average distance from  $ X_{dl} $ to the nearest particle that can effectively nucleate. It is closely related to the effective nucleation particle density and can be evaluated through undercooling. When  $ \Delta T_{n} $ is lower than the undercooling at the solid/liquid interface ( $ \Delta T $), numerous heterogeneous nucleation events are activated, reducing  $ X_{sd} $ and inhibiting columnar grain formation [58].  $ X_{sd} $ is positively correlated with  $ \Delta T $ and negatively correlated with  $ \Delta T_{n} $.  $ \Delta T $ is composed of  $ \Delta T_{cs} $ and thermal undercooling ( $ \Delta T_{t} $) under non-equilibrium solidification conditions [58].  $ \Delta T_{cs} $ is primarily associated with the solute segregation occurring ahead of the solid/liquid interface and can be quantitatively evaluated using Q [25].  $ \Delta T_{t} $ is the thermal undercooling when the actual growth rate ( $ V_{a} $) at the solid/liquid interface lags behind the theoretical pull rate ( $ V_{theo} $) induced by the high cooling rate that prevails during LPBF [58]. Generally,  $ V_{a} $ is directly correlated with laser scanning speed  $ \nu $ [53].  $ \varphi $ is the angle ( $ ^{\circ} $)
Fig. 11. EBSD data for  $ Nb_{15}Ta_{10}W_{75} $ and  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $. (a1-a4) Grain boundary distribution maps used to measure irregular grain size. (b) Average grain sizes measured by the area method. (c) Horizontal grain sizes and (d) Vertical grain sizes measured by the line intercept method.

between the  $ V_{a} $ and  $ \nu $ directions. The degree of  $ \Delta T_{t} $ is controlled by the values of  $ \nu $. As the value of  $ \nu $ increases, the delay between  $ V_{a} $ and  $ V_{theo} $ becomes more pronounced, resulting in a larger  $ \Delta T_{t} $.

The comparative evaluation of the solidification distance and undercooling illustrates the inhibitory effect of adding WC to RHEA and the resulting NbC precipitates on the columnar grains, as shown in Fig. 12. The incorporation of WC and the presence of NbC reduces  $ X_{cs} $ for three reasons. First, NbC being coherent with the matrix (Fig. 7(e1)) reduces  $ \Delta T_{n} $ and shorten  $ X_{cs} $. Second, WC powder markedly improves the laser absorptivity (Fig. 2(d2)) and increases  $ \nu $ (Section 3.1), resulting in the shortening of  $ X_{cs} $. Third, C that is released through the dissolution of WC increases Q of (Nb $ _{15} $Ta $ _{10} $W $ _{75} $) $ _{98.5} $C $ _{1.5} $ (Table 3), further reducing  $ X_{cs} $. Therefore, (Nb $ _{15} $Ta $ _{10} $W $ _{75} $) $ _{98.5} $C $ _{1.5} $ exhibits a smaller  $ X_{cs} $ compared to Nb $ _{15} $Ta $ _{10} $W $ _{75} $. The  $ X_{dl} $ term of (Nb $ _{15} $Ta $ _{10} $W $ _{75} $) $ _{98.5} $C $ _{1.5} $ is slightly smaller.

Growth restriction factors and related calculation parameters for i th solutes.

|  | m | k | Q | Ref. |
| --- | --- | --- | --- | --- |
| Nb | 3.4 | 1.08 | 0.27 | [17] |
| Ta | 16.5 | 1.48 | 8.0 | [17] |
| W | 15.1 | 2.50 | 22.7 | [17] |
| C | -55 | $ \rightarrow $0 | 55 | [17] |
| Nb $ _{15} $Ta $ _{10} $W $ _{75} $ | / | / | 17.82 | This work |
| (Nb $ _{15} $Ta $ _{10} $W $ _{75} $) $ _{98.5} $C $ _{1.5} $ | / | / | 18.38 | This work |

than that of  $ Nb_{15}Ta_{10}W_{75} $ due to higher Q. The presence of NbC also reduces  $ X_{sd} $. The coherency between NbC and the matrix also helps reduce  $ \Delta T_{n} $ required for heterogeneous nucleation. In  $ Nb_{15}Ta_{10}W_{75} $,
Fig. 12. Schematic illustrations of the generation of the undercooling including  $ \Delta T_{n} $,  $ \Delta T_{cs} $,  $ \Delta T_{t} $ and the solidification distance including  $ X_{cs} $,  $ X_{db} $,  $ X_{sd} $ in (a)  $ Nb_{15}Ta_{10}W_{75} $ and (b)  $ Nb_{15}Ta_{10}W_{75} $ $ _{98.5}C_{1.5} $, illustrating the inhibitory effect of adding WC powder and optimizing process parameters on columnar grains. The schematic illustration is not drawn to scale and is intended for illustrative purposes; actual undercooling and solidification distances may have deviations.

heterogeneous nucleation primarily occurs on the native nuclei particles, such as impurities or oxides that may be present in the melt pool. Such nuclei are usually incoherent with the matrix, characterized by relatively high  $ \delta $, leading to larger  $ \Delta T_{n} $ [52]. Besides, the incorporation of the WC powders into  $ Nb_{15}Ta_{10}W_{75} $ increases  $ \Delta T_{cs} $ owing to the presence of C in solution, which has a high Q value (Table 3). Simultaneously, the added WC powder significantly enhances the laser absorptivity in  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $, thereby increasing  $ \nu $ (Section 3.1) and ultimately increasing the degree of  $ \Delta T_{t} $. The incorporation of WC and the presence of in-situ NbC nano-precipitates reduce  $ \Delta T_{n} $ while increase  $ \Delta T $, meeting the nucleation condition of  $ \Delta T \geq \Delta T_{n} $, which, in turn, shortens  $ X_{sd} $ for  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $. In conclusion, the above theoretical analysis made on the basis of the interdependence model indicates that adding WC powder and the in-situ NbC formation reduces  $ X_{cs} $,  $ X_{dl} $, and  $ X_{sd} $, which effectively inhibit the columnar grain growth in  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $. Moreover, driven by the combination of low  $ \Delta H_{mix} $ and high  $ \Delta G^{*} $,  $ N_{v} $,  $ \zeta $ values, NbC particles re-precipitate from the liquid phase and are uniformly distributed, which serve as heterogeneous nucleation sites and pin grain boundaries (preventing grain coarsening) during repeated heating that solidified layers undergo during LPBF [52].

## 4.3. Effect of NbC on the mechanical properties at room temperature

The anisotropy of the mechanical properties at RT is mainly controlled by grain morphology [15]. Both as-fabricated  $ Nb_{15}Ta_{10}W_{75} $ and  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ exhibit a high relative density of above 99.2% (Fig. 3), which minimizes the potential influence of porosity on mechanical properties and anisotropy [60,61]. The formation of NbC nano-precipitates in the  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ effectively reduces anisotropy. During the manufacturing of  $ Nb_{15}Ta_{10}W_{75} $ using the LPBF technique, the presence of a steep thermal gradient promotes grain growth towards the melt pool core [16], ultimately forming a microstructure with columnar grains that are parallel to the Z-axis (Figs.5 ( $ c_{2} $) and ( $ d_{1} $)). When the alloy is stressed along the Z-axis, they align with the long axis of the columnar grains (Figs.5 ( $ c_{2} $) and ( $ d_{1} $)). The straight boundaries of the columnar grains along their long axis promote crack propagation during plastic deformation [59], resulting in poor compressibility and strength of 2.6 % and 759 MPa, respectively. In contrast, forces applied along the X-axis are parallel to the short axis of the columnar grains (Figs.5 ( $ c_{2} $) and ( $ d_{1} $)). Compared to long-axis columnar GBs, short-axis curved boundaries effectively hinder crack propagation [59], enhancing compressibility (5.3 %) and strength (1409 MPa). The incorporation of WC powder into  $ Nb_{15}Ta_{10}W_{75} $ induces the NbC precipitates (Fig. 7) and changes the grain morphology to an equiaxed one (Figs.5 ( $ c_{4} $) and ( $ d_{2} $)). As a result, the mechanical anisotropy is reduced substantially. In addition, NbC enhances the RT mechanical properties. For  $ Nb_{15}Ta_{10}W_{75} $ and  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $, the contributions from solid-solution hardening ( $ \Delta\sigma_{SSH} $), grain boundary strengthening ( $ \Delta\sigma_{GB} $), dislocation strengthening ( $ \Delta\sigma_{DIS} $), and precipitation strengthening ( $ \Delta\sigma_{P} $) to the total yield strength ( $ \sigma_{y} $) can be estimated using the following relations [62–64]:

 $$ \sigma_{\mathrm{y}}=\Delta\sigma_{0}+\Delta\sigma_{\mathrm{S S H}}+\Delta\sigma_{\mathrm{G B}}+\Delta\sigma_{\mathrm{D I S}}+\Delta\sigma_{\mathrm{p}} $$ 

 $$ \Delta\sigma_{0}=\sum x_{i}\sigma_{i} $$ 

 $$ \Delta\sigma_{G B}=K d^{-1/2} $$ 

 $$ \Delta\sigma_{\mathrm{D I S}}=M\alpha\mu b\rho^{1/2} $$ 

 $$ \Delta\sigma_{\mathrm{P}}=0.26\frac{\mu b}{r}f^{1/2}\ln\left(\frac{r}{b}\right) $$ 

where  $ \Delta\sigma_0 $ is the lattice friction stress of the matrix which is estimated using the weighed average of the lattice friction stresses ( $ \sigma_i $) of the constituent pure metals [64],  $ k $ is the Hall-Petch slope (210 MPa· $ \mu $m $ ^{1/2} $ for refractory metals [64]),  $ d $ is the average grain size (estimated using the area method on the EBSD data obtained on the X-Z plane (Fig. 11(b)),  $ M $ is the Taylor factor ( $ \sim $2.733 for BCC refractory metals) [64],  $ \alpha $ is an empirically determined constant (0.5 for BCC metals [64]),  $ \mu $ is the shear modulus calculated according to the mixed weighting equation [29], and  $ \rho $ is obtained from the XRD analysis (Fig. 4). Since dislocations cannot cut through the NbC particles because of their large size (>37 nm) [63], the Orowan looping mechanism is the primary precipitation-strengthening mechanism [63], which was used to estimate  $ \Delta\sigma_P $ for (Nb $ _{15} $Ta $ _{10} $W $ _{75} $) $ _{98.5} $C $ _{1.5} $. Due to the rapid cooling rates and the small melt pool sizes associated with the LPBF process, it is difficult for solutes and solute atoms to rapidly diffuse and generate concentration gradient over a larger length scale (of micrometer level) [13]’ [65]. The Toda-Caraballo model can evaluate the solid-solution hardening effect of RMPEAs fabricated using the LPBF process [66]. This model overcomes the difficulty of distinguishing "solute-solvent" in the high entropy alloys, and utilizes a matrix to calculate lattice distortion caused by a small amount of component fluctuations, which is consistent with the atomic diffusion behavior under non-equilibrium conditions.  $ \Delta\sigma_{SSH} $ was assumed to be the same for Nb $ _{15} $Ta $ _{10} $W $ _{75} $ and (Nb $ _{15} $Ta $ _{10} $W $ _{75} $) $ _{98.5} $C $ _{1.5} $, as all the added C precipitates out in the form of NbC.

The contributions of the different strengthening mechanisms to  $ \mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75} $ and  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ at RT are shown in Fig. 13. Their sum, being close to  $ \sigma_{y} $ obtained from the experiment, renders reasonable validity to the methods employed for the estimation.  $ \Delta\sigma_{0} $ and  $ \Delta\sigma_{SSH} $ are the primary contributors to the strength of  $ \mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75} $, providing 430 and 337 MPa respectively, which correspond to 32.9 % and 25.8 % of  $ \sigma_{y} $ [64], respectively.  $ \sigma_{i} $ of Nb, Ta, and W are 240, 189, and 550 MPa, respectively. The high proportion of W content in  $ \mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75} $ significantly enhances  $ \Delta\sigma_{0} $, contributing substantially to  $ \sigma_{y} $. The severe lattice distortion significantly improves  $ \Delta\sigma_{SSH} $ [29], thereby positively contributing to  $ \sigma_{v} $.

In (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅, both \Delta\sigma₀ and \Delta\sigma_SSH continue to be the major strengthening contributors, accounting for 28.3 % and 22.2 % of \sigma_y, respectively. The strengthening effect of these mechanisms does not vary because of negligible variations in the matrix composition. However, the NbC precipitates generated during LPBF of (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅ can pin GBs (from coarsening during the thermal cycles of LPBF) and dislocations, thereby refining grains (Fig. 11) and increasing \rho (Fig. 4). Benefiting from these microstructural modifications, \Delta\sigma_GB and \Delta\sigma_DIS increase to 269 and 313 MPa, respectively. Moreover, the NbC precipitates themselves can also enhance the strength by hindering the dislocation mobility, contributing an additional 167 MPa. Thus, the enhanced strength of (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅ mainly arises from the combination of \Delta\sigma_GB, \Delta\sigma_DIS, and \Delta\sigma_P.

Furthermore,  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ exhibits superior plasticity (8.3%) compared to  $ Nb_{15}Ta_{10}W_{75} $ (5.3%), despite comparable dislocation densities in them (Section 3.2). The higher plasticity is also reflected in the fracture morphologies (Figs.8 ( $ b_{3}-b_{4} $)). This difference in the plastic deformability between the two alloys examined is mainly due to the differences in microstructure. Specifically,  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ contains a higher population of LAGBs than  $ Nb_{15}Ta_{10}W_{75} $ (Figs.11( $ a_{2} $)) and  $ (a_{4}) $), which is caused by the pinning effect of precipitates on grain boundaries (Fig. 6). The high proportion of LAGBs can blunt the crack tips and hinder crack propagation [59], and bear a larger degree of deformation before fracture by homogenizing the strain [60], ultimately improving plasticity and transforming fracture mechanism from partial cleavage to quasi-cleavage.

## 4.4. Effect of the nano-precipitates on HT mechanical properties

Fig.14(a) compares the HT strengths of  $ Nb_{15}Ta_{10}W_{75} $ and  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ with those of other RHEAs reported in literature [67–73]. It shows  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ exceeds all the others at
Fig. 13. Comparison of  $ Nb_{15}Ta_{10}W_{75} $ versus  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ in terms of strengthening mechanisms contributions and proportions.
Fig. 14. A comparison of the (a) HT strengths and (b) softening temperatures and atomic mismatch of various RMPEAs with those examined in this study.

various testing temperatures. The softening temperature ( $ T_{c} $) and atomic mismatch degree ( $ \delta_{r} $) are important aspects of HT strength of alloys and hence can serve as the critical parameters for evaluation [29]. As the temperature is increased, a transition in the dominant deformation mechanism—from screw to edge dislocation mobility dominated regimes—occurs, and  $ T_{c} $ reflects this transition temperature range (usually 0.3–0.5 times melting temperature) [74,75]. A higher  $ T_{c} $ is beneficial for maintaining strength at higher temperatures.  $ \delta_{r} $ reflects the degree of lattice mismatch and is related to the resistance of dislocation movement at HT, and can be estimated using the following equation:

 $$ \delta_{r}=100\sqrt{\sum_{i=1}^{n}c_{i}\left(1-\frac{r_{i}}{\sum_{i=1}^{n}c_{i}r_{i}}\right)^{2}} $$ 

where  $ c_i $ is the atomic fraction of the  $ i^{th} $ element and  $ r_i $ is the atomic radius. Fig.14(b) compares the values of  $ T_c $ and  $ \delta_r $ of  $ Nb_{15}Ta_{10}W_{75} $ and  $ (\text{Nb}_{15}\text{Ta}_{10}\text{W}_{75})_{98.5}\text{C}_{1.5} $ with the respective values reported for other RMPEAs. It is observed that  $ (\text{Nb}_{15}\text{Ta}_{10}\text{W}_{75})_{98.5}\text{C}_{1.5} $ has the highest  $ T_c $ and  $ \delta_r $ values, consistent with its superior HT strength.

The impact of NbC on the HT properties is evaluated by analyzing the work-hardening rates and dislocation types at different compression temperatures. The work-hardening curves, classified into two types (Figs.15 (a1) and (a2)), reveal distinct behaviors based on the compression temperature. Below 1400 ^\circC, the work hardening curves of  $ Nb_{15}\text{Ta}_{10}\text{W}_{75} $ and  $ (\text{Nb}_{15}\text{Ta}_{10}\text{W}_{75})_{98.5}\text{C}_{1.5} $ exhibit high work-hardening rates, indicating strong HT softening resistance. Above 1400 ^\circC, the work hardening behavior shows a significant transformation, with a sharp decrease in hardening rate with true strain in stage I ( $ \varepsilon_T < 10\% $), indicating that dislocation slip occurs readily at this temperature. Besides,  $ (\text{Nb}_{15}\text{Ta}_{10}\text{W}_{75})_{98.5}\text{C}_{1.5} $ exhibits a lower slope in the work-hardening curve ( $ K_{WH} $) than  $ Nb_{15}\text{Ta}_{10}\text{W}_{75} $, indicating stronger resistance to HT deformation. The difference in work-hardening ability is closely related to temperature and micro-deformation mechanisms. To this end, the phase type and  $ \rho $ of compressed samples subjected to  $ \varepsilon_T = 10\% $ at 1400 and 1600 ^\circC are evaluated using XRD, as shown in Fig. 15(b). NbC nano-precipitates still exist in  $ (\text{Nb}_{15}\text{Ta}_{10}\text{W}_{75})_{98.5}\text{C}_{1.5} $ after undergoing HT compression with  $ \varepsilon_T = 10\% $, which is beneficial for HT strength. The value of  $ \rho $, estimated using the Scherrer formula, in  $ (\text{Nb}_{15}\text{Ta}_{10}\text{W}_{75})_{98.5}\text{C}_{1.5} $ is higher than that in  $ Nb_{15}\text{Ta}_{10}\text{W}_{75} $ after HT
Fig. 15. Work hardening rate curves for (a₁) Nb₁₅Ta₁₀W₇₅ and (a₂) (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅ at different compression temperatures; (b) Phase structure, \rho and d of samples compressed at 1400 ^\circC and 1600 ^\circC with \epsilonₜ = 10 % detected by XRD test; BF TEM images of dislocation types in deformed samples with \epsilonₜ = 10 %: Nb₁₅Ta₁₀W₇₅ compressed at (c₁) 1400 ^\circC and (c₂) 1600 ^\circC, (Nb₁₅Ta₁₀W₇₅)₉₈.₅C₁.₅ compressed at (c₃) 1400 ^\circC and (c₄) 1600 ^\circC.

compression (Table 4), which benefits the HT strength [76].

Furthermore, the type of dislocation dominating the deformation plays a critical role in determining the HT strength [75]. The maximum  $ T_c $ of both  $ Nb_{15}Ta_{10}W_{75} $ and  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ is about 1500 ^\circC. Thus, the compression temperature of 1600 ^\circC marks the transition between dislocation types. At temperatures below  $ T_c $, work-hardening curves dominated by the screw dislocations show continuous deformation behavior, while deformation dominated by the edge dislocations at temperatures above  $ T_c $ results in a rapid decrease in the hardening rate [77]. The observed hardening curve conforms to such a change in the pattern, supporting the hypothesis that the HT strength transitions from screw-dominated to edge-dominated dislocation motion. To further clarify the types of dislocations operating at different temperatures, two-beam BF TEM images are obtained from compressed samples subjected to  $ \varepsilon_T = 10\% $ at 1400 and 1600 ^\circC. Results are shown in Figs.15 ( $ c_1-c_4 $). The g vector is marked in each image, and its direction is denoted by a white arrow. b is determined using the  $ g \times b = 0 $ condition; detailed information is provided in Supplementary-Note 5 of supplementary material.  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ shows more dislocation lines than  $ Nb_{15}Ta_{10}W_{75} $, consistent with the higher  $ \rho $ results obtained using XRD. The dislocations are colored according to their respective orientation relationships with b. It is found that there are two kinds of dislocations based on their orientation relationship with different  $ b: \pm 1/2[11-1] $ in red, and  $ \pm 1/2[001], \pm 1/2[111], \pm 1/2[1-11] $ in orange. It is observed that only the edge dislocations exist in the  $ Nb_{15}Ta_{10}W_{75} $ and  $ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $ samples compressed to  $ \varepsilon_T $ of 10 % at 1400 ^\circC. In contrast, both screw and edge dislocations coexist in the samples that

## Table 4

The  $ \rho $ values of samples compressed at 1400 ^\circC and 1600 ^\circC with  $ \varepsilon_{T}=10\% $.

<table border="1" style="margin: auto; word-wrap: break-word;"><tr><td style="text-align: center; word-wrap: break-word;"></td><td colspan="2">$ Nb_{15}Ta_{10}W_{75} $</td><td colspan="2">$ (Nb_{15}Ta_{10}W_{75})_{98.5}C_{1.5} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;"></td><td style="text-align: center; word-wrap: break-word;">1400 ^\circC</td><td style="text-align: center; word-wrap: break-word;">1600 ^\circC</td><td style="text-align: center; word-wrap: break-word;">1400 ^\circC</td><td style="text-align: center; word-wrap: break-word;">1600 ^\circC</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \rho $ ( $ 10^{14}/m^{2} $)</td><td style="text-align: center; word-wrap: break-word;">8.35</td><td style="text-align: center; word-wrap: break-word;">5.35</td><td style="text-align: center; word-wrap: break-word;">9.67</td><td style="text-align: center; word-wrap: break-word;">5.71</td></tr></table>

were compression tested at 1600 ^\circC ( $ \varepsilon_{T}=10\% $). The accumulation of dislocations at the GBs, which is also observed, increases the back stress that could hinder dislocation glide. The average dislocation velocity ( $ \nu_{d} $) is estimated using the Orowan equation [78,79]:

 $$ \mathbf{v_{d}}={\frac{\varepsilon_{\nu}}{\rho b}} $$ 

 $$ \varepsilon_{\nu}=\frac{\varepsilon_{L}}{H} $$ 

where  $ \rho $ is obtained from the XRD results (see Table 4),  $ \varepsilon_{v} $ is the strain rate, H is the height of the HT compressed sample,  $ \varepsilon_{L} $ is a constant loading rate of HT compression. At temperatures below  $ T_{c} $, only pure edge dislocations survived in the compressed samples  $ Nb_{15}Ta_{10}W_{75} $ and  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $. This is because of the difficulty of screw dislocation cores dissociating into nonplanar structures during motion, while edge dislocations tend to divide into segments that slip more easily along the glide planes [72]. Therefore, screw dislocations are more prone to annihilation than edge dislocations, leading to the survival of pure edge dislocations and dominating the slip rate and HT strength. The estimated velocity of screw dislocations ( $ \nu_{ds} $) in  $ Nb_{15}Ta_{10}W_{75} $ and  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ compressed at 1400 ^\circC are 1.51 and 1.30 mm/s, respectively. When the temperature exceeds  $ T_{c} $, numerous Frank-Read sources are activated for dislocation multiplication, promoting the glide of the screw dislocations, whereas edge dislocations are less influenced. With deformation, the speed of screw dislocations becomes comparable to those of edge dislocations ( $ \nu_{de} $), consequently maintaining the HT strength. The screw and edge dislocations in  $ Nb_{15}Ta_{10}W_{75} $ and  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ at 1600 ^\circC have similar mobilities, with  $ \nu_{ds} = \nu_{de} = 2.36 $ mm/s for  $ Nb_{15}Ta_{10}W_{75} $ and  $ \nu_{ds} = \nu_{de} = 2.21 $ mm/s for  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $. The HT strength of  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ increases by about 111 MPa at 1400 ^\circC and 110 MPa at 1600 ^\circC compared to  $ Nb_{15}Ta_{10}W_{75} $, attributed to the impediment of screw/edge dislocation movement by the NbC particles. Based on these results, it can be concluded that the NbC nano-precipitates can stably survive at HT and

effectively impede screw/edge dislocation movement at HT, leading to higher  $ \rho $ and improved HT strength.

## 5. Summary and conclusions

A design strategy for composite RMPEAs, suitable for LPBF via ceramic powder addition and in-situ nano-precipitate formation, was developed to simultaneously enhance printability, reduce anisotropy, and sustain strength at HT conditions. The main conclusions of this study are the following.

1) By estimating the solid solubility and critical re-precipitation amounts of the in-situ nano-precipitates, and measuring the powder flowability and laser absorptivity, we found that adding 1.5 at. % WC powder to matrix powders promotes the formation of in-situ phase and improves the print quality.

2) Incorporating 1.5 at. % WC powder also enhanced the laser absorptivity from 71 % to 86 % without compromising powder flowability, expanding printing ranges of about 50 Jmm $ ^{-3} $, reducing LOF pores, and improves the printed part density from 99.2 \pm 0.15 % to 99.5 \pm 0.1 %.

3) During LPBF, the added WC powder particles dissolve in the melt pool and the C combines with Nb to form NbC in-situ. These precipitates, subsequently, act as heterogeneous nucleates to shorten solidification distance and inhibit columnar grain growth. As a result, a substantial reduction in microstructural and mechanical anisotropy is obtained. Moreover,  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ exhibits a superior yield strength at RT, which is attributed to the grain boundary, dislocation, and precipitation strengthening mechanisms. The HT strength of  $ (\mathrm{Nb}_{15}\mathrm{Ta}_{10}\mathrm{W}_{75})_{98.5}\mathrm{C}_{1.5} $ also increased due to the suppression of dislocation mobility by the NbC nano-precipitates.

## CRediT Authorship

Ran Duan: Writing – review & editing, Writing – original draft, Validation, Methodology, Data curation. Yakai Zhao: Writing – review & editing, Validation, Supervision. Xiaodan Li: Resources, Methodology. Jintao Xu: Validation, Investigation. Meng Qin: Validation, Investigation, Data curation. Kai Feng: Writing – review & editing, Project administration, Methodology, Funding acquisition, Conceptualization. Zhuguo Li: Resources, Project administration, Methodology, Funding acquisition. Beibei Xu: Visualization, Validation, Software, Resources, Formal analysis, Data curation. Upadrasta Ramamurty: Writing – review & editing, Supervision, Methodology, Investigation, Formal analysis, Data curation, Conceptualization.

## Declaration of Competing Interest

The authors declare that they do not have any commercial or associative interest that could have appeared to influence the work reported in this paper.

## Acknowledgements

This work was financially supported by National Key R&D Program of China (No. 2022YFB4602102), Shanghai Collaborative Innovation Project (No. HCXBCY-2023-064). We would like to acknowledge the support from the Instrumental Analysis Center of Shanghai Jiao Tong University and Instrument and equipment sharing platform of School of Materials Science and Engineering, SJTU. YZ would like to thank the support by A*STAR via the Advanced Models for Additive Manufacturing (AM2) programme (No. M22L2b0111).

## Supplementary Materials

## Supplementary Material

## References

[1] E.P. George, D. Raabe, R.O. Ritchie, High-entropy alloys, Nat. Rev. Mater. 4 (2019) 515–534.

[2] Y.K. Zhao, D.H. Lee, M.Y. Seok, J.A. Lee, M.P. Phaniraj, J.Y. Suh, H.Y. Ha, J.Y. Kim, U. Ramamurty, J.I. Jang, Resistance of CoCrFeMnNi high-entropy alloy to gaseous hydrogen embrittlement, Scripta. Mater. 135 (2017) 54–58.

[3] D.H. Lee, M.Y. Seok, Y.K. Zhao, I.C. Choi, J.Y. He, Z.P. Lu, J.Y. Suh, U. Ramamurty, M. Kawasaki, T.G. Langdon, J.I. Jang, Spherical nanoindentation creep behavior of nanocrystalline and coarse-grained CoCrFeMnNi high-entropy alloys, Acta. Mater. 109 (2016) 314–322.

[4] J. Gubicza, A. Heczel, M. Kawasaki, J.K. Han, Y.K. Zhao, Y.F. Xue, S. Huang, J. L. Lábar, Evolution of microstructure and hardness in Hf_{25}Nb_{25}Ti_{25}Zr_{25} high-entropy alloy during high-pressure torsion, J. Alloy. Compd. 788 (2019) 318–328.

[5] A.H. Jeon, Y.K. Zhao, Z. Gao, J.Y. Suh, H.J. Ryu, H.S. Kim, U. Ramamurty, J. I. Jang, Stochastic nature of incipient plasticity in a body-centered cubic medium-entropy alloy, Acta. Mater. 278 (2024) 120244.

[6] R. Feng, B. Feng, M.C. Gao, C. Zhang, J.C. Neuefeind, J.D. Poplawsky, Y. Ren, K. An, M. Widom, P.K. Liaw, Superior High-Temperature Strength in a Supersaturated Refractory High-Entropy Alloy, Adv. Mater. 33 (48) (2021) 2102401.

[7] P. Kumar, S. Huang, D.H. Cook, K. Chen, U. Ramamurty, X.P. Tan, R.O. Ritchie, A strong fracture-resistant high-entropy alloy with nano-bridged honeycomb microstructure intrinsically toughened by 3D-printing, Nat. Commun. 15 (2024) 841.

[8] O.N. Senkov, D.B. Miracle, K.J. Chaput, J.P. Couzinie, Development and exploration of refractory high entropy alloys—A review, J. Mater. Res. 33 (19) (2018) 3092–3128.

[9] O.N. Senkov, G.B. Wilks, D.B. Miracle, C.P. Chuang, P.K. Liaw, Refractory high-entropy alloys, Intermetallics 18 (9) (2010) 1758–1765.

[10] C.Y. Yap, C.K. Chua, Z.L. Dong, Z.H. Liu, D.Q. Zhang, L.E. Loh, S.L. Sing, Review of selective laser melting: materials and applications, Appl. Phys. Rev. 2 (4) (2015) 041101.

[11] Z. Li, Y.N. Cui, W.T. Yan, D. Zhang, Y. Fang, Y.J. Chen, Q. Yu, G. Wang, H. Ouyang, C. Fan, Q. Guo, D.B. Xiong, S.B. Jin, G. Sha, N. Ghoniem, Z. Zhang, Y.M. Wang, Enhanced strengthening and hardening via self-stabilized dislocation network in additively manufactured metals, Mater. Today. 50 (2021) 79–88.

[12] D. Wang, L. Liu, G. Deng, C. Deng, Y. Bai, Y. Yang, W. Wu, J. Chen, Y. Liu, Y. Wang, X. Lin, C. Han, Recent progress on Additive manufacturing of multi-material structures with laser powder bed fusion, Virtual. Phys. Prototy. 17 (2) (2022) 329–365.

[13] S. Chandra, J. Radhakrishnan, S. Huang, S.Y. Wei, U. Ramamurty, Solidification in metal additive manufacturing: challenges, solutions, and opportunities, Prog. Mater. Sci. 148 (2025) 101361.

[14] A. Roh, D. Kim, S. Nam, D.I. Kim, H.Y. Kim, K.A. Lee, H. Choi, J.H. Kim, NbMoTaW refractory high entropy alloy composites strengthened by in-situ metal-non-metal compounds, J. Alloy. Compd. 822 (2020) 153423.

[15] J. Sun, P. Kumar, P. Wang, U. Ramamurty, X.H. Qu, B.C. Zhang, Effect of columnar-to-equiaxed microstructural transition on the fatigue performance of a laser powder bed fused high-strength Al alloy, J. Mater. Sci. Technol. 227 (2025) 276–288.

[16] S.Y. Wei, P. Wang, L. Zhang, U. Ramamurty, Grain morphologies in additively manufactured alloys: from solidification fundamentals to advanced microstructure control, J. Mater. Sci. Technol. 235 (2025) 133–145.

[17] D.Y. Zhang, A. Prasad, M.J. Bermingham, C.J. Todaro, M.J. Benoit, M.N. Patel, D. Qiu, D.H. StJohn, M. Qian, M.A. Easton, Grain Refinement of Alloys in Fusion-Based Additive Manufacturing Processes, Metall. Mater. Trans. A. 51 (2020) 4341–4359.

[18] Y.K. Zhao, K.B. Lau, W.H. Teh, J.J. Lee, F.X. Wei, M. Lin, P. Wang, C.C. Tah, U. Ramamurty, Compositionally graded CoCrFeNiTix high-entropy alloys manufactured by laser powder bed fusion: a combinatorial assessment, J. Alloy. Compd. 883 (2021) 160825.

[19] Y.X. Wan, Study On the Preparation and Mechanical Properties of Rare Metals Nb/Mo/Ta/W Based Ultra-High-Temperature High-entropy Alloys, China University of Mining and Technology, 2021.

[20] T.K. Kai, H. Hsuan, W.W. Ren, Y.J. Wei, T.C. Wei, Edge-dislocation-induced ultrahigh elevated temperature strength of HfMoNbTaW refractory high-entropy alloys, Sci. Technol. Adv. Mat. 23 (1) (2022) 642–654.

[21] L. Wang, Z.X. Guo, G.C. Peng, S.W. Wu, Y.M. Zhang, W.T. Yan, Evaporation-Induced Composition Evolution in Metal Additive Manufacturing, Adv. Funct. Mater. 24 (2024) 12071.

[22] Z. Sun, Y. Ma, D. Ponge, S. Zaefferer, E.A. Jägle, B. Gault, A.D. Rollett, D. Raabe, Thermodynamics-guided alloy and process design for dditive manufacturing, Nat. Commun. 13 (1) (2022) 4361.

[23] R. Duan, J.T. Xu, Y.K. Zhao, Q.J. Zhou, Z.Y. Yan, Y. Xie, P. Dong, K. Feng, Z.G. Li, X.B. Liang, U. Ramamurty, High entropy alloys amenable for laser powder bed fusion: a thermodynamics guided machine learning search, Addit. Manuf. 86 (2024) 104195.

[24] Q.Y. Tan, Y. Yin, M.X. Zhang, Comparison of the Grain-Refining Efficiencies of Ti and LaB6 Inoculants in Additively Manufactured 2024 Aluminum Alloy: the Important Role of Solutes, Metals-Basel 13 (8) (2023) 1490.

[25] C. Guo, G. Li, S. Li, X.G. Hu, H.X. Lu, X.G. Li, Z. Xu, Y.H. Chen, Q.Q. Li, J. Lu, Q. Zhu, Additive manufacturing of Ni-based superalloys: residual stress,

mechanisms of crack formation and strategies for crack inhibition, Nano. Mater. Sci. 5 (1) (2023) 53–77.

[26] C.L. Tan, J. Zou, D. Wang, W.Y. Ma, K. Zhou, Duplex strengthening via SiC addition and in-situ precipitation in additively manufactured composite materials, Compos. Part b-Eng. 236 (2022) 109820.

[27] Z. Chen, X.L. Wen, W.L. Wang, X. Lin, H.O. Yang, Z. Jiang, L.Y. Chen, H.B. Wu, W.H. Li, N. Li, Engineering fine grains, dislocations and precipitates for enhancing the strength of TiB2-modified CoCrFeMnNi high-entropy alloy using laser powder bed fusion, J. Mater. Res. Technol. 26 (2023) 1198–1213.

[28] J. Hu, X. Lin, Y.l. Hu, High wear resistance and strength of Hastelloy X reinforced with TiC fabricated by laser powder bed fusion additive manufacturing, Appl Surf Sci 648 (2024) 159004.

[29] R. Duan, Y.K. Zhao, J.T. Xu, Q.J. Zhou, Z.Y. Yan, Y. Xie, P. Dong, K. Feng, Z.G. Li, B.B. Xu, X.B. Liang, U. Ramamurty, Additive manufacturing of refractory multi-principal element alloy with ultrahigh-temperature strength via simultaneous enhancements in printability and solid solution hardening, Addit. Manuf. 91 (2024) 104340.

[30] J.L. Zhang, J.B. Gao, B. Song, L.J. Zhang, C.J. Han, C. Cai, K. Zhou, Y.S. Shi, A novel crack-free Ti-modified Al-Cu-Mg alloy designed for selective laser melting, Addit. Manuf. 38 (2021) 101829.

[31] Q. Ge, D.D. Gu, D.H. Dai, C.L. Ma, Y.X. Sun, X.Y. Shi, Y.Z. Li, H.M. Zhang, H.Y. Chen, Mechanisms of laser energy absorption and melting behavior during selective laser melting of titanium-matrix composite: role of ceramic addition, J. Phys. D. Appl. Phys. 54 (2021) 115103.

[32] M.A. Balbaa, A. Ghasemi, E. Fereiduni, M.A. Elbestawi, S.D. Jadhav, J.P. Kruth, Role of powder particle size on laser powder bed fusion processability of AlSi10mg alloy, Addit. Manuf. 37 (2021) 101630.

[33] P.D. Niu, R.D. Li, T.C. Yuan, S.Y. Zhu, C. Chen, M.B. Wang, L. Huang, Microstructures and properties of an equimolar AlCoCrFeNi high entropy alloy printed by selective laser melting, Intermetallics 104 (2019) 24–32.

[34] P. Gu, T. Qi, L. Chen, T. Ge, X. Ren, Manufacturing and analysis of VNbMoTaW refractory high-entropy alloy fabricated by selective laser melting, Int. J. Refract. Met. H. 54 (11) (2022) 115103.

[35] D.W. Wang, H.L. Han, B. Sa, K.L. Li, J.J. Yan, J.Z. Zhang, J.G. Liu, Z.D. He, N. Wang, M. Yan, A review and a statistical analysis of porosity in metals additively manufactured by laser powder bed fusion, Opto-Electron. Adv. 5 (10) (2022) 34.

[36] J.Y. He, H. Wang, H.L. Huang, X.D. Xu, M.W. Chen, Y. Wu, X.J. Liu, T.G. Nieh, K. An, Z.P. Lu, A precipitation-hardened high-entropy alloy with outstanding tensile properties, Acta. Mater. 102 (2016) 187–196.

[37] Y.H. Zhao, X.Z. Liao, Z. Jin, R.Z. Valiev, Y.T. Zhu, Microstructures and mechanical properties of ultrafine grained 7075 Al alloy processed by ECAP and their evolutions during annealing, Acta. Mater. 52 (15) (2004) 4589–4599.

[38] N.T. Tayade, M.P. Tirpude, Frustrated microstructures composite PbS material's size perspective from XRD by variant models of Williamson–Hall plot method, B. Mater. Sci. 46 (20) (2023) 102843.

[39] H.W. Deng, M.M. Wang, Z.M. Xie, T. Zhang, X.P. Wang, Q.F. Fang, Y. Xiong, Enhancement of strength and ductility in non-equiatomic CoCrNi medium-entropy alloy at room temperature via transformation-induced plasticity, Mat. Sci. Eng. A Struct. 804 (2021) 140516.

[40] D. Thomas, D. Patricia, C.J. Marc, L. Williams, F.D. Geuser, D. Alexis, Size distribution and volume fraction of T1 phase precipitates from TEM images: direct measurements and related correction, Micron 78 (2015) 19–27.

[41] A. Roy, P. Sreeramagiri, T. Babuska, B. Krick, P.K. Ray, G. Balasubramanian, Lattice distortion as an estimator of solid solution strengthening in high-entropy alloys, Mater. Charact. 172 (2021) 110877.

[42] X.C. Yang, X.J. Di, Q.Y. Duan, W. Fu, L.Z. Ba, C.N. Li, Effect of precipitation evolution of NiAl and Cu nanoparticles on strengthening mechanism of low carbon ultra-high strength seamless tube steel, Mat. Sci. Eng. A-Struct. 872 (2023) 144939.

[43] S. Yin, Y. Zuo, A.A. Odeh, H. Zheng, X.G. Li, J. Ding, S.P. Ong, M. Asta, R. O. Ritchie, Atomistic simulations of dislocation mobility in refractory high-entropy alloys and the effect of chemical short-range order, Nat. Commun. 12 (1) (2021) 4873.

[44] Y.G. Liu, J.Q. Zhang, R.M. Niu, M. Bayat, Y. Zhou, Y. Yin, Q.Y. Tan, S.Y. Liu, J. H. Hattel, M.Q. Li, X.X. Huang, J. Cairney, Y.S. Chen, M. Easton, C. Hutchinson, M. X. Zhang, Manufacturing of high strength and high conductivity copper with laser powder bed fusion, Nat. Commun. 15 (2024) 1283.

[45] D. Huang, J. Yan, X. Zuo, Co-precipitation kinetics, microstructural evolution and interfacial segregation in multicomponent nano-precipitated steels, Mater. Charact. 155 (2019) 109786.

[46] X.Q. Liu, C.C. Wang, Y.F. Zhang, L.Y. Wang, W. Xu, Design of a 2.7 GPa ultra-high-strength high Co-Ni secondary hardening steel by two-step nano-size precipitation tailoring, J. Mater. Process. Tech. 28 (2024) 4212–4221.

[47] S. Guan, K. Solberg, D. Wan, F. Berto, T. Welo, T.M. Yue, K.C. Chan, Formation of fully equiaxed grain microstructure in additively manufactured AlCoCrFeNiTi0.5 high entropy alloy, Mater. Design. 184 (2019) 108202.

[48] X. Li, Y. Feng, B. Liu, D. Yi, X. Yang, W. Zhang, G. Chen, Y. Liu, P. Bai, Influence of NbC particles on microstructure and mechanical properties of AlCoCrFeNi high-entropy alloy coatings prepared by laser cladding, J. Alloy. Compd. 788 (2019) 485–494.

[49] G. Neumann, C. Tuijn, Self-diffusion and Impurity Diffusion in Pure metals: Handbook of Experimental Data, Elsevier, 2011.

[50] G. Wang, Y.M. Zhang, B.K. Zou, Y. Liu, S.Q. Zheng, X.C. Li, W.T. Yan, Z. Li, Y.M. Wang, Enhanced plasticity due to melt pool flow induced uniform dispersion of reinforcing particles in additively manufactured metallic composites, Int. J. Plasticity. 164 (2023) 103591.

[51] Y.A. Coutinho, S.C.K. Rooney, E.J. Payton, Analysis of ebsd grain size measurements using microstructure simulations and a customizable pattern matching library for grain perimeter estimation, Metall. Mater. Trans. A. 48 (5) (2017) 2375–2395.

[52] Z.J. Fan, C. Li, H.L. Yang, Z.L. Liu, Effects of TiC nanoparticle inoculation on the hot-tearing cracks and grain refinement of additively-manufactured AA2024 Al alloys, J. Mater. Process. Tech. 19 (2022) 194–207.

[53] K. Fu, Y.Y. Liu, Y.Q. Wang, Z. Xu, W. Jiang, Z. Chen, S.Q. Liu, L. Sun, Z.L. Zhang, J. Y. He, Grain refinement of Ti6Al4V by incorporating in-situ TiB nanowhiskers in laser melting depositions, J. Mater. Process. Tech. 27 (2023) 2893–2901.

[54] S.N. Tedman-Jones, S.D. McDonald, M.J. Bermingham, D.H. Stjohn, M. S. Dargusch, Investigating the morphological effects of solute on the  $ \beta $-phase in as-cast titanium alloys, J. Alloy. Compd. 788 (2019) 204–214.

[55] B. Yin, H.W. Ma, Y.D. Wang, H. Zhao, G. Jin, J.M. Wang, Modeling and application of continuous growth restriction factor for elucidating development of as-welded grain size, J. Alloy. Compd. 739 (2018) 901–908.

[56] S.N. Tedman-Jones, M.J. Bermingham, S.D. McDonald, D.H. StJohn, M. S. Dargusch, Titanium sponge as a source of native nuclei in titanium alloys, J. Alloy. Compd. 818 (2019) 153353.

[57] H.Y. Liu, S. Wang, J. Liang, H. Hu, Q.T. Li, H.R. Chen, Effect of Lanthanum Oxide on the Microstructure and Properties of Ti-6Al-4V Alloy during CMT-Additive Manufacturing, Crystals 13 (3) (2023) 515.

[58] Q.Y. Tan, M.X. Zhang, Recent advances in inoculation treatment for powder-based additive manufacturing of aluminium alloys, Mat. Sci. Eng. R. 158 (2024) 100773.

[59] Y.N. Zhao, T. Ma, Z.J. Gao, Y.Y. Feng, C. Li, Q.Y. Guo, Z.Q. Ma, Y.C. Liu, Significant reduction of grain size and texture intensity in laser powder bed fusion fabricated nickel-based superalloy by increasing constitutional supercooling, Compos. Part. B-Eng. 266 (2023) 111040.

[60] Z.Y. Ji, C.L. Qiu, Achieving superior high-temperature strength in an additively manufactured high-entropy alloy by controlled heat treatment, Appl. Mater. Today. 40 (2024) 102412.

[61] H.B. Dai, H.W. Zhao, Y.H. Xia, X.Y. Cai, B.L. Dong, S.B. Lin, Y. Zhao, Wire arc additive manufacturing of ZL205A: heat input effect on the forming quality, pore defects and mechanical properties, J. Alloy. Compd. 1005 (2024) 175777.

[62] X.H. Du, W.P. Li, H.T. Chang, T. Yang, G.S. Duan, B.L. Wu, J.C. Huang, F.R. Chen, C.T. Liu, W.S. Chuang, Y. Lu, M.L. Sui, E.W. Huang, Dual heterogeneous structures lead to ultrahigh strength and uniform ductility in a Co-Cr-Ni medium-entropy alloy, Nat. Commun. 11 (1) (2020) 2390.

[63] W. Fu, C.N. Li, X.J. Di, J.J. Wang, K.J. Fu, W.Y. Hu, D.P. Wang, Effect of peak temperature on nanoscale Cu-rich re-precipitation behavior and strength-toughness of welding heat affected zones for Cu-bearing high strength steel, Mater. Charact. 199 (2023) 112809.

[64] X.F. Xie, Z.M. Xie, R. Liu, Q.F. Fang, C.S. Liu, W.Z. Han, X. Wu, Hierarchical microstructures enabled excellent low-temperature strength-ductility synergy in bulk pure tungsten, Acta. Mater. 228 (2022) 165187.

[65] D.H. Lee, J.A. Lee, Y.K. Zhao, Z.P. Lu, J.Y. Suh, J.Y. Kim, U. Ramamurty, M. Kawasaki, T.G. Langdon, J.I. Jang, Annealing effect on plastic flow in nanocrystalline CoCrFeMnNi high-entropy alloy: a nanomechanical analysis, Acta. Mater. 140 (2017) 443–451.

[66] I. Toda-Caraballo, A general formulation for solid solution hardening effect in multicomponent alloys, Scripta. Mater. 127 (2017) 113–117.

[67] J.P. Couzinie, O.N. Senkov, D.B. Miracle, G. Dirras, Comprehensive data compilation on the mechanical properties of refractory high-entropy alloys, Data. Brief. 21 (2018) 1622–1641.

[68] Z.D. Han, N. Chen, S.F. Zhao, L.W. Fan, G.N. Yang, Y. Shao, K.F. Yao, Effect of Ti additions on mechanical properties of NbMoTaW and VNbMoTaW refractory high entropy alloys, Intermetallics 84 (2017) 153–157.

[69] S. Wu, D. Qiao, H. Zhao, J. Wang, Y. Lu, A novel NbTaW0.5(Mo2C)x refractory high-entropy alloy with excellent mechanical properties, J. Alloy. Compd. 889 (2021) 161800.

[70] S. Alvi, O.A. Waseem, F. Akhtar, High Temperature Performance of Spark Plasma Sintered W_{0.5}(TaTiVCr)0.5 Alloy, Metals-Basel 10 (11) (2020) 1512.

[71] Y. Zhang, Q. Wei, P. Xie, X. Xu, An ultrastrong niobium alloy enabled by refractory carbide and eutectic structure, Mater. Res. Lett. 11 (3) (2022) 169–178.

[72] S. Wu, D. Qiao, H. Zhang, J. Miao, H. Zhao, J. Wang, Y. Lu, T. Wang, T. Li, Microstructure and mechanical properties of C Hf_{0}.25NbTaW0.5 refractory high-entropy alloys at room and high temperatures, J. Mater. Sci. Technol. 97 (2022) 229–238.

[73] K.K. Tseng, C.C. Juan, S. Tso, H.C. Chen, C.W. Tsai, J.W. Yeh, Effects of Mo, Nb, Ta, Ti, and Zr on Mechanical Properties of Equiatomic Hf-Mo-Nb-Ta-Ti-Zr Alloys, Entropy-Switz 21 (1) (2018) 15.

[74] C. Baruffi, F. Maresca, W.A. Curtin, Screw vs. edge dislocation strengthening in body-centered-cubic high entropy alloys and implications for guided alloy design, Mrs. Commun. 12 (6) (2022) 1111–1118.

[75] W. Huang, J. Hou, X. Wang, J. Qiao, Y. Wu, Excellent room-temperature tensile ductility in as-cast Ti_{37}V_{15}Nb_{22}Hf_{23}W_{3} refractory high entropy alloys, Intermetallics 151 (2022) 107735.

[76] X.R. Zhou, X.Y. Wang, L. Fey, S.C. He, I. Beyerlein, P.H. Cao, J. Marian, Models of dislocation glide and strengthening mechanisms in bcc complex concentrated alloys, Mrs. Bull. 12 (2023) 1111–1118.

## R. Duan et al.

[77] C. Xiang, C. Han, M. Siming, Insights into flow stress and work hardening behaviors of a precipitation hardening AlMgScZr alloy: experiments and modeling, Int. J. Plasticity. 172 (2024) 103852.

[78] Y. Lu, Y.H. Zhang, E. Ma, W.Z. Han, Relative mobility of screw versus edge dislocations controls the ductile-to-brittle transition in metals, P. Natl. Acad. Sci. USA. 118 (37) (2021) 21105.

[79] P. Kumar, M. Michalek, D.H. Cook, H. Sheng, K.B. Lau, P. Wang, M.W. Zhang, A.M. Minor, U. Ramamurty, R.O. Ritchie, On the strength and fracture toughness of an additive manufactured CrCoNi medium-entropy alloy, Acta. Mater. 258 (2023) 119249.