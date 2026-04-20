DOI: 10.1016/j.mattod.2025.05.022

Research

# Nanotwinned precipitates induced ultra-strong AlCoCrFeNi_{2.1} eutectic high-entropy alloy through additive manufacturing

Lin Zhou $ ^{a,1} $, Fenghui Duan $ ^{a,1} $, Yinghao Zhou $ ^{a} $, Xiangren Bai $ ^{a} $, Zhihao Jiang $ ^{a} $, Tianshui Zhou $ ^{b} $, Qian Li $ ^{c} $, Hengwei Luan $ ^{a} $, Gan Li $ ^{a} $, Junhua Luan $ ^{c} $, Xuliang Chen $ ^{a} $, Annan Chen $ ^{a} $, Ying Li $ ^{d} $, Xu Wang $ ^{e} $, Tao Yang $ ^{c} $, Jian Lu $ ^{a,d,f,*} $

 $ ^{a} $ Department of Mechanical Engineering, City University of Hong Kong, Hong Kong, China

 $ ^{b} $ School of Materials Science and Engineering, Lanzhou University of Technology, Lanzhou 730050, China

 $ ^{c} $ Department of Materials Science and Engineering, City University of Hong Kong, Hong Kong, China

 $ ^{d} $ CityU-Shenzhen Futian Research Institute, Shenzhen 518045, China

 $ ^{e} $ School of Mechanical Engineering, Northwestern Polytechnical University, Xi'an, Shanxi 710072, China

 $ ^{f} $ Centre for Advanced Structural Materials, Greater Bay Joint Division, Shenyang National Laboratory for Materials Science, City University of Hong Kong Shenzhen Research Institute, Shenzhen, China

## ARTICLE INFO

## Keywords

Nanotwinned precipitates

Eutectic high-entropy alloy

Additive manufacturing

Precipitation Mechanism

Mechanical properties

## Abstract

Modulating the secondary phase is a key approach to enhancing the mechanical properties of metallic materials, relying heavily on processing methods and alloy composition. Here, we harness the extreme printing conditions of laser-based powder bed fusion to create a non-equilibrium microstructure dominated by the B_{2} phase in an AlCoCrFeNi $ _{2.1} $ eutectic high-entropy alloy (EHEA). A simple post-heat treatment introduces high-density nanoprecipitates, featuring ultrafine parallel twin lamellae ( $ \sim $2.4 nm), into the B_{2} matrix. These nanotwinned (NT) precipitates, unprecedented in traditionally processed HEAs, form via an intriguing two-step process, involving the transformation of the hexagonal close-packed into an NT structure through the slipping of Shockley partial dislocations. The successful incorporation of nanotwin into precipitates delivers remarkable strengthening of 565 MPa without compromising ductility compared to the as-built sample. The resulting tensile strength reaches 2200 MPa at room temperature, marking one of the highest strengths reported for additively manufactured HEAs. This breakthrough paves the way to fabricate structural materials with unique microstructures and excellent properties for broad applications.

## Introduction

The incorporation of second phases into microstructures is a powerful strategy employed by metallurgists to manipulate the properties of engineering metallic materials [1,2]. Achieving optimal microstructures typically involves complex solidification and solid-state phase transformation processes, which are influenced by interfacial chemistry, non-equilibrium vacancies, metastable phases, and interactions with structural defects [3,4]. These transformations are driven by the interplay of thermodynamic and kinetic factors, leading to phenomena such as nucleation, growth, and spinodal decomposition [4–6]. The specific outcomes depend on both the fabrication techniques and alloy composition.

Additive manufacturing (AM) is a revolutionary technology enabling the fabrication of almost any geometrical part. Laser-based powder bed fusion (PBF-LB), as a typical metal AM technique, is rapidly advancing metal fabrication across various industries [7–11]. With the inherent rapid solidification and complex thermal cycling, PBF-LB demonstrates the potential to manipulate the precipitation microstructure for exceptional mechanical performance. In terms of solidification mechanisms, (PBF-LB)-produced microstructures share similarities with other rapid solidification techniques, which introduce non-equilibrium energy fluctuations into the material. This process not only refines grain size but also promotes the formation of lattice defects, such as dislocations and twins, in the secondary phase. For example, in rapidly solidified eutectic Al-Si [12] and Al-Al₂Cu [13] systems, high-density twins or dislocations

are introduced into the nanoscale second phase, improving the matching of dislocation slip in the matrix, thus resulting in a simultaneous enhancement of both strength and plasticity.

Furthermore, the rapid and spatially variable heating, melting, solidification, and cooling cycles inherent to PBF-LB generate substantial internal energy and a high degree of metastability. These dynamics result in heterogeneous grain structure, non-equilibrium phase compositions, and compositional fluctuations [14,15]. More importantly, the associated stress and energy fluctuations provide a strong driving force for post-treatment solid-state phase transformations, facilitating precise modulation of the secondary phase [16,17]. This capability is particularly advantageous for high-entropy alloys (HEAs), which are characterized by multiple principal elements and sluggish diffusion. By modifying the chemical ordering preference of constituent elements, nanoprecipitates with special intrinsic structures, such as local chemical ordering [18] or order complexation [19], are enhanced, fostering the synergy between ductility and strength. In essence, the interplay between HEAs composition and the advanced capability of AM gives new insights into tailoring novel precipitates with specific intrinsic structures for high-performance alloys, which merits in-depth exploration.
Fig. 1. Microstructures of the as-built AlCoCrFeNi₂.₁ EHEA. (a) 3D reconstructed SEM micrographs. (b) Inverse pole figure and (c) phase map with the high-magnification microscope. (d) Bright-field (BF) TEM image of the B_{2} and FCC nano-lamellae (indicated by a blue dot and a pink dot, respectively), with the zone axis of [011] for the FCC phase and [111] for the B_{2} phase. (e) Atomic-scale HAADF-STEM image of an enlarged view of the local area in (d) showing the phase boundary between FCC and B_{2} phases. (f) Corresponding fast Fourier transform (FFT) pattern of the image in (e), showing the K-S relationship between FCC- and B_{2}-lamellae. (g) STEM-EDS mapping of the lamellar colony. (h) BF image of the cellular structure with a B_{2} cell (indicated by a blue dot) surrounded by an FCC shell (indicated by a pink dot). (insert) Corresponding selected area electron diffraction (SAED) pattern from the [001] zone axis, showing the superlattice structure of B_{2}. (i) HRTEM image of the enlarged view of the local area in (h) showing the phase boundary between FCC and B_{2} phases. (j) Corresponding FFT pattern of the image in (i) showing the N-W relationship between the B_{2} and FCC phases. (k) STEM-EDS mapping of the cellular colony. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

However, the understanding of as-AM microstructures in HEAs remains limited, warranting further investigation.

Herein, we exploit the extreme printing conditions (e.g., rapid cooling rate, large temperature gradient, and complex thermal cycling) of PBF-LB to create high-density nanoprecipitates with extremely fine, parallel twin boundaries (TBs) in the B_{2}-phase dominated AlCoCrFeNi₂.₁ EHEA. Experimental characterizations reveal a two-step formation mechanism for the NT precipitates. Initially, hexagonal close-packed (HCP) precipitates form as precursors, which then transform into the nanotwinned (NT) structure through partial dislocation motions. The dense-dispersed NT nanoprecipitates contribute to a remarkable strength enhancement of 565 MPa, achieving an impressive room temperature (RT) tensile strength of approximately 2.2 GPa. Notably, the material exhibits a tensile strength of 1133 MPa at 600 ^\circC, surpassing most additively manufactured metals for intermediate-temperature applications. Our findings demonstrate that the inherent thermal cycling and rapid solidification of PBF-LB can be leveraged to create an NT microstructure, resulting in exceptional mechanical properties.

## Results

## As-built microstructure

A dual-phase hierarchical microstructure is achieved in the as-built AlCoCrFeNi₂.₁ EHEA by optimizing the PBF-LB process (Fig. 1). The 3D reconstructed SEM image (Fig. 1a) displays regular and smooth scan tracks, measuring approximately 52 \mum, which corresponds to the preset hatch space of 50 \mum. Further observations show that the solidified melt pools (MPs) are partially overlapped with their adjacent ones, each featuring a mixture of nano-lamellar and cellular eutectic colonies (Fig. 1a, Fig. S2a–e). These eutectic colonies exhibit an elongated morphology and are oriented toward the centers of the MPs (Fig. S2a–c), leading to almost random shape orientations (Fig. 1b). Specifically, the nano-lamellar colonies form in the heat-affected zone (HAZ) around the MPs due to overlapped tracks and repeated heating (Fig. S2a, b) [20], while the cellular structures within the MPs are driven by the high cooling rate of PBF-LB (Fig. S2a, c). Compared with the majority of AM-ed AlCoCrFeNi₂.₁ EHEAs that are predominantly composed of the FCC phase [14,21–25], the present EHEA obtained through PBF-LB exhibits a lower volume fraction of the FCC phase (16.4 %) and a much higher volume fraction of the B_{2} phase (83.6 %) (Fig. 1c), attributed to the rapid cooling rate from PBF-LB [26]. The predominant B_{2} phase in the as-built condition indicates a non-equilibrium microstructure, with the phase and elemental distributions deviating markedly from the equilibrium state.

The lamellar colonies are composed of alternating FCC and ordered B_{2} nanolayers (Fig. 1d), which are commonly observed in the as-built AlCoCrFeNi₂.₁ EHEA [14]. The as-built microstructure has no precipitates in the FCC and B_{2} matrix. Instead, a high density of dislocations is present due to the rapid solidification of PBF-LB (Fig. S_{3}). TEM characterizations (Fig. 1e, f) reveal that the interfaces between FCC and B_{2} phases follow the Kurdjumov–Sachs (K-S) orientation relationship ( $ \{011\}_{B_{2}}//\{111\}_{FCC} $ and  $ <111>_{B_{2}}//<011>_{FCC} $). The average thicknesses of the FCC and B_{2} nanolayers are measured as  $ \lambda_{FCC} = 87 $ nm and  $ \lambda_{B_{2}} = 160 $ nm, respectively. Additionally, compositional analysis by STEM-EDS (Fig. 1g, Fig. S4a, b) shows that the element distribution between the FCC and B_{2} phases deviates notably from the equilibrium components and differs from those in as-cast or additively manufactured samples with similar lamellar structures [14,27]. Specifically, the concentrations of Co, Cr, Fe, and Ni are comparable between the two phases, while the Al content in the B_{2} phase (16.8 at.%) is higher than that in the FCC phase (14.1 at.%) (summarized in Table S_{2}). Intriguingly, biconinuous Ni-Al-rich and Co-Cr-Fe-rich nanostructures are observed within the B_{2} colony (Fig. 1g), suggesting the occurrence of spinodal decomposition [14]. Such nanoscale-modulated chemical inhomogeneity has not been reported in conventionally processed AlCoCrFeNi₂.₁ EHEAs [27]. Moreover, anomalous elemental fluctuations at the boundary of these two phases are identified, which might be related to the interdiffusion coefficient difference of constituent elements between the B_{2} and FCC phases [28].

Cellular colonies are primarily composed of the BCC phase with a high density of dislocations (Fig. 1c, Fig. S3c, d), which do not form via traditional metallurgical routes. TEM observation (Fig. 1h, i) reveals that the BCC subgrain (with an average cell size of 800 nm) adopts an ordered-B_{2} structure encapsulated by a disordered FCC interfacial nanolayer (~14 nm). The FCC and B_{2} phases in the cellular colony exhibit the Nishiyama-Wasserman (N-W) relationship (Fig. 1j) ( $ \{110\}_{B_{2}} // \{111\}_{FCC} $ and  $ <001 >_{B_{2}} // <011 >_{FCC} $). Elemental analysis shows that the primary difference in the composition between the two phases also lies in Al content, with the B_{2} phase being Al-enriched, in contrast to the FCC phase (Fig. 1k, Fig. S4c, d). Similar nanoscale-modulated chemical inhomogeneity is also observed within the B_{2} cellular colonies, potentially playing a crucial role in the precipitation and mechanical behavior of EHEAs [14]. Altogether, the extreme solidification conditions of PBF-LB create a hierarchical microstructure characterized by a high degree of metastability, thus offering great opportunities for distinct microstructural evolution compared to as-cast counterparts during the subsequent heat treatment.

## Post-annealed microstructure

The as-built samples were subjected to 600 ^\circC for 8 h to trigger nanoprecipitation. A multiple-order hierarchical multiphase architecture is achieved through this treatment. At the macro-scale (Fig. 2a), the annealed sample retains a mixture of nano-lamellar and cellular eutectic colonies, with only slight coarsening observed. Specifically,  $ \lambda_{FCC} $ and  $ \lambda_{B_{2}} $ increase from 87 to 96 nm and from 160 to 176 nm, respectively, while the average diameter of the cellular structure grows from ~ 549 to ~ 653 nm (Fig. S_{5}). At the micro-scale, the nanoscale precipitates are observed in both colonies after annealing (Fig. 2b–i, Fig. S2f, g). In the FCC phase, ordered L1₂ precipitates are identified, as evidenced by super-lattice spots in the SAED pattern (Fig. 2d, Fig. S_{6}, Supplementary Text 3). Whereas, high-density needle-like nanoprecipitates (indicated by yellow arrows) are evenly distributed within the B_{2} phases (Fig. 2b, f). These nanoprecipitates average ~ 180 nm in length and ~ 20 nm in diameter, with volume fractions of 20 % in lamellar colonies and 45 % in cellular colonies.

High-magnification BF-TEM images (Fig. 2e, i) reveal a fascinating feature — extremely fine lamellae substructures within the needle-like precipitates, distinguishable by numerous parallel lamellae. Atomic-resolution HAADF-STEM imaging (Fig. 3) confirms that these lamellae correspond to nanotwins (Fig. 3). These nanoprecipitates exhibit two distinct structure types. Specifically, the thicker nanoprecipitates (type I precipitates in Fig. 3a, b), with a width diameter exceeding 20 nm, have an FCC structure containing ultrafine nanotwins (Fig. 3c). These nanotwins show a twin thickness ranging from 0.4 nm to 16 nm with an average of 2.4 nm (inset in Fig. 3c). In contrast, the thinner nanoprecipitates (type II precipitates in Fig. 3a, b), with a width diameter under 10 nm, feature an HCP structure interspersed with high-density stacking faults (SFs) (Fig. 3d), where the SF spacing ranges from 0.4 to 2.9 nm, averaging 1.1 nm. Additionally, some nanoprecipitates showcase alternating HCP and FCC phases, with a high density of planar defects, including SFs and TBs (Fig. S_{7}). A rough estimation reveals that 76 % of needle-like nanoprecipitates are FCC-type, while the remainder are HCP-type or hybrid-type two. Further investigation of the precipitate-matrix interfaces shows that both NT FCC and HCP precipitates are semi-coherent with the B_{2} matrix (Fig. 3e–h). A classical KS orientation relationship is identified between the FCC precipitate and B_{2} matrix ( $ \{110\}_{B_{2}}//\{111\}_{FCC}, <\overline{1}11>_{B_{2}}//<1\overline{1}0>_{FCC} $), while a Burgers orientation relationship is identified between the HCP precipitate and B_{2}-matrix ( $ \{110\}_{B_{2}}//\{0001\}_{HCP} $ and  $ \overline{1}11>_{B_{2}}//<11\overline{2}0>_{HCP} $).
Fig. 2. Microstructures of the as-annealed AlCoCrFeNi₂.₁ EHEA. (a) SEM morphology of the multiple-order hierarchical multi-phase structure. (b) BF-TEM image of the lamellar structure, including the FCC phase (L1₂) (pink dot), B_{2} phase (blue dot), and needle-like precipitates in the B_{2}-lamellar (yellow arrows). (c, d) SAED patterns corresponding to B_{2} and FCC (L1₂) phases along the [111] and [011] zone axis, respectively. (e) High-magnification BF imaging of the B_{2}-lamellar showing a high density of lamella contrast in the needle-like precipitates. (f) BF-TEM image of the cellular structure, including the FCC-shell (pink dot), B_{2}-cell (blue dot), and needle-like precipitates in the B_{2}-cell (yellow arrows). (g, h) SAED patterns corresponding to the B_{2}-cell and the FCC-shell along the [001] and [110] zone axis, respectively. (i) High-magnification BF-TEM image of the B_{2}-cell showing extremely fine lamellae structures in the needle-like precipitates. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

To unveil the intragranular distribution and spatial morphology of elements at the atomic scale, 3D-APT and STEM-EDS characterizations were performed in the B_{2} colonies. The analysis reveals strong partitioning of Co, Cr, and Fe atoms into the NT FCC nanoprecipitates, whereas the Ni and Al atoms are depleted (Fig. 3i, Fig. S8a, c). The composition profile (Fig. 3i, Fig. S8b) and quantitative analysis (Table S_{2}) indicate that nanoprecipitates consist of Co, Cr, Fe, and Ni in nearly equiatomic ratios (approximately 24.4 at.%) and 2.4 at.% Al. These NT nanoprecipitates should correspond to the CoCrFeNiAl $ _{0.1} $ HEA, which are known for their exceptional ductility and excellent work-hardening capability under tensile deformation [29].

## Mechanical properties

To evaluate the influence of the NT precipitates on the mechanical properties, tensile tests were performed on both as-built and annealed EHEAs at RT and intermediate temperature (e.g., 600 ^\circC). Fig. 4a shows the representative engineering stress–strain curves of the as-built and as-annealed samples at RT and 600 ^\circC. At RT, as-built samples exhibit a high yield strength ( $ \sigma_{0.2} $) of 1388 \pm 10 MPa, and an ultimate tensile strength ( $ \sigma_{u} $) of 1731 \pm 31 MPa while maintaining an adequate uniform elongation of 3.9 \pm 0.3 %. Such high strength aligns with the previous findings, which reported a high hardness of 568.8 HV in a B_{2}-dominated EHEA [30]. We noticed the as-built samples exhibit reduced ductility compared to the additively manufactured AlCoCrFeNi₂.₁ EHEA reported by Ren et al., despite having similar  $ \sigma_{u} $ [14]. This discrepancy is attributed to the significantly higher volume fraction of the B_{2} phase (~83.6 %) in the current samples, which is 50 % more than that in the previously additive-manufactured samples [14]. The B_{2} phase’s limited deformability contributes to this reduction in ductility.

Upon post-annealing at 600 ^\circC for 8 h,  $ \sigma_{0.2} $ and  $ \sigma_{u} $ reach  $ 1723 \pm 37 $ MPa and  $ 2153 \pm 24 $ MPa, approximately 24 % higher than the values for the as-built samples, respectively. To the best of our knowledge, this  $ \sigma_{u} $ value is the highest reported for AlCoCrFeNi $ _{2.1} $ EHEA, surpassing counterparts prepared by hybrid-rolling (i.e. cryo-rolling followed by warm-rolling) [31] and most AM steels [32], Ti-based alloys [32], Ni-based superalloys [32–35] and EHEAs [14,21,23–25,28,36] (Fig. 4b). At 600 ^\circC, the as-annealed sample achieves a higher tensile strength ( $ 1090 \pm 34 $ MPa) with an adequate ( $ 3.0 \pm 0.14\% $) ductility compared to the as-built samples. This exceptional strength at RT and 600 ^\circC places the as-annealed EHEA above most AM and conventional Fe-based, Ti-based alloys, and Ni-based superalloys for intermediate-temperature applications [37–54] (Fig. 4c).

## Discussion

## Formation of NT precipitates

Generally, the development of NT metallic materials is constrained to growth-twin and deformation-twin methods [55–58]. Herein, our study introduces a novel fabrication pathway by employing AM to create high-density NT structures. Detailed analysis of the precipitation process reveals that NT FCC precipitates form within the B_{2} phase through a two-step mechanism. Initially, we detected the formation of unstable HCP-structured primary precipitates with high-density SFs at the early stage of heat treatment, i.e., 600 ^\circC for 5 and 30 min (Fig. 5). These precipitates are considerably narrower, averaging less than 10 nm in width, compared to those observed after 8 h of annealing at 600 ^\circC. Over time, the HCP phase gradually transforms into an NT FCC structure.
Fig. 3. Formation of extremely fine needle-like precipitates in the B_{2}-lamellae after annealing at 600 ^\circC for 8 h. (a) Low-magnification, and (b) High-resolution HAADF-STEM images of the lamellar structure, showing two types of precipitates (type I and II). (c) Atomic-scale HAADF-STEM image of type I precipitates, revealing the dominant FCC structure with dense nanotwins. (Inset) Twin thickness. (d) Atomic-scale HAADF-STEM image of type II precipitates, revealing the primary HCP structure with dense SFs and corresponding SAED pattern. (e, g) HAADF-STEM images of the interface between (e) the NT FCC phase and B_{2} matrix, and (g) the HCP phase and B_{2} matrix. (f) FFT pattern corresponding to (e), the insert FFT pattern confirming the twinning structure. (h) FFT pattern corresponding to (g), the insert FFT pattern confirming the HCP structure. (i) 3D reconstruction map of an APT needle tip and corresponding one-dimensional concentration profile showing the element distributions across the NT FCC precipitate and B_{2}-matrix.

## (Fig. 3 and Fig. 6).

It is crucial to highlight that in conventional AlCoCrFeNi₂.₁ EHEAs, primary precipitates within the B_{2} matrix are typically BCC particles [27,59]. This underscores the critical role of the PBF-LB process in inducing the formation of the primary HCP and the NT FCC precipitates. The extremely large cooling rates and thermal gradients (10⁵–10⁷ K/s) inherent to the PBF-LB’s spatiotemporal characteristics result in diffusion-limited solidification, producing non-equilibrium microstructures [14]. In our study, a severe PBF-LB protocol was implemented using a small laser spot size of 40 \mum, a high laser power of 100 W, a high scan speed of 1000 mm/s, and no preheating. These conditions generate microstructures dominated by the B_{2} phase, in contrast to samples produced by other AM methods, which primarily exhibit FCC structures [14,21–25]. The as-built samples also contain a supersaturated solution that is thermodynamically unstable. The composition of the B_{2} phase (Al₁₅.₉Co₁₆.₉Cr₁₅.₇Fe₁₆.₈Ni₃₄.₇) significantly deviates from its equilibrium state (Al₃₈.₅₆Co₁₀.₁₂Cr₄.₁₂Fe₉.₂Ni₃₇.₉₈ [59]). This non-equilibrium microstructure facilitates the formation of metastable precipitate phases or hierarchical precipitate structures (i.e., HCP and NT-FCC phases) during subsequent heat treatment.

Local compositional fluctuations (Fig. 1g, k), pre-existing dislocations (Fig. S_{3}), and substantial internal stress in the B_{2} phase facilitate
Fig. 4. Mechanical performance of AM-ed AlCoCrFeNi₂.₁ EHEAs at RT and 600 ^\circC. (a) Engineering stress–strain curves for the as-built and as-annealed AlCoCrFeNi₂.₁ EHEAs. (b) Tensile strength versus uniform elongation of as-annealed EHEAs against steels [32], Ti-based alloys [32], Ni-based superalloys [32–35], and EHEAs [14,21,23–25,28,36] (\sigmaₐ > 1000 MPa) at RT fabricated by AM. (c) Correlation between the tensile strength of as-annealed EHEAs at 600 ^\circC and RT, compared with other metallic materials for the intermediate-temperature applications, including Fe-based, Ti-based alloys, and Ni-based superalloys fabricated by AM [37–49] and their counterparts fabricated by conventional methods [42,50–54]. (Wire arc additive manufacturing (WAAM), Directed energy deposition (DED), Electron beam powder bed fusion (PBF-EB), Electron beam melting (EBM), Laser metal deposition (LMD).

the formation of HCP precursors. During annealing, high internal stress triggers a shear-dominated martensitic transformation, accompanied by atomic reconfiguration that modifies local compositions, yielding HCP phases with distinct chemistries from the B_{2} matrix (Table S_{2}). This transformation is characterized by intragranular HCP precipitation with needle morphology, and rapid kinetics (observed within 5 min of annealing) (Fig. 5a-c) [60,61]. The process involves coordinated dislocation slip along  $ \{110\}_{B_{2}} $ planes in  $ \langle\overline{1}11\rangle_{B_{2}} $ directions, adhering to the Burgers orientation relationship ( $ \{110\}_{B_{2}}//\{0001\}_{HCP}, \langle\overline{1}11\rangle_{B_{2}}//\langle11\overline{2}0\rangle_{HCP} $) (Fig. 3h). Our findings reveal a new transitional B_{2} \rightarrow HCP transformation pathway driven by simple shear, exhibiting a lower kinetic energy barrier than the conventional B_{2} \rightarrow FCC transformation commonly observed in HEAs. The latter, following the K-S relationship ( $ \{011\}_{B_{2}}//\{111\}_{FCC} $ and  $ \langle111\rangle_{B_{2}}//\langle011\rangle_{FCC} $), demands diffusion-mediated reconstruction or complex multi-step shear, leading to a relatively long kinetic process [62]. Although the equilibrium phase at 600 ^\circC is FCC rather than HCP, the Gibbs free energy difference between the two phases is minimal [63]. Consequently, the transformation kinetics of both phases in the B_{2} matrix are significantly influenced by the interfacial energy between the precipitate and the matrix. HAADF-STEM imaging (Fig. 3e-g) reveals that the lattice misfit at the HCP-B_{2} interface (1.4 %) is smaller than that of the FCC-B_{2} interface (2.4 %), favoring the preferential precipitation of the metastable HCP phase. Extended annealing (30 min) further reduces internal stress, increasing the density of needle-like HCP precipitates. Simultaneously, internal stress (e.g., interfacial stress, residual thermal stress, etc.) promotes SF formation within the HCP phase (Fig. 5d-f).

Additionally, internal stress drives the transition from the intermediate HCP phase to an NT FCC structure via Shockley partial dislocation slip (b = 1/6 <11 $ \overline{2}0> $) on HCP {0001} planes (Fig. 2, 3, 6c). We noted that the composition of the needle-like nanoprecipitates closely approaches FeCoCrNiAl $ _{x} $ (x < 0.45) (Table S_{2}), representing a typical system with a low stacking fault energy (SFE). Density functional theory (DFT) calculations indicate that the SFE of FeCoCrNiAl $ _{0.36} $ is approximately  $ -10 $ mJ/m $ ^{2} $ at RT, increasing to  $ \sim 5 $ mJ/m $ ^{2} $ at 600 ^\circC [63]. This low SFE is critical for the HCP  $ \rightarrow $ NT FCC transformation, which is governed by Shockley partial dislocation slip. During the further 8 h annealing, the metastability of the HCP phase relative to the FCC phase provides an additional thermodynamic driving force [63]. Therefore, high-density nanotwins are formed within the FCC precipitates. This shear-driven reconfiguration can serve as a stress-accommodation pathway, effectively redistributing internal stress inherited from PBF-LB processing while minimizing the system’s overall free energy [32]. The redistributing efficiency is evidenced by the reduction of internal
Fig. 5. Formation of needle-like precipitates in the B_{2}-matrix after annealing at 600 ^\circC for (a-c) 5 min, (d-f) 30 min. (a, b) BF-TEM images. (c) High-magnification BF-TEM image of an independent HCP structure and its corresponding nanobeam electron diffraction pattern. (d, e) BF-TEM images of HCP precipitates with dense SFs and (inset) corresponding nanobeam electron diffraction pattern. (f) High-resolution TEM image of the HCP structure.

stress based on the lattice constant change in the B_{2} phase.

Overall, the two-step martensitic transformation (Fig. 6) is kinetically favored over diffusion-mediated one-step FCC formation, due to the typical slow diffusion effect of multi-principal element alloys. Our research identifies three key factors driving the formation of distinct NT precipitates. First, the non-equilibrium microstructure, characterized by a supersaturated solid solution and high internal stress induced by rapid cooling and complex thermal cycling, enables the formation of metastable precipitates. Second, the multiphase alloy system provides a broad processing window to tailor the microstructure and composition away from equilibrium. Third, when a low SFE equilibrium phase (e.g., FCC or HCP) precipitates from a non-equilibrium BCC or other phases, a high density of Shockley partial dislocations is readily generated. These findings offer valuable insights for the rational design of high-performance alloys with tunable NT microstructures, potentially unlocking unprecedented combinations of strength and ductility.

## Strengthening mechanism of NT precipitates

As analyzed above, the as-built AlCoCrFeNi₂.₁ EHEA is predominantly composed of B_{2} phases, accompanied by a minor fraction of FCC phases. Therefore, high-density NT FCC phases precipitated from B_{2} phases, rather than L1₂ precipitated from FCC phases, are expected to provide the dominant contribution to nanoprecipitation strengthening. Generally, the precipitation of the FCC phase in the B_{2} matrix contributes negligibly to strengthening because the FCC phase commonly exhibits lower strength compared to the B_{2} phase [27]. However, in this work, the introduction of ultrafine nanotwins within the FCC precipitates noticeably enhances their strengthening effect on the material, as TBs are effective barriers to the nucleation and motion of dislocations [64]. The ultrafine twin spacing is expected to significantly enhance the yield stress of the precipitates through pronounced Hall-Petch hardening, potentially exceeding that of the B_{2} matrix. Observations of dislocation-precipitate interactions (Fig. S_{12}) show that dislocations pile up before the interfaces of nanoprecipitates, verifying that gliding dislocations are bypassed by Orowan bowing mechanism, similar to the semi-coherent HCP-structured precipitates in the CoFeV alloy [65].

The strengthening contribution of the NT FCC phase to the B_{2} matrix via the Orowan bowing mechanism can be expressed by [66]

 $$ \Delta\sigma_{\mathrm{orw}}=M\frac{0.4Gb}{\pi\sqrt{1-\nu}}\frac{ln(2r_{m}/b)}{\lambda_{p}} $$ 

where M is the Taylor factor for the B_{2} phase (~2.71) [14], G is the shear modulus for the B_{2} phase (~57 GPa) [14], b is the Burgers vector of the B_{2} phase (~0.248 nm) [14],  $ \nu $ is the Poisson ratio of the B_{2} phase (~0.25) [66],  $ r_{m} $ is the mean radius of the precipitates and  $ \lambda_{p} $ is the interprecipitate spacing within the B_{2} matrix ~ 64 nm.

Since precipitates formed in the B_{2} matrix are needle-shaped, equation (1) should be adjusted to account for their aspect ratio [67]:

 $$ K=h^{\frac{1}{6}}(\frac{2+h^{2}}{3})^{-\frac{1}{4}} $$ 

 $$ \Delta\sigma_{o r w-m o d i f i e d}=K^{-1}\Delta\sigma_{o r w} $$ 

where K is the shape correction factor, and h = c/a is the aspect ratio of precipitates ( $ \sim $8.75 for NT nanoprecipitates). Therefore, the strengthening contribution of the NT FCC precipitates in the B_{2} phase to the overall material can be expressed as:

 $$ \Delta\sigma=f_{B2}\Delta\sigma_{o r w-m o d i f i e d} $$ 

where  $ f_{B_{2}} $ is the volume fraction of the B_{2} phase.

The increment of yield strength contributed by NT precipitates in the B_{2}-matrix is estimated to be  $ \sim $ 565 MPa, which slightly surpasses the overall increment in yield strength ( $ \sim $335 MPa). This is primarily attributed to the diminishing impact of dislocation strengthening of the as-annealed samples compared with that of the as-built ones. The calculation underscores that ultrafine twin-spaced NT nanoprecipitates formed in the B_{2} phases play a dominant role in the observed
Fig. 6. Schematic drawings illustrate the microstructure evolution within the B_{2} matrix. (a) Evolved precipitation upon annealing from B_{2} (with a high density of dislocations) \rightarrow HCP \rightarrow NT FCC. Magnified illustration showing (I) highly faulted HCP structure, (II) NT FCC structure with extremely fine twins. (b) Stacking sequences of the HCP structure with SFs and the FCC structure with TBs at the atomic scale. (c) Shear transformation mechanism of HCP \rightarrow FCC through gliding of a group of Shockley partial dislocations.

strengthening. After annealing, the simultaneous reduction in dislocation effects and the alloy’s ordering degree, stemming from the precipitation behavior of B_{2} phases, is likely to yield a comparable level of ductility to that observed in the as-built specimens [3,14].

Additionally, TBs generally exhibit outstanding thermal stability compared with conventional high-angle GBs, efficiently hindering dislocation movement at high temperatures [68]. The coarsening temperature of nanotwins is expected to  $ 0.8T_{m} $ (the melting point, over  $ 600\ ^{\circ}C $) and thus exhibits exceptional thermal stability at  $ 600\ ^{\circ}C $ [69]. When dislocation slip encounters TBs, additional energy/force is required for slip transfer across these boundaries. As a result, the combination of thermal stability and dislocation resistance allows the current as-annealed EHEA to achieve exceptional strength across a broad temperature range, from RT to  $ 600\ ^{\circ}C $. These characteristics further highlight the pivotal role of NT precipitates in enhancing mechanical performance under diverse operating conditions.

## Conclusion

In summary, we propose a novel second-phase modulation paradigm induced by AM with the multi-principal element alloy design to develop high-performance metallic materials. The success of this approach is demonstrated in a non-equilibrium AlCoCrFeNi_{2.1} EHEA with dominant B_{2} phases fabricated by PBF-LB. After annealing, a unique nanoprecipitation microstructure characterized by ultrafine twin thicknesses is achieved in the EHEA, which enables exceptional mechanical performance across a wide temperature range from RT to 600 ^\circC. Such NT nanoprecipitates have not been previously reported in other HEAs and form through an intriguing two-step process. Initially, HCP precipitates with SFs form as precursors, which then transform into the NT structure through the slipping of Shockley partial dislocations. This approach offers significant potential for tailoring precipitation microstructures and enhancing properties in other multiphase compositionally complex alloys.

## Materials and Methods

## Material fabrication

The gas-atomized AlCoCrFeNi $ _{2.1} $ powder was fabricated by LangFeng Material Technology Co., Ltd., Foshan, China. The particle sizes of the powder ranged from 15 to 53  $ \mu $m with an average value of 31.5  $ \mu $m. The chemical composition of the powder is listed in Table S_{1}. The PBF-LB process was conducted using an EOS M100 Laser-sintering system (Germany) equipped with a 200 W fiber laser and a laser spot diameter of 40  $ \mu $m. The adopted optimized parameters were a laser power (P) of 100 W, a scan speed (v) of 1000 mm/s, a hatch spacing (h) of 0.05 mm, and a layer thickness (t) of 0.02 mm. Prior to the AM process, a 20  $ \mu $m thick layer of powder was deposited onto a 304 stainless-steel build platform without preheating in a high-purity argon environment (<1000 ppm oxygen). A laser beam traversed the powder feedstock along a predefined path, generating sufficient heat to melt the powder and form a melt pool, which subsequently solidified into a fused layer. After each scan, a new layer of powder was deposited, and the laser scanning direction was rotated by 67^\circ relative to the previous layer. This operation was repeated for each subsequent layer. The final printed rectangular plates, with dimensions of 40 mm (length) \times 8 mm (width) \times 4 mm (building height), exhibited a relative density exceeding 99 % and were used for mechanical testing. The chemical composition of an as-built sample is listed in Table S_{1}. The dog-bone-shaped samples with a thickness of 1.1 mm, gauge length of 8 mm, and width of 2 mm were cut from the printed products through electro-discharge machining. Post-heat treatments were performed in a muffle furnace at 600 ^\circC for various durations, followed by water quenching.

## Mechanical testing

All specimens were mechanically polished to remove impurities and oxides on the surface and to ensure a more accurate determination of a gauge dimension of 8 mm (length) \times 2 mm (width) \times 1 mm (thickness). The quasi-static uniaxial tensile tests at room temperature and 600 ^\circC were conducted on an Instron 5565 testing machine at an initial strain rate of  $ 1.0 \times 10^{-3} \, s^{-1} $ with a video extensometer. The direction of testing was perpendicular to the building direction. All tests were repeated at least three times to ensure reproducibility.

The phase identification was analyzed through X-ray diffraction (XRD) performed on a Bruker D8 Advance diffractometer operated at 40 kV and 40 mA, with a Cu radiation target (wavelength, 0.15406 nm) and scanning 2\theta from 20^\circ to 100^\circ.

## Microstructure characterization

Scanning electron microscopy (SEM) and electron back-scattered diffraction (EBSD) observations were conducted in an FEI Scios instrument equipped with an HKL-Technology EBSD system (orientation imaging microscopy, OIM software). For the SEM and EBSD tests, specimens were mechanically ground and then electrolytically polished.

Transmission electron microscopy (TEM) observations were performed on a JEOL JEM-2100F microscope operated at 200 kV. High-angle annular dark-field scanning transmission microscopy (HAADF-STEM) and high-resolution TEM (HRTEM) observations were conducted on a Cs-corrected TEM (FEI Themis Z) operated at 300 kV, to trace the microstructural evolutions of the post-annealing at the atomic level. Energy-dispersive X-ray spectrometry (EDS) analysis was carried out based on HAADF-STEM to quantify the compositions of all phases. TEM foils were mechanically ground to a thickness of  $ \sim $ 30  $ \mu $m and subsequently thinned using an ion-milling system (Gatan 695).

The chemical composition of each phase was also measured through three-dimensional atom probe tomography (3D-APT, CAMECA LEAP 5000XR). Needle-shaped specimens required for the APT were prepared via a lift-out method and then annularly milled in an FEI Scios focused ion beam (FIB)/SEM system. The specimens were analyzed at 70 K in voltage mode at a pulse repetition rate of 200 kHz, a pulse fraction of 20%, and an evaporation detection rate of 0.2 % atoms per pulse.

## CRediT Authorship

Lin Zhou: Writing – review & editing, Writing – original draft, Resources, Methodology, Investigation, Formal analysis, Data curation. Fenghui Duan: Writing – review & editing, Software, Resources, Methodology. Yinghao Zhou: Writing – review & editing, Methodology. Xiangren Bai: Writing – review & editing, Methodology. Zhihao Jiang: Resources, Methodology. Tianshui Zhou: Resources, Methodology. Qian Li: Writing – review & editing, Methodology. Hengwei Luan: Writing – review & editing, Methodology. Gan Li: Writing – review & editing. Junhua Luan: Methodology. Xuliang Chen: Writing – review & editing. Annan Chen: Methodology. Ying Li: Writing – review & editing. Xu Wang: Writing – review & editing. Tao Yang: Writing – review & editing. Jian Lu: Writing – review & editing, Methodology.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

This work was supported by Guangdong Province Science and Technology Plan Project 2023B1212120008, National Natural Science Foundation of China/ Hong Kong Research Grants Council Joint Research Scheme (Project No the RGC Theme-based Research Scheme AoE/M-402/20, Hong Kong JLFS - RGC-Joint Laboratory Funding Scheme (Grant No. JLFS/E-102/24) and the Hong Kong Innovation and Technology Commission via the Hong Kong Branch of National Precious Metals Materials Engineering Research Centre. T.Y is also grateful for financial support from the Shenzhen Science and Technology Program (Grant No. SGDX20210823104002016). J. Lu thanks for the IMR-CityU Joint Laboratory of Nanomaterials & Nanomechanics and Guangdong-Hong Kong Joint Laboratory of Modern Surface Engineering Technology.

## Appendix A. Supplementary data

## Supplementary Material

## Data Availability

Data will be made available on request.

## References

[1] J.L. Gu, et al., Chem. Rev. 124 (2024) 1247–1287.

[2] L.Y. Liu, et al., Adv. Sci. 8 (2021) 2100870.

[3] T. Yang, et al., Science 362 (2018) 933–937.

[4] L. Fan, et al., Nat. Commun. 11 (2020) 6240.

[5] Y.J. Liang, et al., Nat. Commun. 9 (2018) 4063.

[6] X.R. Bai, et al., Nat. Mater. 23 (2024) 747–754.

[7] T. DebRoy, et al., Prog. Mater. Sci. 92 (2018) 112–224.

[8] G. Liu, et al., Mater. Sci. Eng. R Rep. 145 (2021) 100596.

[9] C. Chua, et al., J. Manuf. Syst. 73 (2024) 75–105.

[10] Y.T. Liu, et al., Mater. Sci. Addit. Manuf. 2 (2023) 1587.

[11] W.X. Chen, et al., Virtual Phys. Prototy. 19 (2024) e2383302.

[12] H.H. Lien, et al., Mater. Res. Lett. 8 (2020) 291–298.

[13] S.J. Wang, et al., Acta Mater. 156 (2018) 52–63.

[14] J. Ren, et al., Nature 608 (2022) 62–68.

[15] G. Li, et al., Mater. Today 76 (2024) 40–51.

[16] Y.K. Mu, et al., Acta Mater. 232 (2022) 117975.

[17] Z.G. Zhu, et al., Mater. Today 52 (2022) 90–101.

[18] L. Wang, et al., Nat. Mater. 22 (2023) 950–957.

[19] Z.F. Lei, et al., Nature 563 (2018) 546–550.

## L. Zhou et al.

[20] J.C. Wang, et al., Adv. Powder Mater. 2 (2023) 100137.

[21] Y. Guo, et al., Addit. Manuf. 60 (2022) 103257.

[22] L. He, et al., J. Mater. Sci. Technol. 117 (2022) 133–145.

[23] Y.N. Guo, et al., J. Mater. Sci. Technol. 111 (2022) 298–306.

[24] X.T. Wang, et al., Mater. Sci. Eng. A 913 (2024) 147060.

[25] Y.N. Guo, et al., Int. J. Plast. 179 (2024) 104050.

[26] S. Mooraj et al., Commun. Mater. 5 (2024) 101.

[27] O Cheng et al. Acta Mater. 252 (2023) 118905

[27] Q. Cheng, et al., Acta Mater. 252 (2023) 118905.

[28] Z.W. Geng, et al., Addit. Manuf. 56 (2022) 102941.

[29] X.D. Xu, et al., Materialia 4 (2018) 395–405.

[30] L.W. Lan, et al., Virtual Phys. Prototyp. 19 (2024) e2355640.

[31] S.R. Reddy, et al., Sci. Rep. 9 (2019) 11505.

[46] R.F. Xu, et al., Adv. Powder Mater. 1 (2022) 100056.

32] Y. Zhu, et al., Nat. Mater. 21 (2022) 1258–1262.

[33] X. Yang, et al., Mater. Sci. Eng. A 767 (2019) 138394.

[45] C.H. Yu, et al., Addit. Manuf. 36 (2020) 101672.

[47] A.N.M. Tanvi, et al., J. Mater. Sci. Technol. 67 (2021) 80–94.

[48] S. Dryepondt, et al., Addit. Manuf. 37 (2021) 101723.

[34] Q.Q. Han, et al., Addit. Manuf. 30 (2019) 110919.

[40] Z. Zhu, et al., J. Mater. Res. Technol. 18 (2022) 2582–2592.

[37] Z.H. Zhu, et al., Mater. Sci. Eng. A 883 (2023) 145519.

[36] J. Ren, et al., Acta Mater. 257 (2023) 119179.

[34] Q.Q. Han, et al., Addit. Manuf. 36 (2017) 110519.

[35] D. Ivanov et al. Addit. Manuf. 18 (2017) 269–275.

[41] T.H. Wen, et al., J. Mater. Res. Technol. (2025) 776–784.

[39] H.Z. Niu, et al., Scr. Mater. 200 (2021) 113916.

[35] D. Ivanov, et al., Addit. Manuf. 18 (2017) 269–275.

[38] M. Todai, et al., Addit. Manuf. 13 (2017) 61–70.

[49] S.B. Zhang, et al., Scr. Mater. 235 (2023) 115627.

[42] S. Taller, T. Austin, Addit. Manuf. 60 (2022) 103280.

[43] M.M. Keleshteri, et al., Addit. Manuf. 94 (2024) 104499.

[50] J.W. Zhang, et al., Mater. at, High Temp. 40 (2023) 479–491.

[44] R.H. Hu, et al., Metals 14 (2024) 809.

[51] X.H. Qiang, et al., Eng. Struct. 112 (2016) 60–70.

[52] Z.H. Zhu, et al., Acta Metall. Sin-ENGL. 37 (2024) 2068–2082.

[54] Y. Liu, et al., Crystals 12 (2022) 1336.

[55] F.H. Duan, et al., Sci. Adv. 7 (2021) eabg5113.

[53] M.M. De Oliveira, et al., Metals 9 (2019) 301.

[56] Y.T. Zhu, et al., Prog. Mater. Sci. 57 (2012) 1–62.

[57] Q.S. Pan, et al., Science 382 (2023) 185–190.

[58] Q.S. Pan, et al., Science 374 (2021) 984–989.

[59] X.Z. Gao, et al., Acta Mater. 141 (2017) 59–66.

[60] L. Wang, et al., Scr. Mater. 189 (2020) 129–134.

[61] C. Wang, et al., Mater. Sci. Eng. A 786 (2020) 139371.

[62] P. Peng, et al., J. Alloys Compd. 939 (2023) 168843.

[63] P.J. Yu, et al., Acta Mater. 181 (2019) 491–500.

[64] K. Lu, et al., Science 324 (2009) 349–352.

[65] H. Chung, et al., Nat. Commun. 14 (2023) 145.

[66] T. Xiong, et al., Scr. Mater. 186 (2020) 336–340.

[67] B. Sonderegger, E. Kozeschnik, Scr. Mater. 66 (2012) 52–55.

[68] D.Y. Liu, et al., Scr. Mater. 242 (2024) 115938.

[69] O. Anderoglu, et al., J. Appl. Phys. 103 (2008).

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

Materials Today 88 (2025) 99–108

Materials Today

## Keywords
Nanotwinned precipitates
Eutectic high-entropy alloy
Additive manufacturing
Precipitation Mechanism
Mechanical properties
## ABSTRACT
 $ ^{1} $ These authors contributed equally to this work.
$ ^{1} $ These authors contributed equally to this work.
1369-7021/© 2025 Published by Elsevier Ltd.
## Materials and Methods
## CRediT Authorship
## Declaration of Competing Interest
## Supplementary Material
## Data Availability

## ABSTRACT

https://doi.org/10.1016/j.mattod.2025.05.022 https://doi.org/10.1016/j.mattod.2025.05.022 Local compositional fluctuations (Fig. 1g, k), pre-existing dislocations (Fig. S_{3}), and substantial internal stress in the B_{2} phase facilitate stress based on the lattice constant change in the B_{2} phase. The strengthening contribution of the NT FCC phase to the B_{2} matrix via the Orowan bowing mechanism can be expressed by [66] where M is the Taylor factor for the B_{2} phase (~2.71) [14], G is the shear modulus for the B_{2} phase (~57 GPa) [14], b is the Burgers vector of the B_{2} phase (~0.248 nm) [14],  $ \nu $ is the Poisson ratio of the B_{2} phase (~0.25) [66],  $ r_{m} $ is the mean radius of the precipitates and  $ \lambda_{p} $ is the interprecipitate spacing within the B_{2} matrix ~ 64 nm. Since precipitates formed in the B_{2} matrix are needle-shaped, equation (1) should be adjusted to account for their aspect ratio [67]: where K is the shape correction factor, and h = c/a is the aspect ratio of precipitates ( $ \sim $8.75 for NT nanoprecipitates). Therefore, the strengthening contribution of the NT FCC precipitates in the B_{2} phase to the overall material can be expressed as: where  $ f_{B_{2}} $ is the volume fraction of the B_{2} phase. The increment of yield strength contributed by NT precipitates in the B_{2}-matrix is estimated to be  $ \sim $ 565 MPa, which slightly surpasses the overall increment in yield strength ( $ \sim $335 MPa). This is primarily attributed to the diminishing impact of dislocation strengthening of the as-annealed samples compared with that of the as-built ones. The calculation underscores that ultrafine twin-spaced NT nanoprecipitates formed in the B_{2} phases play a dominant role in the observed strengthening. After annealing, the simultaneous reduction in dislocation effects and the alloy’s ordering degree, stemming from the precipitation behavior of B_{2} phases, is likely to yield a comparable level of ductility to that observed in the as-built specimens [3,14]. The phase identification was analyzed through X-ray diffraction (XRD) performed on a Bruker D8 Advance diffractometer operated at 40 kV and 40 mA, with a Cu radiation target (wavelength, 0.15406 nm) and scanning 2\theta from 20^\circ to 100^\circ. [34] Q.Q. Han, et al., Addit. Manuf. 36 (2017) 110519. [35] D. Ivanov et al. Addit. Manuf. 18 (2017) 269–275.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

ELSEVIER

Contents lists available at ScienceDirect

journal homepage: www.elsevier.com/locate/mattod

Keywords:
Nanotwinned precipitates
Eutectic high-entropy alloy
Additive manufacturing
Precipitation Mechanism
Mechanical properties

A B S T R A C T

* Corresponding author at: Department of Mechanical Engineering, City University of Hong Kong, Hong Kong, China.
E-mail address: jianlu@cityu.edu.hk (J. Lu).
 $ ^{1} $ These authors contributed equally to this work.

https://doi.org/10.1016/j.mattod.2025.05.022
Received 10 January 2025; Received in revised form 8 May 2025; Accepted 28 May 2025
Available online 8 June 2025
1369-7021/© 2025 Published by Elsevier Ltd.

Local compositional fluctuations (Fig. 1g, k), pre-existing dislocations (Fig. S3), and substantial internal stress in the B2 phase facilitate

stress based on the lattice constant change in the B2 phase.

The strengthening contribution of the NT FCC phase to the B2 matrix via the Orowan bowing mechanism can be expressed by [66]

where M is the Taylor factor for the B2 phase (~2.71) [14], G is the shear modulus for the B2 phase (~57 GPa) [14], b is the Burgers vector of the B2 phase (~0.248 nm) [14],  $ \nu $ is the Poisson ratio of the B2 phase (~0.25) [66],  $ r_{m} $ is the mean radius of the precipitates and  $ \lambda_{p} $ is the interprecipitate spacing within the B2 matrix ~ 64 nm.

Since precipitates formed in the B2 matrix are needle-shaped, equation (1) should be adjusted to account for their aspect ratio [67]:

where K is the shape correction factor, and h = c/a is the aspect ratio of precipitates ( $ \sim $8.75 for NT nanoprecipitates). Therefore, the strengthening contribution of the NT FCC precipitates in the B2 phase to the overall material can be expressed as:

where  $ f_{B2} $ is the volume fraction of the B2 phase.

The increment of yield strength contributed by NT precipitates in the B2-matrix is estimated to be  $ \sim $ 565 MPa, which slightly surpasses the overall increment in yield strength ( $ \sim $335 MPa). This is primarily attributed to the diminishing impact of dislocation strengthening of the as-annealed samples compared with that of the as-built ones. The calculation underscores that ultrafine twin-spaced NT nanoprecipitates formed in the B2 phases play a dominant role in the observed

strengthening. After annealing, the simultaneous reduction in dislocation effects and the alloy’s ordering degree, stemming from the precipitation behavior of B2 phases, is likely to yield a comparable level of ductility to that observed in the as-built specimens [3,14].

Materials and methods

The phase identification was analyzed through X-ray diffraction (XRD) performed on a Bruker D8 Advance diffractometer operated at 40 kV and 40 mA, with a Cu radiation target (wavelength, 0.15406 nm) and scanning 2θ from 20° to 100°.

CRediT authorship contribution statement

Declaration of competing interest

Supplementary data to this article can be found online at https://doi.org/10.1016/j.mattod.2025.05.022.

Data availability

[34] Q.Q. Han, et al., Addit. Manuf. 36 (2017) 110519.
[35] D. Ivanov et al. Addit. Manuf. 18 (2017) 269–275.