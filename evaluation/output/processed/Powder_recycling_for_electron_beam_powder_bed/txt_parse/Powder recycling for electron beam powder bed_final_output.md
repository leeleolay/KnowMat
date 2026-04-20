DOI: 10.1016/j.matdes.2025.114473

# Powder recycling for electron beam powder bed fusion of TiAl alloy☆

Feihong Wang $ ^{a} $, Mengchen Song $ ^{a} $, Yongfeng Liang $ ^{a,*} $ $ ^{ID} $, Gengwu Ge $ ^{a} $, Xiaoyu Liang $ ^{b,*} $, Feng Lin $ ^{b} $, Honghui Wu $ ^{a} $, Dongfang Wang $ ^{b} $, Wenbin Kan $ ^{c} $, Li Liu $ ^{c} $, Junpin Lin $ ^{a,*} $

$^{a}$ State Key Laboratory for Advanced Metals and Materials, University of Science and Technology Beijing, Beijing 100083, China

$^{b}$ Department of Mechanical Engineering, Tsinghua University, Beijing 100084, China

$^{c}$ Beijing Quick Beam Technology Co., Ltd., Beijing 100176, China

## ARTICLE INFO

## Keywords

Electron beam powder bed fusion

Powder recycling

TiAl alloy

Thermal exposure

Mechanical properties

## Abstract

This study systematically investigates the impact of powder recycling (up to 70 cycles) on Ti-48Al-2Cr-2Nb (at. %) alloy processed by electron beam powder bed fusion (EB-PBF). Comprehensive characterization (SEM/XRD/EBSD/XPS) reveals three key phenomena of recycling powder: (1) progressive Al depletion (48.43 \rightarrow 46.31 at.%) and oxygen uptake (560 \rightarrow 2000 ppm) at 22–28 ppm/cycle, (2) phase evolution from  $ \alpha/\alpha_{2} $ to  $ \gamma + B_{2} $ with C_{14} Laves phase precipitation (>30 cycles), and (3) surface oxide transformation from TiO $ _{2} $/Al $ _{2} $O $ _{3} $ (54 %:46 %) to Al $ _{2} $O $ _{3} $-dominated (82 %). The changes in these powders will affect the room temperature ultimate tensile strength (750 MPa) and ductility (reduced by 40 %) of the formed workpiece through grain refinement (\leq 10  $ \mu $m) and other means. The phase transformations of powders and parts are attributed to thermal exposure at 900–1150 ^\circC, with Cr segregation driving Laves phase formation. While oxide modification improves powder flowability, the increase of irregular powder increases part surface roughness. Quantitative analysis demonstrates that maintaining 15–30 % fresh powder optimizes the cost-performance ratio, providing practical guidelines for industrial implementation. These findings advance the understanding of powder degradation mechanisms in EBPBF and establish scientifically-grounded limits for TiAl alloy powder reuse in critical aerospace applications.

## 1. Introduction

TiAl alloys were known for their low density, high strength and good creep resistance at elevated temperatures [1,2]. Electron beam powder bed fusion (EB-PBF) technology had advantages in building TiAl alloy parts, such as high vacuum environment that can suppress oxygen addition, near net building that can avoid pollution, and high-temperature building that can suppress cracking [3,4]. Turbine blades made of Ti-48Al-2Cr-2Nb (at.%), fabricated using the EB-PBF, were used in the GE9X engine [3,4], indicating a growing trend towards large-scale production of TiAl alloy components using EB-PBF [5]. The price of TiAl pre-alloyed powders was relatively expensive, and there is a large amount of un-melted powders that needs to be recycled and reused for the EB-PBF process [6].

Due to the high crack sensitivity of TiAl alloys, the lightweight and easy occurrence of “smoking” in TiAl alloy powder, the building temperature for EB-PBF of TiAl alloy components generally ranges between 950 ^\circC and 1200 ^\circC [7,8]. During the EB-PBF process builds complex thin-walled structures, the majority of powders in the powder bed remains unused. These powders are subjected to multiple electron beam irradiations, high vacuum conditions, and are subsequently need to be recycled after cooling [9]. The microstructure and physical properties of these powders usually change after repeated electron beam exposure (Since EB-PBF involves repeated melting and solidification—similar to thermal exposure—this study uses the term ‘thermal exposure’ to describe this phenomenon) [10]. Meanwhile, commonly used TiAl powders are pre-alloyed, produced via methods such as the Plasma Rotating Electrode Process (PREP) or Electrode Induction Gas Atomization (EIGA), which result in non-equilibrium solidification states. During EB-PBF building, un-melted powders are exposed to prolonged heating, resulting in inevitable solid-state phase transformations [11]. Currently, there is limited research on the impact of phase transformation of powders on EB-PBF built parts. Therefore, investigating TiAl recycled powders is crucial for ensuring formability stability and regulating microstructure.

In recent years, there have been some reports on the research of

recycled powders. Shanbhag et al. [12] compared virgin Ti-6Al-4 V powders with powders recycled after two cycles and a mixture of virgin powder with equal mass fractions of powder recycled once and twice. The results showed degradation in morphology, particle size distribution, fluidity, and spreadability of recycled powders. Montelione et al. [13] conducted morphological and chemical analyses on Ti-6Al-4 V powders after 30 cycles, noting thermal cycling effects on microstructure and oxygen-rich surface layers due to environmental exposure during recycle. Wang et al. [14] studied Ti-48Al-2Cr-2Nb powders after 15 cycles with a total heating time of nearly 300 h, observing decreased fluidity, increased deformed particles with cycling, and stable mechanical properties. Gorji et al. [15] also reported a significant increase in O content in the recycled powders. The above studies indicate that powder recycling often increases O content and phase transformation.

\gamma, \alpha₂ and \beta₀ phases are main phase constituents for \gamma-TiAl alloys, while the \beta₀ phase has an ordered bcc structure and is rich in Cr and Mo [16,17]. But the \beta/\beta₀ phase does not appear in large quantities in Ti-48Al-2Cr-2Nb alloy prepared under traditional near-equilibrium solidification conditions [17,18]. Unlike traditional preparation methods, the content and effect of \beta₀ in Ti-48Al-2Cr-2Nb alloy formed under non-equilibrium solidification conditions in additive manufacturing (AM) become more pronounced [19,20]. In laser AM, liquation cracking is a common defect caused by grain boundaries segregation [20,21]. Wang et al. [20] found that cracking occurs in Nb depletion regions and at \alpha₂/\beta₀ phase interface during selective laser melting of Ti-48Al-2Cr-2Nb alloy. The presence of \beta₀ phase in Ti-48Al-2Cr-2Nb alloy prepared by EB-PBF has also been widely reported [21,22], and most researches attribute the changes in phase content in Ti-48Al-2Cr-2Nb alloy to the changes in Al content caused by different energy densities [21,22]. Meanwhile, the high-temperature building environment and thermal cycling during the layer by layer building process are also the main reasons for phase transition [22,23]. As far as the relevant reports are concerned, most of them have focused on the phase transformation and microstructure control of formed blocks, while there are few reports focusing on the phase transformation of reused powders after thermal cycles and repeated long-term thermal exposure, not to mention its impact on the microstructure and properties of formed components.

This study continuously tracked and characterized the production process of a thin-walled TiAl alloy component prepared using EB-PBF, focusing on the changes in physical properties and phase transitions of the powders across different recycling iterations. Furthermore, the microstructure and room temperature (RT) mechanical properties of the thin-walled specimens were tested. The results reveal significant alterations in the physical properties of the powders, e.g., particle size distribution, flowability, apparent density, elemental composition, surface oxide film, and alloy phases after up to 70 recycling cycles. Changes in the oxide and phases of the powders may affect the microstructure of the parts, while modifications in physical properties affect the powder spreading quality. Variations in O and Al content of the powders lead to changes in the microstructure of the built thin-walled parts, subsequently influencing their RT mechanical properties. In addition, a large number of C_{14}-Laves phases are discovered in the powders and the built parts after multiple cycles, the formation mechanism is also revealed.

## 2. Experimental methods

## 2.1. Powder recycling process and EB-PBF process

Ti-48Al-2Cr-2Nb powders, produced by EIGA with particle size ranging from 53–150  $ \mu $m were supplied by the Institute of Metal Research, Chinese Academy of Sciences. As illustrated in Fig. 1 (a), after exposure to high temperatures (parameters detailed in Table 1) and cooled to RT, both the powders in the hoppers and the un-melted powders were processed in the powder recovery system (PRS). The resulting blended powders were sieved, mixed, stored, and reloaded. The new powders were labeled as R0, first recycled powders as R1, while
Fig. 1. EB-PBF powders recycling process diagram and the effect of cycle times on powder: (a) Schematic of EB-PBF powders recycling process, (b) Schematic diagram of the total amount of powders and the proportion of powder not irradiated by EB during the cycling process.

Table 1

Ti-48Al-2Cr-2Nb thin-wall parts building process parameters.

<table border="1" style="margin: auto; word-wrap: break-word;"><tr><td style="text-align: center; word-wrap: break-word;">Average single furnace building time (h)</td><td style="text-align: center; word-wrap: break-word;">Melting strategy</td><td style="text-align: center; word-wrap: break-word;">Length of scanning line (mm)</td><td style="text-align: center; word-wrap: break-word;">Scanning speed (m/s)</td><td style="text-align: center; word-wrap: break-word;">Mean beam current (mA)</td><td style="text-align: center; word-wrap: break-word;">Line offset (mm)</td><td style="text-align: center; word-wrap: break-word;">EA(J/mm $ ^{2} $)</td></tr><tr><td rowspan="3">20</td><td rowspan="3">Hatching</td><td style="text-align: center; word-wrap: break-word;">10</td><td style="text-align: center; word-wrap: break-word;">1.8</td><td style="text-align: center; word-wrap: break-word;">5.40</td><td style="text-align: center; word-wrap: break-word;">0.1</td><td style="text-align: center; word-wrap: break-word;">1.80</td></tr><tr><td style="text-align: center; word-wrap: break-word;">20</td><td style="text-align: center; word-wrap: break-word;">2.1</td><td style="text-align: center; word-wrap: break-word;">7.35</td><td style="text-align: center; word-wrap: break-word;">0.1</td><td style="text-align: center; word-wrap: break-word;">1.94</td></tr><tr><td style="text-align: center; word-wrap: break-word;">40</td><td style="text-align: center; word-wrap: break-word;">2.3</td><td style="text-align: center; word-wrap: break-word;">8.60</td><td style="text-align: center; word-wrap: break-word;">0.1</td><td style="text-align: center; word-wrap: break-word;">2.24</td></tr><tr><td colspan="2">Substrate preheating temperature (^\circC)</td><td colspan="2">Powder bed preheating temperature (^\circC)</td><td style="text-align: center; word-wrap: break-word;"></td><td style="text-align: center; word-wrap: break-word;">Building temperature (^\circC)</td><td style="text-align: center; word-wrap: break-word;">Layer thickness (^\circC)</td></tr><tr><td style="text-align: center; word-wrap: break-word;">1070</td><td style="text-align: center; word-wrap: break-word;"></td><td style="text-align: center; word-wrap: break-word;">900-1150</td><td style="text-align: center; word-wrap: break-word;"></td><td style="text-align: center; word-wrap: break-word;"></td><td style="text-align: center; word-wrap: break-word;">900-1100</td><td style="text-align: center; word-wrap: break-word;">50</td></tr></table>

parts processed from new powders were labeled as S0, parts processed from first recycled powders as S1, i.e. Powders: R0, R1, R5, R10, R15, R30, R45, R70; Thin-walled samples: S0, S5, S10, S15, S30, S45, S70. The total duration of each EB-PBF building process is approximately 20 h. During this experiment, the filament state of the equipment was calibrated before building, and the model, process parameters, etc. were kept consistent for each cycling experiment.

A total of 30 kg of new powders were added to the hoppers on both sides, with approximately 5 kg of powders irradiated by EB during each sample building process. The loss during building and recycling was about 200 g, and each sampling and testing consumes about 100 g respectively. After the 30 cycles, 10 kg of new powders were mixed. The powders were mixed using a tilting mixer with a speed of 30 r/min, and the powders were mixed for 30–45 min under an inert gas atmosphere. The ratio of the number of building cycles to the remaining powders in the hopper that has not been irradiated can be calculated using the following formula:

 $$ T_{n+1}=T_{n}-M $$ 

 $$ N_{n+1}=N_{N}\times\frac{T_{n}-5}{T_{n}} $$ 

 $$ R_{n}=\frac{N_{n}}{T_{n}} $$ 

The remaining amount of new powders after n processing steps is  $ N_{n} $, the total remaining powder amount is  $ T_{n} $, the consumed powder amount is M, and M = 0.3 kg is required for sampling. The calculation results are shown in Fig. 1 (b), the remaining powder for furnace steps was M = 0.2 kg. After 15 cycles, the proportion of powders irradiated by EB exceeds 93%, while after 20 cycles the proportion of powders irradiated exceeds 97%. After 30 cycles, more than 99.6% of the powders were irradiated with EB at least once. Before the 31st building, mixed with 10 kg of new powders (from the original batch). Following remixing (termed R30b), the 31st building process (S30b) was conducted. Post-mixing, the new powders comprised approximately 30.3% of the mixture. By the 45th cycle, this ratio was reduced to 2.4%, decreased further to 0.04% by the 70th cycle.

The Ti-48Al-2Cr-2Nb parts were fabricated using EB-PBF equipment (Qbeam S200, Beijing Quick Beam Technology Co.) with a constant accelerating voltage of 60 kV. The layer thickness was 50  $ \mu $m, and the powder-bed temperature ranged from 900 ^\circC to 1150 ^\circC during building. Materialise Magics (version 24.0) was used for slice processing and model creation. More details on the EB-PBF process can be found in published paper [24] and Supporting Fig. 1 (S-Fig. 1). The dense building process for thin-walled parts is detailed in Table 1.

## 2.2. Characterization of microstructure

Powder morphology and particle size distribution were analyzed using a Zeiss Sigma360 SEM coupled with laser particle analysis (D10/D50/D90 parameters). Powder flowability and apparent density measured by Hall flowmeter (LICHEN, XF-02). High-resolution microstructural examination was conducted using a Zeiss SUPRA 55 field emission SEM in backscattered electron (BSE) mode (20 kV, WD = 10 mm) and electron back scatter diffraction (EBSD) analysis on a Zeiss Gemini 450 SEM (step sizes 0.8–2.5  $ \mu $m, 20 kV), with samples prepared by electrochemical polishing in a 5 % HClO $ _{4} $-35 % n-butanol-60 % methanol solution ( $ -30 $ ^\circC, 30 V). Transmission electron microscopy (TEM) investigations were carried out using FEI Tecnai Cube and aberration-corrected Titan G260-300 microscopes. Elemental composition was determined by SEM-EDS (Ti, Al, Cr, Nb, C), OH-300 oxygen analyzer, and X-ray Photoelectron Spectroscopy (XPS) depth profiling (Thermo Scientific K-Alpha, 30 mg samples). Phase analysis was performed using XRD (JADE 6.5 software) and EBSD (Aztec Crystal software), while bulk composition was measured via titration (Al) and ICP-AES (Cr, Nb).

## 2.3. Mechanical properties

Surface roughness (Ra, Eq. (4)) was measured using white light interferometry (MICROXAM-3D: Field of view range: 8 mm \times 10 mm, resolution: 752 \times 480 pixels, vertical scanning resolution: 0.01 nm.) and contact profilometry (Time-3233, U-diamond stylus: 5 \mum tip; 8 mm traverse). Profilometry adhered to DIN 4777 with Gaussian filtering (\lambdac = 0.8 mm, standard \lambdas). Parameters were evaluated over 8 mm sampling length. Instrument range: 800 \mum max, Vertical range: \pm 50 \mum. For EBPBF parts with significant surface variations, we combined both approaches: contact measurements for initial screening and optical analysis for detailed characterization of sidewall quality.

 $$ R a=\frac{1}{l_{a}}\int_{0}^{l_{a}}|Z(x)|d x $$ 

The Ra represents the arithmetic mean of the absolute ordinate  $ Z(x) $ within the sampling length( $ l_{a} $).

Samples for tensile testing were machined to dimensions of 12 mm gauge length, 2 mm width, and 1 mm thickness. The tensile specimen dimensions should refer to Fig. 2 (c). Tensile properties were evaluated using a YSL-100 quasi-static tensile testing machine with \pm 20 kN load capacity and strain rate of  $ 1 \times 10^{-4} $ s $ ^{-1} $ at RT.

## 3. Results and discussion

## 3.1. Powder characteristics

The particle size distribution curves, flowability, and apparent density of powders after multiple recycling cycles are shown in Fig. 2. Notably, significant property changes occurred after the first cycle, while the addition of fresh powder (R30b) broadened the particle size distribution (Fig. 2 a). Initial powder characterization revealed approximately 3 % sub-50  $ \mu $m fines and 5 % oversized particles (>150  $ \mu $m). During recycling, fine particles either agglomerated under electron beam irradiation or were removed by airflow in the powder recovery system (PRS), while oversized particles were eliminated through sieving. These processes narrowed the particle size distribution after the first cycle, improving uniformity (Fig. 2 b). The enhanced homogeneity increased flowability (Fig. 2 c) and elevated apparent density through the removal of large irregular particles (Fig. 2 d). After 15–30 recycling cycles, the particle size distribution continued to narrow, with 50–100
Fig. 2. Powder characteristics at different recycling cycles: (a) size distribution (The attached figure showed the particle size distribution after adding new powders), (b) D10, D50, and D90, (c) flowability, and (d) apparent density (All data points throughout this paper are presented as mean values from triplicate measurements, with error bars representing  $ \pm 1 $ standard deviation).

 $ \mu $m particles becoming predominant. The R30 powder exhibited a slight peak shift toward larger sizes compared to R15.

Interestingly, the addition of fresh powder (R30b) broadened the distribution range, with further broadening observed in R45 and R70. This phenomenon arises from two factors: (1) Fresh powder introduces fines (<50  $ \mu $m) and coarse particles (>100  $ \mu $m), broadening the distribution and shifting the peak toward smaller sizes; (2) With increasing cycles, elongated irregular-shaped particles formed through unidirectional fusion of fine powders evaded sieving. To further demonstrate this mechanism, SEM was used to characterize powders with different cycles.

The EIGA-produced powders exhibited high sphericity, with hollow and satellite particles being the primary defects in virgin powders (Fig. 3a-c). A small amount of irregular particles were observed in R1 and R5, while their abundance progressively increased from R15 to R70 (Fig. 3d-g), manifesting distinct morphologies (Fig. 3 h). At R15, two distinct types of irregular particles emerged: (1) fused satellite particles adhering to larger counterparts (Fig. 3 d, h2), and (2) particles with partial surface melting traces without complete fusion (Fig. 3 h3, h4). Rod-shaped particles dominated in R30 irregular particles (Fig. 3 e), while R45-R70 powders exhibited semi-molten agglomerates with elongated structures that evaded sieving despite exceeding nominal size thresholds. These morphological anomalies directly contributed to the broadening particle size distribution in R45 and R70, as elongated agglomerates (53–150 µm) and adhered fines (<50 µm) coexisted within the recycled powder system.

During powder recycling, EB irradiation and PRS fragmentation critically influenced particle size and morphology. The S-Fig. 2 systematically compares: Post-PRS powders exhibited a particle size shift toward smaller ranges (S-Fig. 2 a). Powders near melt zones showed larger sizes than distal regions (S-Fig. 2 b), with SEM confirming irregular oversized particles in melt-adjacent areas (S-Fig. 2b2-3). The results of the proportion of irregular powder in different furnaces (S-Table 1) indicate that the proportion of R45-R70 irregular powder is all greater than 30%.

## 3.2. Powder microstructures

During the powder recycling process, un-melted powders in the powder bed remained in a thermal environment of 900–1150 ^\circC continuously within the chamber, enduring an aging process for the un-melted powders. XRD characterization (Fig. 4) revealed changes in phase composition as the number of recycling cycles increased. Initially, the new powders consisted of \gamma and \alpha/\alpha₂ phases primarily, with the distinction between \alpha and \alpha₂ phases being challenging via XRD. Similar to findings by Guyon et al. [25] on Ti-48Al-2Cr-2Nb powders, which used ordered “super-\alpha₂” peaks to distinguish \alpha/\alpha₂ phases, the results by comparing the characteristic peaks showed that the initial powders were dominated by disordered \alpha and \gamma phases [26]. With increasing aging cycles, the \alpha phase content gradually decreased, while the proportion of \gamma phase increased. During the powder production process, the powder undergoes non-equilibrium solidification. Elevated temperatures significantly accelerate the diffusion rates of elements, with Al atoms (\alpha stabilizers) diffusing into the \alpha region and Nb and Cr (\beta stabilizers) diffusing into the \beta region [27,28]. Meanwhile, during the EB-PBF building process, a stable high-temperature environment leads to the transformation of metastable \alpha phases into stable \gamma + B_{2} phases.

Powders from different cycling stages were dissected and analyzed using BSE analysis and EDS line scanning, as shown in Fig. 5. The changes in surface elements of the powder are shown in S-Fig. 3. Initially, the powder particles exhibited a dendritic microstructure (Fig. 5 a) with dark solidification segregation (S-segregation) [28]
Fig. 3. 1ne secondary electron images of new powders and recycled powders: (a) new powders, (b) R1, (c) R5, (d) R15, (e) R30, (f) R45, (g) R70, (h) irregular powder, (h1) hollow powder (Ho-P, yellow circle), (h2) stick powder (St-P, orange circle) and satellite powder (Sa-P, green circle), (h3, h4) semi-melted powder (S-M P, red box), (h5, h6) adhesion powder (Ad-P, purple box). (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article).
Fig. 4. XRD and phase ratios of powders at different numbers of cycles: (a) new-R15 and (b) new-R70. The phase content is calculated using the Rietveld-Intensity Ratio (RIR) method.
Fig. 5. BSE images of powders at different numbers of cycles: (a) new powder, (b) R1-R15, (c) R30, (d) R45, (e) R70, (f) typical microstructures of powders, (g) line scan energy spectrum of typical microstructures of powders.

enriched in Al (Fig. 5 f1, g1) and bright  $ \beta $ segregation (Fig. 5 f1, g2) enriched in Ti and Cr [29,30].

In powders from R1 to R15 (Fig. 5 b), the  $ \alpha/\alpha_{2} $-phase gradually decreased with increasing recycling number, and the interdendritic  $ \gamma $-region expanded. By R30, the powder was predominantly composed of the  $ \gamma $-phase (Fig. 5 c), with S-segregation disappeared due to the high diffusion rate of Al at temperatures of approximately 900-1150 ^\circC (Fig. 5 f2). The bright dendritic structure caused by  $ \beta $ segregation transformed into a block-like morphology ( $ \alpha_{2} $) (Fig. 5 f2, f3).

After adding new powders (Fig. 5 d), three structures were observed. Some powder particles lost their dendritic structure completely, showing dispersed bright spots (Fig. 5 d) enriched with Cr, with decreased Ti and Al content. In R70 powders, irregularly shaped particles increased, along with powder particles containing aggregated bright spots (Fig. 5 e1, f4, g4). Microstructures of irregular powders like R70 were non-uniform due to varying Al loss during melting, resulting in uneven Al content within the powder and appearing as lamellar agglomerates ( $ \alpha_{2} + \gamma $) in Al-poor areas (Fig. 5 e2). Irregular powders were mainly caused by splashing or fusion of semi-molten powders in the heat radiation zone around the melt.

Titration analysis revealed the Al content evolution in recycled powders (Table. 2). Minimal Al loss (<0.5 at.%) occurred within 5 cycles, escalating to 1.62–2 at.% after 30 cycles with increased data fluctuations. Fresh powder addition in R30b reduced oxygen content and increased Al levels to 47.86 \pm 0.5 at.%, though significant variability persisted. Oxygen uptake progressed at 22 ppm/cycle during initial 15 cycles, accelerating to 27.33 ppm/cycle in cycles 15–30. Blending low/high-oxygen powders temporarily moderated oxygenation rates, achieving 48.12 at.% Al in R45, but subsequent cycles (\geq45) exhibited renewed oxygen increase (28 ppm/cycle), likely from accumulated irregular powders. Al depletion correlated strongly with electron beam (EB) exposure history. Below 10 cycles, high proportions of unirradiated powders (>30 %) minimized Al loss. Beyond 15 cycles, >93 % of powders underwent EB irradiation, with repeated exposures inducing progressive Al volatilization. Post-R30b processing restored unirradiated powder ratios to ~ 30 %, yet Al content fluctuations (\pm0.5 at.%) remained pronounced. Extreme variations emerged at R70, with Al content spanning 42.12– 49.52 at.%, reflecting heterogeneous irradiation and melting histories across particles.

In the EB-PBF building process, the generation of irregular shaped powders in the reused powder mainly occurs in the following two processes (Fig. 6 a): 1) During the preheating process of the powder bed, the defocused EB heats the powder bed to 950–1150 ^\circC, and the powder bed presents a pseudo-sintered state. This state is characterized by interparticle neck formation without complete melting [32]. During the irradiation process of defocused EB, there is charge transfer and heat

Table 2 O and Al content in powders.

|  | New | R1 | R5 | R15 | R30 | R30b | R45 | R70 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| O (ppm) | 560 | 580 | 660 | 890 | 1200 | 860 | 1300 | 2000 |
| Al (at. %) | 48.43 | 48.47 | 48.32 | 47.24 | 46.81 | 47.86 | 47.12 | 46.31 |
|  | $ \pm 0.12 $ | $ \pm 0.2 $ | $ \pm 0.2 $ | $ \pm 0.1 $ | $ \pm 0.7 $ | $ \pm 0.5 $ | $ \pm 0.6 $ | $ \pm 3 $ |
Fig. 6. Possible sources of irregular powder during the building process, (a) Single track scanning process captured by high-speed camera; (b) Heat transfer and charge transfer between powders during powder bed preheating process; (c) Multi physics field simulation of single-track scanning; (d) Schematic diagram of the formation of irregular powder after multiple irradiation.

transfer between powders (Fig. 6 b). The smaller the particle size, the more likely it is to form sintering necks, and pseudo connections may also occur between larger particles during heat transfer. 2) As shown in Fig. 6 (a), (c), there is a large amount of partially melted powder on both sides of the scanning track, which adheres to the side surface of the parts after building and is peeled off and mixed into the powder during PRS processing. Meanwhile, during the continuous scanning process, the molten pool is easily affected by Plateau-Rayleigh instability, causing splashing. The splashed molten material falls into the powder bed and forms slag. Some of the molten material merges with spherical powder to form irregular shaped powder similar to Fig. 3 (h3, h4) and Fig. 5 (e1).

Complementary XPS (S-Figs. 4, 5) and TEM (S-Fig. 6) analyses revealed the coupled evolution of surface oxides and internal phase transformations during powder recycling. XPS demonstrated a progressive transition from mixed TiO₂/Al₂O₃ (46.02%/53.98%) to Al₂O₃-dominated (82.11%) surface oxides after 70 cycles, accompanied by Ti³⁺/Cr³⁺ enrichment and Al-O peak shifts (531.75 \rightarrow 532.02 eV), indicative of oxide densification (S-Figs. 4, 5). TEM characterization (S-Figs. 6, 7) correlated these changes with microstructural evolution: virgin powders exhibited homogeneous \alpha-phase structures, while cycled powders developed Cr-Ti Laves phases (10–20 nm at R15) and Ti-Nb-Cr precipitates (R70). FIB-TEM mapping (S-Figs. 6, 7) further identified three critical features: (1) distinct oxide layers in R15/R30 powders with Cr enrichment at oxide/matrix interfaces, (2) Ti/O-rich regions at R70 particle edges despite lacking continuous oxide films, and (3) progressive \gamma-phase coarsening with cycling (\alpha₂+\gamma dendrites \rightarrow equiaxed \gamma grains). These observations collectively demonstrate that EB-PBF’s thermal cycling (900–1150 ^\circC) simultaneously drives surface oxidation (Al₂O₃ stabilization) and solid-state phase transformations (\alpha \rightarrow \gamma + B_{2} \rightarrow Laves), with Cr segregation acting as the bridge between surface chemistry and bulk precipitation.

## 3.3. Part performance and microstructure analysis

During powders recycling, the chemical composition may change as elements were lost or gained during the building process, significantly impacting the microstructure and mechanical properties of the final part. Table 3 showed the chemical composition of the final parts. The O content in the powders gradually increased with cycling, exceeding 800 ppm in R30. In the samples, O content also increased gradually but at a slower rate compared to the powders. At higher recycling cycles, the O content in the samples remained significantly lower than in the powder. Recycling had little effect on the Cr and Nb content in the samples, both fluctuating around 2 at.\%. Similar to the change in Al content of the powders, the Al content of the thin-walled samples also showed a significant decrease at S_{15}.

XRD and SEM analyses of samples (S_{0}-S_{70}) revealed microstructural evolution. In Fig. 7 (a), XRD analysis revealed  $ \gamma $ and  $ \alpha_{2} $ phases in all samples, with characteristic peaks of the  $ \beta_{0}/B_{2} $ (Cr-Ti) phase appearing prominently in S_{30} to S_{70}, particularly in S_{70}. BSE analysis (Fig. 7 b) showed equiaxed  $ \gamma $ grains, fine lamellar colonies ( $ \alpha_{2} + \gamma $), and dispersed bright spots ( $ \beta_{0}/B_{2} $) along lamellar colony boundaries across S_{0} to S_{70}. As the cycle number increased, the microstructures exhibited an increased presence of bright spots. The addition of new powders slightly reduced the number of bright spots in S30b and S_{45}. For S_{70}, these spots grew larger and transformed from point-like to irregular agglomerations. Furthermore, they were found not only inside lamellar colonies but also in the  $ \gamma $ bulk in S_{30} and S_{70}. In addition, more pronounced lamellar clusters were observed in S_{15}, S30b, and S_{45}, while the S_{0}, S_{5}, S_{10} and S3b exhibited distinct “ $ \gamma $ bands” with annealed twins.

Table 3

Chemical composition of samples with different recycling cycles.

| Elements |  | S_{0} | S_{5} | S_{10} | S_{15} | S_{30} | S30b | S_{45} | S_{70} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| O (ppm) | part | 680 | 680 | 730 | 740 | 860  $ \pm $ 10 | 760  $ \pm $ 15 | 900 | 940  $ \pm $ 40 |
| Al (at.%) | part | 47.51 | 47.67 | 47.56 | 46.95 | 46.89  $ \pm $ 0.6 | 47.56  $ \pm $ 0.2 | 47.35 | 47.04  $ \pm $ 0.5 |
| Cr (at.%) | part | 2.12 | 2.03 | 1.98 | 1.92 | 2.02 | 2.14 | 1.98 | 1.83 |
| Nb (at %) | part | 2.04 | 2.04 | 2.04 | 2.06 | 2.01 | 2.03 | 2.04 | 1.99 |
Fig. 7. Thin-walled microstructure at different number of cycles: (a) XRD, (b) SEM analyses, (c) Isopleth section of Ti-48Al-2Cr-2Nb alloy phase diagram: The black dashed line indicates the range of possible Al content in the powder, the red dashed line indicates the Al content of the formed block, and the green dashed line indicates the temperature range of the building process. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

Thermo-Calc and compositional data (Table 3, Fig. 7 c) predicted the solidification path: L\rightarrow(L + \beta) \rightarrow (\alpha + L) \rightarrow (\alpha) \rightarrow (\alpha + \gamma) \rightarrow (B_{2} + \gamma) [33,34]. The high cooling rates (10⁵–10⁶ K/s) and pronounced localized thermal gradients inherent to EB-PBF significantly intensify non-equilibrium solidification phenomena. These localized thermal inputs induce deviations in melt pool solidification behavior from equilibrium pathways [35]. Post-solidification, the elevated thermal environment of EB-PBF promotes partial transformation of metastable phases (e.g., \beta₀/B_{2} or \alpha/\alpha₂ phases) toward equilibrium configurations (\gamma phases) [36]. However, rapid cooling rates and complex thermal histories in EB-PBF may lead to partial retention of non-equilibrium phases (e.g., \beta₀/B_{2} or C_{14} Laves phases), particularly in the absence of sufficient post-process heat treatment. Such residual non-equilibrium phases can critically influence material performance, including strength and toughness, by altering dislocation dynamics and interfacial cohesion mechanisms.

XRD and BSE results showed that the primary phases in bulk samples S_{0}-S_{15} were  $ \alpha_{2} $ and  $ \gamma $. The  $ \beta $/Laves phase peaks appeared in XRD patterns for bulk samples S_{30}, S_{45}, and S_{70}, although their content was too low to be detected by XRD and only observed in the duplex region of BSE images. EB-PBF’s deep melt pools (exceeding layer thickness) induced remelting and Al loss [37,38]. This resulted in different solidification paths for initial melting and remelting. For new powders with an assumed Al content of 47.5–48.5 at.\%, the solidification path during cooling to ambient temperature was  $ L \rightarrow (L + \beta) \rightarrow (\alpha + L) \rightarrow (\alpha) \rightarrow (\alpha + \gamma) \rightarrow (\gamma (48-48.5 \text{ at.\% Al})) / (B_{2} + \gamma (47.5-48 \text{ at.\% Al})) $ for 900–1150 ^\circC. With a 1 % Al loss in a single remelting process, the path changed to  $ L \rightarrow (L + \beta) \rightarrow (\alpha + L) \rightarrow (\alpha) \rightarrow (\alpha + \gamma) \rightarrow (\alpha + \gamma + B_{2}) \rightarrow (\alpha_{2} + \gamma + B_{2}) < 47 \text{ at.\% Al}) $. Increasing powder recycling cycles further reduced Al content and the predominant phase became  $ \alpha_{2} + \gamma + B_{2} $. With new powders added to R30b, the  $ \gamma $ band reappeared in the S30b thin-wall, while the Al content of powders being 47.86 at.\%. In bulk structures of S_{45} and S_{70}, the  $ \gamma $ bands were barely visible, while content of spheroidized and agglomerated  $ \beta_{0}/B_{2} $ phase increases. During subsequent high-temperature exposure in EB-PBF, TiAl alloys undergo thermal cycling (e.g., interlayer reheating or prolonged thermal exposure), which provides kinetic conditions for the transformation of metastable phases toward equilibrium states. Prolonged thermal cycling (>300 h at 900–1150 ^\circC, near  $ \alpha_{2}+\gamma + B_{2} $ phase field) accelerated phase transformations. For instance, prolonged aging at 1100 ^\circC facilitates the decomposition of metastable  $ \alpha_{2} $ phases into equilibrium  $ \gamma + B_{2} $ mixtures,

while Cr-rich C_{14} Laves phases nucleate preferentially at  $ \alpha_{2}/\gamma $ interfaces under near-equilibrium conditions [39].

EBSD analysis (Fig. 8 a, b) revealed pronounced  $ \gamma $ bands in the microstructure of S_{0}, S_{5}, S_{10}, and S_{30}, but not in S_{15}, S_{45}, and S_{70}. The  $ \beta_{0}/B_{2} $ phase primarily distributed near grain boundaries (Fig. 8 b). Statistical data (Fig. 8 c) showed an increasing  $ \beta_{0}/B_{2} $ phase content in thin-walled structures after multiple powder cycles (S_{0} to S_{30}), with a decrease observed after the addition of new powders. The  $ \beta_{0}/B_{2} $ phase content reached 4.6 % in S_{70}. Grain size analysis (Fig. 8 d) indicated excellent uniformity in grain size for both S_{15} and S_{70}, with average sizes less than 10  $ \mu $m, and S_{70} exhibiting even finer grains. Kernel average misorientation (KAM) diagram reveals residual stress and uneven deformation in 3D printed parts. Comparing KAM and grain boundaries maps of S_{0}, S_{15}, and S_{70} (Fig. 8 e), uneven KAM distributions were observed, with S_{0} exhibiting values up to 4.97 and high KAM values in the duplex phase regions, low-angle grain boundaries (LAGB) and high-angle grain boundaries (HAGB), which accounted for 94.8 % of the total. No stress concentration was observed near  $ \gamma $ bands but numerous  $ \gamma $ [110]70^\circ twin boundaries were present. The layer-by-layer EB-PBF process induced localized heating and rapid cooling, generating thermal stresses that activated twinning deformation to reduce overall stress levels [31]. Similarly, non-uniform KAM distributions (max 4.99) in S_{15} and S_{70} were attributed to the layer-by-layer printing nature. S_{70} exhibited more regions with high KAM values compared to S_{15}, accompanied by significant LAGB presence. In S_{15} and S_{70}, LAGB accounted for 7.40 % and 8.15 %, respectively, exceeding the 5.2 % in S_{0}. In addition, both S_{15} and S_{70} exhibited more special boundaries in the  $ \gamma $ [111] 60^\circ plane compared to S_{0}. Meanwhile,
Fig. 8. EBSD analysis: (a, b) Phase map. (c) Phase content statistics. (d) Grain size statistics (number of grains > 2000). (e) Distribution of KAM, grain boundaries, and special boundaries; (e1) KAM, grain boundaries, and special boundaries of the S_{0}, S_{15}, S_{70}, (e2) Statistical of grain boundaries and special boundaries.

the proportion of twin boundaries of  $ \gamma $ [110]70^\circ, predominantly within equiaxial  $ \gamma $ crystals, decreased from 12.5 % in S0 to 5.61 % in S70.

To further analyze the thin-wall microstructure, TEM analysis was performed on S_{0}, S_{15}, and S_{70}. Fig. 9 (a1, a2) showed that the dual-phase structure of S_{0} consisted of lamellar colonies ( $ \alpha_2 + \gamma $) and equiaxed  $ \gamma $ grains. Additionally, cubic  $ \beta_0/B_2 $ phase was observed between the lamellar colonies and  $ \gamma $ grain boundaries, as shown in Fig. 9 (b, c). Scanning the bright lines in the lamellar colonies and  $ \gamma $ grains revealed a Ti-rich, Al-poor phenomenon. For S_{15} and S_{70}, a dual-phase structure was still present. Calibration of the diffraction spots of the bright aggregates suggested a composition primarily of cubic Cr-Ti (Cr_{1.93}Ti_{1.07}, C_{15} Laves phase, Fig. 9 b2). As shown in Fig. 9 (a-c), the precipitated phase in S_{0} differed from that in S_{15} and S_{70}. In S_{0}, sub-micron-sized precipitates were distributed between the equiaxed  $ \gamma $ grains and the lamellar colonies and had a  $ \beta_0/B_2 $ phase structure. In S_{15}, there was a predominance of Ti and Cr without significant enrichment of Al and Nb elements. The precipitated phase in S_{70} reached 2 – 3  $ \mu $m in size, with a notable depletion of Al and enrichment of Ti, Cr, and Nb, corresponding to TiNbCr4 (C_{14} Laves phase) in composition. In contrast, the precipitates in S_{15} were mainly dispersed around the boundaries and within the  $ \alpha_2 $ regions of the lamellar colonies.

To understand the possible reasons, examining the simplified projection of the Ti–Al–Cr ternary phase diagram (pseudo-ternary phase diagram) is useful [33,34]. Babu et al. [40] equated the 2 at.% Nb content in Ti-48Al-2Cr-2Nb to the Cr content, discovering that \gamma phase coexisted with 4 mol% B_{2} phase and less than 2 mol% \alpha₂-phase at 800 ^\circC. During high cooling rate non-equilibrium solidification, excessive \alpha₂ formed, creating a strong driving force to reduce its content, leading to the generation of the B_{2} phase at the expense of \alpha₂ after thermal exposure [41]. In this study, based on the pseudo-ternary phase diagram, it was found that at 950 ^\circC, a miscibility gap region formed in the BCC region, leading to the formation of a three-phase field consisting of C_{15} Laves + \alpha₂ + \beta (Ti) and C_{15} Laves + \alpha₂ + B_{2} [39]. Cr exhibits higher diffusivity in \alpha₂-Ti₃Al (DCr² = 1.2 \times 10⁻¹⁶ m²/s at 1100 ^\circC) than in \gamma-TiAl (DCr³ 3.8 \times 10⁻¹⁷ m²/s), driving preferential accumulation at \alpha₂/\gamma interfaces [42]. During the building process, regions with BCC structure may contain the C_{15} Laves phase, explaining the presence of the \alpha₂ phase coexisting with the \beta₀/B_{2} phase in the EBSD analysis (Fig. 8) and the occurrence of the C_{15} Laves phase between \alpha₂ plates observed in TEM (Fig. 9 b).

The stress–strain curves of the samples are shown in Fig. 10 (a). Plasticity initially rose and then declined, with S_{15} exhibiting the highest plasticity. The elimination of large-scale \gamma-band structures enhanced microstructural homogeneity, mitigating localized stress concentrations (Fig. 8 e). Furthermore, the proliferation of true twin boundaries acted as potent dislocation sources, activating additional slip systems (e.g., {111}⟨110⟩ in \gamma-phase) and thereby improving crystallographic slip capability. The tensile strength ranged between 682 and 750 MPa, with S_{70} showing the highest strength. Although S_{70} exhibited superior tensile strength, two parallel specimens experienced brittle fracture, attributed to the combined effects of elevated irregular powder content and associated oxygen contamination (>2000 ppm). Excessive oxygen doping significantly degraded room-temperature ductility, as evidenced by the 60 % reduction in elongation (2.1 %-0.8 %). EBSD and BSE analyses revealed substantial grain refinement in S_{70}, with over 60 % of grains measuring < 5 \mum (Fig. 8 d). Grain refinement originates from heterogeneous nucleation, where partially unmelted powders in the melt pool (especially chromium rich aggregates from recycled powders) and in-situ formed second phases (such as TiCr₂, Al₂O₃) serve as effective nucleation sites. The Hall-Petch strengthening effect from grain refinement, coupled with the Orowan strengthening by submicron intergranular precipitates, collectively contributed to the enhanced strength. However, the resultant grain boundary proliferation and oxide dispersion simultaneously embrittled the material, explaining the observed brittle fractures in high-oxygen specimens. Quantitative analysis established that each 0.1 at.% Al loss (0.05–0.08 at.%/cycle) increased tensile strength by 3.2 \pm 0.5 MPa but reduced ductility by 0.8 \pm 0.2 %, with critical degradation occurring beyond 1.5 at.% Al loss (30 cycles). EBSD revealed a 1.2 vol% Laves phase increase per 0.1 at.% Al loss, exacerbated by oxygen (12 % effect amplification per 100 ppm).

The mechanical properties of thin-walled samples showed significant fluctuations after adding new powder, i.e. the elongation of S30b was improved compared to S30. The side surface roughness of thin-walled samples (Fig. 10 b) showed a gradual increasing trend. In addition, the white light interference 3D images of the side surfaces of different thin walls in S-Fig. 8 show that more fusion lines and abnormal convex points appear on the surface in S70. The synergistic effects of Al depletion and O enrichment govern microstructural evolution in EB-PBF. Al loss dictates solidification pathways while O ingress promotes
Fig. 9. TEM analysis: (a) S_{0}, (b) S_{15}, (c) S_{70}; (a1-c1) precipitates in bright-field TEM image; (a2-c2) diffraction pattern from the precipitates; (a3-c6) elemental mapping.
Fig. 10. Variations in room temperature mechanical properties and lateral surface roughness of samples prepared from powders with different numbers of cycles: (a) stress–strain curves; the attached table showed the average values for three parallel specimens (x indicates the presence of brittle rupture). (b) Lateral surface roughness of different thin wall samples.

Laves phase precipitation. Thermal cycling drives these phase transformations, necessitating maintenance of 15–30 % fresh powder to control powder degradation and Laves phase accumulation. This strategy effectively mitigates property variations between production batches.

## 4. Conclusions

This study examined the changes in particle size distribution, morphology, chemical composition, and phase constituents of Ti-48Al-2Cr-2Nb alloy powders after up to 70 recycling cycles and their impact on the microstructure and mechanical properties of the TiAl alloy. The feasibility of powder recycling for preparing TiAl alloy using EB-PBF technology was analyzed, providing guidance for improving powder utilization and reducing production costs. The key findings are as follows:

• With more cycles, the oxide film on the powder surface transitioned from a loose TiO₂ + Al₂O₃ composite to predominantly dense Al₂O₃. The alloy phases within the powder shifted from primarily \alpha/\alpha₂ phase to predominantly \gamma phase.

- The rapid solidification in the EB-PBF process promoted  $ \alpha_{2} $ phase formation. However, prolonged thermal exposure at 900-1150 ^\circC during EB-PBF caused the  $ \alpha_{2} $ phase degrade to B_{2} phase. This thermal exposure occurred within a three-phase region, leading to C_{15} Laves phase formation and affecting Cr segregation, disrupting equilibrium of B_{2} phase and promoting formation of C_{14} Laves phase.

- RT ultimate tensile strength and yield strength of thin-walled components increased with increasing number of powder recycling cycles, while ductility decreased. These changes in properties were attributed to enhanced microstructure homogeneity and increased Laves phase/B_{2} phase content.

- The synergistic effects of Al depletion and O enrichment govern microstructural evolution in EB-PBF TiAl alloys. Maintaining 15–30% fresh powder with  $ \leq $ 30 recycling cycles effectively controls Laves phase (<4 vol%) and Al fluctuation ( $ \Delta Al < 1.2 $ at.%), ensuring batch consistency.

## CRediT Authorship

Feihong Wang: Writing – review & editing, Writing – original draft, Formal analysis, Data curation, Conceptualization. Mengchen Song: Formal analysis, Data curation. Yongfeng Liang: Writing – review & editing, Writing – original draft, Project administration, Funding acquisition, Formal analysis. Gengwu Ge: Validation, Investigation, Formal analysis. Xiaoyu Liang: Writing – review & editing, Project administration, Funding acquisition, Data curation. Feng Lin: Validation, Supervision, Project administration, Formal analysis. Honghui Wu: Visualization, Validation, Software. Dongfang Wang: Formal analysis, Data curation. Wenbin Kan: Resources, Methodology. Li Liu: Supervision, Resources, Project administration. Junpin Lin: Writing – review & editing, Resources, Funding acquisition, Formal analysis, Conceptualization.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

This work was supported by the National Key R&D Program of China [grant number 2021YFB3700501]; the National Science and Technology Major Project of China (grant number J2019-VII-0016-0156); the Defense Industrial Technology Development Program (grant number JCKY2022204B008); the Funds for Creative Research Groups of China (grant number 51921001); the NSFC (National Natural Science Foundation of China)-DFG (Deutsche Forschungsgemeinschaft) Joint Research Program (Grant No. 52061135113) and the State Key Laboratory for Advanced Metals and Materials of China (grant number 2022Z-03).

## Appendix A. Supplementary data

## Supplementary Material

## Data Availability

No data was used for the research described in the article.

## References

[1] T.L. Zhang, C.T. Liu, Design of titanium alloys by additive manufacturing: a critical review, Adv. Powder Mater. 1 (1) (2022) 100014, https://doi.org/10.1016/j.apmate.2021.11.001.

[2] M. Reith, M. Franke, M. Schloffffer, C. Körner, Processing 4th generation titanium aluminides via electron beam based additive manufacturing characterization of microstructure and mechanical properties, Materialia 14 (2020) 100902, https://doi.org/10.1016/j.mtla.2020.100902.

[3] J.C. Wang, R. Zhu, Y.J. Liu, L.C. Zhang, Understanding melt pool characteristics in laser powder bed fusion: an overview of single- and multi-track melt pools for process optimization, Adv. Powder Mater. 2 (4) (2023) 100137, https://doi.org/10.1016/j.apmate.2023.100137.

[4] Anon, GE aviation invests in EBM, Met. Powder Rep. 74 (5) (2019) 272, https://doi.org/10.1016/j.mprp.2019.07.036.

[5] M. Reith, M. Franke, M. Schloffer, C. Körner, Processing 4th generation titanium aluminides via electron beam based additive manufacturing – characterization of microstructure and mechanical properties, Materialia 14 (11) (2020) 100902, https://doi.org/10.1016/j.mtla.2020.100902.

[6] A. Emiralioglu, R. Ünal, Additive manufacturing of gamma titanium aluminide alloys: a review, J. Mater. Sci. 57 (7) (2022) 4441–4466, https://doi.org/10.1007/s10853-022-06896-4.

[7] C. Körner, Additive manufacturing of metallic components by selective electron beam melting - a review, Int. Mater. Rev. 61 (5) (2016) 361–377, https://doi.org/10.1080/09506608.2016.1176289.

[8] Y. Li, et al., Microstructure, mechanical properties and strengthening mechanisms of IN738LC alloy produced by Electron Beam Selective Melting, Addit. Manuf. (2021) 47, https://doi.org/10.1016/j.addma.2021.102371.

[9] A. Chiba, Y. Daino, K. Aoyagi, K. Yamanaka, Smoke suppression in electron beam melting of inconel 718 alloy powder based on insulator–metal transition of surface, Materials 14 (2021), https://doi.org/10.3390/ma14164662.

[10] B. Liu, M. Wang, Y. Du, J. Li, Size-dependent structural properties of a high-Nb TiAl alloy powder, Materials 13 (2020) 1–7, https://doi.org/10.3390/ma13010161.

[11] Y. Li, et al., Microstructures and mechanical properties evolution of IN939 alloy during electron beam selective melting process, J. Alloy. Compd. (2021) 883, https://doi.org/10.1016/j.jallcom.2021.160934.

[12] G. Shanbhag, M. Vlasea, The effect of reuse cycles on Ti-6Al-4V powder properties processed by electron beam powder bed fusion, Manuf. Lett. 25 (2020) 60–63, https://doi.org/10.1016/j.mfglet.2020.07.007.

[13] A. Montelione, S. Ghodsa, R. Schura, C. Wisdom, D. Arola, M. Ramulu, Powder reuse in electron beam melting additive manufacturing of Ti6Al4V: particle microstructure, oxygen content and mechanical properties, Addit. Manuf. 35 (2020) 101216, https://doi.org/10.1016/j.addma.2020.101216.

[14] P. Wang, M.L.S. Nai, F.L. Ng, A. Tan, W.J. Sin, M.H. Goh, Y. Maruno, Revealing mechanisms underlying powder reusability of Ti-48Al-2Cr-2Nb intermetallic in electron beam powder bed fusion process, Addit. Manuf. 59 (2022) 103155, https://doi.org/10.1016/j.addma.2022.103155.

[15] N.E. Gorji, R. O'Connor, A. Mussatto, S. Matthew, P.G.M. González, D. Brabazon, Recyclability of stainless steel (316 L) powder within the additive manufacturing process, Materialia 8 (2019) 100489, https://doi.org/10.1016/j.mtla.2019.100489.

[16] W.B. Kan, B. Chen, C. Jin, H. Peng, J.P. Lin, Microstructure and mechanical properties of a high Nb-TiAl alloy fabricated by electron beam melting, Mater Design. 160 (2018) 611–623, https://doi.org/10.1016/j.matdes.2018.09.044.

[17] R.R. Xu, M.Q. Li,  $ \gamma \rightarrow \beta $ phase transformation in Ti-42.9Al-4.6Nb-2Cr, Intermetallics 133 (2021) 107169. https://doi.org/10.1016/j.intermet.2021.107169.

[18] R.R. Xu, M.Q. Li, Y.H. Zhao, A review of microstructure control and mechanical performance optimization of  $ \gamma $-TiAl alloys, J. Alloys Compd. 932 (2023) 167611, https://doi.org/10.1016/j.jallcom.2022.167611.

[19] L. Wang, C. Shen, Y.L. Zhang, F. Li, Y. Huang, Y.H. Ding, J.W. Xin, W.L. Zhou, X.M. Hua, Effect of Al content on the microstructure and mechanical properties of  $ \gamma $-TiAl alloy fabricated by twin-wire plasma arc additive manufacturing system, Mater. Sci. Eng. A 826 (2021) 142008, https://doi.org/10.1016/j.msea.2021.142008.

[20] M.S. Wang, E.W. Liu, Y.L. Du, T.T. Liu, W.H. Liao, Cracking mechanism and a novel strategy to eliminate cracks in TiAl alloy additively manufactured by selective laser melting, Scr. Mater. 204 (2021) 114151, https://doi.org/10.1016/j.scriptamat.2021.114151.

[21] Y.Y. Chen, H.Y. Yue, X.P. Wang, S.L. Xiao, F.T. Kong, X.K. Cheng, H. Peng, Selective electron beam melting of TiAl alloy: microstructure evolution, phase transformation and microhardness, Mater Charact 142 (2018) 584–592, https://doi.org/10.1016/j.matchar.2018.06.027.

[22] M. Todai, T. Nakano, T. Liu, H.Y. Yasuda, K. Hagihara, K. Cho, M. Ueda, M. Takeyama, Effect of building direction on the microstructure and tensile properties of Ti-48Al-2Cr-2Nb alloy additively manufactured by electron beam melting, Addit. Manuf. 13 (2017) 61–70, https://doi.org/10.1016/j.addma.2016.11.001.

[23] K. Cho, H. Kawabata, T. Hayashi, H.Y. Yasuda, H. Nakashima, M. Takeyama, T. Nakano, Peculiar microstructural evolution and tensile properties of  $ \beta $-containing  $ \gamma $-TiAl alloys fabricated by electron beam melting, Addit. Manuf. 46 (2021) 102091, https://doi.org/10.1016/j.addma.2021.102091.

[24] F.H. Wang, C.C. Wu, Y.F. Liang, X.Y. Liang, H.H. Wu, L. Liu, F. Lin, W.B. Kan, J.P. Lin, A surface quality optimization strategy based on a dedicated melt-pool control via the dashed-scan contouring technique in electron beam powder bed fusion, J. Mater. Process. Technol. 330 (2024) 118445, https://doi.org/10.1016/j.jmatprotec.2024.118445.

[25] J. Guyon, A. Hazotte, E. Bouzy, Evolution of metastable a phase during heating of Ti48Al2Cr2Nb intermetallic alloy, J. Alloys Compd. 656 (2016) 667–675, https://doi.org/10.1016/j.jallcom.2015.09.179.

[26] C. Schuh, D.C. Dunand, Transformation superplasticity of super  $ \alpha_{2} $ titanium aluminide, Acta Mater. 46 (16) (1998) 5663–5675, https://doi.org/10.1016/S1359-6454(98)00252-3.

[27] S.J. Qu, S.Q. Tang, A.H. Feng, C. Feng, J. Shen, D.L. Chen, Microstructural evolution and high-temperature oxidation mechanisms of a titanium aluminide based alloy, Acta Mater. 148 (2018) 300–310, https://doi.org/10.1016/j.actamat.2018.02.013.

[28] G.L. Chen, X.J. Xu, Z.K. Teng, Y.L. Wang, J.P. Lin, Microsegregation in high Nb containing TiAl alloy ingots beyond laboratory scale, Intermetallics 15 (5–6) (2007) 625–631, https://doi.org/10.1016/j.intermet.2006.10.003.

[29] R.X. Ma, Z.Q. Liu, W.B. Wang, G.J. Xua, W. Wang, Microstructures and mechanical properties of Ti6Al4V-Ti48Al2Cr2Nb alloys fabricated by laser melting deposition of powder mixtures, Mater Charact 164 (2020) 110321, https://doi.org/10.1016/j.matchar.2020.110321.

[30] J. Guyon, A. Hazotte, F. Wagner, E. Bouzy, Recrystallization of coherent nanolamellar structures in Ti48Al2Cr2Nb intermetallic alloy, Acta Mater. 103 (2016) 672–680, https://doi.org/10.1016/j.actamat.2015.10.049 Get rights and content.

[31] J. Schwerdtfeger, C. Körner, Selective electron beam melting of Ti-48Al-2Nb-2Cr: microstructure and aluminium loss, Intermetallics 49 (2014) 29–35, https://doi.org/10.1016/j.intermet.2014.01.004.

[32] F. Wakai, K.A. Brakke, Mechanics of sintering for coupled grain boundary and surface diffusion, Acta Mater. 59 (14) (2011) 5379–5387, https://doi.org/10.1016/j.actamat.2011.05.006.

[33] V. Raghavan, Al-Cr-Ti (Aluminum-Chromium-Titanium), J. Phase Equilib. Diffus. 26 (2005) 349–356.

[34] V. Raghavan, Al-Cr-Ti-Nb (Aluminum-Chromium-Niobium-Titanium), J. Phase Equilib. Diffus. 26 (2005) 370.

[35] X.Y. Zhang, C.W. Li, M.H. Wu, Z.H. Ye, Q. Wang, J.F. Gua, Atypical pathways for lamellar and twinning transformations in rapidly solidified TiAl alloy, Acta Mater. 227 (2022) 117718, https://doi.org/10.1016/j.actamat.2022.117718.

[36] L.E. Murr, S.M. Gaytan, A. Ceylan, E. Martinez, J.L. Martinez, D.H. Hernandez, B.I. Machado, D.A. Ramirez, F. Medina, S. Collins, R.B. Wicker, Characterization of titanium aluminide alloy components fabricated by additive manufacturing using electron beam melting, Acta Mater. 58 (5) (2010) 1887–1894, https://doi.org/10.1016/j.actamat.2009.11.032.

[37] B. Gao, H. Peng, H. Yue, H. Guo, C. Wang, B. Chen, Electron beam powder bed fusion of Y₂O₃/\gamma-TiAl nanocomposite with balanced strength and toughness, Addit. Manuf. 72 (2023) 103650, https://doi.org/10.1016/j.addma.2023.103650.

[38] J. Knörlein, M.M. Franke, M. Schloffer, C. Körner, In-situ aluminum control for titanium aluminide via electron beam powder bed fusion to realize a dual microstructure, Addit. Manuf. 59 (2022) 103132, https://doi.org/10.1016/j.addma.2022.103132.

[39] Z.C. Xie, D. Chauraud, E. Bitzek, S. Korte-Kerzel, J. Guénolé, Laves phase crystal analysis (LaCA): atomistic identification of lattice defects in C_{14} and C_{15} topologically close-packed phases, J. Mater. Res. 36 (2021) 2010–2024, https://doi.org/10.1557/s43578-021-00237-y.

[40] R.P. Babu, S. Karthikeyan, Effect of stress orientation on microstructural evolution during creep of near-lamellar Ti–47Al–2Cr–2Nb, Mater. Sci. Eng. A 564 (2013) 218–231, https://doi.org/10.1016/j.msea.2012.10.033.

[41] Z.W. Huang, W. Voice, P. Bowen, Thermal exposure induced  $ \alpha_{2}+\gamma\rightarrow B_{2}(\omega) $ and  $ \alpha_{2}\rightarrow B_{2}(\omega) $ phase transformations in a high Nb fully lamellar TiAl alloy, Scripta Mater. 48 (1) (2003) 79–84, https://doi.org/10.1016/S_{1359}-6462(02)00350-0.

[42] C. Herzig, T. Przeorski, M. Friesel, F. Hisker, S. Divinski, Tracer solute diffusion of Nb, Zr, Cr, Fe, and Ni in  $ \gamma $-TiAl: effect of preferential site occupation, Intermetallics 9 (6) (2001) 461–472, https://doi.org/10.1016/S0966-9795(01)00025-5.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

Materials & Design 257 (2025) 114473

Materials & Design

a State Key Laboratory for Advanced Metals and Materials, University of Science and Technology Beijing, Beijing 100083, China  
b Department of Mechanical Engineering, Tsinghua University, Beijing 100084, China  
c Beijing Quick Beam Technology Co., Ltd., Beijing 100176, China

## Keywords
Electron beam powder bed fusion
Powder recycling
TiAl alloy
Thermal exposure
Mechanical properties
## ABSTRACT
☆ This article is part of a special issue entitled: ‘Additive Manufacturing’ published in Materials & Design.
## CRediT Authorship
## Declaration of Competing Interest
## Supplementary Material
## Data Availability

## ABSTRACT

https://doi.org/10.1016/j.matdes.2025.114473 0264-1275/© 2025 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY-NC license (http://creativecommons.org/licenses/by-nc/4.0/). Samples for tensile testing were machined to dimensions of 12 mm gauge length, 2 mm width, and 1 mm thickness. The tensile specimen dimensions should refer to Fig. 2 (c). Tensile properties were evaluated using a YSL-100 quasi-static tensile testing machine with \pm 20 kN load capacity and strain rate of  $ 1 \times 10^{-4} $ s $ ^{-1} $ at RT. In the EB-PBF building process, the generation of irregular shaped powders in the reused powder mainly occurs in the following two processes (Fig. 6 a): 1) During the preheating process of the powder bed, the defocused EB heats the powder bed to 950–1150 ^\circC, and the powder bed presents a pseudo-sintered state. This state is characterized by interparticle neck formation without complete melting [32]. During the irradiation process of defocused EB, there is charge transfer and heat while Cr-rich C_{14} Laves phases nucleate preferentially at  $ \alpha_{2}/\gamma $ interfaces under near-equilibrium conditions [39]. the proportion of twin boundaries of  $ \gamma $ [110]70^\circ, predominantly within equiaxial  $ \gamma $ crystals, decreased from 12.5 % in S_{0} to 5.61 % in S_{70}. • With more cycles, the oxide film on the powder surface transitioned from a loose TiO₂ + Al₂O₃ composite to predominantly dense Al₂O₃. The alloy phases within the powder shifted from primarily \alpha/\alpha₂ phase to predominantly \gamma phase. - The rapid solidification in the EB-PBF process promoted  $ \alpha_{2} $ phase formation. However, prolonged thermal exposure at 900-1150 ^\circC during EB-PBF caused the  $ \alpha_{2} $ phase degrade to B_{2} phase. This thermal exposure occurred within a three-phase region, leading to C_{15} Laves phase formation and affecting Cr segregation, disrupting equilibrium of B_{2} phase and promoting formation of C_{14} Laves phase. - RT ultimate tensile strength and yield strength of thin-walled components increased with increasing number of powder recycling cycles, while ductility decreased. These changes in properties were attributed to enhanced microstructure homogeneity and increased Laves phase/B_{2} phase content. [37] B. Gao, H. Peng, H. Yue, H. Guo, C. Wang, B. Chen, Electron beam powder bed fusion of Y₂O₃/\gamma-TiAl nanocomposite with balanced strength and toughness, Addit. Manuf. 72 (2023) 103650, https://doi.org/10.1016/j.addma.2023.103650. [39] Z.C. Xie, D. Chauraud, E. Bitzek, S. Korte-Kerzel, J. Guénolé, Laves phase crystal analysis (LaCA): atomistic identification of lattice defects in C_{14} and C_{15} topologically close-packed phases, J. Mater. Res. 36 (2021) 2010–2024, https://doi.org/10.1557/s43578-021-00237-y. [41] Z.W. Huang, W. Voice, P. Bowen, Thermal exposure induced  $ \alpha_{2}+\gamma\rightarrow B_{2}(\omega) $ and  $ \alpha_{2}\rightarrow B_{2}(\omega) $ phase transformations in a high Nb fully lamellar TiAl alloy, Scripta Mater. 48 (1) (2003) 79–84, https://doi.org/10.1016/S_{1359}-6462(02)00350-0.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

ELSEVIER

Contents lists available at ScienceDirect

journal homepage: www.elsevier.com/locate/matdes

Keywords:
Electron beam powder bed fusion
Powder recycling
TiAl alloy
Thermal exposure
Mechanical properties

A B S T R A C T

* Corresponding authors.

E-mail addresses: liangyf@skl.ustb.edu.cn (Y. Liang), xiaoyu_liang@tsinghua.edu.cn (X. Liang), linjunpin@ustb.edu.cn (J. Lin).

Received 20 January 2025; Received in revised form 8 July 2025: Accented 25 July 2025

Available online 26 July 2025

F. Wang et al.

Samples for tensile testing were machined to dimensions of 12 mm gauge length, 2 mm width, and 1 mm thickness. The tensile specimen dimensions should refer to Fig. 2 (c). Tensile properties were evaluated using a YSL-100 quasi-static tensile testing machine with ± 20 kN load capacity and strain rate of  $ 1 \times 10^{-4} $ s $ ^{-1} $ at RT.

In the EB-PBF building process, the generation of irregular shaped powders in the reused powder mainly occurs in the following two processes (Fig. 6 a): 1) During the preheating process of the powder bed, the defocused EB heats the powder bed to 950–1150 °C, and the powder bed presents a pseudo-sintered state. This state is characterized by interparticle neck formation without complete melting [32]. During the irradiation process of defocused EB, there is charge transfer and heat

while Cr-rich C14 Laves phases nucleate preferentially at  $ \alpha_{2}/\gamma $ interfaces under near-equilibrium conditions [39].

the proportion of twin boundaries of  $ \gamma $ [110]70°, predominantly within equiaxial  $ \gamma $ crystals, decreased from 12.5 % in S0 to 5.61 % in S70.

• With more cycles, the oxide film on the powder surface transitioned from a loose TiO₂ + Al₂O₃ composite to predominantly dense Al₂O₃. The alloy phases within the powder shifted from primarily α/α₂ phase to predominantly γ phase.

- The rapid solidification in the EB-PBF process promoted  $ \alpha_{2} $ phase formation. However, prolonged thermal exposure at 900-1150 °C during EB-PBF caused the  $ \alpha_{2} $ phase degrade to B2 phase. This thermal exposure occurred within a three-phase region, leading to C15 Laves phase formation and affecting Cr segregation, disrupting equilibrium of B2 phase and promoting formation of C14 Laves phase.

- RT ultimate tensile strength and yield strength of thin-walled components increased with increasing number of powder recycling cycles, while ductility decreased. These changes in properties were attributed to enhanced microstructure homogeneity and increased Laves phase/B2 phase content.

CRediT authorship contribution statement

Declaration of competing interest

Supplementary data to this article can be found online at https://doi.org/10.1016/j.matdes.2025.114473.

Data availability

[37] B. Gao, H. Peng, H. Yue, H. Guo, C. Wang, B. Chen, Electron beam powder bed fusion of Y₂O₃/γ-TiAl nanocomposite with balanced strength and toughness, Addit. Manuf. 72 (2023) 103650, https://doi.org/10.1016/j.addma.2023.103650.

[39] Z.C. Xie, D. Chauraud, E. Bitzek, S. Korte-Kerzel, J. Guénolé, Laves phase crystal analysis (LaCA): atomistic identification of lattice defects in C14 and C15 topologically close-packed phases, J. Mater. Res. 36 (2021) 2010–2024, https://doi.org/10.1557/s43578-021-00237-y.

[41] Z.W. Huang, W. Voice, P. Bowen, Thermal exposure induced  $ \alpha_{2}+\gamma\rightarrow B2(\omega) $ and  $ \alpha_{2}\rightarrow B2(\omega) $ phase transformations in a high Nb fully lamellar TiAl alloy, Scripta Mater. 48 (1) (2003) 79–84, https://doi.org/10.1016/S1359-6462(02)00350-0.