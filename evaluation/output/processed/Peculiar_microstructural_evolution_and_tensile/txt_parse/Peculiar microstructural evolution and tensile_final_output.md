DOI: 10.1016/j.addma.2021.102091

# Peculiar microstructural evolution and tensile properties of  $ \beta $-containing  $ \gamma $-TiAl alloys fabricated by electron beam melting

Ken Cho $ ^{a,b} $, Hajime Kawabata $ ^{a} $, Tatsuhiro Hayashi $ ^{a} $, Hiroyuki Y. Yasuda $ ^{a,b,*} $, Hirotoyo Nakashima $ ^{c} $, Masao Takeyama $ ^{c} $, Takayoshi Nakano $ ^{a,b} $

$^{a}$ Division of Materials and Manufacturing Science, Graduate School of Engineering, Osaka University, 2–1 Yamadaoka, Suita, Osaka 565-0871, Japan

$^{b}$ Anisotropic Design & Additive Manufacturing Research Center, Graduate School of Engineering, Osaka University, 2-1 Yamadaoka, Suita, Osaka 565-0871, Japan

$^{c}$ Department of Materials Science and Engineering, School of Materials and Chemical Technology, Tokyo Institute of Technology, 2-12-1 Ookayama, Meguro-ku, Tokyo 152-8552, Japan

## ARTICLE INFO

## Keywords

Additive manufacturing

Electron beam melting

Titanium aluminide

Microstructure

Tensile properties

## Abstract

The microstructure and tensile properties of  $ \beta $-containing Ti–44Al–4Cr alloy rods additively manufactured by electron beam melting (EBM) process were examined as a function of input energy density determined by the processing parameters. To the best of our knowledge, this is the first report to demonstrate that two types of fine microstructures have been obtained in the  $ \beta $-containing  $ \gamma $-TiAl alloys by varying the energy density during the EBM process. A uniform  $ \alpha_{2}/\beta/\gamma $ mixed structure containing an  $ \alpha_{2}/\gamma $ lamellar region and a  $ \beta/\gamma $ dual-phase region is formed at high energy density conditions. On the other hand, a lower energy density leads to the formation of a peculiar layered microstructure perpendicular to the building direction, consisting of a ultrafine  $ \alpha_{2}/\gamma $ lamellar grain layer and a  $ \alpha_{2}/\beta/\gamma $ mixed structure layer. The difference in the microstructures originates from the difference in the solidification microstructure and the temperature distribution from the melt pool, which are dependent on the energy density. Furthermore, it was found that the strength of the alloys is closely related to the volume fractions of the  $ \beta $ phase and the ultrafine  $ \alpha_{2}/\gamma $ lamellar grains which originates from the massive  $ \alpha $ grains formed by rapid cooling under low energy density conditions. The alloys with high amounts of these peculiar microstructures exhibit high strength comparable to and higher than the conventional  $ \beta $-containing  $ \gamma $-TiAl at room temperature and 1023 K, respectively.

## 1. Introduction

\gamma-Titanium aluminide ( $ \gamma $-TiAl) alloys have received considerable attention for aircraft and automotive engine applications due to their low density (approximately 3.8 g/cm $ ^{3} $) and excellent strength at room and high temperatures (RT and HT) [1,2]. In recent years, in order to improve the efficiency of aircraft engines by reducing their weight, Ti–48Al–2Cr–2Nb (at%, hereafter 48–2–2) alloys which are typical \gamma-TiAl alloys have replaced nickel-based superalloys in low-pressure turbine (LPT) blades of the engines [3,4]. In addition, the development of new \gamma-TiAl alloys with mechanical properties superior to those of 48–2–2 alloys is also being actively pursued. \beta-containing \gamma-TiAl alloys that have an ordered \beta phase (B_{2} structure) at service temperatures have been proposed by Takeyama et al. [5–7]. Likewise, Clemens et al. developed Ti–Al–Nb–Mo–B (TNM) alloys as \beta-containing alloys for practical use [8]. These next-generation \gamma-TiAl alloys are likely to contribute to the advancement of more efficient aircraft engines and expand the application range of these alloys owing to their high strength at HT and good creep resistance, compared with 48–2–2 alloys [7,8].

LPT blades of  $ \gamma $-TiAl alloys are predominantly fabricated by precision investment casting [9,10]. However, the low ductility at RT and the high reactivity of the alloys are significant concerns in the casting process. The surface oxide and contamination from the casting mold must be removed after the process [11]. However, precise cutting of the alloys is difficult because of their low ductility at RT, which leads to a large amount of material waste and high production costs. Thus, it is necessary to establish an innovative manufacturing process for  $ \gamma $-TiAl alloys.

The new additive manufacturing process of electron beam melting (EBM) for metallic materials has attracted much attention for metal products, particularly for applications in the aerospace and biomedical

industries, that require a high degree of complexity [12–14]. In the EBM process, near-net shaped parts can be fabricated directly from three-dimensional computer-aided design data in vacuum by repeating feed and fusion of metal powder by scanning focused electron beam as a heat source. Therefore, highly reactive materials can be fabricated by the EBM process while suppressing the oxidation and contamination of the parts during the process. Recently, the microstructure and mechanical properties of various materials, including Ti alloys [15,16], Co–Cr–Mo alloys [17,18], Ni-based superalloys [19,20] and high-entropy alloys [21,22] prepared by the EBM process have been studied, focusing on the influence of the process parameters such as beam current and scanning speed. As a result of these investigations, researchers found that the microstructure of the alloys can be controlled by the EBM process through selection of the process parameters and it is possible to obtain alloys with better mechanical properties than conventional cast or forged materials. In order to clarify the mechanism of the microstructural changes, the influence of the process conditions on the shape and thermal gradient of the melt pool, the velocity of the solidification rate and the temperature distribution from the melt pool have also been investigated using numerical simulations [23–25]. These reports suggest that the characteristics of the melt pool have a significant impact on the microstructure.

In recent years, research on the manufacturing techniques for  $ \gamma $-TiAl alloy parts and improvement of the mechanical properties of alloys using the EBM processes have also been conducted. Schwerdtfeger et al. [26], Murr et al. [27] and Abdulrahman et al. [28] investigated the effect of the process parameters on the surface quality and microstructure of 48–2–2 alloys or alloys having a similar chemical composition. In addition, the mechanical properties of these alloys were studied, focusing on their microstructures [29–32]. In our previous study, we found that it is possible to obtain 48–2–2 alloys with a unique layered microstructure composed of a duplex-like region and an equiaxed  $ \gamma $ grain region (referred to as  $ \gamma $ band) using the EBM process [33]. This layered microstructure is formed by repeated thermal effects from the melt pool, which is a unique phenomenon of the EBM process. The alloys with the layered microstructure show an elongation higher than 2.5% at RT owing to the localized shear deformation in the  $ \gamma $ band [33]. Moreover, even without hot isostatic pressing (HIP) treatment, the alloys exhibit excellent fatigue strength compared to HIP-treated cast alloys, owing to their large ductility and high fracture toughness [34–36]. These results indicate that it is possible to manufacture  $ \gamma $-TiAl alloys with greatly improved mechanical properties by controlling the EBM process when the relationship between the process conditions and the microstructure of the alloys is fully understood.

Most recently, some researchers reported that the EBM process can be applied to fabricate  $ \beta $-containing  $ \gamma $-TiAl alloys [37,38]. However, the effects of the process conditions on the structural integrity, microstructure and mechanical properties of the alloys have not yet been systematically investigated. In the present study, the influence of input energy density during the process on the microstructure of the  $ \beta $-containing  $ \gamma $-TiAl alloys were investigated. We chose Ti–44Al–4Cr (at%, hereafter 44–4) alloy for our investigation, which was originally designed as a  $ \beta $-containing alloy by Takeyama et al. [7]. As a result, two types of microstructures could be first obtained by controlling the process parameters during the process. Moreover, the relationship between these microstructures and tensile properties at RT and 1023 K were systematically examined, focusing particularly on the mechanical property, volume fraction and deformation structure of each constituent phase.

## 2. Experimental

## 2.1. Preparation of raw powder

The 44–4 alloy raw powder was fabricated by Ar gas atomization (at Osaka Yakin Kogyo Co., Ltd., Japan) from master ingots of the alloy provided by Kobe Steel, Ltd., Japan. The chemical composition of the raw powder was analyzed using inductively coupled plasma optical emission spectroscopy for metallic elements and an inert gas fusion method for oxygen. The morphology of the raw powder was observed using a scanning electron microscope (SEM). The circularity (K) of the raw powder was investigated using Eq. (1) [39],

 $$ K=\frac{4\pi A}{P^{2}} $$ 

where A and P are the projected area and perimeter of the raw powder, respectively. These values were measured using ImageJ image analysis software. At least 200 particles were measured for the investigation. The particle size distribution and mean diameter of the powder were measured using a laser diffraction particle size distribution analyzer. The flowability of the powder was evaluated according to the angle of repose, which was measured using a revolution powder analyzer.

## 2.2. Sample fabrication by EBM

Rectangular rods of 44–4 alloy with dimensions of  $ 10 \times 10 \times 15 $ mm (Fig. 1(a)) and  $ 10 \times 10 \times 30 $ mm (Fig. 1(b)) were fabricated using an Arcam Q10 EBM system at an accelerating voltage of 60 kV and a preheating temperature of 1333 K. The layer thickness for each fed powder layer was 90  $ \mu $m, and the building direction was parallel to the longitudinal direction of the rods. The influence of the EBM process parameters on the dimensional accuracy, formation of defects, microstructure and mechanical properties of the alloys were evaluated as a function of different input energy density (ED) given by,

 $$ ED=\frac{UI}{vh} $$ 

where U is the accelerating voltage, I is the beam current,  $ \nu $ is the scanning speed and h is the line offset. In this study, the ED was changed from 0.9 J/mm $ ^{2} $ to 12.5 J/mm $ ^{2} $ by controlling I and  $ \nu $ from 6 mA to 28 mA and from 800 mm/s to 5000 mm/s, respectively. The chemical composition of the as-built rods was analyzed using the same methods as for the raw powder. Here, it should be noted that the rods fabricated by the EBM were not subjected to any post-annealing processes including
Fig. 1. Schematic drawings of the short (a) and long (b) 44–4 alloy rods fabricated by the EBM and the specimen configuration for tensile tests (c).

HIP treatment.

## 2.3. Microstructure observation

The internal defects, pores and microstructures of the as-built rods were observed using an optical microscope (OM), an SEM equipped with a back-scattered electron (BSE) detector and a transmission electron microscope (TEM). The OM and SEM images were taken from the cross-section of the rods with respect to the building direction. The quantitative analyses of the defects, pores and microstructures were performed based on the OM and SEM images of the rods using the software ImageJ.

## 2.4. Mechanical testing

The tensile properties of the rods fabricated by the EBM at various ED were examined using an Instron-type testing machine at RT and 1023 K in vacuum with an initial strain rate of  $ 1.7 \times 10^{-4} \, s^{-1} $. The specimens for the tensile tests with gauge dimensions  $ 5.0 \times 1.5 \times 0.5 \, mm $ were cut from the center of the as-built rods (Fig. 1(c)). The specimens were polished mechanically using both SiC emery papers and colloidal  $ SiO_{2} $ suspensions before tensile testing. The loading axis was set parallel to the longer direction of the rods during the tests. In the case of HT tensile tests, the specimens were deformed after waiting until the thermal expansion of the tensile jig became stable. The elongation of the specimens was determined by the displacement of the crosshead, which subtracted the influence of elastic deformation. The fracture surfaces of the tensile-fractured specimens were observed using a SEM. The dislocation structures in the tensile-deformed specimens were analyzed by TEM. The hardness of each constituent phase was measured by nano-indentation tests with a maximum load of 4.9 mN.

## 3. Results

## 3.1. Characteristics of raw powder

Fig. 2 shows (a) a typical SEM image and (b) particle diameter distribution of the raw powder. The particles have a spherical shape with K = 0.94. As shown in Fig. 2(b), the particle size distribution has a single peak with a narrow width, and the mean diameter ( $ d_{m} $) of the particles is 70.2  $ \mu $m. High flowability of the powder is required to make an accurate rake during the EBM process. The angle of repose of the powder is approximately 44.8^\circ, which is almost comparable to that of other reported powders for the EBM process [40]. The high flowability of the powder is due to small amounts of fine particles with a diameter of 10  $ \mu $m or less and satellites indicated in Fig. 2(a).

The chemical composition of the raw powder is listed in Table 1. It should be noted that the actual composition of Cr is almost the same as the nominal composition of 44–4 alloy, but that of Al is 0.8 at% higher

(a)

Table 1 Chemical composition of the 44–4 alloy raw powder and rods fabricated by the EBM (at%).

|  | Ti | Al | Cr | O |
| --- | --- | --- | --- | --- |
| Alloy composition (Nominal) | Bal. | 44 | 4 | 0 |
| Raw powder (Actual) | Bal. | 44.8 | 4.0 | 0.15 |
| Rectangular rod (Actual) | Bal. | 43.9 | 4.0 | 0.18 |

than the nominal value. The Al content of the powder was determined by considering that approximately 1 at% of Al evaporates during fusion in the EBM process [33]. Furthermore, 0.15 at% of O is mainly derived from the surface oxide layer, and is never as high as the oxygen content of gas atomized powder for the process [33,41]. These results indicate that the 44–4 alloy raw powder used in this study was well suited for the EBM manufacturing.

## 3.2. Structural integrity of rods fabricated by EBM

The actual chemical composition of the rods fabricated by the EBM at an ED of 2.0 J/mm² is listed in Table 1. The Al content decreases by 0.9 at% during the fabrication, although the Cr content does not change from the raw powder. The chemical composition of the rods shows good agreement with the nominal alloy composition due to the expected Al loss. It should be noted that there is no significant increase in the O content after fabrication, indicating limited oxidation during the process.

Fig. 3 shows the ED-v process map for dimensional error ( $ E_{d} $) of the rods prepared under various conditions. Note that it is difficult to
Fig. 3. ED- $ \nu $ process map for  $ E_{d} $ of the 44–4 alloy rods fabricated by the EBM.
Fig. 2. A typical SEM image (a) and particle diameter distribution (b) of the 44–4 alloy raw powder.

fabricate rods under the process conditions indicated by the black rhombus in Fig. 3 due to excessively high ED. Fig. 4(a)–(c) show the rods fabricated at conditions A, B and C, respectively, that correspond to the conditions in Fig. 3. These samples were fabricated at the same v but progressively smaller values of ED (ED: A > B > C). The layered asperity and the elevation can be seen on the side surfaces and top surface of the rods built at conditions A and B. The  $ E_{d} $ for condition A is larger than 1 mm. Previous studies have reported that ED has a great effect on the stability of the melt pool by affecting the convection flow and temperature-dependent surface tension of the melt pool [25,42]. High ED leads to poor dimensional accuracy of EBM samples due to the unstable melt pool. As evident in Fig. 4(c), the side and top of the rod fabricated at condition C have flat surfaces, resulting in a low  $ E_{d} $ (< \pm0.5 mm). This means that  $ E_{d} $ can be reduced by stabilizing the melt pool by reducing ED. In addition, Fig. 4(d) shows the rod prepared at condition D indicated in Fig. 3, which has almost the same ED as condition C but v is twice as fast. The rod also exhibits a flat surface and small  $ E_{d} $ (< \pm0.5 mm), indicating that the dimensional accuracy of the samples can be controlled by focusing on ED, even if individual conditions such as the scan speed and current of the electron beam are different.

focus on internal defects and pores because they often affect mechanical properties of the alloys, such as tensile and fatigue strengths. Six samples were selected from the rods satisfying a condition where  $ E_{d} < \pm 0.5 $ mm to clarify the influence of ED on the formation of defects and pores. The rod number and ED of each selected rod are listed in Table 2. Fig. 5(a) and (c) show typical OM images of cross sections of R6 and R1, respectively. Although the rod fabricated at the lowest ED (R6, 1.2 J/mm $ ^{2} $) exhibits a smooth surface and low  $ E_{d} $, large non-uniform defects with a volume fraction ( $ f_{d} $) of 4.9% can be observed inside the sample (Table 2, Fig. 5(a)). As shown in Fig. 5(b), many unmelted raw powder particles are found within the defects, suggesting that the defects are formed by a lack of fusion. Thus,  $ f_{d} $ is reduced with increasing ED and attains of 0.1% in R1 which has the highest ED (4.0 J/mm $ ^{2} $) of the six rods (Table 2, Fig. 5(c)). On the other hand, circular pores with diameters less than 100  $ \mu $m can be seen in all rods (Fig. 5(d)), and the porosity ( $ f_{p} $) does not depend on ED (Table 2). These pores are difficult to reduce by optimizing the process conditions of the EBM, as these are
Fig. 4. 44–4 alloy rods fabricated by the EBM under process conditions A (a), B (b), C (c) and D (d), as indicated in Fig. 3.

Table 2 ED,  $ f_{d} $ and  $ f_{p} $ of the 44–4 alloy rods fabricated by the EBM.

| Rod No. | $ ED\ (J/mm^{2}) $ | $ f_{d}\ (\%) $ | $ f_{p}\ (\%) $ |
Fig. 5. Typical OM images of a cross section of R6 (a) and R1 (c) and SEM images of defects in R6 (b) and a pore in R1 (d).

attributed to the atomization gas (Ar) trapped in the raw powder. These results indicate that in order to obtain 44–4 alloy with good structural integrity, including low  $ E_{d} $ and  $ f_{d} $, it is necessary to select process parameters where ED is 1.4 J/mm $ ^{2} $ or more within the range plotted by the red circle in Fig. 3.

## 3.3. Microstructure of 44–4 alloys fabricated by EBM

To evaluate the microstructure of 44–4 alloys fabricated by the EBM process, the longitudinal section of the rods listed in Table 2, excluding R6, were observed by a SEM. Fig. 6(a) and (b) show the microstructures of the rods fabricated at high (R1, 4.0 J/mm²) and low (R5, 1.4 J/mm²) ED, respectively. In SEM-BSE images, the \alpha₂, \gamma and \beta phases exhibit gray, black and white contrasts, respectively. The microstructures of these rods are much finer than those of the cast and forged alloys (grain size: 100–800 \mum) [43–45], although the alloy fabricated at the high and low ED show completely different microstructural features from each other. This is attributed to the rapid solidification and the fast cooling rate, which are important features of the EBM process. The high ED rod has a uniform \alpha₂/\beta/\gamma mixed structure composed of two regions: the \alpha₂/\gamma lamellar region and the \beta/\gamma dual phase region (Fig. 6(a) and (c)) (hereafter called a high energy density (HED) microstructure). Fig. 7(a) and (b) show a bright-field (BF) image and a selected area electron diffraction (SAED) pattern of the \beta phase in the \beta/\gamma dual phase region with a beam direction (B) of [110]\beta. Superlattice 001 diffraction spot can be seen in the SAED pattern taken from the \beta phase indicating that the \beta phase has an ordered B_{2} structure. The volume fraction of the \beta and \gamma phases in the \beta/\gamma dual phase region is approximately 50%. In contrast, the alloy with the low ED exhibits a layered microstructure perpendicular to the building direction, which is composed of layers A and B.
Fig. 6. Microstructure of R1 fabricated at high ED (4.0 J/mm²) (a) and R5 at low ED (1.4 J/mm²) (b). Enlarged SEM images of the \alpha₂/\beta/\gamma mixed structure in R1 (c), layer A (d) and layer B (e) in R5 and the \alpha₂/\beta/\gamma mixed structure in layer B of R5 (f).
Fig. 7. Typical BF images (a), (c), (e) and SAED patterns (b), (d), (f) of the \beta phase in R1 (a), (b) with B = [110]\beta, the lamellae in R1 (c), (d) and R5 (e), (f) with B = [110]\gamma//[1120]\alpha₂.

(Fig. 6(b)) (hereafter called a low energy density (LED) microstructure). The  $ \alpha_{2}/\gamma $ lamellae with jagged grain boundaries and the  $ \beta/\gamma $ cell structure can be observed in layer A (Fig. 6(d)). Fig. 7(c)–(f) show BF images of the lamellar structure in the HED (R1) and LED (R5) microstructures and SAED patterns taken from these areas. Both of these lamellae consist of the  $ \alpha_{2} $ plates and some variants of the  $ \gamma $ plates with twin boundaries. However, the average lamellar spacing ( $ \lambda $) of the lamellae in the LED microstructure ( $ \lambda = 32.5 $ nm) is smaller than that in the HED microstructure ( $ \lambda = 62.1 $ nm). The fine lamellar structure in the LED microstructure will hereafter be referred to as the “ultrafine lamellar grain” in order to clearly distinguish it from the “lamellar region” observed in the HED microstructure because they have completely different formation mechanisms and mechanical properties. The  $ \beta/\gamma $ cell structure is a unique microstructure in  $ \beta $-containing  $ \gamma $-TiAl alloys, which is precipitated at the grain boundary of the  $ \alpha_{2}/\gamma $ lamellar grain through a discontinuous precipitation reaction usually by aging in the  $ \beta + \gamma $ two-phase region [46]. The volume fraction of the  $ \gamma $ phase in the  $ \beta/\gamma $ cell structure is approximately 75%. The  $ \alpha_{2}/\beta/\gamma $ mixed structure composed of the  $ \alpha_{2}/\gamma $ lamellar and  $ \beta/\gamma $ dual phase regions, which is typical in the HED microstructure, can be found in layer B (Fig. 6(e) and (f)). It should be noted that the width of layers A and B is approximately 45  $ \mu $m, and the combined width of the two layers agrees with the thickness for each fed powder layer (90  $ \mu $m) of the fabrication process. This feature suggests that the formation of the layered microstructure in the low ED sample is associated with the layer-on-layer process during the EBM fabrication. It is known that the solidification path and the microstructure of TiAl alloys depend on the Al content. The difference of Al content between low ED (R5, 1.4 J/mm $ ^{2} $) and high ED (R1, 4.0 J/mm $ ^{2} $) rods is less than 0.3 at%. Thus the influence of the variation of Al content on the microstructural evolution is considered to be insignificant. The details of the formation mechanisms of the LED and HED microstructures will be discussed later.

The variations in the volume fractions of the  $ \alpha_{2}/\beta/\gamma $ mixed structure ( $ V_{\alpha2/\beta/\gamma} $), ultrafine  $ \alpha_{2}/\gamma $ lamellar grain ( $ V_{\alpha2/\gamma G} $) and  $ \beta/\gamma $ cell structure ( $ V_{\beta/\gamma C} $) of the rods are shown in Fig. 8(a) as a function of ED.  $ V_{\alpha2/\beta/\gamma} $ increases to 100% with increasing ED up to approximately 3 J/mm $ ^{2} $ and then remains constant. In contrast,  $ V_{\alpha2/\gamma G} $ and  $ V_{\beta/\gamma C} $ decrease to 0% with increasing ED due to replacement by the  $ \alpha_{2}/\beta/\gamma $ mixed structure. These results indicate that the morphology of the microstructure changes from the LED to HED microstructure at an ED of approximately 3 J/mm $ ^{2} $. Fig. 8(b) shows the influence of ED on the volume fraction of all the  $ \alpha_{2}/\gamma $ lamellae (the combination of both the ultrafine lamellar grain in the LED microstructure and the lamellar region in the  $ \alpha_{2}/\beta/\gamma $ mixed structure,  $ V_{\text{all}\alpha2/\gamma} $), the volume fraction of all the  $ \gamma $ phases excluding that in the lamellae ( $ V_{\text{all}\gamma} $) and the volume fraction all the  $ \beta $ phases ( $ V_{\text{all}\beta} $). In addition, the relationships between ED and the fraction of these phases in the  $ \alpha_{2}/\beta/\gamma $ mixed structure (the  $ \alpha_{2}/\gamma $ lamellar region:  $ f_{\alpha2/\gamma MS} $, the  $ \gamma $ phase:  $ f_{\gamma MS} $, the  $ \beta $ phase:  $ f_{\beta MS} $) are shown in Fig. 8(c). As shown in Fig. 8
Fig. 8. Variations in microstructural factors as a function of ED (a)  $ V_{\alpha2/\beta/\gamma} $,  $ V_{\alpha2/\gamma G} $ and  $ V_{\beta/\gamma C} $, (b)  $ V_{\text{all}\alpha2/\gamma} $,  $ V_{\text{all}\gamma} $ and  $ V_{\text{all}\beta} $, (c)  $ V_{\alpha2/\gamma MS} $,  $ V_{\beta MS} $ and  $ V_{\gamma MS} $, and (d)  $ f_{\alpha2/\gamma R} $ and  $ f_{\alpha2/\gamma G} $.

(b),  $ V_{\text{all}\alpha2/\gamma} $ decreases from approximately 60–50% with increasing ED. This is because not only  $ V_{\alpha2/\gamma G} $ but also  $ f_{\alpha2/\gamma MS} $ decrease with increasing ED (Fig. 8(a) and (c)). It is important to note that there are more ultrafine lamellar grains ( $ f_{\alpha2/\gamma G} $) in the low ED, but the proportion of the lamellar region ( $ f_{\alpha2/\gamma R} $) increases with increasing ED (Fig. 8(d)). Moreover,  $ V_{\text{all}\beta} $ also varies depending on ED. The increases in  $ V_{\alpha2/\beta/\gamma} $ and  $ f_{\beta MS} $ with increasing ED (Fig. 8(a) and (c)) cause an increase in  $ V_{\text{all}\beta} $. On the other hand, the  $ \beta/\gamma $ cell structure ( $ V_{\beta/\gamma C} $) with a high fraction of the  $ \gamma $ phase and  $ V_{\gamma MS} $ decreases and increases, respectively, with increasing ED (Fig. 8(a) and (c)), resulting in a nearly constant  $ V_{\text{all}\gamma} $ regardless of ED. The volume fractions of each constituent phase is closely related to the mechanical properties of the rods.

## 3.4. Tensile properties of 44–4 alloy fabricated by EBM

Stress-strain (S–S) curves of R1, R2 and R5 tensile-deformed at RT are shown in Fig. 9(a). The ultimate tensile strengths ( $ \sigma_{B} $) of these rods at RT exceed 700 MPa (773 MPa for R1) and are higher than those of the cast 48–2–2 alloys (450–550 MPa) and comparable to those of cast TNM alloys (700–800 MPa) [43,45]. Furthermore, the strength of the rods decreases with increasing ED up to approximately 3 J/mm $ ^{2} $ and then increases with a further increase in ED (Fig. 9(c)). As described in Section 3.3, the microstructure of the rods can be divided into the LED or HED microstructure by an ED of approximately 3 J/mm $ ^{2} $ as a boundary. These results imply that the RT strength of the alloys depends strongly on the type or morphology of the microstructure. These rods show plastic deformation even at RT, although the elongations to failure (EL) are less than 1%, regardless of the process parameters. It should be noted that the fracture surfaces of the tensile tested rods deformed to fracture at RT are covered by facets, and the defects are difficult to observe, as shown in Fig. 9(b). This result indicates that the limited plastic deformation of the rods is not due to crack initiation at defects, but instead is due to brittle fracture of the alloys, which has a tradeoff relationship with high strength.

Fig. 10(a) shows S–S curves of R1, R2 and R5 pulled at 1023 K. In addition,  $ \sigma_{B} $ and EL of the rods at 1023 K are plotted against ED in Fig. 10(c) and (d), respectively.  $ \sigma_{B} $ of these alloys at 1023 K remains almost constant up to an ED of approximately 3 J/mm $ ^{2} $ and then increases with an increase in ED. As a result, the  $ \sigma_{B} $ of the rods fabricated at an ED of 4.0 J/mm $ ^{2} $ reaches 644 MPa, which is higher than those of cast 48–2–2 ( $ \sim $450 MPa) and TNM alloys ( $ \sim $600 MPa) [43,45]. It is interesting to note that all the samples exhibit large EL at 1023 K, compared with the cast alloys (10%) [43,45], and the values are approximately 40%. Moreover, only dimples can be seen in the fracture surfaces of the specimens after tensile deformation to fracture at 1023 K (Fig. 10(b)), which indicates that the fracture mode of the alloys changes completely from brittle fracture mode to ductile fracture mode by increasing the deformation temperature, irrespective of the type of microstructure.

Fig. 11 shows typical TEM images of R1 and R5 tensile-deformed at 1023 K. Numerous dislocations and twins can be seen in the  $ \gamma $ phase of the deformed R1 (Fig. 11(a)). It is well known that the  $ \gamma $ phase deforms
Fig. 9. S–S curves of R5, R2 and R1 tensile-deformed at RT (a) and a typical SEM fractograph of R1 after tensile deformation to fracture at RT (b). Variations in  $ \sigma_{B} $ (c) and EL (d) at RT of the 44–4 alloy rods fabricated by the EBM as a function of ED.
Fig. 10. S–S curves of R5, R2 and R1 tensile-deformed at 1023 K (a) and a typical SEM fractograph of R1 after tensile deformation to fracture at 1023 K (b). Variations in  $ \sigma_{B} $ (c) and EL (d) at 1023 K of the 44–4 alloy rods fabricated by the EBM as a function of ED.
Fig. 11. Typical TEM images of R1 (a), (b), (d), (e) and R5 (f) tensile-deformed at 1023 K. BF images of the  $ \gamma $ phase (a) and the  $ \beta $ phase (b) in R1 with B  $ \approx $ [110] $ \gamma $, g = 111 and B  $ \approx $ [001] $ \beta $, g = 110, respectively. A SAED pattern of the  $ \beta $ phase in R1 with B = [110] $ \beta $ (c) and a DF image obtained from the  $ \omega_{0} $ spot indicated by a red circle (d). BF images of the lamellae in R1 (e) and R5 (f) with B  $ \approx $ [112] $ \gamma $, g = 110 and 220, respectively. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

by the  $ \{111\}(1/2) < 1\overline{1}0 $ ordinary dislocation,  $ \{111\} < 101 $ superlattice dislocation and  $ \{111\}(1/6) < 11\overline{2} $ twinning [47]. As a result of investigation of the Burgers vectors (b) of the dislocations shown in Fig. 11(a) by g·b contrast analyses (reflection vectors (g)), it was revealed that both the ordinary and superlattice dislocations move at 1023 K, together with deformation twins. This means that all possible deformation modes are activated in the \gamma phase during deformation at 1023 K, though the number of the ordinary dislocations is larger than that of the superlattice dislocations, as reported in previous papers [48–50]. It should be noted that the hexagonal  $ \omega_{0} $ phase with a mean diameter of approximately 100 nm is precipitated in the \beta phase by exposure at 1023 K during the tensile test (Fig. 11(c) and (d)), although dislocations associated with deformation are difficult to find (Fig. 11(b)). Since the \beta phase has the ordered B_{2} structure, the  $ \omega_{0} $ phase is also ordered with some extra spots [51,52]. Schloffer et al. and Wang et al. reported that the  $ \omega_{0} $ phase is transformed from the \beta phase during isothermal treatment at temperature range from 973 K to 1098 K and significantly increases the hardness of the \beta phase [51,52]. Therefore, it is possible to consider that the \beta phase strengthened by the  $ \omega_{0} $ phase plays an important role in the HT strength of the alloys. It should be also noted that the two types of the lamellae show different deformation behavior at 1023 K. As shown in Fig. 11(e) and (f), dislocations are observed in the widely-spaced \gamma plates of the coarse lamellar region but hardly found in the fine lamellar grain. These results suggest that the \gamma phase and the coarse lamellar region are primarily responsible for the deformation, while the \beta phase and the ultrafine lamellar grain are barely deformed at 1023 K.

## 4. Discussion

The microstructure and mechanical properties of 44–4 alloy rods built by the EBM at different process parameters were investigated, focusing on the energy density. It was found that the microstructure of the alloys can be classified into two types: the homogenous HED and layered LED microstructures, depending on ED. Moreover, the tensile properties of the alloys are also affected by the process conditions. The formation mechanisms of the HED and LED microstructures were discussed according to the solidification microstructure that can be seen in the top part of the rods and the thermal effect from the melt pool during the fabrication process. Furthermore, the relationships between the microstructure and tensile properties of the alloys were also discussed.

with consideration of the mechanical property, volume fraction and deformation structure of each phase in the HED and LED microstructures.

## 4.1. Microstructural evolution

## 4.1.1. Formation of the HED microstructure

To understand the formation mechanism of the HED microstructure developed at ED higher than approximately 3 J/mm², it is necessary to methodically analyze each region of the microstructure. The microstructure of the top part of R1 (ED = 4.0 J/mm²) is shown in Fig. 12(a). This area also has the  $ \alpha_2/\beta/\gamma $ mixed structure composed of the  $ \alpha_2/\gamma $ lamellar and  $ \beta/\gamma $ dual phase regions, similar to the interior of the rod (Fig. 6(a)). However, the mixed structure in this area is not uniform and can be divided into three areas based on the morphology. Area 1 from the top surface to a depth of approximately 220  $ \mu $m exhibits a finer microstructure than the interior, and is considered to the last melt pool in the fabrication process (Fig. 12(b)). As shown in the schematic phase diagram of the  $ \beta $-containing  $ \gamma $-TiAl alloys (Fig. 13(a)), the  $ \beta $ phase is formed initially from a liquid phase with solidification of the melt pool (Fig. 13(a)I and (c)I). Thereafter, area 1 enters the  $ \beta + \alpha $ two-phase region (Fig. 13(a)II) as the temperature decreases, and the single  $ \beta $ phase separates into the  $ \beta $ and  $ \alpha $ phases (Fig. 13(c)II). As a result of this  $ \beta \rightarrow \beta + \alpha $ phase separation, the Cr-rich  $ \beta $ and the Al-rich  $ \alpha $ phases form due to atom partitions of Al and Cr along the  $ \beta/\alpha $ equilibrium tie line shown in Fig. 13(b). After that, when the temperature decreases to the  $ \alpha + \gamma $ two-phase region in the phase diagram and reaches the preheating temperature (Fig. 13(a)III and (c)III), the  $ \gamma $ phase is precipitated in the Al-rich  $ \alpha $ phase, resulting in the formation of the  $ \alpha_2/\gamma $ lamellar region. At the same time, the Cr-rich  $ \beta $ phase transforms into the  $ \beta/\gamma $ dual phase region by annealing in the  $ \beta + \gamma $ two-phase region (Fig. 13(a)III and (c)III).

It is important to note that the microstructures of areas 2 and 3, as indicated in Fig. 12(a), are affected by the thermal effect caused by the temperature distribution from the melt pool during fusion of the area 1, as shown in Fig. 14(a). Area 2, directly below the melt pool, is aged mainly in the  $ \beta + \alpha $ two-phase region (Fig. 13(a)II), and consequently
Fig. 12. Microstructure of the top part of R1 (a) and enlarged SEM images of area 1 (b), area 2 (c) and area 3 (d) indicated in (a).
Fig. 13. Schematic phase diagrams of Ti–Al–Cr alloys; (a) vertical section of Ti–44Al alloys as a function of Cr content and (b) isothermal section at temperature II in (a) and schematic illustrations showing evolution of solidification microstructure at top surface of the 44–4 alloy rods with the HED microstructure (c).

has the coarser  $ \alpha_{2}/\beta/\gamma $ mixed structure than area 1. Clearly, the heat treatment temperature in area 2 increases with increasing ED. As a result, the proportion of the  $ \beta $ phase increases at the  $ \beta \rightarrow \beta + \alpha $ phase separation according to the lever rule of the phase diagram. This leads to a decrease and increase in the  $ \alpha_{2}/\gamma $ lamellar and  $ \beta/\gamma $ dual phase regions, respectively, in the  $ \alpha_{2}/\beta/\gamma $ mixed microstructure with increasing ED (Fig. 8(c)). Area 3, located farthest from the top surface of the three areas, shows the  $ \alpha_{2}/\beta/\gamma $ mixed structure with comparable size but a high amount of the  $ \gamma $ phase ( $ f_{\gamma MS} = 23\% $) compared with area 2 ( $ f_{\gamma MS} = 10\% $). This is because area 3 is heat treated at a lower temperature than area 2, where the  $ \gamma $ phase is precipitated in the  $ \alpha_{2}/\gamma $ lamellar and  $ \beta/\gamma $ dual phase regions. In the EBM process, the feed and fusion of a new powder layer are alternately repeated for the fabrication of new layers (Fig. 14(b)). Thus, the microstructural distribution shown in Fig. 12 is re-formed repeatedly with each fabrication of a new layer (Fig. 14(c)). However, the thermal effect from the melt pool does not reach deeper than area 3 because of the long distance from the top surface. Therefore, the  $ \alpha_{2}/\beta/\gamma $ mixed structure formed in area 3 is maintained throughout the fabrication process (Fig. 14(d)).

## 4.1.2. Formation of LED microstructure

When the ED is lower than approximately 3 J/mm², the unique LED microstructure that consists of the layered structure is obtained. Fig. 15 (a) shows the microstructure of the top part of R5 ( $ ED = 1.4 \, J/mm^2 $). Area 1, nearest to the top surface, exhibits the  $ \alpha_2/\gamma $ lamellar grain with jagged grain boundary, which corresponds to the last melt pool. The depth of the melt pool decreases from approximately 220  $ \mu $m to 160  $ \mu $m by lowering ED from 4.0 J/mm $ ^2 $ to 1.4 J/mm $ ^2 $. It has been reported that the depth and lifetime of the melt pool in the EBM process depend on the process conditions, and they decrease with decreasing ED [23,24]. The decreases in the depth and lifetime of the melt pool induce fast cooling rates of the melt pool and its vicinity. Similar to the high ED conditions, the  $ \beta $ phase is formed firstly by the solidification of the melt pool under low ED conditions (Fig. 16(a)I and (c)I). However, in the case of fast cooling rates, the  $ \beta \rightarrow \beta + \alpha $ phase separation in the  $ \beta + \alpha $ two-phase region becomes difficult to occur because of its slow reaction rate, resulting in the direct formation of the  $ \alpha $ grain by the  $ \beta \rightarrow \alpha $ massive phase transformation (Fig. 16(b) and (c)II). The jagged grain boundary
Fig. 14. Schematic illustrations showing microstructural evolution and HED microstructure formation in the 44–4 alloy rods during the EBM; (a) fusion top surface, (b) feed a new powder layer, (c) fusion top surface again and (d) fabricated rod with the HED microstructure.
Fig. 15. Microstructure of the top part of R5 (a) and enlarged SEM images of area 1 (b), area 2 (c), area 3 (d), area 4 (e) and area 5 (f) indicated in (a).

observed in area 1 (Fig. 15(b)), which is attributed to the ledge structure for maintaining atom matching at the grain boundary with no specific orientation relationship, is one of the features of the massive grains [53]. The massive  $ \alpha $ phase transformation has been reported in  $ \beta $-containing  $ \gamma $-TiAl powder fabricated by gas atomization process, since the process exhibits high solidification and cooling rates [54]. The massive  $ \alpha $ grains become the lamellar grains through precipitation of the  $ \gamma $ plate during further cooling when they enter the region that the  $ \gamma $ phase can be precipitated (Fig. 16(a)III and (c)III). The lamellar grain contains the same amount of Al and Cr as the alloy composition because the massive  $ \alpha $ grains are formed directly from the single  $ \beta $ phase without passing through the atom partition at the  $ \beta \rightarrow \beta + \alpha $ phase separation. Thus, the Al or Cr content of the lamellar grain in the LED microstructure is lower and higher, respectively, than those of the lamellar region in the HED microstructure. Liu et al. examined the effect of Al content on the lamellar spacing in the TiAl alloys with the fully lamellar structure [55]. They found that the decrease in the Al content is effective in reducing the lamellar spacing. Therefore, the ultrafine structure of the lamellar grain in the LED microstructure, compared with the lamellar region in the HED microstructure can be attributed to the lower Al content. The difference in the chemical composition of these lamellar structures also has a great influence on their mechanical properties.

It is interesting to note that the  $ \alpha_{2}/\beta/\gamma $ mixed structure is observed in area 2 just below area 1 (Fig. 15(c)). In this area, the ultrafine lamellar
Fig. 16. Schematic drawing of phase diagram (vertical section) of Ti–4Al alloys as a function of Cr content (a), time-temperature-transformation (TTT) diagram of 44–4 alloy (b) and illustrations showing evolution of solidification microstructure at the top surface of the 44–4 alloy rods with the LED microstructure (c).

grain is broken and replaced by the  $ \beta $ grain because this area is exposed to high temperatures near the melting point during the fusion of area 1. As in the case of the high ED conditions, the  $ \beta $ grain is separated into the  $ \beta $ and  $ \alpha $ phases due to cooling to and annealing at temperatures corresponding to the  $ \beta + \alpha $ two-phase region, and the subsequent annealing at the lower temperature causes the precipitation of the  $ \gamma $ phase, forming the  $ \alpha_{2}/\beta/\gamma $ mixed structure. On the other hand, the ultrafine lamellar grain is maintained in area 3 because of the reduction of the maximum temperature of the heat effect from the melt pool due to the increase in distance from the top surface (Fig. 15(d)). As schematically shown in Fig. 17(a), this area is mainly heat treated at the temperatures in region III ( $ \beta + \gamma $ two-phase region) indicated in Fig. 16(a), resulting in discontinuous precipitation of the  $ \beta/\gamma $ cell at the grain boundary of the lamellar grain. Note that the increase in ED raises the temperature of the thermal effect from the melt pool and increases the fraction of the  $ \alpha_{2}/\beta/\gamma $ mixed structure (area 2) and decreases the ultrafine  $ \alpha_{2}/\gamma $ lamellar grain with the  $ \beta/\gamma $ cell (area 3) (Fig. 8(a)). As the distance from the surface increases from area 3 to area 4 and beyond, the microstructures observed in areas 2 and 3 are repeated due to the continuous reduction of thermal effect (Fig. 15(e) and (f)). A layered microstructure is formed (Fig. 17(d)) by repeating the microstructural evolution in areas 2 and 3 during the feed and fusion of new powder layers.
Fig. 17. Schematic illustrations showing microstructural evolution and LED microstructure formation in the 44–4 alloy rods during the EBM; (a) fusion top surface, (b) feed a new powder layer, (c) fusion top surface again and (d) fabricated rod with the LED microstructure.

## 4.2. Effect of microstructure on tensile properties at RT

To clarify the key factors for controlling the strength of the alloy, the nanoindentation hardness of the ultrafine  $ \alpha_{2}/\gamma $ lamellar grain in the LED microstructure and the  $ \alpha_{2}/\gamma $ lamellar region along with the  $ \beta $ and  $ \gamma $ phases in the HED microstructure were measured at RT. As shown in Fig. 18, the hardness of the lamellae and the  $ \beta $ phase is higher than that of the  $ \gamma $ phase. Further, the ultrafine lamellar grain in the LED microstructure is much harder than the lamellar region in the HED microstructure. In a lamellar structure in which the  $ \gamma $ and  $ \alpha_{2} $ plates are alternately densely arranged, dislocations generated in the  $ \gamma $ phase require a large stress to pass through the lamellar interface, and the Hall–Petch relationship can be applied between the lamellar spacing and the strength [56]. Therefore, the lamellar grain with narrower lamellar spacing is more difficult to deform than the lamellar region. Additionally, solid solution strengthening due to the high Cr content is likely one of the reasons for the high hardness of the ultrafine lamellar grain. The  $ \beta $ phase with an ordered B_{2} structure also is harder than the coarse lamellar region. These results imply that the fine lamellar grain with high Cr content and the  $ \beta $ phase are the source of the high strength of the 44–4 alloy rods at RT. On the other hand, the soft  $ \gamma $ phase serves as a factor for increasing the ductility of alloys.

In the case of the alloys with the LED microstructure ( $ ED \leq 3 \, J/mm^2 $),  $ V_{\text{all}\beta} $ decreases and  $ V_{\text{all}\alpha2/\gamma} $ and  $ f_{\alpha2/\gamma G} $ increase with decreasing ED (Fig. 8(b) and (d)), resulting in a higher volume fraction of the ultrafine  $ \alpha_2/\gamma $ lamellar grain ( $ V_{\alpha2/\gamma G} $) than that of the  $ \beta $ phase. Fig. 19(a) shows the relationship between  $ V_{\alpha2/\gamma G} $ and  $ \sigma_B $ of the rods fabricated by the low ED conditions. The strength of the alloys fabricated by the low ED conditions depends strongly on  $ V_{\alpha2/\gamma G} $. On the other hand, the lamellar grain disappears in the rods fabricated at the high ED conditions (Fig. 8(a) and (d)), and the  $ \beta $ phase that increases with increasing ED (Fig. 8(b)) becomes the hardest phase in the alloys. Thus,  $ \sigma_B $ of the rods with the HED microstructure increases linearly with increasing  $ V_{\text{all}\beta} $ (Fig. 19(b)). These results indicate that the dominant factor for the RT strength of the alloys is the ultrafine  $ \alpha_2/\gamma $ lamellar grain or the  $ \beta $ phase, whichever exhibits a higher volume fraction.

As shown in Fig. 9(d), the EL of the alloys at RT does not vary as a function of ED. This is because the volume fraction of the  $ \gamma $ phase that is mainly responsible for the plastic deformation is not significantly affected by ED (Fig. 8(b)).

## 4.3. Effect of microstructure on tensile properties at 1023 K
Fig. 18. Nanoindentation hardness of the ultrafine  $ \alpha_{2}/\gamma $ lamellar grain, the  $ \alpha_{2}/\gamma $ lamellar region, the  $ \beta $ phase and the  $ \gamma $ phase in the 44–4 alloy rods fabricated by the EBM.
Fig. 19. Variations in  $ \sigma_{B} $ at RT of the 44–4 alloy rods fabricated by the EBM at low (a) and high (b) ED conditions as a function of  $ V_{\alpha2/\gamma G} $ (a) and  $ V_{\text{all}\beta} $ (b), respectively, and variations in  $ \sigma_{B} $ at 1023 K of the rods as a function of  $ V_{\text{all}\beta} $ (c).

the  $ \beta $ phase during the HT tensile tests. The hexagonal  $ \omega_{0} $ phase with lower crystal symmetry are known as extremely brittle phase at RT due to less possible slip systems but acts as a strong strengthening phase at HT. Thus,  $ \sigma_{B} $ of the alloys at 1023 K basically increases with increasing volume fraction of the  $ \beta $ phase containing the  $ \omega_{0} $ phase (Fig. 19(c)). However, the HT strength does not decrease with decreasing  $ V_{all\beta} $ when the value is approximately 20% or less. These alloys with low  $ V_{all\beta} $ have the LED microstructure with a high amount of the ultrafine  $ \alpha_{2}/\gamma $ lamellar grain ( $ \lambda = 32.5 $ nm, Fig. 7(e)) including high Cr. As shown in Fig. 11(f), not only the  $ \beta $ phase but also the lamellar grain hardly deform at 1023 K. It is considered that the ultrafine lamellar grain keeps high strength at 1023 K due to the solid solution strengthening caused by Cr atoms. In fact, Yan et al. presented that the yield stress of high-Nb-containing TiAl alloys with the fully lamellar structure is approximately 900 MPa at 1023 K [57]. Therefore, it is considered that the increase in the ultrafine lamellar grain prevents the decrease in HT strength of the rods with low  $ V_{all\beta} $.

The alloys demonstrate a high HT ductility of approximately 40%, irrespective of the fabrication conditions (Fig. 10(d)). As shown in Fig. 11(a) and (e), dislocations can be observed in both the  $ \gamma $ phase and the  $ \alpha_{2}/\gamma $ lamellar region which has relatively large lamellar spacing ( $ \lambda = 61.2 $ nm, Fig. 7(c)) and low Cr content after the tensile loading at 1023 K. This result indicates that the strength of the coarse lamellar region without the solid solution strengthening of Cr decreases at 1023 K, and both the  $ \gamma $ phase and the lamellar region exhibit plastic deformation at HT. The softening of these microstructures promotes to a change in the fracture mode from brittle fracture mode to ductile fracture mode (Fig. 9(b), Fig. 10(b)) and induces high ductility. In addition, the fine microstructure of the alloys, which is one of the features of the samples fabricated by the EBM process, also contributes to the large ductility by reducing the stress concentration at the grain boundaries due to fewer piled-up dislocations at grain boundaries.

## 5. Conclusions

The influences of the input energy density on the structural integrity and microstructure of the  $ \beta $-containing 44–4 alloy rods fabricated by the EBM process were investigated. In addition, relationships between the microstructure and tensile properties of the rods were also examined, focusing particularly on the mechanical property, volume fraction and deformation structure of each constituent phase. The following conclusions were drawn from the present study:

## 1. Excessively high ED leads to poor dimensional accuracy of the samples due to an unstable melt pool. However, defects due to insufficient fusion of the powder are formed with ED values of 1.2 J/mm $ ^{2} $ or less.

2. The Ti–44Al–4Cr alloy rods with the uniform  $ \alpha_{2}/\beta/\gamma $ mixed structure consisting of the  $ \alpha_{2}/\gamma $ lamellar and  $ \beta/\gamma $ dual phase regions can be fabricated by the EBM with ED values higher than approximately  $ 3 \, J/mm^{2} $. On the other hand, when the ED is lower than approximately  $ 3 \, J/mm^{2} $, the layered microstructure perpendicular to the building direction, consisting of the ultrafine  $ \alpha_{2}/\gamma $ lamellar grain layer with the  $ \beta/\gamma $ cell structure and the  $ \alpha_{2}/\beta/\gamma $ mixed structure layer can be first obtained.

## 3. The difference in the microstructure originates from the differences in the solidification microstructure and the temperature distribution from the melt pool, which depend on the energy density of the EBM process.

4.  $ \sigma_{B} $ of the Ti–44Al–4Cr alloy rods manufactured by the EBM process reaches 773 MPa and 644 MPa at RT and 1023 K, respectively. Furthermore, the rods exhibit EL of approximately 40% at 1023 K. The high temperature tensile properties of the alloys are better than those of cast 48–2-2 and TNM alloys.

5. The  $ \beta $ phase and ultrafine  $ \alpha_{2}/\gamma $ lamellar grain with high Cr, which originated from the massive  $ \alpha $ grains formed by rapid cooling under low ED conditions, are factors determining the strength of the alloys at both RT and 1023 K. The large ductility of the alloys at 1023 K is attributed to the fine microstructure and the change in the fracture mode from brittle fracture mode to ductile fracture mode due to softening of the  $ \gamma $ phase and the  $ \alpha_{2}/\gamma $ lamellar region with low Cr.

## CRediT Authorship

Ken Cho: Conceptualization, Formal analysis, Methodology, Validation, Visualization, Data curation, Writing - original draft, Writing - review & editing. Hajime Kawabata: Formal analysis, Investigation, Validation. Tatsuhiro Hayashi: Formal analysis, Investigation, Validation. Hiroyuki Y. Yasuda: Conceptualization, Methodology, Writing - review & editing, Supervision, Project administration. Hiroto Nakashima: Formal analysis, Writing - review & editing. Masao Takeyama: Conceptualization, Methodology, Writing - review & editing, Project administration. Takayoshi Nakano: Conceptualization, Writing - review & editing, Project administration.

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Declaration of Competing Interest

## Acknowledgements

This study was supported by the Council for Science, Technology and Innovation (CSTI), Cross-ministerial Strategic Innovation Promotion Program (SIP), “Materials integration for revolutionary design system of structural materials”, Japan.

## References

[1] Y.W. Kim, Ordered intermetallic alloys, part III: gamma titanium aluminides, JOM 46 (1994) 30–39, https://doi.org/10.1007/BF03220745.

[2] P. Bartolotta, J. Barrett, T. Kelly, R. Smashey, The use of cast Ti—48Al—2Cr—2Nb in jet engines, JOM 49 (1997) 48–50, https://doi.org/10.1007/BF02914685.

[3] J. Aguilar, A. Schievenbusch, O. Kättlitz, Investment casting technology for production of TiAl low pressure turbine blades – Process engineering and parameter analysis, intermetallics 19 (2011) 757–761, https://doi.org/10.1016/j.intermet.2010.11.014.

[4] B.P. Bewlay, S. Nag, A. Suzuki, M.J. Weimer, TiAl alloys in commercial aircraft engines, Mater. High. Temp. 33 (2016) 549–559, https://doi.org/10.1080/09603409.2016.1183068.

[5] M. Takeyama, S. Kobayashi, Physical metallurgy for wrought gamma titanium aluminides: microstructure control through phase transformations, Intermetallics 13 (2005) 993–999, https://doi.org/10.1016/j.intermet.2004.12.014.

[6] T. Tetsui, K. Shindo, S. Kobayashi, M. Takeyama, A newly developed hot worked TiAl alloy for blades and structural components, Scr. Mater. 47 (2002) 399–403, https://doi.org/10.1016/S_{1359}-6462(02)00158-6.

[7] A. Shaaban, H. Wakabayashi, H. Nakashima, M. Takeyama, Phase equilibria among  $ \beta/\alpha/\alpha_{2}/\gamma $ phases and phase transformations in Ti–Al–Cr system at elevated temperatures, Process. Manuf. 4 (2019) 1471–1476, https://doi.org/10.1557/adv.2019.111.

[8] H. Clemens, W. Wallgram, S. Kremmer, V. Güther, A. Otto, A. Bartels, Design of novel  $ \beta $-solidifying TiAl alloys with adjustable  $ \beta/B_{2} $-phase fraction and excellent hot-workability, Adv. Eng. Mater. 10 (2008) 707–713, https://doi.org/10.1002/adem.200800164.

[9] M.T. Jovanović, B. Dimčić, I. Bobić, S. Zec, V. Maksimović, Microstructure and mechanical properties of precision cast TiAl turbocharger wheel, J. Mater. Process. Technol. 167 (2005) 14–21, https://doi.org/10.1016/j.jmatprotec.2005.03.019.

[10] M. Yamaguchi, High temperature intermetallics – with particular emphasis on TiAl, Mater. Sci. Technol. 8 (1992) 299–307, https://doi.org/10.1179/mst.1992.8.4.299.

[11] C. Renjie, G. Ming, Z. Hu, G. Shengkai, Interactions between TiAl alloys and yttria refractory material in casting process, J. Mater. Process. Technol. 210 (2010) 1190–1196, https://doi.org/10.1016/j.jmatprotec.2010.03.003.

[12] L. Nickels, AM and aerospace: an ideal combination, Met. Powder Rep. 70 (2015) 300–303, https://doi.org/10.1016/j.mprp.2015.06.005.

[13] T. Nakano, W. Fujitani, T. Ishimoto, J.W. Lee, N. Ikeo, H. Fukuda, K. Kuramoto, Formation of new bone with preferentially oriented biological apatite crystals using a novel cylindrical implant containing anisotropic open pores fabricated by the electron beam melting (EBM) method, ISIJ Int. 51 (2011) 262–268, https://doi.org/10.2355/isijinternational.51.262.

[14] T. Ishimoto, R. Ozasa, K. Nakano, M. Weinmann, C. Schnitter, M. Stenzel, A. Matsugaki, T. Nagasea, T. Matsuzaka, M. Todai, H.S. Kim, T. Nakano, Development of TiNbTaZrMo bio-high entropy alloy (BioHEA) super-solid solution by selective laser melting, and its improved mechanical property and biocompatibility, Scr. Mater. 194 (2021), 113658, https://doi.org/10.1016/j.scriptamat.2020.113658.

[15] N. Hrabe, T. Quinn, Effects of processing on microstructure and mechanical properties of a titanium alloy (Ti-6Al-4V) fabricated using electron beam melting (EBM), part 2: energy input, orientation, and location, Mater. Sci. Eng. A 573 (2013) 271–277, https://doi.org/10.1016/j.msea.2013.02.065.

[16] N. Ikeo, T. Ishimoto, T. Nakano, Novel powder/solid composites possessing low Young's modulus and tunable energy absorption capacity, fabricated by electron beam melting, for biomedical applications, J. Alloy. Compd. 639 (2015) 336–340, https://doi.org/10.1016/j.jallcom.2015.03.141.

[17] S.H. Sun, Y. Koizumi, S. Kurosu, Y.P. Li, H. Matsumoto, A. Chiba, Build direction dependence of microstructure and high-temperature tensile property of Co–Cr–Mo alloy fabricated by electron beam melting, Acta Mater. 64 (2014) 154–168, https://doi.org/10.1016/j.actamat.2013.10.017.

[18] X.P. Tan, P. Wang, Y. Kok, W.Q. Toh, Z. Sun, S.M.L. Nai, M. Descoins, D. Mangelinck, E. Liu, S.B. Tor, Carbide precipitation characteristics in additive manufacturing of Co–Cr–Mo alloy via selective election beam melting, Scr. Mater. 143 (2018) 117–121, https://doi.org/10.1016/j.scriptamat.2017.09.022.

[19] L.E. Murr, E. Martinez, S.M. Gaytan, D.A. Ramirez, B.I. MacHado, P.W. Shindo, J.L. Martinez, F. Medina, J. Wooten, D. Ciscel, U. Ackelid, R.B. Wicker, Microstructural architecture, microstructures, and mechanical properties for a nickel-base superalloy fabricated by electron beam melting, Metall. Mater. Trans. A 42 (2011) 3491–3508, https://doi.org/10.1007/s11661-011-0748-2.

[20] E. Chauvet, P. Kontis, W.A. Jägle, B. Gault, D. Raabe, C. Tassin, J.J. Blandin, R. Dendievel, B. Vayre, S. Abed, G. Martin, Hot cracking mechanism affecting a non-weldable Ni-based superalloy produced by selective electron beam melting, Acta Mater. 142 (2018) 82–94, https://doi.org/10.1016/j.actamat.2017.09.047.

[21] P. Wang, P. Huang, F.L. Ng, W.J. Sin, S. Lu, M.L.S. Nai, Z.L. Dong, J. Wei, Additively manufactured CoCrFeNiMn high-entropy alloy viapre-alloyed powder, Mater. Des. 168 (2019), 107576, https://doi.org/10.1016/j.matdes.2018.107576.

[22] K. Kuwabara, H. Shiratori, T. Fujieda, K. Yamanaka, Y. Koizumi, A. Chiba, Mechanical and corrosion properties of AlCoCrFeNi high-entropy alloy fabricated with selective electron beam melting, Addit. Manuf. 23 (2018) 264–271, https://doi.org/10.1016/j.addma.2018.06.006.

[23] D. Riedlbauer, T. Scharowsky, R.F. Singer, P. Steinmann, C. Körner, J. Mergheim, Macroscopic simulation and experimental measurement of melt pool characteristics in selective electron beam melting of Ti–6Al–4V, Int J. Adv. Manuf. Technol. 88 (2017) 1309–1317, https://doi.org/10.1007/s00170-016-8819-6.

[24] W. Kan, B. Chen, H. Peng, Y. Liang, J. Lin, Formation of columnar lamellar colony grain structure in a high Nb–Ti–Al alloy by electron beam melting, J. Alloy. Compd. 809 (2019), 151673, https://doi.org/10.1016/j.jallcom.2019.151673.

[25] P. Karimia, E. Sadeghi, J. Ålgårdha, J. Andersson, EBM-manufactured single tracks of Alloy 718: influence of energy input and focus offset on geometrical and microstructural characteristics, Mater. Charact. 148 (2019) 88–99, https://doi.org/10.1016/j.matchar.2018.11.033.

[26] J. Schwerdtfeger, C. Körner, Selective electron beam melting of Ti–48Al–2Nb–2Cr: microstructure and aluminium loss, Intermetallics 49 (2014) 29–35, https://doi.org/10.1016/j.intermet.2014.01.004.

[27] L.E. Murr, S.M. Gaytan, A. Ceylan, E. Martinez, J.L. Martinez, D.H. Hernandez, B.I. Machado, D.A. Ramirez, F. Medina, S. Collins, R.B. Wicker, Characterization of titanium aluminide alloy components fabricated by additive manufacturing using electron beam melting, Acta Mater. 58 (2010) 1887–1894, https://doi.org/10.1016/j.actamat.2009.11.032.

[28] A.A. Abdulrahman, A. Mohammad, A. Abdullah, A. Basem, A. Abdulrahman, D. Abdelnaser, Predicting surface quality of  $ \gamma $-TiAl produced by additive manufacturing process using response surface method, J. Mech. Sci. Technol. 30 (2016) 345–352, https://doi.org/10.1007/s12206-015-1239-y.

[29] A. Mohammad, A.M. Alahmari, M.K. Mohammed, R.K. Renganayagalu, K. Moiduddin, Effect of energy input on microstructure and mechanical properties of titanium aluminide alloy fabricated by the additive manufacturing process of electron beam melting, Materials 10 (2017) 211, https://doi.org/10.3390/ma10020211.

[31] H. Yue, Y. Chen, X. Wang, F. Kong, Effect of beam current on microstructure, phase, grain characteristic and mechanical properties of Ti–47Al–2Cr–2Nb alloy fabricated by selective electron beam melting, J. Alloy. Compd. 750 (2018) 617–625, https://doi.org/10.1016/j.jallcom.2018.03.343.

[30] Y. Chen, H. Yue, X. Wang, S. Xiao, F. Kong, X. Cheng, H. Peng, Selective electron beam melting of TiAl alloy: microstructure evolution, phase transformation and microhardness, Mater. Charact. 142 (2018) 584–592, https://doi.org/10.1016/j.matchar.2018.06.027.

[32] Y.K. Kim, S.J. Youn, S.W. Kim, J. Hong, K.A. Lee, High-temperature creep behavior of gamma Ti–48Al–2Cr–2Nb alloy additively manufactured by electron beam melting, Mater. Sci. Eng.: A 763 (2019), 138138, https://doi.org/10.1016/j.msea.2019.138138.

[33] M. Todai, T. Nakano, T. Liu, H.Y. Yasuda, K. Hagihara, K. Cho, M. Ueda, M. Takeyama, Effect of building direction on the microstructure and tensile properties of Ti–48Al–2Cr–2Nb alloy additively manufactured by electron beam melting, Addit. Manuf. 13 (2017) 61–70, https://doi.org/10.1016/j.addma.2016.11.001.

[34] K. Cho, R. Kobayashi, J.Y. Oh, H.Y. Yasuda, M. Todai, T. Nakano, A. Ikeda, M. Ueda, M. Takeyama, Influence of unique layered microstructure on fatigue

properties of Ti–48Al–2Cr–2Nb alloys fabricated by electron beam melting,

Intermetallics 95 (2018) 1–10, https://doi.org/10.1016/j.intermet.2018.01.009.

[35] K. Cho, R. Kobayashi, T. Fukuoka, J.Y. Oh, H.Y. Yasuda, M. Todai, T. Nakano, A. Ikeda, M. Ueda, M. Takeyama, Microstructure and fatigue properties of TiAl with unique layered microstructure fabricated by electron beam melting, Mater. Sci. Forum 941 (2018) 1597–1602.  $ \langle $https://www.scientific.net/MSF.941.1597 $ \rangle $.

[36] M. Sakata, J.Y. Oh, K. Cho, H.Y. Yasuda, M. Todai, T. Nakano, A. Ikeda, M. Ueda, M. Takeyama, Effects of heat treatment on unique layered microstructure and tensile properties of TiAl fabricated by electron beam melting, Mater. Sci. Forum 941 (2018) 1366–1371.  $ \langle $https://www.scientific.net/MSF.941.1366 $ \rangle $.

[37] R. Wartbichler, H. Clemens, S. Mayer, Electron beam melting of a  $ \beta $-solidifying intermetallic titanium aluminide alloy, Adv. Eng. Mater. 21 (2019), 1900800, https://doi.org/10.1002/adem.201900800.

[38] P.L. Narayana, C.L. Li, S.W. Kim, S.E. Kim, A. Marquardt, C. Leyens, N.S. Reddy, J.T. Yeom, J.K. Hong, High strength and ductility of electron beam melted  $ \beta $ stabilized  $ \gamma $-TiAl alloy at 800 ^\circC, Mater. Sci. Eng. A 756 (2019) 41–45, https://doi.org/10.1016/j.msea.2019.03.114.

[39] E. Cox, A method of assigning numerical and percentage values to the degree of roundness of sand grains, J. Paleontol. 1 (1927) 179–183.

[40] Y.Y. Sun, Gulizia, C.H. Oh, C. Doblin, Y.F. Yang, M. Qian, Manipulation and characterization of a novel titanium powder precursor for additive manufacturing applications, JOM 67 (2015) 564–752, https://doi.org/10.1007/s11837-015-1301-3.

[41] S. Biamino, A. Penna, U. Ackelid, S. Sabbadini, O. Tassa, P. Fino, M. Pavese, P. Gennaro, C. Badini, Electron beam melting of Ti–48Al–2Cr–2Nb alloy: Microstructure and mechanical properties investigation, Intermetallics 19 (2011) 776–781, https://doi.org/10.1016/j.intermet.2010.11.017.

[42] Y. Zhao, K. Aoyagi, K. Yamanaka, A. Chiba, Role of operating and environmental conditions in determining molten pool dynamics during electron beam melting and selective laser melting, Addit. Manuf. (2019), 101559, https://doi.org/10.1016/j.addma.2020.101559.

[43] J. Han, J. Dong, S. Zhang, C. Zhang, S. Xiao, Y. Chen, Microstructure evolution and tensile properties of conventional cast TiAl based alloy with trace Ni addition, Mater. Sci. Eng. A 715 (2018) 41–48, https://doi.org/10.1016/j.msea.2017.12.092.

[44] J. Yang, Z. Gao, X. Zhang, R. Hu, Continuous-cooling-transformation (CCT) behaviors and fine-grained nearly lamellar (FGNL) microstructure formation in a cast Ti–48Al–4Nb–2Cr alloy, Metall. Mater. Trans. A 51 (2020) 5285–5295, https://doi.org/10.1007/s11661-020-05934-7.

[45] E. Schwaighofer, H. Clemens, S. Mayer, J. Lindemann, J. Klose, W. Smarsly, V. Güther, Microstructural design and mechanical properties of a cast and heat-treated intermetallic multi-phase  $ \gamma $-TiAl based alloy, Intermetallics 44 (2014) 128–140, https://doi.org/10.1016/j.intermet.2013.09.010.

[46] L.J. Signori, T. Nakamura, Y. Okada, R. Yamagata, H. Nakashima, M. Takeyama, Fatigue crack growth behavior of wrought  $ \gamma $-based TiAl alloy containing  $ \beta $-phase, Intermetallics 100 (2018) 77–87, https://doi.org/10.1016/j.intermet.2018.04.024.

[47] M.A. Morris, Dislocation configurations in two phase TiAl alloys. I. Annealed and indented structures, Philos. Mag. A 68 (1993) 237–257, https://doi.org/10.1080/01418619308221203.

[48] H. Inui, K. Kishida, M. Misaki, M. Kobayashi, Y. Shirai, M. Yamaguchi, Temperature dependence of yield stress, tensile elongation and deformation structures in polysynthetically twinned crystals of Ti–Al, Philos. Mag. A 72 (1995) 1609–1631, https://doi.org/10.1080/01418619508243933.

[49] H.Y. Yasuda, T. Nakano, Y. Umakoshi, The deformation substructure in cyclically deformed TiAl PST crystals, Philos. Mag. A 73 (1996) 1035–1051, https://doi.org/10.1080/01418619608243702.

[50] T. Nakano, H. Biermann, M. Riemer, H. Mughrabi, Y. Nakai, Y. Umakoshi, Classification of  $ \gamma $- $ \gamma $ and  $ \gamma $- $ \alpha_{2} $ lamellar boundaries on the basis of continuity of strains and slip-twinning planes in fatigued TiAl polysynthetically twinned crystals, Philos. Mag. A 81 (2001) 1447–1471, https://doi.org/10.1080/014186100100021618.

[51] M. Schloffer, B. Rashkova, T. Schöberl, E. Schwaighofer, Z. Zhang, H. Clemens, S. Mayer, Evolution of the  $ \omega_{0} $ phase in a  $ \beta $-stabilized multi-phase TiAl alloy and its effect on hardness, Acta Mater. 64 (2014) 241–252, https://doi.org/10.1016/j.actamat.2013.10.036.

[52] X. Wang, J. Yang, K. Zhang, R. Hu, L. Song, H. Fu, Atomic-scale observations of B_{2}\rightarrow\omega-related phases transition in high-Nb containing TiAl alloy, Mater. Charact. 130 (2017) 135–138, https://doi.org/10.1016/j.matchar.2017.06.003.

[53] T.B. Massalski, Massive transformations revisited, Metall. Mater. Trans. A 33 (2002) 2277–2283, https://doi.org/10.1007/s11661-002-0351-7.

[54] M. Kastenhuber, T. Klein, B. Rashkova, I. Weißensteiner, H. Clemens, S. Mayer, Phase transformations in a  $ \beta $-solidifying  $ \gamma $-TiAl based alloy during rapid solidification, Intermetallics 91 (2017) 100–109, https://doi.org/10.1016/j.intermet.2017.08.017.

[55] Z.C. Liu, J.P. Lin, S.J. Li, G.L. Chen, Effects of Nb and Al on the microstructures and mechanical properties of high Nb containing TiAl base alloys, Intermetallics 10 (2002) 653–659, https://doi.org/10.1016/S_{0966}-9795(02)00037-7.

[56] Y. Umakoshi, T. Nakano, The role of ordered domains and slip mode of  $ \alpha_{2} $ phase in the plastic behaviour of TiAl crystals containing oriented lamellae, Acta Metall. Mater. 41 (1993) 1155–1161, https://doi.org/10.1016/0956-7151(93)90163-M.

[57] Y.Q. Yan, Z.Q. Zhang, G.Z. Luo, K.G. Wang, L. Zhou, Microstructures observation and hot compressing tests of TiAl based alloy containing high Nb, Mater. Sci. Eng. A 280 (2000) 187–191, https://doi.org/10.1016/S_{0921}-5093(99)00664-4.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

Additive Manufacturing 46 (2021) 102091

a Division of Materials and Manufacturing Science, Graduate School of Engineering, Osaka University, 2–1 Yamadaoka, Suita, Osaka 565-0871, Japan
b Anisotropic Design & Additive Manufacturing Research Center, Graduate School of Engineering, Osaka University, 2-1 Yamadaoka, Suita, Osaka 565-0871, Japan
c Department of Materials Science and Engineering, School of Materials and Chemical Technology, Tokyo Institute of Technology, 2-12-1 Ookayama, Meguro-ku, Tokyo 152-8552, Japan

## Keywords
Additive manufacturing
Electron beam melting
Titanium aluminide
Microstructure
Tensile properties
## ABSTRACT
## CRediT Authorship

## ABSTRACT

https://doi.org/10.1016/j.addma.2021.102091 2214-8604/© 2021 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/). [6] T. Tetsui, K. Shindo, S. Kobayashi, M. Takeyama, A newly developed hot worked TiAl alloy for blades and structural components, Scr. Mater. 47 (2002) 399–403, https://doi.org/10.1016/S_{1359}-6462(02)00158-6. [8] H. Clemens, W. Wallgram, S. Kremmer, V. Güther, A. Otto, A. Bartels, Design of novel  $ \beta $-solidifying TiAl alloys with adjustable  $ \beta/B_{2} $-phase fraction and excellent hot-workability, Adv. Eng. Mater. 10 (2008) 707–713, https://doi.org/10.1002/adem.200800164. properties of Ti–48Al–2Cr–2Nb alloys fabricated by electron beam melting, Intermetallics 95 (2018) 1–10, https://doi.org/10.1016/j.intermet.2018.01.009. [38] P.L. Narayana, C.L. Li, S.W. Kim, S.E. Kim, A. Marquardt, C. Leyens, N.S. Reddy, J.T. Yeom, J.K. Hong, High strength and ductility of electron beam melted  $ \beta $ stabilized  $ \gamma $-TiAl alloy at 800 ^\circC, Mater. Sci. Eng. A 756 (2019) 41–45, https://doi.org/10.1016/j.msea.2019.03.114. [52] X. Wang, J. Yang, K. Zhang, R. Hu, L. Song, H. Fu, Atomic-scale observations of B_{2}\rightarrow\omega-related phases transition in high-Nb containing TiAl alloy, Mater. Charact. 130 (2017) 135–138, https://doi.org/10.1016/j.matchar.2017.06.003. [55] Z.C. Liu, J.P. Lin, S.J. Li, G.L. Chen, Effects of Nb and Al on the microstructures and mechanical properties of high Nb containing TiAl base alloys, Intermetallics 10 (2002) 653–659, https://doi.org/10.1016/S_{0966}-9795(02)00037-7. [57] Y.Q. Yan, Z.Q. Zhang, G.Z. Luo, K.G. Wang, L. Zhou, Microstructures observation and hot compressing tests of TiAl based alloy containing high Nb, Mater. Sci. Eng. A 280 (2000) 187–191, https://doi.org/10.1016/S_{0921}-5093(99)00664-4.

=== SUPPLEMENTARY OCR LINES (paragraph blocks missing from main text) ===

ELSEVIER

Contents lists available at ScienceDirect

journal homepage: www.elsevier.com/locate/addma

Keywords:
Additive manufacturing
Electron beam melting
Titanium aluminide
Microstructure
Tensile properties

A B S T R A C T

* Corresponding author at: Division of Materials and Manufacturing Science, Graduate School of Engineering, Osaka University, 2-1 Yamadaoka, Suita, Osaka 565-0871, Japan.

E-mail address: hyyasuda@mat.eng.osaka-u.ac.jp (H.Y. Yasuda).

Received 24 November 2020; Received in revised form 23 February 2021; Accepted 30 May 2021

Available online 8 June 2021

K. Cho et al.

CRediT authorship contribution statement

[6] T. Tetsui, K. Shindo, S. Kobayashi, M. Takeyama, A newly developed hot worked TiAl alloy for blades and structural components, Scr. Mater. 47 (2002) 399–403, https://doi.org/10.1016/S1359-6462(02)00158-6.

[8] H. Clemens, W. Wallgram, S. Kremmer, V. Güther, A. Otto, A. Bartels, Design of novel  $ \beta $-solidifying TiAl alloys with adjustable  $ \beta/B2 $-phase fraction and excellent hot-workability, Adv. Eng. Mater. 10 (2008) 707–713, https://doi.org/10.1002/adem.200800164.

properties of Ti–48Al–2Cr–2Nb alloys fabricated by electron beam melting,
Intermetallics 95 (2018) 1–10, https://doi.org/10.1016/j.intermet.2018.01.009.

[38] P.L. Narayana, C.L. Li, S.W. Kim, S.E. Kim, A. Marquardt, C. Leyens, N.S. Reddy, J.T. Yeom, J.K. Hong, High strength and ductility of electron beam melted  $ \beta $ stabilized  $ \gamma $-TiAl alloy at 800 °C, Mater. Sci. Eng. A 756 (2019) 41–45, https://doi.org/10.1016/j.msea.2019.03.114.

[52] X. Wang, J. Yang, K. Zhang, R. Hu, L. Song, H. Fu, Atomic-scale observations of B2→ω-related phases transition in high-Nb containing TiAl alloy, Mater. Charact. 130 (2017) 135–138, https://doi.org/10.1016/j.matchar.2017.06.003.

[55] Z.C. Liu, J.P. Lin, S.J. Li, G.L. Chen, Effects of Nb and Al on the microstructures and mechanical properties of high Nb containing TiAl base alloys, Intermetallics 10 (2002) 653–659, https://doi.org/10.1016/S0966-9795(02)00037-7.

[57] Y.Q. Yan, Z.Q. Zhang, G.Z. Luo, K.G. Wang, L. Zhou, Microstructures observation and hot compressing tests of TiAl based alloy containing high Nb, Mater. Sci. Eng. A 280 (2000) 187–191, https://doi.org/10.1016/S0921-5093(99)00664-4.