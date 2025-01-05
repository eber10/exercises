/*Dados los números enteros diferentes X, Y y Z, imprima los números de
forma ascendiente.*/
#include<iostream>
using namespace std;
int main()
{
    int x,y,z;
    cout<<"X: "; cin>>x;
    cout<<"Y: "; cin>>y;
    cout<<"Z: "; cin>>z;
    if(x>y) swap(x,y);
    if(x>z) swap(x,z);
    if(y>z) swap(y,z);
    cout<<x<<" "<<y<<" "<<z;
    return 0;
}
//para python 
/*x=int(input("Ingrese el valor x: "))
y=int(input("Ingrese el valor y: "))
z=int(input("Ingrese el valor z: "))
if x>y:
    x,y=y,x
if x>z:
    x,z=z,x
if y>z:
    y,z=z,y

print(x,y,z)
*/