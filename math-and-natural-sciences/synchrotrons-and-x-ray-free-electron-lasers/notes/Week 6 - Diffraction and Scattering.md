# Synchrotrons and X-Ray Free Electron Lasers
# Week 6: Diffraction and Scattering

## What is XRD and why is it used?

Using XRD it's possible to access the atomic structure of chemical systems. For example, the discover of DNA double-helix structure (Nobel Prize to Watson and Crick).

It's **not possible** to build X-Ray lens and it's used the x-ray scattering in a area detector to obtain image data. We send this scattered signal to a computer which then performs the operation of the lens using mathematical algorithms with Fourier transformations. This is called **phasing** the signal, as the detector measures not the signal amplitude but the intensity.

| <img src="images/xrd-imaging.png" width="500"> |
|:--:|
| *Representation of X-Ray Scattering using Area Detector to obtain images.* |

## Diffraction and Scattering at Synchrotrons

Main reason to profit is the **High Brilliance**, which can be separated as:

- Low Divergence
  - High angular resolution scattering
  - Diffraction patterns
- Tight Focus
  - Small sample sizes (protein crystals have <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/8a85b02d1a89030681c0f4fa1ebd802e.svg?invert_in_darkmode" align=middle width=32.55723404999999pt height=21.18721440000001pt/>)
- Low Emittance
  - Large working distance
  - Bulky sample environments
- High Flux
  - Fast data acquisition turns possible time-resolved studies

| <img src="images/scattering-energy.png" width="500"> |
|:--:|
| *Effects of photon energy in the scattering.* |

Access high photon energies turns possible to penetrate deep in the samples and get bulk properties.

A **unique property** of synchrotron light is its **tunability**.

As the scattering amplitude and phase of a certain atom type changes abruptly close to an absorption edge of that atom, that is, at an energy equating the binding energy of one of the core electrons. By recording diffraction data in this region, techniques such as multi-wavelength anomalous diffraction (MAD) and single-wavelength anomalous diffraction (SAD), can unambiguously solve
the phase problem.

- **MAD**: exploits the tunability are only possible at synchrotrons and XFELs;
- **SAD**: uses a single wavelength, can in principle be carried out using a lab source;

### Diffraction patterns and Reciprocal Space

The larger the separation between the scatterers, the smaller their angular separation, or separation in reciprocal space, and vice versa.

| <img src="images/diffraction-patterns.png" width="500"> |
|:--:|
| *Examples of diffraction patterns.* |

The scattering vector <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/1afcdb0f704394b16fe85fb40c45ca7a.svg?invert_in_darkmode" align=middle width=12.99542474999999pt height=22.465723500000017pt/> was defined previously as the difference between the incoming and scattered wavelengths:
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/cfe7545edfe9546042b0eb9ca7e3cf73.svg?invert_in_darkmode" align=middle width=173.05325399999998pt height=32.990165999999995pt/></p>
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/0bdb3a2e1c8afa7e40f4b321bdc61e23.svg?invert_in_darkmode" align=middle width=208.383615pt height=19.68035685pt/></p>

In terms of Miller indexes <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/cf245bbc0025a0f27025e0bf6a8cad9f.svg?invert_in_darkmode" align=middle width=23.77482854999999pt height=22.831056599999986pt/> (crystal surface structure):
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/d4c68555d1314aeffd1b396c3ebc8509.svg?invert_in_darkmode" align=middle width=74.58177705pt height=35.45589465pt/></p>

| <img src="images/ewald-sphere.png" width="500"> |
|:--:|
| *Ewald Sphere.* |

The **Ewald sphere** is applied to **reconstruct** the crystalline structure.

In the figure, the incident beam points in the (000) direction, whereas the scattered beam, if at a Bragg peak defined by the Miller indices (<img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/cf245bbc0025a0f27025e0bf6a8cad9f.svg?invert_in_darkmode" align=middle width=23.77482854999999pt height=22.831056599999986pt/>), terminates on that Bragg maximum. The orientation of the crystal that will result in the <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/cf245bbc0025a0f27025e0bf6a8cad9f.svg?invert_in_darkmode" align=middle width=23.77482854999999pt height=22.831056599999986pt/> Bragg peak lighting up is when this point in the diffraction pattern sits on the Ewald sphere.

**Rotating a crystal around an axis** while recording the pattern using an area detector, different Bragg maxima will light up and can be recorded, as shown schematically here. This is the basic approach to most single-crystal diffraction experiments.

## Crystalographic Techniques

### Crystalline Sample Types

| <img src="images/samples-examples.png" width="500"> |
|:--:|
| *Examples of Crystalline Sample Types in order of disorder degree.* |

The nanocrystalline powder structure representes the more **"real"** kind of sample.

### Different Approaches to Single Crystals

#### Laue Method

Although the majority of x-ray diffraction methods use (quasi-)monochromatic x- rays
and a sample which must be rotated in space in order to satisfy the diffraction condition,
it is also possible to record diffraction patterns of stationary single crystals using
a broad spectrum of x-rays.

Consider a diffraction pattern (a regularly spaced set of diffraction maxima),
or Bragg spots, in reciprocal space. If we irradiate the crystal with a quasi-monochromatic x-ray beam, it is unlikely that the crystal will be oriented such that a diffraction spot lies on the surface of the Ewald sphere.

| <img src="images/laue-diffraction.png" width="500"> |
|:--:|
| *Comparison between using a single wavelength and a sort of them.* |

A large subset of all the possible detected diffraction peaks with different wavelengths can be accessed by rotating the crystal and recording the signal frame after frame.

#### Selected Bragg-Peak Method

It's useful to record a subset of the diffraction data. So, it can be used to follow specific Bragg points and observe physical phenomena related to structural changes.

An example might be orbital, charge (i.e., valence), or even spin ordering of electronic states in electronic materials, which increases the crystal periodicity and thereby introduces additional Bragg peaks at nominally non-integral positions in reciprocal space.

In the experiment, the crystal is oriented to light up a certain diffraction peak.

| <img src="images/bragg-peak-method.png" width="500"> |
|:--:|
| *Illustration of the Bragg-Peak Method.* |

With the advent of modern detectors, with readout times in the range of a few milliseconds,
a new approach called fine **phi-slicing** became possible. The exposures were over much narrower angular ranges by an order of magnitude, and the crystal was allowed to rotate continuously, as the dead time between exposures was sufficiently small. A full data set can be recorded in just a few seconds.

Because the angles covered by each exposure are typically smaller than the angular width
of the diffraction signal, the peak shape and position can be accurately determined using fine phi-slicing.

#### Debye-Sherrer Method

For some materials, it may prove to be very difficult or indeed impossible to grow macroscopic crystals of sufficient quality to be investigated using single-crystal diffraction. In such instances, powder diffraction (also called the ‘Debye-Scherrer’ method) is applied.

Powder diffraction not only provides a rapid and nondestructive means to identify the composite parts in multicomponent mixtures or complex system, but is also indispensable in extreme environmental studies, where phase changes are studied as a function of temperature and/or pressure.

Because of the cylindrical symmetry of this method, all the necessary information can
be recorded in a narrow strip of the rings, that is, along one coordinate, <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/f06574dcb619a95e8016371cead80e5a.svg?invert_in_darkmode" align=middle width=16.39273679999999pt height=22.831056599999986pt/>.

| <img src="images/debye-sherrer-rings.png" width="500"> |
|:--:|
| *Illustration of the Debye-Sherrer Method.* |

### Macromolecular Crystallography

Macromolecular Crystallography is a form of single-crystal diffraction which uses the rotation method.

| <img src="images/macromolecules-crystallography.png" width="500"> |
|:--:|
| *Some features of Macromolecular Crystallography.* |

The large unit-cell dimensions also mean that the diffraction spots in MX are separated by much smaller angles and that many more diffraction peaks will lie on the Ewald sphere and thus be detected.

## X-Ray Reflectivity

X-ray reflectivity one measures the specular reflectivity of x-rays as a function of incident angle.

Provides informations about electron-density profiles, surface or interface roughness, film thickness and density, etc.

| <img src="images/reflectivity.png" width="500"> |
|:--:|
| *Representation of X-Ray Reflectivity.* |

The reflectivity amplitude <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/89f2e0d2d24bcf44db73aab8fc03252c.svg?invert_in_darkmode" align=middle width=7.87295519999999pt height=14.15524440000002pt/> is given by the Fresnel equations for reflectivity and transmission, and is obtained the incident (<img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/c745b9b57c145ec5577b82542b2df546.svg?invert_in_darkmode" align=middle width=10.57650494999999pt height=14.15524440000002pt/>) and transmitted (<img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/416094f51a15e9295762f52b33c73615.svg?invert_in_darkmode" align=middle width=14.36645924999999pt height=24.7161288pt/>) angles across the surface:
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/f2478aadff212222a65387db12ae6711.svg?invert_in_darkmode" align=middle width=77.61923895pt height=36.124496099999995pt/></p>

The reflectivity intensity <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/1e438235ef9ec72fc51ac5025516017c.svg?invert_in_darkmode" align=middle width=12.60847334999999pt height=22.465723500000017pt/> is given by:
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/ab4dec0253472336a990f10dfa12cddc.svg?invert_in_darkmode" align=middle width=188.20878449999998pt height=41.3963847pt/></p>

For angles significantly greater than <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/971651e87c9aebb6ec102860c98ae161.svg?invert_in_darkmode" align=middle width=16.390298099999992pt height=14.15524440000002pt/>:
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/e22263d012f70031cc3caf0eca2872a1.svg?invert_in_darkmode" align=middle width=128.9347323pt height=35.77743345pt/></p>

### Surface Roughness

The reflectivity drops off even more rapidly if the x-rays are being reflected off a rough
surface, even for roughnesses of the order of a few Angstroms.

| <img src="images/surface-roughness.png" width="500"> |
|:--:|
| *Effects of Surface Roughness in the Reflectivity.* |

The roughness can be described by a gaussian distribution, so the reflectivity intensity <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/649c8afa862e3f2dbe87261105cc769f.svg?invert_in_darkmode" align=middle width=18.93892274999999pt height=22.465723500000017pt/> is given by:
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/292a66eed492c999f1da96c979b5eb86.svg?invert_in_darkmode" align=middle width=131.43846704999999pt height=21.7480065pt/></p>

### Thin Films

| <img src="images/thin-films.png" width="500"> |
|:--:|
| *Effects of Film Thickness.* |

It is essentially a restatement of Bragg’s law, where we approximate the <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/25bbb9d1d127005d100cb02b004ef24d.svg?invert_in_darkmode" align=middle width=33.49885109999999pt height=21.95701200000001pt/> with <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/c745b9b57c145ec5577b82542b2df546.svg?invert_in_darkmode" align=middle width=10.57650494999999pt height=14.15524440000002pt/> for the shallow angles, and the “d-spacing” is simply the film thickness Delta.

This causes the reflectivity curve to exhibit oscillations known as “Kiessig fringes”. The separation between fringes is simply <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/b5d1eaf0c94aa37a7a498a06d5f29b1a.svg?invert_in_darkmode" align=middle width=39.72617384999999pt height=24.65753399999998pt/>.

### Atomic-Resolution Film-Growth Monitoring

The decrease in reflectivity with surface roughness can be exploited in in-situ XRR
experiments to monitor film growth.

| <img src="images/atomic-resolution-film.png" width="500"> |
|:--:|
| *Representation of Atomic-Resolution Film-Growth process.* |

If the film grows in a layer-for-layer manner (called Frank van der Merwe growth), then the roughness will vary sinusoidally, being maximally rough when each new monolayer is half complete.

## Small-Angle X-Ray Scattering (SAXS)

X-ray scattering from larger objects up to about a micron in size can also provide important structural and dimensional information.

The samples investigated using SAXS need not be crystalline. Scattering occurs, just as it does in x-ray reflectivity, through electron-density variations <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/1d8d47c164a8f41d614e9d51c3fa8e6f.svg?invert_in_darkmode" align=middle width=22.19755559999999pt height=22.465723500000017pt/>, and not from individual atoms, the case in diffraction.

Typical information extracted from SAXS include characteristic shapes and sizes, surface-area to volume ratios, and in special cases, the relationship between two well-defined sizes, such as between the radius and thickness of a circular platelet.

| <img src="images/saxs.png" width="500"> |
|:--:|
| *Representation of SAXS experimental setup.* |

The scattering vector <img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/1afcdb0f704394b16fe85fb40c45ca7a.svg?invert_in_darkmode" align=middle width=12.99542474999999pt height=22.465723500000017pt/> is given by:
<p align="center"><img src="https://raw.githubusercontent.com/carlosevmoura/courses-notes/master/svgs/fe021256be4a1b87579b623e088392a8.svg?invert_in_darkmode" align=middle width=163.7987868pt height=33.81208709999999pt/></p>

## Crystallography in XFELs

It was predicted that crystallites could survive irradiation by XFELs just long enough before exploding. This concept of diffraction before destruction led to the method of serial femtosecond crystallography, in which successive diffraction images of freshly delivered and randomly oriented crystals are recorded.

The delivery method may be through some sort of liquid jet, an aerosol, or on a fixed membrane system. To obtain a complete diffraction pattern with a resolution that allows identification of individual atoms, several hundred thousand or even more partial patterns must be recorded.

| <img src="images/crystallography-xfels.png" width="500"> |
|:--:|
| *Some ideas in Crystallography in XFELs.* |

Single-particle imaging using XFEL radiation was one of the first long-term goals when
funding for XFELs was being sought. It is the coherent cousin to SAXS - the whole mesoscopically-sized particle is irradiated coherently and the scatter pattern is recorded. The major difference here being that each particle is obliterated after each shot.

