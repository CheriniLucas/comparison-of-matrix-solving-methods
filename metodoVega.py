#Resolucion de matrices python
import os

#ingreso de datos
os.system('clear')
print('\t\t\tResolucion de Matrices Python!\n')
incog = input('Cantidad de incognitas?\t\t')
incognitas = int(incog)

if incognitas > 8:
	print('\nerror, el programa admite solo hasta 8 incognitas\n')
	quit()

os.system('clear')
print('\t\t\tResolucion de Matrices Python!\n')
print('Ingrese los valores de la matriz')

A = []
for i in range(incognitas):
	for j in range(incognitas+1):
		dato = input('%d%d: ' % (i+1, j+1))
		datos = float(dato)
		A.append(datos)
	print('')


#clasificacion
B = []
for i in range(incognitas):
	 B.append(A[i*(incognitas+1):(i+1)*(incognitas+1)])

B1 = B[0]
B2 = B[1]
if incognitas > 2:
	B3 = B[2]
if incognitas > 3:
	B4 = B[3]
if incognitas > 4:
	B5 = B[4]
if incognitas > 5:
	B6 = B[5]
if incognitas > 6:
	B7 = B[6]
if incognitas > 7:
	B8 = B[7]


#metodo vega
X11 = []
for i in range(incognitas):
	mVega1 = B1[0]*B2[i+1]-B2[0]*B1[i+1]
	X11.append(mVega1)

if incognitas > 2:
	X12 = []
	X21 = []
	for i in range(incognitas):
		mVega1 = B1[0]*B3[i+1]-B3[0]*B1[i+1]
		X12.append(mVega1)
	for i in range(incognitas-1):
		mVega2 = X11[0]*X12[i+1]-X12[0]*X11[i+1]
		X21.append(mVega2)

if incognitas > 3:
	X13 = []
	X22 = []
	X31 = []
	for i in range(incognitas):
		mVega1 = B1[0]*B4[i+1]-B4[0]*B1[i+1]
		X13.append(mVega1)
	for i in range(incognitas-1):
		mVega2 = X11[0]*X13[i+1]-X13[0]*X11[i+1]
		X22.append(mVega2)
	for i in range(incognitas-2):
		mVega3 = X21[0]*X22[i+1]-X22[0]*X21[i+1]
		X31.append(mVega3)

if incognitas > 4:
	X14 = []
	X23 = []
	X32 = []
	X41 = []
	for i in range(incognitas):
		mVega1 = B1[0]*B5[i+1]-B5[0]*B1[i+1]
		X14.append(mVega1)
	for i in range(incognitas-1):
		mVega2 = X11[0]*X14[i+1]-X14[0]*X11[i+1]
		X23.append(mVega2)
	for i in range(incognitas-2):
		mVega3 = X21[0]*X23[i+1]-X23[0]*X21[i+1]
		X32.append(mVega3)
	for i in range(incognitas-3):
		mVega4 = X31[0]*X32[i+1]-X32[0]*X31[i+1]
		X41.append(mVega4)

if incognitas > 5:
	X15 = []
	X24 = []
	X33 = []
	X42 = []
	X51 = []
	for i in range(incognitas):
		mVega1 = B1[0]*B6[i+1]-B6[0]*B1[i+1]
		X15.append(mVega1)
	for i in range(incognitas-1):
		mVega2 = X11[0]*X15[i+1]-X15[0]*X11[i+1]
		X24.append(mVega2)
	for i in range(incognitas-2):
		mVega3 = X21[0]*X24[i+1]-X24[0]*X21[i+1]
		X33.append(mVega3)
	for i in range(incognitas-3):
		mVega4 = X31[0]*X33[i+1]-X33[0]*X31[i+1]
		X42.append(mVega4)
	for i in range(incognitas-4):
		mVega5 = X41[0]*X42[i+1]-X42[0]*X41[i+1]
		X51.append(mVega5)

if incognitas > 6:
	X16 = []
	X25 = []
	X34 = []
	X43 = []
	X52 = []
	X61 = []
	for i in range(incognitas):
		mVega1 = B1[0]*B7[i+1]-B7[0]*B1[i+1]
		X16.append(mVega1)
	for i in range(incognitas-1):
		mVega2 = X11[0]*X16[i+1]-X16[0]*X11[i+1]
		X25.append(mVega2)
	for i in range(incognitas-2):
		mVega3 = X21[0]*X25[i+1]-X25[0]*X21[i+1]
		X34.append(mVega3)
	for i in range(incognitas-3):
		mVega4 = X31[0]*X34[i+1]-X34[0]*X31[i+1]
		X43.append(mVega4)
	for i in range(incognitas-4):
		mVega5 = X41[0]*X43[i+1]-X43[0]*X41[i+1]
		X52.append(mVega5)
	for i in range(incognitas-5):
		mVega6 = X51[0]*X52[i+1]-X52[0]*X51[i+1]
		X61.append(mVega6)

if incognitas > 7:
	X17 = []
	X26 = []
	X35 = []
	X44 = []
	X53 = []
	X62 = []
	X71 = []
	for i in range(incognitas):
		mVega1 = B1[0]*B8[i+1]-B8[0]*B1[i+1]
		X17.append(mVega1)
	for i in range(incognitas-1):
		mVega2 = X11[0]*X17[i+1]-X17[0]*X11[i+1]
		X26.append(mVega2)
	for i in range(incognitas-2):
		mVega3 = X21[0]*X26[i+1]-X26[0]*X21[i+1]
		X35.append(mVega3)
	for i in range(incognitas-3):
		mVega4 = X31[0]*X35[i+1]-X35[0]*X31[i+1]
		X44.append(mVega4)
	for i in range(incognitas-4):
		mVega5 = X41[0]*X44[i+1]-X44[0]*X41[i+1]
		X53.append(mVega5)
	for i in range(incognitas-5):
		mVega6 = X51[0]*X53[i+1]-X53[0]*X51[i+1]
		X62.append(mVega6)
	for i in range(incognitas-6):
		mVega7 = X61[0]*X62[i+1]-X62[0]*X61[i+1]
		X71.append(mVega7)


#resolucion
if incognitas == 2:
	X = [0, 0, 0]
	X[2] = (X11[1])/X11[0]
	X[1] = (B1[2]-B1[1]*X[2])/B1[0]

if incognitas == 3:
	X = [0, 0, 0, 0]
	X[3] = (X21[1])/X21[0]
	X[2] = (X11[2]-X11[1]*X[3])/X11[0]
	X[1] = (B1[3]-B1[1]*X[2]-B1[2]*X[3])/B1[0]

if incognitas == 4:
	X = [0, 0, 0, 0, 0]
	X[4] = (X31[1])/X31[0]
	X[3] = (X21[2]-X21[1]*X[4])/X21[0]
	X[2] = (X11[3]-X11[1]*X[3]-X11[2]*X[4])/X11[0]
	X[1] = (B1[4]-B1[1]*X[2]-B1[2]*X[3]-B1[3]*X[4])/B1[0]

if incognitas == 5:
	X = [0, 0, 0, 0, 0, 0]
	X[5] = (X41[1])/X41[0]
	X[4] = (X31[2]-X31[1]*X[5])/X31[0]
	X[3] = (X21[3]-X21[1]*X[4]-X21[2]*X[5])/X21[0]
	X[2] = (X11[4]-X11[1]*X[3]-X11[2]*X[4]-X11[3]*X[5])/X11[0]
	X[1] = (B1[5]-B1[1]*X[2]-B1[2]*X[3]-B1[3]*X[4]-B1[4]*X[5])/B1[0]

if incognitas == 6:
	X = [0, 0, 0, 0, 0, 0, 0]
	X[6] = (X51[1])/X51[0]
	X[5] = (X41[2]-X41[1]*X[6])/X41[0]
	X[4] = (X31[3]-X31[1]*X[5]-X31[2]*X[6])/X31[0]
	X[3] = (X21[4]-X21[1]*X[4]-X21[2]*X[5]-X21[3]*X[6])/X21[0]
	X[2] = (X11[5]-X11[1]*X[3]-X11[2]*X[4]-X11[3]*X[5]-X11[4]*X[6])/X11[0]
	X[1] = (B1[6]-B1[1]*X[2]-B1[2]*X[3]-B1[3]*X[4]-B1[4]*X[5]-B1[5]*X[6])/B1[0]

if incognitas == 7:
	X = [0, 0, 0, 0, 0, 0, 0, 0]
	X[7] = (X61[1])/X61[0]
	X[6] = (X51[2]-X51[1]*X[7])/X51[0]
	X[5] = (X41[3]-X41[1]*X[6]-X41[2]*X[7])/X41[0]
	X[4] = (X31[4]-X31[1]*X[5]-X31[2]*X[6]-X31[3]*X[7])/X31[0]
	X[3] = (X21[5]-X21[1]*X[4]-X21[2]*X[5]-X21[3]*X[6]-X21[4]*X[7])/X21[0]
	X[2] = (X11[6]-X11[1]*X[3]-X11[2]*X[4]-X11[3]*X[5]-X11[4]*X[6]-X11[5]*X[7])/X11[0]
	X[1] = (B1[7]-B1[1]*X[2]-B1[2]*X[3]-B1[3]*X[4]-B1[4]*X[5]-B1[5]*X[6]-B1[6]*X[7])/B1[0]

if incognitas == 8:
	X = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	X[8] = (X71[1])/X71[0]
	X[7] = (X61[2]-X61[1]*X[8])/X61[0]
	X[6] = (X51[3]-X51[1]*X[7]-X51[2]*X[8])/X51[0]
	X[5] = (X41[4]-X41[1]*X[6]-X41[2]*X[7]-X41[3]*X[8])/X41[0]
	X[4] = (X31[5]-X31[1]*X[5]-X31[2]*X[6]-X31[3]*X[7]-X31[4]*X[8])/X31[0]
	X[3] = (X21[6]-X21[1]*X[4]-X21[2]*X[5]-X21[3]*X[6]-X21[4]*X[7]-X21[5]*X[8])/X21[0]
	X[2] = (X11[7]-X11[1]*X[3]-X11[2]*X[4]-X11[3]*X[5]-X11[4]*X[6]-X11[5]*X[7]-X11[6]*X[8])/X11[0]
	X[1] = (B1[8]-B1[1]*X[2]-B1[2]*X[3]-B1[3]*X[4]-B1[4]*X[5]-B1[5]*X[6]-B1[6]*X[7]-B1[7]*X[8])/B1[0]


#muestra de resultados
os.system('clear')
print('\t\t\tResolucion de Matrices Python!\n')

for i in range(incognitas):
	print('\t', A[i*(incognitas+1):(i+1)*(incognitas+1)])
print('\n')

for i in range(incognitas):
	print('\tx%d: %g' % (i+1, X[i+1]))
print('\n')
