v1 = float(input('Digite o valor em metros: ' ))
mm = v1 * 1000
cm = v1 * 100
dm = v1 * 10
dam = v1 * 0.1
hm = v1 * 0.01
km = v1 * 0.001
print('Esse valor equivale a: {:.0f} mm '.format(mm))
print('Esse valor equivale a: {:.0f} cm'.format(cm))
print('Esse valor equivale a: {:.0f} dm'.format(dm))
print('Esse valor equivale a: {:.1f} dam'.format(dam))
print('Esse valor equivale a: {} hm'.format(hm))
print('Esse valor equivale a: {} km'.format(km))

