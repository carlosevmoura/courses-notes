# Synchrotrons and X-Ray Free Electron Lasers
# Week 4: Basics of Machine Physics - Part II

## Important factors of a Light Source

### Flux

The flux associated with an x-ray source is simply the number of photons it emits for a standardized relative spectral bandwidth:
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/965e04d795859658176e69f8dea6f115.svg?invert_in_darkmode" align=middle width=183.2558277pt height=39.452455349999994pt/></p>

Where:

- <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/8b315c12c08fd5b9b3d2a80e5db71bb5.svg?invert_in_darkmode" align=middle width=26.780867849999986pt height=22.465723500000017pt/> is a range of energies around a central energy <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/84df98c65d88c6adf15d4645ffa25e47.svg?invert_in_darkmode" align=middle width=13.08219659999999pt height=22.465723500000017pt/>;

### Brilliance

The brilliance is simply the flux divided by the source size in units of area, and also by the divergence in the two orthogonal planes perpendicular to the beam axis.

<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/85f4f97041ae4fd78946cb6e18a47bd3.svg?invert_in_darkmode" align=middle width=166.40202315pt height=33.81208709999999pt/></p>

### Emittance

The product of the divergence in the two orthogonal planes perpendicular to the beam axis, given in units, that is, **the source size and divergence**, is
known as the emittance.

<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/7478775e6dcb7c5b7ed00dac3fc3e6c8.svg?invert_in_darkmode" align=middle width=104.33427015pt height=19.48126455pt/></p>

| <img src="images/emittance.png" width="450"> |
|:--:|
| *Pictorial representation of emittance in terms of standard deviation.* |

#### Contributions of Electrons and Photons in the emittance

Because the sources are independent of each other, their contributions add orthogonally, as given by the following equations:
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/9cfd29f9a10b5ea72f0113a79529a9fd.svg?invert_in_darkmode" align=middle width=153.56313555pt height=29.58934275pt/></p>
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/d1b2f190345b602ab0fddefe212ebd18.svg?invert_in_darkmode" align=middle width=157.35309314999998pt height=29.58934275pt/></p>

##### Photon emittance

For photons, the standard deviation is given by:
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/60429ebc2fb9457dc8c8194feb6de191.svg?invert_in_darkmode" align=middle width=102.78327345pt height=39.452455349999994pt/></p>
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/03bcbd4e2907c5064cb1ac130b0fb9da.svg?invert_in_darkmode" align=middle width=83.07886785pt height=39.452455349999994pt/></p>

So, the emittance is:
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/c0fca241653c12ce06eeb2fb91fc85b6.svg?invert_in_darkmode" align=middle width=117.2104131pt height=33.81208709999999pt/></p>

Several facilities can now say that the magnet alignment has been so perfectly tuned that the vertical total emittance is essentially equal to the theoretical minimum (given by Heisenberg's principle).

### If a storage ring has a given emittance, how can this be “expressed”?

As the emittance is the product of the source size and divergence, we can either sacrifice source size for a very parallel beam, or vice versa, squeezing the source size to be as small as possible, and accepting a larger divergence.

| <img src="images/source-divergence.png" width="500"> |
|:--:|
| *Small source or small divergence?* |

A large beta function <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/8217ed3c32a785f0b5aad4055f432ad8.svg?invert_in_darkmode" align=middle width=10.16555099999999pt height=22.831056599999986pt/> corresponds to a large source emitting parallel radiation, while as small beta describes a small but divergent source:

<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/b5987cb5da7f62e53244155332407283.svg?invert_in_darkmode" align=middle width=115.17905189999999pt height=19.48126455pt/></p>

For example, along the parts of the ring which contain the straights (to accommodate insertion devices), the beta functions are minimised in order to bring the electrons exactly to the centre of the insertion devices for optimal operation.

### Typical Values in a third-generator light source

- Undulator @ <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/a7b9643119abd196cee618898ec3daeb.svg?invert_in_darkmode" align=middle width=20.61653714999999pt height=27.91243950000002pt/> generation
- Flux <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/c247a6c33e4ee7c5619bcda0173d976d.svg?invert_in_darkmode" align=middle width=152.37481874999997pt height=26.76175259999998pt/>
- Horizontal <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/92480d08df94e35729e5c902a8b31ee9.svg?invert_in_darkmode" align=middle width=126.40972244999999pt height=22.831056599999986pt/>
- Vertical <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/bfa3a11a7137e9efd66305722e9c52db.svg?invert_in_darkmode" align=middle width=131.27274764999999pt height=26.76175259999998pt/>
- Brilliance <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/cd2a903340d847b530d991fcb2357af6.svg?invert_in_darkmode" align=middle width=432.7175589pt height=29.534320200000014pt/>

## Coherence

Coherence describes the relative phase relationship between different parts of the x-ray source, or, from a quantum mechanical viewpoint, of the photons.

A source is said to be coherent if **the emitted waves are all in phase** and (by necessity) have the same wavelength.

- Lasers have a very high degree of coherence;
- Synchrotron sources are only partially coherent;
  - “coherent fraction” less than <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/a1915fadccc3db02e00e4bf9ea9fe782.svg?invert_in_darkmode" align=middle width=34.70331479999999pt height=24.65753399999998pt/> for hard x-rays;

In optical techniques (like microscopy), the size of the object that can be measured depends on the degree of coherence;

- X-ray diffraction is concerned with objects of the order of a few Angstroms to a couple of tens of nanometers (the unit cell size);
- In the case of coherent x-ray diffractive imaging of an object of characteristic dimensions measured in microns, we must take careful measures to ensure the beam is coherent enough that the scattered signal (called “speckle”) contains the required information to regain the sample’s structure;

### Types of Coherence

The coherent volume is spanned by two transverse and one longitudinal coherence length, resulting in a coherent volume.

- The transverse coherence lengths are determined by the divergence of the beam;
- The longitudinal value depends on the monochromacity of the beam;

#### Longitudinal Coherence Length

The longitudinal coherence length is defined as the length required for parts of the beam with different wavelengths (or energies) that begin in phase to be entirely out of phase and then in phase once more.

| <img src="images/longitudinal-coherence.png" width="500"> |
|:--:|
| *Longitudinal coherence features.* |

#### Transverse Coherence Length

The transverse coherence length is determined similarly as the lateral distance between parts of the wavefront separated by a phase of <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/5a7b63fcb316fdefe42e319d18ab939a.svg?invert_in_darkmode" align=middle width=18.179315549999988pt height=21.18721440000001pt/>, due to the source divergence.

- The more parallel the beam (small Delta theta), the larger the transverse coherence;

| <img src="images/transverse-coherence.png" width="500"> |
|:--:|
| *Transverse coherence features.* |

Beamlines constructed for scattering experiments of mesoscopically sized objects, such as in SAXS, CXDI, and ptychography, tend to have long source - end-station distances <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/1e438235ef9ec72fc51ac5025516017c.svg?invert_in_darkmode" align=middle width=12.60847334999999pt height=22.465723500000017pt/> and small source sizes <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode" align=middle width=14.06623184999999pt height=22.465723500000017pt/>.

### The impact of imperfect optics

The wavefront can be further scrambled by imperfect optics, such as for specular reflections off an x-ray mirror, caused by that mirror not being perfectly flat. Beamlines exploiting coherence take great care in minimizing it.

### The Coeherent Fraction of a Light Source

The coherent fraction as a function of the electrons' and photons' source
sizes and divergences is given by:

<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/d4ab4d68100e46e719523c398ed62c3d.svg?invert_in_darkmode" align=middle width=525.2374478999999pt height=53.88180104999999pt/></p>

- In third generation light sources, the coherent fractions of the order of <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/7478f3ddcc5c4a0d602772a3057efe42.svg?invert_in_darkmode" align=middle width=33.26498669999999pt height=26.76175259999998pt/> or less are typical;

- Next-generation storage rings, DLSRs, promise to make a quantum leap in this direction, obtaining coherent fractions of a few percent, that is almost two orders of magnitude greater than presently possible;

- In the case of XFELs, the electron emittance is significantly smaller than the photon emittance, and coherent fractions close to unity are achieved;

---

## Magnetic Lattice

The **magnetic lattice** is responsible for keeping the electron beam on a closed orbit, including focusing it and chromatically correcting for electrons of slightly different kinetic energies.

| <img src="images/magnetic-lattices.png" width="500"> |
|:--:|
| *Examples of Magnetic Lattices in different generations of Light Sources.* |

Typically, bending magnets come in pairs in a given arc-section of the storage ring. At third-generation facilities, they comes in triplets. In DLSRs, they come in clusters of five, seven or even nine in an arc section of the ring.

The Focusing Quadrupole Magnet (FQM) acts to reduce the energy losses by electron spreads in bending magnets.

| <img src="images/double-bend-achromats.png" width="500"> |
|:--:|
| *Double-bending achromats system.* |

The magnet lattice design and its optimization therefore largely determine the horizontal emittance of the facility.

### Quadrupoles

Quadrupoles are the central element in bending magnets.

Deviations in the electrons’ position up or down from the central plane will cause them to **experience a restoring force** to the centre (refocussed).

| <img src="images/quadrupoles.png" width="400"> |
|:--:|
| *Representation of electromagnetic fields in a Focusing quadrupole magnet (FQM).* |

By the correct placement of a FQM (F-4) and a DQM (D-4) after each other, the electron beam can be **focussed both vertically and horizontally**, though at different positions along the central axis, according to the electrons’ energy.

This longitudinal dispersion can be subsequently **chromatically corrected using sextupole magnets**, which have focal lengths that are inversely proportional to the distance of the electrons from the central axis.

| <img src="images/sextupoles.png" width="600"> |
|:--:|
| *Representation of the FQM and DQM combination and the sextupole system.* |

## Insertion devices

Insertion devices are sources of synchrotron radiation consisting of arrays of alternating N-S, S-N dipoles placed at the straight sections of the storage rings.

There are two sorts of insertion devices: the **wiggler** and the **undulator**.

| <img src="images/insertion-devices.png" width="500"> |
|:--:|
| *Examples of Insertion Devices.* |

The parameter that best distinguishes undulators from wigglers is the so-called <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/d6328eaebbcd5c358f426dbea4bdbf70.svg?invert_in_darkmode" align=middle width=15.13700594999999pt height=22.465723500000017pt/> parameter. This expresses the ratio between the maximum angular excursion of the electrons due to the magnet array, <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/ab790c9d998db250161677b4a1a65b34.svg?invert_in_darkmode" align=middle width=36.044149349999984pt height=22.831056599999986pt/>, to the natural opening angle of the synchrotron radiation, <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/7add4c9887c7af67f05998f047cbe90b.svg?invert_in_darkmode" align=middle width=25.862299649999994pt height=24.65753399999998pt/>:
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/008808d8766d324bf70e2fd876bb3d13.svg?invert_in_darkmode" align=middle width=323.88163499999996pt height=38.332593749999994pt/></p>

- For **wigglers**:
  - <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/ca8d30c0e6a8ff424c99455559dce15e.svg?invert_in_darkmode" align=middle width=130.73250794999998pt height=22.831056599999986pt/>
  - <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/5108b59e1eed4c4f00ab1e31c5ebf072.svg?invert_in_darkmode" align=middle width=90.02266019999998pt height=22.465723500000017pt/>
- For **undulators**:
  - <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/0c9081de8d428ad6e01a90b067c71952.svg?invert_in_darkmode" align=middle width=128.68536285pt height=22.831056599999986pt/>
  - <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/053c70555775e3610dd28f7803f2cb84.svg?invert_in_darkmode" align=middle width=86.36967404999999pt height=22.465723500000017pt/>

### Wigglers

The spectral features of wigglers are essentially the same as from a bending magnet:

  - The spectra are broadband, although the flux is larger because of the 2N poles;

**Thermal management** of this is therefore **critical** in order to avoid optical elements downstream of the wiggler at the beamline being destroyed.

### Undulators

Undulators have a very different spectra when comparing with wigglers.

| <img src="images/undulators.png" width="500"> |
|:--:|
| *Comparison between the spectra of undulators and wigglers.* |

The reduction in <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/d6328eaebbcd5c358f426dbea4bdbf70.svg?invert_in_darkmode" align=middle width=15.13700594999999pt height=22.465723500000017pt/> means that the emission lobes with natural opening angle <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/0948db5ccdbf37485c04a96b2947fe1a.svg?invert_in_darkmode" align=middle width=66.95813354999999pt height=24.65753399999998pt/> will now overlap. This overlap means that they interfere with one another, and consequently **only certain wavelengths will interfere constructively**.

The condition to obtain this constructive interference is given by:
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/16b033608f2a7e122147bccc81f68632.svg?invert_in_darkmode" align=middle width=378.24809055pt height=40.11819404999999pt/></p>

<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/7fa32f88e75c9ff96d9b58af5a05b99b.svg?invert_in_darkmode" align=middle width=260.04663135pt height=39.887022449999996pt/></p>

We therefore need only to adjust the **gap size** so that the spectrum contracts along the energy axis until a spectral maximum lies at our energy (or wavelength) of interest.

Undulators are therefore tuned by varying the gap between the poles of the magnet array.

| <img src="images/undulator-turnings.png" width="500"> |
|:--:|
| *Variation of photon energy when changing the gap size of undulators.* |

The spectrally integrated power from undulators is much less than that from wigglers, by an order of magnitude, while their peak intensities are generally significantly higher.

Undulators are, at about <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/6784e1fd68d75a57b35bd36247a1aefe.svg?invert_in_darkmode" align=middle width=33.26498669999999pt height=26.76175259999998pt/>, therefore approximately 100 times more efficient than wigglers and pose a **less severe problem with thermal management**, though this can still be significant if one considers that the beam divergence is much smaller, hence the areal power density on the first optical elements before monochromatization can be higher.

The brilliance of undulators is approximately <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/ea725bd25efe81eaa72385d2f2075926.svg?invert_in_darkmode" align=middle width=285.78284130000003pt height=26.76175259999998pt/>, three orders of magnitude larger than for wigglers.

#### APPLE Undulators

The polarisation of the light produced by undulators can be adjusted so that any desired polarisation can be achieved regarding both its angle around the emission axis and its degree of ellipticity, between linear and fully circular. This is achieved using a so-called Advanced Planar Polarized Light Emmiter: **APPLE undulator**.

---

## Diffraction-Limited Storage Rings (DLSRs)

Diffraction-limited storage rings represent the **next refinement in synchrotron performance**, the “fourth generation” facilities.

- It is a significant improvement in the horizontal emittance;

A cursory glance at the equation describing the horizontal emittance of DBAs should provide a clue as to how we might achieve this:
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/97310209ae7c996edac49244950ee313.svg?invert_in_darkmode" align=middle width=145.1362308pt height=20.50407645pt/></p>

**Solution**: Reduce <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/27e556cf3caa0673ac49a8f0de3c73ca.svg?invert_in_darkmode" align=middle width=8.17352744999999pt height=22.831056599999986pt/> and use more BMs!

- Miniaturization possible due to:
  - Computer numerical control of machining;
  - Improved vacuum technology (NEGs);

### Advantages of DLSRs

- Low emittance:
  - <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/58aad910df6f6cc24d0356fda07e4b99.svg?invert_in_darkmode" align=middle width=23.755726499999987pt height=24.7161288pt/> improves by 1-2 orders of magnitude;
  - Small source size <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/8cda31ed38c6d59d14ebefa440099572.svg?invert_in_darkmode" align=middle width=9.98290094999999pt height=14.15524440000002pt/>:
    - Good for scanning techniques (STXM, scanning XAS, XRF);
- Low divergence:
  - Good coherence for XPCS and ptychography;
  - Reduced optics size for horizontal focussing;
- Combination:
  - Large working distance for given focal spot size;
  - Focus on sample and detector;

## X-Ray Free-Electron Lasers

XFELs are defined by **their exceedingly high peak brilliance**, some <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/065159456ed4c790e33155c119a0726f.svg?invert_in_darkmode" align=middle width=22.990966349999994pt height=26.76175259999998pt/> or even <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/c2782f8129873d99a5fcdfe43ef0e1dc.svg?invert_in_darkmode" align=middle width=32.03208854999999pt height=26.76175259999998pt/> times that achievable using synchrotrons.

The pulse produced by XFELs are **very short**, typically between a femtosecond and <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/68399e6e2d2d99a90a9e8395f7dc1f11.svg?invert_in_darkmode" align=middle width=24.657628049999992pt height=21.18721440000001pt/> fs.

### What is the motivation for the construction of XFELs?

While X-rays provide atomic resolution, synchrotrons has the temporal resolution limited to a few tens of picoseconds. However, many physical and chemical processes occurs on femtoseconds scale.

So, XFELs combine the spatial resolution of x-rays with a temporal resolution down to the fs-scale, previously only possible using lasers in the visible, or near visible regime.

### XFELs vs. Synchrotrons

| <img src="images/xfels-vs-synchrotrons.png" width="650"> |
|:--:|
| *Comparison table between XFELs and Synchrotrons facilities.* |

### XFEL Archtecture: The Low Emittance Gun

Electron bunches are produced by irradiating a semiconductor or metallic surface with a femtosecond laser to produce photoemission.

The timing of this laser pulse is so chosen that the resulting electron cloud is then **accelerated by an RF cavity**, which reduces the impact on the emittance of space-charge effects.

The emittance emerging from this system is of the order of magnitude of <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/71b995974e07ea27c2d9fa9fad13043a.svg?invert_in_darkmode" align=middle width=77.67148949999999pt height=22.831056599999986pt/> in both transverse directions, while the peak current is approximately <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/d3f5403a42b8bd4cacc30c769702a622.svg?invert_in_darkmode" align=middle width=28.76721704999999pt height=22.465723500000017pt/>.

#### SASE Effect

**Bunch compressors** are used to induce SASE, the process responsible for the formation of the high-intensity femtosecond x-ray pulses.

The consequence of these unequal forces in bunch compressors is that the electrons begin to be bunched together to form microbunches, separated by a distance equal to the wavelength of the light they generate and are bathed in. Each microbunch therefore has a duration of a few femtoseconds to a few tens of femtoseconds.

As the microbunches begin to form, the electrons become more squeezed together, resulting in an increase in the instantaneous current. This produces a intenser undulator radiation, which in turn acts more strongly on the electrons, further enhancing the micro bunching process. This runaway effect is called **SASE** - Self-Amplified Spontaneous Emission.

| <img src="images/sase.png" width="500"> |
|:--:|
| *Self-Amplified Spontaneos Emission microbunches.* |

Coherente bunches gives high intensity light (<img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/ac7c181c28eacba4b88a1ebf4a5826f4.svg?invert_in_darkmode" align=middle width=46.895044349999985pt height=26.76175259999998pt/>), while noncoherente bunches gives <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/47f9eb85a2e6c0e6304462348194b255.svg?invert_in_darkmode" align=middle width=40.34249834999999pt height=26.76175259999998pt/>.

The performance of an XFEL is encapsulated in the dimensionless so-called **Pierce parameter**, or XFEL parameter, given by:
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/8fe5afd04d2d19529e82bbc6cdedcaa6.svg?invert_in_darkmode" align=middle width=170.23192065pt height=44.68443705pt/></p>

Although XFELs provide radiation with exceedingly coherent radiation in the transverse direction, due to its unmatched parallelity and small source size, the longitudinal coherence.

