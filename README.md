# comparison-of-matrix-solving-methods

As an engineering student, my biggest problem is the time it takes me to solve a system of equations manually during exams, since these are not the point of interest, but a mandatory step to face the real problem.
In my search for a method to speed things up I found three worth mentioning:

-Cramer's rule
It is a theorem of linear algebra that gives the solution of a linear system of equations in terms of determinants. It is named after Gabriel Cramer (1704-1752), who published the rule in his Introduction à l'analyse des lignes courbes algébriques of 1750.
Cramer's rule is of theoretical importance because it gives an explicit expression for the solution of the system. However, for systems of linear equations with more than three equations, its application to solve it is excessively expensive. However, since it is not necessary to pivot matrices, it is more efficient than Gaussian elimination for small matrices, particularly when SIMD operations are used.
With this in mind, I can already assume that it won't be the best method for solving my system, but I'm going to try it anyway to really compare how it performs.

-Gaussian elimination
Named after Carl Friedrich Gauss (1777-1855), it is an algorithm used to transform the matrix of a system of linear equations to a superior triangular matrix, reducing the system to another equivalent with one less unknown than the previous one.
Once the staggered form is obtained, it follows that the last value of the extended part is the result of the last unknown. With this value, the remaining unknowns are calculated upwards.

-Vega method
I have not been able to find official information about this method, so I don't know its real name or original author; and therefore should be used at your discretion. In my opinion I can say that the method has worked correctly for me in the years that I have been applying it.
This method was published on July 23, 2016 on YouTube by Mechatronic Engineer Héctor Manual Vega, professor at the University of San Buenaventura, Colombia.
The method consists, like Gauss's, in a reduction of the original matrix, but making use of the calculation of determinants. It is complex to explain, so let's go to an example.

                      |a11 a12 a13 : A1|       |b11 b12 : B1|                    b11 = a11*a22-a21*a12
                      |a21 a22 a23 : A2|  -->  |b21 b22 : B2|                    b12 = a11*a23-a21*a13
                      |a31 a32 a33 : A3|                                         B2  = a11*A3-a31*A1

The idea now is to compare the steps needed to solve the system of equations with each of the methods, also taking into account the traditional way. For this I will use a system of six equations with six unknowns, since it is a fairly common system in my day to day.

Once the resolutions are done, I obtain the following data:
-traditional way:         114 min
-Cramer's rule:           2086 min  (estimated value from partial resolution)
-Gaussian elimination:    72 min
-Vega method:             48 min

Already with the results, I was very surprised to see how slow Cramer's rule becomes for matrices larger than 3x3, it was much more than I expected, so I abandoned the resolution when I had approximately 1/6 of the resolution of the first determinant, with 52 minutes and being 7 determinants in total.
In the traditional way it was what was expected, I solved the exercise in 114min, it was a long and tedious process, where you have to be careful not to confuse any value and sign.
With the Gauss method, you save a lot of time, it is easy to carry out without getting lost and it does not generate much error (around 0.4%).
Finally, the Vega method. By far my favorite on the list, it has a very fast resolution, it is easy to carry out and it introduces practically no error (just under 0.1%).To this is added that during the process equivalent matrices are generated with one degree less per step, giving the possibility of using the resolution of equations of a calculator (simple scientific) when arriving at a 3x3 matrix. This manages to improve the time to 39 minutes and reducing the error to 0.03%.

I leave the files with the resolutions in case you want to see and review the step by step. Along with these there is also a small C program that applies the Vega method in matrices of up to 10x10 showing the step by step until reaching the final result.
