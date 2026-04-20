DOI: 10.1016/j.addma.2021.101912

Research Paper

# Densification, microstructure, and mechanical properties of heat-treated MAR-M247 fabricated by Binder Jetting

T. Dahmen $ ^{a,*} $, N.G. Henriksen $ ^{a} $, K.V. Dahl $ ^{a} $, A. Lapina $ ^{b} $, D.B. Pedersen $ ^{a} $, J.H. Hattel $ ^{a} $, T. L. Christiansen $ ^{a} $, M.A.J. Somers $ ^{a} $

 $ ^{a} $ Department of Mechanical Engineering, Technical University of Denmark, Produktionstorvet, Building 425, 2800 Kgs. Lyngby, Denmark

 $ ^{b} $ MAN Energy Solutions, Teglholmsgade 41, 2450 Copenhagen, Denmark

## ARTICLE INFO

## Keywords

Binder Jetting

MAR M247 superalloy

Turbine engine

Hot isostatic pressing

Additive Manufacturing

## Abstract

Additive Manufacturing (AM) enables the design of complex part geometries for high-temperature applications. Laser Powder Bed Fusion or Direct Energy Deposition of the nickel-based superalloy MAR-M247 poses a challenge in AM due to its poor weldability. Binder Jetting does not utilize a heat source and interaction with a liquid metal during build-up and thus has the potential to overcome this limitation. In this study, MAR-M247 was manufactured by Binder Jetting and subsequently characterized regarding density and microstructure. Combinations of two different Hot-Isostatic-Pressing (HIP) treatments (T = 1120–1180 ^\circC, p = 1000–1500 bar, t = 4 h) and four different heat-treatments involving solution treatment (T = 1250 ^\circC, t = 4 h) and different aging steps (T = 700–1000 ^\circC, t = 12–24 h) were applied to study the densification and microstructural evolution of binder-jetted MAR-M247. The influence of the build direction in combination with HIP is studied concerning the resulting density and mechanical properties at room temperature. The results show that close-to-full densification can be achieved after HIP. Subsequent solution treatment and double-aging after HIP lead to a favorable bimodal microstructure. A process chain for binder-jetted MAR-M247 is presented, which yields tensile properties comparable to those of analogously post-processed cast material. Further possibilities of microstructural optimization and the design philosophy are discussed in the light of the Binder Jetting process-chain.

## 1. Introduction

Additive Manufacturing (AM) of complex components based on nickel-based superalloys is increasingly adopted in the aerospace and energy sector [1,2]. Examples of such applications include turbine blades, compressor blades and blisks, gas burners, and fuel injectors [3–8]. Hastelloy X, IN625, IN718, and IN939 are commonly applied nickel-based superalloys and are successfully processed by Laser Powder Bed Fusion (LPBF) or Direct Energy Deposition (DED) [9]. However, the portfolio of available superalloys for AM is continuously expanding, including efforts of processing more advanced nickel-based superalloys such as the MAR-M247 alloy.

The MAR-M247 superalloy was initially developed for vacuum investment casting of turbine components by the Martin Marietta Corporation in the early 1970s [10]. The microstructure of the alloy is characterized by a high volume fraction of  $ \gamma' $-phase  $ [Ni_{3}(Al, Ti)] $ dispersed in a  $ \gamma $-matrix [Ni] that contains carbide precipitates along the grain boundaries. The alloying elements Co, W, Cr, and Mo, strengthen the  $ \gamma $-matrix by solid solution strengthening. Furthermore, Hf, B, and Zr are present as (stable) primary carbides. After casting, the alloy requires a solution-treatment and age-hardening, typically in multiple steps [11]. Overall, the resulting microstructure imparts the material with superior mechanical strength, high creep resistance, and resistance to hot corrosion at high temperatures. However, the material (microstructure) is associated with extreme challenges when it comes to weldability [12]. Due to the obtainable high volume fraction of  $ \gamma' $-phase, the alloy is prone to lose its ductility through precipitation hardening that occurs within the range of aging temperatures of the alloy. Consequently, upon reheating through welding and post-weld heat treatments, the material becomes susceptible to different cracking mechanisms, which were identified as solidification cracking, liquation cracking, strain-age cracking, and ductility-dip cracking [13].

Nevertheless, numerous studies can be found in the AM literature to process and investigate the crack-behavior of MAR-M247 or its low

carbon derivative CM247LC by conventional L-PBF, DED or Electron Beam Melting (EBM) [14–19]. However, crack-free processing of MAR-M247 has so far only been achieved by employing highly specialized L-PBF or DED equipment, including in-situ high-temperature induction heating in the range of 700–1200 ^\circC or single-layer scanning laser epitaxy on top of cast MAR-M247 substrates [20–22]. Hence, the fusing of MAR-M247 by lasers currently entails additional costs or compromises in design freedom when compared to the processing of other commercially available AM superalloys.

Binder Jetting (BJ), as a promising alternative metal AM process, has the potential to overcome these limitations by its process-inherent separation between the form-shaping and fusing step. Consequently, Binder Jetting does not only possess the ability to process a wide range of materials, including non-weldable materials but also pushes the level of achievable productivity within metal AM. In recent years, Binder Jetting has gained more momentum due to progress in achieving high densities for various materials, including superalloys such as IN625 and IN718 [23–25]. Hot-isostatic-pressing (HIP) is considered to be a promising post-processing treatment in other metal AM processes such as LPBF and EBM to remove the remaining porosity [26]. However, close to full density (>99.5%) through HIP in binder-jetted components has not been reported in the literature yet [27].

Recently, Persson et al. suggested a process-window for Binder Jetting of MAR-M247 [28]. The present study, for the first time, characterizes the microstructure and mechanical properties of the sintered, hot-isostatically pressed, and heat-treated MAR-M247 specimens made by Binder Jetting. The findings are compared to conventionally manufactured MAR-M247, and further possibilities of microstructural optimization are discussed in the light of the Binder Jetting process-chain.

## 2. Methods

## 2.1. Binder Jetting of MAR-M247

Gas-atomized MAR-M247 powder $ ^{1} $ was used as a feedstock material for the Binder Jetting process. A secondary electron image of MAR-M247 powder shows a spherical morphology being typical for the applied atomization technique (Fig. 1).

The median particle size at 50% of the volume distribution, D50, was
Fig. 1. SEM image of gas atomized MAR-M247 powder.

15  $ \mu $m. The chemical composition of the used powder was determined by Inductively Coupled Plasma Mass Spectroscopy (ICP-MS). Table 1 shows the composition, which lies within the specifications of MAR-M247 [10].

The specimens in this work were manufactured on a DMP2500 system (Digital Metal AB, Sweden) with a layer thickness of 42  $ \mu $m and an approximate droplet volume of 30 picoliter. The Binder Jetting process was performed in an ambient atmosphere at room temperature. An aqueous binder, C20, was used, and the saturation was set to Dark 3, which corresponds to 69% of the pixels being saturated. The main working principle of the Binder Jetting process is illustrated in Fig. 2.

Two different specimen geometries were manufactured: cuboids for microstructural analysis and hexagonal prisms for tensile testing, as shown in Fig. 3. Based on earlier findings, a volumetric scaling factor of 1.79 was applied [28]. Thus, the specimen sizes were scaled 21% in the horizontal plane (x- and y-direction) and 22% in the vertical direction (z-direction) to compensate for shrinkage on sintering. The hexagonal tensile specimens were manufactured in both the vertical and horizontal build orientations.

## 2.2. Post-processing, HIP, and heat treatments

After manufacturing, the specimens were cured in an ambient atmosphere at 200 ^\circC for 8 h, depowdered with compressed air, and removed from the building box. Subsequent thermal debinding was performed in an ambient atmosphere at 345 ^\circC for three hours. Thereafter, the specimens were sintered in an H800 SF vacuum furnace (Vacua Therm Ltd., UK) at 1320 ^\circC and approximately 0.1 Pa for 6 h and finally slowly cooled in the furnace (< 20 ^\circC/min).

Thereafter, the specimens received different combinations of HIP and heat treatments. First, samples in the sintered condition and HIP conditions were investigated with respect to microstructure, hardness, and density. Secondly, the influence of heat treatments on microstructural evolutions was investigated and compared to the initial conditions. Based on the results, one HIP cycle and heat treatment combination was chosen for the tensile specimens. Finally, the tensile properties were obtained at room temperature. In Fig. 4, an overview of the experimental procedure, including the applied process-chains in this work, is shown.

The two different HIP cycles were based on the supplier’s recommendation (Quintus Technologies AB, Sweden) and executed in argon (see Table 2). Thereby, similar HIP parameters for conventionally manufactured MAR-M247 from the literature were followed [29,30], and an additional combination with lower temperature and pressure was chosen to limit potential grain growth and permit the analysis of possible left-over porosity.

Four different heat treatments (HT1–HT4) were applied, consisting of one to three steps (Table 3). HT1 aimed to create a uniform size distribution of  $ \gamma' $-precipitates, while HT2 aimed to realize a bi-modular size distribution. HT3 and 4 were chosen to evaluate the effect of aging and double-aging in the HIP1 condition, respectively, without including a separate solution treatment. The heat treatments, HT1 and HT2, were only applied to the as-sintered condition, while HT1-4 were applied in the condition after the HIP1-treatment.

The cuboid specimens were heat-treated in a Jupiter STA 449 F1 thermal analyzer (Netzsch GmbH, Germany) in an argon atmosphere (purity 99.999%). Heat treatment of the unmachined hexagonal tensile bars was carried out in an N 7/H furnace (Nabertherm GmbH, Germany) in an ambient atmosphere.

## 2.3. Sample preparation and methods

Cuboids in the as-sintered and HIP-condition were cut into smaller specimens with dimensions of  $ 5 \times 5 \times 7.5 \pm 0.1 $ mm. The cut samples were prepared for analysis using standard metallographic grinding and polishing methods. A final surface polishing with a one-micron diamond

Table 1

Chemical composition of the consumed powder obtained by Inductively Coupled Plasma Mass Spectroscopy (ICP/ICP-MS).

| Elements | Ni | Co | W | Cr | Al | Ta | Hf | Ti | Mo | C | Zr | Fe | B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W% | Bal. | 10.06 | 9.98 | 8.53 | 5.46 | 3.02 | 1.32 | 1.05 | 0.62 | 0.15 | 0.05 | 0.03 | 0.01 |
Fig. 2. Illustration of the Binder Jetting process in 2D. The build direction is represented by z.
Fig. 3. Dimensions of cuboids and hexagonal tensile specimens in CAD before up-scaling in mm (left) and actual binder-jetted hexagonal tensile specimens and cuboids after sintering (right).

suspension was used to prepare the samples for Light Optical Microscopy (LOM). Subsequently, a colloidal silica suspension was used to prepare the samples for the Scanning Electron Microscope (SEM). The microstructure of the samples was revealed using an etching solution of 15 mL 37% HCl, 10 mL 68% HNO₃, and 10 mL 80% CH₃COOH. A Zeiss Axio Vert.A1 was used for LOM, and SEM was performed in a Zeiss Supra 35 FEG (Carl Zeiss AG, Germany). The grain sizes were measured following ISO 643:2012 via EBSD texture maps [31]. The equilibrium phase fractions and phase compositions of MAR-M247 were estimated as a function of temperature with Thermo-Calc Software version 2019b [32] using the Thermotech Ni-DATA ver. 4 database (Thermo-Calc Software AB, Sweden), to assist in the interpretation of the microstructures. The carbon content in the alloy after sintering was determined using a CS230 elemental analyzer (LECO, USA). The measurement was repeated three times with an approx. weight of 0.5 g per sample.

The specific densities,  $ \rho $, of the specimens were determined using the Archimedes principle. A Sartorius BP-210S precision balance with a measuring accuracy of  $ \pm 0.1 $ mg was used. Being equipped with the specific Archimedes determination kit YDK01 (Sartorius AG, Germany), the rack method was used in compliance with ISO3369:2006 [33]. The specimens were weighed in air and subsequently immersed and weighed in deionized water to determine their specific density. Following the suggestions proposed by Spierings and Schneider in [34], the dependence of the liquid density on temperature and air buoyancy were taken into account. Furthermore, the depth of immersion was taken into account following the manufacturer's recommendation by applying the equipment specific correction factor  $ \alpha $. Before immersing and weighing the specimens in water, they were wetted in a separate container to reduce the risk of measurement errors by the presence of air bubbles. Additionally, tensides were added to the liquid to counteract measurement errors through the adhesion of liquid to the wire. Each measurement was repeated five times.

Eq. (1) was applied to calculate the specific density

Overview of applied HIP conditions for MAR M247 specimens made by Binder Jetting.

| Cycle | HIP1 | HIP2 |
| --- | --- | --- |
| Pressure | 1000 bar | 1500 bar |
| Temperature | 1120 ^\circC | 1180 ^\circC |
| Holding time | 4 h | 4 h |
| Approx. cooling rate | 180 ^\circC/min | 180 ^\circC/min |

Applied heat treatments with respective temperatures and holding times.

| Step | 1 | 2 | 3 |
| --- | --- | --- | --- |
| Purpose | Solution treatment | Age hardening | Age hardening |
| HT1 | 1250 ^\circC, 4 h | 700 ^\circC, 24 h | - |
| HT2 | 1250 ^\circC, 4 h | 1000 ^\circC, 12 h | 700 ^\circC, 24 h |
| HT3 | - | 700 ^\circC, 24 h | - |
| HT4 | - | 1000 ^\circC, 12 h | 700 ^\circC, 24 h |
Fig. 4. Overview of the applied process-chains of MAR M247 specimen made by Binder Jetting.

 $$ \rho=\left(\rho_{fl}(T)-\rho_{air}\right)\quad\bullet\quad\frac{m_{air}}{\alpha\left(m_{air}-m_{fl}\right)}+\rho_{air} $$ 

where  $ m_{air} $ is the weight of the specimen in air,  $ m_{fl} $ the weight of the specimen when being immersed in the fluid,  $ \rho_{air} $ and  $ \rho_{fl} $ the density of air and the fluid respectively, and with  $ \alpha = 0.99983 $ being the equipment specific correction factor.

Mechanical properties were determined through Vickers hardness indentation and tensile testing. Hardness indentations were carried out on polished surfaces of the cut cuboids using a Durascan 70-G5 (Struers ApS, Denmark) with a load of 100 g and a dwell time of 10 s in compliance with ISO 6507-1:2018 [35]. The hexagonal tensile specimens were machined to the specification shown in Fig. 5. Tensile tests at room temperature were performed on an Instron 5587 (Illinois Tool Works Inc., US) system with a strain rate of 400 MPa/min until 0.2% strain and a consecutive changeover to a strain rate of 10%/min until rupture following ISO 6892-1:2019 [36].

## 3. Results

## 3.1. Densification of cuboids

In Fig. 6, polished and unetched micrographs of the cuboids cut in the middle xy- and zy-plane are shown before and after the HIP1 treatment. Two additional planes for each direction were investigated 5 mm from the edges of the cuboid showing no significant difference. Hence, the middle planes are considered to be representative and are shown in the following. Spots of different sizes and shades are spread irregularly over the different planes. The larger and dark spots indicate pores, while the smaller and dark grey spots were identified as carbides. The pores are irregularly shaped, and their sizes range from approximately 1  $ \mu $m to 20  $ \mu $m in diameter. The cut zy-planes in the as-sintered condition show slightly larger pores as compared to the xy-plane. After the HIP treatments, essentially only the smaller carbide particles are visible (dark grey features), indicating that the vast majority of pores is removed. No significant difference was observed between the micrographs of the HIP1 and HIP2 conditions.

Due to the visibility of carbides in the micrographs, a determination of relative density through light optical microscopy and image analysis is not feasible. The specific density, as determined using the Archimedes principle for five approximately equally sized samples, are summarized in Table 4. Evidently, the specific density increased by approximately 1.4% on average after the HIP1-treatment. The theoretical density of the alloy and the resulting relative densities are further assessed in the discussion Section 4.3.
Fig. 5. Technical drawing of the machined tensile specimens.

## 3.2. Densification of hexagonal tensile specimens and part-to-part density variation

To evaluate the density in the HIP2-condition and part-to-part density variations of the hexagonal tensile specimens depending on their build-orientation, the specific density of five randomly drawn vertically built and horizontally built tensile specimens was determined in the assintered and the HIP2 condition. Fig. 7 shows the average specific density from each of the drawn tensile bars in ascending order (#1-5) and the overall average values across all five bars. Significant variations in the specific density were observed between the different bars both in the vertically and horizontally built directions. Due to the considerable standard deviation, there is no reliable evidence of a higher specific density of the horizontally built tensile bars ( $ \rho_{H,1-5} = 8.358 \pm 0.051 \, g/cm^3 $) when compared to the vertically built bars ( $ \rho_{V,1-5} = 8.343 \pm 0.046 \, g/cm^3 $). However, the deviations between the tensile bars of the same build direction were minimized after the HIP2-treatment. Again, there was no significant difference observed between the two different build directions. At the same time, the specific density was raised through densification above the obtained level of HIP1, as expected. Possible causes for the difference in the observed density values are discussed in Section 4.3.

## 3.3. Microstructure after sintering and HIP-treatment

The equilibrium phase fractions and phase compositions of MAR-M247 were estimated via Thermo-Calc and are shown in Fig. 8 as a function of temperature. Of particular interest are the phase fractions and phase compositions of the  $ \gamma $ and  $ \gamma' $-phase, which vary substantially over the temperature range of interest (700–1350 ^\circC), as shown in Fig. 8a.

Fig. 9 shows the etched microstructure of MAR-M247 in the assintered state (1320 ^\circC), the HIP1 (1120 ^\circC), and the HIP2 condition (1180 ^\circC). Several phases are identified in the micrographs. The light grey phase observed is most likely the \gamma-phase. The grain boundaries of the \gamma-matrix are decorated with the white \gamma' and a finer distribution of precipitates. Agglomerations of dark spots are assumed to be either carbides or porosities and are mainly located along the grain boundaries. This applies to all three conditions. In the enlarged views of the microstructure, the contours of the larger \gamma'-precipitates are traced with a solid line while visible areas of finely distributed \gamma'-precipitates are highlighted with a dashed line. Carbides, or more likely porosities in the as-sintered condition, are colored black in the enlargements.

After the HIP1 treatment, the  $ \gamma' $-precipitates within the  $ \gamma $-grains appear less dense but are generally larger as compared to the as-sintered condition. In the HIP2 condition, the density of disperse  $ \gamma' $-precipitates within the  $ \gamma $-grains seems reduced further, and the size of visible  $ \gamma' $-precipitates is smaller when compared to the HIP1 condition. Based on the higher temperature used for HIP2 when compared to HIP1, this observation is in line with the expected smaller mass fraction of  $ \gamma' $ from the thermodynamical calculations shown in Fig. 8.

In the as-sintered condition, the coarser fraction ranges in size approximately from one to two micrometers, while the finer fraction shows precipitates with sizes smaller than one micron. In the HIP1-condition, the coarser fraction has grown to sizes above five micrometers at the expense of the finer fraction. In the HIP2-condition, on the contrary, the coarse fraction has not grown extensively, while the finer fraction shows even smaller precipitates, with sizes significantly smaller than one micron. The results suggest the simultaneous occurrence of dissolution of  $ \gamma' $-phase and Ostwald ripening, implying that the large particles grow at the cost of the smaller ones. The increase in size and decrease of phase fraction of  $ \gamma' $ after HIP1 is further observable at higher magnification in the backscatter electron images shown in Fig. 10. Furthermore, the pores and carbides are readily differentiated due to their difference in density in comparison to the background. Carbides appear white, indicating a high atomic density, while pores appear
Fig. 6. Polished micrographs showing porosities and carbides before and after HIP in the zy- and xy-plane. Z-direction corresponds to building direction.

Table 4

Specific density measurements of different cuboids via Archimedes principle.

| Density [g/cm $ ^{3} $] | #1 | #2 | #3 | #4 | #5 | Average |
| --- | --- | --- | --- | --- | --- | --- |
| As-sintered | 8.401 | 8.394 | 8.395 | 8.423 | 8.414 | 8.405 |
| Std. | 0.013 | 0.024 | 0.007 | 0.007 | 0.010 | 0.011 |
| After HIP1 | 8.569 | 8.545 | 8.561 | 8.571 | 8.554 | 8.560 |
| Std. | 0.017 | 0.008 | 0.010 | 0.022 | 0.021 | 0.009 |

black. The microstructure is littered with carbides, with a tendency of carbides to be located along grain boundaries. In the as-sintered condition, pores are primarily observed at the grain boundaries. After HIP1, the amount and the size of the remaining pores are visibly reduced, as expected. Noticeably, agglomerations of carbides are observed inside, and along the rim of pores as exemplified in the high magnification secondary electron image (Fig. 10).

Elemental analysis reveals, in particular, partitioning of Al, Cr, and Co (Fig. 11). The darker regions in the Cr and Co maps show higher elemental concentrations, indicating this is  $ \gamma $-phase (Ni-matrix) in
Fig. 7. Specific density of five different hexagonal tensile specimens of two different build orientations and processing conditions measured through the Archimedes principle. The error bars represent the respective standard deviations.
Fig. 8. Thermocalc calculations of the mass fractions of phases and elements of the MAR-M247 superalloy as a function of temperature.

accordance with the Thermocalc diagrams shown in Fig. 8b and c. Conversely, in the regions depleted in Cr and Co, an enrichment of Al is observed, consistent with the presence of the  $ \gamma' $-phase (Ni $ _{3} $Al).

At the locations with bright spots on the backscatter electron images, the Ni content is low, strongly indicating that these particles are carbides. Consistently, the elemental distribution maps show enrichment with Hf, Ti, Ta, and W at these locations, corroborating the presence of carbides of different compositions. Following the Thermocalc diagrams shown in Fig. 8d, these are assumed to be primary HfC, TaC, TiC, and WC. $ ^{2} $ The presence of MC carbides was also confirmed with X-ray diffraction analysis. The amount of carbon in the as-sintered condition was determined to be  $ 0.133 \pm 0.044 $ wt%, marginally lower than the initial content. Decarburization during different stages of sintering is not unusual and is a known phenomenon in Metal Injection Molding, which follows a similar process-chain as Binder Jetting [37,38].

The EBSD texture maps of the samples in the as-sintered condition and after the HIP1-treatment are shown in Fig. 12a and b. The measurements of the sizes of the austenite grains were based on 20 equally spaced vertical and horizontal line intercepts. No significant difference was observed between both directions, indicating an equiaxed morphology. The average grain size of the as-sintered condition was 11.3  $ \mu $m and in the HIP1 condition 10.3  $ \mu $m. No noticeable grain growth occurred after the HIP1-treatment (Fig. 12c). Moreover, no indications for strong crystallographic texture were observed in the pole figures (not shown here).

In general, the  $ \gamma' $-precipitates are relatively large and randomly distributed after sintering. After HIP-treatment, unwanted coarsening of  $ \gamma' $-precipitates (HIP1) and reduced areal fractions of  $ \gamma' $ are observed. Therefore, subsequent heat treatment is required in order to refine and control the size (distribution) of the  $ \gamma' $-precipitates. This entails a solution treatment at a temperature where the  $ \gamma' $-phase is no longer stable, i.e., above 1220 C^\circ (cf. Fig. 8) followed by age hardening at a (or several) temperature(s) where  $ \gamma' $-phase precipitates.
Fig. 9. LOM micrographs of the MAR-M247 superalloy in the xy-plane made by Binder Jetting in the (a) as-sintered condition, (b) HIP1 condition, and (c) HIP2 condition. The enlarged views show an additional magnification of 2.4x and traced contours.

## 3.4. Microstructural evolution through heat treatments HT 1-4

The four different heat treatments, HT1-4, were chosen to investigate the microstructural evolution. In particular, a bi-modal distribution of the  $ \gamma' $-precipitates is essential for favorable high-temperature properties of this alloy [39]. The results presented concern HT1 and HT2 applied to the as-sintered condition, and HT1-4 applied based on the HIP1-treatment.

The LOM micrographs in Figs. 13 and 14 show the microstructural evolutions after the heat treatments (HT1-4). Upon solution treatment at 1250 ^\circC, the \gamma'-precipitates present in the as-sintered and HIP1 conditions should have dissolved (cf. Fig. 8). Occasionally, \gamma'-precipitates are still present after solution heat treatment. HT1, comprising age hardening at 700 ^\circC after solution heat treatment, resulted in the finest dispersion of \gamma' while HT2, including double-stage aging, had a similar size of \gamma'-precipitates, including a fraction of larger \gamma-precipitates.

“Age hardening” of the HIP1 samples without prior solution treatment only leads to the coarsening of the undissolved  $ \gamma' $-precipitates (HIP1 + HT3). Including an “age-hardening” step at 1000 ^\circC (HIP1 + HT4) resulted in a uniformly distributed bi-modal distribution of the  $ \gamma' $-precipitates as compared to the as-sintered condition. Evidently, solution treatment is necessary prior to age-hardening, else the distribution of  $ \gamma' $-precipitates is strongly biased by the presence of the undissolved  $ \gamma' $-phase in the initial condition (as-sintered or HIP1).

Further assessment of the  $ \gamma' $ size fractions through X-ray diffraction analysis was inconclusive due to the overlap of the major reflections of  $ \gamma $ and  $ \gamma' $-phase that prevented distinguishing between these two phases (see Supplementary material Fig. S_{1}).

## 3.5. Mechanical properties

Hardness measurements were determined on the samples with the microstructural evolutions described in the previous section. The samples exposed to HIP1 after sintering experienced an average increase in hardness of approximately 50 HV $ _{0.1} $. The variation among the individual hardness values for a specific sample was reduced significantly after HIP, along with the annihilation of porosity (Fig. 15). Evidently, the various heat treatments HT1-4 have a limited effect on the resulting hardness.

A finely dispersed bimodal distribution of  $ \gamma' $-precipitates is known to improve the high-temperature strength and creep performance through the retardation of crack growth. Therefore, the two-stage age-hardening treatment, HT2, was chosen for the vertically and horizontally built tensile specimens. Half of the specimens were subjected to the HIP2-cycle before heat treatment HT2.

The results of the tensile tests at room temperature are shown in Fig. 16. The horizontally and vertically built specimen show similar tensile properties after sintering and heat treatment, albeit with larger variation in the yield strength and ultimate tensile strength for the horizontally built specimen. After the HIP2-treatment and subsequent heat treatment HT2, the yield strength and ultimate tensile strength increased slightly as compared to the HT2 condition after sintering only. The maximum elongation increased after HIP2, especially for the horizontally built specimen. Nevertheless, the tensile properties still show a considerable variation after HIP2 treatment, which is most clearly reflected by the vertically built specimen. The stress-strain tensile testing curves (not shown) showed no indications of necking, and the fracture
Fig. 10. Backscattered electron images in the xy-plane showing the microstructure before and after HIP. The magnification in the center shows a secondary electron image in the xy-plane with porosity (without HIP).
Fig. 11. Elemental analysis via EDS mapping and point measurements of the MAR-M247 made by Binder Jetting after HIP1 treatment. Note that all scale bars are 10  $ \mu $m.
Fig. 12. Orientation image maps of binder-jetted MAR-M247 in the as-sintered condition (a) and the HIP1-condition (b). The grain size distributions for both conditions (c).

surfaces reflected brittle fracture, consistent with the low elongation reported in Fig. 16.

## 4. Discussion

## 4.1. Microstructural evolution

The sintering process of the binder-jetted samples was terminated with relatively slow furnace cooling. The resulting microstructure is characterized through coarse  $ \gamma' $-precipitates that developed during cooling, as this phase is not stable at the sintering temperature. Relatively large  $ \gamma' $-precipitates are known to negatively influence the ultimate tensile strength at high-temperature [39]. Additionally, porosities were observed, with voids as large as 20  $ \mu $m. Therefore, solution treatment and HIP are regarded to be necessary for enhancing the mechanical properties, especially for high-temperature applications.

Subjecting the material to a HIP treatment does not only reduce the porosity but also affects the resulting microstructure depending on the applied HIP parameters. After the HIP1-treatment, Ostwald ripening of the  $ \gamma' $-precipitates was observed and perhaps some dissolution; the HIP2-treatment reduced the mass fraction of precipitated  $ \gamma' $ importantly. Fig. 8 shows that the HIP2 temperature of 1180 ^\circC is just below the temperature where the  $ \gamma' $-phase is no longer stable. Hence, the HIP2-treatment almost functioned as a solution treatment. In similar treatments of MAR-M247 in the literature, extremely fine  $ \gamma' $-precipitates were found [40–42]. In the present case, fast cooling at a rate of 180^\circC/min after the HIP-cycles prevents the precipitation of  $ \gamma' $-phase on cooling.

For high-temperature applications of binder-jetted MAR-M247, solution treatment and further densification are regarded as unavoidable. For this purpose, a HIP treatment at a higher temperature than applied here (e.g., 1250 ^\circC) could enable both densification and dissolution of \gamma'-phase. The observed grain boundary pinning by the presence of carbides is anticipated to avoid grain growth during a HIP-treatment in the temperature range for solution heat treatment.

The different aging treatments were applied for different purposes (see Section 2.2). The solution treatment of the samples dissolved most of the  $ \gamma' $-precipitates, but some larger precipitates were still present in the samples afterwards (HT1-2). This indicates that the dissolution of large precipitates requires more time than allocated. The sluggish dissolution could be compensated by a higher temperature or longer holding time. Particularly, this was observed for HT1, and HT2 applied for the HIP1 samples, where the  $ \gamma' $-precipitates were larger before the solution treatment. Omitting the solution treatment and aging at 1000 ^\circC, the samples aged at 700 ^\circC (HT3) did not influence the size distribution of the  $ \gamma' $-precipitates. Without the solution treatment, the
Fig. 13. LOM micrographs in the xy-plane of the etched MAR-M247 samples in the as-sintered condition and after heat treatment HT1-2.

coarse  $ \gamma' $-precipitates were still present, and the double-aging (HT4) resulted in two additional size ranges of  $ \gamma' $-precipitates in the magnitude of approximately one micron and submicron size. In return, this microstructure, on average, indicated a slightly higher hardness, strengthening the possibility of a hybrid HIP/solution treatment. Combining the solution treatment with subsequent double-aging (HT2), the coarsest  $ \gamma' $-precipitates were no longer present, leading to a genuinely bimodal  $ \gamma' $-precipitate distribution. Based on the HIP1 samples, HT3 and 4 resulted in less uniform microstructures when compared to HT1 and HT2.

The similar hardness values observed after HT1-4 are related to the high volume fractions of precipitated  $ \gamma' $ that is observed in all heat-treated cases, including the samples that did not receive an additional solution treatment (HT3-4). In these cases, a high volume fraction of precipitated  $ \gamma' $ remained from the slow furnace cooling after sintering and did not noticeably increase upon further aging. As a result, HT3-4 yielded similar hardness values as HT1-2. On the contrary, the initial HIP1 condition yielded slightly lower hardness values on average when compared to subsequent HT1-4, further underlining that minor dissolution of  $ \gamma' $-precipitates occurred during HIP1. However, in addition to the volume fraction, the size and distribution of  $ \gamma' $ is decisive for creep and high-temperature strength, which is not reflected in the obtained hardness values.

For the tensile specimen in this work, the HIP2 treatment was applied due to enhanced densification. Based on this, the solution treatment and double-aging were chosen to adjust a bimodal size distribution of  $ \gamma' $. Other studies have shown that the presence of larger  $ \gamma' $-precipitates will retard the propagation of cracks from brittle carbides in the material [39]. Moreover, the solution treatment was included in the heat treatment for the specimens to avoid the unfavorable size distribution of  $ \gamma' $-precipitates observed for the HIP1 condition. It is noted that the “transferability” of the chosen heat-treatment is ensured by the solution treatment step to recrystallize the  $ \gamma' $-precipitates before applying the double-age-hardening step. Based on the observed pinning effect, no significant grain-growth was expected from HIP2 when compared to HIP1. In general, the aging parameters should be tailored after the intended service temperature. Double-aging to retard crack propagation in the many carbides could prove advantageous.

HIP1

HIP1 + HT1 (1250^\circC \rightarrow 700^\circC)

HIP1 + HT3 (700^\circC)

HIP1 + HT4 (1000^\circC \rightarrow 700^\circC)
Fig. 14. LOM micrographs in the xy-plane of the etched MAR-M247 samples in the HIP1-condition and after heat treatment HT1-4.
Fig. 15. Hardness values of the MAR-M247 as-sintered and HIP1 sample, before and after the heat treatments HT1-4. The error bars represent the respective standard deviations.

## 4.2. Comparison of resulting microstructure and properties to conventionally manufactured MAR-M247

On the basis of similarities in the process-chains, the shown microstructures in this work are expected to be most comparable to MAR-M247 manufactured by Metal Injection Moulding (MIM) [30,43], as both processes include debinding and sintering, where the grain boundaries have formed along the surfaces of powder particles. Accordingly, equiaxed grains with sizes comparable to the used D50 powder particle size, 15–20 µm, are obtained. \gamma'-precipitates in size ranges of 0.5–1 µm, and finely distributed carbide structures (MC, M₂₃C₆, and M₆C) are present along grain boundaries, leaving a remaining porosity of approximately 2%. Similar to BJ, HIP can be successfully applied without notable grain-growth after MIM densification, and solution treatment followed double-aging yields a uniform bimodular \gamma'-phase distribution [30].

The typical microstructure of MAR-M247 obtained from Vacuum Investment Casting (VIC) shows substantial differences from their BJ- and MIM-manufactured counterparts. VIC results in a dendritic structure with relatively large grains (> 200 µm), and compositional inhomogeneities on micro- and macroscale [11,30]. Thick \gamma'-plates of five microns in size, as well as sub-micron \gamma'-precipitates in eutectic pools, are reported [11]. Furthermore, the distribution and morphology of the obtained carbides differ significantly. Large script-like MC carbides with high aspect ratios and sizes up to 40 µm can be located inside the grains, whereas M₂₃C₆ carbides can be present at grain boundaries [11,39]. A remaining level of porosity of approximately 0.25% was reported after VIC [44]. By solution treatment, a uniform size distribution of \gamma'-precipitates and an improved segregation profile can be obtained. However, slight dendritic segregation remains after solution treatment due to the heavy elements of the alloy defusing slowly. Even though the carbides become smaller in size and more round after heat treatment, the script-like MC carbides remain inside the grains [11].

In Fig. 17, the average tensile properties at room temperature, independent of build-direction, in the HIP and HT2 conditions that were obtained in this work are shown. The values are compared to tensile properties obtained from MIM and VIC from the literature that were also exposed to HIP, solution treatment, and aging steps [30,45].

The processed BJ specimens show a similar yield and ultimate tensile strength when compared to the specimens obtained by VIC. In comparison with the processed MIM specimens, the BJ specimens exhibit a 200 MPa higher yield strength, while the ultimate tensile strength is reduced by approximately the same value. In general, the processed BJ specimens show a considerably lower elongation than MIM and VIC.

The lower elongation and brittle fracture behavior of the processed BJ specimens are assumed to be provoked by the strong presence of precipitated carbides along the grain boundaries. These carbides were identified in the as-sintered and HIP conditions to be as MC type (M = Hf, W, Ta, Ti), which are known for their high hardness, density, and brittleness. A fine microstructure with dispersed carbides contributes to a higher strength of the alloy but potentially reduces the ductility because they can act as crack initiation sites [39].
Fig. 16. Tensile strength after heat treatment and HIP treatment at room temperature. The error bars represent the respective standard deviations.
Fig. 17. Tensile properties of MAR-M247 made by Binder Jetting (BJ), Metal Injection Molding (MIM), and Vacuum Investment Casting (VIC) after HIP and heat treatment. HIP for MIM and VIC was at 1185 ^\circC and approx. 170 MPa for 4 h. Heat treatment for MIM was at 1230 ^\circC for two hours, 1280 ^\circC for two hours, 1080 ^\circC for four hours, and 870 ^\circC for 20 h [30]. Heat treatment for VIC was at 1185 ^\circC for two hours and 871 ^\circC for 20 h [45]. The error bars represent the respective standard deviations. For MIM, no standard deviation was reported.
Fig. 18. Relative densities of MAR-M247 samples made by Binder Jetting. The error bars represent the respective standard deviations.

## 4.3. Relative density and sources of porosity

Theoretical values for specific densities are ranging from 8.54 g/cm³ to 8.58 g/cm³ for conventionally manufactured MAR-M247 [30,44,46,47]. The inconsistency that is reported across the literature is associated with variations in the contents of the heavy elements. In this work, a density of  $ 8.579 \pm 0.003 \, g/cm^3 $ was determined after the HIP2-treatment, while the highest value was assessed for one of the horizontally built tensile specimens with  $ 8.581 \pm 0.002 \, g/cm^3 $. Assuming that the HIP2-treatment resulted in fully dense material, the average relative densities of the samples are shown in Fig. 18 in the as-sintered, HIP1- and HIP2-condition.

The density assessment for the cuboid-samples was based on different samples that are cut from the same part, while the averaged measurements of the hexagonal tensile specimens include part-to-part deviations. For these tensile specimens, a standard deviation of 0.58% in relative density was observed in the as-sintered condition regardless of their build orientation.

Possible sources for the variation of porosity within parts made by Binder Jetting are primarily linked to the printing process itself and the subsequent sintering process. During printing, the clogging of inkjet nozzles or defects in the powder bed, such as voids, are typical process anomalies that lead to unbound areas in the green part [27,48].

During sintering, the temperature and the holding time are driving factors for the densification. Based on prior investigations in connection with the used samples in the present study, a deviation of 10 ^\circC in sintering temperature may influence approximately 2–4% on the resulting density [28]. In light of the narrow sintering-process window, further part-to-part variations in the degree of porosity can result from temperature gradients inside the furnace, especially in the high-temperature regime applied for sintering of MAR M247.

Nevertheless, the applied HIP-treatments in this work showed that the part-to-part density differences can be reduced, and the specific density converges towards a consistent value.

## 4.4. Further improvement of heat treatment and design philosophy

As shown in this work, the additively manufactured MAR-M247 samples made by Binder Jetting show a level of approx. 2.5% porosity after solid-state sintering. Typical applications for nickel-based superalloys require excellent thermo-mechanical fatigue and creep resistance [49]. Therefore, further densification could become essential to fulfill the specifications of potential applications.

One approach of densifying powder metallurgical components is to raise the sintering temperature. In the present case, a further rise of the sintering temperature would trigger super solidus liquid phase sintering (SLPS) as also observed in investigations on binder-jetted IN625 and IN718 [24,25]. Although beneficial for densification, a major concern with SLPS is the loss of component shape during sintering [50]. When a certain temperature is exceeded and excess liquid is formed, slumping occurs and gravitational forces cause non-uniform distortions [51]. For components with tight industrial tolerances, this effect is known to entail costly dimensional adjustments after sintering [52]. Moreover, the presence of a liquid phase in this alloy may lead to solidification and liquation cracking, and thus jeopardize the benefits of the Binder Jetting process-chain when compared to other AM processes that involve melting [13–19].

Another approach supposes to decrease the powder particle size to increase the sintering energy and thereby reach higher densification [53]. However, in the context of powder bed based AM, the deposition of extremely fine powder particles is considered to be a significant obstacle. Powders with smaller particle sizes have more surface area, which amplifies the impact of inter-particle forces that reduce the powder’s flowability during the handling and feeding process [54]. Thus, the use of extremely fine powders (typically < 10  $ \mu $m) necessitates substantial machine modifications such as advanced powder recoating systems, e.g. vibration-assisted dispensing, to enable the formation of homogenous powder layers [55]. In light of the already fine powder particles used in the present study (D50 = 15  $ \mu $m), a substantial reduction in particle size is expected to be challenging without significant modifications to the equipment.

Thus, both approaches, i.e. raising the sintering temperature and decreasing the size of the powder particles, have practical limitations in the present case. From this perspective, a HIP-treatment is a promising approach for binder-jetted MAR-M247 to reach further densification.

Moreover, if HIP-treatment is selected as a standard route for post-processing these BJ components, previous steps in the process chain could potentially be adapted to create process synergies. Based on the premise that the resulting porosities in the sintered condition are closed, a lower green part and sintered density could become acceptable.

Consequently, lower sintering temperatures, shorter holding times, or both, can be selected. Alternatively, the powder particle size and layer-thickness could be increased if a lower green part density, a lower detail-resolution, and a larger resulting grain size are accepted [56]. As a result, the productivity of the process could be increased.

As previously shown in Section 3.1, the HIP treatment caused coarse  $ \gamma' $-precipitates to grow on the expense of fine  $ \gamma' $-precipitates, which necessitates a subsequent solution treatment. Exploiting grain boundary pinning through the presence of carbides, the temperature of the HIP-treatment could most likely be further raised to above 1200 ^\circC to realize the dissolution of  $ \gamma' $-phase during HIP. Thereby, the rapid cooling applied in the HIP cycle can effectively be utilized to suppress the precipitation of  $ \gamma' $-phase prior to subsequent aging treatments. The benefit of integrated HIP heat treatments was earlier demonstrated for VIC-, EBM- and LPBF-manufactured nickel-based superalloys [57–59].

Additionally, the role and evolution of carbides in binder-jetted MAR-M247 need further attention. It has been demonstrated that modification of the heat treatments to fine-tune the carbide distribution can lead to improved ductility with higher elongation for conventionally VIC-manufactured MAR-M247 [39].

## 5. Conclusions

A processing route for Binder Jetting of MAR-M247 was presented that is capable of yielding dense material with a satisfactory  $ \gamma' $-microstructure and mechanical properties.

- The as-sintered microstructure of binder-jetted MAR-M247 consists of equiaxed grains with an average size of 10.3  $ \mu $m, which contain homogeneously distributed  $ \gamma' $-precipitates of various submicron sizes and remaining porosity in the range of 2.1–3.3%.

- Close to full densification through HIP was achieved while grain growth was avoided because of grain boundary pinning by carbides. Meanwhile, coarsening and Ostwald ripening of  $ \gamma' $-precipitates occurred, wherefore subsequent solution treatment is recommended to dissolve all  $ \gamma' $-phase. It was suggested that the solution treatment could be combined with HIP by increasing the temperature during the latter.

• Through solution and double-aging heat treatment (HT2), homogeneously distributed bimodular  $ \gamma' $-structures can be achieved.

- No significant anisotropy of tensile properties was observed between horizontally and vertically built specimens. Independent of build direction, the average yield strength, ultimate tensile strength, and elongation after HIP2 + HT2 were 1000 MPa, 1105 MPa, and 3.1%, respectively.

- Binder Jetting offers an alternative manufacturing process of MAR-M247 with similar yield and tensile strength at room temperature as conventional Metal Injection Molding or Vacuum Investment Casting.

For further optimization, the role and evolution of carbides for binder-jetted MAR-M247 needs to be more thoroughly investigated. The integration of the solution treatment into the HIP-cycle could be a promising approach for microstructural improvement and to utilize additional process synergies. The altered microstructural morphology of binder-jetted MAR-M247 suggests different high-temperature behavior in comparison to conventionally manufactured microstructure. Hence, mechanical properties such as tensile, fatigue, and creep tests under high-temperature should be investigated in further steps.

## CRediT Authorship

T. Dahmen: Conceptualization, Data curation, Formal analysis, Funding acquisition, Investigation, Methodology, Project administration, Software, Validation, Visualization, Writing - original draft. N.G. Henriksen: Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Software, Validation, Visualization, Writing - review & editing. K.V. Dahl: Data curation, Software, Writing - review & editing. A. Lapina: Funding acquisition, Project administration, Resources, Supervision, review & editing. D.B. Pedersen: Project administration, Supervision, Writing - review & editing. J.H. Hattel: Funding acquisition, Project administration, Resources, Supervision, Writing - review & editing. T.L. Christiansen: Conceptualization, Formal analysis, Investigation, Methodology, Validation, Writing - review & editing. M.A.J. Somers: Conceptualization, Formal analysis, Investigation, Methodology, Resources, Validation, Writing - review & editing.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

Technical discussions, the manufacturing, and HIP of the test-artifacts were provided by Digital Metal (Höganäs AB) and Quintus AB. The collaboration was highly appreciated. The research was partially funded by the company MAN Energy Solutions SE. Their financial support was much appreciated. Emilie Hørdum Valente, Cecilie Vase Funch, and Tianbo Yu are acknowledged for their assistance in SEM and EBSD. David de Baere is acknowledged for his assistance in reviewing the manuscript.

## Acknowledgments

## Appendix A. Supporting information

## Supplementary Material

## References

[1] R. Liu, Z. Wang, T. Sparks, F. Liou, J. Newkirk, 13 - aerospace applications of laser additive manufacturing, in: M. Brandt (Ed.), Laser Additive Manufacturing, Elsevier, Woodhead, Amsterdam, 2017, pp. 351–371, https://doi.org/10.1016/B978-0-08-100433-3.00013-0.

[2] L. Xue, Y. Li, J. Chen, S. Wang, Laser Consolidation: A Novel Additive Manufacturing Process for Making Net-Shape Functional Metallic Components for Gas Turbine Applications, in: Proceeding of the ASME Turbo Expo 2015: Turbine Technical Conference and Exposition, June 15–19, Canada, 2015. https://doi.org/10.1115/GT2015-43971.

[3] G. Bi, A. Gasser, Restoration of nickel-base turbine blade knife-edges with controlled laser aided additive manufacturing, Phys. Procedia 12 (2011) 402–409, https://doi.org/10.1016/j.phpro.2011.03.051.

[4] F. Caiazzo, V. Alfieri, G. Corrado, P. Argenio, Laser powder-bed fusion of Inconel 718 to manufacture turbine blades, Int. J. Adv. Manuf. Technol. 93 (2017) 4023–4031.

[5] E. Salvati, A.J.G. Lunt, S. Ying, T. Sui, H.J. Zhang, C. Heason, G. Baxter, A. M. Korsunsky, Eigenstrain reconstruction of residual strains in an additively manufactured and shot peened nickel superalloy compressor blade, Comput. Methods Appl. Mech. Eng. 320 (2017) 335–351, https://doi.org/10.1016/j.cma.2017.03.005.

[6] J. Witzel, J. Schrage, A. Gasser, I. Kelbassa, Additive manufacturing of ablade-integrated disk by laser metal deposition, in: ICALEO: 30th Intern. Congress on Applications of Lasers & Electro-Optics, October 23-27, Laser Institute of America, Orlando, F.L., pp. 250–256, 2011. https://doi.org/10.2351/1.5062243.

[7] T. Petrat, B. Graf, A. Gumenyuk, M. Rethmeier, Laser metal deposition as repair technology for a gas turbine burner made of Inconel 718, Phys. Procedia 83 (2016) 761–768, https://doi.org/10.1016/j.phpro.2016.08.078.

[8] A.A. Sadek Tadros, G.W. Ritter, C.D. Drews, D. Ryan, Additive Manufacturing of Fuel Injectors, Technical report, U.S. Department of Energy, Office of Scientific and Technical Information, 2017. https://doi.org/10.2172/1406179.

[9] B. Graybill, M. Li, D. Malawey, C. Ma, J.-M. Alvarado-Orozco, E. Martinez-Franco, Additive Manufacturing of Nickel-Based Superalloys, in: ASME 2018 13th International Manuf. Science and Eng. Conference, June 18–22, ASME Digital Collection, 2018. https://doi.org/10.1115/MSEC2018-6666.

[10] W. Danesi, Thielemann R., Nickel Base Alloy, US3720509A, Google Patents, 1970. https://patents.google.com/patent/US3720509A/en. (Accessed 23 June 2020).

[11] R. Baldan, R.L.P. da Rocha, R.B. Tomasiello, C.A. Nunes, C. da Silva, A. Matos, M.J. R. Barboza, G.C. Coelho, R. Rosenthal, Solutioning and aging of MAR-M247 nickel-

based superalloy, J. Mater. Eng. Perform. 22 (2013) 2574–2579, https://doi.org/10.1007/s11665-013-0565-4.

[12] A. Gunderson, S.J. Setlak, W.F. Brown. Aerospace Structural Metals Handbook, CINDAS LLC, West Lafeyette, Indiana, 2007.

[13] L. Carter, M. Attallah, R. Reed, Laser powder bed fabrication of nickelbase superalloys: influence of parameters; characterisation, quantification and mitigation of cracking, Superalloys (2012) 577–586.

[14] J.H. Boswell, D. Clark, W. Li, M.M. Attallah, Cracking during thermal post-processing of laser powder bed fabricated CM247LC Ni-superalloy, Mater. Des. 174 (2019), 107793, https://doi.org/10.1016/j.matdes.2019.107793.

[15] L.N. Carter, C. Martin, P.J. Withers, M.M. Attallah, The influence of the laser scan strategy on grain structure and cracking behaviour in SLM powder-bed fabricated nickel superalloy, J. Alloy. Compd. 615 (2014) 338–347, https://doi.org/10.1016/j.jallcom.2014.06.172.

[16] S. Catchpole-Smith, N. Aboulkhair, L. Parry, C. Tuck, I.A. Ashcroft, A. Clare, Fractal scan strategies for selective laser melting of ‘unweldable’ nickel superalloys, Addit. Manuf. 15 (2017) 113–122, https://doi.org/10.1016/j.addma.2017.02.002.

[17] V.D. Divya, R. Muñoz-Moreno, O.M.D.M. Messé, J.S. Barnard, S. Baker, T. Illston, H.J. Stone, Microstructure of selective laser melted CM247LC nickel-based superalloy and its evolution through heat treatment, Mater. Charact. 114 (2016) 62–74, https://doi.org/10.1016/j.matchar.2016.02.004.

[18] Y.S. Lee, M.M. Kirka, S. Kim, N. Sridharan, A. Okello, R.R. Dehoff, S.S. Babu, Asymmetric cracking in Mar-M247 alloy builds during electron beam powder bed fusion additive manufacturing, Metall. Mater. 49 (2018) 5065–5079, https://doi.org/10.1007/s11661-018-4788-8.

[19] X. Wang, L.N. Carter, B. Pang, M.M. Attallah, M.H. Loretto, Microstructure and yield strength of SLM-fabricated CM247LC Ni-superalloy, Acta Mater. 128 (2017) 87–95, https://doi.org/10.1016/j.actamat.2017.02.007.

[20] A. Seidel, T. Finaske, A. Straubel, H. Wendrock, T. Maiwald, M. Riede, E. Lopez, F. Brueckner, C. Leyens, Additive manufacturing of powdery Ni-based superalloys Mar-M-247 and CM 247 LC in hybrid laser metal deposition, Metall. Mater. 49 (2018) 3812–3830, https://doi.org/10.1007/s11661-018-4777-y.

[21] Y.C. Hagedorn, J. Risse, W. Meiners, N. Pirch, K. Wissenbach, R. Poprawe, Processing of nickel based superalloy MAR M-247 by means of high temperature-selective laser melting (HT-SLM), in: Bartolo (Ed.), High Value Manufacturing, Taylor & Francis, London, 2014, pp. 291–295.

[22] A. Basak, S. Das, Microstructural Characterization of MAR-M247 Fabricated Through Scanning Laser Epitaxy, in: Proceeding of the 27th Annual International Solid Freeform Fabrication Symposium, August 8–10, SFF, Austin, United States, 2016.

[23] T. Do, P. Kwon, C.S. Shin, Process development toward full-density stainless steel parts with binder jetting printing, Int. J. Mach. Tools Manuf. 121 (2017) 50–60, https://doi.org/10.1016/j.ijmachtools.2017.04.006.

[24] A. Mostafaei, E.L. Stevens, E.T. Hughes, S.D. Biery, C. Hilla, M. Chmielus, Powder bed binder jet printed alloy 625: densification, microstructure and mechanical properties, Mater. Des. 108 (2016) 126–135, https://doi.org/10.1016/j.matdes.2016.06.067.

[25] P. Nandwana, A.M. Elliott, D. Siddel, A. Merriman, W.H. Peter, S.S. Babu, Powder bed binder jet 3D printing of Inconel 718: densification, microstructural evolution and challenges, Curr. Opin. Solid State Mater. Sci. 21 (2017) 207–218, https://doi.org/10.1016/j.cossms.2016.12.002.

[26] A. Du Plessis, E. Macdonald, Hot isostatic pressing in metal additive manufacturing: X-ray tomography reveals details of pore closure, Addit. Manuf. 34 (2020), 101191, https://doi.org/10.1016/j.addma.2020.101191. http://www.sciencedirect.com/science/article/pii/S2214860420305637.

[27] A. Yegyan Kumar, Y. Bai, A. Eklund, C.B. Williams, The effects of hot isostatic pressing on parts fabricated by binder jetting additive manufacturing, Addit. Manuf. 24 (2018) 115–124, https://doi.org/10.1016/j.addma.2018.09.021.

[29] H.Y. Bor, C. Hsu, C.N. Wei, Influence of hot isostatic pressing on the fracture transitions in the fine grain MAR-M247 superalloys, Mater. Chem. Phys. 84 (2004) 284–290, https://doi.org/10.1016/j.matchemphys.2003.08.014.

[30] B. Albert, Hochtemperaturverhalten von Spritzguss-Nickelbasis-Superlegierungen am Beispiel von Honigwaben-Dichtungen, Dissertation. Uwe Glatzel, University of Bayreuth, Bayreuth, Germany, 2013. https://eref.uni-bayreuth.de/id/eprint/23497. (Accessed 14 July 2020).

[31] International Organization for Standardization, ISO 643: 2012, Steels - Micrographic Determination of the Apparent Grain Size, 2012.

[32] J.-O. Andersson, T. Helander, L. Höglund, P. Shi, B. Sundman, Thermo-Calc & DICTRA, computational tools for materials science, Calphad 26 (2002) 273–312, https://doi.org/10.1016/S0364-5916(02)00037-8.

[33] International Organization for Standardization, ISO 3369: 2006, Impermeable Sintered Metal Materials and Hardmetals - Determination of Density, 2006.

[34] A.B. Spierings, M. Schneider, R. Eggenberger, Comparison of density measurement techniques for additive manufactured metallic parts, Rapid Prototyp. J. 17 (2011) 380–386, https://doi.org/10.1108/13552541111156504.

[35] International Organization for Standardization, ISO 6507-1: 2018, Metallic Materials - Vickers Hardness Test - Part 1: Test Method, 2018.

[36] International Organization for Standardization, ISO 6892-1: 2019, Metallic Materials - Tensile Testing - Part 1: Method of Test at Room Temperature, 20

[37] Y. Wu, R.M. German, D. Blaine, B. Marx, C. Schlaefer, Effects of residual carbon content on sintering shrinkage, microstructure and mechanical properties of injection molded 17-4 pH stainless steel, J. Mater. Sci. 37 (2002) 3573–3583, https://doi.org/10.1023/A:1016532418920.

[38] J. Lou, M. Liu, H. He, X. Wang, Y. Li, X. Ouyang, C. An, Investigation of decarburization behaviour during the sintering of metal injection moulded 420 stainless steel, Metals 10 (2020), 211, https://doi.org/10.3390/met10020211.

[39] H.Y. Bor, C.N. Wei, R.R. Jeng, P.Y. Ko, Elucidating the effects of solution and double ageing treatment on the mechanical properties and toughness of MAR-M247 superalloy at high temperature, Mater. Chem. Phys. 109 (2008) 334–341, https://doi.org/10.1016/j.matchemphys.2007.11.041.

[40] C.T. Sims, N.S. Stoloff, W.C. HAGEL (Eds.), Superalloys II: High-Temperature Materials for Aerospace and Industrial Power, Wiley, New York, 1987.

[41] P. Beardmore, Hyperfine precipitation in nickel alloys, Mater. Sci. Eng. 5 (1970) 350–352, https://doi.org/10.1016/0025-5416(70)90027-3.

[42] K. Kakehi, Tension/compression asymmetry in creep behavior of a Ni-based superalloy, Scr. Mater. 41 (1999) 461–465, https://doi.org/10.1016/S_{1359}-6462(99)00191-8.

[43] A. Meyer, E. Daenicke, K. Horke, M. Moor, S. Müller, I. Langer, R.F. Singer, Metal injection moulding of nickel-based superalloy CM247LC, Powder Metall. 59 (2016) 51–56, https://doi.org/10.1080/00325899.2016.1142058.

[44] Q. He, L. Li, Z. Gao, G. Yang, H. Zeng, Z. Yang, Effect of hot isostatic pressing on microstructures and mechanical properties of Mar M247 alloy, J. Chin. Soc. Power Eng. 39 (2019) 860–864. https://shorturl.at/awES0.

[45] J.-H. Liao, H.-Y. Bor, C.-G. Chao, T.-F. Liu, Influence of rhenium on the mechanical behavior and fracture mechanism of a fine-grain superalloy at elevated temperatures, Mater. Trans. 52 (2011) 201–209, https://doi.org/10.2320/matertrans.M2010299.

[46] J.R. Kattus, Aerospace Structural Metals Handbook, Code 4218, West Lafeyette, Indiana, 1999.

[47] F. Klocke, M. Zeis, A. Klink, D. Veselovac, Experimental research on the electrochemical machining of modern titanium- and nickel-based alloys for aero engine components, Procedia CIRP 6 (2013) 368–372, https://doi.org/10.1016/j.procir.2013.03.040.

[48] H. Miyanaji, M. Orth, J.M. Akbar, L. Yang, Process development for green part printing using binder jetting additive manufacturing, Front. Mech. Eng. 13 (2018) 504–512, https://doi.org/10.1007/s11465-018-0508-8.

[49] R.C. Reed, The Superalloys: Fundamentals and Applications, Cambridge University Press, Cambridge, 2006, https://doi.org/10.1017/CBO9780511541285.

[50] J. Liu, R.M. German, Densification and shape distortion in liquid-phase sintering, Metall. Mater. 30 (1999) 3211–3217.

[51] R.M. German, Supersolidus liquid-phase sintering of prealloyed powders, Metall. Mater. 28 (1997) 1553–1567, https://doi.org/10.1007/s11661-997-0217-0.

[52] R.M. German, P. Suri, S.J. Park, Review: liquid phase sintering, J. Mater. Sci. 44 (2009) 1–39, https://doi.org/10.1007/s10853-008-3008-0.

[53] R.M. German, Sintering Theory and Practice, Wiley-VCH, 1996.

[54] M. Ziaee, N.B. Crane, Binder jetting: a review of process, materials, and methods, Addit. Manuf. 28 (2019) 781–801, https://doi.org/10.1016/j.addma.2019.05.031.

[55] B. Nagarajan, Z. Hu, X. Song, W. Zhai, J. Wei, Development of micro selective laser melting: the state of the art and future perspectives, Engineering 5 (2019) 702–720, https://doi.org/10.1016/j.eng.2019.07.002.

[56] Miyanaji Hadi, Momenzadeh Niknam, Effect of powder characteristics on parts fabricated via binder jetting process, Rapid Prototyp. J. 25 (2019) 332–342, https://doi.org/10.1108/RPJ-03-2018-0069.

[57] L. Mujica Roncery, I. Lopez-Galilea, B. Ruttert, D. Bürger, P. Wollgramm, G. Eggeler, W. Theisen, On the effect of hot isostatic pressing on the creep life of a single crystal superalloys, Adv. Eng. Mater. 18 (2016) 1381–1387, https://doi.org/10.1002/adem.201600071.

[58] C. Meid, A. Dennstedt, M. Ramsperger, J. Pistor, B. Ruttert, I. Lopez-Galilea, W. Theisen, C. Körner, M. Bartsch, Effect of heat treatment on the high temperature fatigue life of single crystalline nickel base superalloy additively manufactured by means of selective electron beam melting, Scr. Mater. 168 (2019) 124–128, https://doi.org/10.1016/j.scriptamat.2019.05.002.

[59] Z.A. Sentyurina, F.A. Baskov, P.A. Loginov, Y.Y. Kaplanskii, A.V. Mishukov, I.A. Logachev, M.Y. Bychkova, E.A. Levashov, A.I. Logacheva, The effect of hot isostatic pressing and heat treatment on the microstructure and properties of EP741NP nickel alloy manufactured by laser powder bed fusion, Addit. Manuf. (2020), 101629, https://doi.org/10.1016/j.addma.2020.101629.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

Additive Manufacturing 39 (2021) 101912

$ ^{a} $ Department of Mechanical Engineering, Technical University of Denmark, Produktionstorvet, Building 425, 2800 Kgs. Lyngby, Denmark
 $ ^{b} $ MAN Energy Solutions, Teglholmsgade 41, 2450 Copenhagen, Denmark

## Keywords
Binder Jetting
MAR M247 superalloy
Turbine engine
Hot isostatic pressing
Additive Manufacturing
## ABSTRACT
## CRediT Authorship
## Supplementary Material

## ABSTRACT

https://doi.org/10.1016/j.addma.2021.101912 2214-8604/© 2021 Elsevier B.V. All rights reserved. After manufacturing, the specimens were cured in an ambient atmosphere at 200 ^\circC for 8 h, depowdered with compressed air, and removed from the building box. Subsequent thermal debinding was performed in an ambient atmosphere at 345 ^\circC for three hours. Thereafter, the specimens were sintered in an H800 SF vacuum furnace (Vacua Therm Ltd., UK) at 1320 ^\circC and approximately 0.1 Pa for 6 h and finally slowly cooled in the furnace (< 20 ^\circC/min). $ ^{1} $ It is noted that a material with a similar composition was commercialized under the trade name DM247 (Digital Metal AB, Sweden) after this research project was initiated. The equilibrium phase fractions and phase compositions of MAR-M247 were estimated via Thermo-Calc and are shown in Fig. 8 as a function of temperature. Of particular interest are the phase fractions and phase compositions of the  $ \gamma $ and  $ \gamma' $-phase, which vary substantially over the temperature range of interest (700–1350 ^\circC), as shown in Fig. 8a. $ ^{2} $ It is noted that the Thermo-Calc results reflect thermodynamic equilibrium compositions and phase fractions. In particular for the carbides, which contain slowly diffusing heavy elements, appreciable deviations from the equilibrium compositions can occur. For this reason a large variation in carbide composition can occur. Further assessment of the  $ \gamma' $ size fractions through X-ray diffraction analysis was inconclusive due to the overlap of the major reflections of  $ \gamma $ and  $ \gamma' $-phase that prevented distinguishing between these two phases (see Supplementary material Fig. S_{1}). For high-temperature applications of binder-jetted MAR-M247, solution treatment and further densification are regarded as unavoidable. For this purpose, a HIP treatment at a higher temperature than applied here (e.g., 1250 ^\circC) could enable both densification and dissolution of \gamma'-phase. The observed grain boundary pinning by the presence of carbides is anticipated to avoid grain growth during a HIP-treatment in the temperature range for solution heat treatment. [42] K. Kakehi, Tension/compression asymmetry in creep behavior of a Ni-based superalloy, Scr. Mater. 41 (1999) 461–465, https://doi.org/10.1016/S_{1359}-6462(99)00191-8.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

ELSEVIER

Contents lists available at ScienceDirect

journal homepage: www.elsevier.com/locate/addma

Keywords:
Binder Jetting
MAR M247 superalloy
Turbine engine
Hot isostatic pressing
Additive Manufacturing

A B S T R A C T

* Corresponding author.

E-mail addresses: tdah@mek.dtu.dk (T. Dahmen), nigehe@mek.dtu.dk (N.G. Henriksen), kvd@mek.dtu.dk (K.V. Dahl), alberto.lapina@man-es.com (A. Lapina), dbpe@mek.dtu.dk (D.B. Pedersen), jhat@mek.dtu.dk (J.H. Hattel), tch@mek.dtu.dk (T.L. Christiansen), somers@mek.dtu.dk (M.A.J. Somers).

Received 14 September 2020; Received in revised form 8 January 2021; Accepted 9 February 2021

Available online 13 February 2021

T. Dahmen et al.

After manufacturing, the specimens were cured in an ambient atmosphere at 200 °C for 8 h, depowdered with compressed air, and removed from the building box. Subsequent thermal debinding was performed in an ambient atmosphere at 345 °C for three hours. Thereafter, the specimens were sintered in an H800 SF vacuum furnace (Vacua Therm Ltd., UK) at 1320 °C and approximately 0.1 Pa for 6 h and finally slowly cooled in the furnace (< 20 °C/min).

The equilibrium phase fractions and phase compositions of MAR-M247 were estimated via Thermo-Calc and are shown in Fig. 8 as a function of temperature. Of particular interest are the phase fractions and phase compositions of the  $ \gamma $ and  $ \gamma' $-phase, which vary substantially over the temperature range of interest (700–1350 °C), as shown in Fig. 8a.

Further assessment of the  $ \gamma' $ size fractions through X-ray diffraction analysis was inconclusive due to the overlap of the major reflections of  $ \gamma $ and  $ \gamma' $-phase that prevented distinguishing between these two phases (see Supplementary material Fig. S1).

For high-temperature applications of binder-jetted MAR-M247, solution treatment and further densification are regarded as unavoidable. For this purpose, a HIP treatment at a higher temperature than applied here (e.g., 1250 °C) could enable both densification and dissolution of γ'-phase. The observed grain boundary pinning by the presence of carbides is anticipated to avoid grain growth during a HIP-treatment in the temperature range for solution heat treatment.

CRediT authorship contribution statement

Supplementary data associated with this article can be found in the online version at doi:10.1016/j.addma.2021.101912.

[42] K. Kakehi, Tension/compression asymmetry in creep behavior of a Ni-based superalloy, Scr. Mater. 41 (1999) 461–465, https://doi.org/10.1016/S1359-6462(99)00191-8.