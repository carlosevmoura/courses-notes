# Week 4

**Ideal Monoatomic Gas: qtrans**

* Partition Function of a non-interacting system, _Q_, in terms of individual partition functions, _q_:

![Screen Shot 2015-02-19 at 17.19.15.png](image/Screen Shot 2015-02-19 at 17.19.15.png)

* To apply to an ideal gas:
*
* The molecules are indistinguishable
* The number of states greatly exceeds the number of molecules (low pressure)

* The atomic partition function is the product of the partition functions from each degree of freedom:

![Screen Shot 2015-02-19 at 17.24.44.png](image/Screen Shot 2015-02-19 at 17.24.44.png)

* Translation component of Partition Function, qtrans:
*
* Using the results of quantum particle in a box and assuming the same quantum number for each dimension:

![Screen Shot 2015-02-19 at 17.32.12.png](image/Screen Shot 2015-02-19 at 17.32.12.png)

*
* There’s no simply solution to this sum. Then, since translational energy levels are spaced very densely, we can approximate the sum as a integral:

![Screen Shot 2015-02-19 at 17.37.07.png](image/Screen Shot 2015-02-19 at 17.37.07.png)

*
*  Approximating the partition function to a gaussian function, to simplify the integral:

![Screen Shot 2015-02-19 at 17.44.55.png](image/Screen Shot 2015-02-19 at 17.44.55.png)

*
* Summing, we will have:
![Screen Shot 2015-02-19 at 17.48.27.png](image/Screen Shot 2015-02-19 at 17.48.27.png)

**Ideal Monoatomic Gas: Q**

* Now, we focus in electronic contribution of partition function, qelec:
![Screen Shot 2015-02-19 at 18.02.18.png](image/Screen Shot 2015-02-19 at 18.02.18.png)

* Setting the arbitrary value to ground state (ε1) as zero:

![Screen Shot 2015-02-19 at 18.04.22.png](image/Screen Shot 2015-02-19 at 18.04.22.png)

* Note that this series is a rapidly convergent sum, which terms are getting small rapidly, since electronic energy levels are spaced far apart.  Then, we only need to consider the first one or two terms in the series.

![Screen Shot 2015-02-19 at 18.18.14.png](image/Screen Shot 2015-02-19 at 18.18.14.png)

* In general, electronic partition functions are the simplest partition functions. However, one should always keep in mind that for very high temperatures (like on the sun), or smaller values of εj (like in metals), additional terms may contribute.

* So, the Partition Function to an Ideal Monoatomic Gas:

![Screen Shot 2015-02-19 at 18.26.04.png](image/Screen Shot 2015-02-19 at 18.26.04.png)

**Ideal Monoatomic Gas: Properties**

* Ideal Monoatomic Gas Internal Energy, _U_:

![Screen Shot 2015-02-19 at 18.45.59.png](image/Screen Shot 2015-02-19 at 18.45.59.png)

*
* qelec generally has small values (low temperatures):

![Screen Shot 2015-02-19 at 18.47.22.png](image/Screen Shot 2015-02-19 at 18.47.22.png)

* Ideal Monoatomic Gas Heat Capacity, _Cv_:

![Screen Shot 2015-02-19 at 18.53.23.png](image/Screen Shot 2015-02-19 at 18.53.23.png)

* Ideal Monoatomic Gas Pressure, _P_:

![Screen Shot 2015-02-19 at 18.59.35.png](image/Screen Shot 2015-02-19 at 18.59.35.png)

*
* This result recovers Ideal Gases Law:
![Screen Shot 2015-02-19 at 18.59.47.png](image/Screen Shot 2015-02-19 at 18.59.47.png)

---

**Ideal Diatomic Gas**

* Energy expression of an Ideal Diatomic Gas:

![Screen Shot 2015-02-19 at 22.24.40.png](image/Screen Shot 2015-02-19 at 22.24.40.png)

* Components of **Partition Function**:

![Screen Shot 2015-02-19 at 22.27.46.png](image/Screen Shot 2015-02-19 at 22.27.46.png)

* **Translational partition function**, qtrains, is the same as in the monoatomic gas case

* **Electronic partition function**, qelec, we take the zero of energy to be the infinitely separated atoms in their ground electronic states

![Screen Shot 2015-02-19 at 22.39.30.png](image/Screen Shot 2015-02-19 at 22.39.30.png)

* **Vibrational partition function**, qvib:

![Screen Shot 2015-02-19 at 22.47.32.png](image/Screen Shot 2015-02-19 at 22.47.32.png)

*
* Vibrational Temperature:

![Screen Shot 2015-02-19 at 22.57.05.png](image/Screen Shot 2015-02-19 at 22.57.05.png)

*
* So, we can rewrite qvib as:
![Screen Shot 2015-02-19 at 23.03.09.png](image/Screen Shot 2015-02-19 at 23.03.09.png)

*
* We can calculate the vibrational contribution to the average energy and molar heat capacity:

![Screen Shot 2015-02-19 at 23.08.08.png](image/Screen Shot 2015-02-19 at 23.08.08.png)

![Screen Shot 2015-02-19 at 23.08.16.png](image/Screen Shot 2015-02-19 at 23.08.16.png)

*
* Relations between vibration and accessible states:

![Screen Shot 2015-02-19 at 23.28.49.png](image/Screen Shot 2015-02-19 at 23.28.49.png)

* **Rotational partition function**, qrot:

![Screen Shot 2015-02-19 at 23.41.04.png](image/Screen Shot 2015-02-19 at 23.41.04.png)

*
* Rotational temperature:
![Screen Shot 2015-02-19 at 23.42.02.png](image/Screen Shot 2015-02-19 at 23.42.02.png)

*
* Rewriting:
![Screen Shot 2015-02-19 at 23.42.52.png](image/Screen Shot 2015-02-19 at 23.42.52.png)

*
* As for translational partition function, if the energy levels are sufficiently closely spaced (rotational temperature smaller than temperature), we can replace the sum by an integral:

![Screen Shot 2015-02-19 at 23.47.41.png](image/Screen Shot 2015-02-19 at 23.47.41.png)

*
* Then:
![Screen Shot 2015-02-20 at 00.01.20.png](image/Screen Shot 2015-02-20 at 00.01.20.png)

*
* Some properties:

![Screen Shot 2015-02-20 at 00.05.10.png](image/Screen Shot 2015-02-20 at 00.05.10.png)

*
* A diatomic has 2 degrees of rotational freedom, each contributes R/2 to CV

* Occupation of Rotational States:
![Screen Shot 2015-02-20 at 00.11.56 copy.png](image/Screen Shot 2015-02-20 at 00.11.56 copy.png)

**Ideal Diatomic Gas: Partition Function Q**

* Symmetry Number: to differentiate heteronuclear and homonuclear diatomic molecules

![Screen Shot 2015-02-20 at 01.38.15.png](image/Screen Shot 2015-02-20 at 01.38.15.png)

* Full Diatomic Partition Function:

![Screen Shot 2015-02-20 at 01.42.28.png](image/Screen Shot 2015-02-20 at 01.42.28.png)

* Energy and Heat Capacity:

![Screen Shot 2015-02-20 at 01.44.47.png](image/Screen Shot 2015-02-20 at 01.44.47.png)

![Screen Shot 2015-02-20 at 01.45.05.png](image/Screen Shot 2015-02-20 at 01.45.05.png)

*
* The vibrational term is the only one that depends of temperature in heat capacity
* As the temperature of a diatomic ideal gas goes from below to above its vibrational temperature, the molar heat capacity goes from ~(5/2)R to ~(7/2)R

---

**Ideal Polyatomic Gases**

* Translational energy: Also comes from the particle in a box and depends only on the mass of the particle and a chosen volume
* Electronic energy: Assume a ground electronic state but instead of a single De we sum over the dissociation energies of all of the bonds
* Rotational energy: According to the geometry of the molecule
*
* Linear polyatomics: Same as the diatomic rigid rotor
* Nonlinear polyatomics: According to inertia moment

![Screen Shot 2015-02-20 at 16.55.16.png](image/Screen Shot 2015-02-20 at 16.55.16.png)

*
*
* For example, energy expression to spherical top is similar to rigid rotor, changing only the degeneracy

![Screen Shot 2015-02-20 at 16.57.09.png](image/Screen Shot 2015-02-20 at 16.57.09.png)

*
* Applying a treatment similar to diatomic case (approximating the sum to an integral when low rotational temperatures):

![Screen Shot 2015-02-20 at 17.02.00.png](image/Screen Shot 2015-02-20 at 17.02.00.png)

*
* All qrot expressions depends in a power of 3/2 of temperature, so the expressions to energy and heat capacity are the same:

![Screen Shot 2015-02-20 at 17.06.13.png](image/Screen Shot 2015-02-20 at 17.06.13.png)

* Vibrational energy: We divide intramolecular motions into normal modes and express each as an independent harmonic oscillator

![Screen Shot 2015-02-20 at 17.19.19.png](image/Screen Shot 2015-02-20 at 17.19.19.png)

*
* Partition function is the following product:

![Screen Shot 2015-02-20 at 17.20.28.png](image/Screen Shot 2015-02-20 at 17.20.28.png)

*
* And energy and heat capacity is given by sums of individual contribution of each vibration mode:
![Screen Shot 2015-02-20 at 17.21.50.png](image/Screen Shot 2015-02-20 at 17.21.50.png)

* Full polyatomic ideal gas:
![Screen Shot 2015-02-20 at 17.29.18.png](image/Screen Shot 2015-02-20 at 17.29.18.png)
