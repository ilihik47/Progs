global M A W;
M=1; A=0; W=2;
y0=[0,1];
t0=[1:0.005:40];
opts= odeset('RelTol',1e-8,'AbsTol',1e-8);
[t,y]=ode45(@vdp,t0,y0,opts);
figure(1);
plot(y(:,1),y(:,2));
grid on
grid minor
hold on
figure(2);
grid on
grid minor
plot(t,y(:,1));