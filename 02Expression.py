# we can assign two variable at same time
A,B=2,3
Txt="@"
print(A*Txt*B) # yaha par Txt*6 ho jayega means @@@@@@

C,D="2",3
Txt2 = "@"
print((C+Txt2)*D)  # we can add string through + operator and output 2@2@2@

E,F=2,3
G=4
print(E+F*G) #bha gu sa ba vala rule ans=14

H,I=10,5.0
J=H*I
print(J) #answer float aayega ans=50.0

K,L=1,2
M=K/L #simple devision hai
print(M) #yaha par answer float aayega ans=0.5

N,O=1.5,3
P=N//O #devide karne ke baad nearest lowest integer ko print karvayega
print(P , N/O) #ans=0.0 0.5

Q,R=12,5
S=Q//R #nearest lowest integer answer hoga
print(S) # ans = 2

T,U=-12,5
V=T//U #yaha par normal ans -2.4 par uska lowest nearest integer is -3
print(V) #ans=-3

X,Y=12,-5
Z=X//Y #upar vale ki tarah hi hoga 
print(Z) #ans=-3

#modulo or remainder

a,b = -5,2
c=a%b #yaha par remainder yani ki shesh 1 hogi
print(c) #ans=1

d,e=5,2
f=d%e #yaha par bhi remainder 1 hi hoga
print(f) #ans=1

g,h=5,-2
i=g%h #haya par jisse divide ho raha hai vo negative hai so answer mai bhi negative aayega
print(i) #ans=-1