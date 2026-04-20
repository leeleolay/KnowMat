DOI: 10.1016/j.jmatprotec.2018.08.031

# Characterization of Inconel 625 fabricated using powder-bed-based additive manufacturing technologies

J.A. Gonzalez $ ^{a,b} $, J. Mireles $ ^{a,c} $, S.W. Stafford $ ^{b} $, M.A. Perez $ ^{a,*} $, C.A. Terrazas $ ^{a,c} $, R.B. Wicker $ ^{a,c} $

 $ ^{a} $ W.M. Keck Center for 3D Innovation, The University of Texas at El Paso, El Paso, TX 79968, USA

 $ ^{b} $ Department of Metallurgical, Materials and Biomedical Engineering, The University of Texas at El Paso, El Paso, TX 79968, USA

 $ ^{c} $ Department of Mechanical Engineering, The University of Texas at El Paso, TX 79968, USA

## ARTICLE INFO

Associate Editor: Gary J. Cheng

## Keywords

Binder jetting

Powder bed fusion

Microstructure

Electron beam powder bed fusion

Laser powder bed fusion

Inconel 625

## Abstract

The purpose of this study was to perform a comparative analysis of powder-bed-based additive manufacturing (AM) technologies during the production of metallic components using Inconel 625 powder material. The AM technologies explored in this study include electron beam powder bed fusion (EPBF), laser powder bed fusion (LPBF), and binder jetting technology. Samples were fabricated in two build directions (X and Z build orientations) for this evaluation process, where all specimens underwent a hot isostatic pressing (HIP) post-process. The comparison was made in terms of microstructure and mechanical properties including ultimate tensile strength (UTS), yield strength (YS), percent elongation, and modulus of elasticity (E). Microstructural characterization showed evidence of equiaxed grain formation for binder jetting and LPBF parts, whereas EPBF parts displayed a more columnar grain formation parallel to the build direction. Six specimens were tested per technology, three built in the X orientation and three built in the Z orientation. All six specimens were built in a single run of each AM machine. Results indicated that all three technologies are capable of meeting the minimum requirements of the ASTM F_{3056}-14 standard for parts produced in the X orientation, with properties that are similar to wrought Inconel 625. In the Z orientation, however, only LPBF was able to meet the minimum standard requirements. Through the comparative analysis of the mechanical properties, this work showed that LPBF outperformed the other technologies in a majority of the evaluated properties, followed by EPBF and binder jetting. An analysis of the fracture surfaces of tensile specimens was also performed, and it indicated ductile fracture (dimple rupture) for the specimens produced with all three of the AM technologies studied. Nevertheless, the characterization also showed certain differences in the fractured surfaces, such as the presence of un-sintered powder particles for the binder jetting processed Inconel 625, or the development of the so called woody structure for the EPBF processed material. This study can be used to determine distinct characteristics between the three powder-bed-based technologies for the fabrication of Inconel 625 that can further include other technologies and materials using similar approaches.

## 1. Introduction

Additive manufacturing (AM) represents manufacturing processes that fabricate parts through the addition of material in a layer-by-layer fashion. AM is gaining popularity for part manufacturing that can directly compete with traditional manufacturing methods such as subtractive, joining, or formative (Conner et al., 2014). As of 2016, the market value of AM was ~$6.06 billion with an estimated potential growth of 4.3 times by the year 2022 (Wohlers, 2017). Advantages when using AM technologies can include such things as time and cost reduction, minimal human interaction, less waste creation, and reduced geometric shape constraints (Wong and Hernandez, 2012). Although growth is apparent across nearly all AM platforms, technologies with capabilities of producing metallic parts have arguably received the most widespread interest, where powder bed fusion (PBF) technologies using lasers (LPBF) and electron beams (EPBF), as per ISO/ASTM 52900 (ASTM International, 2015), as the energy sources lead with 90% of fabrication in the metal AM market (Context 3D Printing Analysis Service, 2016). Along with PBF, binder jetting is an emerging lower cost technology for the fabrication of metallic components. For example, binder jetting offers a versatile range of materials for fabrication, and is currently being utilized for sand mold and casting applications (Wohlers, 2017). PBF processes, however, are already being employed in the biomedical and aerospace markets. For example, ~50,000 hip

implants fabricated using electron beam melting (EBM, a tradename for EPBF) have been implanted in patients today, while General Electric has undergone manufacture of its LEAP engine fuel nozzles using direct metal laser melting (DMLM, a tradename for LPBF) providing them with higher life cycles while reducing overall weight and production costs (Wohlers, 2017). The adaptation of these technologies continues to expand into multiple application markets, driving the AM industry towards the qualification of more metal alloys for use with PBF processes. Nickel-based superalloys such as Inconel 718 and 625 have seen widespread adoption in multiple fields due to the alloys' multipurpose capabilities and range of applications. While conventional manufacturing of components using these high-performance alloys has been difficult due to excessive tool wear and low material removal rates, the use of powder-based AM technologies can remove these constraints while also improving lead times and reducing manufacturing costs (Costes et al., 2007; Buchbinder et al., 2011).

Inconel 625 can best be described as a nickel-based superalloy that exhibits excellent mechanical strength, resistance to thermal deformation, good surface stability and resistance to oxidation (Rai et al., 2004). Inconel 625 consists mostly of nickel (61.0 wt%) and chromium (21.5 wt%) with other alloying elements including molybdenum, niobium, and iron (Eiselstein and Tillack, 1991). For PBF AM, the chemical requirements (in wt%) for Inconel 625 include: Cr at 20-23%, Mo at 8-10%, Niobium at 3.15-4.15%, and maximum wt% for C at 0.10, Mn at 0.50, Si at 0.50, P at 0.015, S at 0.015, Co at 1.00, Ti at 0.40, Al at 0.40 and Fe at 5.00, with the remainder of Ni (ASTM International, 2014a). Inconel alloys are known as superalloys because of their excellent mechanical strength and resistance to creep and corrosion in harsh environments. Inconel 625 has found widespread and diverse applications in the aerospace, marine service and petrochemical industries due to the excellent combination of strength, resulting from age hardening, at both ambient and elevated temperatures, as well as corrosion resistance (Rai et al., 2004). In the aerospace industry, gas turbine engine exhaust systems, spray bars, thrust reverser systems, turbine shroud rings, fuel/hydraulic line tubing and bellows, are just a few examples of components where Inconel 625 is used (Floreen et al., 1994). Finally, Inconel 625 has seen widespread use in marine service and in the nuclear industry due to the ability of the material to resist sea water corrosion (Hu et al., 2010). Inconel 625 components have been manufactured using several conventional manufacturing processes such as casting, powder metallurgy, spray forming, weld overlaying and co-extrusion of piping components (Song and Nakata, 2010).

As the demand and growth of AM continues, fabrication using AM with Inconel 625 has emerged as a promising method for part production. Therefore, the focus of this research is a characterization of Inconel 625 components fabricated by three different powder-bed-based AM technologies with an emphasis on comparing the mechanical properties of components manufactured with each technology. Each technology has associated benefits, and efforts are ongoing to compete with conventional production processes across several industries, despite each technology's unique differences. The three AM technologies evaluated in this study consist of two PBF processes, including EPBF and LPBF, and the binder jetting process. A thorough material characterization of Inconel 625 parts fabricated using these three technologies was performed followed by a mechanical properties comparison for components built in two orientations: horizontal (X) and vertical (Z). The mechanical properties evaluated include ultimate tensile strength (UTS), yield strength (YS), percent elongation and modulus of elasticity. In addition to mechanical properties, metallurgical characterization consisting of microstructural and fracture analysis was performed to further analyze differences in the fabrication process. Results were then compared to ASTM standards established for AM fabrication of Inconel 625.

## 2. Technologies studied

## 2.1. Binder jetting

The first powder-bed-based AM technology explored in this comparison was binder jetting. Binder Jetting is defined as an “additive manufacturing process in which a liquid bonding agent is selectively deposited to join powder materials,” according to ISO/ASTM 52900 (ASTM International, 2015). It is an AM process in which parts are fabricated in a layer-by-layer fashion using a polymer-based or aqueous binder. A roller mechanism is utilized to spread the precursor powder onto a powder bed. The powder particles are subsequently joined together through the deposition of binder, using a piezo-driven print head, according to a CAD design. The deposited binder is treated by an infrared heating system, slightly hardening the layer to allow the spreading of a new powder layer to take place. This process is repeated until the part is complete. Parts fabricated via binder jetting must undergo two essential post-fabrication processes: (1) binder curing (referred to as drying by ExOne, the manufacturer of the system studied herein) and (2) sintering. The curing cycle, performed on the entire powder bed, further hardens the printed part (green body), creating a brown body capable of withstanding the subsequent removal of unwanted powder. This process takes place in an oven at temperatures of 195 ^\circC ours (1 hour for ~1 h per 10 mm of part height. The final step in the creation of a dense part, sintering, is performed on the brown body at elevated temperatures necessary to initiate sintering, usually ranging from 0.5 to 0.8 times the melting point (T_m, 1290–1350 ^\circC for Inconel 625), allowing the powder particles to fuse together (Anon., 2018). One advantage of binder jetting over other powder-bed-based technologies is its ability to manufacture parts using a wider range of materials, including ceramics, metals, polymers and sand (Gaytan et al., 2015).

## 2.2. Powder bed fusion (PBF)

As per ISO/ASTM 52900, powder bed fusion is defined as “an additive manufacturing process in which thermal energy selectively fuses regions of a powder bed” (ASTM International, 2015). The fabrication of metal components is achieved by controlling the powder fusion to a prescribed region at the given layer as commanded by a CAD design, followed by the creation of a new layer. As previously mentioned, the two most common forms of powder bed fusion are EPBF and LPBF, which are described in further detail in the following sub-sections as well as characterized and compared.

## 2.2.1. Electron beam powder bed fusion (EPBF)

The EPBF process is an AM technique used for fabrication of metallic components through the use of an electron beam as the energy source to melt powder particles together. The process can be broken down into three major steps: (1) raking of a powder layer, (2) preheating of powder particles (sintering), and (3) melting of the powder particles. After a particular layer is melted, the build platform is lowered one layer height (50–70 µm) and the process is repeated until the fabrication is complete. The process takes place in a vacuum environment (~10⁴ Torr) and at a high powder bed temperature of ~850 ^\circC for Inconel 625, producing parts with reduced build up of residual stress (Murr et al., 2012). EPBF can process a vast variety of materials and Arcam, the manufacturer of the EPBF equipment used here, has commercially released parameters for materials such as the titanium alloy Ti6Al4V, Ti6Al4V ELI, titanium grade 2, Arcam ASTM F_{75} cobalt-chrome, and nickel-based superalloy Inconel 718 (Arcam, 2011).

## 2.2.2. Laser powder bed fusion (LPBF)

The LPBF process accomplishes the fusion of powder particles with the use of a laser beam as the thermal energy source. The LPBF fabrication process is completed in an inert gas environment (argon or nitrogen), differing from EPBF. A blade mechanism spreads a new powder

layer onto the build area, where the laser beam then selectively fuses powder particles together, generating fully dense components (Bremen et al., 2012). In contrast to EPBF where the electron beam can be used to preheat the powder bed in each layer to temperatures in excess of 700 ^\circC for most materials, LPBF fabrication is done at relatively lower powder bed temperatures (typically less than 200–300 ^\circC), and finer precursor powder is generally used for fabrication, ranging commonly from 10 to 45 \mum. Commercially available parameters for LPBF enable for fabrication of parts at layer heights that usually range from 20 to 70 \mum. Another noteworthy difference is that a post-fabrication processes such as stress relief may be required for certain materials due to potential residual stress build up during fabrication with the LPBF process (Kruth et al., 2004). LPBF technology has achieved success in the fabrication of titanium alloys, stainless steel, tool steels, aluminum, cobalt chrome and nickel based alloys (SLM Solutions, 2018).

## 3. Materials and methods

## 3.1. Fabrication

Binder jetting specimens were fabricated by the ExOne Company using an M-Flex system (ExOne, North Huntingdon, PA, USA) with an ethylene glycol monobutyl ether (aqueous-based) binder. The green body products were sintered utilizing a sintering profile that reached maximum temperatures of 1310 ^\circC (with a dwell time of 2 h), taking roughly 16 h total until cooldown. Both PBF fabricated specimens were built at the W.M. Keck Center for 3D Innovation at the University of Texas at El Paso (UTEP). EPBF specimens were printed using an Arcam A2 system (Mölndal, Sweden) with optimized parameters developed in-house for which density was the success metric. These parameters included a powder bed preheat temperature target of ~850 ^\circC, a beam speed of 500 mm/s, an average current of 14 mA, and a focus offset of 20 mA. LPBF parts were fabricated in an SLM Solutions 125 HL system (Lübeck, Germany) available in-house using commercially available parameters specifically developed by SLM Solutions GmbH for processing the Inconel 625 alloy at 30 \mum layers. These parameters consisted of a power of 175 W, laser speed of 600 mm/s, and hatching space of 0.14 mm. The processing parameters employed for fabrication using each technology lead to microstructural differences that also translate into variations in mechanical properties. These differences are intrinsic to the AM processes themselves. For example, an interesting feature that occurs in binder jetting is the development of microstructural twins post-sintering, a feature not reported as of yet for PBF as-fabricated parts. In the case of PBF, for both EPBF and LPBF, it is common to see the development of microstructure with a directional solidification character, where precipitates are observed to follow a columnar array pattern. Specifically in the case of LPBF, the microstructure of as-fabricated parts usually exhibits the presence of melt-pool bands and has a micro-cellular and columnar morphology.

Using each technology, round bars were built in two orientations (i.e. horizontal or X direction, and vertical or Z direction, as referred in Fig. 1) for evaluation and testing of mechanical properties. A total of six cylindrical bars (8 mm radius x 90 mm height) were fabricated using each technology; three in the X direction and three in the Z direction. The specimen size and shape were chosen to best satisfy ASTM E8/E8M test standards (ASTM International, 2014a). Build orientations were followed as defined by the applicable ASTM standard terminology for AM coordinate system and test methodologies (ASTM International, 2014b). For all technologies used, Z bars were built directly on the substrate. In the case of X bars built using EPBF and LPBF, these were fabricated using a 3 mm offset from the substrate with pin supports in down skin surfaces. This was done as a means to prevent effects of diffusion of elements from the substrate to the sample's gauge section that could influence the microstructure and mechanical properties. No support structures were required for any parts built using binder jetting; they were fabricated directly in the powder bed.

## 3.2. Post-processing

All as-fabricated cylindrical samples underwent post-fabrication hot isostatic pressing (HIPing) for 3 h at 1163^\circC \pm 3.5^\circC and 102 MPa \pm 1.72 MPa. Samples fabricated using EPBF and LPBF were cut from the start plate using a band saw before HIPing was performed. HIPed samples were then machined to required specifications.

## 3.3. Powder analysis

The metal powders used for each technology were analyzed and compared as they originated from different manufacturers. Powder used for EPBF fabrication was purchased from Carpenter Powder Products (Product #2221103-0007, Bridgeville, PA, USA) while powder for fabrication with LPBF was purchased directly from SLM Solutions GmbH (Product #2015000568, Lübeck, Germany). As previously noted, ExOne produced the binder jetting test specimens at their North Huntingdon, PA facility. In this case, the powder provider was not disclosed by ExOne. The powder used for binder jetting fabrication was provided by ExOne and analyzed at UTEP. The characteristics of available powders were determined prior to fabrication. Their morphology, particle size and chemical composition were evaluated using a Hitachi TM 1000 Tabletop Scanning Electron Microscope (Tokyo, Japan). Particle size was measured using a method described previously (Gaytan et al., 2015). Flow rates for the powders were determined following ASTM Standard B_{213}-13 (ASTM International, 2014c).

## 3.4. Characterization

Characterization of properties for powder-bed-based fabricated Inconel 625 was determined by the following specifications and standards. Apparent density measurements of as-fabricated and HIPed samples were conducted using ASTM standard B311-13. The percent
Fig. 1. Generic representation of fabricated bars for tensile testing used in the comparison study. (A) shows the X and Z orientations utilized for fabrication of the cylindrical specimens, while (B) shows the final test specimens after machining.

relative density (%RD) for parts was calculated as the quotient of the obtained density value over the density of Inconel 625 (8.44 g/cm³) (Special Metals Corporation, 2013). HIPed specimens were then prepared for metallographic analysis to determine grain size and orientation differences between the fabrication processes following ASTM standard E3. Cubes (measuring 15 mm per side) were mounted and ground with the use of SiC grit paper, then polished with an alumina (Al₂O₃) and distilled water mixture. Once the final polishing process was complete, the specimens were electro-etched at 5 V for 7 s using chromic acid (H₂CrO₄) to reveal the microstructure and grain boundaries. Etched samples were examined under bright field optical microscopy using a Leica Reichert MEF4 A/M inverted metallographic system (Leica Microsystems, Wetzlar, Germany).

Tensile testing was performed on all six samples fabricated with all three technologies using an MTS Landmark servohydraulic test system (Eden Prairie, MN). Specimens were tested using a strain rate of 0.005 mm/mm/min and results were calculated based on data provided by the testing system. After tensile testing was concluded, specimens were viewed under a Hitachi Scanning Electron Microscope SU3500 (Tokyo, Japan) for analysis of the fracture surfaces to identify fracture modes.

## 4. Results and discussion

## 4.1. Density measurements and powder characterization

Density measurements of powder-bed-based specimens revealed that both EPBF and LPBF specimens in either condition (i.e. as-fabricated or HIPed) had an average apparent density of 99.9%. The average apparent density for binder jetting printed parts increased from 96.5% to 98.3% once post-processing (HIPing) was performed.

Powder images for the three powders used for fabrication are seen in Fig. 2, where EPBF and LPBF powders are nearly all spherical; a typical feature of gas atomized powders used for PBF AM processes. However, finer, more agglomerated powder particles are seen in powder used for binder jetting fabrication. Also, this powder exhibited the smallest particle size, with an average of 11  $ \mu $m (refer to Table 1), and appeared with a large amount of satellites when compared with the other two powders. It has been found previously that finer powder particle sizes lead to a larger amount of satellite formations (Özbilen, 1999). The irregular shape and satellite formation also contribute to a slower flow rate compared to the powders used for EPBF or LPBF fabrication, and are hence less ideal for powder-bed-based AM fabrication (Spierings et al., 2016). Although not considered in this research, the flowability of powders, a characteristic directly related to the powder size distribution and shape, can influence the AM process and the resulting mechanical properties of the fabricated components. For example, Nguyen et al. described how the powder size distribution and shape influenced the raking process during LPBF. The authors found that powder shape changed as the number of process cycles increased leading to differences in packing density and hence of the final density of the parts (Nguyen et al., 2017). Sutton et al. recently reviewed the techniques used for characterization of precursor powders used in PBF processes concluding that a correlation exists between particle size and size distribution and the powder's ability to flow which in turn influences the homogeneity of each layer and the potential for porosity to develop (Sutton et al., 2017). All measured powder characteristics are listed in Table 3. The chemical composition for the precursor powder of the three technologies is compared in Table 1, confirming that all powders used during fabrication met ASTM chemical requirements.

## 4.2. Microstructure

Microstructure analysis provides insight as to how the fabrication process may affect the performance of the final product. It is well known that AM technologies, because of their layerwise approach, produce anisotropic properties, an effect that is related to the anisotropy of microstructure such as the observed preferential growth of grains in the build direction in EPBF and non-heat treated LPBF (Murr, 2015). Samples produced through binder jetting showed a consistent microstructure regardless of build orientation, with an amount of porosity present in both microstructural directions (Fig. 3(A)). The visible porosity in the micrographs can be correlated with a decrease in mechanical properties. For this material, larger grains are evident when
Fig. 2. SEM images of Inconel 625 powders used for (A) binder jetting, (B) EPBF and (C) LPBF fabrication.

As-received powder characteristics and analysis for the three technologies.

| Technology | Mass (g) | AD (g/cc) | Solid density (g/cc) | %Density change | Flow rate x avg. (s/50g) | Particle size distribution ( $ \mu $m) | Avg. particle size ( $ \mu $m) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Binder Jetting | 97.56 | 3.9 | 8.44 | 46.16 | 18.56 | 7-24 | 11 |
| EPBF | 108.82 | 4.35 | 8.44 | 51.57 | 130.69 | 21-46 | 23 |
| LPBF | 82.78 | 3.31 | 8.44 | 39.23 | 204.3 | 8-33 | 16 |

compared to those of the fusion technologies with an average grain diameter of 57  $ \mu $m, measured using the line intercept method. Recent research by Mostafaei et al. on the binder jetting printing of Inconel 625 showed the presence of pores that were not interconnected, and that formed preferentially at the grain boundaries (Mostafaei et al., 2016a). The porosity formation detailed by this study occurred even after sintering to temperatures of 1200 ^\circC. Furthermore, in research from the same group, porosity was substantially reduced, after sintering to 1300 ^\circC, for specimens printed using binder jetting and gas atomized Inconel 625 as the precursor powder, in contrast to the persistent porosity observed for specimens printed using water atomized powder (Mostafaei et al., 2017). The micrographs of the binder jetting produced material also revealed annealed twins within the austenitic grains, a characteristic indicative of a material with a low stacking-fault energy (Tehovnik et al., 2015). Twins formation typically occurs when recrystallization of a cubic-closed packed austenitic metal is accomplished at elevated temperatures (Tehovnik et al., 2015), such as those reached during the sintering process of binder jetting. The formation of twins has also been characterized by SEM for the Inconel 625 alloy processed by binder jetting after sintering (Mostafaei et al., 2016a). The microstructure of EPBF fabricated components has distinct characteristics that appear to be dependent on build orientation (Fig. 3(B)). For
Fig. 3. Microstructure three-dimensional cube representation of sectioned specimen's after polishing and electro-etching of Inconel 625. (A) Shows binder jetting microstructure, (B) EPBF microstructure and (C) LPBF microstructure.

example, parallel to the build direction grains have a more uniform pattern. However, perpendicular to the build direction the microstructure of these samples appears with a textured columnar grain morphology, with grains measuring an average of 16 \mum wide and 356 \mum in length. Murr et al. showed that EPBF fabricated Inconel alloys, such as 625 and 718, exhibit directional growth of precipitates within the melt zones (Murr, 2015). The precipitates that are formed in a columnar pattern, parallel to the build direction, have been identified as \gamma'' (bct) Ni₃Nb disk platelets coincident with Ni-Cr (fcc) {111} planes (Murr, 2015). In this work, the dark linear areas visible in the micrograph in Fig. 3(B) are the columns of \gamma'' precipitates, following the build direction as was described by Murr et al. Similarly, Amato et al. showed the characteristic directional microstructure that developed for as-fabricated Inconel 625 produced by EPBF. Their work, similar to the findings presented in this manuscript, detailed the columnar arrays of Ni₃Nb precipitates that spanned multiple layers in height and that arranged parallel to the build direction. The average diameter for columnar grains in the EPBF processed Inconel 625 was measured at ~10 \mum in size, although the average grain length was not reported. Further, Amato et al. demonstrated a change in the microstructure of the components after HIPing, which induced the formation of equiaxed grains and of annealing twins (Amato et al., 2012). It is important to state that the formation of twins was induced through HIPing, but not during the EPBF printing process itself. The microstructure of LPBF fabricated parts appears homogenous and with equiaxed grains compared to those of produced by EPBF and binder jetting in both studied orientations (Fig. 3(C)). The average grain size using the line intercept method for this material was 27 \mum, a 53% decrease in size from that of binder jetting. Amato et al. described the microstructure of HIPed Inconel 625 processed by LPBF as consisting of a NiCr equiaxed grains with the presence of annealing twins. The study also found a large amount of grain boundary precipitates (i.e. intergranular precipitates) for the material (Amato et al., 2012). Recent results by Marchese et al. characterized the evolution of LPBF processed Inconel 625. The study found that the microstructure consisted of columnar grains aligned in the build direction which were characterized as very fine columnar cellular structures when observed at higher magnifications. The microstructure was unaltered under aging at 700 ^\circC for 24 h, but under solutioning at 1150 ^\circC for 2 h, or a combination of solutioning and aging using the previous parameters, did result in recrystallization of grains ranging from 10 to 90 \mum in size (Marchese et al., 2018). Hall-Petch relation states that a finer grain size will strengthen a material's mechanical properties by promoting the resistance of dislocation motion (Hansen, 2004). As such, it can be inferred that the LPBF process has the capability of producing a more desirable microstructure for high strength applications. Further, the microstructure of LPBF components shares the most similarity to that of microstructure typically seen in wrought Inconel 625 in its non-annealed state (American Society for Metals, 2018; Li et al., 2011).

## 4.3. Mechanical properties

Results of mechanical testing for the three technologies were compared to the ASTM standard F_{3056}-14 as this specification provides a baseline for components produced by AM technologies to meet mechanical properties equivalent to those of forged and/or wrought nickel alloy products (ASTM International, 2014a). The minimum acceptance requirements outlined by the standard were the values used as a reference point. Bar charts for the calculated mechanical properties are presented in Fig. 4. Data points were also compared statistically to determine if the difference between the obtained mechanical property values for the three technologies were significantly different by the use of a t-test. t-test results were used to determine a p-value with the use of a t-distribution. A p-value can be used to determine statistical difference between two data populations where the null hypothesis is rejected when p is less than 0.05 (at a 95% confidence level) (Montgomery and Runger, 2004). The average values for the mechanical properties obtained from the three technologies are presented in Table 4 with the indication of build direction.

## 4.3.1. Ultimate tensile strength (UTS)

The UTS was calculated based on the highest level of force (kN) that a given specimen was able to withstand during the tensile test, divided by the original area of the gauge section (mm $ ^{2} $). Based on the results of specimens fabricated in the X orientation, LPBF samples had the highest ultimate tensile strength (0.91 \pm 0.03 GPa) with binder jetting displaying the lowest UTS (0.71 \pm 0.02 GPa). There was no significant difference between LPBF and EPBF produced specimens, but a significant difference was noted between binder jetting samples and the other two technologies. For specimens fabricated in the Z orientation, LPBF also displayed the highest UTS (0.84 \pm 0.02 GPa) followed by EPBF and binder jetting with only a 0.02 GPa non-significant difference between the two. The average UTS for LPBF produced samples did display a significant difference when compared with the two other technologies. All three technologies surpassed the minimum requirement set by the ASTM F_{3056}-14 standard (0.485 GPa in both the X and Z build orientations). A level of 95% confidence was calculated for the stated results.

## 4.3.2. Yield strength (YS)

YS was determined by the stress achieved before plastic deformation occurred and was measured based on the 0.2% offset method. Specimens fabricated in the X orientation showed very similar YS values with LPBF slightly above EPBF and binder jetting by 0.03 GPa and 0.07 GPa, respectively. Statistical results indicated no significant difference between LPBF and EPBF at a 95% confidence level. On the other hand, the results for binder jetting did show a significant difference compared to the other two techniques. For specimens fabricated in the Z orientation, binder jetting displayed the highest YS  $ (0.39 \pm 0.02 \text{ GPa}) $ and LPBF the lowest  $ (0.35 \pm 0.01 \text{ GPa}) $. A significant difference was seen between LPBF and the other two technologies. Yield strength results from all technologies met or exceeded the ASTM standard (0.275 GPa) required in both orientations.

## 4.3.3. % Elongation

The percent elongation is the maximum linear deflection relative to the original length that each sample was able to endure before the point of complete failure and rupture. Specimens produced in the X orientation achieved the largest elongation overall for all three technologies, with corresponding values of  $ 62\% \pm 1.99\% $ for LPBF,  $ 59\% \pm 2.14\% $ for binder jetting, and  $ 44\% \pm 4.95\% $ for EPBF. For these results, no significant difference, at a 95% confidence level, was seen between binder jetting and LPBF. Otherwise, a significant difference was noted between the other tested samples.

As for specimens built in the Z orientation, the elongation value for LPBF was much higher than the other two technologies with values that exceeded those of binder jetting and EPBF by  $ \sim $29% in each case. A significant difference was clear between LPBF and the two other technologies but not amongst binder jetting and EPBF. All specimens built in the X orientation were able to exceed the minimum 30% elongation required as per the ASTM standard; however only the LPBF built samples exceeded the minimum requirement in the Z orientation.

## 4.3.4. Modulus of elasticity

The modulus of elasticity (represented by the letter E) indicates the tensile resistance to deformation along the axis where the force is acting upon (Callister, 2007). To determine the modulus of elasticity, the slope for the elastic region of the stress-strain curve was used. This property provides the stiffness of the fabricated material in relation to the stress applied onto it. The greatest modulus of elasticity for specimens fabricated in the X orientation was seen in LPBF (0.56 GPa \pm 0.04 GPa) while the lowest was seen in EPBF (0.48 GPa \pm 0.05 GPa). A similar
Fig. 4. Mechanical properties of the three powder-bed-based technologies for horizontal (X) and vertical (Z) build Inconel 625 samples. (A) Represents ultimate tensile stress; (B) yield stress; (C) % elongation; and (D) modulus of elasticity, where the dashed line is the value for minimum tensile properties according to ASTM F_{3056}-14.

behavior was noted in Z orientation fabricated samples. However, no significant difference between any of the tested samples in either orientation was seen at a 95% confidence level.

## 4.3.5. Discussion on mechanical properties

The results obtained in this manuscript show that HIPing of binder jetting printed parts enabled higher strength values compared to other reported values for Inconel 625 in the aged condition. For example, for binder jetting as-sintered parts, Mostafaei et al. reported values of UTS, YS, and strain of 612 MPa, 327 MPa, and 41% respectively. They showed that following a solutionizing treatment, the strength values decreased to 587 MPa while strain increased by 4%. Finally, the UTS, YS and % elongation (reported as strain by this study) were 697 MPa, 329 MPa, and 30%, following aging for 60 h at 745 ^\circC (Mostafaei et al., 2016b). Amato et al. reported an increase in hardness and UTS at the expense of elongation for LPBF printed Inconel 625 specimens that were HIPed versus as-fabricated. The reported UTS, YS, and elongation values averaged ~0.90 GPa, ~0.37 GPa, and 58%, respectively, for LPBF printed specimens that had undergone HIPing at 0.1 GPa and 1120 ^\circC for 4 h. EPBF printed specimens, also subjected to the same HIPing schedule were reported to have a UTS of 0.33 GPa, YS of 0.77 GPa, and elongation of 69% by the same study. Results from Marchese et al. showed increases in YS and UTS for aged Inconel 625 that had been processed using LPBF. They showed that under an aging schedule of 700 ^\circC for 24 h, the YS and UTS were 1024 \pm 54 MPa and 1222 \pm 56 MPa, respectively with a ductility of 23% \pm 1%. This was in contrast to the as-fabricated values that were YS of 783 \pm 23 MPa, UTS of 1041 \pm 36 MPa, and ductility of 33% \pm 1% (Marchese et al., 2018).

## 4.3.6. Discussion on effects of processing parameters

In the discussion preceding this section, the developed microstructures, and mechanical properties were reported for the specimens produced using the three powder-bed-based AM methods discussed in this work. Nevertheless, it is instructive to also discuss the effects that processing parameters have on the produced components as the thermal history for a given component will vary as per the parameters employed for its fabrication. Multiple studies have concentrated on understanding the effects of processing parameters for AM produced components. Specifically related to the material of this work, for example, Mumtaz and Hopkinson investigated parameters that included pulse duration and laser speed to reduce roughness and the appearance of balling on the top surface of thin walled Inconel 625 components produced by LPBF (Mumtaz and Hopkinson, 2009). More recently,
Fig. 5. SEM images of fracture surfaces after tensile samples failed. (A) Shows the fracture surface of binder jetting horizontal build (X) with arrows pointing to the unsintered powder particles, (B) binder jetting vertical build (Z), (C) EPBF horizontal build (X) with arrows pointing in the direction of the fibering structure, (D) EPBF vertical build (Z), (E) LPBF horizontal build (X), and (F) LPBF vertical build (Z).

Koutiri et al. adjusted the volume energy density during LPBF processing of Inconel 625 to control porosity and surface finish for produced components, and related the results to their fatigue strength. They concluded that one mechanism influencing the fatigue strength was related to surface or sub-surface porosity created during the LPBF process as parameters, such as laser contour scan speed, laser diameter, and hatching strategy, were modified (Koutiri et al., 2018). The effect of laser parameters, that included current, scan speed, and frequency, were correlated with measurements of the density and layer thickness for Inconel 625 produced by LPBF in a study by Fatemi et al. (Fatemi et al., 2017). Their findings suggested that there was an increase in layer thickness from frequency gains, whereas a decreased layer thickness was observed from increases in scan speed. With regards to EPBF, List et al. investigated the effects of the electron beam parameters (including the current, speed, and focus) on the physical and mechanical properties, including elastic modulus and yield strength, for Inconel 625 cubes. They found that besides the microstructural anisotropy inherent to PBF AM processes, a structural anisotropy, due to the layering processing and influenced by the combination of processing parameters, also contributed to the anisotropic mechanical properties observed for the produced mesh cubes (List et al., 2014). Finally, although the literature is sparse for binder jetting of Inconel 625, the studies by Mostafei et al. demonstrated the variation in physical characteristics, such as porosity, depending on the post-processing (i.e. sintering and heat treatment) parameters employed, and their effect on the mechanical properties for this material produced by the aforementioned AM technique (Mostafaei et al., 2016a, 2017).

## 4.4. Fractography

A comparison of the fracture surfaces on tested tensile specimens was conducted using the SU3500 SEM. By analyzing the fracture surface, a confirmation of ductile fracture should be apparent since all samples performed with high elongation. All images shown in Fig. 5 have evidence of ductile fracture mode via indications of dimple formation on the fracture surfaces. Fractured specimens exhibited the characteristic double cup fracture, identifiable at the macroscale. Double cup fracture indicates that localized shear bands ahead of the crack tip lead to the separation of metal, and it is considered a characteristic of ductile failure in metals (Wigley, 1971). SEM images revealed equiaxed dimples in spherical morphology, which appear as the coalescence of voids formed at inclusions during plastic deformation.
Fig. 6. SEM image of binder jetting fracture surface with point EDS analysis conducted on particles and matrix metal, followed by EDS individual elemental maps of fracture surface showing a concentration of oxygen in captured particles. (For interpretation of the references to colour in the figure text, the reader is referred to the web version of this article).

Analysis of chemical composition for the powder used for fabrication with each technology.

<table border="1" style="margin: auto; word-wrap: break-word;"><tr><td style="text-align: center; word-wrap: break-word;">Element (wt %)</td><td style="text-align: center; word-wrap: break-word;">Ni</td><td style="text-align: center; word-wrap: break-word;">Cr</td><td style="text-align: center; word-wrap: break-word;">Mo</td><td style="text-align: center; word-wrap: break-word;">Nb</td><td style="text-align: center; word-wrap: break-word;">Fe</td><td style="text-align: center; word-wrap: break-word;">Mn</td><td style="text-align: center; word-wrap: break-word;">Si</td></tr><tr><td style="text-align: center; word-wrap: break-word;">Binder Jetting</td><td style="text-align: center; word-wrap: break-word;">60.12</td><td style="text-align: center; word-wrap: break-word;">22.84</td><td style="text-align: center; word-wrap: break-word;">9.16</td><td style="text-align: center; word-wrap: break-word;">4.15</td><td style="text-align: center; word-wrap: break-word;">2.9</td><td style="text-align: center; word-wrap: break-word;">0.42</td><td style="text-align: center; word-wrap: break-word;">0.32</td></tr><tr><td style="text-align: center; word-wrap: break-word;">EPBF</td><td style="text-align: center; word-wrap: break-word;">61.3</td><td style="text-align: center; word-wrap: break-word;">21.01</td><td style="text-align: center; word-wrap: break-word;">9.8</td><td style="text-align: center; word-wrap: break-word;">4.1</td><td style="text-align: center; word-wrap: break-word;">3.0</td><td style="text-align: center; word-wrap: break-word;">0.33</td><td style="text-align: center; word-wrap: break-word;">0.4</td></tr><tr><td style="text-align: center; word-wrap: break-word;">LPBF</td><td style="text-align: center; word-wrap: break-word;">61.55</td><td style="text-align: center; word-wrap: break-word;">21.25</td><td style="text-align: center; word-wrap: break-word;">9.55</td><td style="text-align: center; word-wrap: break-word;">4.05</td><td style="text-align: center; word-wrap: break-word;">2.8</td><td style="text-align: center; word-wrap: break-word;">0.5</td><td style="text-align: center; word-wrap: break-word;">0.2</td></tr><tr><td style="text-align: center; word-wrap: break-word;">ASTM</td><td style="text-align: center; word-wrap: break-word;">Balance</td><td style="text-align: center; word-wrap: break-word;">20-23</td><td style="text-align: center; word-wrap: break-word;">8-10</td><td style="text-align: center; word-wrap: break-word;">3.15-4.15</td><td style="text-align: center; word-wrap: break-word;">5.0 (max)</td><td style="text-align: center; word-wrap: break-word;">0.5</td><td style="text-align: center; word-wrap: break-word;">0.5 (max)</td></tr><tr><td colspan="6">Requirements</td><td colspan="2">(max)</td></tr></table>

(Anderson and Anderson, 2005). LPBF fabricated samples have evidence of dimples at the fracture surface present on both build orientations (Fig. 5(E) and (F)). Dimples evident in the fracture surface are caused during the plastic flow of the matrix metal surrounding nucleation sites, leading to the formation of micro-voids (Hertzberg, 1989). EPBF samples fabricated in the Z orientation also showed dimples on the fracture surface (Fig. 5(D)). However, samples fabricated in the X orientation exhibited a predominant texture appearance of fracture surface (Fig. 5(C)) in comparison to that of the Z built EPBF sample (Fig. 5(D)). This texture appears to be elongated fibering, which is a typical effect for metals that have been mechanically processed, and has been referred to as a “woody structure” (Hertzberg, 1989). The mechanical processed components may result in alloy segregation stringers, leading to phases with alignment along a specific orientation,

Average value for the mechanical properties of the three compared powder-bed-based AM technologies. The valued is based on an average of all samples after tensile testing.

<table border="1" style="margin: auto; word-wrap: break-word;"><tr><td style="text-align: center; word-wrap: break-word;"></td><td colspan="2">Binder Jetting</td><td colspan="2">EPBF</td><td colspan="2">LPBF</td></tr><tr><td style="text-align: center; word-wrap: break-word;"></td><td style="text-align: center; word-wrap: break-word;">X</td><td style="text-align: center; word-wrap: break-word;">Z</td><td style="text-align: center; word-wrap: break-word;">X</td><td style="text-align: center; word-wrap: break-word;">Z</td><td style="text-align: center; word-wrap: break-word;">X</td><td style="text-align: center; word-wrap: break-word;">Z</td></tr><tr><td style="text-align: center; word-wrap: break-word;">UTS (GPa)</td><td style="text-align: center; word-wrap: break-word;">$ 0.707 \pm 0.012 $</td><td style="text-align: center; word-wrap: break-word;">$ 0.708 \pm 0.022 $</td><td style="text-align: center; word-wrap: break-word;">$ 0.849 \pm 0.037 $</td><td style="text-align: center; word-wrap: break-word;">$ 0.723 \pm 0.029 $</td><td style="text-align: center; word-wrap: break-word;">$ 0.906 \pm 0.028 $</td><td style="text-align: center; word-wrap: break-word;">$ 0.842 \pm 0.029 $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">% Elongation (at break)</td><td style="text-align: center; word-wrap: break-word;">$ 58.74 \pm 2.14 $</td><td style="text-align: center; word-wrap: break-word;">$ 27.02 \pm 5.39 $</td><td style="text-align: center; word-wrap: break-word;">$ 44.32 \pm 4.95 $</td><td style="text-align: center; word-wrap: break-word;">$ 26.92 \pm 5.49 $</td><td style="text-align: center; word-wrap: break-word;">$ 62.34 \pm 1.98 $</td><td style="text-align: center; word-wrap: break-word;">$ 56.3 \pm 6.24 $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">Yield Stress (GPa)</td><td style="text-align: center; word-wrap: break-word;">$ 0.32 \pm 0.014 $</td><td style="text-align: center; word-wrap: break-word;">$ 0.393 \pm 0.002 $</td><td style="text-align: center; word-wrap: break-word;">$ 0.367 \pm 0.033 $</td><td style="text-align: center; word-wrap: break-word;">$ 0.369 \pm 0.007 $</td><td style="text-align: center; word-wrap: break-word;">$ 0.396 \pm 0.033 $</td><td style="text-align: center; word-wrap: break-word;">$ 0.349 \pm 0.005 $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">Modulus of elasticity (GPa)</td><td style="text-align: center; word-wrap: break-word;">$ 0.524 \pm 0.047 $</td><td style="text-align: center; word-wrap: break-word;">$ 0.506 \pm 0.051 $</td><td style="text-align: center; word-wrap: break-word;">$ 0.484 \pm 0.052 $</td><td style="text-align: center; word-wrap: break-word;">$ 0.459 \pm 0.036 $</td><td style="text-align: center; word-wrap: break-word;">$ 0.561 \pm 0.014 $</td><td style="text-align: center; word-wrap: break-word;">$ 0.539 \pm 0.058 $</td></tr></table>

Table 4

Chemical composition of binder jetting fracture surface, with oxygen now being detected.

| Element | Ni | Cr | Mo | Nb | Fe | O |
| --- | --- | --- | --- | --- | --- | --- |
| Wt(%) | 54.21 | 32.34 | 4.57 | 1.65 | 1.22 | 6.43 |

which in turn lead to weak paths during deformation (Blake, 1985). EPBF microstructure revealed  $ \gamma^{\prime\prime} $(bct) precipitates in a columnar pattern which may be where the voids originated and led to segregation. These textures in EPBF fabricated samples, parallel to the build direction, imply anisotropic properties. The fracture surface of samples built using binder jetting showed a presence of what appears to be un-sintered powder particles within the fracture micro-voids (arrows in Fig. 5(A)). These particles are not present in LPBF or EPBF parts and hence, may be due to the unique fabrication process, which includes curing and sintering, that binder jetting samples undergo.

Further evaluation of these unsintered particles was conducted to determine their composition. Using the SU3500 SEM, an energy-dispersive X-ray spectroscopy (EDS) study was performed on these particles to accurately identify their chemical composition, resulting in subtle differences compared to the metal matrix of the fabricated specimens (Fig. 6). Using EDS mapping various elements were identified, including Ni (green), Cr (red), Mo (pink), Nb (dark green), Fe (orange), and O (blue) on the fracture surface, seen in Fig. 6. Oxygen can be seen at a relatively high concentration within the encapsulated and unsintered particles (seen with a bright blue color indication), with point EDS results indicating  $ \sim $20 wt% oxygen content in certain particles. Particles also showed a high chromium content, considered to be an oxidation sensitive element, where thermodynamically stable oxides can be found on surfaces at elevated temperatures (Tunberg and Nyborg, 1995). The presence of oxygen might impede the formation of bonds and the coalescence of powder particles during sintering (Bergman, 2011), which can help explain the presence of these particles even after the material was subjected to a high temperature sintering. As mentioned before, sintering of these samples was performed in a vacuum/inert gas environment and the precursor powder showed no signs of oxygen content (Table 2). However, deposited binder during the fabrication process may be a source of oxidation, as the binder will vaporize and can become captured within the fabricated layers during the curing and sintering post-fabrication steps. The full chemical composition of the fracture surface of binder jetting samples, including oxygen, is defined in Table 2.

## 5. Conclusion

This work has presented a comparative analysis of three powder-bed-based AM techniques (LPBF, EPBF and binder jetting) that can be used for manufacturing of Inconel 625, by assessing the microstructures and mechanical properties of components fabricated using them. To the authors' knowledge, this is the first time such comparative data have been published. The mechanical testing results indicated that all three technologies were able to surpass the minimum values for UTS, % elongation, and YS that are required by the ASTM standard F_{3056}-14, achieving equivalent properties to wrought Inconel 625 for the X build orientation specimens. LPBF fabricated samples performed with the most uniformity in the majority of the mechanical properties evaluated, with both orientations satisfying the minimum ASTM standard requirements. The microstructure of EPBF produced parts showed the development of columnar grains which are associated with anisotropic mechanical properties as confirmed in this study. Binder jetting fabrication resulted in some oxidation of the powder particles, that contained chromium and oxygen as characterized by EDS, and which may be a result of the type of binder used in the fabrication process. The uniqueness of each technology brings a degree of variability that affects the properties of a printed part. Therefore, it is important to determine which technology is most adequate and best suited for a particular application. Nevertheless, with the ability for the three technologies to exceed the minimum standard requirements, it can be stated that these techniques can be used effectively for fabrication of Inconel 625 components, at least in the X build orientation. While this study only considered static mechanical properties and metallurgical features, other variables also need to be taken into account to appropriately select a manufacturing process for a given application. One such example is the fatigue performance for components fabricated using each AM technique, which might be the subject of further research. Although additional research is required, this study can be used to assist companies with considering powder-bed-based technologies as alternative metal fabrication processes to conventional methods.

## Acknowledgements

The research was performed at The University of Texas at El Paso (UTEP) within the W.M. Keck Center for 3D Innovation, a state-of-the-art additive manufacturing research facility. The research was supported, in part, by the U.S. Department of Energy (DOE) through award No. DE-FE0012321. Any findings, opinions, conclusions, or suggestions herein are those of the authors, and do not necessarily reflect the views of DOE or any other individual, corporation or federal agency. The authors are grateful to Dr. David Roberson, from the Metallurgical, Materials and Biomedical Engineering department, for facilitating access to the SU3500 SEM, and to Philip Morton for his participation and contribution in various aspects of this work.

## References

Amato, K., Hernandez, J., Murr, L.E., Martinez, E., Gaytan, S.M., Shindo, P.W., Collins, S., 2012. Comparison of microstructures and properties for a Ni-base superalloy (Alloy 625) fabricated by electron beam melting. J. Mater. Sci. Res. 1 (2), 3.

Anderson, T.L., Anderson, Ted L., 2005. Fracture Mechanics: Fundamentals and Applications, 3rd ed. CRC Press Taylor & Francis Group, Boca Raton.

ExOne Digital Part Materialization, Available: http://www.exone.com/Systems/Production-Printers/M-Flex. (Accessed 25 January 2017).

Arcam, A.B., 2011. Arcam EBM Users’s Manual. Arcam, Sweden.

ASTM International, 2014a. ASTM F_{3056}-14 Standard Specification for Additive Manufacturing Nickel Alloy (UNS N_{06625}) With Powder Bed Fusion. ASTM International, West Conshohocken, PA, USA.

ASTM International, 2014b. F2921-11 Standard Terminology for Additive Manufacturing-Coordinate System and Test Methodologies. ASTM International, West Conshohocken, PA, USA.

ASTM International, 2014c. Standard Test Methods for Flow Rate of Metal Powders Using the Hall Flowmeter Funnel. ASTM International, West Conshohocken, PA, USA.

ASTM International, 2015. ISO/ASTM 52900: Standard Terminology for Additive Manufacturing - General Principles - Terminology. ASTM International, West Conshohocken, PA, USA.

Bergman, O., 2011. Key Aspects of Sintering Powder Metallurgy Steel. Chalmers University of Technology, Gothenburg, Sweden.

Blake, A., 1985. Handbook of Mechanics, Materials, and Structures. Wiley-Interscience, Livermore, CA.

Bremen, S., Meiners, W., Diatlov, A., 2012. Selective laser melting: a manufacturing technology for the future? Rapid Manuf. 33–38.

Buchbinder, D., Schleifenbaum, H., Heidrich, S., Meiners, W., Bültmann, J., 2011. High power selective laser melting (HP SLM) of aluminum parts. Phys. Procedia 12, 271–278.

Callister Jr., W.D., 2007. Materials Science and Engineering an Introduction. John Wiley & Son, Inc., York, PA.

Conner, B.P., Manogharan, G.P., Martof, A.N., Rodomsky, L.M., Rodomsky, C., Jordan, D.C., Limperos, J.W., 2014. Making sense of 3-D printing: creating a map of additive manufacturing products and services. Addit. Manuf. 1–4, 64–76.

Context 3D Printing Analysis Service, 2016. Powder Bed 3D Printing Solutions on the Rise Powder Bed Fusion for Metal and Plastics Set for Highest Growth Potential Amongst Seven Main 3D Printing Technologies. 8 September Available: https://www.contextworld.com/documents/20182/367799/CONTEXTQ2_16 + Powder + Bed + Fusion + on + the + rise + Sept2016.pdf/4a7ab03c-c80f-451b-8352-8ca89da2b5bf (Accessed 30 January 2017).

Costes, J.P., Guilet, Y., Poulachon, G., Dessoly, M., 2007. Tool-life and wear mechanisms of CBN tools in machining of Inconel 718. Int. J. Mach. Tools Manuf. 47 (7–8), 1081–1087.

Eiselstein, H.L., Tillack, D.J., 1991. The invention and definition of alloy 625. Superalloys 718, 625 and Various Derivatives. pp. 1–14.

Fatemi, S.A., Ashany, J.Z., Aghchai, A.J., Abolghasemi, A., 2017. Experimental investigation of process parameters on layer thickness and density in direct metal laser sintering: a response surface methodology approach. Virtual Phys. Prototyp. 12 (2), 133–140.

Floreen, S., Fuchs, G.E., Yang, W.J., 1994. The metallurgy of alloy 625. Superalloys 718, 625, 706 and Various Derivatives. pp. 13–37.

Gaytan, S.M., Cadena, M.A., Karim, H., Delfin, D., Lin, Y., Espalin, D., Macdonald, E., Wicker, R.B., 2015. Fabrication of barium titanate by binder jetting additive manufacturing technology. Ceram. Int. 41 (5), 6610–6619.

Hansen, N., 2004. Hall-Petch relation and boundary strengthening. Scr. Mater. 51 (8), 801–806.

Hertzberg, R.W., 1989. Deformation and Fracture Mechanics of Engineering Materials. John Wiley & Sons.

Hu, H.X., Zheng, Y., Qin, C.P., 2010. Comparison of Inconel 625 and Inconel 600 in resistance to cavitation erosion and jet impingement erosion. Nucl. Eng. Des. 240, 2721–2730.

Koutiri, I., Pessard, E., Peyre, P., Amlou, O., De Terris, T., 2018. Influence of SLM process parameters on the surface finish, porosity rate and fatigue behavior of as-built Inconel 625 parts. J. Mater. Process. Technol. 255, 536–546.

Kruth, J.P., Froyen, L., Van Vaerenbergh, J., Mercelis, P., Rombouts, M., Lauwers, B., 2004. Selective laser melting of iron-based powder. J. Mater. Process. Technol. 149

 $ (1-3) $, 616-622.

Li, D., Guo, Q., Guo, S., Peng, H., Wu, Z., 2011. The microstructure evolution and nucleation mechanisms of dynamic recrystallization in hot-deformed Inconel 625 superalloy. Mater. Des. 32, 696–705.

List, F.A., Dehoff, R.R., Lowe, L.E., Sames, W.J., 2014. Properties of Inconel 625 mesh structures grown by electron beam additive manufacturing. Mater. Sci. Eng. A 615, 191–197.

Marchese, G., Lorusso, M., Parizia, S., Bassini, E., Lee, J.W., Calignano, F., Manfredi, D., Terner, M., Hong, H., Ugues, D., Lombardi, M., Biamino, S., 2018. Influence of heat treatments on microstructure evolution and mechanical properties of Inconel 625 processed by laser powder bed fusion. Mater. Sci. Eng. A 729, 64–75.

Montgomery, D.C., Runger, G.C., 2004. Applied Statistics and Probability for Engineering. Pearson Prentice Hall, Upper Saddle River, NJ.

Mostafaei, A., Stevens, E.L., Hughes, E.T., Biery, S.D., Hilla, C., Chmielus, M., 2016a. Powder bed binder jet printed alloy 625: densification, microstructure and mechanical properties. Mater. Des. 108, 126–135.

Mostafaei, A., Behnamian, Y., Krimer, Y.L., Stevens, E.L., Luo, J.L., Chmielus, M., 2016b. Effect of solutionizing and aging on the microstructure and mechanical properties of powder bed binder jet printed nickel-based superalloy 625. Mater. Des. 111, 482–491.

Mostafaei, A., Toman, J., Stevens, E.L., Hughes, E.T., Krimer, Y.L., Chmielus, M., 2017. Microstructural evolution and mechanical properties of differently heat-treated binder jet printed samples from gas- and water-atomized alloy 625 powders. Acta Mater. 124, 280–289.

Mumtaz, K., Hopkinson, N., 2009. Top surface and side roughness of Inconel 625 parts processed using selective laser melting. Rapid Prototyp. J. 15 (2), 96–103.

Murr, L.E., 2015. Metallurgy of additive manufacturing: examples from electron beam melting. Addit. Manuf. 5, 40–53.

Murr, L.E., Gaytan, S.M., Martinez, E., Medina, F.R., Wicker, R.B., 2012. Fabricating functional Ti-Alloy biomedical implants by additive manufacturing using electron beam melting. Glob. J. Biotechnol. Biomater. Sci. 2 (3), 1–11.

Nguyen, Q.B., Nai, M.L.S., Zhu, Z., Sun, C.-N., Wei, J., Zhou, W., 2017. Characteristics of inconel powders for powder-bed additive manufacturing. Engineering 3 (5), 695–700.

Özbilen, S., 1999. Satellite formation mechanism in gas atomized powders. Powder Metall. 1 (42), 70–78.

Rai, S.K., Kumar, A., Shankar, V., Jayakumar, T., Rao, K.B.S., Raj, B., 2004. Characterization of microstructures in Inconel 625 using". Acta Mater. (51), 59–63.

SLM Solutions SLM-Solutions (Accessed February 2017). https://slm-solutions.com/products/accessories-and-consumables/slm-metal-powder.

Song, K.H., Nakata, K., 2010. Effect of precipitation on post-heat-treated Inconel 625 alloy after friction stir welding. Mater. Des. 31, 2942–2947.

Special Metals Corporation, 2013. INCONEL Alloy 625. A PCC Company, New Hartford.

Spierings, A.B., Voegtlin, M., Bauer, T., Wegener, K., 2016. Powder nowability and characterization methodology for powder-bed-based metal additive manufacturing. Prog. Addit. Manuf. 1 (1–2), 9–20.

Sutton, A.T., Kriewall, C.S., Leu, M.C., Newkirk, J.W., 2017. Powder characterisation techniques and effects of powder characteristics on part properties in powder-bed fusion processes. Virtual Phys. Prototyp. 12 (1), 3–29.

Tehovnik, F., Burja, J., Podgornik, B., Godec, M., Vode, F., 2015. Microstructural evolution of INCONEL 625 during hot rolling. Mater. Technol. 49 (5), 801–806.

Tunberg, T., Nyborg, L., 1995. Surface reactions during water atomization and sintering of austenitic stainless steel powder. Powder Metall. 38 (2), 120–130.

Wigley, D.A., 1971. Mechanical Properties of Materials at Low Temperature. Plenum Press, New York.

Wohlers, T., 2017. Wohlers Report 2017: 3D Printing and Additive Manufacturing State of the Industry Annual Worldwide Progress Report. Wohlers Associates, Fort Collins.

Wong, K.V., Hernandez, A., 2012. A Review of Additive Manufacturing. International Scholarly Research Network.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

Journal of Materials Processing Tech. 264 (2019) 200–210

Journal of Materials Processing Tech.

## Keywords

Binder jetting
Powder bed fusion
Microstructure
Electron beam powder bed fusion
Laser powder bed fusion
Inconel 625

## ABSTRACT

https://doi.org/10.1016/j.jmatprotec.2018.08.031
0924-0136/© 2018 Elsevier B.V. All rights reserved.

J.A. Gonzalez et al.

All as-fabricated cylindrical samples underwent post-fabrication hot isostatic pressing (HIPing) for 3 h at 1163^\circC \pm 3.5^\circC and 102 MPa \pm 1.72 MPa. Samples fabricated using EPBF and LPBF were cut from the start plate using a band saw before HIPing was performed. HIPed samples were then machined to required specifications.

ASTM International, 2014a. ASTM F_{3056}-14 Standard Specification for Additive Manufacturing Nickel Alloy (UNS N_{06625}) With Powder Bed Fusion. ASTM International, West Conshohocken, PA, USA.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

ELSEVIER

Contents lists available at ScienceDirect

journal homepage: www.elsevier.com/locate/jmatprotec

Keywords:
Binder jetting
Powder bed fusion
Microstructure
Electron beam powder bed fusion
Laser powder bed fusion
Inconel 625

A B S T R A C T

* Corresponding author.
E-mail address: maperez4@utep.edu (M.A. Perez).

https://doi.org/10.1016/j.jmatprotec.2018.08.031
Received 30 August 2017; Received in revised form 14 August 2018; Accepted 21 August 2018
Available online 23 August 2018
0924-0136/© 2018 Elsevier B.V. All rights reserved.

All as-fabricated cylindrical samples underwent post-fabrication hot isostatic pressing (HIPing) for 3 h at 1163°C ± 3.5°C and 102 MPa ± 1.72 MPa. Samples fabricated using EPBF and LPBF were cut from the start plate using a band saw before HIPing was performed. HIPed samples were then machined to required specifications.

ASTM International, 2014a. ASTM F3056-14 Standard Specification for Additive Manufacturing Nickel Alloy (UNS N06625) With Powder Bed Fusion. ASTM International, West Conshohocken, PA, USA.