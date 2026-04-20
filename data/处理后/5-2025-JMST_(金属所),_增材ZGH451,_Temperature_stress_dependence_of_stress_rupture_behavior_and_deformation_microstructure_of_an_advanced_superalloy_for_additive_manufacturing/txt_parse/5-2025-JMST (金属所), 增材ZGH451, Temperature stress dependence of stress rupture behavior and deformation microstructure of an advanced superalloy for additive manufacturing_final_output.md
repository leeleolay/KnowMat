DOI: 10.1016/j.jmst.2024.03.072

Research Article

# Temperature/stress dependence of stress rupture behavior and deformation microstructure of an advanced superalloy for additive manufacturing

Wei Song $ ^{a,b} $, Junying Yang $ ^{a,b} $, Jingjing Liang $ ^{a,*} $, Nannan Lu $ ^{a} $, Yizhou Zhou $ ^{a} $, Xiaofeng Sun $ ^{a} $, Jinguo Li $ ^{a,*} $

 $ ^{a} $ Shi-Changxu Innovation Center for Advanced Materials, Superalloys Division, Institute of Metal Research, Chinese Academy of Sciences Shenyang 110016, China

 $ ^{b} $ School of Materials Science and Engineering, University of Science and Technology of China, Shenyang 110016, China

## ARTICLE INFO

Article history:

Revised 27 March 2024

## Keywords

Additive manufacturing
Nickel-based superalloys
Stress rupture behavior
Microstructure evolution
Deformation mechanisms

## Abstract

© 2024 Published by Elsevier Ltd on behalf of The editorial office of Journal of Materials Science & Technology

## Abstract

A self-developed crack-free advanced superalloy ZGH451 fabricated by direct energy deposition (DED) was applied to investigate the microstructure evolution, stress rupture behavior, and deformation mechanisms at moderate-high temperatures and high-low stress conditions. The high Ta/Al ratio induces large misfit lattice stress and low stacking fault energy of alloy, resulting in approximate cubic  $ \gamma' $ phases in dendrites and the formation of initial dislocation tangles. After the stress rupture test at 760 ^\circC/780 MPa, high content cubic  $ \gamma' $ phases, small size of voids as well as preserved dislocation tangles are observed, showing stable structures with high-stress rupture resistance. High content and suitable size of cubic  $ \gamma' $ phases, initial dislocation tangles, and L-C locks hinder the dislocation motion, which decreases the minimum strain rate and prolongs life significantly, forming four stress rupture stages. Hence, the deformation mechanism is determined by dislocation piled-up on  $ \gamma/\gamma' $ interface, formation of stacking faults in  $ \gamma' $ phases, and dislocations shearing  $ \gamma' $ phases. However, the microstructure exhibits uneven structures composed of large sizes of rafted  $ \gamma' $ phases and voids at 980 ^\circC/260 MPa. The rafted structure and high temperature provide continuous channels and enough energy for dislocation motion, resulting in the increase of minimum strain rate, decline of life, and typical three stress rupture stages, even though there are obstacles to dislocation movement caused by dislocation networks. The deformation mechanism transforms to form dislocation networks on  $ \gamma/\gamma' $ interface and dislocations shearing  $ \gamma' $ phases. Besides, the decomposition of carbides on GBs also depends on temperature, which decomposes into harmful chain-like  $ M_{23}C_{6} $ carbides at moderate temperatures and reinforced granular-shaped  $ M_{6}C $ carbides at high temperatures. The applied stress always decreases mechanical properties due to its degradation of microstructure induced by elongating the precipitates and defects.

## 1. Introduction

Nickel-based superalloys are widely used to prepare turbine blades and disks in advanced aircraft engines, attributed to their excellent performance at medium or high temperatures and operational reliability [1–4]. To further improve fuel efficiency and reduce carbon emissions, the turbine inlet temperature of advanced aero-engines is increasing, which also puts forward more complex structures for the novel integrated parts and higher requirements for the conventional manufacturing industry. The conventional preparation processes such as casting, powder metallurgy, and form wrought stock lack the ability to make complicated components due to their complex preparation steps, wasting stuff, and insufficient precision, limiting the further development of superalloys. Additive manufacturing (AM) is an emerging preparation technology that realizes the near-net shape through computer control based on the three-dimensional graphics parts, showing higher precision and flexibility in manufacturing complex geometry components and presenting great advantages in terms of cost and energy/materials savings [5–8]. Up to the present, many fruitful researches about AM-ed superalloys focusing on process optimization [9,10], microstructure characterization [11–13], and mechanical properties [14–18] have been carried out. Among various properties, the creep and stress rupture properties are

especially important for superalloys as they are usually exposed to high-temperature/stress conditions for a long period and thus fail through creep-induced microstructural damage [19,20].

Various additive manufacturing approaches have been explored to produce Ni-based superalloys, such as direct energy deposition (DED) [21–23], selective laser melting (SLM) [24–26], and selective electron-beam melting (SEBM) [27,28]. Since their different preparation methods and physical metallurgy features, the microstructure and mechanical properties are not identical to each other. The parts fabricated by SLM are typically characterized by fine microstructures which are facilitated by high cooling rates ( $ 10^{5} $– $ 10^{7} $ K/s), enhancing their mechanical properties at room temperature [29,30]. However, due to the weakening effect of a large density of grain boundaries at elevated temperatures, these parts with high precision normally show reduced medium to high-temperature strengths compared with their coarse-grained or single-crystal counterparts. The SEBM process has low cooling rates ( $ 10^{2} $– $ 10^{3} $ K/s) and large laser beam diameter which is conducive to forming coarse columnar grains in parts, while the parts show high surface roughness and precision limit [31–33]. In comparison, the DED is readily capable of producing materials of near-full densification and high-precision as well as coarse columnar microstructure due to its moderate cooling rates ( $ 10^{3} $– $ 10^{5} $ K/s) and laser beam diameter, potentially beneficial to their high-temperature strengths and creep resistance [34,35].

Many researchers have been conducted so far to investigate the microstructure and stress rupture properties of the AM-ed superalloys. Zhang et al. [36] suggested that the fine grains in IN718 fabricated by SLM underwent much more serious plastic deformation to accommodate heterogeneous strain from surrounding coarse grains, resulting in a high-risk area of the initiation and propagation of cracks and worse stress rupture properties under 690 MPa at 650 ^\circC. Pasiowiec et al. [37] suggested the evenly distributed  $ \delta $ particles enhanced the creep life of IN625 additively manufactured by SLM at the temperature range 700–800 ^\circC. Probstle et al. [38] implied the higher amount of strengthening precipitates and the lack of  $ \delta $ phases in LPBF-ed IN718, leading to longer creep life compared with conventionally cast and wrought alloys. Kalyanasundaram et al. [39] introduced the creep-rupture response of CM247LC alloy fabricated by SLM at 800 ^\circC and 500–650 MPa and attributed the reduction in both strength and ductility to microcrack development aided by matrix-agglomerated carbide decohesion. However, present studies are concentrated on the alloys with lower content of high-temperature strengthening  $ \gamma' $ phase and stress rupture properties at medium-low temperatures. There are few reports on the high-performance superalloys with high  $ \gamma' $ content. C. Kørner et al. [40] have successfully fabricated large-sized CMSX-4 samples by SEBM and investigated the creep properties of as-built at 850 ^\circC /600 MPa. The additively manufactured superalloys have a little larger creep life than conventional cast. Ci et al. [41] observed a gradual eutectic increase during deposition in DD32 single crystal Ni-base superalloy repaired by DED, leading to cracking and reduced stress rupture properties in the heat-affected zone (HAZ). Overall, related research on microstructure evolution and deformation mechanism of AM-superalloy after stress rupture tests was insufficient and controversial, especially under high temperatures (up to 1000 ^\circC) and for the advanced superalloys containing high  $ \gamma' $ content fabricated by DED. Generally, the relationships among microstructure, stress rupture behavior, and deformation mechanism are essentially correlated with grain crystallographic orientation, grain size, boundary configuration, defects, composition segregation, precipitation (such as size, shape, and distribution of  $ \gamma' $ phases and carbides), and any evolutions during stress rupture of the materials [42–44]. These unique structures and precipitate characteristics in DED-ed advanced superalloys govern the overall stress rupture damage kinetics and mechanisms involving the processes of vacancy diffusion, microstructure coarsening, the interaction of crystal defects (such as dislocation glide-climb and tangles, formation of stacking faults or dislocation networks), and/or grain boundary sliding [45,46].

This work presents a systematic study on the medium & high-temperature stress rupture behavior (at 760 ^\circC/780 MPa and 980 ^\circC/260 MPa) of a self-developed crack-free superalloy ZGH451 with high content of  $ \gamma' $ phase fabricated by DED, with a particular focus on the understanding of the response of microstructure, defects, and stress rupture properties to temperature/stress. The initial microstructure and crystallographic texture as well as the microstructure evolution and corresponding deformation mechanism after stress rupture tests are studied in detail using a range of techniques. It is worth emphasizing that the present work offers an improved understanding of the high-temperature stress rupture behavior and mechanism of DED-manufactured advanced precipitation strengthening Ni-based superalloy, which is important for its high-temperature practical applications.

## 2. Materials and methods

## 2.1. Experimental materials

The spherical ZGH451 superalloy powder was prepared by argon gas atomization, of which the D50 is about 92.94  $ \mu $m as shown in Fig. 1(a, b). The powders have few defects with excellent sphericity of 90 %, flowability of 16.81 s/50 g, and tap density of g/cm $ ^{3} $. The chemical composition of the powder shown in Table 1 was measured by inductively coupled plasma-optical emission spectroscopy (ICP-OES) and ICP-combustion analysis. Before the experiment, the powders were dried in a vacuum drying oven
Fig. 1. Microstructural characteristics of ZGH451 powders and process of DED: (a) SEM morphology of powders; (b) size distribution of powders; (c) schematic diagram of the additive manufacturing process.

Table 1 Alloy composition for the current study in wt.% (Ni-base), measured using ICP-OES, ICP-combustion (carbon), and Spark OES (boron).

| Alloy | Co+Cr+W+Mo | Al | Ti | Ta | C | B | Ni | Ta/Al ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ZGH451 | 28 | 4.30 | 1.22 | 5.60 | 0.01 | 0.03 | Bal | 1.30 |

at a temperature of 120 ^\circC for 6 h. The substrate prepared by vacuum melting furnace with the same composition as powders was employed with dimensions of 30 mm \times 30 mm \times 20 mm. The substrate surface was polished using sandpaper and cleaned with acetone to remove oil and oxide layers.

A  $ CO_{2} $ laser deposition machine assembled by the Institute of Metal Research, Chinese Academy of Sciences was used for printing. The machine has a coaxial powder delivery system with argon protection and a pulsed laser of about 2.0 mm beam diameter. Lots of processing parameter ranges were optimized including laser power from 1300 to 2000 W, scanning speed from 900 to 1500 mm/min, and powder feeding rate from 8 to 11 g/min. The optimal process parameters determined in this work are laser power 1800 W, powder feeding rate 10.5 g/min, scanning speed 1100 mm/min, laser beam diameter 2.0 mm, beam-on time 0.16 s, and beam-off time 0.4–0.6 s. The schematic illustration of the scan strategy is shown in Fig. 1(c). The laser moves in a straight line in each cladding layer and is rotated 90^\circ compared to the motion direction of the previous layer, with the powder-feeding head raised by one layer. Before printing, the laser will scan on the substrate surface three times without powder-feeding to preheat the substrate to diminish the temperature gradient.

## 2.2. The laser-directed energy deposition (DED) process parameters

## 2.3. Microstructure characterization

The microstructures were characterized by a Zeiss optical microscope (OM) and Thermo Scientific Apreo 2 field emission gun scanning electron microscope (FEG-SEM) on longitudinal sections (parallel to the build direction) of DED specimens sectioned from the deposited bulk (20 mm \times 20 mm \times 60 mm). Samples were chemically etched in a solution of  $ CuCl_{2} $ (50 g) + HCl (100 mL) +  $ C_{2}H_{5}OH $ (100 mL) for 20 s or electrolytically etched using 30 % phosphoric acid at 8 V direct current for 5 s, which etches away the  $ \gamma' $ phase or  $ \gamma $ matrix, respectively and highlights the unetched areas. Furthermore, samples after vibration polishing were investigated by a Symmetry S_{2} electron backscattered diffraction (EBSD) system to characterize crystal orientation (included in-verse pole figure (IPF) and pole figure maps), texture, geometrically necessary dislocation (GND) distribution, and grain size in the as-printed microstructures. X-ray computed tomography (XCT) was used to investigate the three-dimensional (3D) distribution of the micro-voids in the initial as-built samples, including size, morphology, and content. All the XCT samples were cylinders with a diameter of 3 mm and length of 5 mm, cut using a wire electrical discharge machine (WEDM) at the middle position of the deposited bulk. The effective detection length of the XCT was 2 mm. The rotation step size and total voxel of the XCT are 1^\circ and 1,342,926.2, respectively. The transmission electron microscope (TEM) specimens were sectioned 5 mm away from the stress rupture fracture surface on the gauge section. These specimens were mechanically ground to about 50  $ \mu $m in thickness and electrochemically polished by a twin jet polisher at the temperature of -27 ^\circC and voltage of 22 V in a perchloric acid and ethanol solution. Moreover, the ImageJ Pro-software was then used for measuring the size (length or width) and Per Area (Obj./Total: the ratio of the area of the objective to total) of precipitates, examining at least five pictures. The  $ \gamma' $ content was approximately replaced with Obj./Total, regarded as area percent or volume fraction.

## 2.4. Assessment of mechanical behavior

The stress rupture tests were carried out until fractured on the F-25 creep machine at 760 ^\circC/780 MPa and 980 ^\circC/260 MPa,

Table 2 The parameters of stress rupture tests of experimental alloy ZGH451.

| Temperature (^\circC) | Stress (MPa) | Gauge length (mm) | Gauge diameter (mm) | Length (mm) |
| --- | --- | --- | --- | --- |
| 760 | 780 | 20 | 3 | 47 |
| 980 | 260 | 20 | 3 | 47 |

respectively, for estimating the mechanical properties of the as-fabricated alloy. For each condition, three identical samples were tested and investigated using the average results. The tested specimens were sectioned parallel to the building direction from the deposited bulks. The size of the tested specimens was the M6 $ \phi $3 cylindrical shape bars with a gauge length and diameter of 20 mm and 3 mm, thread segment diameter of 6 mm, and total length of 47 mm (listed in Table 2). The surface of the specimens was polished clean and smooth. All tests were conducted under an atmospheric environment and the uniaxial loading was applied along the build direction. Besides, the extensometer was used to measure the strain during the whole stress rupture life to present related curves.

## 3. Results

## 3.1. Observation of as-built microstructure and defects

Fig. 2 shows the overall viewing (observation direction parallels the building direction) of microstructures of as-built alloy ZGH451 obtained by SEM and TEM. The samples are sectioned at the middle of bars about 20 cm from the bottom and the top to avoid the influence of the DED process on experimental analysis. It is noticeable that the as-built microstructure is constituted by typical coarse columnar grains that grow along the build direction (Fig. 2(a, b)). The fusion lines are smooth and pass through several grains, indicating large molten pools with a high width-depth ratio. Besides, there are lots of epitaxial growth of dendrites perpendicular to the fusion line, and little tilting dendrites parallel to the direction of scanning speed.

Based on the enlarged pictures of the interior of grains, the dendrite core (DC), interdendritic region (IR), primary dendrite arms, carbides, and  $ \gamma' $ phase can be distinguished clearly (Fig. 2(c, d)). Typical MC-type carbides are fine and distributed in DC, IR, and grain boundaries (GBs). Due to the inherent heat treatment, tiny  $ \gamma' $ phases with low cubicity precipitated in the DC and IR, accompanied by a gradual increase in size. Furthermore, Fig. 2(e) exhibits the TEM images of the initial microstructures, it is obvious that the size of  $ \gamma' $ phases in DC is smaller than those in IR due to the segregation of  $ \gamma' $ forming elements [47]. Herein, the boundaries of DC, IR, and transition region are decided on the average size of  $ \gamma' $ phases. In the DC, the average size of  $ \gamma' $ phases is 124.10 nm. In the transition region (between the brown and red lines marked in Fig. 2(d, e)), the average size of  $ \gamma' $ phases has a significant increase, which is 135.6 nm. The width of the transition region is about 200–300 nm, which is about the width of two  $ \gamma' $ precipitates. In the IR, the average size of  $ \gamma' $ phases is 150.50 nm. Hence, the size of  $ \gamma' $ phases changes with various regions and increases from DC to IR.

Moreover, several initial dislocation tangles are also observed in  $ \gamma'/\gamma $ interface and GBs. Since alloy ZGH451 has excellent crack-resistance, no cracks are shown in all microstructures. There are only some void defects formed by gas or lack of powder fusion observed in IR. The former voids are usually induced by shielding gas or metallic vapor escaping and present tiny and regular spheres. The latter can induce irregular voids with unmelted powder. Three-dimensional features of voids obtained by XCT are shown in Fig. 3, which presents the distribution, size, and content of voids intu-
Fig. 2. Overall inspection and analysis of as-built microstructures observed parallel to building direction: (a, b) SEM morphologies of typical columnar grains structures; (c, d) SEM morphologies of dendrites, including DC, IR, tiny  $ \gamma' $ phase and MC carbides; (e) TEM morphologies of DC, IR, tiny  $ \gamma' $ phase and initial dislocations.

Table 3 Several important characteristic parameters of as-built ZGH451 fabricated by DED such as PDAS, size of voids and  $ \gamma'/\gamma $ phases in DC/IR, volume fraction of  $ \gamma' $ in alloy.

| Average size of  $ \gamma' $ in DC/IR (nm) | Average volume fraction of  $ \gamma' $ in alloy (%) | Average size of  $ \gamma $ in DC/IR (nm) | PDAS ( $ \mu $m) | Average size of voids ( $ \mu $m) | Volume fraction of voids (%) |
| --- | --- | --- | --- | --- | --- |
| 124.10/150.50 | 50.52 | 40.31/75.42 | 17.43 | 9.59 | 0.10 |

itively. Both types of voids are rare and minor, indicating a high density of samples.

Finally, several critical characteristic microstructure parameters are examined quantitatively, such as primary dendrite arm spacing (PDAS), size of  $ \gamma' $ phase in DC/IR and its average volume fraction in alloy as well as voids characteristic (listed in Table 3 detailed). The various structures and multi-scale of AM-ed alloy ZGH451 will induce a unique influence on stress rupture properties compared to cast or forged superalloys.

## 3.2. Texture characteristics

Fig. 4 illustrates the EBSD information of the as-built sample. The epitaxial growth of dendrites perpendicular to the fusion lines brings the approximate growth direction of columnar grains (Fig. 4(a)), forming the strong texture along the BD. Based on the results from EBSD scans (covering an area of 3 mm²) located in the middle of alloy bulk, the inverse pole figure (IPF) maps of the longitudinal section (parallel to BD) demonstrate that the preferred
Fig. 3. Three-dimensional features of the micro-voids in an as-built sample obtained by X-ray computed tomography (XCT): (a) actual measurement region; (b, b₁) mean diameter distribution of micro-voids and local magnified area in the image; (c) distributing location and volume of micro-voids.

orientation is {100} along with the building direction (Fig. 4(b)). There are only 9 coarse columnar grains with high aspect ratios observed (misorientation between grains > 10^\circ) in alloy ZGH451, whose average grain size is 395.4  $ \mu $m (Fig. 4(c)), much greater than those of selective laser melting samples [48,49]. The pole figure maps in Fig. 4(e) further demonstrate that the alloy has the strongest {1 0 0} texture component based on the texture strength that plane family {1 0 0} is higher than plane families {1 1 0} and {1 1 1}, which is consistent with IPF results.

The distribution of GND density is shown in Fig. 4(d). Noticeably, the grain boundaries, subgrain boundaries, and IR contain prominent GND accumulation, especially at the high-angle grain boundary (HAGB). It is known that the GND density reflects stress situations regarding the dislocation accumulations [50]. The initial dislocation tangles at  $ \gamma'/\gamma $ interface located in IR and GBs are well demonstrated above GND characteristics (Fig. 2(e)). Statistics indicate that the value of GND density is about  $ 0.25 \times 10^{14} \, m^{-2} $. The low GND density may be attributed to a low cooling rate (compared to selective laser melting (SLM)), a flat molten pool, and the preferential fiber texture constituted by large grains. On the one hand, the low cooling rate leaves a small mechanical driving force and the flat molten pool can simultaneously relieve residual stress, alleviating the dislocation tangles (Fig. 2(e)). On the other hand, the large grains reduce the number of grain boundaries, namely the GND regions, and they can allow sizeable thermal expansion along [0 0 1]. Based on the above EBSD results, alloy ZGH451 has stable structures of columnar grains with [0 0 1] orientation and relatively low GND density, which could exclude the influence of the DED process on subsequent experimental results and influence the stress rupture properties.

## 3.3. Stress rupture behavior

Fig. 5 illustrates the stress rupture curves of alloy ZGH451 under the conditions of 760 ^\circC/780 MPa and 980 ^\circC/260 MPa. Based on the curves, the stress rupture behavior can be summed up as follows: (I) It is noticeable that the stress rupture lives decrease with the increase of testing temperatures (Fig. 5(a)), which are

Table 4 The time for different stress rupture stages and their percentage in the whole stress rupture life, and the minimum stress rupture rate under two experimental conditions.

| Experimental condition | $ t_{0}^{a} $ (h) | $ t_{1}^{a} $ (h) | $ t_{2}^{a} $ (h) | $ t_{3}^{a} $ (h) | $ t_{4}^{a} $ (h) | $ \varepsilon \bullet_{\text{min}} $ ( $ s^{-1} $) |
| --- | --- | --- | --- | --- | --- | --- |
| 760 ^\circC/780 MPa | 3.11 | 6.52 | 112.22 | 12.35 | 134.20 | 1.78  $ \times $ 10 $ ^{-5} $ |
| 980 ^\circC/260 MPa | 0 | 2.96 | 16.14 | 7.80 | 26.90 | 2.08  $ \times $ 10 $ ^{-4} $ |

 $ ^{a} $  $ t_{0} $,  $ t_{1} $,  $ t_{2} $,  $ t_{3} $, and  $ t_{4} $ represent the time span of the incubation period, primary, secondary, and tertiary stress rupture stages, and stress rupture life.

134.20. and 26.90 h of the two conditions respectively (listed in Table 4). Herein, due to the high similarity between creep and stress rupture, the stress rupture process could also be divided into different stages via the change of stress rupture strain rate, which are the incubation period, primary stage, secondary stage, and tertiary stage. At 760 ^\circC/780 MPa, the alloy shows four stages, which have an incubation period of about 3.11 h accompanied by a stress rupture strain rate decreasing first and then increasing within a small strain range (Fig. 5(b–d)). However, there are only typical three stages after fracture under 980 ^\circC/260 MPa, i.e., primary stage, secondary stage, and tertiary stage, with no occurrence of an incubation period observed. The detailed time of each stage is shown in Table 4. (II) The life of secondary stage is the important stage that represents the stress rupture performance level of the alloy due to it occupies a large part of the whole stress rupture life, which is 83.6 % and 60 % based on the ratio of time, respectively. The secondary stages begin with the stress rupture strain of (9.31\pm0.05)% and (3.17\pm0.03)% (Fig. 5(a, d)) at the above two conditions. When the stress rupture strain reaches about (17.94\pm0.05)% and (9.45\pm0.03)% it gets into the tertiary stage and fractures within 12.35 or 7.80 h, respectively. (III) According to the strain rate-strain and strain rate-time curves (Fig. 5(c, d)), the stress rupture strain rate increases firstly, then decreases and stabilizes at the minimum strain rate, and finally increases rapidly until fractured during the testing at 760 ^\circC/780 MPa. However, for the testing at 980 ^\circC/260 MPa, the stress rupture strain rate is reduced to the minimum strain rate directly, and stables
Fig. 4. SEM, EBSD-IPF (Y-axis), GND density, grain size distribution and pole figure maps of as-built sample: (a) SEM images of columnar grains; (b) IPF along building direction; (c) the distribution of grain size; (d) the distribution of GND density; (e) texture strength of  $ \{1\ 0\ 0\} $,  $ \{1\ 1\ 0\} $ and  $ \{1\ 1\ 1\} $ poles.

at the minimum strain rate for a short time, and then the alloy fractures rapidly. Besides, the average minimum strain rate under 980 ^\circC/260 MPa is much higher than that of 760 ^\circC/780 MPa, which are 2.08 \times 10⁻⁴/s and 1.78 \times 10⁻⁵/s, respectively.

Herein, due to the slight shaking of the external extensometer, the record of strain is unstable, hence, the minimum stain rate exhibits a range of  $ 1.15 \times 10^{-4}-3.33 \times 10^{-5} $ /s for 760 ^\circC/780 MPa and  $ 2.77 \times 10^{-4}-1.38 \times 10^{-4} $ /s for 980 ^\circC/260 MPa.

## 3.4. Fracture morphology

Fig. 6 exhibits the macro-morphology of stress rupture fracture surfaces after testing at 760 ^\circC/780 MPa. It is obvious that the fracture surface contains two regions, one has smooth cleavage planes with large areas showing typical brittleness fracture features; another one shows uneven surfaces with some dimples exhibiting ductile fracture characteristics. Hence, the fracture mode is a mixed fracture with some plasticity, which is consistent with the strain in Fig. 5. Moreover, some voids can also be observed on the fracture surfaces, which are formed by the formation of vacancies or extension of initial voids, influenced by temperature and stress.

To further confirm the source of failure at 760 ^\circC/780 MPa, the crack initiation and propagation were investigated by the longitudinal section microstructures near fracture obtained by SEM (Fig. 7). Based on the 2D projection of the fracture surface, the fracture is composed of straight and twisted lines (corresponding yellow and red lines in Fig. 7(a)), which represents the brittleness fracture and ductile fracture, respectively. The cracks are usually observed along grain boundaries but rarely emerge in grains (Fig. 7(b)). There are lots of voids in IR or located on GBs, which are deformed along the applied external force direction. The
Fig. 5. Stress rupture curves of alloy ZGH451 under two testing conditions. (a) overall stress rupture curves; (b) enlarged stress rupture curves; (c) stress rupture strain rate-stress rupture strain curve; (d) stress rupture strain rate-stress rupture time curve.

content and size of them are higher than those of the as-built state due to the long-term effect of temperature and stress, which are 1.09% and 10.91  $ \mu $m. Also, some large voids can become the initiation of cracks, or the voids located on GBs break their integrity, promoting the propagation of cracks. In the grains, a large number of cubical  $ \gamma' $ phases can be observed in DC and IR. Due to the segregation of  $ \gamma' $ forming elements in IR, the size of  $ \gamma' $ is significantly larger than that of in DC (Fig. 7(c, d)). Besides, there are also some chain-like carbides enriched with Cr and Mo elements that occurred on GBs (Fig. 7(e)). In fact, the shape chain-like is composed of the continuous distribution of carbides with an average size of 620 nm (equivalent length) formed by the decomposition of initial carbides, leaving some voids and consuming alloy elements, which will be discussed in Section 4.1. This kind of continuous chain-like shape enhances the brittleness of carbides and GBs, weakening their coherence and inducing the formation of cracks. Hence, the microstructural evolution has a direct influence on the stress rupture resistance of alloy ZGH451 under 760 ^\circC/780 MPa, including the characteristics of dendrites, voids, cracks, GBs,  $ \gamma' $ phase, and carbides.

Fig. 8 exhibits the macro-morphology of fracture surfaces after testing at 980 ^\circC/260 MPa. The fracture surface exhibits a single deformation region, namely, composed of uneven surfaces with lots of dimples, exhibiting ductile fracture characteristics. The cleavage planes are much smaller than those at 760 ^\circC/780 MPa. Hence, the fracture mode is typical micro-void aggregation fracture with some obvious necking. Moreover, the high temperature further promotes the formation and motion of vacancies, inducing some large-sized voids that occur on the fracture surfaces.

The longitudinal-section microstructures near the stress-ruptured surface of alloy ZGH451 at 980 ^\circC and 260 MPa are also examined to determine the location of crack initiation (Fig. 9). The fracture is only composed by twisted lines (corresponding red lines in Fig. 9(a)), showing typical ductile fracture. The cracks are mostly located or initiated near lots of voids in the IR of grains (Fig. 9(b)) and terminated on DC (marked as red circles in Fig. 9(c)). The content and size of voids, which are 2.91 % and 16.43 \mum, respectively, are greater than those of as-built and 760 ^\circC/780 MPa state due to higher temperature. The voids can be categorized into two groups: One type of them exhibits specific crystallographic characteristics with regular shape originating from the gradual accumulation and continuously growing along a specific crystallographic plane of high concentration vacancies, which is polyhedral-shaped consisting of an octahedron faced by {111} planes or a dodecahedron faced by {111} and {001} planes (as marked I in yellow rectangle in Fig. 9(c)). Another type is formed by the evolution of initial voids in the IR (as marked II in the blue circle in Fig. 9(c)). In the grains, plentiful rafted \gamma′ phases can be observed in DC and IR. Due to the higher temperature and segregation of \gamma′ forming elements in IR, the rafted structures are significantly coarser and uneven than those in DC (Fig. 9(d)). Moreover, there are also some carbides with an average size of 450 nm (equivalent length) occurring on GBs while they are enriched Mo and W elements.
Fig. 6. Morphologies of the stress-ruptured surface of alloy ZGH451 at 760 ^\circC and 780 MPa: (a) overall fracture morphology; (b–d) magnified local morphologies.
Fig. 7. The longitudinal-section microstructures near the stress-ruptured surface of alloy ZGH451 at 760 ^\circC and 780 MPa: (a–d) SEM images of overall fracture and its nearby microstructures; (e) SEM image of carbide on GBs and its EDS mapping of the distribution of elements.

(Fig. 9(e)), and exhibit a discontinuous distribution of blocks. The change of decomposition of initial carbides induces the difference in shape, size, and distribution of carbides between two testing conditions. This nanometer and discontinuous block shape enhance the strength of GBs and limit their motion, avoiding becoming a crack source. Hence, the microstructural evolution of  $ \gamma' $ rafting, voids and cracks extending and carbides characteristics influences the stress rupture properties of the alloy under 980 ^\circC/260 MPa, bringing different stress rupture behavior between the two conditions.
Fig. 8. Morphologies of the stress-ruptured surface of alloy ZGH451 at 980 ^\circC and 260 MPa: (a) overall fracture morphology; (b–d) magnified local morphologies.

## 4. Discussions

## 4.1. Evolution of microstructure and defects

The microstructures are mainly composed of dendrites,  $ \gamma/\gamma' $ phases and carbides, while the defects consist of voids and cracks. They are all changed in different degrees after two stress rupture tests compared to initial states. The primary dendrite arm spacing (PDAS) is a considerable characterization of the dendrite structures. According to the Kurz-Fisher (KF) model, the PDAS can be described as the following formula [51]:

 $$ \lambda_{1}=4.3\left(D_{\mathrm{L}}\Gamma\Delta T_{0}/k\right)^{1/4}G^{-1/2}V^{-1/4} $$ 

 $$ k=1-\Delta T_{0}/T_{\mathrm{m}}-T_{\mathrm{S}} $$ 

where  $ D_{L} $ is the diffusion coefficient of liquid, which is mainly related to the alloy compositions,  $ \Gamma $ is the Gibbs-Thomson coefficient,  $ \Delta T_{0} $ is the crystallization interval, k is the equivalent solute segregation coefficient, which is related to the solidus and liquidus temperatures, G is the temperature gradient, V is the crystal growth rate,  $ T_{S} $ is the liquidus temperature,  $ T_{m} $ is the melting point of pure Ni. The DED is well-known as a rapid solidification process with a cooling rate of  $ 10^{3}-10^{5} $ K/s, resulting in a partial large temperature gradient G during printing. Besides, the element Ta has a large atomic size with a low diffusion coefficient, lowering the effective diffusivity ( $ D_{eff} $) of alloy and weakening the diffusion ability of elements [52], namely, the decline of  $ D_{L} $. The other parameters are mainly related to the alloy itself, which is unchanged. Hence, a high-temperature gradient and cooling rate can inhibit the nucleation of dendrites and shorten the time of element diffusion at the solid-liquid front while the low diffusion coefficient further limits the element supplement for the growth of dendrites. Hence, based on Eq. (1), the finer PDAS  $ \lambda_{1} $ (17.43  $ \mu $m) of the AM process compared to that of traditional casting (30–50  $ \mu $m) [53–56] demonstrates it reasonable and unique once more. Small dendrite spacing can obtain fine dendrite structures and reduce the segregation of the alloying elements, which can improve the mechanical properties of superalloys. After stress rupture testing, the dendrite structures became increasingly difficult to observe and almost disappeared (Figs. 7 and 9). There are only some composition segregation regions with an average width of 6.1  $ \mu $m at 760 ^\circC/780 MPa and 10.3  $ \mu $m at 980 ^\circC/260 MPa, respectively, which are both smaller than the PDAS and attributed to the element homogenization induced by long-term thermal exposure at mid-and-high temperature.

It is universally known that the  $ \gamma' $ particles precipitate from the  $ \gamma $ matrix and they have similar FCC crystal structure, exhibiting a coherent interface. The morphology of the  $ \gamma' $ phases is the result of competition between the interfacial energy and elastic strain energy, concerned with the interfacial shape and the magnitude of the  $ \gamma/\gamma' $ lattice misfit [57]. When the interfacial energy is larger than the elastic strain energy, to release the interfacial energy, the particles will be shown as sphericity due to their minimum surface area with the same volume. By contrast, the particles will be shown as cubes due to the crystalline anisotropy and lowest elastic modulus. At the as-built state, due to the rapid solidification process and short time of inherent heat treatment, the precipitation of  $ \gamma' $ phases is limited, showing a small size. The tiny  $ \gamma' $ phases have high interfacial energy and the elastic strain energy on  $ \gamma/\gamma' $ interface lacks time to adjust their shape. Therefore, the initial  $ \gamma' $ phase exhibits approximate cubic with circular corners and has an average volume fraction of 50.52% (Fig. 2).

After testing at 760 ^\circC/780 MPa, the supersaturated solid solution of  $ \gamma $ induced by the AM process and long-term (134.20 h) thermal exposure of 760 ^\circC provide high precipitation force and
Fig. 9. The longitudinal-section microstructures near the stress-ruptured surface of alloy ZGH451 at 980 ^\circC and 260 MPa: (a–d) SEM images of overall fracture and its nearby microstructures; (e) SEM image of carbide on GBs and its EDS mapping of the distribution of elements.

Several important characteristic parameters of as-built ZGH451 after stress rupture tests.

| Testing conditions | Average size of  $ \gamma' $ in DC/IR (nm) | Volume fraction of  $ \gamma' $ (%) | Average size of  $ \gamma $ in DC/IR (nm) |
| --- | --- | --- | --- |
| 760 ^\circC/780 MPa | 220.45/279.65 | 56.85 | 100.85/135.49 |
| 980 ^\circC/260 MPa | 362.38/423.08 | 62.55 | 320.86/420.06 |

adequate time for plenty of  $ \gamma' $ phases precipitation and growing up, respectively. The  $ \gamma' $ phases have a high volume fraction of 56.85 % and an average size of 220.45 nm/279.65 nm (listed in Table 5). At this moment, the morphology of  $ \gamma' $ phase is determined by integral elastic strain energy on  $ \gamma/\gamma' $ interface. It presumes that the  $ \gamma $ matrix is elastically isotropic, and the elastic modulus of the  $ \gamma $ matrix is the same as the  $ \gamma' $ phase. The integral elastic strain energy  $ \Delta G_{s} $ is defined as [58]:

 $$ \Delta G_{s}\propto\mu\delta^{2}V $$ 

where  $ \mu $ is the shear modulus of the matrix, which is a constant.  $ \delta $ is the  $ \gamma/\gamma' $ lattice misfit and V is the volume of  $ \gamma' $ particle. Obviously,  $ \Delta G_s $ is proportional to the  $ \gamma/\gamma' $ lattice misfit and the volume of  $ \gamma' $ particle. The initial dislocation tangles on  $ \gamma/\gamma' $ interface and low cubicity  $ \gamma' $ phase fully prove that the alloy has a relatively high lattice misfit. Moreover, it is well-known that Ta has a large atomic radius, which can also induce large lattice distortion of  $ \gamma' $ phase after the substitution of Ni [59]. Hence, the alloy has sufficient elastic strain energy  $ \Delta G_s $ on  $ \gamma/\gamma' $ interface, making the shape of  $ \gamma' $ phases cubic (Fig. 7). Meanwhile, applied high stress makes the cubic  $ \gamma' $ phases slightly elongated along the loading direction. With the increase of testing temperature, it can be seen that the original approximate cubic  $ \gamma' $ phase turns to directional coarsening, which is mostly normal to applied stress direction, namely, the N-type coarsening. According to the LSW theory [60], the coarsening is determined by elements diffusion coefficient and interface energy. During testing of 980 ^\circC/260 MPa, high temperature induces a large diffusion coefficient of elements diffusion coefficient, providing composition conditions timely for the precipitation and coarsening of  $ \gamma' $ phases. The increasingly interfacial energy of alloy provides plenty of power for the transformation of  $ \gamma' $ phase shape [61,62]. Therefore, the rafted  $ \gamma' $ phase emerges in the deformed microstructure under the combined action of high temperature, long testing time, large diffusion coefficient, and high interfacial energy. The average size and volume fraction of  $ \gamma' $ phase is 362.38 nm/423.08 nm (width direction) and 62.55 % (listed in Table 5), which are both larger than those of 760 ^\circC/780 MPa. Moreover, the  $ \gamma $ matrix is also increasingly coarsening after both tests (listed in Table 5).

For the evolution of carbides, at an as-built state, due to the low content of C element (0.03 wt.%) and inhibition of element segregation induced by the AM process, the common MC-type carbides enriched Ti and Ta [63] only emerge on GBs, where the elements are easily to accumulate. After testing at different temperatures, carbides undergo different decomposition modes, which is shown as follows [64]:

 $$ \mathrm{MC}+\gamma\rightarrow\mathrm{M}_{6}\mathrm{CorM}_{23}\mathrm{C}_{6}+\gamma^{\prime} $$ 

After a long test time at 760 ^\circC/780 MPa, the carbides have enough time to provide the carbon diffusion and react to form  $ M_{23}C_{6} $ carbides preferentially due to their relatively low precipitation temperatures (650 ^\circC) [65]. However, the long time and temperature also make the  $ M_{23}C_{6} $ carbides [66] grow, showing continuous distribution with large size on GBs, namely, chain-like. This kind of morphology highlights the hard and brittle carbides, making them a source of cracks. Besides, the large size of  $ M_{23}C_{6} $ carbides can not be enveloped within layers of  $ \gamma' $ phase completely, leaving voids with their surrounding  $ \gamma' $ phases (Fig. 7(e)). Therefore, the capability of  $ M_{23}C_{6} $ carbides inhibiting grain boundary sliding and crack propagation is weakened, forming local intergranular fracture. In contrast, at 980 ^\circC/260 MPa, the initial carbides mainly decompose into typical  $ M_{6}C $ carbides enriched Mo and W, which precipitate at higher temperatures (870 ^\circC). Due to the relatively short time of stress rupture life, the  $ M_{6}C $ carbides grow up insufficiently even at high temperatures, showing a shape of discontinuous fine granular (Fig. 9(e)). The granular-shaped  $ M_{6}C $ carbides can be enveloped by  $ \gamma' $ phase with better coherence.

between each other, which stables the structure and avoids the formation of voids on GBs. Hence, the GBs are pinned by carbides and still have enough strength at high temperatures, preventing the motion of GBs and the formation of cracks. Based on the previous reports [67–69], it is believed that the granular-shaped carbides can improve the mechanical properties but the brittle plate-like or needle-like phases usually promote crack propagation and are detrimental to stress-rupture or creep properties.

The initial void defects are mainly formed by gas entrapped into the molten pool or lack of powder fusion. The former voids are usually induced by shielding gas or metallic vapor escaping and present tiny and regular spheres. Lack of powder fusion can induce irregular pores with unmelted powder, attributed to slight process variations during deposition. Under the action of temperature and stress, voids are deformed and grow along the loading direction while cracks initiate and propagate near them. At 760 ^\circC/780 MPa, the increase in the number of voids disrupts the integrity of GBs, leading to crack initiation and propagation, and damaging the alloy's performance. However, in grains, the voids are small due to their low driving force of aggregate growth and there are lots of cubic \gamma′ phases with suitable size (200–400 nm), effectively limiting the formation and propagation of cracks. With the increase in temperature, due to the significant mutual aggregation of initial voids and vacancies, as well as the combined effect of external stress, their size and content significantly increase in IR. Cracks form in large numbers along the voids, and their ability to impede crack propagation becomes poorer due to the structures rafting, resulting in significant increase in crack size, seriously damaging the alloy properties. In a word, the evolution of size, shape, and distribution of phases and structures can influence the stress rupture properties.

4.2. Deformation mechanism under medium temperature and high stress (760 ^\circC/780 MPa)

Fig. 10 displays the TEM images near stress rupture fracture at the condition of 760 ^\circC/780 MPa. The deformation mechanism is mainly concerned with the dislocation piled-up (marked in red circle in Fig. 10(a)) on  $ \gamma/\gamma' $ interface, formation of stacking faults (SFs marked in yellow circle in Fig. 10(b)) in  $ \gamma' $ phases, and dislocations cut into  $ \gamma' $ phases (marked as green and yellow triangles in Fig. 10(b, c)). According to Fig. 5 and Table 4, the time of every stage and the corresponding percentage is different, which implies that the microstructure characteristics (such as dislocation patterns, SFs structures, and  $ \gamma' $ morphologies) are evolving, accompanied by the change of deformation mechanisms during diverse stress rupture stages. The stress rupture mechanism can be summarized as follows: (I) There is an incubation period of 3.11 h (as shown in Fig. 5) before the primary stage. Due to this stage being at the beginning of the stress rupture deformation, the initial microstructure (as shown in Fig. 2) plays a decisive role. The driving force of the dislocation motion in the incubation stage is the applied stress and temperature, and the primary resistance of the dislocation motion is the Orowan resistance in the  $ \gamma $ matrix which is the initial location of the dislocation source. The Orowan stress can be described as the following formula [70]:

 $$ \tau_{\mathrm{or}}=\sqrt{\frac{2}{3}}\frac{\mu b}{h} $$ 

where b is the Burgers vector,  $ \mu $ is the shear modulus, and h is the width of the  $ \gamma $ matrix channel. Therefore, according to Tables 3 and 4, the initial and tested width of the  $ \gamma $ matrix channel is both fine, inducing a strong Orowan stress in the  $ \gamma $ matrix. Moreover, the reaction between initial dislocation tangles and newly generated dislocations also increases the resistance of dislocation movement, which is a unique feature for AM-ed superalloys compared to those fabricated by casting [71]. The  $ \gamma' $ phase is small and approximately cubic with high content at the initial state, generating a misfit stress field, which is another effective way to impede the motion of dislocations. Meanwhile, the short time and relatively low temperature ensure the above occurrence of the phenomenon. Thus, the movement of the dislocation is heavily restricted, resulting in the decline of strain rate at first, which implies the emergence of a short incubation stage. However, the broadening of the  $ \gamma $ matrix channel and the dislocation multiplication carry on with the progress of the stress rupture deformation, which creates favorable conditions for the dislocation movement. The stress rupture strain rate increases rapidly accompanied by the termination of the incubation stage. After a short deformation time of the incubation stage, the number of movable dislocations becomes more and more, which begins to tangle with each other in the  $ \gamma $ matrix, further limiting the motion of dislocations. The stress rupture strain rate transforms from increasing rapidly to decreasing gradually, which represents the beginning of the primary stage. (II) Epishin and Link [72] suggested that the slide of the a/2  $ \langle 011 \rangle $ type dislocations in the  $ \gamma $ matrix channels is the common deformation mode of superalloys during the primary stage. Under the regulation of temperature and high misfit lattice stress, the cubic and high content of  $ \gamma' $ phases appear gradually (detail introduced in Section 4.1), limiting the motion of a/2  $ \langle 011 \rangle $ type dislocations. Besides, it is well known that the anti-phase boundary (APB) energy and the stacking fault energy (SFE) compete [73] when the APB energy is lower than the stacking faults energy, the dislocation pairs containing APB will appear abundantly and vice versa. It was reported when 1 at% Ta is used to replace 1 at% Al, the APB energy of Ni $ _{3} $Al increases from 180 to 240 mJ m $ ^{-2} $ [74]. Hence, due to the high content of Ta of alloy ZGH451, SFE decreases significantly accompanied by the increase of APB energy. The stacking faults (SFs) begin to appear in the  $ \gamma $ matrix and  $ \gamma' $ phase (Fig. 10(c)) at a condition of high applied stress, low SFE, moderate temperature, and the motion of a/2  $ \langle 011 \rangle $ type dislocations. The SFs in the  $ \gamma $ matrix channel take shape as the following equation [75]:

 $$ a/2<011\rightarrow a/6<112>+a/6<121>+SFin\gamma $$ 

based on Eq. (1), the  $ a/2 < 011> $ interface dislocation in the  $ \gamma $ matrix channel turns into two extended dislocations which are  $ a/6 < 112> $ and  $ a/6 < 121> $, forming SFs simultaneously. Besides, the stacking faults in the  $ \gamma' $ phase are formed as following equation [76]:

 $$ a/2<011\rightarrow a/3<121>+a/6<112>+SFin\gamma/ $$ 

the  $ a/2 < 011> $ dislocation turns into two extended dislocations of  $ a/3 < 121> $ and  $ a/6 < 112> $, respectively. It is widely accepted that the  $ a/3 < 121> $ dislocation cuts into the  $ \gamma' $ phase (100 nm long marked as green triangles in Fig. 10(c)), which creates the SFs in the  $ \gamma' $ precipitates. The  $ a/6 < 112> $ dislocation remains in the  $ \gamma $ matrix channel. Therefore, lots of dislocation piled-ups are generated on  $ \gamma/\gamma' $ interface and interact with SFs (illustrated in Fig. 10(b, c)) as the testing progresses, further hindering the dislocation motion. The stress rupture strain rate decreases rapidly under the above multiple structure constraints on dislocation movement. (III) The secondary stage is the most important stage for stress rupture properties due to the minimum stress rupture strain rate and stable deformation. The content of  $ \gamma' $ phase was increased as well as the shape more cubic as the tests carried on. The size of  $ \gamma' $ phase is gradually close to the best size range ( $ \sim $300 nm) on creep resistance based on previous reports [77,78]. Furthermore, the self-strength of  $ \gamma' $ phase is also strengthened due to the excellent solid solution strengthening effect of the Ta element. Therefore, the characteristic of  $ \gamma' $ phase further reduces the probability of dislocations to cut into the  $ \gamma' $ phase and locks them in  $ \gamma $ matrix, inducing heavy dislocation pile-up. Meanwhile, based on the
Fig. 10. TEM images showing deformation microstructures under 760 ^\circC/780 MPa after fractured: (a–c) TEM morphologies; (d, e) the schematic illustration of the deformation mechanism

previous discussion, the APB energy increases with high content of Ta, and there are only few short coupled pairs of a/2 type dislocations with APB ( $ \sim $70 nm) observed in  $ \gamma' $ precipitate (arcuate and wavy shaped marked as yellow triangle in Fig. 10(b)), which can reduce the minimum strain rate due to the low quantity of superdislocations according to the report of Zhang et al. [79]. Here, the relationship between the creep rate ( $ \varepsilon $) and average particle size (d) of  $ \gamma' $ precipitates could be confirmed qualitatively in the shearing mode as follows [80]:

 $$ \varepsilon\propto d^{-2} $$ 

the minimum stress rupture strain rate decreases with increasing particle size. As the dislocations partially cut in, the number of SFs increases as well as the intersection of SFs (marked as blue arrows in Fig. 10(c)), known as Lomer-Cottrell (L-C) lock [81] caused by the reaction of leading partial dislocations from two {111} slip planes. The L-C locks have been also proven to be effective obstacles for dislocation movement by pinning the leading partial dislocations. The increasing number of L-C locks provides more pinning sites and intensifies dislocation stacking. Hence, due to the favorable morphology and high content of  $ \gamma' $ phases and multiple types of defect interactions, the dislocation motion is hindered efficiently, resulting in low minimum stress rupture strain rate, and prolonging the time of the secondary stage. (III) It is obvious that the strain rate and strain increase rapidly at the tertiary stage. The severe local deformation (such as GBs) promotes the initiation and propagation of cracks near voids and chain-like carbides, creating the abrupt rise of stress rupture strain rate and decrease of strain (mentioned in Section 3.4). However, due to the stable structure of high content of cubic  $ \gamma' $ phases, the cracks are suppressed in grains while easy to propagate along the GBs, which slightly alleviates the rapid increase of strain rate. The detailed deformation mechanism is shown in the schematic illustration in Fig. 10(d, e).

4.3. Deformation mechanism under high temperature and low stress (980 ^\circC/260 MPa)

Fig. 11 exhibits the microstructure obtained by TEM near-stress rupture fracture and the corresponding schematic illustration of the deformation mechanism after testing under 980 ^\circC/260 MPa. The dislocations bypassing the \gamma′ phase and the dislocation networks on the \gamma/\gamma′ interface are the key deformation mechanisms affecting the performance of the alloy. Similarly, the stress rupture process can be divided into typic three stages based on the different time of every stage. (I) Due to the high temperature giving a high driving force for dislocation motion, the initial dislocations annihilate each other or terminate at GBs or crystal surfaces. The impediment on dislocation motion of the initial microstructure is weakened, inducing the disappearance of the incubation period. The slide of the a/2 〈011〉 type dislocation loops in the \gamma matrix channels is also the major deformation mode during the primary stage at high temperatures and low stress. With the dislocation multiplication, some movable dislocations promote the formation of the dislocation networks on \gamma/\gamma′ interface driven by temperature and misfit stress. The formation of dislocation networks could effectively release the misfit stress, weakening the ability of the alloy to regulate \gamma′ shape. Hence, as the increasing dissolution of the \gamma matrix channel (fine residual \gamma matrix marked in the yellow circle in Fig. 9(e)) and the directional coarsening of the \gamma′ phase, the rafting of \gamma′ phase starts to take place. However, it was reported that the Ostwald ripening and directional coarsening were accompanied with the rafting process and their competitive results would determine the width of \gamma′ rafting. The smaller
Fig. 11. TEM images showing deformation microstructures under 980 ^\circC/260 MPa after fractured: (a–c) TEM morphologies; (d, e) the schematic illustration of the deformation mechanism.

initial  $ \gamma' $ phase makes the Ostwald ripening in a dominant position [82], which delays the evolution of  $ \gamma' $ rafting. Therefore, slow rafting of the initial fine approximate cubic  $ \gamma' $ phase and increasingly formed dislocation networks impeded the dislocation movement, inducing the continuous decrease of strain rate during the primary stage. Once the complete  $ \gamma' $ rafting is formed, the primary stage will be terminated, followed by the start of the secondary stage. (II) There are two main factors which are the dislocation networks on the  $ \gamma/\gamma' $ interface and rafted  $ \gamma' $ phases determined the stress rupture properties at the secondary stage, different from those at 760 ^\circC/780 MPa. As mentioned above, high Ta content induces intense  $ \gamma/\gamma' $ lattice misfit, namely strong elastic strain energy on the  $ \gamma/\gamma' $ interface. Thus, the dislocation networks on the  $ \gamma/\gamma' $ interface are increasingly stable, homogeneous, and regular during the secondary stage (as shown in Fig. 11), which effectively hinders the glide of the dislocations. When a dislocation wants to separate itself from the dislocation networks, the stress ( $ \tau $) for the separateness can be described as the following formula [83]:

 $$ \tau=\alpha Gb/R $$ 

where  $ \alpha $ is a constant, G is the shear force, b is the Burgers vector, and R is the radius of the dislocation separateness. Due to the fine dislocation spacing ( $ \sim $12 nm) of dislocation networks, the R is small, inducing large  $ \tau $ in the alloy. Therefore, the movement of the dislocations in the dislocation networks is more difficult, which makes them locked on  $ \gamma/\gamma' $ interface and difficult to shear  $ \gamma' $ phases, resulting in bypassing  $ \gamma' $ phases mostly (demonstrated by dislocation loops in Fig. 11) and the decline of strain rate. However, due to the softening of alloy and  $ \gamma' $ rafting caused by high temperature, several dislocations still cut into the  $ \gamma' $ phase, which has two main categories: the common  $ a < 101> $ superdislocations [84] and the single dislocation (marked as green triangles Fig. 11(c)). The  $ a < 101> $ superdislocations are general  $ \sim $150 nm long (marked as yellow triangles in Fig. 11(b, c)), which present as arcuate and wavy and are formed via an association of the coupled pairs of a/2 type dislocations with APB, same as those at 760 ^\circC/780 MPa. However, the number and length of  $ a < 101> $ superdislocations are larger and longer than those at 760 ^\circC/780 MPa, due to the decline of APB energy under high temperatures. Conversely, the SFE is increasingly higher, the stacking faults have vanished entirely and shearing of single dislocation is few, which is consistent with the previous works [73,85]. The single dislocation is usually shown as short and thick lines with a length of  $ \sim $70 nm, which is formed via the leading dislocation of a/3 < 121> (following Eq. (7)). On the other hand,  $ \gamma' $ rafting is gradually completely at the secondary stage, forming continuous and stable rafted structures, especially in the DC. Plenty of interfaces and a larger length-width ratio of rafted  $ \gamma/\gamma' $ structure can reduce the chance of dislocations entering or bypassing the  $ \gamma' $ phase, further decreasing the strain rate. Hence, based on the above discussions, the beneficial microstructure characteristics of dislocation networks and rafted  $ \gamma' $ reduce the strain rate to the minimum value and stable at this state during the whole stage. However, due to the structure degenerated of  $ \gamma' $ phases induced by dislocations shearing and rafting, the ability to hinder the movement of dislocations is weakened compared to 760 ^\circC/780 MPa, the minimum strain rate is higher and the time of the second stage is shortened. Based on the empirical relationship between the creep rate ( $ \varepsilon $) and average particle size (d) of  $ \gamma' $ precipitates in the bypassing mode as follows [80]:

 $$ \varepsilon\propto d^{2} $$ 

the minimum stress rupture strain rate can also qualitatively be proved to increase with increasing particle size. (III) The topological inversion phenomenon, aggregation and growth of voids,
Fig. 12. Schematic illustration of crack initiation and propagation under 980 ^\circC/20 MPa after fractured: (a) schematic illustration of rafted microstructures, cracks, and two types of voids; (b) the content and diameter of voids.

and formation of cracks are the primary factors for the rapid increase of the stress rupture strain rate at the tertiary stage. Epishin et al. [86] suggested that the topological inversion phenomenon would be observed when the  $ \gamma' $ volume fraction was over 50 %. After statistical analysis, the average  $ \gamma' $ volume fraction of alloys is 62.55 % after the stress rupture test, which would be higher in IR due to the segregation of  $ \gamma' $ forming elements and high temperature. Hence, in IR, high content coarsening  $ \gamma' $ phases are mutually connected and surround the  $ \gamma $ matrix, forming irregular rafted structures, namely, the topological inversion phenomenon. For the above-rafted structures, the threshold shear stress ( $ \tau_{oB} $) of dislocation motion can be expressed as [87]:

 $$ \tau_{\mathrm{oB}}=\frac{Gb}{2\pi\lambda}\ln\left(\frac{\lambda}{r_{0}}\right) $$ 

where  $ \lambda $ is the particle interspacing, and  $ r_{0} $ is the dislocation core radius. If taking  $ G = 62.7 \, GPa $ at 973 K [43],  $ r_{0} = b = 0.26 \, nm $, and  $ \lambda = 0.9 $ and  $ 0.6 \, \mu m $ for the particle interspacing in the IR and DC (Fig. 9), respectively, the Orowan bowing stress is estimated to be 22.94 and 32.06 MPa. Therefore, the topological inversion phenomenon provides continuous and low energy channels for dislocation motion and reduces the obstacle of  $ \gamma/\gamma' $ phase boundary in IR, resulting in a rapid increase in strain rate. In contrast, in DC, rafted  $ \gamma' $ phases are still stable and uniform, limiting the dislocation motion and alleviating the rapid increase of strain rate. Meanwhile, lots of movable dislocation leaves large amounts of vacancies, which promotes the formation and growth of voids in IR (Fig. 9(c)) under the influence of temperature and stress. The large size of voids generates cracks easily. The detailed deformation mechanism is shown in the schematic illustration in Fig. 11(d, e). Moreover, the topological inversion phenomenon also weakens the strength of IR based on the results of Eq. (11) and reduces the number of  $ \gamma/\gamma' $ interfaces, making the propagation of cracks concentrated in IR and terminated on DC (illustrated in Fig. 12). Therefore, large number and size of voids and cracks in IR further increase the strain rate. The alloy fracture failed within a few hours with the quick increase of the strain rate.

## 4.4. Response of microstructure, defects, and stress rupture properties to temperature/stress

According to the above analysis of microstructure evolution, fracture mechanism, deformation mechanism, and corresponding stress rupture curves of the alloy ZGH451 fabricated by DED under two testing conditions, the response of microstructure, defects, and stress rupture properties to temperature/stress can be concluded. The reasonable composition design and printing process make the alloy crack-free and have superior microstructures. On the one hand, numerous  $ \gamma' $ forming elements and high Ta/Al ratio induce enough composition and strong misfit lattice stress for the formation of lots of cubic  $ \gamma' $ phases or regular rafted  $ \gamma' $ phases, which hinders the motion of dislocations throughout the whole stress rupture testing significantly, extending the lives and decreasing the strain rate. On the other hand, the interaction of multiple types of crystal defects (including the dislocation tangles induced by initial dislocations, L-C locks formed by SFs, dislocation networks generated by misfit lattice stress and high temperature) can further impede the slide and shearing of dislocations, reduces the strain rate and prolongs the stress rupture lives, which also illustrates the complexity and uniqueness of the mechanical process of AM-ed superalloys. With the increase of the temperature and extension of the time, the content and size of voids and cracks are both increasing at two testing conditions, resulting in rapid strain rate and shortening lives. Especially at high temperatures and low stress, heavy rafted  $ \gamma' $ phases in IR greatly promote the initiation and propagation of cracks, making the alloy fracturing failure even faster. The applied stress often makes the  $ \gamma' $ phases and defects elongate along the loading direction, which promotes the evolution of microstructure and defects, but not as significantly as the effect of temperature. In a word, the stress rupture properties can be enhanced by the stable and cubic structures at conditions with
Fig. 13. Comparison of stress rupture properties based upon Larson-Miller parameter of reported heat-treated alloy IN718, ABD-900AM, CM247LC [88], and various states of alloy ZGH451.

various temperatures and stresses, but damaged by the irregular rafted structures, high content, and large size of defects. Hence, the self-developed advanced alloy ZGH451 (fabricated by DED or selective laser melting (SLM)) with excellent microstructures at the as-built state and heat treatment (650 ^\circC/4 h, AC (stress relief annealing) + 1200 ^\circC/180 MPa/2 h, AC (HIP)) state both exhibit superior stress rupture properties compared to the recently reported [88] alloy ABD-900AM and commercial alloys IN718 and CM247LC based on the results of Larson-Miller Parameter (LMP) plot (Fig. 13), defined as:

 $$ \mathrm{LMP}=T\times\left(20+\log_{10}(t_{\mathrm{r}})/1000\right) $$ 

where T is the absolute temperature in K and  $ t_{r} $ is the time to rupture in h.

## 5. Conclusions

The microstructure evolution and stress rupture behavior of the as-built ZGH451 Ni-based superalloy fabricated by the DED process were investigated under two testing conditions (760 ^\circC/780 MPa and 980 ^\circC/260 MPa). The following conclusions are established:

(1) The as-built microstructure of alloy ZGH451 is mainly composed of highly textured columnar grains with epitaxial finer dendrites elongated to the deposition direction, small approximate cubic  $ \gamma' $ phases in dendrites, and a few contents of MC-type carbides on GBs. Besides, the formation of initial dislocation tangles on  $ \gamma/\gamma' $ interface driven by misfit lattice stress and residual thermal stress led to the unique sub-structure. The initial microstructure is crack-free with few voids.

(2) At 760 ^\circC/780 MPa, the cubic  $ \gamma' $ phases and small size of voids enhance the deformation resistance of alloy while chain-like  $ M_{23}C_{6} $ carbides weaken the strength of GBs, resulting in fracture mode of mixed fracture. However, at 980 ^\circC/260 MPa, the rafted  $ \gamma' $ phases and large size of voids are profit for crack propagation while the granular-shaped  $ M_{6}C $ carbides firm the structure of GBs, leading to a fracture mode of typical micro-void aggregation fracture.

(3) The deformation mechanism at 760 ^\circC/780 MPa is composed of dislocation piled up on \gamma/ \gamma' interface, formation of stacking faults in \gamma' phases, and dislocations shearing \gamma' phases. High content and suitable size of cubic \gamma' phases, preserved initial dislocation tangles, and l-C locks hinder the dislocation motion, which decreases the minimum strain rate and prolongs life significantly, forming four stress rupture stages. However, the deformation mechanism transforms to form dislocation networks on \gamma/ \gamma' interface and dislocations shearing \gamma' phases at 980 ^\circC/260 MPa. The rafted structure and high temperature provide continuous channels and enough energy for dislocation motion, resulting in an increase of minimum strain rate, decline of life, and typical three stress rupture stages, even though there are obstacles to dislocation movement caused by dislocation networks.

(4) The response of microstructure, defects, and stress rupture properties to temperature/stress can be concluded as: cubic or regular rafted  $ \gamma' $ phases induced by high Ta/Al ratio as well as the interaction of multiple types of crystal defects hinder slide and shearing of dislocations, extending the lives at both conditions. With the increase of temperature and extension of the time, the content and size of rafted  $ \gamma' $ phases, voids, and cracks are increasing, which promotes the initiation and propagation of cracks, and the motion of dislocations, damaging the stress rupture properties. The applied stress accelerates microstructure degradation by elongating the precipitates and defects along the loading direction, further decreasing mechanical properties.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## CRediT Authorship

Wei Song: Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Writing – original draft, Writing – review & editing. Junying Yang: Investigation, Methodology. Jingjing Liang: Funding acquisition, Supervision. Nannan Lu: Funding acquisition, Supervision. Yizhou Zhou: Supervision. Xiaofeng Sun: Supervision. Jinguo Li: Funding acquisition, Project administration, Resources, Supervision.

## Acknowledgements

This work was financially supported by the Technology Area Fund of the Basic Strengthening Program (No. 2021-JCJQ-JJ-0092), the Science Center for Gas Turbine Project (Project No. P_{2022}-C-IV-002-001), the Defense Industrial Technology Development Program (No. JCKY2020130C024), the National Key R&D Program of China (Grant No. 2021YFB3702503), and the National Science and Technology Major Project (No. Y_{2019}-VII-0011-0151). The authors are grateful for those supports.

## References

[1] N. Matan, D.C. Cox, P. Carter, M.A. Rist, C.M.F. Rae, R.C. Reed, Acta Mater. 47 (1999) 1549–1563.

[2] T.M. Pollock, Nat. Mater. 15 (2016) 809–815.

[3] A.C. Yeh, A. Sato, T. Kobayashi, H. Harada, Mater. Sci. Eng. A 490 (2008) 445–451.

[4] D.K. Das, K.S. Murphy, S. Ma, T.M. Pollock, Metall. Mater. Trans. A 39 (2008) 1647–1657.

[5] D.D. Gu, W. Meiners, K. Wissenbach, R. Poprawe, Int. Mater. Rev. 57 (2012) 133–164.

[6] B.B. Milner, P. Gradl, G. Snedden, M. Brooks, J. Pitot, E. Lopez, M. Leary, F. Berto, A. Plessis, Mater. Des. 209 (2021) 110008.

[7] C. Panwisawas, Y.T. Tang, R.C. Reed, Nat. Commun. 11 (2020) 1–4.

[8] C. Körner, Int. Mater. Rev. 61 (2016) 361–377.

[9] T. DebRoy, T. Mukherjee, J.O. Milewski, J.W. Elmer, B. Ribic, J.J. Blecher, W. Zhang, Nat. Mater. 18 (2019) 1026–1032.

[10] L.N. Carter, C. Martin, P.J. Withers, M.M. Attallah, J. Alloy. Comp. 615 (2014) 338–347.

[11] K. Moussaoui, W. Rubio, M. Mousseigne, T. Sultan, F. Rezai, Mater. Sci. Eng. A 735 (2018) 182–190.

[12] K.H. Ryou, H.J. Im, J.W. Park, P.P. Choi, Mater. Des. 234 (2023) 112298.

[13] W.Z. Zhou, Y.S. Tian, Q.B. Tan, S. Qiao, H. Luo, G.L. Zhu, D. Shu, B.D. Sun, Addit. Manuf. 58 (2022) 103016.

[14] K.S. Kim, T.H. Kang, M.E. Kassner, K.T. Son, K.A. Lee, Addit. Manuf. 35 (2020) 101377.

[15] S. Park, Y. Tanaka, S. Okazaki, Y. Funakoshi, H. Kawashima, H. Matsunaga, Mater. Lett. 350 (2023) 134844.

[16] A. Mostafaei, R. Ghiaasiaan, I.T. Ho, S. Strayer, K.C. Chang, N. Shamsaei, S. Shao, S. Paul, A.C. Yeh, S. Tin, A.C. To, Prog. Mater. Sci. 136 (2023) 101108.

[17] H. Qi, M. Azer, A. Ritter, Metall. Mater. Trans. A 40 (2009) 2410–2422.

[18] X. Wang, L.N. Carter, B. Pang, M.M. Attallah, M.H. Loretto, Acta Mater. 128 (2017) 87–95.

[19] X. Lu, J. Du, Q. Deng, J. Zhuang, J. Mater. Res. Technol. 3 (2014) 107.

[20] J. Zhang, Scr. Mater. 48 (2003) 677–681.

[21] R. Wang, J. Wang, T.W. Cao, R.X. Zhao, X.F. Lu, W. Guan, H. Tao, S.S. Shuai, X.S. Zhe, W.D. Xuan, C. Panwisawas, C.Y. Chen, Z.M. Ren, Addit. Manuf. 61 (2023) 103363.

[22] N.N. Lu, Z.L. Lei, K. Hu, X.F. Yu, P. Li, J. Bi, S.B. Wu, Y.B. Chen, Addit. Manuf. 34 (2020) 101228.

[23] M. Zhong, H. Sun, W. Liu, X. Zhu, J. He, Scr. Mater. 53 (2005) 159–164.

[24] S.G. Jeong, S.Y. Ahn, E.S. Kim, S.H. Kang, S.H. Yoo, J.Y. Ryu, J.H. Chun, G.M. Karthik, H.S. Kim, Mater. Sci. Eng. A 888 (2023) 145797.

[25] B. Liu, Y.T. Ding, J.Y. Xu, X.M. Wang, Y.B. Gao, Y. Hu, D.L. Chen, Mater. Sci. Eng. A 866 (2023) 144683.

[26] W. Zhou, G. Zhu, R. Wang, C. Yang, Y. Tian, L. Zhang, A. Dong, D. Wang, D. Shu, B. Sun, Mater. Sci. Eng. A 791 (2020) 139745.

[27] M. Ramsperger, R.F. Singer, C. Körner, Metall. Mater. Trans. A 47 (2016) 1469–1480.

[28] H.E. Helmer, C. Körner, R.F. Singer, J. Mater. Res. 29 (2014) 1987–1996.

[29] J.P. Choi, G.H. Shin, S. Yang, D.Y. Yang, J.S. Lee, M. Brochu, J.H. Yu, Powder Technol. 310 (2017) 60–66.

[30] K.N. Amato, S.M. Gaytan, L.E. Murr, E. Martinez, P.W. Shindo, J. Hernandez, S. Collins, F. Medina, Acta Mater. 60 (2012) 2229–2239.

[31] L.E. Murr, E. Martinez, S.M. Gaytan, D.A. Ramirez, B.I. Machado, P.W. Shindo, J.L. Martinez, F. Medina, J. Wooten, D. Ciscel, U. Ackelid, R.B. Wicker, Metall. Mater. Trans. A 42 (2011) 3491–3508.

[32] M. Ramsperger, L. Mújica Roncery, R.F. Singer, W. Theisen, C. Körner, Adv. Eng. Mater. 17 (2015) 1486–1493.

[33] D. Bürger, A.B. Parsa, M. Ramsperger, C. Körner, G. Eggeler, Mater. Sci. Eng. A 803 (2019) 138089.

[34] P. Sreeramagiri, A. Bhagavatam, H. Alrehaili, G. Dinda, J. Alloys Compd. 838 (2020) 155634.

[35] N.K. Adomako, N. Haghdadi, S. Primig, Mater. Des. 223 (2022) 111245.

[36] S.Y. Zhang, X. Lin, L.L. Wang, X.B. Yu, H.O. Yang, L.M. Lei, W.D. Dong, Mater. Sci. Eng. A 803 (2021) 140702.

[37] H. Pasiowiec, B. Dubiel, R. Dziurka, P. Bała, P. Ledwig, Wróbel M, M. Gajewska, W. Ziaja, Poręba M, Mater. Sci. Eng. A 887 (2023) 145742.

[38] M. Préobstle, S. Neumeier, J. Hopfenmüller, L.P. Freund, T. Niendorf, D. Schwarze, M. Göken, Mater. Sci. Eng. A 674 (2016) 299–307.

[39] V. Kalyanasundaram, A.D. Luca, R. Wróbel, J. Tang, S.R. Holdsworth, C. Leinenbach, E. Hosseini, Addit. Manuf. Lett. 5 (2023) 100119.

[40] C. Kéorner, M. Ramsperger, C. Meid, D. Bürger, P. Wollgramm, M. Bartsch, G. Eggeler, Metall. Mater. Trans. 49 (2018) 3781–3792.

[41] S.W. Ci, J.J. Liang, J.G. Li, H.W. Wang, Y.Z. Zhou, X.F. Sun, Y.T. Ding, J. Alloys Compd. 854 (2021) 157180.

[42] L. Cui, J. Yu, J. Liu, X. Sun, J. Alloys Compd. 746 (2018) 335–349.

[43] W. Song, X.G. Wang, J.G. Li, L.H. Ye, G.C. Hou, Y.H. Yang, J.L. Liu, J.D. Liu, W.I. Pei, Y.Z. Zhou, X.F. Sun, Mater. Sci. Eng. A 772 (2020) 138646–138656

[44] Y. Kuo, S. Horikawa, K. Kakehi, Scr. Mater. 129 (2017) 74.

[45] S. Wu, H.Y. Song, H.Z. Peng, P.D. Hodgson, H. Wang, X.H. Wu, Y.M. Zhu, M.C. Lam, A.J. Huang, Acta Mater. 224 (2022) 117528.

[46] T.G. Langdon, Int. J. Mater. Res. 96 (2005) 522–531.

[47] X.P. Tan, J.L. Liu, X.P. Song, T. Jin, X.F. Sun, Z.Q. Hu, J. Mater. Sci. Technol. 27 (2011) 899–905.

[48] W.M. Tucho, P. Cuvillier, A. Sjolyst-Kverneland, V. Hansen, Mater. Sci. Eng. 689 (2017) 220.

[49] D. Deng, R.L. Peng, H. Brodin, J. Moverare, Mater. Sci. Eng. 713 (2018) 294.

[50] S. Li, Q.S. Wei, Y.S. Shi, Z.C. Zhu, D.Q. Zhang, J. Mater. Sci. Technol. 35 (2015) 946–952.

[51] W. Kurz, D.J. Fisher, Acta Mater. 29 (1981) 11–20.

[52] W. Song, X.G. Wang, J.G. Li, J. Meng, Y.H. Yang, J.L. Liu, J.G. Liu, Y.Z. Zhou, X.F. Sun, J. Mater. Sci. Technol. 89 (2021) 16–23.

[53] A. Heckl, S. Neumeier, M. Gōken, R.F. Singer, Mater. Sci. Eng. A 528 (2011) 3435–3444.

[54] Z.W. Lian, J.J. Yu, X.F. Sun, H.R. Guan, Z.Q. Hu, Mater. Sci. Eng. A 489 (2008) 227–233.

[55] L. Cui, H. Su, J. Yu, J. Liu, T. Jin, X. Sun, Mater. Sci. Eng. 707 (2017) 383–391.

[56] J. Yu, X. Sun, N. Zhao, T. Jin, H. Guan, Z. Hu, Mater. Sci. Eng. 460 (2007) 420–427.

[57] T. Link, A. Epishin, M. Paulisch, T. May, Mater. Sci. Eng. A 528 (2011) 6225–6234.

[58] J.W. Christian, Mater. Today 6 (2003) 53.

[59] S.M. Cardonne, P. Kumar, C.A. Michaluk, H.D. Schwartz, Int. J. Refract. Met. Hard Mater. 13 (1995) 187–194.

[60] A.F. Giamei, D.L. Anton, Metall. Trans. 16 (1985) 1997.

[61] V.A. Vorontsov, J.S. Barnard, K.M. Rahman, H.Y. Yan, P.A. Midgley, D. Dye, Acta Mater. 120 (2016) 14–23.

[62] Z.H. Tan, X.G. Wang, L.H. Ye, G.C. Hou, R. Li, Y.H. Yang, J.L. Liu, J.D. Liu, L. Yang, B. Wang, P. Dong, J.G. Li, Y.Z. Zhou, X.F. Sun, Mater. Sci. Eng. A 761 (2019) 138042.

[63] B.G. Choi, I.S. Kim, D.H. Kim, C.Y. Jo, Mater. Sci. Eng. A 478 (2008) 329–335.

[64] T.J. Garosshen, G.P. Mccarthy, Metall. Trans. A 16 (1985) 1213–1223.

[65] L.Z. He, Q. Zheng, X.F. Sun, G.C. Hou, H.R. Guan, Z.Q. Hu, J. Mater. Sci. 40 (2005) 2959–2964.

[66] A.K. Jena, M.C. Chaturvedi, J. Mater. Sci. 19 (1984) 3132–3139.

[67] W.R. Sun, J.H. Lee, S.M. Seo, S.J. Choe, Z.Q. Hu, Mater. Sci. Eng. A 271 (1999) 143–149.

[68] C.N. Wei, H.Y. Bor, L. Chang, J. Alloys Compd. 509 (2011) 5708–5714.

[69] W. Österle, S. Krause, T. Moelders, A. Neidel, G. Oder, J. Völker, Mater. Charact. 59 (2008) 1564–1571.

[70] X.P. Tan, J.L. Liu, T. Jin, Z.Q. Hu, H.U. Hong, B.G. Choi, I.S. Kim, C.Y. Jo, Mater. Sci. Eng. A 528 (2011) 8381–8388.

[71] J.X. Zhang, T. Murakumo, Y. Koizumi, H. Harada, J. Mater. Sci. 38 (2003) 4883–4888.

[72] A. Epishin, T. Link, Philos. Mag. 84 (2004) 1979–2000.

[73] X.G. Wang, J.L. Liu, T. Jin, X.F. Sun, Mater. Sci. Eng. A 598 (2014) 154–161.

[74] R.C. Reed, N. Matan, D.C. Cox, M.A. Rist, C.M.F. Rae, Acta Mater. 47 (1999) 3367–3381.

[75] S. Ma, L. Carroll, T.M. Pollock, Acta Mater. 55 (2007) 5802–5812.

[76] F. Diologent, P. Caron, Mater. Sci. Eng. A 385 (2004) 245–257.

[77] R.C. Reed, The Superalloys Fundamentals and Applications, Cambridge University Press, Cambridge, UK, 2006.

[78] J.S. VanSluytman, T.M. Pollock, Acta Mater. 60 (2012) 1771–1783.

[79] J.X. Zhang, J.C. Wang, H. Harada, Y. Koizumi, Acta Mater. 53 (2005) 4623–4633.

[80] G. Ansell, J. Weertman, Met. Mater. Soc. 5 (1959) 838.

[81] L.L. Zhu, H.N. Kou, J. Lu, Appl. Phys. Lett. 101 (2012) 081906.

[82] W. Chen, J.P. Immarigeon, Scr. Mater. 39 (1998) 167–174.

[83] R.W. Kozar, A. Suzuki, W.W. Milligan, J.J. Schirra, M.F. Savage, T.M. Pollock, Metall. Mater. Trans. A 40 (2009) 1588–1603.

[84] G. Eggeler, A. Dlouhy, Acta Mater. 45 (1997) 4251–4262.

[85] H. Harada, H. Murakami, Comput. Mater. Sci. 34 (1999) 39–70.

[86] A. Epishin, T. Link, U. Brückner, P.D. Portella, Acta Mater. 49 (2001) 4017–4023.

[87] M. McLean, Acta Mater. 33 (1985) 545–556.

[88] Y.T. Tang, C. Panwisawas, J.N. Ghoussoub, Y. Gong, J.W. Clark, A.A. Németh, D.G. McCartney, R.C. Reed, Acta Mater. 202 (2021) 417–436.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

Journal of Materials Science & Technology 206 (2025) 37–52

Article history:
Revised 27 March 2024

## Keywords

Additive manufacturing
Nickel-based superalloys
Stress rupture behavior
Microstructure evolution
Deformation mechanisms

## ABSTRACT

https://doi.org/10.1016/j.jmst.2024.03.072

1005-0302/© 2024 Published by Elsevier Ltd on behalf of The editorial office of Journal of Materials Science & Technology.

W. Song, J. Yang, J. Liang et al.

at a temperature of 120 ^\circC for 6 h. The substrate prepared by vacuum melting furnace with the same composition as powders was employed with dimensions of 30 mm \times 30 mm \times 20 mm. The substrate surface was polished using sandpaper and cleaned with acetone to remove oil and oxide layers.

The stress rupture tests were carried out until fractured on the F-25 creep machine at 760 ^\circC/780 MPa and 980 ^\circC/260 MPa,

Fig. 5 illustrates the stress rupture curves of alloy ZGH451 under the conditions of 760 ^\circC/780 MPa and 980 ^\circC/260 MPa. Based on the curves, the stress rupture behavior can be summed up as follows: (I) It is noticeable that the stress rupture lives decrease with the increase of testing temperatures (Fig. 5(a)), which are

at the minimum strain rate for a short time, and then the alloy fractures rapidly. Besides, the average minimum strain rate under 980 ^\circC/260 MPa is much higher than that of 760 ^\circC/780 MPa, which are 2.08 \times 10⁻⁴/s and 1.78 \times 10⁻⁵/s, respectively.

Herein, due to the slight shaking of the external extensometer, the record of strain is unstable, hence, the minimum stain rate exhibits a range of  $ 1.15 \times 10^{-4}-3.33 \times 10^{-5} $ /s for 760 ^\circC/780 MPa and  $ 2.77 \times 10^{-4}-1.38 \times 10^{-4} $ /s for 980 ^\circC/260 MPa.

After testing at 760 ^\circC/780 MPa, the supersaturated solid solution of  $ \gamma $ induced by the AM process and long-term (134.20 h) thermal exposure of 760 ^\circC provide high precipitation force and

## 4.2. Deformation mechanism under medium temperature and high stress (760 ^\circC/780 MPa)

## 4.3. Deformation mechanism under high temperature and low stress (980 ^\circC/260 MPa)

The microstructure evolution and stress rupture behavior of the as-built ZGH451 Ni-based superalloy fabricated by the DED process were investigated under two testing conditions (760 ^\circC/780 MPa and 980 ^\circC/260 MPa). The following conclusions are established:

(2) At 760 ^\circC/780 MPa, the cubic  $ \gamma' $ phases and small size of voids enhance the deformation resistance of alloy while chain-like  $ M_{23}C_{6} $ carbides weaken the strength of GBs, resulting in fracture mode of mixed fracture. However, at 980 ^\circC/260 MPa, the rafted  $ \gamma' $ phases and large size of voids are profit for crack propagation while the granular-shaped  $ M_{6}C $ carbides firm the structure of GBs, leading to a fracture mode of typical micro-void aggregation fracture.

## Declaration of Competing Interest

## CRediT Authorship

This work was financially supported by the Technology Area Fund of the Basic Strengthening Program (No. 2021-JCJQ-JJ-0092), the Science Center for Gas Turbine Project (Project No. P_{2022}-C-IV-002-001), the Defense Industrial Technology Development Program (No. JCKY2020130C024), the National Key R&D Program of China (Grant No. 2021YFB3702503), and the National Science and Technology Major Project (No. Y_{2019}-VII-0011-0151). The authors are grateful for those supports.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

ELSEVIER

Contents lists available at ScienceDirect

journal homepage: www.elsevier.com/locate/jmst

Article history:
Received 29 February 2024
Revised 27 March 2024
Accepted 30 March 2024
Available online 25 April 2024

Keywords:
Additive manufacturing
Nickel-based superalloys
Stress rupture behavior
Microstructure evolution
Deformation mechanisms

A B S T R A C T

* Corresponding authors.
E-mail addresses: jjliang@imr.ac.cn (J. Liang), jgli@imr.ac.cn (J. Li).

at a temperature of 120 °C for 6 h. The substrate prepared by vacuum melting furnace with the same composition as powders was employed with dimensions of 30 mm × 30 mm × 20 mm. The substrate surface was polished using sandpaper and cleaned with acetone to remove oil and oxide layers.

The stress rupture tests were carried out until fractured on the F-25 creep machine at 760 °C/780 MPa and 980 °C/260 MPa,

Fig. 5 illustrates the stress rupture curves of alloy ZGH451 under the conditions of 760 °C/780 MPa and 980 °C/260 MPa. Based on the curves, the stress rupture behavior can be summed up as follows: (I) It is noticeable that the stress rupture lives decrease with the increase of testing temperatures (Fig. 5(a)), which are

at the minimum strain rate for a short time, and then the alloy fractures rapidly. Besides, the average minimum strain rate under 980 °C/260 MPa is much higher than that of 760 °C/780 MPa, which are 2.08 × 10⁻⁴/s and 1.78 × 10⁻⁵/s, respectively.

Herein, due to the slight shaking of the external extensometer, the record of strain is unstable, hence, the minimum stain rate exhibits a range of  $ 1.15 \times 10^{-4}-3.33 \times 10^{-5} $ /s for 760 °C/780 MPa and  $ 2.77 \times 10^{-4}-1.38 \times 10^{-4} $ /s for 980 °C/260 MPa.

After testing at 760 °C/780 MPa, the supersaturated solid solution of  $ \gamma $ induced by the AM process and long-term (134.20 h) thermal exposure of 760 °C provide high precipitation force and

4.2. Deformation mechanism under medium temperature and high stress (760 °C/780 MPa)

4.3. Deformation mechanism under high temperature and low stress (980 °C/260 MPa)

The microstructure evolution and stress rupture behavior of the as-built ZGH451 Ni-based superalloy fabricated by the DED process were investigated under two testing conditions (760 °C/780 MPa and 980 °C/260 MPa). The following conclusions are established:

(2) At 760 °C/780 MPa, the cubic  $ \gamma' $ phases and small size of voids enhance the deformation resistance of alloy while chain-like  $ M_{23}C_{6} $ carbides weaken the strength of GBs, resulting in fracture mode of mixed fracture. However, at 980 °C/260 MPa, the rafted  $ \gamma' $ phases and large size of voids are profit for crack propagation while the granular-shaped  $ M_{6}C $ carbides firm the structure of GBs, leading to a fracture mode of typical micro-void aggregation fracture.

Declaration of competing interest

CRediT authorship contribution statement

This work was financially supported by the Technology Area Fund of the Basic Strengthening Program (No. 2021-JCJQ-JJ-0092), the Science Center for Gas Turbine Project (Project No. P2022-C-IV-002-001), the Defense Industrial Technology Development Program (No. JCKY2020130C024), the National Key R&D Program of China (Grant No. 2021YFB3702503), and the National Science and Technology Major Project (No. Y2019-VII-0011-0151). The authors are grateful for those supports.